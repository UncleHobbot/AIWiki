#!/usr/bin/env python3
"""
scripts/fetch_reddit.py
Fetch posts from a subreddit using Reddit's public JSON API (no OAuth needed for public posts).
With .env credentials, switches to OAuth for higher rate limits.
"""

import argparse
import json
import os
import sys
import time
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


def fetch_posts(subreddit: str, limit: int = 25, after: str | None = None) -> list[dict]:
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
            "name": p["name"],          # fullname e.g. t3_abc123
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
        })
    return posts


def fetch_top_comments(permalink: str, limit: int = 5) -> list[dict]:
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
    parser.add_argument("--min-score", type=int, default=10, help="Minimum post score")
    parser.add_argument("--with-comments", action="store_true", help="Include top comments")
    parser.add_argument("--use-cursor", action="store_true", help="Use saved cursor for incremental fetch")
    args = parser.parse_args()

    after = args.after
    if args.use_cursor:
        cursor = load_cursor()
        after = cursor.get(args.subreddit)

    print(f"Fetching r/{args.subreddit} (limit={args.limit}, after={after})...", file=sys.stderr)
    posts = fetch_posts(args.subreddit, limit=args.limit, after=after)

    # Filter by score
    qualifying = [p for p in posts if p["score"] >= args.min_score or p["num_comments"] >= 20]
    print(f"  {len(posts)} posts fetched, {len(qualifying)} qualify (score≥{args.min_score} or comments≥20)", file=sys.stderr)

    if args.with_comments:
        for post in qualifying:
            print(f"  Fetching comments for: {post['title'][:60]}...", file=sys.stderr)
            post["top_comments"] = fetch_top_comments(post["permalink"])
            time.sleep(0.5)  # polite rate limiting

    # Update cursor to newest post
    if posts and args.use_cursor:
        cursor = load_cursor()
        cursor[args.subreddit] = posts[0]["name"]
        save_cursor(cursor)
        print(f"  Cursor updated: {posts[0]['name']}", file=sys.stderr)

    print(json.dumps(qualifying, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
