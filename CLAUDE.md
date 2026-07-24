# CLAUDE.md

Operating manual for Claude Code working in this repository. Keep this file 100%
truthful: if reality diverges, update this file, then the code. Companion prep docs:
[PRODUCT.md](PRODUCT.md), [ARCHITECTURE.md](ARCHITECTURE.md),
[CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), and
[.github/copilot-instructions.md](.github/copilot-instructions.md).

## 1. Project overview

**agentic_content_extraction_blog_writer** is a multiagent content pipeline (per
PRODUCT.md): a curated list of YouTube videos (as transcripts) and personal notes
flows into an Obsidian knowledge graph, and concept-first blog posts are drafted
from that graph. A self-documenting agent keeps the project's own docs current.

The build proceeds in four modules, each with a reference video (the five raw
transcripts in `Inbox/Transcripts_to_Process/` are those videos):

1. **Context engineering** - the prep-docs + plan-then-implement workflow
   (`context-engineering-workflow.md`). Done: this doc set exists.
2. **Knowledge graph extraction** - ingestion plus the transcript processing and
   vault connectivity agents (`obisidian-knowledge-graph/`). Ingestion scripts
   exist (`scripts/`); the agent runs over the vault are specified but the vault
   folders (`Resources/`, `Projects/`, etc.) are not in this repo yet (target).
3. **Blog generation** - the content writing agent
   (`notion-db-to-technical-blog/`). Prompt spec only; no implementation yet
   (target).
4. **Documentation automation** - the self-documenting agent and the weekly
   CLAUDE.md verification workflow (`.github/workflows/update-claude-md.yml`,
   installed; `claude-md-memory-workflow/` is the teaching example it derives from).

The module subfolders (`obisidian-knowledge-graph/`, `notion-db-to-technical-blog/`,
`claude-md-memory-workflow/`) contain working specs and prompts - the behavioral
spec this repo implements. Treat them as reference material, not code to rewrite
casually.

## 2. Repository layout

```
agentic_content_extraction_blog_writer/
├── README.md                        # Solution-accelerator-style README (front-matter, features, architecture, run)
├── PRODUCT.md ARCHITECTURE.md CONTRIBUTING.md CLAUDE.md AGENTS.md TODO.md
├── requirements.txt                 # Third-party deps for scripts/ (youtube-transcript-api only)
├── context-engineering-workflow.md  # Module 1 reference: VS Code context engineering guide
├── custom-automations.md            # Reference doc: claude-code-action automation examples
├── claude.yml                       # @claude responder workflow file (at root; see section 5)
├── create-app.html                  # Static HTML helper page: "Create Claude Code GitHub App"
├── scripts/                         # Module 2 ingestion scripts (see section 3)
│   ├── fetch_transcripts.py
│   ├── scrape_courses.py
│   └── extract_skills.py
├── Inbox/                           # Vault capture zone (see section 4)
│   ├── Transcripts_to_Process/      # 5 raw YouTube transcripts (.txt, named by video ID)
│   ├── Web_to_Process/              # 15 scraped course-overview notes (.md)
│   └── Skills_to_Process/           # 28 extracted Azure skill notes (.md)
├── obisidian-knowledge-graph/       # Module 2 spec (folder name typo is intentional)
│   ├── README.md                    # Video reference (dBebGUgiz34)
│   ├── AGENTS.md                    # Vault overview + rg/fd CLI query playbook
│   └── Agents/Agents/               # Agent briefs (see AGENTS.md at repo root)
├── notion-db-to-technical-blog/     # Module 3 spec
│   ├── README.md                    # Video reference (fbevy5gWDes)
│   └── notion-db-to-technical-blog.md  # Content writing agent prompt
├── claude-md-memory-workflow/       # Module 4 teaching example - DO NOT MODIFY
│   ├── README.md                    # Video reference (ohjMGnEaBxk)
│   ├── update-claude-md.yml         # Example workflow (illustration only)
│   └── claude-md-review-prompt.md   # Example prompt (illustration only)
└── .github/
    ├── copilot-instructions.md      # Copilot context file linking the prep docs
    └── workflows/
        ├── update-claude-md.yml     # Installed Monday verification workflow
        └── claude-md-review-prompt.md  # Prompt the workflow feeds to Claude
```

