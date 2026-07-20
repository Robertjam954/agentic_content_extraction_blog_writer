# Architecture

## Overview

This system is an agentic content pipeline. Agents gather docs from various sources
(websites, notes, blogs, papers, transcripts) into an Obsidian vault that serves as the
connected knowledge graph and RAG store; a writing/summary agent then generates a
structured summary that is uploaded to Notion for human review before publishing. A
separate documentation agent keeps the project's own context current.

The repository is being built module by module. The reference prompts and agent
briefs in the subfolders are the behavioral spec; the implementation realizes them.
Concrete tooling (languages, libraries, services) is chosen when each module is built
and recorded in that module's plan, so this document describes the logical
architecture and the component contracts rather than a fixed stack.

## Components

### Ingestion (built)

Ingestion is implemented as four idempotent Python scripts in `scripts/`, each
landing raw material in its own `Inbox/` subfolder and skipping inputs already there:

- **Transcript acquisition** (`scripts/fetch_transcripts.py`). Takes YouTube URLs or
  11-char IDs (as arguments or via `--file`), fetches each transcript with
  `youtube-transcript-api`, and writes `Inbox/Transcripts_to_Process/<video_id>.txt`
  with a title/source header. Filenames keep the raw video ID (including any dashes)
  so IDs remain matchable downstream.
- **Skill extraction** (`scripts/extract_skills.py`). Reads locally installed Azure
  skills from `.claude/skills/<name>/SKILL.md` (a local cache sourced from
  `github.com/microsoft/azure-skills`; `.claude/` is gitignored) and writes
  provenance-stamped Markdown notes to `Inbox/Skills_to_Process/`.
- **Course-page scraping** (`scripts/scrape_courses.py`). Scrapes public zerotocloud
  (Teachable) course pages - title, overview, price, and curriculum outline only, no
  paid content - to frontmattered Markdown in `Inbox/Web_to_Process/`. Standard
  library only; fetches via `curl`.
- **Paper acquisition** (`scripts/fetch_semantic_scholar.py`). Fetches papers from the
  Semantic Scholar Graph API by search query or paper ID (`DOI:`, `ARXIV:`,
  `CorpusId:`, or an S2 id) and writes Obsidian-native notes to
  `Inbox/Papers_to_Process/`: YAML frontmatter (title, authors, year, venue, doi,
  arxiv, citations, links), a `#paper` tag, author and field-of-study wikilinks, and
  the TL;DR and abstract. Standard library + `curl`; honors `S2_API_KEY` and backs off
  on the shared pool's HTTP 429. `--outdir` can target an Obsidian vault directly.

Still planned for this stage:

- **Note import.** Notes exported from other apps, converted to Markdown for the
  vault. The `obsidian-importer` plugin (reference copy at
  `github_clones/example_projects/_agentic_blog_obsidian-importer_template`) is the
  path for importing Apple Notes, Evernote, Notion, Google Keep, OneNote, Roam, and
  HTML into the vault; the pipeline's own extractors already emit Obsidian-native
  Markdown, so their output needs no conversion.

### Knowledge graph (the Obsidian vault) - planned

The vault is both the human-browsable knowledge base and the retrieval store the
writing agent reads from. It follows a PARA-style folder model
(`vault_structure_overview.md`): an `Inbox/` for raw material, `Resources/` for
processed notes, `Projects/` for human-authored core nodes (treated as read-only by
agents), plus concept, hub/MOC, and technology nodes. Graph structure is expressed
with Obsidian wikilinks, embeds, block IDs, and front matter.

Today only the `Inbox/` exists (populated by the ingestion scripts); `Resources/`,
`Projects/`, and the graph nodes are created when the processing agents are built.

### Agents (briefs are the spec; the content writing agent is partially built)

