# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A multiagent content pipeline built module by module. Ingestion scripts gather raw
material (YouTube transcripts, Azure skill notes, scraped course pages, Semantic
Scholar papers) into `Inbox/`; an Obsidian vault is the intended connected knowledge
graph and RAG store; a writing agent drafts concept-first blog posts grounded in a
local RAG index; drafts are pushed to Notion for human review before publishing; and
a self-documenting agent (Module 4, not yet installed) is meant to keep this file
current.

**The reference prompts and agent briefs in the module subfolders are the behavioral
spec** - implementation catches up to them one module at a time. Treat the assets in
`obisidian-knowledge-graph/` (note the intentional folder spelling), `notion-db-to-technical-blog/`, and
`claude-md-memory-workflow/` as spec to implement, not files to rewrite casually.

Ground any work in the living docs: `PRODUCT.md` (vision and boundaries),
`ARCHITECTURE.md` (components, data flow, module map), `CONTRIBUTING.md` (workflow
and conventions), and `.github/copilot-instructions.md` (working rules). Update them
when a module changes how the system works.

## Commands

Everything runs from the repo root with Python 3 (verified on 3.14).

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt        # pinned lockfile; source list is requirements.in

# Ingestion (Module 2) - all four scripts are idempotent (existing inbox items are skipped)
python3 scripts/fetch_transcripts.py https://youtu.be/VIDEO_ID     # or --file urls.txt
python3 scripts/scrape_courses.py                                  # stdlib only, uses curl
python3 scripts/extract_skills.py                                  # needs .claude/skills/ (gitignored local cache)
python3 scripts/fetch_semantic_scholar.py --query "..." --limit 10 # or ARXIV:/DOI:/CorpusId: ids; S2_API_KEY optional

# RAG index over notes and docs (rag/, ChromaDB + local offline embeddings, no API key)
python3 -m rag index                   # (re)index Inbox material, agent briefs, project docs into .rag/
python3 -m rag search "query" [--type transcript|skill|web|doc|brief]

# Content writing agent (writer/)
python3 -m writer "topic" --dry-run    # retrieval + assembled content object, offline
python3 -m writer "topic" -o draft.md  # live draft; needs anthropic + ANTHROPIC_API_KEY

# Notion review output (notion_review/)
python3 -m notion_review --dry-run     # print the Notion payload offline
python3 -m notion_review               # live upload; needs notion-client + NOTION_TOKEN + NOTION_REVIEW_DB
```

Dependencies: edit `requirements.in` (the hand-edited source), then run `pip-compile`
to regenerate `requirements.txt`. Never edit `requirements.txt` directly - the weekly
maintenance workflow regenerates it.

There is no global test suite. Validation is per stage: run each script or module
against one or two real inputs and check its output against that module's success
criteria and quality checklist (see "How to run and test" in `CONTRIBUTING.md`).

## Architecture

Data flow:

```
sources -> scripts/ (fetch + normalize to Markdown) -> Inbox/<Type>_to_Process/
        -> Obsidian vault (knowledge graph; only Inbox/ exists so far)
        -> rag/ ChromaDB index + obsidian-rag hybrid-search MCP server
        -> writer/ (content object -> Claude draft)
        -> notion_review/ (review card in Notion -> human approval -> publish)
```

- **`scripts/`** - four idempotent ingestion scripts, each landing raw material in its
  own `Inbox/` subfolder (`Transcripts_to_Process/`, `Skills_to_Process/`,
  `Web_to_Process/`, `Papers_to_Process/`).
- **`rag/`** - persistent ChromaDB collection (`notes_and_docs`) under `.rag/`
  (gitignored), local MiniLM embeddings via Chroma's default embedding function.
  `rag/index.py` walks the repo for `.md`/`.txt`/`.srt`, chunks paragraph-aware
  (1200 chars, 200 overlap; see `rag/config.py`), upserts with metadata
  (`source_path`, `title`, `source_type`, `source_url`). `rag/search.py` is the
  retrieval surface `writer/` calls.
- **`writer/`** - `content_object.py` builds the content object the writing brief
  expects (topic -> `rag.search()` chunks -> Key Insights, Source Video, context);
  `agent.py` sends the brief (`notion-db-to-technical-blog/notion-db-to-technical-blog.md`,
  used verbatim as the system prompt) plus that object to Claude. Default model:
  `claude-sonnet-5` (`claude-sonnet-4-20250514` retired 2026-06-15 and now 404s).
- **`notion_review/`** - `upload.py:create_review_page` pushes the structured summary
  to a Notion database as a review card. Notion is the review destination here, not a
  source (unlike the original reference).
- **`obsidian-rag/`** - config and README for the local knowledge-rag MCP server
  (hybrid BM25 + ONNX vectors + cross-encoder reranking, fully local) over the vault;
  index and model caches are gitignored. Registering the MCP server with Claude Code
  is the remaining step. Two retrieval tiers share the same content: `rag/` serves
  programmatic callers, knowledge-rag serves interactive Claude Code sessions.
- **Agent briefs (spec-only)** - transcript processing and vault connectivity agents in
  `obisidian-knowledge-graph/Agents/Agents/`, plus the vault structure overview
  (PARA-style: `Inbox/`, `Resources/`, `Projects/` core nodes, concept/hub/technology
  nodes) and a CLI playbook (`rg`/`fd`) in `obisidian-knowledge-graph/AGENTS.md`.

Module status lives in the README's module-status table and `ARCHITECTURE.md`'s
module map; keep both in sync with reality when building.

## Automation (`.github/workflows/`)

- `claude.yml` - `@claude` mention responder on issues/PRs (`claude-code-action`).
- `weekly-maintenance.yml` - Mondays 09:00 UTC, runs `pip-compile --upgrade` and
  opens a PR (never commits to `main` directly).
- `pages.yml` - deploys the static showcase in `site/` to GitHub Pages on push to `main`.
- The scheduled CLAUDE.md-refresh workflow (`claude-md-memory-workflow/update-claude-md.yml`)
  is a Module 4 reference copy, **not installed**; installing it means copying it and
  its prompt file into `.github/workflows/` and adding a `CLAUDE_CODE_OAUTH_TOKEN`
  (or `ANTHROPIC_API_KEY`) secret.

## Conventions and working rules

- **No stack is locked project-wide.** Decide tooling per module, record it in that
  module's `*-plan.md`. Plan before implementing; keep planning, implementation, and
  review in separate sessions.
- **Use single hyphens, never em dashes**, in all written content.
- **Prefer accuracy over hypotheticals**: read files before editing; document what the
  code and content actually do.
- **Vault conventions:** underscore-separated TitleCased filenames with acronyms
  uppercase (AI, LLM, RAG); raw transcript dumps keep source-generated dashes so video
  IDs stay matchable. Every note links to at least two other notes and carries the
  `> Core Node: [[Projects/AI_Native_Engineer]]` footer. `Projects/` notes are
  human-authored and read-only for agents.
- **Blog content rules:** concept-first, ~700 words, no code/commands/step-by-step
  instructions, valid frontmatter with no colon in the title, close with both the
  source video link and the community link, avoid AI writing cliches.
- **Git:** branch from `main`; do not commit generated documentation directly to
  `main` (automation opens PRs for review). Keep changes focused on a single module.
  Commit or push only when asked.
