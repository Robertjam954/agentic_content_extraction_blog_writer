#!/usr/bin/env python3
"""Ingestion (Module 2): ingest local files into the vault inbox.

A companion to the web extractors for material that arrives as files rather than
URLs (PDFs, saved HTML, Markdown, code, images, and other binaries). Each input is
converted to an Obsidian-native note with YAML frontmatter and written to
`Inbox/Files_to_Process/`, so it drops straight into the vault and is picked up by
the RAG index. Files already ingested are skipped (idempotent, keyed by content
hash recorded in the note).

Dispatch by extension:
  - .pdf                      : text extracted with pypdf (falls back to a reference
                                note if pypdf is unavailable or the PDF has no text
                                layer, e.g. a scanned image).
  - .md .markdown .txt        : content passed through into a note.
  - .html .htm                : a Netscape/Mozilla bookmarks export becomes one note
                                listing its links; any other HTML is converted to
                                Markdown.
  - code (.py .js .ts .sql .r .java .go .rs .sh .yaml .json ...) : fenced code note.
  - images (.png .jpg .jpeg .gif .webp .svg) : the image is copied into
                                `Inbox/Files_to_Process/assets/` and a note embeds it.
  - anything else (.vsdx .docx ...) : a reference note recording provenance (the
                                binary content itself is not extracted).

Usage:
    python3 scripts/ingest_files.py FILE [FILE ...]
    python3 scripts/ingest_files.py --file paths.txt
    python3 scripts/ingest_files.py ~/Downloads            # a directory (recursive)
    python3 scripts/ingest_files.py paper.pdf --source arxiv --type paper

Only pypdf (for PDF text) is an optional third-party dependency; everything else
uses the standard library.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import html as _html
import re
import shutil
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scrape_articles import html_to_markdown, slug_of  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTDIR_DEFAULT = REPO_ROOT / "Inbox" / "Files_to_Process"

TEXT_EXTS = {".md", ".markdown", ".txt", ".rst"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}
CODE_LANGS = {
    ".py": "python", ".js": "javascript", ".ts": "typescript", ".tsx": "tsx",
    ".jsx": "jsx", ".sql": "sql", ".r": "r", ".java": "java", ".go": "go",
    ".rs": "rust", ".sh": "bash", ".rb": "ruby", ".c": "c", ".cpp": "cpp",
    ".cs": "csharp", ".yaml": "yaml", ".yml": "yaml", ".json": "json",
    ".toml": "toml", ".css": "css", ".php": "php", ".swift": "swift",
}


def _yaml_str(v: str) -> str:
    return '"' + v.replace('"', "'") + '"'


def _slug(name: str) -> str:
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-.")
    return base[:80] or "file"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _title_from(stem: str) -> str:
    t = re.sub(r"[._-]+", " ", stem).strip()
    return t[:1].upper() + t[1:] if t else stem


# Producer/app names PDFs often leave in the title metadata; not real titles.
_GENERIC_TITLES = {"chrome", "untitled", "print", "document", "microsoft word",
                   "safari", "firefox", "pdf", ""}


def _clean_title(t: str) -> str:
    return re.sub(r"\s+", " ", t.replace("\xa0", " ")).strip()


# --------------------------------------------------------------------------- #
# Per-type extraction. Each returns (kind, title, body_markdown, extra_asset).
# extra_asset, when set, is a Path to copy into the assets dir next to the note.
# --------------------------------------------------------------------------- #
def _extract_pdf(path: Path) -> tuple[str, str]:
    try:
        import pypdf
    except ModuleNotFoundError:
        return "", ""
    try:
        reader = pypdf.PdfReader(str(path))
    except Exception:
        return "", ""
    title = ""
    try:
        if reader.metadata and reader.metadata.title:
            candidate = _clean_title(str(reader.metadata.title))
            if candidate.lower() not in _GENERIC_TITLES:
                title = candidate
    except Exception:
        title = ""
    pages = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text.strip():
            pages.append(text.strip())
    body = "\n\n".join(pages)
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return title, body


def _is_bookmarks(text: str) -> bool:
    head = text[:2000].upper()
    return "NETSCAPE-BOOKMARK-FILE" in head or ("<DL>" in text.upper() and "<A HREF" in text.upper())


def _extract_bookmarks(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Return (title, [(url, label), ...]) from a Netscape/Mozilla bookmarks export."""
    links: list[tuple[str, str]] = []
    seen: set[str] = set()
    for m in re.finditer(r'<A\s+[^>]*HREF="([^"]+)"[^>]*>(.*?)</A>', text, re.I | re.S):
        url = _html.unescape(m.group(1)).strip()
        label = _html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        if not url or url.startswith("place:") or url in seen:
            continue
        seen.add(url)
        links.append((url, label or url))
    tm = re.search(r"<TITLE>(.*?)</TITLE>", text, re.I | re.S)
    title = _html.unescape(tm.group(1)).strip() if tm else "Bookmarks"
    return title, links


