#!/usr/bin/env python3
"""Ingestion (Module 2): fetch YouTube transcripts into the vault inbox.

Given a list of YouTube URLs or IDs, this fetches each video's transcript and
writes it as a clean .txt file to Inbox/Transcripts_to_Process/, named by the
video ID so the downstream transcript processing agent can derive `youtube_id`
from the filename. Videos already present in the inbox are skipped.

Usage:
    python3 scripts/fetch_transcripts.py URL_OR_ID [URL_OR_ID ...]
    python3 scripts/fetch_transcripts.py --file urls.txt

Requires: youtube-transcript-api (v1.x).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import CouldNotRetrieveTranscript

REPO_ROOT = Path(__file__).resolve().parent.parent
INBOX = REPO_ROOT / "Inbox" / "Transcripts_to_Process"

# 11-char YouTube IDs use [A-Za-z0-9_-]
_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def extract_video_id(url_or_id: str) -> str | None:
    """Pull the 11-char video ID out of a URL or accept a bare ID."""
    s = url_or_id.strip()
    if _ID_RE.match(s):
        return s
    parsed = urllib.parse.urlparse(s)
    host = parsed.netloc.lower()
    if host.endswith("youtu.be"):
        cand = parsed.path.lstrip("/").split("/")[0]
        return cand if _ID_RE.match(cand) else None
    if "youtube.com" in host:
        qs = urllib.parse.parse_qs(parsed.query)
        if "v" in qs and _ID_RE.match(qs["v"][0]):
            return qs["v"][0]
        # /embed/<id>, /shorts/<id>, /live/<id>
        parts = [p for p in parsed.path.split("/") if p]
        if len(parts) >= 2 and _ID_RE.match(parts[-1]):
            return parts[-1]
    return None


def fetch_title(video_id: str) -> str | None:
    """Best-effort video title via YouTube's public oEmbed endpoint.

    Tries urllib first, then falls back to curl (some environments have TLS
    interception that breaks urllib but not curl).
    """
    url = (
        "https://www.youtube.com/oembed?format=json&url="
        + urllib.parse.quote(f"https://www.youtube.com/watch?v={video_id}", safe="")
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            return json.load(resp).get("title")
    except Exception:
        pass
    try:
        out = subprocess.run(
            ["curl", "-fsS", "--max-time", "15", url],
            capture_output=True, text=True, timeout=20,
        )
        if out.returncode == 0 and out.stdout.strip():
            return json.loads(out.stdout).get("title")
    except Exception:
        pass
    return None


def fetch_transcript_text(video_id: str) -> str:
    """Fetch the transcript and return plain text (one line per snippet).

    Prefers a manually-created English track, falls back to any/generated.
    """
    api = YouTubeTranscriptApi()
    try:
        fetched = api.fetch(video_id, languages=["en", "en-US", "en-GB"])
    except Exception:
        # Fall back to whatever transcript exists (any language / generated).
        tlist = api.list(video_id)
        transcript = next(iter(tlist))
        fetched = transcript.fetch()
    lines = [snip.text.strip() for snip in fetched if snip.text.strip()]
    return "\n".join(lines)


def process(video_id: str) -> str:
    out_path = INBOX / f"{video_id}.txt"
    if out_path.exists():
        return f"SKIP  {video_id}  (already in inbox)"
    try:
        text = fetch_transcript_text(video_id)
    except CouldNotRetrieveTranscript as e:
        return f"FAIL  {video_id}  ({type(e).__name__}: {e})"
    except Exception as e:  # network, parsing, etc.
        return f"FAIL  {video_id}  ({type(e).__name__}: {e})"
    title = fetch_title(video_id) or ""
    header = (
        f"Title: {title}\n"
        f"Source: https://youtu.be/{video_id}\n"
        f"Video ID: {video_id}\n"
        "----\n\n"
    )
    out_path.write_text(header + text + "\n", encoding="utf-8")
    words = len(text.split())
    return f"OK    {video_id}  -> {out_path.name}  ({words} words) {title!r}"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("inputs", nargs="*", help="YouTube URLs or 11-char IDs")
    ap.add_argument("--file", help="path to a file with one URL/ID per line")
    args = ap.parse_args(argv)

    raw: list[str] = list(args.inputs)
    if args.file:
        raw += [ln for ln in Path(args.file).read_text().splitlines() if ln.strip()]
    if not raw:
        ap.error("provide at least one URL/ID or --file")

    INBOX.mkdir(parents=True, exist_ok=True)

    # Dedupe by resolved video ID, preserving order.
    seen: dict[str, None] = {}
    unresolved: list[str] = []
    for item in raw:
        vid = extract_video_id(item)
        if vid is None:
            unresolved.append(item)
        elif vid not in seen:
            seen[vid] = None

    for item in unresolved:
        print(f"WARN  could not parse video ID from: {item!r}")

    print(f"Resolved {len(seen)} unique video(s). Inbox: {INBOX}\n")
    results = [process(vid) for vid in seen]
    for line in results:
        print(line)

    failed = sum(1 for r in results if r.startswith("FAIL"))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
