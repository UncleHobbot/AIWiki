# -*- coding: utf-8 -*-
"""
Wiki quality test suite.

Run (fast, default — skips URL checks):
    pytest tests/test_wiki.py -v

Run including external URL reachability:
    pytest tests/test_wiki.py -v -m "slow or not slow"
    pytest tests/test_wiki.py -v --run-slow

Single-category smoke check:
    pytest tests/test_wiki.py -v -k frontmatter
    pytest tests/test_wiki.py -v -k wikilinks
"""

import json
import re
import time
from pathlib import Path

import frontmatter
import pytest
import requests

# ── Project roots ──────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
INDEX_FILE = ROOT / "index.md"
URL_CACHE_FILE = ROOT / ".state" / "url_check_cache.json"

# ── Schema constants ───────────────────────────────────────────────────────────
REQUIRED_FM_KEYS = {"title", "title_ru", "category", "tags", "updated", "sources"}
VALID_CATEGORIES = {"concepts", "tools", "agents", "models", "news", "tips", "people"}

# Exact divider that separates EN from RU in every wiki file
RU_DIVIDER_RE = re.compile(r"---\s*\n<!--\s*RU\s*-->")

# Wikilink pattern: [[slug]], [[slug|alias]], [[slug#section]] — captures only slug
WIKILINK_RE = re.compile(r"\[\[([^\]|#\n]+?)(?:[|#][^\]]+)?\]\]")

# Wiki slugs are always ASCII-lowercase + hyphens, no spaces, no Cyrillic.
# This lets us skip [[wiki links]], [[Концепция множества]], etc. that appear
# as prose examples in entries that explain Obsidian wiki-link syntax.
_SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,54}$")

# How long to trust a cached URL result (7 days)
URL_CACHE_TTL = 7 * 24 * 3600

# Minimum chars in RU section to be considered non-trivial
RU_MIN_CHARS = 100

# HTTP headers for URL reachability probes
_UA = "Mozilla/5.0 (compatible; LLMWikiQA/1.0)"
_PROBE_HEADERS = {"User-Agent": _UA}


# ── Helpers ────────────────────────────────────────────────────────────────────

def _all_wiki_files() -> list[Path]:
    return sorted(WIKI_DIR.rglob("*.md"))


def _all_slugs() -> set[str]:
    return {p.stem for p in _all_wiki_files()}


def _extract_wikilinks(text: str) -> list[str]:
    """Return only slug-shaped wikilinks, ignoring prose examples and Cyrillic text.

    Strips fenced code blocks and inline code spans first so that entries
    which explain [[wiki link]] syntax don't produce false positive failures.
    """
    # Remove fenced code blocks (``` ... ```)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Remove inline code spans (`...`)
    text = re.sub(r"`[^`\n]+`", "", text)
    candidates = WIKILINK_RE.findall(text)
    # Keep only strings that look like real wiki slugs (lowercase ASCII + hyphens)
    return [c for c in candidates if _SLUG_RE.match(c)]


