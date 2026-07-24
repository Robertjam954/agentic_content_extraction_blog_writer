# Agentic Content Extraction & Blog Writer

A multiagent content pipeline. Agents gather docs from various sources (websites, notes,
blogs, papers, video transcripts) into a connected Obsidian knowledge graph that doubles
as the RAG store, then a summary agent produces a structured summary that is uploaded to
Notion for human review before publishing. A self-documenting agent keeps the project's
own documentation current.

- **What it does and why:** [PRODUCT.md](PRODUCT.md)
- **How it fits together:** [ARCHITECTURE.md](ARCHITECTURE.md)
- **How to work on it:** [CONTRIBUTING.md](CONTRIBUTING.md)

## Module status

The system is built module by module. The reference prompts and agent briefs in the
module subfolders are the behavioral spec; implementation catches up to them one
module at a time. Current state:

| Module | Folder | Status |
| --- | --- | --- |
| 1. Context engineering | root docs, `.github/copilot-instructions.md`, `context-engineering-workflow.md` | **Built** - the doc set, instructions file, and plan-then-implement workflow are in place |
| 2. Knowledge graph extraction | `scripts/`, `Inbox/`, `obisidian-knowledge-graph/` | **Partially built** - the three ingestion scripts work and raw material has landed in `Inbox/`; the transcript processing and vault connectivity agents are still spec-only briefs, and no processed notes or vault graph exist yet |
| 3. Summary + review | `writer/`, `rag/`, `notion_review/`, `notion-db-to-technical-blog/` | **Partially built** - `writer/` retrieves from `rag/`, assembles the content object, and drafts via Claude; `notion_review/` pushes a structured summary to Notion for review. Retrieval/assembly and the Notion payload run offline (dry-run); a live draft needs an API key and a live upload needs a Notion token |
| 4. Documentation automation | `claude-md-memory-workflow/` | **Spec only** - the CLAUDE.md workflow is a reference copy, not installed under `.github/workflows/`, and no `CLAUDE.md` exists yet. A separate weekly dependency-refresh action *is* installed |
| (support) Obsidian RAG for Claude | `obsidian-rag/` | **Built** - the local knowledge-rag MCP server is installed and the vault is indexed; MCP registration with Claude Code is the last step |

## What exists today

- **Ingestion scripts (Module 2), Python, run from the repo root:**
  - `scripts/fetch_transcripts.py` - fetches YouTube transcripts (by URL or ID) and
    writes them to `Inbox/Transcripts_to_Process/`, one `.txt` per video ID with a
    title/source header.
  - `scripts/extract_skills.py` - converts locally installed Azure skills
    (`.claude/skills/<name>/SKILL.md`, not committed) into provenance-stamped Markdown
    notes in `Inbox/Skills_to_Process/`.
  - `scripts/scrape_courses.py` - scrapes public zerotocloud (Teachable) course pages
    (title, overview, price, curriculum outline; no paid content) to Markdown in
    `Inbox/Web_to_Process/`.
  - `scripts/fetch_semantic_scholar.py` - fetches papers from the Semantic Scholar
    Graph API (by query or `DOI:`/`ARXIV:`/`CorpusId:`/S2 id) into
    `Inbox/Papers_to_Process/` as Obsidian-native notes (frontmatter, `#paper` tag,
    author/field wikilinks, TL;DR + abstract). Set `S2_API_KEY` for higher rate limits.
  - `scripts/scrape_articles.py` - source-agnostic blog/article/docs extractor. Four
    discovery modes (RSS/Atom feed, XML sitemap with `--match`, HTML listing page, or
    explicit URLs) plus named presets (`anthropic-engineering`, `anthropic-news`,
    `openai-research`, `openai-news`, `ms-learn-secure-research`, `hbc-intro-to-r`).
    Fetches each post, converts the main content to Markdown, and writes an Obsidian
    note to `Inbox/Web_to_Process/`. Blocked hosts fall back to the feed summary.
  - `scripts/fetch_youtube_channel.py` - resolves a YouTube handle/URL/ID to its
    channel ID, reads the channel's public uploads RSS feed, and fetches recent
    transcripts via `fetch_transcripts.py`. `--list` prints video IDs (no deps).
  - `scripts/fetch_gdoc.py` - extracts a public or "published to web" Google Doc to a
    Markdown note in `Inbox/Web_to_Process/` (no auth; private docs are reported
    inaccessible rather than saving a sign-in page).

  All are idempotent: inputs already in the inbox are skipped. Stdlib + curl only,
  except `fetch_transcripts.py` (needs `youtube-transcript-api`).
