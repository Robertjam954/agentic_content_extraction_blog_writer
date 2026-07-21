"""Persistent Chroma client, collection, and embedding function.

The embedding function is local by default (sentence-transformers MiniLM via Chroma's
DefaultEmbeddingFunction) so indexing and search work with no API key and no data
leaving the machine. To use a hosted embedder instead (OpenAI, Voyage, ...), return a
different chromadb embedding function from `embedding_function()`; keep it identical
for indexing and querying or the vectors will not match.
"""
from __future__ import annotations

from .config import COLLECTION, PERSIST_DIR


def get_client():
    import chromadb

    PERSIST_DIR.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(PERSIST_DIR))


def embedding_function():
    from chromadb.utils import embedding_functions

    # Local, offline MiniLM. Swap here for a hosted embedder if you prefer.
    return embedding_functions.DefaultEmbeddingFunction()


def get_collection(client=None):
    client = client or get_client()
    return client.get_or_create_collection(
        name=COLLECTION,
        embedding_function=embedding_function(),
        metadata={"hnsw:space": "cosine"},
    )
