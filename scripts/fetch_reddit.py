#!/usr/bin/env python3
"""
scripts/fetch_reddit.py
Fetch posts from a subreddit using Reddit's public JSON API (no OAuth needed for public posts).
With .env credentials, switches to OAuth for higher rate limits.
Falls back to RSS Atom feed if the JSON API returns 403 (unauthenticated access blocked).
"""

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

import io as _io
sys.stdout = _io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = _io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import requests
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "llm-wiki-bot/1.0")

STATE_FILE = Path(".state/reddit_cursor.json")
STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

PLACEHOLDER_VALUES = {"your_client_id_here", "your_client_secret_here", "your_rapidapi_key_here"}

RSS_NS = {"atom": "http://www.w3.org/2005/Atom"}


def get_oauth_token() -> str | None:
    if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
        return None
    if REDDIT_CLIENT_ID in PLACEHOLDER_VALUES or REDDIT_CLIENT_SECRET in PLACEHOLDER_VALUES:
        return None
    try:
        r = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET),
            data={"grant_type": "client_credentials"},
            headers={"User-Agent": REDDIT_USER_AGENT},
            timeout=10,
        )
        r.raise_for_status()
        return r.json().get("access_token")
    except Exception:
        return None


def load_cursor() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {}


def save_cursor(cursor: dict):
    STATE_FILE.write_text(json.dumps(cursor, indent=2, ensure_ascii=False), encoding="utf-8")


