"""Configuration for the notes/docs RAG index."""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Where the persistent Chroma database lives (gitignored).
PERSIST_DIR = REPO_ROOT / ".rag" / "chroma"
COLLECTION = "notes_and_docs"

# Files to index: any of these extensions, anywhere under the repo, except paths that
# contain one of the excluded parts.
INCLUDE_EXTS = {".md", ".txt", ".srt"}
EXCLUDE_PARTS = {".git", ".claude", ".rag", ".github", "node_modules", ".venv"}

# Chunking (character-based, paragraph-aware).
CHUNK_CHARS = 1200
CHUNK_OVERLAP = 200
