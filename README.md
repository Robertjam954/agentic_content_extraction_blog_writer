This is a collection of public prompts and concepts used in various videos to teach AI Engineering concepts.
For more [join the AI Engineering community](https://skool.com/ai-engineer).

## Blog site + Notion pipeline

This repo now hosts the working blog implementation:

- `site/` - the Jekyll blog, deployed to GitHub Pages by `.github/workflows/pages.yml` on pushes to `main`.
- `scripts/notion_blog/` - pulls notes marked "Ready for Blog" from the shared Notion database and drafts concept-first posts into `drafts/`. See `scripts/notion_blog/README.md` for setup.
- Notes flow in from the `agentic_research_team` repo (`src/publish/notion_uploader.py`), get reviewed in Notion, get drafted here, and are published by moving the reviewed draft into `site/_posts/`.
