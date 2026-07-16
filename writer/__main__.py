"""CLI: `python -m writer "topic" [--dry-run] [-o out.md]`."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .agent import DEFAULT_MODEL, write_blog


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="writer",
        description="RAG-grounded content writing agent (Claude).",
    )
    ap.add_argument("topic", help="blog topic / query to ground the post on")
    ap.add_argument("-k", type=int, default=8, help="RAG chunks to retrieve (default 8)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"model id (default {DEFAULT_MODEL})")
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="retrieve + assemble only; print the prompt without calling the API",
    )
    ap.add_argument("-o", "--out", help="write the draft to this file instead of stdout")
    args = ap.parse_args(argv)

    try:
        out = write_blog(args.topic, k=args.k, model=args.model, dry_run=args.dry_run)
    except ImportError as e:
        print(f"missing dependency ({e}); install with: pip install anthropic", file=sys.stderr)
        return 1
    except Exception as e:  # e.g. missing ANTHROPIC_API_KEY, API/network error
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1

    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
