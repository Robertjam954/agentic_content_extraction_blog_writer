# Contributing

This repository implements a multiagent content pipeline (see `PRODUCT.md` and
`ARCHITECTURE.md`). It is built module by module against the reference prompts and
agent briefs in the subfolders. These guidelines cover how to work on the build.

## Module workflow

Each module has a reference video that outlines how to complete it. For every module:

1. **Watch the module video** and skim its reference assets in the subfolder before
   writing anything.
2. **Plan first.** Produce a short implementation plan (a `*-plan.md` for the module)
   that records the stack decisions for that module, the tasks as a checklist, and
   1-3 open questions. No stack is locked project-wide; the plan is where choices are
   made.
3. **Implement against the plan,** following the existing patterns and the spec in
   that module's reference brief.
4. **Validate** the module against its own success criteria and quality checklist
   (see below), then update `CLAUDE.md` / decision records via the self-documenting
   agent once Module 4 exists.

Keep planning, implementation, and review in separate agent sessions to avoid context
mixing.

## Setup

- Clone the repository.
- Install the tooling a module actually needs, when you reach it - the stack is
  decided per module, so do not pre-install everything. Common dependencies from the
  reference assets: an AI agent runtime (Claude Code or the Claude Agent SDK),
  Obsidian for browsing the vault, and `rg` (ripgrep) and `fd` for the agents' CLI
  playbooks.
- Note import reuses `/Users/robertjames/loc/repos/obsidian-importer` (an Obsidian
  plugin; Node.js + pnpm) as a reference or dependency for the ingestion stage.
- The documentation-automation workflow runs in GitHub Actions on Node.js 20 and uses
  `anthropics/claude-code-action`. It expects a `CLAUDE_CODE_OAUTH_TOKEN` (or
  `ANTHROPIC_API_KEY`) repository secret.

## How to run and test

Validation is per stage; there is no single global test suite yet. As each stage is
built, add the checks that fit its implementation, and always validate behavior end
to end on a small sample:

- **Ingestion:** run against one or two real video URLs and a sample note export;
  confirm transcripts land in `Inbox/` and imported notes are valid Markdown.
- **Transcript processing agent:** run on a sample transcript and confirm the output
  follows the fixed scaffold with quoted receipts and resolvable block IDs.
- **Vault connectivity agent:** run on a sample vault and confirm it follows its
  standard workflow, that generated wikilinks resolve, and that no `Projects/` core
  node was modified.
- **Content writing agent:** paste the prompt plus a representative content object and
  confirm the output passes its own checklist (frontmatter validity, ~700 words, both
  required links, no code blocks, no cliches).
- **Self-documenting agent / workflow:** trigger it via `workflow_dispatch` and review
  the pull request it opens rather than committing generated docs directly to `main`.

## Authoring and coding guidelines

- Use single hyphens, never em dashes, in all written content.
- Keep agent briefs and prompts self-contained and grounded in concrete behavior:
  state the mandate, success criteria, a standard workflow, and a quality checklist,
  as the existing reference briefs do.
- Prefer accuracy over hypotheticals. Document what the code or content actually does;
  read files before editing them.
- Obsidian vault naming: underscore-separated, TitleCased filenames, with acronyms
  kept uppercase (AI, LLM, RAG). Raw transcript dumps may keep source-generated dashes
  so video IDs match.
- In the vault, every note should link to at least two other notes and carry the
  `> Core Node: [[Projects/AI_Native_Engineer]]` footer; treat `Projects/` notes as
  human-authored and read-only.
- Blog content rules: no code, commands, or step-by-step instructions; concept-first;
  ~700 words; valid frontmatter with no colon in the title; close with both the source
  video link and the community link; avoid AI writing cliches.
- Treat the prep docs and agent briefs as living documents. When a module changes how
  the system works, update `PRODUCT.md` / `ARCHITECTURE.md` and the relevant brief.

## Git and pull requests

- Branch from `main`; do not commit generated documentation directly to `main` (the
  automation workflow defaults to opening a PR for review).
- Keep changes focused on a single module or stage where practical, and explain what
  behavior the change affects so it can be validated against the intended use.
- Commit or push only when asked.
