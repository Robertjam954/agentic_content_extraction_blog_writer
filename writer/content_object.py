"""Assemble the writing agent's content object from RAG retrieval.

This is purely mechanical (no LLM): it retrieves the most relevant chunks for a topic
and arranges them into the fields the writing brief consumes. The LLM does the actual
elaboration downstream.
"""
from __future__ import annotations

import re

from rag.search import search


def _lead(text: str, n: int = 240) -> str:
    """First sentence(s) of `text`, up to about n characters."""
    text = " ".join(text.split())
    lead = ""
    for s in re.split(r"(?<=[.!?])\s+", text):
        if lead and len(lead) + len(s) > n:
            break
        lead = f"{lead} {s}".strip()
    return lead or text[:n]


def _video_url(hits: list[dict]) -> str:
    for h in hits:
        if h["source_type"] == "transcript" and h["source_url"]:
            return h["source_url"]
    for h in hits:
        if "youtu" in (h["source_url"] or ""):
            return h["source_url"]
    return ""


def build_content_object(topic: str, k: int = 8) -> dict:
    """Retrieve k chunks for `topic` and assemble a content object."""
    hits = search(topic, k=k)

    seen: set[str] = set()
    insights: list[str] = []
    passages: list[str] = []
    for h in hits:
        loc = h["source_url"] or h["source_path"]
        passages.append(f"[{h['source_type']}] {h['title']} ({loc})\n{_lead(h['text'], 400)}")
        if h["source_path"] in seen:
            continue
        seen.add(h["source_path"])
        insights.append(f"{h['title']}: {_lead(h['text'])}")

    topic_kw = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", topic)]
    title_kw = [
        w.lower() for h in hits[:3] for w in re.findall(r"[A-Za-z][A-Za-z0-9-]{4,}", h["title"])
    ]
    seo = ", ".join(dict.fromkeys(topic_kw + title_kw))

    return {
        "content_topic": topic,
        "hook": "",
        "key_insights": insights[:6],
        "seo_keywords": seo,
        "source_video": _video_url(hits),
        "transcript": "\n\n".join(passages),
        "hits": hits,
    }
