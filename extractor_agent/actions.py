"""Extraction actions: plain functions that wrap the `scripts/` extractors.

These are dependency-free (only the standard library plus the sibling ingestion
scripts) so they can be unit-tested and driven directly. `agent.py` exposes them
as Microsoft Agent Framework tools; nothing here imports `agent_framework`, so the
deterministic extraction path never needs an LLM or a model key.

Every action returns a short human-readable status string (the same lines the CLI
scripts print), which is exactly what an agent needs to report back to the user.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Annotated

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import scrape_articles  # noqa: E402
import fetch_gdoc  # noqa: E402
import fetch_youtube_channel as ytc  # noqa: E402

SOURCES = sorted(scrape_articles.PRESETS)


def list_sources() -> str:
    """List the named blog/article source presets available for extraction."""
    lines = [f"{name}  ->  {scrape_articles.PRESETS[name].target}" for name in SOURCES]
    return "Available source presets:\n" + "\n".join(lines)


def extract_source(
    source: Annotated[str, "a preset name from list_sources, e.g. 'anthropic-engineering'"],
    limit: Annotated[int, "max posts to extract; 0 means all discovered"] = 10,
) -> str:
    """Extract posts from a named blog/article source preset into the vault inbox.

    Discovers the source's posts (via its RSS feed, sitemap, or listing page),
    fetches each one, and writes an Obsidian note to Inbox/Web_to_Process/.
    Already-extracted posts are skipped.
    """
    if source not in scrape_articles.PRESETS:
        return f"Unknown source {source!r}. Choose from: {', '.join(SOURCES)}"
    results = scrape_articles.scrape_source(source, limit=limit)
    return _summarize(f"source={source}", results)


def extract_urls(
    urls: Annotated[list[str], "explicit article/blog post URLs to extract"],
    source_tag: Annotated[str, "value for the note's source: frontmatter field"] = "web",
) -> str:
    """Extract a list of explicit article URLs into the vault inbox as Obsidian notes."""
    results = scrape_articles.scrape_urls(list(urls), source_tag=source_tag)
    return _summarize(f"{len(urls)} url(s)", results)


def extract_youtube_channel(
    channel: Annotated[str, "a YouTube handle (@name), channel URL, or channel ID"],
    limit: Annotated[int, "max recent videos to fetch transcripts for; 0 means all in feed"] = 5,
) -> str:
    """Fetch transcripts for a YouTube channel's recent uploads into the vault inbox.

    Resolves the channel's ID, reads its public uploads RSS feed, and writes one
    transcript .txt per video to Inbox/Transcripts_to_Process/.
    """
    cid = ytc.resolve_channel_id(channel)
    if not cid:
        return f"Could not resolve YouTube channel: {channel!r}"
    vids = ytc.channel_video_ids(cid)
    if limit:
        vids = vids[:limit]
    if not vids:
        return f"{channel} -> {cid}: no videos found in the channel feed."
    import fetch_transcripts  # deferred: needs youtube-transcript-api
    fetch_transcripts.INBOX.mkdir(parents=True, exist_ok=True)
    results = [fetch_transcripts.process(v) for v in vids]
    return _summarize(f"channel={channel} ({cid})", results)


def list_youtube_channel(
    channel: Annotated[str, "a YouTube handle (@name), channel URL, or channel ID"],
    limit: Annotated[int, "max recent videos to list; 0 means all in feed"] = 0,
) -> str:
    """List a YouTube channel's recent upload video IDs without fetching transcripts."""
    cid = ytc.resolve_channel_id(channel)
    if not cid:
        return f"Could not resolve YouTube channel: {channel!r}"
    vids = ytc.channel_video_ids(cid)
    if limit:
        vids = vids[:limit]
    urls = "\n".join(f"https://youtu.be/{v}" for v in vids)
    return f"{channel} -> {cid} ({len(vids)} video(s)):\n{urls}"


def extract_google_doc(
    doc: Annotated[str, "a Google Doc URL or document ID (must be public or published)"],
) -> str:
    """Extract a public/published Google Doc into the vault inbox as an Obsidian note."""
    outdir = fetch_gdoc.OUTDIR_DEFAULT
    outdir.mkdir(parents=True, exist_ok=True)
    return _summarize("google-doc", [fetch_gdoc.process(doc, outdir)])


def _summarize(label: str, results: list[str]) -> str:
    ok = sum(1 for r in results if r.startswith("OK"))
    skip = sum(1 for r in results if r.startswith("SKIP"))
    fail = sum(1 for r in results if r.startswith(("FAIL", "WARN")))
    head = f"[{label}] {ok} written, {skip} skipped, {fail} failed."
    return head + "\n" + "\n".join(results)


# The action set the agent is given as tools.
ACTIONS = [
    list_sources,
    extract_source,
    extract_urls,
    extract_youtube_channel,
    list_youtube_channel,
    extract_google_doc,
]
