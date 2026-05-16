# AIWiki

Personal AI knowledge base inspired by [Andrej Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) concept. Every entry is bilingual (English + Russian) in a single file.

Raw sources (web clips, Reddit, YouTube, tweets, social posts) are automatically distilled into structured wiki entries by LLM agents via [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Architecture

Three-layer pattern:

| Layer | Directory | Purpose |
|---|---|---|
| Raw sources | `inbox/`, `sources/` | Immutable inputs |
| Distilled knowledge | `wiki/` | LLM-written bilingual entries |
| Schema | `CLAUDE.md` | Navigation map for agents |

## Stats

- **61 entries** across 6 active categories: concepts, tools, agents, models, news, tips
- **14 monitored subreddits** scanned daily
- **11 slash commands** for ingestion, search, and maintenance

## Quick Start

```powershell
# Setup (Windows)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\setup.ps1

# Edit credentials
# .env — Reddit API keys (optional, public API works without them)
```

Open in [Obsidian](https://obsidian.md) for graph view and browsing, or use Claude Code for agent-driven ingestion.

## Commands (Claude Code)

| Command | Description |
|---|---|
| `/wiki-inbox` | Process everything in `inbox/` (runs all sub-commands) |
| `/wiki-links` | Fetch and process URLs from `inbox/links.md` |
| `/wiki-reddit` | Scan 14 subreddits for new posts |
| `/wiki-youtube` | Extract knowledge from YouTube transcripts |
| `/wiki-tweets` | Process tweet URLs from `inbox/twitter.md` |
| `/wiki-posts` | Process raw social media text posts from `inbox/posts.md` |
| `/wiki-clippings` | Process Obsidian Web Clipper exports |
| `/wiki-digest` | Generate weekly bilingual digest |
| `/wiki-index` | Rebuild `index.md` |
| `/wiki-search` | Search wiki entries |
| `/wiki-check` | Fix entries missing Russian section |

## Entry Format

Each `wiki/<category>/<slug>.md` contains both languages:

```markdown
---
title: "Entry Title"
title_ru: "Название записи"
category: tools
tags: [tag1, tag2]
sources:
  - https://example.com/source
---

## Summary
English content here...

---
<!-- RU -->

## Краткое описание
Русский контент здесь...
```

## Inbox Files

| File | Purpose |
|---|---|
| `inbox/links.md` | URLs to fetch and process |
| `inbox/youtube.md` | YouTube video URLs |
| `inbox/twitter.md` | Tweet URLs |
| `inbox/posts.md` | Raw social media text posts (LinkedIn, Bluesky, etc.) |
| `inbox/clippings/` | Obsidian Web Clipper `.md` exports |

## Monitored Subreddits

r/GithubCopilot, r/opencodeCLI, r/opencode, r/ClaudeCode, r/ZaiGLM, r/kimi, r/AI_Agents, r/LocalLLaMA, r/MachineLearning, r/singularity, r/ChatGPT, r/ChatGPTCoding, r/ollama, r/vibecoding

## License

MIT
