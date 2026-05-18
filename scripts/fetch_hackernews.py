#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/fetch_hackernews.py
===========================
Fetch articles from The Hacker News (thehackernews.com) and filter by topics.md.

Usage:
    python scripts/fetch_hackernews.py [--limit 30] [--use-cursor] [--min-score 1]

Output: JSON array of matching article objects to stdout.
State:  .state/hackernews_cursor.json
"""

import io, json, sys, re, argparse, datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

def read_text(path):
    with open(path, encoding="utf-8") as f: return f.read()

def read_json(path):
    with open(path, encoding="utf-8") as f: return json.load(f)

def write_json(path, data, indent=2):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
        f.write("\n")

def log(msg, level="INFO"):
    safe = msg.encode("ascii", errors="replace").decode("ascii")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {level}: {safe}", file=sys.stderr)

DEFAULT_KEYWORDS = [
    "ai agent", "agentic", "claude code", "codex", "github copilot", "opencode",
    "llm", "large language model", "gpt", "gemini", "anthropic", "openai",
    "llm wiki", "knowledge base", "rag", "retrieval augmented", "mcp",
    "model context protocol", "vibe coding", "ai coding", "coding assistant",
    "benchmark", "model release", "frontier model",
]

def load_topic_keywords(topics_path="topics.md"):
    try:
        content = read_text(topics_path)
    except FileNotFoundError:
        log(f"topics.md not found, using defaults", "WARN")
        return DEFAULT_KEYWORDS
    keywords = []
    for line in content.splitlines():
        if "**Keywords:**" in line:
            kws_str = line.split("**Keywords:**", 1)[1].strip()
            for kw in kws_str.split(","):
                kw = kw.strip().lower()
                if kw:
                    keywords.append(kw)
    return keywords if keywords else DEFAULT_KEYWORDS

def fetch_articles(limit=30):
    import urllib.request
    from xml.etree import ElementTree as ET
    RSS_URL = "https://feeds.feedburner.com/TheHackersNews"
    log(f"Fetching The Hacker News RSS ({limit} items)...")
    try:
        req = urllib.request.Request(RSS_URL, headers={"User-Agent": "llm-wiki-bot/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
    except Exception as e:
        log(f"Failed to fetch RSS: {e}", "ERROR")
        return []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        log(f"Failed to parse RSS: {e}", "ERROR")
        return []
    articles = []
    channel = root.find("channel")
    if channel is None:
        return []
    for item in channel.findall("item")[:limit]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        desc = re.sub(r"<[^>]+>", " ", item.findtext("description") or "")
        desc = re.sub(r"\s+", " ", desc).strip()[:500]
        pub_date = (item.findtext("pubDate") or "").strip()
        categories = [c.text.strip() for c in item.findall("category") if c.text]
        if title and link:
            articles.append({
                "title": title, "url": link, "description": desc,
                "date": pub_date, "categories": categories,
                "source": "thehackernews.com",
            })
    log(f"Fetched {len(articles)} articles")
    return articles

def score_article(article, keywords):
    text = (article.get("title","") + " " + article.get("description","") + " " +
            " ".join(article.get("categories",[]))).lower()
    score = 0
    matched = []
    for kw in keywords:
        if kw.lower() in text:
            score += 1
            matched.append(kw)
    article["_score"] = score
    article["_matched_keywords"] = matched
    return score

CURSOR_PATH = ".state/hackernews_cursor.json"

def load_cursor():
    try:
        return set(read_json(CURSOR_PATH).get("seen_urls", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()

def save_cursor(seen_urls):
    write_json(CURSOR_PATH, {"seen_urls": list(seen_urls)[-500:]})

def main():
    parser = argparse.ArgumentParser(description="Fetch The Hacker News filtered by topics.md")
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--use-cursor", action="store_true")
    parser.add_argument("--min-score", type=int, default=1)
    parser.add_argument("--topics", default="topics.md")
    args = parser.parse_args()

    keywords = load_topic_keywords(args.topics)
    log(f"Loaded {len(keywords)} keywords from {args.topics}")

    articles = fetch_articles(args.limit)
    if not articles:
        print("[]")
        return 0

    seen_urls = load_cursor() if args.use_cursor else set()
    results = []
    skipped = 0
    for article in articles:
        url = article["url"]
        if args.use_cursor and url in seen_urls:
            skipped += 1
            continue
        if score_article(article, keywords) >= args.min_score:
            results.append(article)
            seen_urls.add(url)

    if args.use_cursor:
        save_cursor(seen_urls)

    log(f"Qualifying: {len(results)} articles (skipped: {skipped})")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
