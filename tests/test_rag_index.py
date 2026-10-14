"""Offline indexing regressions; optional real persistent Chroma integration."""
import contextlib
import importlib.util
import importlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from rag import index

search = importlib.import_module("rag.search")


class MemoryCollection:
    """Small collection double implementing the APIs used by index/search."""
    def __init__(self):
        self.rows = {}

    def get(self, limit, offset, include):
        rows = list(self.rows.items())[offset:offset + limit]
        return {"ids": [key for key, _ in rows],
                "metadatas": [row[1] for _, row in rows]}

    def delete(self, ids=None, where=None):
        if ids is None:
            ids = [key for key, (_, meta) in self.rows.items()
                   if all(meta.get(k) == v for k, v in where.items())]
        for key in ids:
            self.rows.pop(key, None)

    def upsert(self, ids, documents, metadatas):
        self.rows.update(zip(ids, zip(documents, metadatas)))

    def count(self):
        return len(self.rows)

    def query(self, query_texts, n_results, where=None):
        rows = [row for row in self.rows.values()
                if not where or all(row[1].get(k) == v for k, v in where.items())]
        rows.sort(key=lambda row: query_texts[0] not in row[0])
        rows = rows[:n_results]
        return {"documents": [[r[0] for r in rows]],
                "metadatas": [[r[1] for r in rows]],
                "distances": [[0.0 for r in rows]]}


class IndexTests(unittest.TestCase):
    def test_precise_discovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            allowed = ["Inbox/Web_to_Process/source.md", "Resources/Drafts/note.md",
                       "Inbox/Drafts_archive/note.txt", "Inbox/Drafts.md",
                       "other/Inbox/Drafts/note.md"]
            blocked = ["Inbox/Drafts/run.md", "Inbox/Drafts/nested/prompt.srt",
                       ".rag/note.md"]
            for name in allowed + blocked:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("evidence")
            with patch.object(index, "REPO_ROOT", root):
                self.assertEqual({p.relative_to(root).as_posix()
                                  for p in index.iter_files()}, set(allowed))

    def exercise_reindex(self, col):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "Inbox/Web_to_Process/source.md"
            source.parent.mkdir(parents=True)
            source.write_text("# Source\nIndependent evidence on retrieval.")
            draft = root / "Inbox/Drafts/nested/run.md"
            draft.parent.mkdir(parents=True)
            draft.write_text("# Draft\nGenerated operational prompt.")
            paths = ["Inbox/Drafts/deleted.md", "Inbox/Drafts/nested/run.md",
                     "Inbox\\Drafts\\old.txt", "Resources/Drafts/valid.md",
                     "Inbox/Drafts_archive/valid.md"]
            col.upsert(ids=[str(i) for i in range(len(paths))],
                       documents=["legacy evidence"] * len(paths),
                       metadatas=[{"source_path": p} for p in paths])
            with patch.object(index, "REPO_ROOT", root), \
                 patch.object(index, "get_client", return_value=object()), \
                 patch.object(index, "get_collection", return_value=col), \
                 patch.object(search, "get_collection", return_value=col), \
                 contextlib.redirect_stdout(io.StringIO()):
                for _ in range(2):
                    self.assertEqual(index.build(), 0)
                    hits = search.search("Independent evidence", k=3)
                    self.assertTrue(any(h["source_path"] ==
                                        "Inbox/Web_to_Process/source.md" for h in hits))
                    self.assertFalse(any(index.excluded_directory(h["source_path"])
                                         for h in hits))
                    self.assertEqual(col.count(), 3)
                self.assertTrue(draft.exists())

    def test_reindex_and_search(self):
        self.exercise_reindex(MemoryCollection())

    def test_cleanup_pagination_and_missing_metadata(self):
        col = MemoryCollection()
        paths = ["Inbox/Drafts/a.md", "Inbox/Drafts/b.md", "source.md",
                 "Inbox/Drafts/c.md", "Inbox/Drafts_backup/d.md"]
        col.upsert(ids=list("abcde"), documents=["x"] * 5,
                   metadatas=[{"source_path": p} for p in paths])
        col.rows["unknown"] = ("x", None)
        self.assertEqual(index.purge_excluded_chunks(col, batch_size=2), 3)
        self.assertEqual(set(col.rows), {"c", "e", "unknown"})
        self.assertEqual(index.purge_excluded_chunks(col, batch_size=2), 0)

    def test_cleanup_failure_aborts_build(self):
        col = MemoryCollection()
        col.upsert(ids=["draft"], documents=["x"],
                   metadatas=[{"source_path": "Inbox/Drafts/a.md"}])
        with patch.object(index, "get_client", return_value=object()), \
             patch.object(index, "get_collection", return_value=col), \
             patch.object(col, "delete", side_effect=RuntimeError("delete failed")), \
             patch.object(index, "iter_files") as discover:
            with self.assertRaisesRegex(RuntimeError, "delete failed"):
                index.build()
            discover.assert_not_called()

    @unittest.skipUnless(importlib.util.find_spec("chromadb"), "chromadb not installed")
    def test_persistent_chroma_reindex_and_search(self):
        import chromadb
        from chromadb.api.types import EmbeddingFunction

        class OfflineEmbedding(EmbeddingFunction):
            def __init__(self):
                pass

            @staticmethod
            def name():
                return "rag-regression-offline"

            def get_config(self):
                return {}

            @staticmethod
            def build_from_config(config):
                return OfflineEmbedding()

            def __call__(self, input):
                return [[1.0, float("Independent" in text), 0.5] for text in input]

        with tempfile.TemporaryDirectory() as tmp:
            client = chromadb.PersistentClient(path=tmp)
            col = client.get_or_create_collection(
                "regression", embedding_function=OfflineEmbedding())
            self.exercise_reindex(col)
            # Reopen the persistent collection after both builds.
            reopened = chromadb.PersistentClient(path=tmp).get_collection(
                "regression", embedding_function=OfflineEmbedding())
            self.assertEqual(reopened.count(), 3)
            page = reopened.get(include=["metadatas"])
            self.assertFalse(any(index.excluded_directory(m["source_path"])
                                 for m in page["metadatas"]))


if __name__ == "__main__":
    unittest.main()
