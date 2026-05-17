# AIWiki

Personal AI knowledge base inspired by [Andrej Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) concept. Every entry is bilingual (English + Russian) in a single file. Raw sources (Reddit, YouTube, web links, tweets, social posts, Obsidian clips) are automatically distilled into structured wiki entries by LLM agents.

Works with **Claude Code** (primary), **OpenCode**, and any MCP-capable agent via `opencode.json`.

---

## Stats

| | |
|---|---|
| **Entries** | 94 across 7 categories |
| **Categories** | concepts · tools · agents · models · news · tips · people |
| **Subreddits monitored** | 14 (daily cursor-deduped scan) |
| **Commands** | 14 slash commands + `/wiki-pipeline` skill |
| **Quality** | pytest suite (285 tests), pre-commit hooks |
| **Top hub** | `[[llm-wiki-pattern]]` — 24 incoming backlinks |

---

## Architecture

Three-layer pattern:

```
inbox/          ← raw unprocessed inputs (drop zone)
  links.md      ← URLs to fetch
  youtube.md    ← YouTube video URLs
  twitter.md    ← tweet URLs
  posts.md      ← raw social media text
  clippings/    ← Obsidian Web Clipper exports

wiki/           ← LLM-written bilingual entries (one file = EN + RU)
  concepts/     ← foundational AI/ML concepts
  tools/        ← tools, frameworks, products
  agents/       ← coding agents & agentic workflows
  models/       ← LLM models & providers
  news/         ← time-sensitive releases & events
  tips/         ← practical tips & prompting techniques
  people/       ← notable researchers & builders

digests/        ← weekly bilingual digests (YYYY-WNN.md)
              + memory.json — rolling terminology memory for digest coherence

.state/         ← deduplication cache & run state
  processed_urls.json
  reddit_cursor.json
  last_run.json
  relations/    ← per-entry relation index (for /wiki-search relational queries)

CLAUDE.md       ← agent configuration (rules, conventions, commands)
```

---

## Quick Start

```powershell
# One-time setup (Windows)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\setup.ps1

# Install Python dependencies
python -m pip install -r requirements.txt

# Optional: Reddit API credentials
# Edit .env — public JSON API works without OAuth
```

Open the `wiki/` folder in [Obsidian](https://obsidian.md) for graph view and browsing, or use Claude Code / OpenCode for agent-driven ingestion.

---

## Commands

### Ingestion pipeline

| Command | What it does |
|---|---|
| `/wiki-pipeline` | **Full daily maintenance** — reddit → inbox → links → check → index → digest → git push |
| `/wiki-inbox` | Process all inbox sources in sequence |
| `/wiki-inbox-parallel` | Same as `/wiki-inbox` but fetches all source types concurrently (8 workers, ~12s for 72 items) |
| `/wiki-reddit` | Scan 14 subreddits, queue discovered URLs |
| `/wiki-links` | Fetch and process URLs from `inbox/links.md` |
| `/wiki-youtube` | Extract knowledge from YouTube transcripts |
| `/wiki-tweets` | Process tweet URLs from `inbox/twitter.md` |
| `/wiki-posts` | Process raw social media text from `inbox/posts.md` |
| `/wiki-clippings` | Process Obsidian Web Clipper exports |

### Maintenance

| Command | What it does |
|---|---|
| `/wiki-check` | Audit Russian sections + `obs.py` broken/orphan health check |
| `/wiki-fix` | Run pytest suite and auto-fix failures in up to 5 rounds |
| `/wiki-index` | Rebuild `index.md` (with orphan markers from obs.py) |
| `/wiki-digest` | Generate weekly bilingual digest; loads `digests/memory.json` to avoid re-explaining known terms |
| `/wiki-search [query]` | Full-text search + relational queries (`tools using RAG`, `all tips`) via `.state/relations/_index.json` |

---

## Scheduled Automation

A Windows Task Scheduler job runs the full pipeline daily at 08:00:

```powershell
# Install (one-time)
schtasks /Create /XML wiki-pipeline-task.xml /TN "LLMWiki\DailyPipeline" /F

# Test immediately
schtasks /Run /TN "LLMWiki\DailyPipeline"

# Watch the log
Get-Content .state\pipeline.log -Wait
```

The wrapper script `wiki-pipeline-run.ps1` checks network connectivity, runs `claude --print /wiki-pipeline`, and appends all output to `.state/pipeline.log` with 5 MB rotation.

---

## Quality Assurance

```powershell
# Run the test suite (285 tests, <1s)
python -m pytest tests/test_wiki.py -v

# Install pre-commit hooks (run once)
pip install pre-commit
pre-commit install
```

Tests validate: front matter completeness, bilingual sections present, no broken `[[wikilinks]]`, index consistency (no missing / no ghost entries), no orphaned pages.

```powershell
# Vault health report (broken links, orphans, top-linked entries)
python scripts/obs.py check

# Who links to an entry?
python scripts/obs.py backlinks lightrag-graph-rag

# Rebuild relational search index after ingestion
python scripts/build_relations.py
```

---

## Entry Format

Each `wiki/<category>/<slug>.md` contains both languages in one file:

```markdown
---
title: "Entry Title"
title_ru: "Название записи"
category: tools
tags: [tag1, tag2, tag3]
updated: 2026-05-17
sources:
  - https://example.com/source
---

## Summary
One or two sentence TL;DR.

## Key Ideas
- Main idea 1
- Main idea 2
- Main idea 3

## Details
Longer explanation, 2-4 paragraphs.

## Related Entries
- [[related-slug-1]]
- [[related-slug-2]]

---
<!-- RU -->

## Краткое описание
Одно-два предложения.

## Ключевые идеи
- Главная идея 1
- Главная идея 2

## Подробнее
Развёрнутое объяснение.

## Связанные записи
- [[related-slug-1]]
- [[related-slug-2]]
```

---

## Scripts

| Script | Purpose |
|---|---|
| `scripts/_template.py` | **Start here for new scripts** — UTF-8 setup, file I/O helpers, `log()`, yt-dlp JSON parser |
| `scripts/obs.py` | Vault analysis CLI: backlinks, orphans, broken links, top-linked, full health check |
| `scripts/build_relations.py` | Build `.state/relations/` index for relational `/wiki-search` queries |
| `scripts/inbox_coordinator.py` | Group inbox items by source type for parallel fetch |
| `scripts/parallel_fetch.py` | Fetch all source types concurrently (ThreadPoolExecutor) |
| `scripts/fetch_url.py` | Fetch a web page and extract article text |
| `scripts/fetch_youtube.py` | Fetch YouTube transcript + metadata |
| `scripts/fetch_reddit.py` | Fetch Reddit posts (cursor-deduped, with comments) |
| `scripts/fetch_twitter.py` | Fetch tweet text and expand t.co URLs |
| `scripts/benchmark_inbox.py` | Benchmark sequential vs parallel inbox processing |

---

## Monitored Subreddits

r/GithubCopilot · r/opencodeCLI · r/opencode · r/ClaudeCode · r/ZaiGLM · r/kimi · r/AI_Agents · r/LocalLLaMA · r/MachineLearning · r/singularity · r/ChatGPT · r/ChatGPTCoding · r/ollama · r/vibecoding

---

## OpenCode Support

`opencode.json` configures per-command model routing for [OpenCode](https://opencode.ai):

- **deepseek-v4-flash** — high-volume ingestion (reddit, links, clippings, posts)
- **kimi-k2.6** — YouTube transcripts and full pipeline
- **glm-5.1** — quality/fix passes (wiki-check, wiki-fix)

---

## License

MIT
