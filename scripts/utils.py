#!/usr/bin/env python3
"""
scripts/utils.py
Shared utilities for LLM Wiki processing scripts.
"""

import json
import os
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

# ─── State management ──────────────────────────────────────────────────────────

STATE_DIR = Path(".state")
PROCESSED_URLS_FILE = STATE_DIR / "processed_urls.json"
LAST_RUN_FILE = STATE_DIR / "last_run.json"


def ensure_state_dir():
    STATE_DIR.mkdir(parents=True, exist_ok=True)


def load_processed_urls() -> set:
    ensure_state_dir()
    if PROCESSED_URLS_FILE.exists():
        data = json.loads(PROCESSED_URLS_FILE.read_text(encoding="utf-8"))
        # Support both plain-list format (legacy) and {"urls": [...]} dict format
        if isinstance(data, list):
            return set(data)
        return set(data.get("urls", []))
    return set()


def mark_processed(url: str):
    ensure_state_dir()
    urls = load_processed_urls()
    urls.add(url.strip().rstrip("/"))
    PROCESSED_URLS_FILE.write_text(
        json.dumps(sorted(urls), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def is_processed(url: str) -> bool:
    return url.strip().rstrip("/") in load_processed_urls()


def log_run(command: str, stats: dict):
    ensure_state_dir()
    runs = []
    if LAST_RUN_FILE.exists():
        runs = json.loads(LAST_RUN_FILE.read_text())
    runs.append(
        {"command": command, "timestamp": datetime.now(timezone.utc).isoformat(), **stats}
    )
    # Keep last 100 runs
    runs = runs[-100:]
    LAST_RUN_FILE.write_text(json.dumps(runs, indent=2))


# ─── Slug generation ───────────────────────────────────────────────────────────

def slugify(text: str, max_length: int = 50) -> str:
    """Convert text to a filename-safe slug."""
    # Normalize unicode
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    # Lowercase
    text = text.lower()
    # Replace non-alphanumeric with hyphens
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    return text[:max_length]


# ─── Category detection ────────────────────────────────────────────────────────

NEWS_KEYWORDS = [
    "released", "announcing", "launch", "new version", "v1.", "v2.", "v3.",
    "update", "changelog", "breaking:", "just shipped", "available now",
]

TOOL_KEYWORDS = [
    "github.com", "library", "framework", "cli", "sdk", "api", "plugin",
    "extension", "package", "npm", "pip install", "brew install",
]

AGENT_KEYWORDS = [
    "agent", "agentic", "autonomous", "coding agent", "code agent",
    "computer use", "tool use", "function calling", "mcp", "langgraph",
    "autogen", "crewai", "multi-agent",
]

MODEL_KEYWORDS = [
    "gpt-", "claude", "gemini", "llama", "mistral", "qwen", "phi-",
    "weights", "checkpoint", "fine-tun", "gguf", "quantiz",
    "context window", "tokens", "benchmark",
]

TIP_KEYWORDS = [
    "how to", "tip:", "trick:", "best practice", "tutorial", "guide",
    "step by step", "prompting", "prompt engineering", "workflow",
]

PEOPLE_KEYWORDS = [
    "andrej karpathy", "sam altman", "dario amodei", "yann lecun",
    "george hotz", "interview", "ama", "asks me anything",
]


def detect_category(text: str) -> str:
    """Heuristic category classifier. Returns one of the wiki categories."""
    text_lower = text.lower()

    # News check first (time-sensitive)
    if any(kw in text_lower for kw in NEWS_KEYWORDS):
        return "news"

    # Agent check (before tools, as agents are a subset)
    if any(kw in text_lower for kw in AGENT_KEYWORDS):
        return "agents"

    # Tools
    if any(kw in text_lower for kw in TOOL_KEYWORDS):
        return "tools"

    # Models
    if any(kw in text_lower for kw in MODEL_KEYWORDS):
        return "models"

    # Tips
    if any(kw in text_lower for kw in TIP_KEYWORDS):
        return "tips"

    # People
    if any(kw in text_lower for kw in PEOPLE_KEYWORDS):
        return "people"

    return "concepts"  # default


# ─── URL extraction ────────────────────────────────────────────────────────────

URL_PATTERN = re.compile(
    r"https?://(?:[-\w@:%._\+~#=]{1,256})\.(?:[a-zA-Z0-9()]{1,6})\b"
    r"(?:[-\w@:%._\+~#=/?&]*)"
)

SKIP_DOMAINS = {
    "t.co", "twitter.com", "x.com", "bit.ly", "tinyurl.com",
    "pic.twitter.com", "instagram.com",
}


def extract_urls(text: str, skip_shortlinks: bool = True) -> list[str]:
    """Extract all URLs from text, optionally skipping known shortlink domains."""
    urls = URL_PATTERN.findall(text)
    if skip_shortlinks:
        urls = [u for u in urls if not any(d in u for d in SKIP_DOMAINS)]
    return list(dict.fromkeys(urls))  # deduplicate preserving order


def expand_tco(url: str) -> str:
    """Expand a t.co short URL by following the redirect."""
    import requests
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        return r.url
    except Exception:
        return url


# ─── File helpers ──────────────────────────────────────────────────────────────

def load_env():
    from dotenv import load_dotenv
    load_dotenv()


def ensure_dirs():
    """Create all required project directories."""
    dirs = [
        "inbox/clippings",
        "inbox/tweets",
        "sources/reddit",
        "sources/web",
        "sources/transcripts",
        "wiki/en/concepts",
        "wiki/en/tools",
        "wiki/en/agents",
        "wiki/en/models",
        "wiki/en/news",
        "wiki/en/tips",
        "wiki/en/people",
        "wiki/ru/concepts",
        "wiki/ru/tools",
        "wiki/ru/agents",
        "wiki/ru/models",
        "wiki/ru/news",
        "wiki/ru/tips",
        "wiki/ru/people",
        "digests/en",
        "digests/ru",
        "scripts",
        ".state",
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created {len(dirs)} directories")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        ensure_dirs()
    else:
        print("Usage: python scripts/utils.py init")
