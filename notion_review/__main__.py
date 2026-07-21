"""CLI: push a structured summary (JSON) to Notion for review."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .upload import create_review_page

_SAMPLE = {
    "title": "Building an AI knowledge graph in Obsidian",
    "summary": "A structured summary of the collected sources, ready for human review.",
    "source_type": "doc",
    "source_url": "https://youtu.be/dBebGUgiz34",
    "key_points": ["Point one", "Point two"],
    "tags": ["rag", "obsidian"],
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="notion_review", description=__doc__)
    ap.add_argument("summary", nargs="?", help="path to a structured-summary JSON file")
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="print the Notion payload without calling the API",
    )
    args = ap.parse_args(argv)

    summary = json.loads(Path(args.summary).read_text()) if args.summary else _SAMPLE

    try:
        result = create_review_page(summary, dry_run=args.dry_run)
    except Exception as e:
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(json.dumps(result, indent=2))
    else:
        print(f"created Notion review page: {result.get('id', '(no id)')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