`.gitignore` excludes `.DS_Store` and `.claude/` (the local skills cache that
`extract_skills.py` reads from).

## 3. Scripts (Module 2 ingestion)

All three are stdlib-first Python 3 CLIs run from anywhere (they resolve the repo
root from their own path). Each is idempotent: existing output files are skipped.
Each exits 1 if any item failed, 0 otherwise.

### scripts/fetch_transcripts.py

- **What:** fetches YouTube transcripts and writes one clean `.txt` per video to
  `Inbox/Transcripts_to_Process/<video_id>.txt` with a `Title:` / `Source:` /
  `Video ID:` header. Prefers manual English tracks, falls back to any/generated.
  Titles come best-effort from YouTube's oEmbed endpoint (urllib, then curl
  fallback for TLS-intercepted environments).
- **Inputs:** YouTube URLs or bare 11-char IDs as args, and/or `--file urls.txt`
  (one per line). Dedupes by resolved video ID.
- **Run:** `python3 scripts/fetch_transcripts.py URL_OR_ID [...]` or
  `python3 scripts/fetch_transcripts.py --file urls.txt`
- **Requires:** `youtube-transcript-api` (v1.x) - the only third-party dependency
  in the repo, pinned in `requirements.txt` at the root
  (`pip install -r requirements.txt`).

### scripts/scrape_courses.py

- **What:** scrapes public zerotocloud (Teachable) course sales pages and writes
  one Markdown note per page to `Inbox/Web_to_Process/<slug>.md` with frontmatter
  (source_url, title, price, scraped date, type, source), an Overview section, and
  the full curriculum outline (sections + lecture names). Paid lesson content is
  behind the paywall and is NOT captured. Fetches via curl (not urllib) because of
  TLS interception on the authoring machine.
- **Inputs:** URLs as args, or no args to scrape the 15-URL default set hardcoded
  in `DEFAULT_URLS`.
- **Run:** `python3 scripts/scrape_courses.py [URL ...]`

### scripts/extract_skills.py

- **What:** reads locally installed Azure skills from `.claude/skills/<name>/SKILL.md`
  (sourced from github.com/microsoft/azure-skills, cache is gitignored) and writes
  one Markdown note per skill to `Inbox/Skills_to_Process/<name>.md`, carrying over
  the skill's own frontmatter fields plus GitHub provenance and a local-extras list.
- **Inputs:** skill names as args, or no args to extract the 28-skill
  `MANIFEST_SKILLS` set.
- **Run:** `python3 scripts/extract_skills.py [NAME ...]`
- **Gotcha:** fails per-skill with `FAIL ... (no local SKILL.md ...)` if the
  `.claude/skills/` cache is not populated on this machine.

### scripts/scrape_articles.py (blogs, news, docs, courses)

- **What:** one source-agnostic article extractor. Discovers posts via RSS/Atom
  `--feed`, path-filtered XML `--sitemap ... --match` (handles sitemap-index
  nesting), listing-page `--listing ... --match`, or explicit URLs/`--file`, then
  writes readable Markdown (from `<article>`/`<main>`) to
  `Inbox/Web_to_Process/<source>--<slug>.md`. Blocked pages (e.g. openai.com 403)
  fall back to feed summary, stamped `full_text: false`.
- **Presets** (`--source`): `anthropic-engineering`, `anthropic-news`,
  `openai-research`, `openai-news`, `ms-learn-secure-research`, `hbc-intro-to-r`.
  `--list` discovers without fetching; also `--limit`, `--type`, `--outdir`.

### scripts/fetch_youtube_channel.py (channels -> transcripts)

- **What:** resolves a channel `@handle`/URL/legacy `/Name`/`UC...` ID to its
  channel ID, reads the public uploads RSS feed, and hands video IDs to
  `fetch_transcripts.py`. `--list` prints resolved URLs with no dependency.
