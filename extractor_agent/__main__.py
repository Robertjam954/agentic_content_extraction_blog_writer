"""CLI for the extractor agent.

    # Offline: list tools/sources and (optionally) run a preset deterministically -
    # no model or API key required.
    python -m extractor_agent --dry-run
    python -m extractor_agent --dry-run --source anthropic-engineering --limit 3

    # Live: drive extraction in natural language. Local-first (LM Studio) by default;
    # OPENAI_API_KEY or AZURE_OPENAI_ENDPOINT switch to a cloud backend.
    python -m extractor_agent "extract the 5 latest anthropic engineering posts"
    python -m extractor_agent --framework maf "extract latest 3 openai research posts"
"""
from __future__ import annotations

import argparse
import asyncio
import sys

from . import actions


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="Content extraction agent (LangChain or Microsoft Agent Framework).")
    ap.add_argument("prompt", nargs="*", help="natural-language extraction request (live mode)")
    ap.add_argument("--framework", choices=["langchain", "maf"], default="langchain",
                    help="live-mode orchestration framework (default: langchain)")
    ap.add_argument("--dry-run", action="store_true",
                    help="offline: show tools/sources; optionally run a preset without a model")
    ap.add_argument("--source", help="(dry-run) run a named source preset deterministically")
    ap.add_argument("--limit", type=int, default=5, help="(dry-run --source) max posts")
    args = ap.parse_args(argv)

    if args.dry_run:
        print("Extractor agent tools (exposed to the LangChain / Agent Framework agent):")
        for fn in actions.ACTIONS:
            summary = (fn.__doc__ or "").strip().splitlines()[0]
            print(f"  - {fn.__name__}: {summary}")
        print()
        print(actions.list_sources())
        if args.source:
            print(f"\nRunning preset {args.source!r} (limit {args.limit}) ...\n")
            print(actions.extract_source(args.source, args.limit))
        return 0

    prompt = " ".join(args.prompt).strip()
    if not prompt:
        ap.error("provide a natural-language prompt, or use --dry-run")
    try:
        if args.framework == "maf":
            from .agent import run  # deferred: imports agent_framework only in live mode
            print(asyncio.run(run(prompt)))
        else:
            from .langchain_agent import run  # deferred: imports langchain only in live mode
            print(run(prompt))
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
