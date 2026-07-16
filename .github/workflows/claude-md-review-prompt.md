# Task: Update CLAUDE.md Documentation

You are tasked with reviewing and updating the CLAUDE.md file for this
repository. This file provides guidance to Claude Code when working with code
in this repository. If CLAUDE.md does not exist yet, create it at the
repository root.

## Your Mission

Conduct a comprehensive analysis of the entire codebase and update CLAUDE.md so
it is 100% accurate, complete, and helpful for future Claude Code sessions.

## Analysis Requirements

### 1. Project Overview
- Verify the project description against PRODUCT.md, ARCHITECTURE.md, and the
  actual implementation
- This repo contains both reference specs (module folders such as
  `obisidian-knowledge-graph/`, `notion-db-to-technical-blog/`,
  `claude-md-memory-workflow/`) and the working implementation - keep the
  distinction clear

### 2. Blog site (`site/`)
- Verify the Jekyll configuration, layouts, plugins, and permalink structure
- Document how posts are added (drafts/ -> site/_posts/) and how the site is
  deployed (GitHub Pages workflow)
- Verify local preview commands actually match the Gemfile

### 3. Notion pipeline (`scripts/notion_blog/`)
- Document each script's purpose, its environment variables, and the Notion
  database schema it expects
- Verify the status flow (Needs Review -> Ready for Blog -> Drafted ->
  Published) against the code
- Document the companion uploader in the agentic_research_team repo

### 4. Workflows (`.github/workflows/`)
- Document every workflow: trigger, what it does, and required secrets

### 5. Directory structure
- Scan the repository recursively and verify every documented path exists
- Document significant directories or files not yet mentioned

### 6. Commands
- Verify every documented command against reality (Jekyll build/serve, the
  Python scripts, any linting)

### 7. Environment variables
- Document required variables (names and purposes only, never values)

### 8. Conventions
- Extract conventions from the existing code (Python style, single hyphens
  instead of em dashes in prose, review-first publishing)

## Output Requirements

1. Maintain the existing CLAUDE.md structure where one exists; otherwise use a
   clear section layout (Overview, Repository Layout, Blog Site, Notion
   Pipeline, Commands, Environment Variables, Workflows, Conventions, Gotchas)
2. Remove outdated information; if documentation and reality disagree, reality
   wins
3. Be thorough but concise - every line should provide value
4. Include gotchas and non-obvious aspects
5. Use single hyphens, never em dashes

## Process

1. Analyze the codebase systematically
2. Compare findings with the current CLAUDE.md (if any)
3. Write the updated file, with all paths, commands, and details verified
