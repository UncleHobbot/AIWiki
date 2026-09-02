---
name: "source-command-wiki-reddit"
description: "Migrated source command `wiki-reddit`"
---

# source-command-wiki-reddit

Use this skill when the user asks to run the migrated source command `wiki-reddit`.

## Command Template

Scan all configured subreddits for new posts and extract relevant knowledge.

Monitored subreddits:
  r/GithubCopilot, r/opencodeCLI, r/opencode, r/Codex, r/ZaiGLM,
  r/kimi, r/AI_Agents, r/LocalLLaMA, r/MachineLearning, r/singularity,
  r/ChatGPT, r/ChatGPTCoding, r/ollama, r/vibecoding, r/DeepSeek, r/Qwen_AI

Steps:
1. For each subreddit, run:
     python scripts/fetch_reddit.py <subreddit> --use-cursor --with-comments --min-score 50
   This fetches only posts newer than the last-seen cursor and with score >= 50 or comments >= 20.

2. For each qualifying post:
   a. Read the post title, body, and top 5 comments
   b. Classify using these rules:
      - Title contains "released", "announcing", "new version", "launched" → news/
      - Title contains "how to", "tips for", "best practices", "guide" → tips/
      - Link to arxiv.org or huggingface.co/papers → concepts/
      - Link to github.com repo → tools/
      - Discussion of a specific model or benchmark → models/
      - Discussion of agents, MCP, agentic workflows → agents/
      - "Question" or "Help with" flair → skip unless score > 200
   c. Extract: main claim, key points from top comments, any external URLs
   d. Create or update the bilingual wiki entry at wiki/<category>/<slug>.md
      Both English and Russian sections in one file, separated by:
      ---
      <!-- RU -->
   e. Add any external URLs found in the post or top comments to inbox/links.md
      under "## To Read" for later processing

3. Update .state/reddit_cursor.json with the newest post ID seen per subreddit
4. Rebuild index.md
5. Report: per subreddit — N posts scanned, M entries created/updated, K URLs queued
6. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-reddit" "<N subreddits, M entries created: slug1 (cat), slug2 (cat). Index: X total.>"

Wiki entry format to follow: see AGENTS.md § Wiki Entry Format.
