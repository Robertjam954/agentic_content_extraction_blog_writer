#!/usr/bin/env python3
"""Ingestion (Module 2): fetch papers from Semantic Scholar into the vault inbox.

Given search queries or paper IDs (a Semantic Scholar id, `DOI:...`, `ARXIV:...`, or
`CorpusId:...`), this fetches each paper's metadata, abstract, and TL;DR from the
Semantic Scholar Graph API and writes an Obsidian-ready Markdown note (YAML frontmatter,
author/field wikilinks, `#paper` tag) to `Inbox/Papers_to_Process/`. The notes are
native Obsidian Markdown, so they drop straight into the vault and are picked up by the
RAG index. Papers already written are skipped.

Usage:
    python3 scripts/fetch_semantic_scholar.py --query "retrieval augmented generation" --limit 10
    python3 scripts/fetch_semantic_scholar.py ARXIV:2005.11401 DOI:10.18653/v1/2020.acl-main.1
    python3 scripts/fetch_semantic_scholar.py --file ids.txt --outdir "/path/to/Vault/Papers"

Fetching uses curl (this machine's urllib is broken by TLS interception). The public
API is shared and returns HTTP 429 when busy; set S2_API_KEY for higher rate limits.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTDIR_DEFAULT = REPO_ROOT / "Inbox" / "Papers_to_Process"

API = "https://api.semanticscholar.org/graph/v1"
FIELDS = (
    "title,abstract,tldr,year,venue,authors,externalIds,url,openAccessPdf,"
    "citationCount,referenceCount,publicationTypes,fieldsOfStudy,publicationDate"
)


def _curl(url: str, params: list[tuple[str, str]]) -> tuple[int, str]:
    """GET `url` with urlencoded params via curl. Returns (http_code, body)."""
    cmd = ["curl", "-sS", "--max-time", "40", "-w", "\n%{http_code}", "-G", url]
    for k, v in params:
        cmd += ["--data-urlencode", f"{k}={v}"]
    key = os.getenv("S2_API_KEY")
    if key:
        cmd += ["-H", f"x-api-key: {key}"]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=50)
    body, _, code = out.stdout.rpartition("\n")
    try:
        return int(code.strip()), body
    except ValueError:
        return 0, out.stdout


def _get_json(url: str, params: list[tuple[str, str]], tries: int = 4) -> dict | None:
    """Fetch JSON with backoff on 429/5xx."""
    delay = 3.0
    for attempt in range(tries):
        code, body = _curl(url, params)
        if code == 200:
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                return None
        if code in (429, 500, 502, 503, 504) and attempt < tries - 1:
            print(f"    HTTP {code}; backing off {delay:.0f}s ...")
            time.sleep(delay)
            delay *= 2
            continue
        print(f"    HTTP {code}: {body[:160]}")
        return None
    return None


def search(query: str, limit: int) -> list[dict]:
    data = _get_json(
        f"{API}/paper/search",
        [("query", query), ("limit", str(limit)), ("fields", FIELDS)],
    )
    return (data or {}).get("data", []) if data else []


def fetch_by_id(pid: str) -> dict | None:
    return _get_json(f"{API}/paper/{pid}", [("fields", FIELDS)])


def _slug(paper: dict) -> str:
    ext = paper.get("externalIds") or {}
    if ext.get("ArXiv"):
        base = f"arxiv-{ext['ArXiv']}"
    elif ext.get("DOI"):
        base = "doi-" + ext["DOI"]
    elif paper.get("paperId"):
        base = paper["paperId"]
    else:
        base = re.sub(r"\W+", "-", (paper.get("title") or "paper").lower())[:60]
    return re.sub(r"[^A-Za-z0-9._-]+", "_", base)


def _yaml_list(items: list[str]) -> str:
    return "[" + ", ".join('"' + i.replace('"', "'") + '"' for i in items) + "]"


def note_markdown(paper: dict) -> str:
    ext = paper.get("externalIds") or {}
    authors = [a.get("name", "") for a in (paper.get("authors") or []) if a.get("name")]
    fields = paper.get("fieldsOfStudy") or []
    tldr = (paper.get("tldr") or {}).get("text") or ""
    abstract = paper.get("abstract") or ""
    title = (paper.get("title") or "Untitled").replace('"', "'")
    today = _dt.date.today().isoformat()
    pdf = (paper.get("openAccessPdf") or {}).get("url") or ""

    fm = ["---", f'title: "{title}"', "source: semantic-scholar", "type: paper"]
    if authors:
        fm.append(f"authors: {_yaml_list(authors)}")
    if paper.get("year"):
        fm.append(f"year: {paper['year']}")
    if paper.get("venue"):
        fm.append(f'venue: "{paper["venue"].replace(chr(34), chr(39))}"')
    if ext.get("DOI"):
        fm.append(f"doi: {ext['DOI']}")
    if ext.get("ArXiv"):
        fm.append(f"arxiv: {ext['ArXiv']}")
    if ext.get("CorpusId"):
        fm.append(f"corpus_id: {ext['CorpusId']}")
    if paper.get("citationCount") is not None:
        fm.append(f"citations: {paper['citationCount']}")
    if paper.get("url"):
        fm.append(f"source_url: {paper['url']}")
    if pdf:
        fm.append(f"pdf_url: {pdf}")
    tags = ["paper"] + [re.sub(r"\s+", "-", f.lower()) for f in fields]
    fm.append(f"tags: {_yaml_list(tags)}")
    fm += [f"extracted: {today}", "---", ""]

    body = [f"# {paper.get('title') or 'Untitled'}", ""]
    byline = ", ".join(f"[[{a}]]" for a in authors[:8])
    meta_bits = [b for b in [byline, str(paper.get("year") or ""), paper.get("venue") or ""] if b]
    if meta_bits:
        body += ["> " + " · ".join(meta_bits), ""]
    if tldr:
        body += ["## TL;DR", "", tldr, ""]
    if abstract:
        body += ["## Abstract", "", abstract, ""]

    links = []
    if paper.get("url"):
        links.append(f"- Semantic Scholar: {paper['url']}")
    if ext.get("DOI"):
        links.append(f"- DOI: https://doi.org/{ext['DOI']}")
    if ext.get("ArXiv"):
        links.append(f"- arXiv: https://arxiv.org/abs/{ext['ArXiv']}")
    if pdf:
        links.append(f"- PDF: {pdf}")
    if links:
        body += ["## Links", "", *links, ""]
    if fields:
        body += ["", " ".join(f"[[{f}]]" for f in fields)]
    body.append("")
    return "\n".join(fm) + "\n".join(body).rstrip() + "\n"


def process(paper: dict, outdir: Path) -> str:
    if not paper or not paper.get("title"):
        return "FAIL  (empty paper record)"
    out_path = outdir / f"{_slug(paper)}.md"
    if out_path.exists():
        return f"SKIP  {out_path.name}  (already fetched)"
    out_path.write_text(note_markdown(paper), encoding="utf-8")
    n_auth = len(paper.get("authors") or [])
    return f"OK    {out_path.name}  ({paper.get('year') or '?'}, {n_auth} authors)  {paper['title'][:60]!r}"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ids", nargs="*", help="paper IDs: S2 id, DOI:..., ARXIV:..., CorpusId:...")
    ap.add_argument("--query", help="search query (writes the top --limit results)")
    ap.add_argument("--limit", type=int, default=10, help="max search results (default 10)")
    ap.add_argument("--file", help="file with one paper ID per line")
    ap.add_argument("--outdir", help=f"output dir (default {OUTDIR_DEFAULT})")
    args = ap.parse_args(argv)

    outdir = Path(args.outdir).expanduser() if args.outdir else OUTDIR_DEFAULT
    outdir.mkdir(parents=True, exist_ok=True)

    ids = list(args.ids)
    if args.file:
        ids += [ln.strip() for ln in Path(args.file).read_text().splitlines() if ln.strip()]
    if not ids and not args.query:
        ap.error("provide --query and/or one or more paper IDs")

    papers: list[dict] = []
    if args.query:
        print(f"Searching: {args.query!r} (top {args.limit})")
        papers += search(args.query, args.limit)
    for pid in ids:
        print(f"Fetching: {pid}")
        p = fetch_by_id(pid)
        if p:
            papers.append(p)

    print(f"\n{len(papers)} paper(s) -> {outdir}\n")
    results = [process(p, outdir) for p in papers]
    for line in results:
        print(line)
    return 1 if any(r.startswith("FAIL") for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