- **Gotcha:** transcript fetching inherits YouTube's cloud-IP blocking
  (`RequestBlocked`); run from an unblocked IP/proxy. Listing works regardless.

### scripts/fetch_gdoc.py (Google Docs)

- **What:** extracts a public ("anyone with the link") or "published to web" Google
  Doc to Markdown in `Inbox/Web_to_Process/`. Reports FAIL for private/sign-in docs
  rather than saving the login page. Private docs would need a Google API
  credential (target).

### scripts/ingest_files.py (local files)

- **What:** ingests local files into `Inbox/Files_to_Process/` as provenance-stamped
  notes (`source_file`, `sha256`, `type` frontmatter). Dispatch by extension: PDFs
  (text via `pypdf`; scanned/no-text PDFs get a reference note), Markdown/text, HTML
  (a Netscape/Mozilla bookmarks export becomes a link list, other HTML is converted
  to Markdown), source code (fenced block), and images/other binaries (copied into
  `Inbox/Files_to_Process/assets/` with an embedding/reference note). Idempotent
  (keyed by output filename). Accepts files or directories (recursive).
- **Requires:** `pypdf` for PDF text only; every other file type is stdlib-only.

### extractor_agent/ (natural-language orchestration)

- **What:** wraps the extractors above as agent tools so extraction runs from a
  prompt. Default framework is **LangChain** (`langchain_agent.py`, via
  `langchain.agents.create_agent`); **Microsoft Agent Framework** is an option
  (`agent.py`, `--framework maf`). `python3 -m extractor_agent --dry-run` lists
  tools/sources offline (no model). Local-first: the live agent defaults to a local
  **LM Studio** server (`http://localhost:1234/v1`); `OPENAI_API_KEY` or
  `AZURE_OPENAI_ENDPOINT` switch to a cloud backend. The deterministic scripts never
  need a model.
- **Skill:** `skills/content-extraction/SKILL.md` documents this toolset for coding
  agents (agentskills.io convention, from inspecting `cartesia-ai/skills`).

## 4. The Inbox pipeline

`Inbox/` is the vault's capture zone (see `vault_structure_overview.md`). Raw
material lands here and waits for the processing agents:

- `Inbox/Transcripts_to_Process/` - raw YouTube transcripts named `<video_id>.txt`
  (dashes in IDs are kept so the downstream agent can derive `youtube_id` from the
  filename). Currently holds the 5 module reference videos. The transcript
  processing agent consumes these into `Resources/Processed_Transcripts/` and
  archives the raw file - neither destination folder exists in this repo yet
  (target).
- `Inbox/Web_to_Process/` - scraped course-overview notes from `scrape_courses.py`
  plus blog/article/docs notes from `scrape_articles.py` and `fetch_gdoc.py`.
- `Inbox/Skills_to_Process/` - 28 Azure skill notes from `extract_skills.py`.
- `Inbox/Files_to_Process/` - notes from local files ingested by `ingest_files.py`
  (with an `assets/` subfolder holding copied images/binaries).

Everything currently in `Inbox/` is unprocessed. Do not hand-edit inbox content;
it is raw input for the agents.

## 5. GitHub automations

- **`.github/workflows/update-claude-md.yml`** (installed) - the Monday
  verification workflow. Every Monday 09:00 UTC (or via `workflow_dispatch`) it
  runs `anthropics/claude-code-action` with the prompt in
  `.github/workflows/claude-md-review-prompt.md`: verify CLAUDE.md against the
  codebase, fix only drift, regenerate `TODO.md`, and open a PR (direct commit to
  main only with the `skip_pr` input). Requires the `CLAUDE_CODE_OAUTH_TOKEN`
  repository secret (generate with `claude setup-token`).
- **`claude.yml`** (repo root) - an @claude responder workflow: on issue/PR
  comments, issue open/assign, or PR reviews containing `@claude`, it runs
  `anthropics/claude-code-action@v1` with `ANTHROPIC_API_KEY`. Note it sits at the
  repo root, so GitHub does not execute it; move it to `.github/workflows/` to
  activate it (target).
