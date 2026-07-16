"""Create a Notion review page from a structured summary.

The structured summary is a dict with these keys (all optional except title/summary):
    title:        str  - the review card title
    summary:      str  - the main structured summary body (Markdown-ish text)
    source_type:  str  - transcript | skill | web | doc | paper | ...
    source_url:   str  - link back to the source
    key_points:   list[str]
    tags:         list[str]
    status:       str  - defaults to "Needs review"

Config (env):
    NOTION_TOKEN       - a Notion internal integration token
    NOTION_REVIEW_DB   - the target database id (shared with the integration)
"""
from __future__ import annotations

import os

REVIEW_STATUS_DEFAULT = "Needs review"


def build_page_payload(summary: dict, database_id: str) -> dict:
    """Turn a structured summary into a Notion pages.create payload (no API call)."""
    title = summary.get("title") or "Untitled summary"
    props: dict = {
        # Assumes a "Name" title property and a "Status" select in the review DB.
        "Name": {"title": [{"text": {"content": title[:200]}}]},
        "Status": {"select": {"name": summary.get("status") or REVIEW_STATUS_DEFAULT}},
    }
    if summary.get("source_url"):
        props["Source"] = {"url": summary["source_url"]}
    if summary.get("source_type"):
        props["Type"] = {"select": {"name": summary["source_type"]}}
    if summary.get("tags"):
        props["Tags"] = {"multi_select": [{"name": t} for t in summary["tags"][:10]]}

    children: list[dict] = []
    if summary.get("summary"):
        children.append(_paragraph(summary["summary"]))
    for point in summary.get("key_points") or []:
        children.append(_bullet(point))

    return {
        "parent": {"database_id": database_id},
        "properties": props,
        "children": children,
    }


def _paragraph(text: str) -> dict:
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"type": "text", "text": {"content": text[:1900]}}]},
    }


def _bullet(text: str) -> dict:
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text[:1900]}}]
        },
    }


def create_review_page(summary: dict, dry_run: bool = False) -> dict:
    """Create a Notion review page for `summary`. With dry_run, return the payload only."""
    database_id = os.environ.get("NOTION_REVIEW_DB", "")
    payload = build_page_payload(summary, database_id or "<NOTION_REVIEW_DB>")
    if dry_run:
        return payload

    token = os.environ.get("NOTION_TOKEN")
    if not token or not database_id:
        raise RuntimeError("set NOTION_TOKEN and NOTION_REVIEW_DB to create a review page")

    from notion_client import Client  # lazy import so dry-run needs no dependency

    notion = Client(auth=token)
    return notion.pages.create(**payload)
