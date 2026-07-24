#!/usr/bin/env python3
"""Ingestion (Module 2): extract Google Docs into the vault inbox.

Given Google Doc links or IDs, this fetches each document and writes an
Obsidian-native Markdown note (YAML frontmatter, `#gdoc` source) to
`Inbox/Web_to_Process/`. Docs already written are skipped (idempotent).

Access model (no credentials required for the common case):
  - A doc shared "anyone with the link can view" can be exported directly via
    `https://docs.google.com/document/d/<id>/export?format=html` (or `txt`). This
    is the primary path and needs no auth.
  - A doc "published to the web" (File -> Share -> Publish to web) has a
    `/d/e/<pubid>/pub` URL whose HTML is fetched and reduced to its body.
  - A fully private doc returns a Google sign-in page; this script cannot read it.
    Use the Google Docs API with a service account for that (out of scope here);
    the script reports the doc as inaccessible rather than saving a login page.

Accepted forms:
    https://docs.google.com/document/d/<id>/edit
    https://docs.google.com/document/d/e/<pubid>/pub
    <id>            (bare 25+ char document ID)

Usage:
    python3 scripts/fetch_gdoc.py https://docs.google.com/document/d/<id>/edit
    python3 scripts/fetch_gdoc.py <id> <id2> --outdir "/path/to/Vault/Docs"
    python3 scripts/fetch_gdoc.py --file gdoc_urls.txt

Fetching uses curl with a browser User-Agent (matches the other scripts).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scrape_articles import html_to_markdown, parse_meta  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTDIR_DEFAULT = REPO_ROOT / "Inbox" / "Web_to_Process"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0 Safari/537.36"

_SIGNIN_MARKERS = ("accounts.google.com/ServiceLogin", "Sign in - Google Accounts",
                   "to continue to Google Docs")


def _get(url: str, timeout: int = 40) -> tuple[int, str]:
    cmd = ["curl", "-sSL", "--max-time", str(timeout), "-A", UA, "-w", "\n%{http_code}", url]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
    except Exception:
        return 0, ""
    body, _, code = out.stdout.rpartition("\n")
    try:
        return int(code.strip()), body
    except ValueError:
        return 0, out.stdout


def parse_doc(spec: str) -> tuple[str, str] | None:
    """Return (kind, id) where kind is 'doc' or 'pub', or None if unrecognised."""
    spec = spec.strip()
    m = re.search(r"/document/d/e/([A-Za-z0-9_-]+)", spec)
    if m:
        return "pub", m.group(1)
    m = re.search(r"/document/d/([A-Za-z0-9_-]+)", spec)
    if m:
        return "doc", m.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{25,}", spec):
        return "doc", spec
    return None


def fetch_doc(kind: str, doc_id: str) -> tuple[str, str] | None:
    """Return (title, markdown_body) or None if the doc is inaccessible."""
    if kind == "pub":
        url = f"https://docs.google.com/document/d/e/{doc_id}/pub"
    else:
        url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"
    code, body = _get(url)
    if code != 200 or not body or any(mark in body for mark in _SIGNIN_MARKERS):
        return None
    meta = parse_meta(body)
    md = html_to_markdown(body)
    title = meta.get("title") or ""
    # Google's exported/pub HTML repeats the title as the first heading; prefer that.
    if not title:
        m = re.search(r"(?m)^#\s+(.+)$", md)
        title = m.group(1).strip() if m else f"Google Doc {doc_id[:10]}"
    if len(md) < 20:
        return None
    return title, md


def _yaml_str(v: str) -> str:
    return '"' + v.replace('"', "'") + '"'


def process(spec: str, outdir: Path) -> str:
    parsed = parse_doc(spec)
    if not parsed:
        return f"WARN  could not parse Google Doc id from: {spec!r}"
    kind, doc_id = parsed
    out_path = outdir / f"gdoc--{doc_id[:40]}.md"
    if out_path.exists():
        return f"SKIP  {out_path.name}  (already fetched)"
    result = fetch_doc(kind, doc_id)
    if result is None:
        return (f"FAIL  {doc_id[:16]}...  (inaccessible: not public/published, or "
                f"requires Google sign-in)")
    title, md = result
    src = (f"https://docs.google.com/document/d/e/{doc_id}/pub" if kind == "pub"
           else f"https://docs.google.com/document/d/{doc_id}/edit")
    today = _dt.date.today().isoformat()
    fm = [
        "---",
        f"source_url: {src}",
        f"title: {_yaml_str(title)}",
        f"scraped: {today}",
        "type: gdoc",
        "source: google-docs",
        "---",
        "",
    ]
    # html_to_markdown already leads with the '# title' when present.
    if not re.match(r"(?s)^\s*#\s", md):
        fm += [f"# {title}", ""]
    note = "\n".join(fm) + md.rstrip() + f"\n\n---\nSource: {src}\n"
    out_path.write_text(note, encoding="utf-8")
    return f"OK    {out_path.name}  ({len(md.split())} words)  {title[:60]!r}"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docs", nargs="*", help="Google Doc URLs or IDs")
    ap.add_argument("--file", help="file with one Google Doc URL/ID per line")
    ap.add_argument("--outdir", help=f"output dir (default {OUTDIR_DEFAULT})")
    args = ap.parse_args(argv)

    specs = list(args.docs)
    if args.file:
        specs += [ln.strip() for ln in Path(args.file).read_text().splitlines() if ln.strip()]
    if not specs:
        ap.error("provide one or more Google Doc URLs/IDs or --file")

    outdir = Path(args.outdir).expanduser() if args.outdir else OUTDIR_DEFAULT
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"{len(specs)} doc(s) -> {outdir}\n")
    results = [process(s, outdir) for s in specs]
    for line in results:
        print(line)
    return 1 if any(r.startswith("FAIL") for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
