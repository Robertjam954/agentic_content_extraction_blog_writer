"""Content writing agent, grounded in the RAG index.

Retrieves relevant passages from the `rag/` ChromaDB index, assembles the structured
content object the writing brief
(`notion-db-to-technical-blog/notion-db-to-technical-blog.md`) expects, and asks Claude
to draft a concept-first blog post.

CLI:
    python -m writer "your topic"              # draft (needs ANTHROPIC_API_KEY)
    python -m writer "your topic" --dry-run    # retrieve + assemble only, no API call
"""
from .agent import write_blog

__all__ = ["write_blog"]