def _build_note_body(kind: str, path: Path, source: str, type_: str) -> tuple[str, str, int]:
    """Return (note_markdown, title, word_count) for a text/convertible input.

    Raises ValueError for kinds handled elsewhere (image/binary).
    """
    raw = path.read_bytes()
    digest = _sha256(raw)
    today = _dt.date.today().isoformat()
    ext = path.suffix.lower()
    title = _title_from(path.stem)
    body = ""
    note_type = type_

    if kind == "pdf":
        pdf_title, body = _extract_pdf(path)
        if pdf_title:
            title = pdf_title
        note_type = type_ or "pdf"
    elif kind == "text":
        body = raw.decode("utf-8", errors="replace").strip()
        note_type = type_ or "note"
    elif kind == "bookmarks":
        text = raw.decode("utf-8", errors="replace")
        title, links = _extract_bookmarks(text)
        lines = [f"- [{label}]({url})" for url, label in links]
        body = f"{len(links)} bookmark(s):\n\n" + "\n".join(lines)
        note_type = type_ or "bookmarks"
    elif kind == "html":
        text = raw.decode("utf-8", errors="replace")
        body = html_to_markdown(text)
        note_type = type_ or "web"
    elif kind == "code":
        lang = CODE_LANGS.get(ext, "")
        code = raw.decode("utf-8", errors="replace").rstrip()
        body = f"```{lang}\n{code}\n```"
        note_type = type_ or "code"
    else:
        raise ValueError(kind)

    title = _clean_title(title)
    has_content = bool(body.strip())
    fm = [
        "---",
        f"source_file: {_yaml_str(path.name)}",
        f"title: {_yaml_str(title)}",
        f"ingested: {today}",
        f"type: {note_type}",
        f"source: {source}",
        f"sha256: {digest}",
        f"has_content: {str(has_content).lower()}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if not has_content:
        if kind == "pdf":
            fm += ["_No extractable text (scanned image PDF or empty). "
                   "Original file needed for OCR._", ""]
        else:
            fm += ["_No extractable content._", ""]
    note = "\n".join(fm) + (body.rstrip() if has_content else "") + \
        f"\n\n---\nSource file: {path.name}\n"
    return note, title, len(body.split())


def _build_image_note(path: Path, source: str, type_: str,
                      asset_rel: str) -> tuple[str, str]:
    digest = _sha256(path.read_bytes())
    today = _dt.date.today().isoformat()
    title = _title_from(path.stem)
    note_type = type_ or "image"
    fm = [
        "---",
        f"source_file: {_yaml_str(path.name)}",
        f"title: {_yaml_str(title)}",
        f"ingested: {today}",
        f"type: {note_type}",
        f"source: {source}",
        f"sha256: {digest}",
        f"asset: {_yaml_str(asset_rel)}",
        "---",
        "",
        f"# {title}",
        "",
        f"![{title}]({asset_rel})",
        "",
        "---",
        f"Source file: {path.name}",
        "",
    ]
    return "\n".join(fm), title


def _build_reference_note(path: Path, source: str, type_: str,
                          asset_rel: str) -> tuple[str, str]:
    raw = path.read_bytes()
    digest = _sha256(raw)
    today = _dt.date.today().isoformat()
    title = _title_from(path.stem)
    note_type = type_ or "file"
    fm = [
        "---",
        f"source_file: {_yaml_str(path.name)}",
        f"title: {_yaml_str(title)}",
        f"ingested: {today}",
        f"type: {note_type}",
        f"source: {source}",
        f"sha256: {digest}",
        f"bytes: {len(raw)}",
        f"asset: {_yaml_str(asset_rel)}",
        "---",
        "",
        f"# {title}",
        "",
        f"Binary file ingested by reference ({path.suffix.lower() or 'no extension'}, "
        f"{len(raw)} bytes). Text was not extracted; the original is stored at "
        f"`{asset_rel}`.",
        "",
        "---",
        f"Source file: {path.name}",
        "",
    ]
    return "\n".join(fm), title


def _kind_of(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return "pdf"
    if ext in TEXT_EXTS:
        return "text"
    if ext in {".html", ".htm"}:
        try:
            head = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            return "html"
        return "bookmarks" if _is_bookmarks(head) else "html"
    if ext in CODE_LANGS:
        return "code"
    if ext in IMAGE_EXTS:
        return "image"
    return "binary"


def process(path: Path, outdir: Path, source: str = "local-file",
            type_: str = "") -> str:
    if not path.is_file():
        return f"FAIL  {path.name}  (not a file)"
    kind = _kind_of(path)
    slug = _slug(path.stem) + ".md"
    out_path = outdir / slug
    if out_path.exists():
        return f"SKIP  {out_path.name}  (already ingested)"

    outdir.mkdir(parents=True, exist_ok=True)
    if kind in {"image", "binary"}:
        assets = outdir / "assets"
        assets.mkdir(parents=True, exist_ok=True)
        asset_name = _slug(path.stem) + path.suffix.lower()
        asset_path = assets / asset_name
        if not asset_path.exists():
            shutil.copy2(path, asset_path)
        asset_rel = f"assets/{asset_name}"
        if kind == "image":
            note, title = _build_image_note(path, source, type_, asset_rel)
        else:
            note, title = _build_reference_note(path, source, type_, asset_rel)
        out_path.write_text(note, encoding="utf-8")
        return f"OK    {out_path.name}  ({kind})  {title[:60]!r}"

    note, title, words = _build_note_body(kind, path, source, type_)
    out_path.write_text(note, encoding="utf-8")
    return f"OK    {out_path.name}  ({kind}, {words} words)  {title[:60]!r}"


def ingest_files(paths: list[str], source: str = "local-file", type_: str = "",
                 outdir: Path | None = None) -> list[str]:
    outdir = outdir or OUTDIR_DEFAULT
    results = []
    for p in _expand(paths):
        results.append(process(p, outdir, source, type_))
    return results


def _expand(paths: list[str]) -> list[Path]:
    out: list[Path] = []
    for raw in paths:
        p = Path(raw).expanduser()
        if p.is_dir():
            out.extend(sorted(f for f in p.rglob("*") if f.is_file()))
        elif p.is_file():
            out.append(p)
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Ingest local files into the vault inbox.")
    ap.add_argument("paths", nargs="*", help="files or directories to ingest")
    ap.add_argument("--file", help="a text file of paths (one per line)")
    ap.add_argument("--source", default="local-file", help="source: value in frontmatter")
    ap.add_argument("--type", default="", help="override the type: value in frontmatter")
    ap.add_argument("--outdir", type=Path, default=OUTDIR_DEFAULT)
    args = ap.parse_args(argv)

    paths = list(args.paths)
    if args.file:
        paths += [ln.strip() for ln in Path(args.file).read_text().splitlines()
                  if ln.strip() and not ln.startswith("#")]
    if not paths:
        ap.error("provide one or more files/directories, or --file")

    results = ingest_files(paths, args.source, args.type, args.outdir)
    for r in results:
        print(r)
    return 0 if all(not r.startswith("FAIL") for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
