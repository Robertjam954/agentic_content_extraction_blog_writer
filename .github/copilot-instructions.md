# Agentic Content Extraction & Blog Writer - Guidelines

This project is a multiagent content pipeline: it turns a curated list of YouTube
videos (as transcripts) and personal notes into a connected Obsidian knowledge graph,
then drafts concept-first blog posts from that graph, while a self-documenting agent
keeps the project's own docs current. It is built module by module against the
reference prompts in the subfolders.

Always ground your work in these documents:

- [Product vision and goals](../PRODUCT.md): what the system does, who it is for, and
  its boundaries. Align changes with these goals.
- [Architecture and design](../ARCHITECTURE.md): components (ingestion, the Obsidian
  knowledge graph, the four agents), data flow, and the module map.
- [Contributing guidelines](../CONTRIBUTING.md): the module workflow (watch video ->
  plan -> implement -> validate), setup, testing, and authoring conventions.
- [Claude Code operating manual](../CLAUDE.md): repository layout, the ingestion
  scripts, the Inbox pipeline, GitHub automations, gotchas, and the
  self-documentation protocol.
- [Agent roster](../AGENTS.md): purpose, inputs, outputs, and brief locations for
  the agents specified under `obisidian-knowledge-graph/Agents/Agents/`.

## Working rules

- No stack is locked project-wide. Decide concrete tooling per module and record it in
  that module's `*-plan.md`. Plan before implementing.
- Treat the reference assets in `obisidian-knowledge-graph/`,
  `notion-db-to-technical-blog/`, and `claude-md-memory-workflow/` as the behavioral
  spec to implement, not as files to rewrite casually.
- Use single hyphens, never em dashes, in all written content.
- Follow the vault and blog conventions in `CONTRIBUTING.md` (vault naming, two-link
  minimum and core-node footer for notes, concept-first ~700-word posts with valid
  frontmatter and the two required links).
- Prefer accuracy over hypotheticals: read files before editing, and document what the
  code and content actually do.

Suggest updates to these documents if you find incomplete or conflicting information
while working.
