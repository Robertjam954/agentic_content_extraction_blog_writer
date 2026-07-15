---
name: Agentic Content Extraction Blog Writer
description: A multiagent content pipeline that ingests YouTube transcripts, scraped course pages, and skill notes into an Obsidian-style knowledge graph inbox, from which agents (specified, in progress) draft concept-first blog posts.
languages:
- python
page_type: sample
urlFragment: agentic-content-extraction-blog-writer
---
<!-- YAML front-matter schema: https://review.learn.microsoft.com/en-us/help/contribute/samples/process/onboarding?branch=main#supported-metadata-fields-for-readmemd -->

# Agentic Content Extraction Blog Writer

## Table of Contents

- [User story](#user-story)
  - [About this repo](#about-this-repo)
  - [When should you use this repo?](#when-should-you-use-this-repo)
  - [Key features](#key-features)
  - [Target end users](#target-end-users)
  - [Industry scenario](#industry-scenario)
- [Architecture](#architecture)
  - [Outputs](#outputs)
- [Run](#run)
  - [Pre-requisites](#pre-requisites)
  - [Tools and libraries used](#tools-and-libraries-used)
  - [Required licenses](#required-licenses)
  - [Pricing considerations](#pricing-considerations)
  - [Run instructions](#run-instructions)
  - [Verifying the run](#verifying-the-run)
- [Automated self-documentation](#automated-self-documentation)
- [Supporting documentation](#supporting-documentation)
  - [Resource links](#resource-links)
  - [Licensing](#licensing)
- [Disclaimers](#disclaimers)

## User story

### About this repo

A multiagent content pipeline, built module by module against reference specs:
a curated list of YouTube videos (as transcripts) and personal notes flows into
an Obsidian knowledge graph, and concept-first blog posts are drafted from that
graph. A self-documenting agent keeps the project's own docs current.

What runs today is the ingestion layer: three Python scripts that land raw
material in `Inbox/`. The processing agents, the vault folders they operate on
(`Resources/`, `Projects/`, `Areas/`, `Archives/`), and the blog writer are
working specs in the module subfolders, marked (target) below. The weekly
documentation workflow is installed and live.

This README is updated at the end of each working session and verified by the
automated Monday documentation workflow.

### When should you use this repo?

Use it as a worked example of a spec-driven agentic pipeline: ingestion scripts
feeding a PARA-style Obsidian vault, agent briefs for transcript processing and
knowledge-graph hygiene, a strict content-writing prompt, and a self-documenting
loop that keeps CLAUDE.md, TODO.md, and this README honest. It is a portfolio
build to adapt to your own sources and blog stack, not a packaged product.

### Key features

Implemented (runnable today):

- **`scripts/fetch_transcripts.py`** - fetches YouTube transcripts (via
  `youtube-transcript-api`, preferring manual English tracks) and writes one
  clean text file per video to `Inbox/Transcripts_to_Process/<video_id>.txt`
  with a `Title:` / `Source:` / `Video ID:` header. Dedupes by video ID.
- **`scripts/scrape_courses.py`** - scrapes public zerotocloud (Teachable)
  course sales pages and writes one Markdown note per page to
  `Inbox/Web_to_Process/<slug>.md` with frontmatter, an overview, and the full
  curriculum outline. Paid lesson content behind the paywall is not captured.
- **`scripts/extract_skills.py`** - reads locally installed Azure skills from
  the gitignored `.claude/skills/<name>/SKILL.md` cache and writes one Markdown
  note per skill to `Inbox/Skills_to_Process/<name>.md`, carrying over the
  skill's frontmatter plus GitHub provenance.
- **Weekly documentation automation** - `.github/workflows/update-claude-md.yml`
  runs every Monday (09:00 UTC): verifies CLAUDE.md and this README against the
  codebase, regenerates the prioritized `TODO.md`, and opens a PR.

Specified, not yet implemented (target):

- **Transcript processing agent**
  (`obisidian-knowledge-graph/Agents/Agents/transcript_processing_agent.md`) -
  converts each raw transcript into a structured, block-ID-annotated note in
  `Resources/Processed_Transcripts/` and archives the raw file.
- **Vault connectivity agent**
  (`obisidian-knowledge-graph/Agents/Agents/vault_connectivity_agent.md`) -
  audits the vault for orphaned or weakly linked notes, creates missing
  concept/hub/technology nodes, merges duplicates, and enforces bidirectional
  links.
- **Content writing agent**
  (`notion-db-to-technical-blog/notion-db-to-technical-blog.md`) - turns a
  structured content object from the graph into a concept-first, ~700-word blog
  post with valid frontmatter and mandatory source/community links.
- **Self-documenting agent, ADR half**
  (`obisidian-knowledge-graph/Agents/Agents/self-documenting-ai-agent/README.md`) -
  generates Architecture Decision Records from code diffs. The CLAUDE.md
  verification half is the installed weekly workflow above.

### Target end users

Software engineers, data scientists, recent CS graduates, and founders who can
code and want production-ready AI engineering skills (the "Professional Seeking
AI Mastery" persona in the Module 2 spec), and content creators converting
watched videos and scattered notes into a knowledge base and blog posts.

### Industry scenario

Developer-education content pipeline and personal knowledge management: a solo
creator turns long, linear source material (talks, tutorials, course outlines,
personal notes) into a linked knowledge graph and reusable blog drafts. This is
a portfolio build demonstrating the pattern end to end.

## Architecture

```
 SOURCES                       INGESTION (implemented)          CAPTURE ZONE
+---------------------+       +--------------------------+    +--------------------------+
| YouTube videos      |------>| fetch_transcripts.py     |--->| Inbox/                   |
| (URLs / IDs)        |       +--------------------------+    |  Transcripts_to_Process/ |
+---------------------+       +--------------------------+    |  Web_to_Process/         |
| Course sales pages  |------>| scrape_courses.py        |--->|  Skills_to_Process/      |
| (zerotocloud)       |       +--------------------------+    +------------+-------------+
+---------------------+       +--------------------------+                 |
| .claude/skills/     |------>| extract_skills.py        |                 v
| cache (gitignored)  |       +--------------------------+    +--------------------------+
+---------------------+                                       | PROCESSING AGENTS        |
| Personal notes      |--- (note import, target) ------------>| (target - specs only)    |
+---------------------+                                       |  transcript processing   |
                                                              |  vault connectivity      |
                                                              +------------+-------------+
                                                                           |
                                                                           v
                              +--------------------------+    +--------------------------+
                              | BLOG POSTS (target)      |<---| OBSIDIAN VAULT (target)  |
                              | ~700-word concept-first  |    | Resources/ Projects/     |
                              | drafts w/ frontmatter    |    | Areas/ Archives/         |
                              | via content writing agent|    | (knowledge graph)        |
                              +--------------------------+    +--------------------------+

 SELF-DOCUMENTATION LOOP (live)
+-----------------------------+     +------------------------------------------+
| End-of-session doc updates  |---->| CLAUDE.md / TODO.md / README.md          |
+-----------------------------+     | kept honest                              |
| Monday workflow:            |---->| (drift fixed, TODO re-prioritized,       |
| update-claude-md.yml        |     |  changes land as a PR)                   |
+-----------------------------+     +------------------------------------------+
```

Raw material enters through the three ingestion scripts (personal-note import
is still target) and lands in `Inbox/`, the vault's capture zone. From there
the specified agents (target) would build structured notes and a linked
Obsidian vault, and the content writing agent (target) would draft posts from a
structured content object assembled from the graph. Independently, session
updates plus the Monday workflow keep CLAUDE.md, TODO.md, and this README
aligned with the code.

### Outputs

Produced today:

- `Inbox/Transcripts_to_Process/<video_id>.txt` - raw YouTube transcripts (5 present).
- `Inbox/Web_to_Process/<slug>.md` - scraped course-overview notes (15 present).
- `Inbox/Skills_to_Process/<name>.md` - extracted Azure skill notes (28 present).
- `TODO.md` - machine-refreshed weekly backlog at the repo root.

Target (specified, not yet produced in this repo):

- `Resources/Processed_Transcripts/*.md` - structured notes with receipts and block IDs.
- Concept/hub/technology nodes and audit logs across the vault folders.
- Markdown blog post drafts with frontmatter.
- `docs/adr/*.md` - Architecture Decision Records.

## Run

### Pre-requisites

- Python 3. The scripts are stdlib-first CLIs that resolve the repo root from
  their own path, so they run from anywhere.
- `youtube-transcript-api` (v1.x) for `fetch_transcripts.py` - the only
  third-party dependency, pinned in `requirements.txt` at the repo root:
  `pip install -r requirements.txt`.
- `curl` on PATH - `fetch_transcripts.py` and `scrape_courses.py` shell out to
  curl as a TLS-interception workaround.
- For `extract_skills.py` only: a populated local `.claude/skills/` cache
  (skills from github.com/microsoft/azure-skills). The cache is gitignored; on
  a fresh clone the script reports FAIL per skill until it is installed.

### Tools and libraries used

- Python 3 standard library plus `youtube-transcript-api` (pinned in
  `requirements.txt`).
- Markdown/YAML for all specs, notes, and frontmatter.
- GitHub Actions running `anthropics/claude-code-action` for the weekly
  documentation workflow.
- (Target) Obsidian as the knowledge-graph host; `rg` and `fd` as the agents'
  CLI query tooling.

### Required licenses

None to run the scripts. The weekly workflow needs the `CLAUDE_CODE_OAUTH_TOKEN`
repository secret (generated with `claude setup-token` from a Claude
subscription).

### Pricing considerations

The scripts run locally at no cost; this repo provisions no cloud resources.
The weekly workflow consumes Claude usage under its OAuth token's subscription,
plus GitHub Actions minutes.

### Run instructions

```bash
# Fetch YouTube transcripts (URLs or bare 11-char IDs; and/or --file urls.txt)
python3 scripts/fetch_transcripts.py URL_OR_ID [URL_OR_ID ...]
python3 scripts/fetch_transcripts.py --file urls.txt

# Scrape course sales pages (no args = the 15-URL default set in DEFAULT_URLS)
python3 scripts/scrape_courses.py [URL ...]

# Extract installed Azure skills (no args = the 28-skill MANIFEST_SKILLS set)
python3 scripts/extract_skills.py [NAME ...]
```

Each script is idempotent (existing output files are skipped) and exits 1 if
any item failed, 0 otherwise.

### Verifying the run

A successful run means files appear in the matching `Inbox/` subfolder:

- `fetch_transcripts.py` -> `Inbox/Transcripts_to_Process/<video_id>.txt`
- `scrape_courses.py` -> `Inbox/Web_to_Process/<slug>.md`
- `extract_skills.py` -> `Inbox/Skills_to_Process/<name>.md`

Each script prints a per-item OK/SKIP/FAIL line. Do not hand-edit anything
under `Inbox/`; it is raw input for the (target) processing agents.

## Automated self-documentation

This repository keeps its own documentation current on a fixed loop:

- End of every working session: CLAUDE.md, this README, `requirements.txt`, and any affected prep docs are updated to match reality.
- Every Monday at 09:00 UTC: the GitHub Actions workflow [`update-claude-md.yml`](.github/workflows/update-claude-md.yml) runs Claude Code with the prompt in [`claude-md-review-prompt.md`](.github/workflows/claude-md-review-prompt.md). It verifies CLAUDE.md and this README against the code, checks `requirements.txt` against actual imports, regenerates the prioritized [TODO.md](TODO.md), and opens a pull request with any corrections. It can also be triggered manually from the Actions tab.
- The workflow requires the `CLAUDE_CODE_OAUTH_TOKEN` repository secret (generate with `claude setup-token`).

## Supporting documentation

### Resource links

- [PRODUCT.md](PRODUCT.md) - what this is and the problem it solves.
- [ARCHITECTURE.md](ARCHITECTURE.md) - components, data flow, module map.
- [CONTRIBUTING.md](CONTRIBUTING.md) - the plan-then-implement workflow.
- [CLAUDE.md](CLAUDE.md) - the operating manual for agent sessions.
- [AGENTS.md](AGENTS.md) - the agent roster and briefs index.
- [TODO.md](TODO.md) - the machine-refreshed weekly backlog.
- [context-engineering-workflow.md](context-engineering-workflow.md) - Module 1 reference.
- [obisidian-knowledge-graph/](obisidian-knowledge-graph/) - Module 2 spec (the folder-name typo is intentional).
- [notion-db-to-technical-blog/](notion-db-to-technical-blog/) - Module 3 spec.
- [claude-md-memory-workflow/](claude-md-memory-workflow/) - Module 4 teaching example (do not modify).
- External: [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/),
  [microsoft/azure-skills](https://github.com/microsoft/azure-skills),
  [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action).

### Licensing

This repository does not currently include a LICENSE file. Reference material
in the module subfolders retains its upstream provenance.

## Disclaimers

Sample/portfolio code, provided as-is with no warranty. You are responsible for
any costs from cloud resources or API usage you configure (for example, the
Claude subscription behind the weekly workflow). The repo contains no secrets
or sensitive personal data; scraping covers public sales pages only, and
transcripts link back to their sources rather than redistributing video
content.
