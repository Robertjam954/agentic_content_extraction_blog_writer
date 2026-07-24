#!/usr/bin/env python3
"""Ingestion (Module 2): expand YouTube channels into transcripts.

`fetch_transcripts.py` fetches transcripts for individual videos. This script sits
in front of it: given a channel handle, custom URL, or channel ID, it resolves the
channel's ID, reads the channel's public RSS feed
(`https://www.youtube.com/feeds/videos.xml?channel_id=...`, which lists the ~15
most recent uploads), and either prints the video IDs (`--list`) or fetches each
video's transcript into `Inbox/Transcripts_to_Process/` via `fetch_transcripts`.

Accepted channel forms:
    @zenvanriel                                   (bare handle)
    https://www.youtube.com/@zenvanriel/videos    (handle URL)
    https://www.youtube.com/GitHub                (legacy custom URL)
    https://www.youtube.com/channel/UC...         (canonical channel URL)
    UCxxxxxxxxxxxxxxxxxxxxxx                       (bare 24-char channel ID)

Usage:
    python3 scripts/fetch_youtube_channel.py @zenvanriel
    python3 scripts/fetch_youtube_channel.py https://www.youtube.com/GitHub --limit 5
    python3 scripts/fetch_youtube_channel.py @zenvanriel --list

Fetching uses curl with a browser User-Agent (matches the other scripts).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0 Safari/537.36"
_CHANNEL_ID_RE = re.compile(r"^UC[0-9A-Za-z_-]{22}$")


def _get(url: str, timeout: int = 30) -> str | None:
    try:
        out = subprocess.run(
            ["curl", "-fsSL", "--max-time", str(timeout), "-A", UA, url],
            capture_output=True, text=True, timeout=timeout + 10,
        )
        return out.stdout if out.returncode == 0 and out.stdout else None
    except Exception:
        return None


def resolve_channel_id(spec: str) -> str | None:
    """Resolve any accepted channel form to a canonical UC... channel ID."""
    spec = spec.strip()
    if _CHANNEL_ID_RE.match(spec):
        return spec
    # /channel/UC... anywhere in a URL.
    m = re.search(r"/channel/(UC[0-9A-Za-z_-]{22})", spec)
    if m:
        return m.group(1)
    # Normalise a bare handle to a channel URL.
    if spec.startswith("@"):
        url = f"https://www.youtube.com/{spec}"
    elif spec.startswith("http"):
        url = spec
    else:
        url = f"https://www.youtube.com/@{spec}"
    html = _get(url)
    if not html:
        return None
    m = re.search(r'"(?:externalId|channelId)":"(UC[0-9A-Za-z_-]{22})"', html)
    return m.group(1) if m else None


def channel_video_ids(channel_id: str) -> list[str]:
    """Return recent upload video IDs from the channel's public RSS feed."""
    feed = _get(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
    if not feed:
        return []
    ids: list[str] = []
    seen: set[str] = set()
    for vid in re.findall(r"<yt:videoId>([^<]+)</yt:videoId>", feed):
        if vid not in seen:
            seen.add(vid)
            ids.append(vid)
    return ids


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("channels", nargs="+", help="channel handles, URLs, or IDs")
    ap.add_argument("--limit", type=int, default=0,
                    help="max videos per channel (0 = all in the feed)")
    ap.add_argument("--list", action="store_true",
                    help="only print resolved video IDs/URLs, do not fetch transcripts")
    args = ap.parse_args(argv)

    all_ids: list[str] = []
    for spec in args.channels:
        cid = resolve_channel_id(spec)
        if not cid:
            print(f"WARN  could not resolve channel: {spec!r}")
            continue
        vids = channel_video_ids(cid)
        if args.limit:
            vids = vids[: args.limit]
        print(f"{spec}  ->  {cid}  ({len(vids)} video(s))")
        all_ids += vids

    # Dedupe across channels, preserve order.
    seen: set[str] = set()
    ids = [v for v in all_ids if not (v in seen or seen.add(v))]

    if args.list:
        for v in ids:
            print(f"https://youtu.be/{v}")
        return 0

    if not ids:
        print("No videos resolved.")
        return 1

    import fetch_transcripts  # deferred: only needed for the actual transcript fetch
    fetch_transcripts.INBOX.mkdir(parents=True, exist_ok=True)
    print(f"\nFetching {len(ids)} transcript(s) -> {fetch_transcripts.INBOX}\n")
    results = [fetch_transcripts.process(v) for v in ids]
    for line in results:
        print(line)
    return 1 if any(r.startswith("FAIL") for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
