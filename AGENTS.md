# AGENTS.md

Roster of the agents defined in `obisidian-knowledge-graph/Agents/Agents/`. The
brief files are the canonical spec; this page is the index. A vault-level overview
and the `rg`/`fd` CLI query playbook the agents use live in
`obisidian-knowledge-graph/AGENTS.md`.

Shared guardrails across all vault agents:

- `Projects/` notes are human-authored and read-only; agents log recommendations
  instead of editing them.
- Vault filenames are underscore-separated and TitleCased with acronyms uppercase
  (AI, LLM, RAG); raw transcript dumps keep source-generated dashes so video IDs
  stay matchable.
- Every note carries the `> Core Node: [[Projects/AI_Native_Engineer]]` footer and
  links to at least two other notes.
- All content is framed for the "Professional Seeking AI Mastery" persona.

Note: the vault directories these agents operate on (`Resources/`, `Projects/`,
`Areas/`, `Archives/`) are not in this repo yet; only `Inbox/` exists (target).

## Transcript processing agent

- **Brief:** `obisidian-knowledge-graph/Agents/Agents/transcript_processing_agent.md`
- **Purpose:** turn raw video transcripts into actionable AI engineering playbooks:
  structured notes that capture the video's problem, core thesis, architecture and
  environment, key insights with quoted receipts and block IDs, strong opinions,
  intro/CTA patterns, workflow recipes, reusable story assets, and proposed
  downstream content plays. Also creates or enriches concept, hub, technology, and
  framework notes when the video introduces reusable strategies (with explicit
  concept-creation triggers: recurring across 2+ transcripts or a persona pillar,
  fully completable in one pass, resolves ambiguity).
- **Inputs:** a transcript file (`.srt`, `.txt`, or `.md`) from
  `Inbox/Transcripts_to_Process` with the YouTube ID derived from the filename;
  pre-flight scans of `Resources/Processed_Transcripts`, `Resources/Hubs`,
  `Resources/Concepts`, `Resources/Technologies`, `Resources/Script_Frameworks`,
  and active `Projects/` folders (via `rg` sweeps) to avoid duplicates.
- **Outputs:** a structured note in `Resources/Processed_Transcripts/` following
  the brief's fixed scaffold (front matter with `youtube_id` + `source_url`, then
  Context Snapshot, Core Thesis, Architecture & Environment, Key Insights &
  Receipts, Topics & Themes, Strong Opinions & POV, Intro & CTA Patterns, Workflow
  Recipes & Commands, Reusable Story Assets, Content Plays, Resource & Project
  Touchpoints, Linked Technologies, Related, Transcript (Curated)); updated or new
  concept/hub/technology notes with bidirectional links; the processed raw
  transcript moved to `Archives/Transcripts/Raw`.

## Vault connectivity agent

- **Brief:** `obisidian-knowledge-graph/Agents/Agents/vault_connectivity_agent.md`
- **Purpose:** audit the entire vault for linking gaps, orphaned or weakly linked
  notes, missing front matter, and un-modeled themes; ship new concept, hub,
  technology, or framework nodes grounded in transcript receipts within the same
  run; merge duplicated or superseded content into canonical notes; enforce
  bidirectional backlinks (including hub <-> technology lockstep) and persona-
  aligned CTAs. Definition of done: no orphaned high-value notes, redundancy
  merged or archived under `Archives/Retired_Assets/` with rationale, audit log
  confirming zero outstanding items.
- **Inputs:** full read access to the vault directories (`Inbox/`, `Resources/*`,
  `Projects/` read-only, `Areas/`, `Archives/`, `Agents/`); CLI tooling `rg`,
  `fd`/`find`, and `jq` for backlink, orphan, and coverage checks; the latest
  agent briefs.
- **Outputs:** updated notes with added/revised links and merged content; new
  fully populated canonical nodes with complete front matter and the core-node
  footer; archived superseded material under `Archives/Retired_Assets/` with
  context blocks; a working audit note recording every action taken.

## Vault structure overview

- **Brief:** `obisidian-knowledge-graph/Agents/Agents/vault_structure_overview.md`
- **Purpose:** not an agent but a shared reference embedded (via `![[...]]`) into
  the other briefs. Defines the PARA-style vault layout: `Inbox/` capture zone,
  `Resources/` canonical references (Hubs, Concepts, Technologies,
  Processed_Transcripts, Script_Frameworks), `Projects/` active deliverables,
  `Areas/`, `Archives/`, `Excalidraw/`, and `Agents/`; plus the naming convention
  and core-node footer rules.
- **Inputs:** none (static reference document).
- **Outputs:** none; it is consumed by the transcript processing and vault
  connectivity agents as their structure ground truth.

## Persona - Professional Seeking AI Mastery

- **Brief:** `obisidian-knowledge-graph/Agents/Agents/persona_professional_seeking_ai_mastery.md`
- **Purpose:** the audience definition every agent aligns content to: software
  engineers, data scientists, recent CS grads, and founders (0-10+ years) who use
  AI tools superficially and need a structured, project-driven path to
  production-grade AI engineering. Captures their gaps, motivations (career
  acceleration, relevance, launching AI products), support style, and pain points.
- **Inputs:** none (static reference document, embedded into the processing and
  connectivity briefs).
- **Outputs:** none directly; it shapes audience framing, CTA alignment, and the
  `persona:` front matter field in vault notes.

## Self-documenting agent

- **Brief:** `obisidian-knowledge-graph/Agents/Agents/self-documenting-ai-agent/README.md`
  (companion reference: `claude-md-memory-workflow/`, the scheduled CLAUDE.md
  example workflow)
- **Purpose:** keep the project's own documentation current. The brief is an ADR
  generator prompt: run `git diff main`, understand the full change (reading extra
  files as needed), decide whether it is a significant architectural change, and
  if so write an Architecture Decision Record documenting the decisions,
  rationale, and trade-offs observed in the code. Skips ADR creation for minor
  fixes, docs/test-only changes, and config tweaks.
- **Inputs:** the `git diff main` output for the current branch; additional source
  files read for context; the ADR template at `./.claude/adr-template.md` if it
  exists (not currently in the repo).
- **Outputs:** a descriptively named ADR in `docs/adr/` (folder created if
  needed), grounded in actual code details (libraries, data structures,
  configuration values) - or no output when the change is not architectural. The
  related weekly CLAUDE.md verification is implemented in this repo as
  `.github/workflows/update-claude-md.yml`.