- **Content extraction agent (`extractor_agent/`):** wraps the extractors as agent
  tools so extraction runs from a natural-language prompt. Default framework is
  **LangChain** (LangChain + LangGraph); **Microsoft Agent Framework** is an option
  (`--framework maf`). `python -m extractor_agent --dry-run` lists the tools/sources
  offline; a live run
  (`python -m extractor_agent "extract the 5 latest anthropic engineering posts"`) is
  local-first: it uses a local **LM Studio** server by default
  (`http://localhost:1234/v1`), with **OpenAI** (`OPENAI_API_KEY`) and **Azure
  OpenAI** (`AZURE_OPENAI_ENDPOINT`) as options. The deterministic scripts never need
  a model.
- **Reusable Agent Skill (`skills/content-extraction/`):** a `SKILL.md` documenting
  the extractor toolset for coding agents, following the agentskills.io convention.
- **RAG index over notes and docs (`rag/`):** a persistent ChromaDB vector index with
  local (offline) embeddings. `python -m rag index` embeds the Inbox material, agent
  briefs, and project docs (66 files today); `python -m rag search "..."` returns the
  most relevant chunks by meaning, optionally filtered by source type. This is the
  retrieval surface for the writing agent.
- **Content writing / summary agent (`writer/`):** turns a topic into a draft. It
  retrieves from the `rag/` index, assembles the content object the writing brief
  expects, and sends it to Claude (`claude-sonnet-5`). `python -m writer "topic"
  --dry-run` shows the retrieval and assembled object offline; a live draft needs
  `anthropic` and `ANTHROPIC_API_KEY`.
- **Notion review output (`notion_review/`):** pushes a structured summary to a Notion
  database as a review card for a human to approve/edit. `python -m notion_review
  --dry-run` prints the Notion payload offline; a live upload needs `notion-client`,
  `NOTION_TOKEN`, and `NOTION_REVIEW_DB`.
- **Obsidian RAG (`obsidian-rag/`, built):** the local **knowledge-rag** MCP server
  (hybrid BM25 + ONNX vector + cross-encoder reranking) over the vault, so Claude Code
  uses the Obsidian graph as its local knowledge via `search_knowledge(...)`. Installed
  and indexed (95 files / 1123 chunks; embedding + reranker models cached under
  `obsidian-rag/`). Last step: register the MCP server with Claude Code - see
  `obsidian-rag/README.md`.
- **Raw material in `Inbox/`:** 5 video transcripts, 28 extracted skill notes, 15
  scraped course pages (and a `Papers_to_Process/` slot for Semantic Scholar fetches).
- **Reference agent briefs (the spec):** transcript processing, vault connectivity,
  and self-documenting agent briefs in `obisidian-knowledge-graph/`, the content
  writing prompt in `notion-db-to-technical-blog/`, and the CLAUDE.md workflow in
  `claude-md-memory-workflow/`.
- **Portfolio showcase (`site/`):** a static project page deployed to GitHub Pages by
  `.github/workflows/pages.yml`.
- **Automation (`.github/workflows/`):** `claude.yml` (an `@claude` responder),
  `weekly-maintenance.yml` (weekly `pip-compile` refresh -> PR), `pages.yml`, and
  `extract-content.yml` (weekly / on-demand run of the deterministic extractors that
  opens a PR with any new inbox notes; no model key needed).

## Stack

- **Python.** Ingestion scripts need only the standard library plus
  `youtube-transcript-api`. The `rag/` index adds `chromadb` with local (offline)
  embeddings. Verified on Python 3.14.
- **Retrieval.** `rag/` (ChromaDB, programmatic) plus the `obsidian-rag` **knowledge-rag**
  MCP engine (BM25 + ONNX `fastembed` vectors + cross-encoder reranking, all local).
- **Claude** (`anthropic`, `claude-sonnet-5`) for drafting; **Notion** (`notion-client`)
  as the human-review surface.
- **Obsidian conventions** (wikilinks, block IDs, frontmatter) for the knowledge graph.
- **GitHub Actions** for maintenance, the `@claude` responder, and Pages.