- **Transcript processing agent**
  (`obisidian-knowledge-graph/Agents/Agents/transcript_processing_agent.md`).
  Ingests transcripts from `Inbox/Transcripts_to_Process` and produces structured,
  block-ID-annotated notes in `Resources/Processed_Transcripts` following a fixed
  scaffold (Context Snapshot, Core Thesis, Architecture & Environment, Key Insights &
  Receipts, Workflow Recipes, Content Plays, and so on).
- **Vault connectivity agent**
  (`obisidian-knowledge-graph/Agents/Agents/vault_connectivity_agent.md`). Audits the
  whole vault for linking gaps, creates missing concept/hub/technology nodes, merges
  duplicates, and enforces bidirectional backlinks. A CLI query playbook in
  `AGENTS.md` (using `rg` and `fd`) supports inventory and link validation.
- **Content writing agent**
  (brief: `notion-db-to-technical-blog/notion-db-to-technical-blog.md`; code: `writer/`).
  Transforms a structured content object (Content Topic, Hook/Introduction, Key
  Insights, SEO Keywords, Source Video, Transcript) into a concept-focused post under
  strict output rules: valid frontmatter, no code or implementation detail, ~700 words,
  and a mandatory two-link call to action. The `writer/` package implements this:
  `writer/content_object.py` builds the content object from `rag.search()` (topic ->
  retrieved chunks -> Key Insights, Source Video, context), and `writer/agent.py` sends
  the brief as the system prompt plus that object to Claude (`claude-sonnet-5`).
  `python -m writer "topic" --dry-run` shows the retrieval and assembled object without
  calling the API.
- **Self-documenting agent** (`claude-md-memory-workflow/` and
  `obisidian-knowledge-graph/Agents/Agents/self-documenting-ai-agent/`). Re-analyzes
  the codebase to keep `CLAUDE.md` accurate and generates Architecture Decision
  Records from `git diff main`.

### Retrieval (RAG index over notes and docs) - built

A `rag/` Python package maintains a persistent vector index of the project's notes and
docs so agents can retrieve passages by meaning, not just by wikilink traversal.

