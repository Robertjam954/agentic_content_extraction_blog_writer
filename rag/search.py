"""Semantic search over the notes/docs RAG index."""
from __future__ import annotations

from .store import get_collection


def search(query: str, k: int = 5, source_type: str | None = None) -> list[dict]:
    """Return the k most relevant chunks for `query`.

    Each hit is {"score", "title", "source_path", "source_type", "source_url", "text"}.
    `score` is cosine similarity (1.0 = identical); higher is better. Optionally filter
    to a single source_type (transcript / skill / web / doc / brief).
    """
    col = get_collection()
    where = {"source_type": source_type} if source_type else None
    res = col.query(query_texts=[query], n_results=k, where=where)

    docs = res["documents"][0]
    metas = res["metadatas"][0]
    dists = res["distances"][0]
    hits = []
    for doc, meta, dist in zip(docs, metas, dists):
        hits.append(
            {
                "score": round(1.0 - dist, 4),
                "title": meta.get("title", ""),
                "source_path": meta.get("source_path", ""),
                "source_type": meta.get("source_type", ""),
                "source_url": meta.get("source_url", ""),
                "text": doc,
            }
        )
    return hits
