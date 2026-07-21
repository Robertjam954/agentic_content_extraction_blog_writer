"""CLI: `python -m rag index` and `python -m rag search "query"`."""
from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="rag", description="RAG index over the project's notes and docs (ChromaDB)."
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("index", help="build or update the index")
    pi.add_argument("--reset", action="store_true", help="drop and rebuild from scratch")

    ps = sub.add_parser("search", help="semantic search over the index")
    ps.add_argument("query", help="natural-language query")
    ps.add_argument("-k", type=int, default=5, help="number of results (default 5)")
    ps.add_argument(
        "--type",
        dest="source_type",
        choices=["transcript", "skill", "web", "doc", "brief"],
        help="restrict to one source type",
    )

    args = ap.parse_args(argv)

    try:
        if args.cmd == "index":
            from .index import build

            return build(reset=args.reset)

        from .search import search

        hits = search(args.query, k=args.k, source_type=args.source_type)
        if not hits:
            print("no results (is the index built? run: python -m rag index)")
            return 0
        for h in hits:
            loc = h["source_url"] or h["source_path"]
            print(f"[{h['score']:.3f}] {h['title']}  ({h['source_type']}: {loc})")
            snippet = " ".join(h["text"].split())[:220]
            print(f"    {snippet}...\n")
        return 0
    except ImportError as e:
        print(
            f"missing dependency ({e}); install the RAG deps with:\n"
            "    pip install chromadb",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