- **Store.** A persistent ChromaDB collection (`notes_and_docs`) under `.rag/`
  (gitignored). Embeddings are local by default (sentence-transformers MiniLM via
  Chroma's `DefaultEmbeddingFunction`), so indexing and search need no API key and no
  data leaves the machine; the embedder is swappable in `rag/store.py`.
- **Indexing** (`rag/index.py`, `python -m rag index`). Walks the repo for `.md`,
  `.txt`, and `.srt` files (Inbox material, agent briefs, project docs), parses each
  file's title/source from YAML frontmatter or the transcript header, splits the body
  into overlapping paragraph-aware chunks, and upserts them with metadata
  (`source_path`, `title`, `source_type`, `source_url`, `chunk`). It is idempotent:
  a file's chunks are re-keyed and rewritten on each run.
- **Search** (`rag/search.py`, `python -m rag search "..."`). Returns the top-k chunks
  by cosine similarity, optionally filtered to one `source_type`
  (transcript / skill / web / doc / brief). This is the retrieval surface the content
  writing agent draws on, and is portable to `backend/app/rag/` in the app template.

Retrieval is two-tier:

- **Lightweight `rag/` (built).** The programmatic index above, called by `writer/`.
- **Obsidian RAG via knowledge-rag (`obsidian-rag/`, built).** A local hybrid-search
  MCP server (BM25 + ONNX `fastembed` vectors + cross-encoder reranking, no API keys)
  that Claude Code queries natively with `search_knowledge(...)` - so Claude uses the
  Obsidian graph as its local knowledge. The engine (installed at
  `github_clones/infra and deployment/local_rag/local_claude_knowledge_rag_search`) is
  pointed at the vault by `obsidian-rag/config.yaml`; its index (built - 95 files /
  1123 chunks) and model cache live under `obsidian-rag/` (gitignored). The one
  remaining step is registering the MCP server with Claude Code - see
  `obsidian-rag/README.md`. The two tiers share the same vault content; `rag/` serves
  programmatic callers, knowledge-rag serves interactive Claude Code sessions with
  reranked hybrid search.

### Review output (Notion) - `notion_review/`

The final stage. A structured summary (from the writing/summary agent) is pushed to a
Notion database as a **review card** (`notion_review/upload.py`, `create_review_page`),
where a human approves or edits it before it becomes a published post.
`python -m notion_review --dry-run` prints the Notion payload offline; a live upload needs
`notion-client`, `NOTION_TOKEN`, and `NOTION_REVIEW_DB`. Notion is the review surface, not
a source (the original `notion-db-to-technical-blog` reference used Notion as the source;
here it is the destination).

## Data flow

```
various sources (websites, notes, blogs, papers, transcripts)
  -> ingestion scripts (scripts/)                   [fetch + normalize to Markdown]
  -> Inbox/ -> Obsidian vault (the RAG store)
  -> rag/ index (embeddings of notes + docs) + obsidian-rag (hybrid search)
  -> structured summary (writing/summary agent, grounded via search)
  -> Notion review card (notion_review/ -> human review)
  -> approved -> published post
```

Independently, the self-documenting agent reads code diffs to keep `CLAUDE.md` current
and emit ADRs. Retrieval works two complementary ways: the Obsidian vault gives
human-browsable structure via wikilinks and block references, while the `rag/`
ChromaDB index gives semantic search over the same notes and docs. Each chunk carries
its `source_path` back to the file it came from, so what the writing agent retrieves
stays inspectable rather than opaque.

## Module map

The four build modules map onto the components above. Each has a reference video to
watch before implementing, and each module records its own concrete tooling decisions.

| Module | Folder | Builds | Status |
| --- | --- | --- | --- |
| 1. Context engineering | `context-engineering-workflow.md` | This doc set, the instructions file, and the plan-then-implement workflow | Built |
| 2. Knowledge graph extraction | `obisidian-knowledge-graph/`, `scripts/` | Ingestion + transcript processing + vault connectivity agents | Partially built - ingestion scripts done, agents spec-only |
| 3. Blog generation | `notion-db-to-technical-blog/`, `writer/`, `rag/`, `notion_review/` | Content writing agent and the content-object contract | Partially built - retrieval, content-object assembly, Claude drafting, and Notion review card run (live calls need API keys) |
| 4. Documentation automation | `claude-md-memory-workflow/` | Self-documenting agent + scheduled CLAUDE.md workflow | Partially built - initial `CLAUDE.md` exists; the scheduled workflow is not installed |

## Key technologies and decisions

Decisions are deferred to the module that needs them. Candidate technologies, drawn
from the reference assets:

- **Authoring formats:** Markdown and YAML for notes, agent briefs, and frontmatter.
- **Knowledge graph host:** Obsidian (wikilinks, embeds, block IDs, front matter).
- **Agent runtime:** an AI coding/agent tool such as Claude Code or the Claude Agent
  SDK; the reference also uses GitHub Copilot / VS Code custom agents.
- **Ingestion (decided, Module 2):** Python 3 scripts in `scripts/` -
  `youtube-transcript-api` for transcripts, standard library + `curl` for the skill
  and course-page extractors. `obsidian-importer` remains the candidate for the
  planned note-import path.
- **CLI tooling used by agents:** `rg` (ripgrep) and `fd` for search and inventory.
- **Content source contract:** a structured content object (the reference pulls this
  from a Notion database; the implementing module decides the actual source).
- **Blog target:** a static site (the reference CLAUDE.md prompt assumes Astro, e.g.
  `astro.config.mjs` and content collections).
- **Documentation automation:** GitHub Actions running `claude-code-action` on a
  schedule to open a PR with the updated `CLAUDE.md`.

When a module commits to a specific tool, record it in that module's plan and, if it
shapes the system, reflect it back here.
