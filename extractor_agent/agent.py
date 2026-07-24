"""Microsoft Agent Framework orchestration over the content extractors.

This wraps the deterministic extractors in `actions.py` as tools on a Microsoft
Agent Framework agent (https://learn.microsoft.com/en-us/agent-framework/agents/),
so extraction can be driven in natural language, e.g.:

    "Extract the 5 latest Anthropic engineering posts and OpenAI research posts,
     then grab transcripts from the @zenvanriel channel."

The agent decides which extractor tools to call and with what arguments; the tools
still do deterministic, idempotent fetching into `Inbox/`. The deterministic path
(`actions.py` / the `scripts/`) needs no model; only this orchestration layer does.

This project is local-first: the vault (Obsidian) is the database and the default
model backend is a local LM Studio server. Cloud backends stay available as opt-in
options. Backend selection (by environment):
  - Azure OpenAI : if AZURE_OPENAI_ENDPOINT is set (+ AZURE_OPENAI_CHAT_DEPLOYMENT_NAME;
                   auth via AZURE_OPENAI_API_KEY or `az login` credential).
  - OpenAI cloud : else if OPENAI_API_KEY is set (optional OPENAI_CHAT_MODEL_ID).
  - LM Studio    : otherwise (default). Local OpenAI-compatible server at
                   LMSTUDIO_BASE_URL (default http://localhost:1234/v1); load a model
                   in LM Studio and set OPENAI_CHAT_MODEL_ID/LMSTUDIO_MODEL to its id.

Requires (only for the live agent):
    pip install agent-framework-core agent-framework-openai   # LM Studio / OpenAI
    pip install agent-framework-core agent-framework-azure-ai # Azure OpenAI
"""
from __future__ import annotations

import os

from .actions import ACTIONS

DEFAULT_INSTRUCTIONS = (
    "You are a content-extraction orchestrator for an Obsidian knowledge vault. "
    "Use the provided tools to extract blog posts, articles, YouTube transcripts, "
    "and Google Docs into the vault inbox. Prefer the named source presets from "
    "list_sources for the known blogs. Respect any post limits the user gives; "
    "default to a small limit when unsure. After the tools run, report a concise "
    "summary of what was written, skipped, or failed. Never invent results - only "
    "report what the tools return."
)


def build_agent(instructions: str = DEFAULT_INSTRUCTIONS):
    """Construct a Microsoft Agent Framework agent wired to the extractor tools.

    Picks Azure OpenAI when AZURE_OPENAI_ENDPOINT is set, else OpenAI cloud when
    OPENAI_API_KEY is set, else a local LM Studio server (the default). Raises a
    clear error if the needed client package is missing.
    """
    client = _build_chat_client()
    return client.as_agent(
        name="content-extractor",
        instructions=instructions,
        tools=list(ACTIONS),
    )


def _model_id(default: str) -> str:
    return (os.getenv("OPENAI_CHAT_MODEL_ID") or os.getenv("LMSTUDIO_MODEL")
            or os.getenv("OPENAI_CHAT_MODEL") or os.getenv("OPENAI_MODEL") or default)


def _build_chat_client():
    # 1. Azure OpenAI (opt-in).
    if os.getenv("AZURE_OPENAI_ENDPOINT"):
        try:
            from agent_framework.azure import AzureOpenAIChatClient
        except ModuleNotFoundError as e:
            raise RuntimeError(
                "Azure backend selected (AZURE_OPENAI_ENDPOINT set) but the client "
                "package is missing. Run: pip install agent-framework-azure-ai"
            ) from e
        return AzureOpenAIChatClient()

    try:
        from agent_framework.openai import OpenAIChatClient
    except ModuleNotFoundError as e:
        raise RuntimeError(
            "Model client package missing. Run: pip install agent-framework-openai"
        ) from e

    # 2. OpenAI cloud (opt-in): an API key is present.
    if os.getenv("OPENAI_API_KEY"):
        return OpenAIChatClient(model=_model_id("gpt-4o-mini"))

    # 3. Local LM Studio (default): OpenAI-compatible server, no real key needed.
    base_url = os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
    return OpenAIChatClient(
        model=_model_id("local-model"),
        api_key=os.getenv("LMSTUDIO_API_KEY", "lm-studio"),
        base_url=base_url,
    )


async def run(prompt: str, instructions: str = DEFAULT_INSTRUCTIONS) -> str:
    """Run one extraction request through the agent and return its text response."""
    agent = build_agent(instructions)
    response = await agent.run(prompt)
    return getattr(response, "text", str(response))
