# Status

Live checklist of what is left to complete on this project, in the same checkbox
format the portfolio tracking dashboard reads. Check a box (`[ ]` -> `[x]`) as
you finish. The module briefs in the subfolders are the behavioral spec; see the
module status table in `README.md` for narrative detail.

> Project: **Agentic Content Extraction & Blog Writer** · Stage: **module 2/3 build-out**
> Showcase deployed: GitHub Pages via `.github/workflows/pages.yml`.

## 1. Context engineering (Module 1)
- [x] Doc set (`README.md`, `PRODUCT.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md`)
- [x] `.github/copilot-instructions.md` + plan-then-implement workflow (`context-engineering-workflow.md`)

## 2. Knowledge graph extraction (Module 2)
- [x] `scripts/fetch_transcripts.py` - YouTube transcripts -> `Inbox/Transcripts_to_Process/`
- [x] `scripts/extract_skills.py` - installed Azure skills -> `Inbox/Skills_to_Process/`
- [x] `scripts/scrape_courses.py` - public course pages -> `Inbox/Web_to_Process/`
- [x] `scripts/fetch_semantic_scholar.py` - papers -> `Inbox/Papers_to_Process/`
- [x] Raw material landed: 5 transcripts, 28 skill notes, 15 course pages
- [ ] Transcript processing agent (spec-only brief in `obisidian-knowledge-graph/`) - raw transcript -> structured note
- [ ] Vault connectivity agent (spec-only brief) - orphan audit, hub/concept nodes, bidirectional links
- [ ] First processed notes + vault graph exist

## 3. Summary + review (Module 3)
- [x] `rag/` - persistent ChromaDB index, offline embeddings, `python -m rag index|search` (66 files indexed)
- [x] `writer/` - retrieval + content-object assembly + Claude draft path; `--dry-run` works offline
- [x] `notion_review/` - structured summary -> Notion review card; `--dry-run` prints payload offline
- [ ] Live draft run (needs `anthropic` + `ANTHROPIC_API_KEY`)
- [ ] Live Notion upload (needs `notion-client`, `NOTION_TOKEN`, `NOTION_REVIEW_DB`)

## 4. Documentation automation (Module 4)
- [x] Weekly dependency-refresh action installed (`weekly-maintenance.yml`)
- [ ] Install the CLAUDE.md memory workflow from `claude-md-memory-workflow/` under `.github/workflows/`
- [ ] Create `CLAUDE.md` (none exists yet)
- [ ] ADR-from-diffs emission wired up

## 5. Obsidian RAG for Claude (support)
- [x] `obsidian-rag/` knowledge-rag MCP server installed; vault indexed (95 files / 1123 chunks)
- [ ] Register the MCP server with Claude Code (see `obsidian-rag/README.md`)

## 6. Showcase frontend (GitHub Pages)
- [x] `site/index.html` showcase page on `main`
- [x] `.github/workflows/pages.yml` deploys `site/` as-is
- [x] Live and green: first push run failed (Pages not yet enabled), manual dispatch succeeded 2026-07-17 at current `main`. URL: `https://robertjam954.github.io/agentic_content_extraction_blog_writer/`
