# LLM Wiki — Claude Code Configuration
> Personal AI knowledge base inspired by Andrej Karpathy's LLM OS concept.
> Agent: Claude Code | Bilingual output: English + Russian

---

## 🧠 Project Mission

Build and maintain a living, structured knowledge base about AI, coding agents, LLMs, and the surrounding ecosystem. All knowledge is extracted from raw sources (web clippings, links, tweets, YouTube, Reddit) and distilled into clean wiki entries. Every entry is a **single bilingual file** — English content first, Russian content below, in the same `.md` file.

Think of this wiki as a second brain: continuously fed, automatically processed, always searchable.

---

## 📁 Project Structure

```
llm-wiki/
├── CLAUDE.md                   ← You are here. Claude Code reads this first.
├── inbox/                      ← Raw unprocessed inputs (drop zone)
│   ├── clippings/              ← Obsidian Web Clipper exports (.md files)
│   ├── links.md                ← Flat list of URLs to process
│   ├── twitter.md              ← Twitter/X tweet URLs to process (like links.md)
│   ├── youtube.md              ← YouTube video URLs (one per line)
│   └── posts.md                ← Raw text posts from social media (LinkedIn, Bluesky, etc.)
├── sources/                    ← Fetched & cached raw content (do not edit manually)
│   ├── reddit/                 ← Reddit post/comment snapshots
│   ├── web/                    ← Fetched article content
│   └── transcripts/            ← YouTube transcripts
├── wiki/                       ← Bilingual wiki entries (one file = EN + RU)
│   ├── concepts/               ← Foundational AI/ML concepts
│   ├── tools/                  ← Tools, frameworks, products
│   ├── agents/                 ← Coding agents & agentic workflows
│   ├── models/                 ← LLM models & providers
│   ├── news/                   ← Time-sensitive news & releases
│   ├── tips/                   ← Practical tips & prompting techniques
│   └── people/                 ← Notable researchers & builders
├── digests/                    ← Weekly digests (bilingual, one file per week)
├── .claude/
│   └── commands/               ← Custom slash commands (one .md file = one /command)
│       ├── wiki-inbox.md       → /wiki-inbox
│       ├── wiki-clippings.md   → /wiki-clippings
│       ├── wiki-links.md       → /wiki-links
│       ├── wiki-tweets.md      → /wiki-tweets
│       ├── wiki-posts.md       → /wiki-posts
│       ├── wiki-youtube.md     → /wiki-youtube
│       ├── wiki-reddit.md      → /wiki-reddit
│       ├── wiki-digest.md      → /wiki-digest
│       ├── wiki-index.md       → /wiki-index
│       ├── wiki-search.md      → /wiki-search
│       └── wiki-check.md       → /wiki-check
├── scripts/                    ← Python helper scripts
│   ├── fetch_reddit.py
│   ├── fetch_youtube.py
│   ├── fetch_twitter.py
│   ├── fetch_url.py
│   ├── utils.py
│   └── obs.py                  ← Obsidian vault analysis CLI (backlinks, orphans, broken links)
├── .state/                     ← Processing state & deduplication cache
│   ├── processed_urls.json     ← Already-processed URLs (skip list)
│   ├── reddit_cursor.json      ← Last-seen post IDs per subreddit
│   └── last_run.json           ← Timestamps of last runs
└── index.md                    ← Master wiki index (auto-generated)
```

---

## ⚙️ Environment Setup

### First-time setup (Windows)

Run the included PowerShell script from the project root:

```powershell
# One-time: allow local scripts to run (run as your normal user, not Administrator)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Run setup
.\setup.ps1
```

