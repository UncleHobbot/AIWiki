# AIWiki

Personal AI knowledge base inspired by [Andrej Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) concept. Every entry is bilingual (English + Russian) in a single file.

Raw sources (web clips, Reddit, YouTube, tweets) are automatically distilled into structured wiki entries by LLM agents via [opencode](https://opencode.ai) and [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Architecture

Three-layer pattern:

| Layer | Directory | Purpose |
|---|---|---|
| Raw sources | `inbox/`, `sources/` | Immutable inputs |
| Distilled knowledge | `wiki/` | LLM-written bilingual entries |
| Schema | `AGENTS.md` | Navigation map for agents |

## Stats

- **21 entries** across 7 categories: concepts, tools, agents, models, news, tips, people
- **12 monitored subreddits** scanned daily
- **10 slash commands** for ingestion, search, and maintenance

## Quick Start

```powershell
# Setup (Windows)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\setup.ps1

# Edit credentials
# .env — Reddit API keys (optional, public API works without them)
```

Open in [Obsidian](https://obsidian.md) for graph view and browsing, or use opencode/Claude Code for agent-driven ingestion.

## Commands (opencode)

| Command | Description |
|---|---|
| `/wiki-inbox` | Process everything in `inbox/` |
| `/wiki-links` | Fetch and process URLs |
| `/wiki-reddit` | Scan 12 subreddits for new posts |
| `/wiki-youtube` | Extract knowledge from YouTube transcripts |
| `/wiki-tweets` | Process tweet dumps |
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

## Monitored Subreddits

r/GithubCopilot, r/opencodeCLI, r/opencode, r/ClaudeCode, r/ZaiGLM, r/kimi, r/AI_Agents, r/LocalLLaMA, r/MachineLearning, r/singularity, r/ChatGPT, r/ChatGPTCoding

## License

MIT
