# Product

## What this is

A multiagent content pipeline. Agents gather docs from various sources (websites,
notes, blogs, papers, video transcripts) into a connected Obsidian knowledge graph
that doubles as the RAG store, then a writing/summary agent produces a structured
summary that is uploaded to Notion for human review before publishing. A
self-documenting agent keeps the project's own documentation current as the system
evolves.

This is a portfolio AI engineering build, not a collection of prompts. The reference
prompts and agent briefs in the module subfolders
(`obisidian-knowledge-graph/`, `notion-db-to-technical-blog/`,
`claude-md-memory-workflow/`) are the working spec; this repository implements them
as a runnable system. The build proceeds across four modules, each paired with a
walkthrough video that outlines how to complete it.

The sections below describe the target system. Not all of it exists yet: Module 1 is
built; Module 2's ingestion scripts are built (the processing agents are not);
Module 3's retrieval, drafting, and Notion-review code runs (live calls need API
keys); and Module 4 has an initial `CLAUDE.md` but its scheduled workflow is not
installed. See the module status table in `README.md` for the current state of each
piece.

## The problem it solves

High-signal technical content (conference talks, tutorials, the user's own notes)
is locked in long, linear formats. Watching a video or rereading notes does not make
the ideas reusable or discoverable, and turning them into publishable writing is slow
and repetitive. This system extracts the durable ideas once, links them into a graph
that surfaces connections, and reuses that graph to produce on-brand blog posts on
demand.

## What it does

1. **Ingest sources.** Takes a specified list of YouTube videos (converted to
   transcripts) and personal notes exported from other apps, and lands them as raw
   material in an inbox for processing.

2. **Extract structured knowledge.** A transcript processing agent converts each raw
   transcript into a structured, reusable note that captures the source's problem,
   core thesis, architecture and environment, key insights with quoted receipts and
   block IDs, workflow recipes, strong opinions, intro/CTA patterns, and proposed
   downstream content.

3. **Build and maintain the knowledge graph.** A vault connectivity agent audits the
   whole vault for orphaned or weakly linked notes, creates missing concept, hub, and
   technology nodes, merges duplicates, and enforces bidirectional links so insights
   surface where they are needed. The Obsidian vault is both the human-browsable
   knowledge base and the retrieval store the writing agent draws from.

4. **Generate blog posts.** A content writing agent takes a structured content object
   assembled from the graph and writes a polished, concept-oriented post. It strips
   out code, commands, and step-by-step instructions, keeps posts to roughly 700
   words for a 3-5 minute read, integrates SEO keywords naturally, avoids common AI
   writing cliches, emits valid frontmatter, and always closes with links to the
   source video and the community.

5. **Keep itself documented.** A self-documenting agent re-analyzes the codebase to
   keep `CLAUDE.md` accurate and emits Architecture Decision Records from diffs, so
   the project's own context stays fresh without manual effort.

## Key features

- End-to-end extraction: from a list of video URLs and note exports to a linked
  knowledge graph and draft posts, with no manual re-keying of ideas.
- A consistent note scaffold so extracted knowledge is structured and repurposable.
- Knowledge-graph hygiene: link validation, de-duplication, hub/MOC maintenance, and
  naming conventions enforced by an agent rather than by hand.
- Strict, opinionated content rules for concept-first, on-brand blog output.
- Self-maintaining documentation so the project stays understandable as it grows.

## How the build is organized

The system is built module by module, watching the reference video for each before
implementing it. The tooling for each module is chosen when that module is built (no
stack is locked up front), so each module's plan records the concrete choices made.

1. **Context engineering (built).** Establish the `PRODUCT.md` / `ARCHITECTURE.md` /
   `CONTRIBUTING.md` plus instructions-file convention that grounds every agent in
   project context, and the plan-then-implement workflow used for the rest of the
   build.
2. **Knowledge graph extraction (partially built).** Implement the ingestion path
   (transcripts and note imports) and the transcript processing and vault
   connectivity agents that build and maintain the Obsidian graph. The ingestion
   scripts (`scripts/`) exist and the raw material is in `Inbox/`; the agents are
   still spec-only.
3. **Blog generation (planned).** Implement the content writing agent that turns a
   structured content object from the graph into a finished post.
4. **Documentation automation (planned).** Implement the self-documenting agent and
   the scheduled workflow that keeps `CLAUDE.md` and decision records current.

## Intended users and use cases

The primary audience is the "Professional Seeking AI Mastery" persona described in
`obisidian-knowledge-graph/Agents/Agents/persona_professional_seeking_ai_mastery.md`:
software engineers, data scientists, recent CS graduates, and founders who can code
and want production-ready AI engineering skills.

Representative use cases:

- A content creator converting a backlog of watched videos and scattered notes into
  a connected knowledge base and a steady stream of blog posts.
- An engineer demonstrating a real, multi-agent content pipeline as portfolio work.
- A learner following the module videos who wants a working implementation to adapt
  to their own sources, blog stack, and instruction files.

## Boundaries and non-goals

- This is a single-operator pipeline for the user's own sources, not a multi-tenant
  SaaS.
- It drafts blog posts; a human reviews and publishes. It does not auto-publish.
- It does not redistribute source video content; it extracts ideas and always links
  back to the original source.
- The concrete stack (transcript fetching, note import, agent runtime, blog target)
  is decided per module and recorded there, not fixed in this document.