def _load_url_cache() -> dict:
    if URL_CACHE_FILE.exists():
        try:
            return json.loads(URL_CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def _save_url_cache(cache: dict) -> None:
    URL_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    URL_CACHE_FILE.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def _parse_frontmatter(path: Path):
    """Return (post, error_string). error_string is None on success."""
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return None, "file does not start with '---' (missing frontmatter)"
    try:
        post = frontmatter.loads(raw)
        return post, None
    except Exception as exc:
        return None, f"YAML parse error: {exc}"


# ── Session-scoped fixtures ────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def existing_slugs() -> set[str]:
    return _all_slugs()


@pytest.fixture(scope="session")
def index_content() -> str:
    assert INDEX_FILE.exists(), f"index.md not found at {INDEX_FILE}"
    return INDEX_FILE.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def indexed_slugs(index_content) -> set[str]:
    return set(_extract_wikilinks(index_content))


# ── Parametrised file list (collected once at module import) ───────────────────

_WIKI_FILES = _all_wiki_files()
_IDS = [p.stem for p in _WIKI_FILES]


# ══════════════════════════════════════════════════════════════════════════════
# Per-entry tests
# ══════════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("path", _WIKI_FILES, ids=_IDS)
def test_frontmatter_valid(path: Path) -> None:
    """Every entry must have valid YAML frontmatter with all required fields."""
    post, err = _parse_frontmatter(path)
    assert post is not None, err

    meta = post.metadata
    missing = REQUIRED_FM_KEYS - set(meta.keys())
    assert not missing, (
        f"Missing frontmatter keys: {sorted(missing)}\n"
        f"Present keys: {sorted(meta.keys())}"
    )

    cat = meta.get("category")
    assert cat in VALID_CATEGORIES, (
        f"Invalid category '{cat}'. Must be one of: {sorted(VALID_CATEGORIES)}"
    )

    sources = meta.get("sources") or []
    assert isinstance(sources, list) and len(sources) > 0, (
        "sources must be a non-empty YAML list"
    )

    tags = meta.get("tags") or []
    assert isinstance(tags, list) and len(tags) > 0, (
        "tags must be a non-empty YAML list"
    )


@pytest.mark.parametrize("path", _WIKI_FILES, ids=_IDS)
def test_has_ru_section(path: Path) -> None:
    """Every entry must contain the exact RU divider followed by substantive content."""
    raw = path.read_text(encoding="utf-8")

    match = RU_DIVIDER_RE.search(raw)
    assert match, (
        "Missing RU divider. Expected exactly:\n"
        "    ---\n"
        "    <!-- RU -->\n"
        "between English and Russian sections."
    )

    ru_body = raw[match.end():].strip()
    assert len(ru_body) >= RU_MIN_CHARS, (
        f"Russian section is suspiciously short ({len(ru_body)} chars < {RU_MIN_CHARS}). "
        "Run /wiki-check to regenerate it."
    )

    # Must contain at least one Russian heading
    assert re.search(r"##\s+[А-ЯЁа-яё]", ru_body), (
        "Russian section has no Cyrillic headings. "
        "Expected at least '## Краткое описание' or similar."
    )


@pytest.mark.parametrize("path", _WIKI_FILES, ids=_IDS)
def test_wikilinks_resolve(path: Path, existing_slugs: set[str]) -> None:
    """All [[wikilinks]] inside an entry must point to existing wiki files."""
    raw = path.read_text(encoding="utf-8")
    linked = _extract_wikilinks(raw)
    if not linked:
        return

    broken = [s for s in linked if s not in existing_slugs]
    assert not broken, (
        f"Broken wikilinks ({len(broken)}):\n" +
        "\n".join(f"  [[{s}]]" for s in broken)
    )


# ══════════════════════════════════════════════════════════════════════════════
# Vault-level tests
# ══════════════════════════════════════════════════════════════════════════════

def test_index_contains_all_entries(indexed_slugs: set[str]) -> None:
    """index.md must contain a [[wikilink]] for every file in wiki/."""
    actual = _all_slugs()
    missing = actual - indexed_slugs
    assert not missing, (
        f"Entries present on disk but absent from index.md ({len(missing)}):\n" +
        "\n".join(f"  [[{s}]]" for s in sorted(missing)) +
        "\nRun /wiki-index to rebuild."
    )


def test_index_has_no_ghost_entries(indexed_slugs: set[str]) -> None:
    """index.md must not reference slugs whose .md files do not exist."""
    actual = _all_slugs()
    ghosts = indexed_slugs - actual
    assert not ghosts, (
        f"index.md links to non-existent entries ({len(ghosts)}):\n" +
        "\n".join(f"  [[{s}]]" for s in sorted(ghosts)) +
        "\nRun /wiki-index to rebuild."
    )


def test_no_orphan_pages() -> None:
    """Every wiki page must be referenced by index.md or at least one other wiki page.

    Counts backlinks from both EN and RU sections but deduplicates per-file,
    matching the behaviour of scripts/obs.py.
    """
    referenced: set[str] = set()

    # Links in index.md
    referenced.update(_extract_wikilinks(INDEX_FILE.read_text(encoding="utf-8")))

    # Links inside wiki entries — deduplicate per file to match obs.py behaviour
    for f in _all_wiki_files():
        raw = f.read_text(encoding="utf-8")
        # Use a set per file so EN+RU duplicate links count only once
        referenced.update(set(_extract_wikilinks(raw)))

    orphans = _all_slugs() - referenced
    assert not orphans, (
        f"Orphan pages — not linked from index.md or any other entry ({len(orphans)}):\n" +
        "\n".join(f"  {s}" for s in sorted(orphans)) +
        "\nAdd them to Related Entries of semantically close pages."
    )


# ══════════════════════════════════════════════════════════════════════════════
# External URL reachability (slow — skipped by default)
# ══════════════════════════════════════════════════════════════════════════════

@pytest.mark.slow
def test_external_urls_reachable() -> None:
    """All source URLs in frontmatter must return HTTP 2xx.

    Results are cached in .state/url_check_cache.json for 7 days to avoid
    hammering external servers on every commit.

    Skip this test in normal runs:  pytest -m "not slow"   (the default)
    Force a full re-check:          pytest -m slow --cache-clear
    """
    cache = _load_url_cache()
    now = time.time()
    dirty = False
    failures: list[str] = []

    for path in _all_wiki_files():
        post, err = _parse_frontmatter(path)
        if post is None:
            continue

        for url in (post.metadata.get("sources") or []):
            if not isinstance(url, str) or not url.startswith("http"):
                continue

            entry = cache.get(url, {})
            age = now - entry.get("ts", 0)

            if age < URL_CACHE_TTL:
                status = entry["status"]
            else:
                status = _probe_url(url)
                cache[url] = {"status": status, "ts": now}
                dirty = True
                time.sleep(0.25)  # polite rate-limit

            if status == 0 or status >= 400:
                failures.append(f"  [{path.stem}] {url}  →  HTTP {status or 'TIMEOUT/ERROR'}")

    if dirty:
        _save_url_cache(cache)

    assert not failures, (
        f"Dead or unreachable source URLs ({len(failures)}):\n" + "\n".join(failures)
    )


def _probe_url(url: str) -> int:
    """Return HTTP status code, or 0 on connection failure."""
    try:
        r = requests.head(url, timeout=12, allow_redirects=True, headers=_PROBE_HEADERS)
        # Some servers reject HEAD; retry as GET
        if r.status_code in (403, 405):
            r = requests.get(
                url, timeout=12, allow_redirects=True,
                headers=_PROBE_HEADERS, stream=True,
            )
            r.close()
        return r.status_code
    except requests.RequestException:
        return 0
