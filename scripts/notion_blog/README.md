# Notion to blog pipeline

Turns reviewed research notes in a Notion database into blog post drafts for the
Jekyll site in `site/`. The companion uploader in the `agentic_research_team`
repo (`src/publish/notion_uploader.py`) pushes research notes INTO the same
database; this script pulls approved notes OUT and drafts posts from them.

## The workflow

```
agentic_research_team          Notion database              this repo
  research notes  ----------->  Needs Review
                                    |  (you review + approve)
                                Ready for Blog
                                    |
  pull_and_generate.py  <-----------
        |
     drafts/YYYY-MM-DD-slug.md      (you review + edit)
        |
     site/_posts/                   (commit + push = published)
```

Nothing is published automatically. You review twice: once in Notion (is the
note worth a post?) and once on the draft (is the post good enough to ship?).

## One-time Notion setup

1. Create an internal integration at https://www.notion.so/my-integrations
   and copy its secret (this is `NOTION_API_KEY`).
2. Create a database (full-page table) with these properties:

   | Property     | Type         | Notes |
   |--------------|--------------|-------|
   | Name         | Title        | Note / post topic |
   | Status       | Select       | Options: `Needs Review`, `Ready for Blog`, `Drafted`, `Published` |
   | Tags         | Multi-select | Becomes post tags |
   | SEO Keywords | Multi-select | Woven into the generated post |
   | Source       | URL          | Link to the underlying research (optional) |

   The note content itself lives in the page body (headings, paragraphs,
   lists - normal Notion blocks).
3. Share the database with the integration (database page -> `...` ->
   Connections -> your integration).
4. Copy the database ID from its URL (the 32-char hex segment before `?v=`);
   this is `NOTION_DATABASE_ID`.

## Environment variables

| Variable | Required | Purpose |
|----------|----------|---------|
| `NOTION_API_KEY` | yes | Notion internal integration secret |
| `NOTION_DATABASE_ID` | yes | The notes database |
| `ANTHROPIC_API_KEY` | recommended | Enables Claude-written drafts; without it drafts are structural copies of the note |
| `BLOG_MODEL` | no | Claude model override (default `claude-sonnet-4-20250514`) |

## Usage

```bash
pip install anthropic   # only dependency, and only needed for LLM drafting

export NOTION_API_KEY=secret_...
export NOTION_DATABASE_ID=...
export ANTHROPIC_API_KEY=sk-ant-...

# Draft every note marked "Ready for Blog", mark each "Drafted" in Notion
python scripts/notion_blog/pull_and_generate.py

# Try it without touching Notion statuses
python scripts/notion_blog/pull_and_generate.py --dry-run --limit 1
```

Drafts land in `drafts/`. To publish one:

```bash
mv drafts/2026-07-16-my-post.md site/_posts/
git add site/_posts && git commit -m "Publish: my post" && git push
```

GitHub Pages rebuilds the site automatically on push to `main`
(`.github/workflows/pages.yml`). Flip the note's Status to `Published` in
Notion when you ship it, so the queue stays honest.

## Local site preview

```bash
cd site
bundle install
bundle exec jekyll serve   # http://localhost:4000
```
