"""Build/update the RAG index: discover notes and docs, chunk them, embed into Chroma.

Idempotent: each file's chunks are keyed by `<relative_path>::<n>` and re-written on
every run, so editing a file updates its chunks and stale chunks for a shrunken file
are cleared first. Pass reset=True to drop and rebuild the whole collection.
Every build also purges stored chunks under excluded directory prefixes, even
when the corresponding file has been removed from disk.
"""
from __future__ import annotations

import re
from pathlib import PurePosixPath

from .config import CHUNK_CHARS, CHUNK_OVERLAP, EXCLUDE_DIRS, EXCLUDE_PARTS, INCLUDE_EXTS, REPO_ROOT
from .store import COLLECTION, get_client, get_collection


def excluded_directory(rel: str) -> bool:
    """Match configured directories exactly, including nested descendants.

    Accept either separator used by previous platform-native source_path values.
    """
    parts = PurePosixPath(rel.replace("\\", "/")).parts
    return any(
        len(parts) > len(prefix) and parts[:len(prefix)] == prefix
        for prefix in EXCLUDE_DIRS
    )


def purge_excluded_chunks(col, batch_size: int = 1000) -> int:
    """Remove only stored chunks beneath excluded directory prefixes.

    Scan metadata in bounded pages, including paths no longer present on disk.
    Finish scanning before deleting so offsets do not skip shifted records.
    Errors intentionally propagate: a failed cleanup must not report success.
    """
    stale_ids = []
    offset = 0
    while True:
        page = col.get(limit=batch_size, offset=offset, include=["metadatas"])
        ids = page["ids"]
        for chunk_id, meta in zip(ids, page["metadatas"]):
            source_path = (meta or {}).get("source_path")
            if isinstance(source_path, str) and excluded_directory(source_path):
                stale_ids.append(chunk_id)
        if len(ids) < batch_size:
            break
        offset += len(ids)
    for start in range(0, len(stale_ids), batch_size):
        col.delete(ids=stale_ids[start:start + batch_size])
    return len(stale_ids)


def iter_files():
    for p in sorted(REPO_ROOT.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in INCLUDE_EXTS:
            continue
        if any(part in EXCLUDE_PARTS for part in p.relative_to(REPO_ROOT).parts):
            continue
        if excluded_directory(p.relative_to(REPO_ROOT).as_posix()):
            continue
        yield p


def _field(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.*)$", fm)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def parse_document(path, text: str) -> tuple[str, str, str]:
    """Return (title, source_url, body), handling YAML frontmatter, the transcript
    header (Title/Source/Video ID/----), or a leading Markdown heading."""
    title = source = ""
    body = text

    fm = re.match(r"(?s)^\s*---\n(.*?)\n---\n?(.*)$", text)
    if fm:
        block, body = fm.group(1), fm.group(2)
        title = _field(block, "title") or _field(block, "skill")
        source = _field(block, "source_url") or _field(block, "source")
    else:
        hdr = re.match(
            r"(?s)^Title:(.*?)\nSource:(.*?)\n(?:Video ID:.*?\n)?----\n(.*)$", text
        )
        if hdr:
            title, source, body = hdr.group(1).strip(), hdr.group(2).strip(), hdr.group(3)

    if not title:
        h = re.search(r"(?m)^#\s+(.+)$", body)
        title = h.group(1).strip() if h else path.stem
    return title, source, body.strip()


def source_type(rel: str) -> str:
    if "Transcripts_to_Process" in rel:
        return "transcript"
    if "Skills_to_Process" in rel:
        return "skill"
    if "Web_to_Process" in rel:
        return "web"
    if rel.count("/") == 0:
        return "doc"
    return "brief"


def chunk_text(text: str, size: int = CHUNK_CHARS, overlap: int = CHUNK_OVERLAP) -> list[str]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    cur = ""
    for para in paras:
        if cur and len(cur) + len(para) + 1 > size:
            chunks.append(cur)
            cur = (cur[-overlap:] + "\n" + para) if overlap else para
        else:
            cur = f"{cur}\n{para}".strip() if cur else para
        while len(cur) > size * 1.5:
            chunks.append(cur[:size])
            cur = cur[size - overlap :]
    if cur.strip():
        chunks.append(cur)
    return chunks


def build(reset: bool = False) -> int:
    client = get_client()
    if reset:
        try:
            client.delete_collection(COLLECTION)
            print(f"reset: dropped collection '{COLLECTION}'")
        except Exception:
            pass
    col = get_collection(client)
    purged = purge_excluded_chunks(col)
    if purged:
        print(f"removed {purged} chunks from excluded directories")

    n_files = n_chunks = 0
    for p in iter_files():
        rel = p.relative_to(REPO_ROOT).as_posix()
        text = p.read_text(encoding="utf-8", errors="ignore")
        title, source, body = parse_document(p, text)
        chunks = chunk_text(body)
        if not chunks:
            continue

        # Clear any prior chunks for this file, then (re)add.
        try:
            col.delete(where={"source_path": rel})
        except Exception:
            pass

        ids = [f"{rel}::{i}" for i in range(len(chunks))]
        metas = [
            {
                "source_path": rel,
                "title": title,
                "source_type": source_type(rel),
                "source_url": source or "",
                "chunk": i,
            }
            for i in range(len(chunks))
        ]
        col.upsert(ids=ids, documents=chunks, metadatas=metas)
        n_files += 1
        n_chunks += len(chunks)
        print(f"  {rel:60}  {len(chunks):3d} chunks  [{source_type(rel)}]")

    print(f"\nindexed {n_chunks} chunks from {n_files} files into '{COLLECTION}'")
    print(f"total chunks in collection: {col.count()}")
    return 0