- **`.github/workflows/extract-content.yml`** - runs the deterministic content
  extractors (`scrape_articles.py`) weekly and via `workflow_dispatch` (choose a
  source preset and limit), committing any new `Inbox/` notes on a branch and
  opening a PR. Deterministic only: it never runs the LLM agent, so it needs no
  model key.
- **`claude-md-memory-workflow/`** - the teaching example the installed workflow
  is modeled on (from the Module 4 video). Illustration only; leave untouched.
- **`custom-automations.md`** - reference examples for prompt-driven
  claude-code-action automations; documentation, not an active workflow.

## 6. Conventions

- No em dashes anywhere - use a single hyphen `-` only. (Exception: raw transcript
  dumps and reference-asset content may keep source-generated characters.)
- No emojis in code or docs unless explicitly requested. (The reference prompt
  `notion-db-to-technical-blog.md` contains emojis; it is upstream source material,
  leave it as-is.)
- Markdown-first repo: the deliverables are Markdown specs, notes, and docs. Code
  lives in `scripts/` (ingestion) and the `extractor_agent/`, `rag/`, `writer/`,
  and `notion_review/` packages.
- Plan before implementing: each module gets a `*-plan.md` recording its stack
  decisions (see CONTRIBUTING.md). No stack is locked project-wide.
- Vault naming: underscore-separated, TitleCased filenames, acronyms uppercase
  (AI, LLM, RAG). Every vault note links to at least two others and carries the
  `> Core Node: [[Projects/AI_Native_Engineer]]` footer. `Projects/` notes are
  human-authored and read-only for agents.
- Blog output rules: concept-first, ~700 words, valid frontmatter with no colon in
  the title, no code/commands/step-by-step, ends with both the source video link
  and the community link.
- Read files before editing them; document what the code actually does; mark
  aspirational items as (target).

## 7. Gotchas

- **The folder is spelled `obisidian-knowledge-graph`** (not "obsidian"). The typo
  is existing/intentional - do not rename it; links and specs reference it as-is.
- **`claude-md-memory-workflow/` is teaching material** - never modify it. The
  live workflow lives in `.github/workflows/`.
- **`Inbox/` content is raw input** - the automation and doc passes must not edit
  it.
- **`claude.yml` at the root is inert** - GitHub only runs workflows under
  `.github/workflows/`.
- **`extract_skills.py` depends on a gitignored local cache** (`.claude/skills/`);
  on a fresh clone it will report FAIL for every skill until skills are installed.
- **`scrape_courses.py` and `fetch_transcripts.py` shell out to curl** as a TLS
  workaround; behavior may differ on machines without curl.
- **No tests** - the scripts have no test suite. The only third-party dependency
  is `youtube-transcript-api`, pinned in `requirements.txt`; run
  `pip install -r requirements.txt` before `fetch_transcripts.py`.
- **The vault itself is not in this repo.** Only `Inbox/` exists; `Resources/`,
  `Projects/`, `Areas/`, `Archives/` are described by the specs but not yet
  created (target).

## 8. Self-documentation protocol

This repository is self-documenting. Two mechanisms keep the docs honest:

1. **End of every session:** before finishing any working session that changed
   code, commands, dependencies, structure, or conventions, update CLAUDE.md (and
   the affected prep docs: README.md, PRODUCT.md, ARCHITECTURE.md, CONTRIBUTING.md,
   AGENTS.md) and `requirements.txt` (keep the dependency manifest in sync with the
   actual third-party imports in `scripts/`) so they match reality. Reality wins
   over stale documentation. This applies to human and agent sessions alike.
2. **Every Monday:** the `.github/workflows/update-claude-md.yml` workflow runs an
   automated verification pass (09:00 UTC). It re-analyzes the codebase, corrects
   any drift in CLAUDE.md and README.md that session updates missed, regenerates
   the prioritized `TODO.md` at the repo root, and opens a PR for review. It
   requires the `CLAUDE_CODE_OAUTH_TOKEN` repository secret (generate with
   `claude setup-token`).

`TODO.md` is machine-refreshed weekly: treat it as the current backlog, edit it
freely during the week, and expect the Monday run to re-prioritize it.
