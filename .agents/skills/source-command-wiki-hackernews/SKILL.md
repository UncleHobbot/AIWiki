---
name: "source-command-wiki-hackernews"
description: "Migrated source command `wiki-hackernews`"
---

# source-command-wiki-hackernews

Use this skill when the user asks to run the migrated source command `wiki-hackernews`.

## Command Template

Fetch and process AI-relevant articles from The Hacker News (thehackernews.com), filtered by topics defined in topics.md.

Steps:
1. Run:
     python scripts/fetch_hackernews.py --use-cursor --min-score 2
   This fetches the RSS feed, scores each article against topic keywords from topics.md,
   skips already-seen URLs, and returns only articles with score ≥ 2.

2. For each qualifying article:
   a. Fetch full article content: python scripts/fetch_url.py <url>
      (if fetch_url fails or robots.txt blocks: use article title + description only)
   b. Score against topics.md to classify priority (highest/high/medium)
   c. Skip if the article is primarily about:
      - Specific malware/ransomware campaigns with no AI angle
      - Data breaches not involving AI systems
      - Non-technical political/regulatory news
      Skip threshold: score < 2 after reading full content
   d. Classify using the standard category decision tree from AGENTS.md
   e. Create or update a bilingual wiki entry at wiki/<category>/<slug>.md
   f. Mark the URL as processed in .state/processed_urls.json

3. Rebuild index.md and per-topic indexes (topics/ directory)

4. Report: N articles fetched, M qualified, K entries created/updated, J skipped

5. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-hackernews" "<N articles fetched, M qualified, K entries created: slug1 (cat), slug2 (cat). Index: X total.>"

**Article scoring reference (from topics.md):**
- Score ≥ 3: create wiki entry
- Score 1-2: queue to inbox/links.md for later review
- Score 0: skip entirely

**thehackernews.com coverage relevant to this wiki:**
- AI model security vulnerabilities and jailbreaks
- LLM-powered cyberattack tools
- AI coding tool compromises (supply chain, prompt injection)
- AI safety and governance news
- New AI product/model launches covered in security context
- Agent security and MCP server vulnerabilities
