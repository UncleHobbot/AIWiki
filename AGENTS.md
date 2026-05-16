# LLM Wiki — Configuration
> Personal AI knowledge base inspired by Andrej Karpathy's LLM OS concept.
> Bilingual output: English + Russian

---

## 🧠 Project Mission

Build and maintain a living, structured knowledge base about AI, coding agents, LLMs, and the surrounding ecosystem. All knowledge is extracted from raw sources (web clippings, links, tweets, YouTube, Reddit) and distilled into clean wiki entries. Every entry is a **single bilingual file** — English content first, Russian content below, in the same `.md` file.

Think of this wiki as a second brain: continuously fed, automatically processed, always searchable.

### Three-Layer Architecture

This project follows Karpathy's 3-layer pattern for LLM-powered knowledge systems:

| Layer | Directory | Role |
|---|---|---|
| **Raw sources** | `inbox/`, `sources/` | Immutable inputs — web clips, transcripts, Reddit dumps |
| **Wiki (distilled knowledge)** | `wiki/` | LLM-written bilingual entries with structure and cross-links |
| **Schema (this file)** | `AGENTS.md` | Navigation map — tells the agent what exists, where to find it, what format it's in |

This file (AGENTS.md) is the **schema layer**: it controls context injection by telling the agent exactly where to look and what format data is in, preventing unnecessary scanning and context window bloat. The same pattern scales from personal wikis to multi-agent production systems.

---

## 📁 Project Structure

```
llm-wiki/
├── AGENTS.md                   ← You are here. Read by opencode first.
├── opencode.json               ← opencode config: commands, instructions, agents
├── inbox/                      ← Raw unprocessed inputs (drop zone)
│   ├── clippings/              ← Obsidian Web Clipper exports (.md files)
│   ├── links.md                ← Flat list of URLs to process
│   ├── tweets/                 ← Twitter/X post dumps (.txt or .md)
│   └── youtube.md              ← YouTube video URLs (one per line)
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
├── scripts/                    ← Python helper scripts
│   ├── fetch_reddit.py
│   ├── fetch_youtube.py
│   ├── fetch_twitter.py
│   ├── fetch_url.py
│   └── utils.py
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

## 🤖 Behavior Rules

### Core Principles

1. **Every entry is bilingual.** Each `.md` file in `wiki/` contains both English and Russian content in the same file — English section first, Russian section second, separated by a clear divider. Never create separate files for translations.
2. **Deduplicate aggressively.** Before creating a new entry, check `index.md` and `.state/processed_urls.json`. Update existing entries rather than creating duplicates.
3. **Preserve source attribution.** Every wiki entry must include a `sources:` front-matter block with original URLs.
4. **Be concise, not exhaustive.** Entries should be scannable. Use bullet points for facts, short paragraphs for concepts. Max ~600 words per language section.
5. **Date-stamp news entries.** Anything in `wiki/news/` must have a `date:` field in front matter.
6. **Update the index.** After creating or updating any entry, regenerate `index.md`.
7. **Log what you did.** After each run, append a one-line summary with date, command, and outcome to `log.md`.
8. **Controlled context injection.** Structure information so agents receive only the context relevant to the current task. Use `AGENTS.md` as the navigation map — know where data lives and in what format — rather than scanning everything and bloating the context window.

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
- **The `---\n<!-- RU -->` divider is the exact separator used to locate and update each language section independently.
- Front-matter keys are always in English; `title_ru` holds the Russian title.
- Code blocks, command-line examples, and file paths are **never** translated — they appear only in the English section and are not repeated in the Russian section.
- The `## Related Entries` links are identical in both sections (slugs are language-neutral).

---

## 🚀 Commands

Commands are defined in `opencode.json` under the `command` key and triggered with `/<name>` in the opencode CLI.

**Quick reference:**

| Type in opencode | What it does |
|---|---|
| `/wiki-inbox` | Process everything in `inbox/` (runs all sub-commands in sequence) |
| `/wiki-clippings` | Process Obsidian Web Clipper `.md` exports |
| `/wiki-links` | Fetch and process URLs from `inbox/links.md` |
| `/wiki-tweets` | Process tweet dumps from `inbox/tweets/` |
| `/wiki-youtube` | Process YouTube URLs from `inbox/youtube.md` |
| `/wiki-reddit` | Scan all configured subreddits for new posts |
| `/wiki-digest` | Generate the weekly bilingual digest |
| `/wiki-index` | Rebuild `index.md` from all wiki entries |
| `/wiki-search` | Search wiki entries — e.g. `/wiki-search RAG retrieval` |
| `/wiki-check` | Find and fix entries missing their Russian section |

> **How it works:** each command in `opencode.json` contains the full instructions opencode follows when you type that command. The detail for each command is summarised below.

---

### `/wiki-inbox`

Runs `/wiki-clippings` → `/wiki-links` → `/wiki-tweets` → `/wiki-youtube` in sequence, then rebuilds `index.md` and logs the run to `.state/last_run.json`.

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

Reads all files in `inbox/tweets/` (plain text `---`-separated, markdown blockquotes, or JSON arrays), expands t.co URLs via `python scripts/fetch_twitter.py`, queues external URLs for the `/wiki-links` workflow, and creates bilingual entries for any notable insights found directly in the tweet text.

---

### `/wiki-youtube`

Parses YouTube URLs from `inbox/youtube.md`, runs `python scripts/fetch_youtube.py <url>` for each to download metadata and transcript, saves the raw transcript to `sources/transcripts/<video-id>.txt`, analyzes the transcript for main ideas / concepts / tips / quotes, and writes a bilingual entry with `## Video Notes` (EN) and `## Заметки по видео` (RU) sections including timestamp references.

---

### `/wiki-reddit`

Runs `python scripts/fetch_reddit.py <subreddit> --use-cursor --with-comments` for each monitored subreddit, filters posts with score > 50 or comment count > 20, classifies each post, writes bilingual entries to `wiki/<category>/<slug>.md`, queues any external URLs for the `/wiki-links` workflow, and updates `.state/reddit_cursor.json`.

**Monitored subreddits:** r/GithubCopilot, r/opencodeCLI, r/opencode, r/ClaudeCode, r/ZaiGLM, r/kimi, r/AI_Agents, r/LocalLLaMA, r/MachineLearning, r/singularity, r/ChatGPT, r/ChatGPTCoding

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

## 💬 Example Session

```
You: /wiki-reddit

opencode: Scanning 12 subreddits...
  r/ClaudeCode: 8 new posts (3 qualifying)
  r/AI_Agents: 15 new posts (7 qualifying)
  r/LocalLLaMA: 22 new posts (5 qualifying)
  ...
  
  Created: wiki/tools/open-code-cli.md  (EN + RU)
  Updated: wiki/news/claude-code-1-0-release.md  (EN + RU)
  Queued 12 external URLs for processing.
  
  Run /wiki-links to process queued URLs.

You: /wiki-links

opencode: Processing 12 queued URLs...  [1/12] https://github.com/... → Created wiki/tools/some-tool.md  (EN + RU)
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

_This AGENTS.md is the single source of truth for opencode operating in this project. Update it as the wiki evolves._
