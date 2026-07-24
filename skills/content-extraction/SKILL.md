---
name: content-extraction
description: Extract blog posts, articles, YouTube transcripts, and Google Docs into the Obsidian vault inbox (Inbox/) as provenance-stamped Markdown notes. Use when the user asks to ingest, scrape, or pull content from a blog, news feed, docs site, YouTube channel, or Google Doc into the knowledge graph, or to run the extraction agent. For processing already-ingested inbox notes into vault Resources, use the transcript-processing / vault-connectivity agent briefs instead.
compatibility: Python 3 standard library plus curl for all web extractors (no API key). fetch_transcripts.py additionally needs youtube-transcript-api and an IP YouTube does not block (cloud IPs are often blocked). ingest_files.py needs pypdf for PDF text (other file types are stdlib-only). The optional natural-language agent defaults to LangChain (langchain + langgraph + langchain-openai); Microsoft Agent Framework (agent-framework-core + agent-framework-openai) is an alternative via --framework maf. Local-first default backend is LM Studio (http://localhost:1234/v1), with OpenAI cloud (OPENAI_API_KEY) and Azure OpenAI (AZURE_OPENAI_ENDPOINT) as options.
---

# Content Extraction

Ingest external content into the vault capture zone (`Inbox/`) as Obsidian-native
Markdown notes with YAML frontmatter (`source_url`, `title`, `scraped`, `type`,
`source`). Every extractor is idempotent: an item already written to the inbox is
skipped. Notes land unprocessed for the downstream transcript-processing and
vault-connectivity agents, and are picked up by the `rag/` index.

## Core directives

- **Run from anywhere.** The scripts resolve the repo root from their own path and
  write into `Inbox/`. Point `--outdir` elsewhere to target a live vault.
- **Idempotent by design.** Re-running only fetches new items; do not delete notes
  to force a re-fetch unless the source changed.
- **Discovery beats hardcoding.** Prefer a source's RSS/Atom feed or XML sitemap
  over a hand-listed set of URLs; fall back to listing-page link extraction, then
  explicit URLs.
- **Full text is best-effort.** Some hosts (e.g. openai.com) return a bot wall
  (HTTP 403) for non-browser fetches. The article extractor then falls back to the
  feed summary and stamps `full_text: false`. This is expected, not a failure.
- **No em dashes, no emojis** in generated notes or code (repo convention).

## Extractors (scripts/)

### scrape_articles.py - blogs, news, docs, courses

One source-agnostic article extractor with five discovery modes and named presets.

- **Presets** (`--source`): `anthropic-engineering`, `anthropic-news`,
  `openai-research`, `openai-news`, `ms-learn-secure-research`, `hbc-intro-to-r`,
  `openai-api-reference`.
- **Discovery modes:** `--feed URL` (RSS/Atom), `--sitemap URL --match PATTERN`
  (path-filtered `<loc>`; handles sitemap-index nesting), `--listing URL --match
  PATTERN` (filtered `<a href>`), `--llms-txt URL --match PATTERN` (collects a
  site's Markdown twin pages listed in an `llms.txt` index; a stub twin falls back
  to the rendered HTML page), or explicit URLs / `--file`.
- **Output:** `Inbox/Web_to_Process/<source>--<slug>.md`, with the main content
  (`<article>`/`<main>`) converted to readable Markdown (headings, lists, links,
  code, blockquotes).
- **Flags:** `--limit N`, `--list` (discover only, no fetch), `--source-tag`,
  `--type`, `--outdir`.

```
python3 scripts/scrape_articles.py --source anthropic-engineering --limit 15
python3 scripts/scrape_articles.py --source openai-research --limit 25
python3 scripts/scrape_articles.py --source openai-api-reference
python3 scripts/scrape_articles.py --sitemap https://site/sitemap.xml --match /blog/
python3 scripts/scrape_articles.py --llms-txt https://site/llms.txt --match /docs/
python3 scripts/scrape_articles.py https://site/a-post https://site/another-post
```

### fetch_youtube_channel.py - channels -> transcripts

Resolves a channel handle/URL/ID to its channel ID, reads the public uploads RSS
feed (most recent ~15 uploads), and fetches each video's transcript into
`Inbox/Transcripts_to_Process/` via `fetch_transcripts.py`.

- Accepts `@handle`, `https://www.youtube.com/@handle/videos`, a legacy
  `/GitHub` custom URL, `/channel/UC...`, or a bare `UC...` ID.
- `--list` prints resolved video URLs without fetching (needs no dependency).
- Transcript fetching inherits `fetch_transcripts.py`'s limitation: YouTube blocks
  many cloud-provider IPs (`RequestBlocked`); run from an unblocked IP or a proxy.

```
python3 scripts/fetch_youtube_channel.py @zenvanriel --limit 5
python3 scripts/fetch_youtube_channel.py https://www.youtube.com/GitHub --list
```

### fetch_gdoc.py - Google Docs

Extracts a public or published Google Doc to Markdown in `Inbox/Web_to_Process/`.

- Doc shared "anyone with the link can view": exported via
  `.../export?format=html` (no auth).
- Doc "published to the web" (`/d/e/<id>/pub`): the published HTML is reduced to
  its body.
- A fully private doc returns a sign-in page; the script reports it inaccessible
  rather than saving the login page. Use the Google Docs API with a service
  account for private docs (out of scope here).

```
python3 scripts/fetch_gdoc.py https://docs.google.com/document/d/<id>/edit
```

### ingest_files.py - local files

Ingests local files into `Inbox/Files_to_Process/` as provenance-stamped notes
(`source_file`, `title`, `ingested`, `type`, `sha256` frontmatter). Use this for
material that arrives as files rather than URLs. Dispatch by extension:

- **PDF** (`.pdf`): text extracted with `pypdf`. A scanned/no-text PDF gets a
  reference note (`has_content: false`) instead of empty content.
- **Text** (`.md`, `.markdown`, `.txt`, `.rst`): content passed through.
- **HTML** (`.html`, `.htm`): a Netscape/Mozilla bookmarks export becomes one note
  listing its links; any other HTML is converted to Markdown.
- **Code** (`.py`, `.js`, `.ts`, `.sql`, `.r`, `.java`, `.go`, ...): a fenced block.
- **Images / other binaries** (`.png`, `.jpg`, `.vsdx`, ...): copied into
  `Inbox/Files_to_Process/assets/` with an embedding (images) or reference note.

Accepts files or directories (recursive). Idempotent by output filename.

```
python3 scripts/ingest_files.py paper.pdf notes.md bookmarks.html diagram.png
python3 scripts/ingest_files.py ~/Downloads --source attachment
```

## Natural-language agent (extractor_agent/)

`extractor_agent` wraps the extractors as agent tools so extraction can be driven in
natural language. The default framework is **LangChain** (LangChain framework +
LangGraph runtime, via `langchain.agents.create_agent`); **Microsoft Agent
Framework** (https://learn.microsoft.com/en-us/agent-framework/agents/) is an
alternative with `--framework maf`. The deterministic path needs no model; only the
live agent does.

```
python -m extractor_agent --dry-run                        # list tools/sources, offline
python -m extractor_agent --dry-run --source anthropic-engineering --limit 3
python -m extractor_agent "extract the 5 latest anthropic engineering posts"   # live (LangChain)
python -m extractor_agent --framework maf "extract latest 3 openai research posts"
python -m extractor_agent "ingest ~/Downloads/paper.pdf into the vault"
```

Live mode is local-first: it uses a local **LM Studio** server by default
(`LMSTUDIO_BASE_URL`, default `http://localhost:1234/v1`; load a model in LM Studio
and set `OPENAI_CHAT_MODEL_ID`/`LMSTUDIO_MODEL` to its id). It switches to **Azure
OpenAI** when `AZURE_OPENAI_ENDPOINT` is set, or **OpenAI cloud** when
`OPENAI_API_KEY` is set. Summaries of extracted content are published to Notion via
the existing `notion_review/` module; the vault stays the source of truth. With the
LangChain framework, set `LANGSMITH_API_KEY` + `LANGSMITH_TRACING=true` to trace
runs in LangSmith (optional, no code change).

## Automation

`.github/workflows/extract-content.yml` runs the deterministic extractors on a
schedule (weekly) and via `workflow_dispatch` (choose a source and limit), opening
a PR with the new inbox notes. It never runs the LLM agent, so it needs no model
key.
