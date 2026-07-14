# Architecture

## Overview

This system is an agentic content pipeline. Raw material (YouTube transcripts and
imported notes) flows through extraction and writing agents and out to draft blog
posts, with an Obsidian vault serving as the connected knowledge graph in the middle.
A separate documentation agent keeps the project's own context current.

The repository is being built module by module. The reference prompts and agent
briefs in the subfolders are the behavioral spec; the implementation realizes them.
Concrete tooling (languages, libraries, services) is chosen when each module is built
and recorded in that module's plan, so this document describes the logical
architecture and the component contracts rather than a fixed stack.

## Components

### Ingestion

- **Source list.** A curated list of YouTube video URLs/IDs plus a set of personal
  note exports is the system's input.
- **Transcript acquisition.** Each video is converted to a transcript and dropped in
  `Inbox/Transcripts_to_Process`. Raw transcript dumps may keep source-generated
  dashes so video IDs remain matchable.
- **Note import.** Notes exported from other apps are converted to Markdown for the
  vault. The `obsidian-importer` project
  (`/Users/robertjames/loc/repos/obsidian-importer`) is the reference for importing
  from Apple Notes, Evernote, Notion, Google Keep, OneNote, Roam, HTML, and Markdown,
  and is a candidate dependency for this stage.

### Knowledge graph (the Obsidian vault)

The vault is both the human-browsable knowledge base and the retrieval store the
writing agent reads from. It follows a PARA-style folder model
(`vault_structure_overview.md`): an `Inbox/` for raw material, `Resources/` for
processed notes, `Projects/` for human-authored core nodes (treated as read-only by
agents), plus concept, hub/MOC, and technology nodes. Graph structure is expressed
with Obsidian wikilinks, embeds, block IDs, and front matter.

### Agents

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
  (`notion-db-to-technical-blog/notion-db-to-technical-blog.md`). Transforms a
  structured content object (Content Topic, Hook/Introduction, Key Insights, SEO
  Keywords, Source Video, Transcript) into a concept-focused post under strict output
  rules: valid frontmatter, no code or implementation detail, ~700 words, and a
  mandatory two-link call to action.
- **Self-documenting agent** (`claude-md-memory-workflow/` and
  `obisidian-knowledge-graph/Agents/Agents/self-documenting-ai-agent/`). Re-analyzes
  the codebase to keep `CLAUDE.md` accurate and generates Architecture Decision
  Records from `git diff main`.

## Data flow

```
source list (video URLs + note exports)
  -> transcript acquisition / note import          [Ingestion]
  -> Inbox/ (raw transcripts, imported notes)
  -> transcript processing agent
  -> Resources/Processed_Transcripts (structured notes w/ receipts + block IDs)
  -> vault connectivity agent (link, de-dupe, create hub/concept/tech nodes)
  -> Obsidian vault = knowledge graph / retrieval store
  -> structured content object (assembled from the graph)
  -> content writing agent
  -> Markdown blog post with frontmatter (draft for human review)
```

Independently, the self-documenting agent reads code diffs to keep `CLAUDE.md` current
and emit ADRs. The vault doubles as the RAG layer: retrieval is graph traversal over
wikilinks and block references rather than an opaque vector index, which keeps what
the writing agent draws on inspectable.

## Module map

The four build modules map onto the components above. Each has a reference video to
watch before implementing, and each records its own concrete tooling decisions.

| Module | Folder | Builds |
| --- | --- | --- |
| 1. Context engineering | `context-engineering-workflow.md` | This doc set, the instructions file, and the plan-then-implement workflow |
| 2. Knowledge graph extraction | `obisidian-knowledge-graph/` | Ingestion + transcript processing + vault connectivity agents |
| 3. Blog generation | `notion-db-to-technical-blog/` | Content writing agent and the content-object contract |
| 4. Documentation automation | `claude-md-memory-workflow/` | Self-documenting agent + scheduled CLAUDE.md workflow |

## Key technologies and decisions

Decisions are deferred to the module that needs them. Candidate technologies, drawn
from the reference assets:

- **Authoring formats:** Markdown and YAML for notes, agent briefs, and frontmatter.
- **Knowledge graph host:** Obsidian (wikilinks, embeds, block IDs, front matter).
- **Agent runtime:** an AI coding/agent tool such as Claude Code or the Claude Agent
  SDK; the reference also uses GitHub Copilot / VS Code custom agents.
- **Ingestion:** a transcript source for YouTube, and `obsidian-importer` for note
  conversion.
- **CLI tooling used by agents:** `rg` (ripgrep) and `fd` for search and inventory.
- **Content source contract:** a structured content object (the reference pulls this
  from a Notion database; the implementing module decides the actual source).
- **Blog target:** a static site (the reference CLAUDE.md prompt assumes Astro, e.g.
  `astro.config.mjs` and content collections).
- **Documentation automation:** GitHub Actions running `claude-code-action` on a
  schedule to open a PR with the updated `CLAUDE.md`.

When a module commits to a specific tool, record it in that module's plan and, if it
shapes the system, reflect it back here.
