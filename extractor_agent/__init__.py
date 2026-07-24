"""Microsoft Agent Framework orchestration layer over the content extractors.

`actions` holds the dependency-free extractor functions (usable without a model);
`agent` wraps them as Agent Framework tools for natural-language orchestration.
"""
from . import actions

__all__ = ["actions"]
