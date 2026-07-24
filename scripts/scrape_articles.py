#!/usr/bin/env python3
"""Ingestion (Module 2): extract blog/article posts from the web into the vault inbox.

A single, source-agnostic article extractor. It DISCOVERS post URLs from any of
four discovery modes, FETCHES each post, extracts a readable Markdown body, and
writes one Obsidian-native note per post to `Inbox/Web_to_Process/`. Notes carry
YAML frontmatter (source_url, title, published, source, type) so they drop
straight into the vault and are picked up by the RAG index. Posts already written
are skipped (idempotent).

Discovery modes:
  - feed     : an RSS 2.0 or Atom feed (items -> title/link/date/summary).
  - sitemap  : an XML sitemap; keep only <loc> URLs matching --match (a substring
               or regex). Handles sitemap-index files (one level of nesting).
  - listing  : an HTML index/listing page; keep <a href> links matching --match,
               resolved against the page URL.
  - urls     : one or more explicit article URLs (positional args or --file).

For each discovered post the extractor tries a full fetch of the article HTML and
converts the main content (<article>/<main>) to Markdown. If the fetch is blocked
(e.g. a 403 bot wall) it falls back to the feed summary when one is available, so
a note is still captured with a link to the original.

Named presets bundle the discovery config for the requested sources:
    anthropic-engineering  anthropic-news  openai-research  openai-news
    ms-learn-secure-research  hbc-intro-to-r

Usage:
    python3 scripts/scrape_articles.py --source anthropic-engineering --limit 15
    python3 scripts/scrape_articles.py --source openai-news --limit 25
    python3 scripts/scrape_articles.py --feed https://example.com/rss.xml
    python3 scripts/scrape_articles.py --sitemap https://site/sitemap.xml --match /blog/
    python3 scripts/scrape_articles.py --listing https://site/posts --match /posts/
    python3 scripts/scrape_articles.py https://site/a-post https://site/another
    python3 scripts/scrape_articles.py --source anthropic-news --list   # discover only

Fetching uses curl with browser-like headers (some machines have TLS interception
that breaks urllib; some hosts 403 non-browser agents).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTDIR_DEFAULT = REPO_ROOT / "Inbox" / "Web_to_Process"

# Cap a single note's body so an outlier page (e.g. an aggregated event-schema
# reference) cannot bloat the vault/git with multi-MB notes.
MAX_BODY_CHARS = 200_000

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)


# --------------------------------------------------------------------------- #
# Presets: (discovery_mode, target, match, source_tag)
# discovery_mode in {"feed", "sitemap", "listing"}; match applies to sitemap/listing.
# --------------------------------------------------------------------------- #
class Preset:
    def __init__(self, mode: str, target: str, source: str,
                 match: str = "", type_: str = "article", enrich_feed: str = ""):
        self.mode = mode          # feed | sitemap | listing | url
        self.target = target
        self.match = match
        self.source = source
        self.type = type_
        self.enrich_feed = enrich_feed  # optional feed to backfill summaries/dates


PRESETS: dict[str, Preset] = {
    "anthropic-engineering": Preset(
        "sitemap", "https://www.anthropic.com/sitemap.xml",
        "anthropic-engineering", match=r"/engineering/", type_="article"),
    "anthropic-news": Preset(
        "sitemap", "https://www.anthropic.com/sitemap.xml",
        "anthropic-news", match=r"/news/", type_="article"),
    "openai-research": Preset(
        "sitemap", "https://openai.com/sitemap.xml/research/",
        "openai-research", type_="article",
        enrich_feed="https://openai.com/news/rss.xml"),
    "openai-news": Preset(
        "feed", "https://openai.com/news/rss.xml",
        "openai-news", type_="article"),
    "ms-learn-secure-research": Preset(
        "url",
        "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/secure-compute-for-research",
        "ms-learn", type_="doc"),
    "hbc-intro-to-r": Preset(
        "listing",
        "https://hbctraining.github.io/Intro-to-R-flipped/schedule/links-to-lessons.html",
        "hbctraining", match=r"/lessons/", type_="lesson"),
    "openai-api-reference": Preset(
        "llms",
        "https://developers.openai.com/api/reference/llms.txt",
        "openai-api-reference", match=r"/reference/resources/", type_="doc"),
}


# --------------------------------------------------------------------------- #
# Fetch
# --------------------------------------------------------------------------- #
def fetch(url: str, timeout: int = 40) -> tuple[int, str]:
    """GET `url` via curl with browser headers. Returns (http_code, body)."""
    cmd = [
        "curl", "-sSL", "--max-time", str(timeout),
        "-A", UA,
        "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "-H", "Accept-Language: en-US,en;q=0.9",
        "-w", "\n%{http_code}",
        url,
    ]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
    except Exception:
        return 0, ""
    body, _, code = out.stdout.rpartition("\n")
    try:
        return int(code.strip()), body
    except ValueError:
        return 0, out.stdout


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #
def _cdata(s: str) -> str:
    return re.sub(r"(?is)<!\[CDATA\[(.*?)\]\]>", r"\1", s)


def discover_feed(url: str) -> list[dict]:
    """Parse an RSS 2.0 or Atom feed into [{url, title, date, summary}, ...]."""
    code, body = fetch(url)
    if code != 200 or not body:
        return []
    items: list[dict] = []
    # RSS <item>
    for block in re.findall(r"(?is)<item[ >].*?</item>", body):
        link = _tag(block, "link")
        items.append({
            "url": link,
            "title": _clean(_tag(block, "title")),
            "date": _norm_date(_tag(block, "pubDate") or _tag(block, "dc:date")),
            "summary": _clean(_tag(block, "description")),
        })
    # Atom <entry>
    for block in re.findall(r"(?is)<entry[ >].*?</entry>", body):
        link = ""
        m = re.search(r'(?is)<link[^>]*href="([^"]+)"', block)
        if m:
            link = m.group(1)
        items.append({
            "url": link,
            "title": _clean(_tag(block, "title")),
            "date": _norm_date(_tag(block, "updated") or _tag(block, "published")),
            "summary": _clean(_tag(block, "summary") or _tag(block, "content")),
        })
    # dedupe by url, preserve order
    seen: set[str] = set()
    out = []
    for it in items:
        u = it["url"].strip()
        if u and u not in seen:
            seen.add(u)
            out.append(it)
    return out


def discover_sitemap(url: str, match: str) -> list[dict]:
    """Parse an XML sitemap (or sitemap index) and keep <loc> matching `match`."""
    code, body = fetch(url)
    if code != 200 or not body:
        return []
    locs = [html.unescape(m) for m in re.findall(r"(?is)<loc>\s*(.*?)\s*</loc>", body)]
    pat = re.compile(match) if match else None

    # Sitemap index: nested .xml sitemaps -> recurse one level.
    if locs and all(u.lower().endswith(".xml") for u in locs):
        collected: list[dict] = []
        for sub in locs:
            collected += discover_sitemap(sub, match)
        return collected

    return [{"url": u, "title": "", "date": "", "summary": ""}
            for u in locs if (pat.search(u) if pat else True)]


def discover_listing(url: str, match: str) -> list[dict]:
    """Extract <a href> links from an HTML page, keep those matching `match`."""
    code, body = fetch(url)
    if code != 200 or not body:
        return []
    pat = re.compile(match) if match else None
    seen: set[str] = set()
    out: list[dict] = []
    for m in re.finditer(r'(?is)<a\b[^>]*href="([^"#]+)"', body):
        href = html.unescape(m.group(1).strip())
        if href.startswith(("mailto:", "javascript:")):
            continue
        absu = urllib.parse.urljoin(url, href)
        absu = absu.split("#")[0]
        if pat and not pat.search(absu):
            continue
        if absu not in seen:
            seen.add(absu)
            out.append({"url": absu, "title": "", "date": "", "summary": ""})
    return out


def discover_llms_txt(url: str, match: str) -> list[dict]:
    """Parse an llms.txt index (Markdown link list) and keep .md links matching `match`.

    llms.txt files list a site's Markdown "twin" pages as `- [Title](URL.md): desc`.
    Fetching a twin returns clean Markdown, so notes get full text with no HTML
    conversion (see build_note's Markdown pass-through).
    """
    code, body = fetch(url)
    if code != 200 or not body:
        return []
    pat = re.compile(match) if match else None
    seen: set[str] = set()
    out: list[dict] = []
    for m in re.finditer(r"\[([^\]]*)\]\((https?://[^)]+\.md)\)\s*:?\s*([^\n]*)", body):
        title, link, summary = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        if pat and not pat.search(link):
            continue
        if link not in seen:
            seen.add(link)
            out.append({"url": link, "title": title, "date": "", "summary": summary,
                        "slug": _md_slug(link)})
    return out


def _md_slug(url: str) -> str:
    """Slug for a deep Markdown-twin URL: join path segments, drop filler words.

    Many endpoint twins end in a generic verb (create/list/retrieve), so a
    last-segment slug would collide. Keep the meaningful path context instead.
    """
    path = urllib.parse.urlparse(url).path
    path = re.sub(r"\.md$", "", path)
    parts = [p for p in path.split("/")
             if p and p not in ("api", "reference", "resources", "subresources", "methods")]
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", "-".join(parts)).strip("-")
    return slug[:120] or "doc"


# --------------------------------------------------------------------------- #
# HTML -> Markdown (readable body)
# --------------------------------------------------------------------------- #
def _tag(s: str, name: str) -> str:
    m = re.search(rf"(?is)<{name}[^>]*>(.*?)</{name}>", s)
    return _cdata(m.group(1)) if m else ""


def _clean(fragment: str) -> str:
    fragment = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", fragment)
    text = re.sub(r"(?s)<[^>]+>", " ", _cdata(fragment))
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def _norm_date(raw: str) -> str:
    raw = _clean(raw)
    if not raw:
        return ""
    # ISO 8601 already?
    m = re.match(r"(\d{4}-\d{2}-\d{2})", raw)
    if m:
        return m.group(1)
    # RFC 822 (RSS pubDate): "Thu, 23 Jul 2026 00:00:00 GMT"
    m = re.search(r"(\d{1,2})\s+([A-Za-z]{3})\w*\s+(\d{4})", raw)
    if m:
        months = {mn: i for i, mn in enumerate(
            ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
        mon = months.get(m.group(2)[:3].title())
        if mon:
            return f"{int(m.group(3)):04d}-{mon:02d}-{int(m.group(1)):02d}"
    return raw[:40]


def parse_meta(h: str) -> dict:
    def meta(*names: str) -> str:
        for n in names:
            m = re.search(
                rf'(?is)<meta[^>]*(?:property|name)="{re.escape(n)}"[^>]*content="([^"]*)"', h)
            if not m:
                m = re.search(
                    rf'(?is)<meta[^>]*content="([^"]*)"[^>]*(?:property|name)="{re.escape(n)}"', h)
            if m:
                return html.unescape(m.group(1)).strip()
        return ""

    title = meta("og:title", "twitter:title")
    if not title:
        m = re.search(r"(?is)<title>(.*?)</title>", h)
        title = html.unescape(m.group(1)).strip() if m else ""
    return {
        "title": title,
        "description": meta("og:description", "description", "twitter:description"),
        "date": _norm_date(meta("article:published_time", "og:article:published_time",
                                 "article:modified_time", "date", "og:updated_time")),
    }


_BLOCK_MAIN = re.compile(r"(?is)<article\b[^>]*>(.*?)</article>")
_BLOCK_MAIN2 = re.compile(r'(?is)<main\b[^>]*>(.*?)</main>')


def _extract_main(h: str) -> str:
    m = _BLOCK_MAIN.search(h) or _BLOCK_MAIN2.search(h)
    return m.group(1) if m else h


def html_to_markdown(fragment: str) -> str:
    """Convert a block of article HTML to a readable Markdown-ish string."""
    s = fragment
    # Drop non-content elements entirely.
    s = re.sub(r"(?is)<(script|style|svg|nav|form|header|footer|aside|figure|picture|noscript|button)\b[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?is)<!--.*?-->", " ", s)

    # Headings.
    for lvl in range(1, 7):
        s = re.sub(rf"(?is)<h{lvl}\b[^>]*>(.*?)</h{lvl}>",
                   lambda m, l=lvl: f"\n\n{'#' * l} {_inline(m.group(1))}\n\n", s)
    # Preformatted / code blocks.
    s = re.sub(r"(?is)<pre\b[^>]*>(.*?)</pre>",
               lambda m: "\n\n```\n" + _strip_inline_tags(m.group(1)) + "\n```\n\n", s)
    # List items.
    s = re.sub(r"(?is)<li\b[^>]*>(.*?)</li>",
               lambda m: f"\n- {_inline(m.group(1))}", s)
    s = re.sub(r"(?is)</(ul|ol)>", "\n\n", s)
    s = re.sub(r"(?is)<(ul|ol)\b[^>]*>", "\n", s)
    # Blockquotes.
    s = re.sub(r"(?is)<blockquote\b[^>]*>(.*?)</blockquote>",
               lambda m: "\n\n> " + _inline(m.group(1)) + "\n\n", s)
    # Paragraphs and line breaks.
    s = re.sub(r"(?is)<p\b[^>]*>(.*?)</p>",
               lambda m: f"\n\n{_inline(m.group(1))}\n\n", s)
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    s = re.sub(r"(?is)</(div|section)>", "\n\n", s)

    # Anything left: inline-convert then strip residual tags.
    s = _inline(s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)

    # Whitespace cleanup.
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _inline(fragment: str) -> str:
    """Convert inline tags (a/strong/em/code) to Markdown; keep text."""
    s = fragment
    s = re.sub(r"(?is)<a\b[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>",
               lambda m: f"[{_strip_inline_tags(m.group(2))}]({m.group(1)})", s)
    s = re.sub(r"(?is)<(strong|b)\b[^>]*>(.*?)</\1>",
               lambda m: f"**{_strip_inline_tags(m.group(2))}**", s)
    s = re.sub(r"(?is)<(em|i)\b[^>]*>(.*?)</\1>",
               lambda m: f"*{_strip_inline_tags(m.group(2))}*", s)
    s = re.sub(r"(?is)<code\b[^>]*>(.*?)</code>",
               lambda m: f"`{_strip_inline_tags(m.group(1))}`", s)
    return s


def _strip_inline_tags(fragment: str) -> str:
    return html.unescape(re.sub(r"(?s)<[^>]+>", "", fragment)).strip()


# --------------------------------------------------------------------------- #
# Note writing
# --------------------------------------------------------------------------- #
def slug_of(url: str) -> str:
    path = urllib.parse.urlparse(url).path.rstrip("/")
    base = path.split("/")[-1] or urllib.parse.urlparse(url).netloc
    base = re.sub(r"\.(html?|php|aspx?)$", "", base, flags=re.I)
    return re.sub(r"[^A-Za-z0-9._-]+", "-", base).strip("-")[:80] or "post"


def _yaml_str(v: str) -> str:
    return '"' + v.replace('"', "'") + '"'


def build_note(item: dict, source: str, type_: str) -> tuple[str, str, int]:
    """Return (note_markdown, title, word_count). Fetches the article body."""
    url = item["url"]
    code, h = fetch(url)
    body_md = ""
    meta = {"title": item.get("title", ""), "description": item.get("summary", ""),
            "date": item.get("date", "")}
    if code == 200 and h and url.split("?")[0].endswith(".md"):
        # Markdown "twin" page (e.g. an llms.txt-listed .md): use it as-is.
        body_md = h.strip()
        hm = re.match(r"\s*#\s+(.+)", body_md)
        if hm:
            meta["title"] = meta["title"] or hm.group(1).strip()
            # Drop the leading H1; build_note re-adds the title as the heading.
            body_md = body_md[hm.end():].lstrip("\n")
        # Some sites publish stub twins (a pointer, not the real page). If so,
        # fall back to the rendered HTML page (the .md URL minus the suffix).
        if len(body_md) < 400 or "generated by Stainless" in body_md:
            canonical = url[: -len(".md")]
            code2, h2 = fetch(canonical)
            if code2 == 200 and h2 and "<html" in h2.lower():
                alt = html_to_markdown(_extract_main(h2))
                if len(alt) > len(body_md):
                    m = parse_meta(h2)
                    meta["title"] = m["title"] or meta["title"]
                    meta["description"] = m["description"] or meta["description"]
                    meta["date"] = m["date"] or meta["date"]
                    body_md = alt
                    url = canonical
    elif code == 200 and h and "<html" in h.lower():
        m = parse_meta(h)
        meta["title"] = m["title"] or meta["title"]
        meta["description"] = m["description"] or meta["description"]
        meta["date"] = m["date"] or meta["date"]
        body_md = html_to_markdown(_extract_main(h))

    fetched_full = bool(body_md) and len(body_md) > 200
    if not fetched_full:
        # Fall back to the feed/listing summary.
        body_md = item.get("summary", "") or meta["description"]

    title = meta["title"] or slug_of(url).replace("-", " ").title()
    today = _dt.date.today().isoformat()

    fm = [
        "---",
        f"source_url: {url}",
        f"title: {_yaml_str(title)}",
    ]
    if meta["date"]:
        fm.append(f"published: {_yaml_str(meta['date'])}")
    fm += [
        f"scraped: {today}",
        f"type: {type_}",
        f"source: {source}",
        f"full_text: {str(fetched_full).lower()}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if meta["description"] and meta["description"] not in body_md:
        fm += [f"> {meta['description']}", ""]
    if not fetched_full:
        fm += [f"_Full text not captured (source returned HTTP {code or 'error'}); "
               f"summary only. Read the original at the source link._", ""]

    body_md = body_md or "_No extractable content._"
    if len(body_md) > MAX_BODY_CHARS:
        body_md = (body_md[:MAX_BODY_CHARS].rstrip()
                   + f"\n\n_Content truncated at {MAX_BODY_CHARS} characters; "
                   f"read the full page at the source link._")
    note = "\n".join(fm) + body_md.rstrip() + f"\n\n---\nSource: {url}\n"
    return note, title, len(body_md.split())


def process(item: dict, outdir: Path, source: str, type_: str) -> str:
    url = item["url"]
    slug = item.get("slug") or slug_of(url)
    out_path = outdir / f"{source}--{slug}.md"
    if out_path.exists():
        return f"SKIP  {out_path.name}  (already scraped)"
    note, title, words = build_note(item, source, type_)
    out_path.write_text(note, encoding="utf-8")
    return f"OK    {out_path.name}  ({words} words)  {title[:60]!r}"


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _canon(url: str) -> str:
    return url.split("#")[0].rstrip("/")


def enrich(items: list[dict], feed_url: str) -> list[dict]:
    """Backfill empty title/date/summary on items from a feed, matched by URL."""
    feed = {_canon(it["url"]): it for it in discover_feed(feed_url)}
    for it in items:
        src = feed.get(_canon(it["url"]))
        if src:
            it["title"] = it.get("title") or src.get("title", "")
            it["date"] = it.get("date") or src.get("date", "")
            it["summary"] = it.get("summary") or src.get("summary", "")
    return items


def discover(args) -> tuple[list[dict], str, str]:
    """Return (items, source_tag, type_) from the chosen discovery mode."""
    if args.source:
        return collect_source(args.source)
    if args.feed:
        return discover_feed(args.feed), args.source_tag, args.type
    if args.sitemap:
        return discover_sitemap(args.sitemap, args.match or ""), args.source_tag, args.type
    if args.listing:
        return discover_listing(args.listing, args.match or ""), args.source_tag, args.type
    if args.llms_txt:
        return discover_llms_txt(args.llms_txt, args.match or ""), args.source_tag, args.type
    # explicit urls
    urls = list(args.urls)
    if args.file:
        urls += [ln.strip() for ln in Path(args.file).read_text().splitlines() if ln.strip()]
    return [{"url": u, "title": "", "date": "", "summary": ""} for u in urls], \
        args.source_tag, args.type


def collect_source(source: str, limit: int = 0) -> tuple[list[dict], str, str]:
    """Discover posts for a named preset. Returns (items, source_tag, type_)."""
    if source not in PRESETS:
        raise ValueError(f"unknown source {source!r}; choose from {sorted(PRESETS)}")
    p = PRESETS[source]
    if p.mode == "feed":
        items = discover_feed(p.target)
        if p.match:
            pat = re.compile(p.match)
            items = [it for it in items if pat.search(it["url"])]
    elif p.mode == "sitemap":
        items = discover_sitemap(p.target, p.match)
    elif p.mode == "url":
        items = [{"url": p.target, "title": "", "date": "", "summary": ""}]
    elif p.mode == "llms":
        items = discover_llms_txt(p.target, p.match)
    else:
        items = discover_listing(p.target, p.match)
    if p.enrich_feed and items:
        items = enrich(items, p.enrich_feed)
    if limit:
        items = items[:limit]
    return items, p.source, p.type


def scrape_source(source: str, limit: int = 0, outdir: Path | None = None) -> list[str]:
    """Extract posts for a named preset into the inbox. Returns per-post results."""
    items, tag, type_ = collect_source(source, limit)
    outdir = outdir or OUTDIR_DEFAULT
    outdir.mkdir(parents=True, exist_ok=True)
    return [process(it, outdir, tag, type_) for it in items]


def scrape_urls(urls: list[str], source_tag: str = "web", type_: str = "article",
                outdir: Path | None = None) -> list[str]:
    """Extract explicit article URLs into the inbox. Returns per-post results."""
    outdir = outdir or OUTDIR_DEFAULT
    outdir.mkdir(parents=True, exist_ok=True)
    items = [{"url": u, "title": "", "date": "", "summary": ""} for u in urls]
    return [process(it, outdir, source_tag, type_) for it in items]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="*", help="explicit article URLs")
    ap.add_argument("--source", choices=sorted(PRESETS), help="named source preset")
    ap.add_argument("--feed", help="RSS/Atom feed URL to discover posts from")
    ap.add_argument("--sitemap", help="XML sitemap URL to discover posts from")
    ap.add_argument("--listing", help="HTML index/listing URL to discover posts from")
    ap.add_argument("--llms-txt", dest="llms_txt",
                    help="llms.txt index URL to discover Markdown-twin (.md) pages from")
    ap.add_argument("--match", help="substring/regex filter for --sitemap/--listing/--llms-txt")
    ap.add_argument("--file", help="file with one article URL per line")
    ap.add_argument("--limit", type=int, default=0, help="max posts to process (0 = all)")
    ap.add_argument("--source-tag", default="web", help="source: value in frontmatter")
    ap.add_argument("--type", default="article", help="type: value in frontmatter")
    ap.add_argument("--outdir", help=f"output dir (default {OUTDIR_DEFAULT})")
    ap.add_argument("--list", action="store_true",
                    help="only print discovered post URLs, do not fetch/write")
    args = ap.parse_args(argv)

    if not any([args.source, args.feed, args.sitemap, args.listing, args.llms_txt,
                args.urls, args.file]):
        ap.error("provide --source, --feed, --sitemap, --listing, --llms-txt, --file, or URLs")

    items, source, type_ = discover(args)
    if args.limit:
        items = items[: args.limit]

    if args.list:
        print(f"Discovered {len(items)} post(s):")
        for it in items:
            print(it["url"])
        return 0

    outdir = Path(args.outdir).expanduser() if args.outdir else OUTDIR_DEFAULT
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"{len(items)} post(s) [{source}] -> {outdir}\n")
    if not items:
        print("Nothing discovered. Check the source / feed / match filter.")
        return 1
    results = [process(it, outdir, source, type_) for it in items]
    for line in results:
        print(line)
    return 1 if any(r.startswith("FAIL") for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
