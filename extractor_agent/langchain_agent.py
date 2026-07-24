"""LangChain orchestration over the content extractors.

An alternative to `agent.py` (Microsoft Agent Framework) built on the LangChain
stack (LangChain framework + LangGraph runtime via `langchain.agents.create_agent`),
as described in "The Agentic Operating Model". It wraps the same deterministic
extractor actions as LangChain tools, so extraction can be driven in natural
language while the tools stay deterministic and idempotent.

Local-first, matching the rest of the project: the default model backend is a local
LM Studio server (OpenAI-compatible). Cloud backends are opt-in.

Backend selection (by environment):
  - Azure OpenAI : if AZURE_OPENAI_ENDPOINT is set (AzureChatOpenAI; needs
                   AZURE_OPENAI_API_KEY + OPENAI_API_VERSION + a deployment name).
  - OpenAI cloud : else if OPENAI_API_KEY is set (optional OPENAI_CHAT_MODEL_ID).
  - LM Studio    : otherwise (default). Local server at LMSTUDIO_BASE_URL
                   (default http://localhost:1234/v1); set OPENAI_CHAT_MODEL_ID/
                   LMSTUDIO_MODEL to the id of the model loaded in LM Studio.

Observability: set LANGSMITH_API_KEY and LANGSMITH_TRACING=true to trace runs in
LangSmith (no code change needed).

Requires (only for the live agent):
    pip install langchain langgraph langchain-openai
"""
from __future__ import annotations

import os

from .actions import ACTIONS

DEFAULT_SYSTEM_PROMPT = (
    "You are a content-extraction orchestrator for an Obsidian knowledge vault. "
    "Use the provided tools to extract blog posts, articles, YouTube transcripts, "
    "and Google Docs into the vault inbox. Prefer the named source presets from "
    "list_sources for the known blogs. Respect any post limits the user gives; "
    "default to a small limit when unsure. After the tools run, report a concise "
    "summary of what was written, skipped, or failed. Never invent results - only "
    "report what the tools return."
)


def _build_tools():
    from langchain_core.tools import StructuredTool
    return [StructuredTool.from_function(fn) for fn in ACTIONS]


def _build_model():
    if os.getenv("AZURE_OPENAI_ENDPOINT"):
        from langchain_openai import AzureChatOpenAI
        return AzureChatOpenAI(
            azure_deployment=(os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
                              or os.getenv("OPENAI_CHAT_MODEL_ID")),
            api_version=os.getenv("OPENAI_API_VERSION", "2024-10-21"),
            temperature=0,
        )
    from langchain_openai import ChatOpenAI
    model_id = (os.getenv("OPENAI_CHAT_MODEL_ID") or os.getenv("LMSTUDIO_MODEL")
                or os.getenv("OPENAI_CHAT_MODEL") or os.getenv("OPENAI_MODEL"))
    if os.getenv("OPENAI_API_KEY"):
        return ChatOpenAI(model=model_id or "gpt-4o-mini", temperature=0)
    # Local LM Studio default.
    return ChatOpenAI(
        model=model_id or "local-model",
        base_url=os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1"),
        api_key=os.getenv("LMSTUDIO_API_KEY", "lm-studio"),
        temperature=0,
    )


def build_agent(system_prompt: str = DEFAULT_SYSTEM_PROMPT):
    """Construct a LangChain agent wired to the extractor tools."""
    try:
        from langchain.agents import create_agent
    except ModuleNotFoundError as e:
        raise RuntimeError(
            "LangChain agent packages missing. "
            "Run: pip install langchain langgraph langchain-openai"
        ) from e
    return create_agent(_build_model(), tools=_build_tools(),
                         system_prompt=system_prompt)


def run(prompt: str, system_prompt: str = DEFAULT_SYSTEM_PROMPT) -> str:
    """Run one extraction request through the LangChain agent, return its reply."""
    agent = build_agent(system_prompt)
    result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
    messages = result.get("messages", []) if isinstance(result, dict) else []
    if messages:
        last = messages[-1]
        return getattr(last, "content", str(last))
    return str(result)
