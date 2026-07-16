# Obsidian RAG (knowledge-rag engine)

Local, hybrid RAG over this project's Obsidian vault (notes + docs), exposed to Claude
Code as MCP tools so Claude uses the Obsidian graph as its local knowledge. It
complements the lightweight `rag/` package: `rag/` is a simple programmatic index the
`writer/` agent calls; this is a richer retrieval surface (**BM25 + ONNX vector
embeddings + cross-encoder reranking**, 100% local, no API keys) that Claude Code
queries natively via `search_knowledge(...)`.

## Engine

The engine is the **knowledge-rag** MCP server. The active local copy is at (note the
space in the path):

```
/Users/robertjames/loc/repos/github_clones/infra and deployment/local_rag/local_claude_knowledge_rag_search
```

`config.yaml` in *this* folder points the engine at the vault (`documents_dir`) and keeps
the index, model cache (~250MB), and data next to it (gitignored). Change the single
`documents_dir` line to index a different Obsidian vault.

## Setup

Disk note: the install pulls `fastembed[reranking]` (ONNX + cross-encoder), `chromadb`,
`pymupdf`, office parsers, plus ~250MB of models - a few GB. Run these yourself when
ready (the path has a space, so keep it quoted):

1. Install the engine into its own venv:

   ```bash
   ENGINE="/Users/robertjames/loc/repos/github_clones/infra and deployment/local_rag/local_claude_knowledge_rag_search"
   python3 -m venv "$ENGINE/venv"
   "$ENGINE/venv/bin/pip" install -r "$ENGINE/requirements.txt"
   "$ENGINE/venv/bin/pip" install -e "$ENGINE"   # so `python -m mcp_server.server` imports cleanly
   ```

2. Register it with Claude Code, pointing at this project's config via
   `KNOWLEDGE_RAG_DIR`:

   ```bash
   claude mcp add knowledge-rag -s user -- \
     env KNOWLEDGE_RAG_DIR="/Users/robertjames/loc/repos/personal_projects/agentic_content_extraction_blog_writer/obsidian-rag" \
     "$ENGINE/venv/bin/python" -m mcp_server.server
   ```

   Or add a project-scoped `.mcp.json` at the repo root (Claude Code auto-loads it):

   ```json
   {
     "mcpServers": {
       "knowledge-rag": {
         "command": "/Users/robertjames/loc/repos/github_clones/infra and deployment/local_rag/local_claude_knowledge_rag_search/venv/bin/python",
         "args": ["-m", "mcp_server.server"],
         "env": {
           "KNOWLEDGE_RAG_DIR": "/Users/robertjames/loc/repos/personal_projects/agentic_content_extraction_blog_writer/obsidian-rag",
           "PYTHONPATH": "/Users/robertjames/loc/repos/github_clones/infra and deployment/local_rag/local_claude_knowledge_rag_search"
         }
       }
     }
   }
   ```

3. Restart Claude Code. The server indexes the vault on first query (a file watcher
   auto-reindexes on changes), then use the MCP tools - `search_knowledge("...")`,
   `get_document`, `list`, `stats`, `reindex`, and the rest.

## Vault

`documents_dir` (in `config.yaml`) currently points at this content-pipeline repo, so
the vault is its `Inbox/` notes, project docs, and agent briefs (`.md` / `.txt`). As the
agents populate the vault, those notes are picked up automatically. Point `documents_dir`
at a dedicated Obsidian vault to index that instead.

For Obsidian conventions (frontmatter metadata, Dataview queries), the `obsidian-dataview`
plugin under `github_clones/infra and deployment/local_rag/` is the reference.