The script will:
- Verify Python 3.9+ and pip are available
- Create the full directory tree
- Install all Python dependencies from `requirements.txt`
- Scaffold a `.env` file from `.env.example`
- Initialise empty state files under `.state\`
- Run a smoke-test of key imports

**Optional flags:**

```powershell
.\setup.ps1 -SkipPip      # directories + .env only, skip pip install
.\setup.ps1 -ForceEnv     # overwrite existing .env with template
.\setup.ps1 -SkipChecks   # skip prerequisite checks (Python, Node, Claude)
```

### Manual dependency install (if needed)

```powershell
python -m pip install -r requirements.txt
```

### `.env` credentials

Edit `.env` in the project root after setup:

```env
# Reddit API (create app at https://www.reddit.com/prefs/apps)
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=llm-wiki-bot/1.0

# Optional: RapidAPI key for Twitter scraping (twitter241 or similar)
RAPIDAPI_KEY=your_key_here
```

> **Note:** YouTube transcripts and Reddit public posts work without API keys.
> Twitter/X without API key uses public scraping — reliability may vary.

---

## 🪟 Windows Environment

- **All new Python scripts must start from `scripts/_template.py`.** Copy it, rename it, replace the `main()` body. Do not delete the UTF-8 setup block or the helper functions at the top.
- Always use UTF-8 encoding explicitly when writing Python scripts (`# -*- coding: utf-8 -*-` header and `encoding='utf-8'` on all file opens/writes). Use the `read_text`/`write_text`/`read_json`/`write_json` helpers from `_template.py` instead of bare `open()`.
- Avoid emoji/Unicode literals in Python script output; use the `log()` helper from `_template.py` which enforces ASCII-safe output.
- Do NOT use `/tmp/` paths — they don't work with the Read tool on Windows. Use project-relative paths or `%TEMP%`.
- When parsing yt-dlp output, use `parse_ytdlp_json()` or `parse_ytdlp_json_stream()` from `_template.py` — yt-dlp writes download-progress text to the same stream as JSON output.

---

## ✏️ Editing Conventions

- Match existing indentation exactly (tabs vs spaces) when using Edit; if uncertain, Read the file first.
- When editing JSON files (especially `.state/*.json`, `settings.local.json`), validate that there are no trailing commas before saving — Python's `json.load` and Node's `JSON.parse` both reject them.

---

## 🌐 Network Fetching

- Prefer the `web-reader` MCP tool for fetching web content; only fall back to `scripts/fetch_url.py` (direct HTTP) if the MCP fails.
- Respect `robots.txt` — do not write scrapers that bypass it. If a site blocks fetching, note it in the entry's sources and skip.

---

## 🤖 Claude Code Behavior Rules

### Core Principles

1. **Every entry is bilingual.** Each `.md` file in `wiki/` contains both English and Russian content in the same file — English section first, Russian section second, separated by a clear divider. Never create separate files for translations.
2. **Deduplicate aggressively.** Before creating a new entry, check `index.md` and `.state/processed_urls.json`. Also run `python scripts/obs.py backlinks <slug>` to check if other entries already reference a slug — that's a signal the topic exists or is expected. Update existing entries rather than creating duplicates.
3. **Preserve source attribution.** Every wiki entry must include a `sources:` front-matter block with original URLs.
4. **Be concise, not exhaustive.** Entries should be scannable. Use bullet points for facts, short paragraphs for concepts. Max ~600 words per language section.
5. **Date-stamp news entries.** Anything in `wiki/news/` must have a `date:` field in front matter.
6. **Update the index.** After creating or updating any entry, regenerate `index.md`.
7. **Log what you did.** After each run, do both:
   - Append a structured JSON entry to `.state/last_run.json` (machine-readable, for the pipeline)
   - Append a human-readable line to `log.md` under today's `## YYYY-MM-DD` heading (create the heading if it doesn't exist yet)
   
   **`log.md` entry format:** `**HH:MM /command** — N entries created, M updated. Key items: slug1 (category), slug2 (category). Index: X total.`
8. **Keep links healthy.** `python scripts/obs.py broken` lists `[[links]]` to entries that do not yet exist — treat each as a stub to create. `python scripts/obs.py orphans` lists entries no one links to — add them to Related Entries in semantically close entries.

