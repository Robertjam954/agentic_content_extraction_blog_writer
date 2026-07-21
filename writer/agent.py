"""Draft a concept-first blog post: RAG-grounded content object -> Claude."""
from __future__ import annotations

from pathlib import Path

from .content_object import build_content_object

REPO_ROOT = Path(__file__).resolve().parent.parent
BRIEF = REPO_ROOT / "notion-db-to-technical-blog" / "notion-db-to-technical-blog.md"

# Sonnet-tier model for pipeline LLM work (configurable via the CLI --model flag).
# Note: claude-sonnet-4-20250514 retired 2026-06-15 and now 404s; claude-sonnet-5 is
# the current replacement.
DEFAULT_MODEL = "claude-sonnet-5"


def system_prompt() -> str:
    """The writing brief, up to the fill-in input template."""
    text = BRIEF.read_text(encoding="utf-8", errors="ignore")
    return text.split("INPUT OBJECT START:")[0].strip()


def render_input_object(obj: dict) -> str:
    insights = "\n".join(f"- {i}" for i in obj["key_insights"]) or "(none retrieved)"
    return (
        "INPUT OBJECT START:\n\n"
        f"Content Topic\n{obj['content_topic']}\n\n"
        f"Hook/Introduction\n{obj['hook'] or '(none - craft one from the topic and key insights)'}\n\n"
        f"Key Insights\n{insights}\n\n"
        f"SEO Keywords\n{obj['seo_keywords']}\n\n"
        f"Source Video\n{obj['source_video'] or '(none found in the index)'}\n\n"
        "Content Type\nBlog Post\n\n"
        f"Summary Transcript\n{obj['transcript']}\n\n"
        "Status\nDraft\n"
        "INPUT OBJECT FINISH.\n\n"
        "WRITTEN BLOG START:\n"
    )


def write_blog(
    topic: str,
    k: int = 8,
    model: str = DEFAULT_MODEL,
    dry_run: bool = False,
    max_tokens: int = 2000,
) -> str:
    """Retrieve, assemble, and (unless dry_run) draft the post."""
    obj = build_content_object(topic, k=k)
    user_msg = render_input_object(obj)

    if dry_run:
        sources = "\n".join(
            f"  [{h['score']:.3f}] {h['title']} ({h['source_type']}: {h['source_url'] or h['source_path']})"
            for h in obj["hits"]
        )
        return (
            "=== DRY RUN (no API call) ===\n\n"
            f"Retrieved {len(obj['hits'])} chunks for topic: {topic!r}\n{sources}\n\n"
            f"Would call model: {model}\n\n"
            "--- assembled content object (user message) ---\n"
            f"{user_msg}"
        )

    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt(),
        messages=[{"role": "user", "content": user_msg}],
    )
    return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