No stack is locked project-wide; each module records its concrete choices when it is
built (see `CONTRIBUTING.md`).

## How to run what exists

```bash
python -m venv .venv && source .venv/bin/activate
pip install "youtube-transcript-api>=1.0"   # or: pip install -r requirements.txt

# Fetch transcripts for one or more videos (URLs or 11-char IDs)
python3 scripts/fetch_transcripts.py https://youtu.be/VIDEO_ID
python3 scripts/fetch_transcripts.py --file urls.txt

# Scrape the default zerotocloud course pages (stdlib only, uses curl)
python3 scripts/scrape_courses.py

# Extract installed Azure skills (requires the skills under .claude/skills/)
python3 scripts/extract_skills.py

# Fetch papers from Semantic Scholar (by query or ID) into the vault
python3 scripts/fetch_semantic_scholar.py --query "retrieval augmented generation" --limit 10
python3 scripts/fetch_semantic_scholar.py ARXIV:2005.11401 DOI:10.18653/v1/2020.acl-main.1

# Extract blog posts / articles / docs (stdlib + curl only)
python3 scripts/scrape_articles.py --source anthropic-engineering --limit 15
python3 scripts/scrape_articles.py --source openai-research --limit 25
python3 scripts/scrape_articles.py --source ms-learn-secure-research
python3 scripts/scrape_articles.py --source hbc-intro-to-r
python3 scripts/scrape_articles.py --sitemap https://site/sitemap.xml --match /blog/

# Resolve a YouTube channel to recent uploads, then fetch transcripts
python3 scripts/fetch_youtube_channel.py @zenvanriel --list
python3 scripts/fetch_youtube_channel.py https://www.youtube.com/GitHub --limit 5

# Extract a public / published Google Doc
python3 scripts/fetch_gdoc.py https://docs.google.com/document/d/DOC_ID/edit

# Drive extraction in natural language (LangChain by default; --framework maf for MAF)
python3 -m extractor_agent --dry-run                 # offline: list tools + sources
pip install langchain langgraph langchain-openai
# local-first: start LM Studio, load a model, then (defaults to http://localhost:1234/v1)
python3 -m extractor_agent "extract the 5 latest anthropic engineering posts"
# or opt into a cloud backend: export OPENAI_API_KEY=...  (or AZURE_OPENAI_ENDPOINT=...)

# Build the RAG index over notes and docs, then search it
pip install chromadb
python3 -m rag index
python3 -m rag search "how does the transcript processing agent structure notes"

# Draft a summary grounded in the index (--dry-run needs no key)
python3 -m writer "building an AI knowledge graph in Obsidian" --dry-run
pip install anthropic && export ANTHROPIC_API_KEY=...   # for a live draft
python3 -m writer "building an AI knowledge graph in Obsidian" -o draft.md

# Preview the Notion review payload offline (live upload needs NOTION_TOKEN + NOTION_REVIEW_DB)
python3 -m notion_review --dry-run
```

The Obsidian RAG for Claude (`obsidian-rag/`) is installed and indexed; registering its
MCP server with Claude Code is the last step (`obsidian-rag/README.md`). The remaining
pipeline stages (transcript-processing + vault-connectivity agents, and documentation
automation) are planned - see the module status table and each module's folder for its
spec.

## Demo

<!--
Add a short screencast of the pipeline in action. To embed a video that plays inline
on GitHub:

  1. Record a clip (screen recording, ideally .mp4, kept under 100 MB).
  2. On github.com, open an issue, a pull request comment, or edit this README in the
     browser, and drag-and-drop the .mp4 into the text box. GitHub uploads it and
     inserts a URL like https://github.com/user-attachments/assets/<id>.
  3. Copy that URL and paste it below on its own line. GitHub renders it as an inline
     video player. Do not wrap it in Markdown image syntax.

Fallbacks if you would rather not use the drag-and-drop upload:
  - Commit an animated demo.gif to the repo and reference it: ![Demo](docs/demo.gif)
  - Or link a YouTube video behind a thumbnail:
    [![Demo](docs/demo-thumb.png)](https://youtu.be/VIDEO_ID)
-->

_Demo video coming soon - see the comment above for how to drop one in._

## Community

For more, [join the AI Engineering community](https://skool.com/ai-engineer).
