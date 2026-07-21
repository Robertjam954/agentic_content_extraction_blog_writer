"""RAG index over the project's notes and docs.

A thin wrapper around a persistent ChromaDB collection that holds embeddings of the
Inbox material, agent briefs, and project docs, so agents (and the CLI) can retrieve
relevant passages by meaning rather than by keyword or graph traversal.

CLI:
    python -m rag index            # build/update the index
    python -m rag index --reset    # rebuild from scratch
    python -m rag search "query"   # semantic search
"""
from .search import search

__all__ = ["search"]
