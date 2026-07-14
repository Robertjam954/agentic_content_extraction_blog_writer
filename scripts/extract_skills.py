#!/usr/bin/env python3
"""Ingestion (Module 2): extract installed Azure skills into the vault inbox.

The Azure skills listed in the skills manifest are installed locally under
.claude/skills/<name>/SKILL.md (sourced from github.com/microsoft/azure-skills).
This reads each SKILL.md from the local cache, carries over the skill's own
metadata, records GitHub provenance, and writes a clean Markdown note to
Inbox/Skills_to_Process/. Skills already extracted are skipped.

Usage:
    python3 scripts/extract_skills.py                 # extract the manifest set
    python3 scripts/extract_skills.py NAME [NAME ...] # extract specific skills
"""
from __future__ import annotations

import datetime as _dt
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
OUTDIR = REPO_ROOT / "Inbox" / "Skills_to_Process"

SOURCE = "microsoft/azure-skills"
SOURCE_URL = "https://github.com/microsoft/azure-skills"
SKILL_PATH_TMPL = ".github/plugins/azure-skills/skills/{name}/SKILL.md"

# The skills named in the manifest the user provided.
MANIFEST_SKILLS = [
    "microsoft-foundry", "airunway-aks-setup", "appinsights-instrumentation",
    "azure-ai", "azure-aigateway", "azure-cloud-migrate", "azure-compliance",
    "azure-compute", "azure-cost", "azure-deploy", "azure-diagnostics",
    "azure-enterprise-infra-planner", "azure-hosted-copilot-sdk",
    "azure-kubernetes", "azure-kusto", "azure-messaging", "azure-prepare",
    "azure-quotas", "azure-rbac", "azure-reliability", "azure-resource-lookup",
    "azure-resource-visualizer", "azure-storage", "azure-upgrade",
    "azure-validate", "entra-agent-id", "entra-app-registration",
    "python-appservice-deploy",
]


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, body) splitting on the leading --- ... ---."""
    m = re.match(r"(?s)^\s*---\n(.*?)\n---\n?(.*)$", text)
    if m:
        return m.group(1), m.group(2).lstrip("\n")
    return "", text


def field(fm: str, key: str) -> str:
    """Grab a top-level or nested `key: value` from a frontmatter block."""
    m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.*)$", fm)
    if not m:
        return ""
    return m.group(1).strip().strip('"').strip("'")


def extras_of(name: str) -> list[str]:
    d = SKILLS_DIR / name
    skip = {"SKILL.md", ".gitignore", "LICENSE.txt"}
    return sorted(c.name for c in d.iterdir() if c.name not in skip)


def process(name: str) -> str:
    src = SKILLS_DIR / name / "SKILL.md"
    if not src.is_file():
        return f"FAIL  {name}  (no local SKILL.md at {src})"
    out_path = OUTDIR / f"{name}.md"
    if out_path.exists():
        return f"SKIP  {name}  (already extracted)"

    raw = src.read_text(encoding="utf-8", errors="ignore")
    fm, body = split_frontmatter(raw)
    description = field(fm, "description")
    license_ = field(fm, "license")
    author = field(fm, "author")
    version = field(fm, "version")
    extras = extras_of(name)
    today = _dt.date.today().isoformat()

    header = [
        "---",
        f"skill: {name}",
        f"source: {SOURCE}",
        f"source_url: {SOURCE_URL}",
        f"skill_path: {SKILL_PATH_TMPL.format(name=name)}",
    ]
    if license_:
        header.append(f"license: {license_}")
    if author:
        header.append(f"author: {author}")
    if version:
        header.append(f'version: "{version}"')
    if description:
        safe = description.replace('"', "'")
        header.append(f'description: "{safe}"')
    header.append(f"has_references: {'true' if extras else 'false'}")
    if extras:
        header.append(f"local_extras: [{', '.join(extras)}]")
    header += [f"extracted: {today}", "type: skill_doc", "---", ""]

    note = "\n".join(header) + body.rstrip() + "\n"
    out_path.write_text(note, encoding="utf-8")
    wc = len(body.split())
    tag = f"  (+extras: {', '.join(extras)})" if extras else ""
    return f"OK    {name:34} -> {out_path.name}  ({wc}w){tag}"


def main(argv: list[str]) -> int:
    names = argv or MANIFEST_SKILLS
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"Extracting {len(names)} skill(s) from {SKILLS_DIR} -> {OUTDIR}\n")
    results = [process(n) for n in names]
    for line in results:
        print(line)
    return 1 if any(r.startswith("FAIL") for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
