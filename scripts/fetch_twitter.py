#!/usr/bin/env python3
"""
scripts/fetch_twitter.py
Parse Twitter/X post dumps and expand URLs.
Does not require Twitter API — works with manually saved tweet text.
Optional: RapidAPI key for fetching tweet metadata by URL.
"""

import argparse
import io
import json
import os
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import requests
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

URL_PATTERN = re.compile(
    r"https?://(?:[-\w@:%._\+~#=]{1,256})\.(?:[a-zA-Z0-9()]{1,6})\b"
    r"(?:[-\w@:%_\+~#=/?&]*)"
)

TCO_PATTERN = re.compile(r"https://t\.co/\w+")


def expand_url(url: str) -> str:
    """Follow redirects to get the final URL."""
    try:
        r = requests.head(url, allow_redirects=True, timeout=8,
                          headers={"User-Agent": "Mozilla/5.0"})
        return r.url
    except Exception:
        return url


def expand_urls_in_text(text: str) -> tuple[str, list[dict]]:
    """
    Find all t.co links in text, expand them.
    Returns (text_with_expanded_urls, list_of_url_objects).
    """
    url_objects = []
    expanded_text = text

    tco_urls = list(dict.fromkeys(TCO_PATTERN.findall(text)))
    for tco in tco_urls:
        expanded = expand_url(tco)
        if expanded != tco:
            expanded_text = expanded_text.replace(tco, expanded)
        url_objects.append({"original": tco, "expanded": expanded})

    # Also capture any non-t.co URLs already in the text
    all_urls = URL_PATTERN.findall(expanded_text)
    for url in all_urls:
        if not any(o["expanded"] == url for o in url_objects):
            url_objects.append({"original": url, "expanded": url})

    return expanded_text, url_objects


def parse_tweet_block(block: str) -> dict | None:
    """Parse a single tweet text block into a structured dict."""
    block = block.strip()
    if not block:
        return None

    # Try to detect author line (common formats: "@handle:", "Name (@handle):", etc.)
    author = ""
    author_patterns = [
        r"^@(\w+):?\s*\n",
        r"^([^(\n]+)\s*\(@(\w+)\):?\s*\n",
    ]
    for pat in author_patterns:
        m = re.match(pat, block, re.MULTILINE)
        if m:
            author = m.group(1) if len(m.groups()) == 1 else f"{m.group(1)} (@{m.group(2)})"
            block = block[m.end():].strip()
            break

    expanded_text, urls = expand_urls_in_text(block)

    # Filter out Twitter/X self-links from URL list
    external_urls = [
        u["expanded"] for u in urls
        if not any(d in u["expanded"] for d in ["twitter.com", "x.com", "t.co", "pic.twitter.com"])
    ]

    return {
        "author": author,
        "text": expanded_text,
        "original_text": block,
        "external_urls": external_urls,
        "all_urls": urls,
    }


def parse_tweet_file(path: Path) -> list[dict]:
    """Parse a tweet dump file. Supports: plain text (--- separated), MD blockquotes, JSON."""
    content = path.read_text(encoding="utf-8")

    # Try JSON first
    if content.strip().startswith("["):
        try:
            data = json.loads(content)
            results = []
            for item in data:
                text = item.get("text", item.get("full_text", ""))
                expanded_text, urls = expand_urls_in_text(text)
                results.append({
                    "author": item.get("author", item.get("user", {}).get("screen_name", "")),
                    "text": expanded_text,
                    "original_text": text,
                    "external_urls": [u["expanded"] for u in urls if "twitter.com" not in u["expanded"]],
                    "date": item.get("created_at", ""),
                    "url": item.get("url", ""),
                })
            return results
        except json.JSONDecodeError:
            pass

    # Try markdown blockquotes
    if ">" in content and content.count(">") > content.count("---"):
        blocks = re.split(r"\n(?=>)", content)
        results = []
        for block in blocks:
            # Remove > prefix
            clean = re.sub(r"^>\s?", "", block, flags=re.MULTILINE).strip()
            parsed = parse_tweet_block(clean)
            if parsed:
                results.append(parsed)
        return [r for r in results if r]

    # Default: --- separated blocks
    blocks = re.split(r"\n---+\n", content)
    return [r for r in (parse_tweet_block(b) for b in blocks) if r]


def fetch_tweet_by_url(tweet_url: str) -> dict | None:
    """Optionally fetch tweet data via RapidAPI if key is available."""
    if not RAPIDAPI_KEY:
        return None

    tweet_id_match = re.search(r"/status/(\d+)", tweet_url)
    if not tweet_id_match:
        return None

    tweet_id = tweet_id_match.group(1)
    try:
        r = requests.get(
            "https://twitter241.p.rapidapi.com/tweet",
            headers={
                "x-rapidapi-host": "twitter241.p.rapidapi.com",
                "x-rapidapi-key": RAPIDAPI_KEY,
            },
            params={"pid": tweet_id},
            timeout=10,
        )
        r.raise_for_status()
        data = r.json()
        result = data.get("result", {}).get("data", {}).get("tweetResult", {}).get("result", {})
        legacy = result.get("legacy", {})
        return {
            "author": legacy.get("user_id_str", ""),
            "text": legacy.get("full_text", ""),
            "date": legacy.get("created_at", ""),
            "url": tweet_url,
        }
    except Exception as e:
        print(f"  [warn] RapidAPI error: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(description="Parse Twitter/X dumps for LLM Wiki")
    parser.add_argument("input", nargs="?", help="Tweet dump file path or tweet text")
    parser.add_argument("--file", help="Path to tweet dump file")
    parser.add_argument("--url", help="Single tweet URL to fetch (requires RAPIDAPI_KEY)")
    parser.add_argument("--expand-urls", action="store_true", default=True,
                        help="Expand t.co URLs (default: True)")
    args = parser.parse_args()

    if args.url:
        result = fetch_tweet_by_url(args.url)
        if result:
            _, urls = expand_urls_in_text(result["text"])
            result["external_urls"] = [u["expanded"] for u in urls if "twitter.com" not in u["expanded"]]
            print(json.dumps([result], indent=2, ensure_ascii=False))
        else:
            print("[]")
        return

    file_path = args.file or args.input
    if file_path:
        path = Path(file_path)
        if not path.exists():
            print(f"ERROR: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        tweets = parse_tweet_file(path)
    else:
        # Read from stdin
        content = sys.stdin.read()
        tweets = [r for r in [parse_tweet_block(b) for b in content.split("---")] if r]

    print(f"  Parsed {len(tweets)} tweets", file=sys.stderr)
    external_url_count = sum(len(t.get("external_urls", [])) for t in tweets)
    print(f"  Found {external_url_count} external URLs", file=sys.stderr)

    print(json.dumps(tweets, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
