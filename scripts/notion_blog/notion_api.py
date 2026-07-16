"""Minimal Notion REST API client using only the standard library.

Covers the small surface this pipeline needs: query a database, read a page's
blocks, create pages, and update page properties. Auth comes from the
NOTION_API_KEY environment variable (a Notion internal-integration secret).
"""

from __future__ import annotations

import json
import logging
import os
import time
import urllib.error
import urllib.request
from typing import Any, Iterator

logger = logging.getLogger(__name__)

NOTION_BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
MAX_RICH_TEXT_LEN = 2000
MAX_CHILDREN_PER_REQUEST = 100


class NotionError(RuntimeError):
    """Raised when the Notion API returns an error response."""


def _request(method: str, path: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    token = os.environ.get("NOTION_API_KEY")
    if not token:
        raise NotionError("NOTION_API_KEY is not set")

    url = f"{NOTION_BASE_URL}{path}"
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Notion-Version", NOTION_VERSION)
    req.add_header("Content-Type", "application/json")

    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            payload = exc.read().decode("utf-8", errors="replace")
            if exc.code == 429 and attempt < 3:
                wait = float(exc.headers.get("Retry-After", 2 ** attempt))
                logger.warning("Notion rate limit hit; retrying in %.1fs", wait)
                time.sleep(wait)
                continue
            raise NotionError(f"Notion API {exc.code} on {method} {path}: {payload}") from exc
        except urllib.error.URLError as exc:
            if attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise NotionError(f"Network error on {method} {path}: {exc}") from exc
    raise NotionError(f"Exhausted retries on {method} {path}")


def query_database(
    database_id: str, filter_: dict[str, Any] | None = None
) -> Iterator[dict[str, Any]]:
    """Yield every page in a database matching the optional filter."""
    cursor: str | None = None
    while True:
        body: dict[str, Any] = {"page_size": 100}
        if filter_:
            body["filter"] = filter_
        if cursor:
            body["start_cursor"] = cursor
        result = _request("POST", f"/databases/{database_id}/query", body)
        yield from result.get("results", [])
        if not result.get("has_more"):
            return
        cursor = result.get("next_cursor")


def get_block_children(block_id: str) -> list[dict[str, Any]]:
    """Return all child blocks of a page or block, following pagination."""
    blocks: list[dict[str, Any]] = []
    cursor: str | None = None
    while True:
        path = f"/blocks/{block_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        result = _request("GET", path)
        blocks.extend(result.get("results", []))
        if not result.get("has_more"):
            return blocks
        cursor = result.get("next_cursor")


def create_page(
    database_id: str, properties: dict[str, Any], children: list[dict[str, Any]]
) -> dict[str, Any]:
    """Create a page in a database, appending children in batches of 100."""
    first_batch = children[:MAX_CHILDREN_PER_REQUEST]
    rest = children[MAX_CHILDREN_PER_REQUEST:]
    page = _request(
        "POST",
        "/pages",
        {
            "parent": {"database_id": database_id},
            "properties": properties,
            "children": first_batch,
        },
    )
    page_id = page["id"]
    while rest:
        batch, rest = rest[:MAX_CHILDREN_PER_REQUEST], rest[MAX_CHILDREN_PER_REQUEST:]
        _request("PATCH", f"/blocks/{page_id}/children", {"children": batch})
    return page


def update_page_properties(page_id: str, properties: dict[str, Any]) -> dict[str, Any]:
    return _request("PATCH", f"/pages/{page_id}", {"properties": properties})


# ---------------------------------------------------------------------------
# Property helpers
# ---------------------------------------------------------------------------

def prop_plain_text(prop: dict[str, Any]) -> str:
    """Extract plain text from a title or rich_text property value."""
    kind = prop.get("type")
    parts = prop.get(kind, []) if kind in ("title", "rich_text") else []
    return "".join(part.get("plain_text", "") for part in parts)


def prop_select(prop: dict[str, Any]) -> str:
    value = prop.get("select")
    return value.get("name", "") if value else ""


def prop_multi_select(prop: dict[str, Any]) -> list[str]:
    return [item.get("name", "") for item in prop.get("multi_select", [])]


def prop_url(prop: dict[str, Any]) -> str:
    return prop.get("url") or ""


# ---------------------------------------------------------------------------
# Markdown <-> Notion block conversion
# ---------------------------------------------------------------------------

def _rich_text(text: str) -> list[dict[str, Any]]:
    """Split text into Notion rich_text objects under the 2000-char limit."""
    chunks = [text[i : i + MAX_RICH_TEXT_LEN] for i in range(0, len(text), MAX_RICH_TEXT_LEN)]
    return [{"type": "text", "text": {"content": chunk}} for chunk in chunks or [""]]


def markdown_to_blocks(markdown: str) -> list[dict[str, Any]]:
    """Convert a Markdown document into a flat list of Notion blocks.

    Handles headings, bullet and numbered lists, block quotes, fenced code,
    dividers, and paragraphs. Inline formatting is passed through as plain
    text, which Notion renders literally; that is acceptable for review notes.
    """
    blocks: list[dict[str, Any]] = []
    lines = markdown.splitlines()
    i = 0
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(paragraph).strip()
            if text:
                blocks.append(
                    {"type": "paragraph", "paragraph": {"rich_text": _rich_text(text)}}
                )
            paragraph.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            language = stripped[3:].strip() or "plain text"
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            blocks.append(
                {
                    "type": "code",
                    "code": {
                        "rich_text": _rich_text("\n".join(code_lines)),
                        "language": language,
                    },
                }
            )
        elif stripped.startswith("#"):
            flush_paragraph()
            level = min(len(stripped) - len(stripped.lstrip("#")), 3)
            text = stripped.lstrip("#").strip()
            key = f"heading_{level}"
            blocks.append({"type": key, key: {"rich_text": _rich_text(text)}})
        elif stripped.startswith(("- ", "* ")):
            flush_paragraph()
            blocks.append(
                {
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": _rich_text(stripped[2:].strip())},
                }
            )
        elif stripped[:2].rstrip(".").isdigit() and ". " in stripped[:5]:
            flush_paragraph()
            text = stripped.split(". ", 1)[1]
            blocks.append(
                {
                    "type": "numbered_list_item",
                    "numbered_list_item": {"rich_text": _rich_text(text)},
                }
            )
        elif stripped.startswith("> "):
            flush_paragraph()
            blocks.append({"type": "quote", "quote": {"rich_text": _rich_text(stripped[2:])}})
        elif stripped in ("---", "***", "___"):
            flush_paragraph()
            blocks.append({"type": "divider", "divider": {}})
        elif not stripped:
            flush_paragraph()
        else:
            paragraph.append(stripped)
        i += 1

    flush_paragraph()
    return blocks


def _block_text(block: dict[str, Any]) -> str:
    kind = block.get("type", "")
    payload = block.get(kind, {})
    return "".join(part.get("plain_text", "") for part in payload.get("rich_text", []))


def blocks_to_markdown(blocks: list[dict[str, Any]]) -> str:
    """Render Notion blocks back into Markdown text."""
    lines: list[str] = []
    numbered_index = 0
    for block in blocks:
        kind = block.get("type", "")
        text = _block_text(block)
        if kind != "numbered_list_item":
            numbered_index = 0
        if kind == "paragraph":
            lines.append(text)
            lines.append("")
        elif kind in ("heading_1", "heading_2", "heading_3"):
            lines.append("#" * int(kind[-1]) + " " + text)
            lines.append("")
        elif kind == "bulleted_list_item":
            lines.append(f"- {text}")
        elif kind == "numbered_list_item":
            numbered_index += 1
            lines.append(f"{numbered_index}. {text}")
        elif kind == "to_do":
            checked = block.get("to_do", {}).get("checked", False)
            lines.append(f"- [{'x' if checked else ' '}] {text}")
        elif kind == "quote":
            lines.append(f"> {text}")
            lines.append("")
        elif kind == "code":
            language = block.get("code", {}).get("language", "")
            lines.append(f"```{language}")
            lines.append(text)
            lines.append("```")
            lines.append("")
        elif kind == "divider":
            lines.append("---")
            lines.append("")
        elif text:
            lines.append(text)
            lines.append("")
    return "\n".join(lines).strip() + "\n"