### Language Rules for Russian Translation

- Use natural Russian, not machine-literal translation.
- Keep English technical terms that have no established Russian equivalent (e.g., "token", "prompt", "fine-tuning", "RAG", "agent").
- For terms with established Russian equivalents, prefer Russian (e.g., "нейронная сеть", "языковая модель").
- Do NOT translate code blocks, command-line examples, or file paths.
- Headings should be translated; front-matter keys stay in English.

---

## 📋 Wiki Entry Format

Each entry is a **single file** at `wiki/<category>/<slug>.md` containing both languages.

```markdown
---
title: "Entry Title"
title_ru: "Название записи"
category: concepts | tools | agents | models | news | tips | people
tags: [tag1, tag2, tag3]
date: YYYY-MM-DD          # required for news entries
updated: YYYY-MM-DD
sources:
  - https://source-url-1
  - https://source-url-2
---

## Summary
One or two sentence TL;DR of what this entry is about.

## Key Ideas
- Main idea 1
- Main idea 2
- Main idea 3

## Details
Longer prose explanation, 2-4 paragraphs max.

## Notable Quotes
> "Exact quote if particularly insightful" — Author, Source

## Related Entries
- [[related-slug-1]]
- [[related-slug-2]]

---
<!-- RU -->

## Краткое описание
Одно-два предложения о чём эта запись.

## Ключевые идеи
- Главная идея 1
- Главная идея 2
- Главная идея 3

## Подробнее
Развёрнутое объяснение, максимум 2-4 абзаца.

## Примечательные цитаты
> "Цитата, если особенно содержательна" — Автор, Источник

## Связанные записи
- [[related-slug-1]]
- [[related-slug-2]]
```

**Format rules:**
- The `---\n<!-- RU -->` divider is the exact separator Claude Code uses to locate and update each language section independently.
- Front-matter keys are always in English; `title_ru` holds the Russian title.
- Code blocks, command-line examples, and file paths are **never** translated — they appear only in the English section and are not repeated in the Russian section.
- The `## Related Entries` links are identical in both sections (slugs are language-neutral).

---

## 🚀 Commands

Commands live as `.md` files in `.claude/commands/`. Claude Code loads them automatically — each file becomes a slash command named after the file (without the extension).

**Quick reference:**

| Type in Claude Code | What it does |
|---|---|
| `/wiki-inbox` | Process everything in `inbox/` (runs all sub-commands in sequence) |
| `/wiki-clippings` | Process Obsidian Web Clipper `.md` exports |
| `/wiki-links` | Fetch and process URLs from `inbox/links.md` |
| `/wiki-tweets` | Fetch and process tweet URLs from `inbox/twitter.md` |
| `/wiki-posts` | Process raw social media text posts from `inbox/posts.md` |
| `/wiki-youtube` | Process YouTube URLs from `inbox/youtube.md` |
| `/wiki-reddit` | Scan all configured subreddits for new posts |
| `/wiki-digest` | Generate the weekly bilingual digest |
| `/wiki-index` | Rebuild `index.md` from all wiki entries |
| `/wiki-search` | Search wiki entries — e.g. `/wiki-search RAG retrieval` |
| `/wiki-check` | Find and fix entries missing their Russian section |

> **How it works:** each `.claude/commands/wiki-*.md` file contains the full instructions Claude Code follows when you type that command. The detail for each command is in the file itself and summarised below.

---

### `/wiki-inbox`

Runs `/wiki-clippings` → `/wiki-links` → `/wiki-tweets` → `/wiki-posts` → `/wiki-youtube` in sequence, then rebuilds `index.md` and logs the run to `.state/last_run.json`.

---

### `/wiki-clippings`

Reads every `.md` file in `inbox/clippings/`, extracts the source URL from the Obsidian Web Clipper `url:` front-matter field, skips URLs already in `.state/processed_urls.json`, classifies the content, extracts main ideas and key concepts, writes a bilingual entry to `wiki/<category>/<slug>.md`, marks the URL as processed, and moves the source file to `sources/web/`.