def fetch_posts_json(subreddit: str, limit: int = 25, after: str | None = None) -> list[dict]:
    """Fetch posts via the JSON API (requires OAuth or open public access)."""
    token = get_oauth_token()
    base = "https://oauth.reddit.com" if token else "https://www.reddit.com"
    headers = {"User-Agent": REDDIT_USER_AGENT}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    params = {"limit": limit, "raw_json": 1}
    if after:
        params["after"] = after

    url = f"{base}/r/{subreddit}/new.json"
    r = requests.get(url, headers=headers, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()

    posts = []
    for child in data["data"]["children"]:
        p = child["data"]
        posts.append({
            "id": p["id"],
            "name": p["name"],
            "title": p["title"],
            "author": p["author"],
            "url": p["url"],
            "permalink": f"https://www.reddit.com{p['permalink']}",
            "selftext": p.get("selftext", ""),
            "score": p["score"],
            "num_comments": p["num_comments"],
            "created_utc": p["created_utc"],
            "is_self": p["is_self"],
            "link_flair_text": p.get("link_flair_text"),
            "subreddit": subreddit,
            "_via": "json",
        })
    return posts


def fetch_posts_rss(subreddit: str, limit: int = 25, days: int = 14,
                    max_retries: int = 4) -> list[dict]:
    """Fallback: fetch posts via Atom RSS (public, no auth). No scores/comments available.

    Reddit rate-limits RSS aggressively when many feeds are pulled back to back,
    so retry 429/5xx with exponential backoff, honouring Retry-After when sent.
    """
    url = f"https://www.reddit.com/r/{subreddit}/new.rss?limit={min(limit, 100)}"

    r = None
    for attempt in range(max_retries):
        r = requests.get(url, headers={"User-Agent": REDDIT_USER_AGENT}, timeout=15)
        if r.status_code < 400:
            break
        if r.status_code == 429 or r.status_code >= 500:
            if attempt == max_retries - 1:
                break
            retry_after = r.headers.get("Retry-After")
            try:
                delay = float(retry_after) if retry_after else 2.0 * (2 ** attempt)
            except ValueError:
                delay = 2.0 * (2 ** attempt)
            delay = min(delay, 60.0)
            print(f"  [warn] r/{subreddit} RSS HTTP {r.status_code}, retrying in {delay:.0f}s "
                  f"({attempt + 1}/{max_retries - 1})", file=sys.stderr)
            time.sleep(delay)
            continue
        break  # other 4xx: not worth retrying

    r.raise_for_status()

    root = ET.fromstring(r.content)
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    posts = []
    for entry in root.findall("atom:entry", RSS_NS):
        # Permalink
        link_el = entry.find("atom:link[@rel='alternate']", RSS_NS)
        if link_el is None:
            link_el = entry.find("atom:link", RSS_NS)
        permalink = (link_el.attrib.get("href", "") if link_el is not None else "").strip()

        # Post ID from permalink: .../comments/<id>/...
        m = re.search(r"/comments/([a-z0-9]+)/", permalink)
        post_id = m.group(1) if m else ""

        # Timestamp
        updated_str = (entry.findtext("atom:updated", "", RSS_NS) or "").strip()
        try:
            updated = datetime.fromisoformat(updated_str.replace("Z", "+00:00"))
        except Exception:
            updated = datetime.now(timezone.utc)

        if updated < cutoff:
            continue  # older than requested window

        title = (entry.findtext("atom:title", "", RSS_NS) or "").strip()
        author = (entry.findtext("atom:author/atom:name", "", RSS_NS) or "").strip()

        # selftext: strip HTML from content element
        content_el = entry.find("atom:content", RSS_NS)
        content_html = (content_el.text or "") if content_el is not None else ""
        selftext = re.sub(r"<[^>]+>", " ", content_html).strip()[:1000]

        # External URL: try to extract from content HTML, fall back to permalink
        ext_url_m = re.search(r'href="(https?://[^"]+)"', content_html)
        if ext_url_m and "reddit.com" not in ext_url_m.group(1):
            ext_url = ext_url_m.group(1)
        else:
            ext_url = permalink

        posts.append({
            "id": post_id,
            "name": f"t3_{post_id}",
            "title": title,
            "author": author,
            "url": ext_url,
            "permalink": permalink,
            "selftext": selftext,
            "score": 0,          # not available in RSS
            "num_comments": 0,   # not available in RSS
            "created_utc": updated.timestamp(),
            "is_self": ext_url == permalink,
            "link_flair_text": None,
            "subreddit": subreddit,
            "_via": "rss",
        })

    return posts[:limit]


def fetch_posts(subreddit: str, limit: int = 25, after: str | None = None) -> list[dict]:
    """Fetch posts, falling back to RSS if the JSON API returns 403."""
    try:
        return fetch_posts_json(subreddit, limit=limit, after=after)
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code == 403:
            print(f"  [info] JSON API 403 — falling back to RSS for r/{subreddit}", file=sys.stderr)
            return fetch_posts_rss(subreddit, limit=limit)
        raise


def fetch_top_comments(permalink: str, limit: int = 5) -> list[dict]:
    """Fetch top comments via JSON API. Returns [] on 403 (not available via RSS)."""
    token = get_oauth_token()
    base = "https://oauth.reddit.com" if token else "https://www.reddit.com"
    headers = {"User-Agent": REDDIT_USER_AGENT}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = f"{base}{permalink.replace('https://www.reddit.com', '')}.json"
    try:
        r = requests.get(url, headers=headers, params={"limit": limit, "raw_json": 1}, timeout=15)
        r.raise_for_status()
        data = r.json()
        comments = []
        for child in data[1]["data"]["children"][:limit]:
            c = child.get("data", {})
            if c.get("body") and c["body"] != "[deleted]":
                comments.append({
                    "author": c.get("author", ""),
                    "body": c["body"],
                    "score": c.get("score", 0),
                })
        return comments
    except Exception as e:
        print(f"  [warn] Could not fetch comments: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser(description="Fetch Reddit posts for LLM Wiki")
    parser.add_argument("subreddit", help="Subreddit name (without r/)")
    parser.add_argument("--limit", type=int, default=25, help="Max posts to fetch")
    parser.add_argument("--after", help="Fetch posts after this fullname (pagination)")
    parser.add_argument("--min-score", type=int, default=10, help="Minimum post score (ignored when RSS fallback active)")
    parser.add_argument("--with-comments", action="store_true", help="Include top comments")
    parser.add_argument("--use-cursor", action="store_true", help="Use saved cursor for incremental fetch")
    parser.add_argument("--days", type=int, default=14, help="Days to look back when using RSS fallback (default: 14)")
    args = parser.parse_args()

    after = args.after
    if args.use_cursor:
        cursor = load_cursor()
        after = cursor.get(args.subreddit)

    print(f"Fetching r/{args.subreddit} (limit={args.limit}, after={after})...", file=sys.stderr)
    posts = fetch_posts(args.subreddit, limit=args.limit, after=after)

    # Determine if we're in RSS fallback mode
    via_rss = any(p.get("_via") == "rss" for p in posts)

    # Filter: score/comments thresholds only apply when we have real data (JSON mode).
    # In RSS mode all posts pass (no score data), leaving content filtering to the caller.
    if via_rss:
        qualifying = posts
        print(f"  {len(posts)} posts fetched via RSS (no score data — all qualify)", file=sys.stderr)
    else:
        qualifying = [p for p in posts if p["score"] >= args.min_score or p["num_comments"] >= 20]
        print(f"  {len(posts)} posts fetched, {len(qualifying)} qualify (score≥{args.min_score} or comments≥20)", file=sys.stderr)

    if args.with_comments and not via_rss:
        for post in qualifying:
            print(f"  Fetching comments for: {post['title'][:60]}...", file=sys.stderr)
            post["top_comments"] = fetch_top_comments(post["permalink"])
            time.sleep(0.5)  # polite rate limiting
    elif args.with_comments and via_rss:
        print("  [info] Comment fetching skipped (RSS fallback — JSON API unavailable)", file=sys.stderr)

    # Update cursor to newest post (works for both JSON and RSS since both set 'name')
    if posts and args.use_cursor:
        cursor = load_cursor()
        cursor[args.subreddit] = posts[0]["name"]
        save_cursor(cursor)
        print(f"  Cursor updated: {posts[0]['name']}", file=sys.stderr)

    print(json.dumps(qualifying, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
