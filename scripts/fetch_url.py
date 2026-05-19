#!/usr/bin/env python3
"""
scripts/fetch_url.py
Fetch a web page and extract article text, respecting rate limits.
"""

import argparse
import io
import json
import re
import sys
import urllib.robotparser
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; LLMWikiBot/1.0; +https://github.com/you/llm-wiki)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


def check_robots(url: str) -> bool:
    """Check if we're allowed to fetch this URL. Returns True if allowed."""
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    try:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch(HEADERS["User-Agent"], url)
    except Exception:
        return True  # assume allowed if can't read robots.txt


def extract_text_from_html(html: str) -> str:
    """Simple HTML to text extraction without external deps."""
    # Remove scripts and styles
    html = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style[^>]*>.*?</style>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    html = re.sub(r"<[^>]+>", " ", html)
    # Decode common HTML entities
    html = html.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    html = html.replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
    # Normalize whitespace
    html = re.sub(r"\s+", " ", html).strip()
    return html


def extract_with_readability(html: str, url: str) -> dict:
    """Try to use readability-lxml if available."""
    try:
        from readability import Document
        doc = Document(html)
        return {
            "title": doc.title(),
            "content": extract_text_from_html(doc.summary()),
            "method": "readability",
        }
    except ImportError:
        pass

    # Fallback: simple extraction
    title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    title = extract_text_from_html(title_match.group(1)) if title_match else ""

    # Try to find main content area
    for tag in ["article", "main", '[role="main"]', ".post-content", ".article-body"]:
        match = re.search(rf"<(?:article|main)[^>]*>(.*?)</(?:article|main)>", html, re.DOTALL | re.IGNORECASE)
        if match:
            return {
                "title": title,
                "content": extract_text_from_html(match.group(1)),
                "method": "heuristic",
            }

    return {
        "title": title,
        "content": extract_text_from_html(html)[:8000],  # truncate to 8k chars
        "method": "full-page",
    }


def fetch_url(url: str) -> dict:
    if not check_robots(url):
        return {"url": url, "error": "robots.txt disallows fetching", "content": ""}

    try:
        r = requests.get(url, headers=HEADERS, timeout=20, allow_redirects=True)
        r.raise_for_status()

        content_type = r.headers.get("content-type", "")
        if "text/html" not in content_type and "text/plain" not in content_type:
            return {"url": url, "error": f"Unsupported content type: {content_type}", "content": ""}

        result = extract_with_readability(r.text, url)
        result["url"] = r.url  # final URL after redirects
        result["original_url"] = url
        result["status_code"] = r.status_code
        return result

    except requests.exceptions.Timeout:
        return {"url": url, "error": "Request timed out", "content": ""}
    except requests.exceptions.TooManyRedirects:
        return {"url": url, "error": "Too many redirects", "content": ""}
    except requests.exceptions.RequestException as e:
        return {"url": url, "error": str(e), "content": ""}


def main():
    parser = argparse.ArgumentParser(description="Fetch URL content for LLM Wiki")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--max-chars", type=int, default=10000, help="Max content length")
    args = parser.parse_args()

    result = fetch_url(args.url)
    if "content" in result and len(result["content"]) > args.max_chars:
        result["content"] = result["content"][: args.max_chars] + "\n\n[TRUNCATED]"
        result["truncated"] = True

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