---

### `/wiki-links`

Parses all URLs from `inbox/links.md` (ignores comment text), skips already-processed URLs, fetches each page with `python scripts/fetch_url.py`, classifies and extracts knowledge, writes a bilingual entry to `wiki/<category>/<slug>.md`, marks URLs as processed, and moves them to the `## Done` section of `inbox/links.md`.

**`inbox/links.md` format:**
```markdown
## To Read
- https://example.com/article-1
- https://example.com/article-2  <!-- optional note -->
```

---

### `/wiki-tweets`

Parses tweet URLs from `inbox/twitter.md` (same format as `inbox/links.md`: lines under `## To Read`, `## Done` at bottom), runs `python scripts/fetch_twitter.py <url>` for each new URL to fetch the tweet text and expand any t.co links, queues external URLs for `/wiki-links`, creates bilingual entries for notable insights, marks URLs as processed, and moves them to the `## Done` section.

**`inbox/twitter.md` format:**
```markdown
## To Read
- https://x.com/user/status/123456789
- https://twitter.com/user/status/987654321  <!-- optional note -->

## Done
```

---

### `/wiki-posts`

Reads `inbox/posts.md`, processes each raw text post block (separated by `---`), extracts the source/author/date from the optional metadata comment, classifies the insight, and creates or updates a bilingual wiki entry. Marks processed posts by moving them to a `## Done` section.

**`inbox/posts.md` format:**
```markdown
## To Process

<!-- Source: LinkedIn | Author: John Doe | Date: 2026-05-16 -->
Post text goes here. Can be multi-line.
Key insight or announcement from this post.

---

<!-- Source: Bluesky | Author: @user.bsky.social | Date: 2026-05-15 -->
Another post text here.

---

## Done
```

---

### `/wiki-youtube`

Parses YouTube URLs from `inbox/youtube.md`, runs `python scripts/fetch_youtube.py <url>` for each to download metadata and transcript, saves the raw transcript to `sources/transcripts/<video-id>.txt`, analyzes the transcript for main ideas / concepts / tips / quotes, and writes a bilingual entry with `## Video Notes` (EN) and `## Заметки по видео` (RU) sections including timestamp references.

---

### `/wiki-reddit`

Runs `python scripts/fetch_reddit.py <subreddit> --use-cursor --with-comments` for each monitored subreddit, filters posts with score > 50 or comment count > 20, classifies each post, writes bilingual entries to `wiki/<category>/<slug>.md`, queues any external URLs for the `/wiki-links` workflow, and updates `.state/reddit_cursor.json`.

**Monitored subreddits:** r/GithubCopilot, r/opencodeCLI, r/opencode, r/ClaudeCode, r/ZaiGLM, r/kimi, r/AI_Agents, r/LocalLLaMA, r/MachineLearning, r/singularity, r/ChatGPT, r/ChatGPTCoding, r/ollama, r/vibecoding

---

### `/wiki-digest`

Reads all entries modified in the last 7 days, summarises them into a bilingual digest at `digests/YYYY-WNN.md` with Top News, New Tools, Tips, Concepts, and Worth Reading sections in both English and Russian.

---

### `/wiki-index`

Scans all `.md` files in `wiki/`, reads their front-matter, and regenerates `index.md` grouped by category with one-line summaries.

---

### `/wiki-search`

The text after `/wiki-search` is passed as `$ARGUMENTS`. Searches file names and content across `wiki/` and returns matches ranked by relevance (title > tags > body), showing the entry title, category, and a short English excerpt.

---

### `/wiki-check`

Lists all `.md` files in `wiki/`, checks each for the `<!-- RU -->` divider, generates and appends the Russian section for any file that is missing it.

---

## 🐍 Helper Scripts Reference

### `scripts/_template.py` ← start here for every new script

**All new Python scripts must be copied from this file.** It provides:

| Helper | What it does |
|---|---|
| UTF-8 stdout/stderr reconfigure | Prevents CP1252 crashes on Windows before any `print()` call |
| `read_text(path)` / `write_text(path, content)` | File I/O with explicit `encoding='utf-8'` |
| `read_json(path)` / `write_json(path, data)` | JSON I/O with UTF-8 and no trailing commas |
| `log(msg, level)` | Timestamps + strips non-ASCII so logs survive CP1252 pipes |
| `parse_ytdlp_json(raw)` | Strips yt-dlp progress lines, returns single parsed JSON object |
| `parse_ytdlp_json_stream(raw)` | Same but for multi-object (playlist / `--print-json`) output |

```python
# Quickstart — copy _template.py, then:
cp scripts/_template.py scripts/my_new_script.py
# Edit the module docstring and main() body. Keep everything above main() intact.
```

---

### `scripts/fetch_url.py`

```
Usage: python scripts/fetch_url.py <url>
Output: Prints extracted article text to stdout
```

Uses `requests` + basic HTML parsing. Falls back to raw content if parsing fails. Respects `robots.txt` conceptually (does not scrape sites that explicitly block bots).

### `scripts/fetch_youtube.py`

```
Usage: python scripts/fetch_youtube.py <youtube-url>
Output: JSON with keys: title, channel, date, description, transcript
```

Uses `youtube-transcript-api`. If transcript unavailable in English, tries other languages. Falls back to `yt-dlp --write-auto-sub` for auto-generated subtitles.

### `scripts/fetch_reddit.py`

```
Usage: python scripts/fetch_reddit.py <subreddit> [--limit 25] [--after <post-id>]
Output: JSON array of post objects
```

Uses Reddit public JSON API (no auth needed for public posts) or OAuth if credentials are in `.env`.

### `scripts/fetch_twitter.py`

```
Usage: python scripts/fetch_twitter.py <tweet-url-or-text>
Output: JSON with keys: text, author, urls (expanded), date
```

Expands t.co URLs. Uses RapidAPI Twitter endpoint if `RAPIDAPI_KEY` is set; otherwise attempts public embed API.

### `scripts/utils.py`

Shared utilities:
- `load_processed_urls()` / `mark_processed(url)`
- `slugify(title)` — creates filename-safe slugs
- `detect_category(text)` — heuristic classifier
- `load_env()` — loads `.env` file

### `scripts/obs.py`

```
Usage: python scripts/obs.py <command> [args]

Commands:
  backlinks <slug>   Who links TO this entry (reverse lookup)
  links <slug>       What this entry links TO (with [BROKEN] flags)
  broken             All [[links]] pointing to nonexistent .md files
  orphans            Entries with zero incoming backlinks
  isolated           Entries with no links in or out
  top [N]            Top N most-linked entries (default 10)
  check              Full vault health report (all of the above)
```

Backed by `obsidiantools` — parses `[[wiki-link]]` syntax and builds the full backlink graph.

**When to use `obs.py`:**

| Situation | Command |
|---|---|
| Creating a new entry — find other entries that already reference it | `python scripts/obs.py backlinks <new-slug>` |
| Filling in "Related Entries" for an entry | `python scripts/obs.py links <slug>` to see outbound links; `backlinks` for inbound |
| After any batch run (`/wiki-reddit`, `/wiki-inbox`) | `python scripts/obs.py check` to surface broken links and new orphans |
| In `/wiki-check` — validate link integrity | `python scripts/obs.py broken` |
| In `/wiki-index` — flag entries no one links to | `python scripts/obs.py orphans` |
| Deciding which entries to write next | `python scripts/obs.py broken` — every target is a stub to create |

**Note on duplicate backlink counts:** because each `.md` file contains both an English and a Russian `## Related Entries` section with identical `[[links]]`, obsidiantools counts each backlink twice. `obs.py` automatically deduplicates these so reported counts are accurate.

