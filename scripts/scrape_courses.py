#!/usr/bin/env python3
"""Ingestion (Module 2): scrape zerotocloud (Teachable) course pages to Markdown.

The public course pages on learn.zerotocloud.co are server-rendered Teachable
sales pages. They expose the course title, overview, price, and full curriculum
outline (sections + lecture names). The actual paid lessons are behind a paywall
and are NOT captured. Each page is written as a clean Markdown note to
Inbox/Web_to_Process/, skipping any slug already scraped.

Usage:
    python3 scripts/scrape_courses.py                 # scrape the default set
    python3 scripts/scrape_courses.py URL [URL ...]   # scrape specific pages

Fetching uses curl (this machine's urllib is broken by TLS interception).
"""
from __future__ import annotations

import datetime as _dt
import html
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTDIR = REPO_ROOT / "Inbox" / "Web_to_Process"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

# The set requested (learn.zerotocloud.co = Teachable, server-rendered).
DEFAULT_URLS = [
    "https://learn.zerotocloud.co/p/5-beginner-aws-cloud-projects",
    "https://learn.zerotocloud.co/p/5-intermediate-aws-cloud-projects",
    "https://learn.zerotocloud.co/p/5-advanced-aws-cloud-projects",
    "https://learn.zerotocloud.co/p/ai-practitioner-notes",
    "https://learn.zerotocloud.co/p/cloud-practitioner-notes",
    "https://learn.zerotocloud.co/p/solutions-architect-associate-notes",
    "https://learn.zerotocloud.co/p/aws-cloud-practitioner-practice-tests",
    "https://learn.zerotocloud.co/p/aws-solutions-architect-associate-practice-tests",
    "https://learn.zerotocloud.co/p/learning-path-cloud-support-engineer",
    "https://learn.zerotocloud.co/p/learning-path-solutions-architect",
    "https://learn.zerotocloud.co/p/learning-path-cloud-engineer",
    "https://learn.zerotocloud.co/p/learning-path-cloud-ai-ml-engineer",
    "https://learn.zerotocloud.co/p/learning-path-cloud-security-engineer",
    "https://learn.zerotocloud.co/p/aws-interview-mastery",
    "https://learn.zerotocloud.co/p/the-part-time-tech-youtuber",
]


def fetch(url: str) -> str | None:
    try:
        out = subprocess.run(
            ["curl", "-fsSL", "--max-time", "40", "-A", UA, url],
            capture_output=True, text=True, timeout=50,
        )
        return out.stdout if out.returncode == 0 and out.stdout else None
    except Exception:
        return None


def _strip_tags(fragment: str) -> str:
    fragment = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", fragment)
    text = re.sub(r"(?s)<[^>]+>", " ", fragment)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def parse_title(h: str) -> str:
    m = re.search(r'(?is)<meta[^>]*property="og:title"[^>]*content="([^"]*)"', h)
    if m:
        return html.unescape(m.group(1)).strip()
    m = re.search(r"(?is)<title>(.*?)</title>", h)
    return html.unescape(m.group(1)).strip() if m else ""


def parse_price(h: str) -> str:
    # Covers single courses ("Enroll in Course for $69") and bundles/learning
    # paths ("Enroll Now for $299").
    m = re.search(r"(?is)Enroll(?:\s+in\s+Course|\s+Now)?\s+for\s*(\$[\d,]+(?:\.\d+)?)", h)
    if m:
        return m.group(1)
    if re.search(r"(?is)Enroll(?:\s+in\s+Course|\s+Now)?\s+for\s*Free", h):
        return "Free"
    return ""


def parse_overview(h: str) -> str:
    """Visible text from the top of the page up to the curriculum block."""
    body = h
    cut = re.search(r"(?is)Course Content", body)
    if cut:
        body = body[: cut.start()]
    text = _strip_tags(body)
    # Drop the leading nav/login noise and the repeated title.
    text = re.sub(r"^.*?(Login|Log In)\s*", "", text, count=1)
    # Trim boilerplate CTA fragments.
    text = re.sub(r"\s*Enroll in Course.*$", "", text).strip()
    return text[:1500]


def parse_curriculum(h: str) -> list[tuple[str, list[str]]]:
    """Return [(section_name, [lecture_name, ...]), ...] in document order."""
    # Tokenise section titles and lecture links with their positions.
    events: list[tuple[int, str, str]] = []
    for m in re.finditer(
        r"(?is)<div[^>]*block__curriculum__section__title[^>]*>(.*?)</div>\s*</div>",
        h,
    ):
        name = _clean_section(m.group(1))
        if name:
            events.append((m.start(), "section", name))
    for m in re.finditer(
        r"(?is)<a[^>]*block__curriculum__section__list__item__link[^>]*>(.*?)</a>",
        h,
    ):
        name = _clean_lecture(m.group(1))
        if name:
            events.append((m.start(), "lecture", name))
    events.sort(key=lambda e: e[0])

    sections: list[tuple[str, list[str]]] = []
    for _pos, kind, name in events:
        if kind == "section":
            sections.append((name, []))
        else:
            if not sections:
                sections.append(("(unsectioned)", []))
            sections[-1][1].append(name)
    return sections


def _clean_section(fragment: str) -> str:
    # Remove the lock icon and the drip-date sub-block, then strip tags.
    fragment = re.sub(r"(?is)<span[^>]*lock-icon.*?</span>", " ", fragment)
    fragment = re.sub(r"(?is)<div[^>]*days-to-drip.*", " ", fragment)
    return _strip_tags(fragment)


def _clean_lecture(fragment: str) -> str:
    text = _strip_tags(fragment)
    # Teachable appends a status word to each lecture link.
    text = re.sub(r"\s*(Start|Preview)\s*$", "", text).strip()
    return text


def slug_of(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def process(url: str) -> str:
    slug = slug_of(url)
    out_path = OUTDIR / f"{slug}.md"
    if out_path.exists():
        return f"SKIP  {slug}  (already scraped)"
    h = fetch(url)
    if not h:
        return f"FAIL  {slug}  (fetch failed)"
    title = parse_title(h)
    price = parse_price(h)
    overview = parse_overview(h)
    curriculum = parse_curriculum(h)
    n_lect = sum(len(l) for _, l in curriculum)

    today = _dt.date.today().isoformat()
    lines = [
        "---",
        f"source_url: {url}",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f'price: "{price}"',
        f"scraped: {today}",
        "type: course_overview",
        "source: zerotocloud",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if overview:
        lines += ["## Overview", "", overview, ""]
    if curriculum:
        lines += ["## Curriculum", ""]
        for section, lectures in curriculum:
            lines.append(f"### {section}")
            lines += [f"- {lec}" for lec in lectures] or ["- (no lectures listed)"]
            lines.append("")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return (
        f"OK    {slug}  -> {out_path.name}  "
        f"({len(curriculum)} sections, {n_lect} lectures) {title!r}"
    )


def main(argv: list[str]) -> int:
    urls = argv or DEFAULT_URLS
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"Scraping {len(urls)} page(s) -> {OUTDIR}\n")
    results = [process(u) for u in urls]
    for line in results:
        print(line)
    return 1 if any(r.startswith("FAIL") for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