---

## 📅 Recommended Automation Schedule

Run these manually or set up a cron job / Task Scheduler:

| Command | Frequency | Notes |
|---|---|---|
| `/wiki-reddit` | Daily | Morning scan for overnight posts |
| `/wiki-inbox` | As needed | After adding files to inbox/ |
| `/wiki-digest` | Weekly | Every Monday morning |
| `/wiki-check` | After any batch | Ensures every entry has its Russian section |
| `/wiki-index` | After any batch | Keep index current |

---

## 🏷️ Category Decision Guide

When classifying content, use this decision tree:

```
Is it time-sensitive (news, release, announcement)?
  → YES → news/
  → NO ↓

Is it about a specific tool, library, or product?
  → YES → tools/
  → NO ↓

Is it about a specific AI model or provider?
  → YES → models/
  → NO ↓

Is it about agentic systems, coding agents, autonomous AI?
  → YES → agents/
  → NO ↓

Is it a practical how-to, tip, or technique?
  → YES → tips/
  → NO ↓

Is it about a researcher, builder, or public figure?
  → YES → people/
  → NO → concepts/ (default)
```

---

## 🔍 Quality Checklist

Before finalizing any wiki entry, verify:

- [ ] Front matter is complete (`title`, `title_ru`, `category`, `tags`, `sources`, `updated`)
- [ ] Summary is 1-2 sentences, jargon-free (English section)
- [ ] At least 3 bullet points in Key Ideas (both sections)
- [ ] Sources list contains at least one URL
- [ ] No raw HTML in the file
- [ ] `---\n<!-- RU -->` divider is present and Russian section follows it
- [ ] Entry is linked in `index.md`
- [ ] URL is recorded in `.state/processed_urls.json`

---

## 🌐 Source Reliability Tiers

When extracting information, weight sources by reliability:

| Tier | Sources | Treatment |
|---|---|---|
| 1 - Primary | arxiv.org, official docs, GitHub release notes | Extract fully, high confidence |
| 2 - Reputable | HuggingFace blog, Anthropic blog, OpenAI blog, Google DeepMind | Extract fully |
| 3 - Community | Reddit, Hacker News, Twitter/X | Extract with skepticism; note as "community reports" |
| 4 - Unknown | Random blogs, Medium | Extract main claim only; verify against Tier 1-2 if possible |

Always note the source tier in entries when the information is not from Tier 1-2.

---

## 💬 Example Claude Code Session

```
You: /wiki-reddit

Claude Code: Scanning 12 subreddits...
  r/ClaudeCode: 8 new posts (3 qualifying)
  r/AI_Agents: 15 new posts (7 qualifying)
  r/LocalLLaMA: 22 new posts (5 qualifying)
  ...
  
  Created: wiki/tools/open-code-cli.md  (EN + RU)
  Updated: wiki/news/claude-code-1-0-release.md  (EN + RU)
  Queued 12 external URLs for processing.
  
  Run /wiki-links to process queued URLs.

You: /wiki-links

Claude Code: Processing 12 queued URLs...
  [1/12] https://github.com/... → Created wiki/tools/some-tool.md  (EN + RU)
  ...
  
  12 processed, 0 errors.
  Running /wiki-check...
  Running /wiki-index...
  Done. 8 new entries, 3 updated.
```

---

## 📝 Notes & Conventions

- **Slug convention:** lowercase, hyphens only, max 50 chars. E.g., `claude-code-memory-management.md`
- **No orphan entries:** every entry must appear in `index.md`
- **No stub entries:** minimum viable entry = summary + 3 key ideas + 1 source
- **Conflict resolution:** if two sources contradict, note both perspectives in `## Debate` section
- **Versioning:** for tools with multiple versions, use a single entry and maintain a `## Version History` section
- **Privacy:** never store API keys or credentials in wiki entries

---

_This CLAUDE.md is the single source of truth for Claude Code operating in this project. Update it as the wiki evolves._
