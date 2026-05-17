---
title: "LLM Wiki Ecosystem: Implementations and Variants"
title_ru: "Экосистема LLM-вики: реализации и варианты"
category: tools
tags: [llm-wiki, knowledge-base, obsidian, mcp, open-source, second-brain, karpathy, ecosystem]
updated: 2026-05-17
sources:
  - https://github.com/andysingal/LLMops/blob/main/LLM_Knowledge_bases.md
  - https://github.com/topics/llm-wiki-personal-knowledge-base
  - https://llm-wiki.net/
  - https://arxiv.org/abs/2605.07068
  - https://news.ycombinator.com/item?id=47640875
---

## Summary
A curated map of open-source implementations of Karpathy's LLM Wiki pattern, updated to reflect the May 2026 ecosystem: 30+ repos, a peer-reviewed scientific benchmark (WiCER), a dedicated hub site, and two distinct camps — personal PKM tools and agent knowledge layers.

## Key Ideas
- **The core pattern is a substrate, not a product.** Raw sources → LLM-managed wiki → schema/instructions. Every project below instantiates this same three-layer architecture differently.
- **Two camps have emerged:** *Personal knowledge bases* (single user, local-first, Obsidian/markdown) and *agent knowledge layers* (multi-agent, structured retrieval APIs, explicit lint operations).
- **The compilation gap is the critical unsolved problem.** The only scientific study (WiCER, arXiv:2605.07068) found blind compilation fails 53–60% of the time. Most implementations have no quality checks.
- **Retrieval without RAG.** Most implementations use a simple index file + LLM navigation rather than vector embeddings, sidestepping the infrastructure cost of a vector DB for collections under ~500 documents.
- **Queries compound the wiki.** All mature implementations file valuable query answers back as wiki pages — the compounding property that distinguishes this pattern from RAG.

## Key Implementations

### Personal Knowledge Bases (Obsidian-centered)

| Project | Stars | Key features |
|---|---|---|
| **SamurAIGPT/llm-wiki-agent** | ~2,000 | Cross-platform: Claude Code, Codex, OpenCode, Gemini CLI. Accepts PDF, DOCX, PPTX, XLSX, EPUB via markitdown |
| **AgriciDaniel/claude-obsidian** | ~1,500 | 10 skills, 2 parallel research agents, hot cache, `/wiki` `/save` `/autoresearch` commands |
| **memoriki** | — | LLM Wiki + MemPalace MCP server for real memory. `pip install mempalace` |
| **kytmanov/obsidian-llm-wiki-local** | — | 100% local via Ollama; no data leaves the machine |
| **NicholasSpisak/second-brain** | — | Clean vault structure: `raw/` inbox → `wiki/` with sources/entities/concepts/synthesis |
| **llmwiki** (lucasastorian) | — | FastAPI + Next.js + stdio MCP, SQLite FTS5, hosted version at llmwiki.app |

### Agent Knowledge Layers (multi-agent / API-first)

| Project | Key features |
|---|---|
| **nvk/llm-wiki** | Parallel multi-agent research, thesis-driven investigation, Claude Code marketplace plugin via llm-wiki.net |
| **ktundwal/librarian** | "Personal knowledge layer for coding agents." Zero API keys, CLI-first, local. Emphasis on coding context |
| **skyllwt/OmegaWiki** | Most ambitious: arXiv ingest → KG (9 entity types) → gap detection → idea generation → paper writing → peer review. 23 Claude Code skills, bilingual EN/ZH, daily GitHub Actions |
| **OpenKB** | CLI-based; uses PageIndex for long PDFs without chunking. Structure: sources/ → summaries/ → concepts/ → explorations/ → reports/ |
| **claude-memory-compiler** | Captures Claude Code sessions via hooks → extracts decisions/lessons/patterns → compiles to structured wiki |

### Extensions of the Original Pattern

| Resource | What it adds |
|---|---|
| **LLM Wiki v2 gist** (rohitg00) | Memory lifecycle: confidence scoring, retention decay, consolidation tiers (working → procedural), typed knowledge graph |
| **Hermes Agent skill** (Nous Research) | Only major agent framework to ship LLM Wiki as a built-in; includes ingest/query/lint |
| **llm-wiki.net** | Hub site and plugin registry for implementations across Claude Code, Codex, OpenCode, Gemini CLI |
| **awesome-llm-wiki** (tjiahen) | Community-maintained curated list of all implementations |

### Architecture Pattern

```
YOUR AGENTS
(writer, researcher, strategist, analyst)
        ↓ reads from          ↓ reads from
KNOWLEDGE BASE LAYER    BRAND FOUNDATION
(dynamic, LLM-           (static, human-edited:
maintained, grows)       voice, rules, positioning)
        ↑ compiles from
    raw/ inbox
(tweets, articles, bookmarks, PDFs, notes)
```

## Details

**The WiCER benchmark** is a critical reference for anyone building on this pattern. Juan M. Huerta tested 17 RepLiQA knowledge domains (6,800 questions) and found that naive compilation fails catastrophically. The WiCER loop (Compile → Evaluate → Refine, CEGAR-inspired) closes the gap — but requires the implementation to include a systematic evaluation step that most community projects skip. If you're building or using an LLM Wiki tool, verify it has a lint/health-check pass.

**OmegaWiki** and **Hermes Agent** represent the research/enterprise end of the spectrum. OmegaWiki treats the wiki as the single source of truth for an entire academic lifecycle: 23 Claude Code skills orchestrate each phase from reading the first paper to responding to journal reviewers. Hermes Agent (Nous Research) ships the pattern as a first-class built-in, making it available to all framework users by default.

**The claude-memory-compiler** project applies the pattern to an often-overlooked source: the coding sessions themselves. When Claude Code ends or auto-compacts, a hook spawns a background process that extracts decisions, lessons, and patterns from the transcript. These are compiled into a wiki — your Claude Code usage history becomes a knowledge base without any manual note-taking.

**The Obsidian debate** is growing. A minority — exemplified by the Hermes Agent blog (J. Song, "Why I'm Not Using Obsidian") and the HN "git-native" thread — argues VS Code + Git suffices. The graph-view and backlink UI that make Obsidian valuable for human note-takers are less useful when the LLM is doing all the linking.

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-implementations-landscape]] ([LLM Wiki Implementations Landscape: State of the Ecosystem (May 2026)](../concepts/llm-wiki-implementations-landscape.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[llm-wiki-enterprise-patterns]] ([LLM Wiki for Enterprise and Agents](../agents/llm-wiki-enterprise-patterns.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))

---
<!-- RU -->

## Краткое описание
Кураторская карта реализаций паттерна LLM-вики Карпатого, обновлённая до состояния на май 2026: 30+ репозиториев, рецензируемый научный бенчмарк (WiCER), специализированный хаб-сайт и два лагеря — инструменты персонального PKM и агентные слои знаний.

## Ключевые идеи
- **Паттерн — это подложка, не продукт.** Сырые источники → LLM-управляемая вики → схема/инструкции. Каждый проект ниже реализует одну и ту же трёхуровневую архитектуру по-своему.
- **Сложились два лагеря:** *Персональные базы знаний* (один пользователь, локально, Obsidian) и *уровни знаний агента* (мульти-агентные, структурированные API, явные lint-операции).
- **Пробел компиляции — главная нерешённая проблема.** Единственное научное исследование (WiCER) выявило 53–60% катастрофических отказов при слепой компиляции. Большинство реализаций не имеют проверок качества.
- **Поиск без RAG.** Большинство реализаций используют простой индексный файл + навигацию LLM, не требующие векторной БД до ~500 документов.
- **Запросы пополняют вики.** Все зрелые реализации сохраняют ценные ответы на запросы обратно как страницы вики.

## Ключевые реализации

### Персональные базы знаний (Obsidian-центрированные)

| Проект | Звёзды | Ключевые особенности |
|---|---|---|
| **SamurAIGPT/llm-wiki-agent** | ~2000 | Кроссплатформенный: Claude Code, Codex, OpenCode, Gemini CLI; принимает PDF, DOCX, PPTX, XLSX, EPUB |
| **AgriciDaniel/claude-obsidian** | ~1500 | 10 навыков, 2 параллельных агента, горячий кэш, команды `/wiki` `/save` `/autoresearch` |
| **memoriki** | — | LLM Wiki + MCP-сервер MemPalace для настоящей памяти |
| **kytmanov/obsidian-llm-wiki-local** | — | 100% локально через Ollama; данные не покидают машину |
| **NicholasSpisak/second-brain** | — | Чистая структура vault: `raw/` inbox → `wiki/` с источниками/сущностями/концепциями/синтезом |
| **llmwiki** (lucasastorian) | — | FastAPI + Next.js + stdio MCP, SQLite FTS5, хостируемая версия llmwiki.app |

### Агентные слои знаний

| Проект | Ключевые особенности |
|---|---|
| **nvk/llm-wiki** | Параллельный мультиагентный режим, тезисное исследование, marketplace-плагин Claude Code |
| **ktundwal/librarian** | «Персональный уровень знаний для coding agents»: нулевые API-ключи, CLI-first, локально |
| **skyllwt/OmegaWiki** | Самый амбициозный: arXiv → граф знаний → обнаружение пробелов → написание статей → рецензии. 23 навыка Claude Code, двуязычный, ежедневные GitHub Actions |
| **OpenKB** | CLI; PageIndex для длинных PDF без нарезки |
| **claude-memory-compiler** | Захватывает сессии Claude Code через хуки → компилирует решения/уроки в вики |

### Расширения оригинального паттерна

| Ресурс | Что добавляет |
|---|---|
| **LLM Wiki v2 gist** (rohitg00) | Жизненный цикл памяти: уверенность, затухание, уровни консолидации, типизированный граф |
| **Hermes Agent** (Nous Research) | Единственный крупный фреймворк агентов со встроенным LLM Wiki |
| **llm-wiki.net** | Хаб-сайт и реестр плагинов для Claude Code, Codex, OpenCode, Gemini CLI |

## Подробнее

**Бенчмарк WiCER** — критически важный ориентир для всех, кто строит на этом паттерне: без систематического шага оценки компиляция отказывает в более чем половине случаев. Проверьте наличие lint/health-check в любом инструменте LLM-вики, прежде чем доверять ему свои знания.

**OmegaWiki** и **Hermes Agent** представляют исследовательский/корпоративный конец спектра. OmegaWiki использует вики как единый источник истины для полного академического жизненного цикла. Hermes Agent поставляет паттерн как встроенный навык по умолчанию — единственный крупный фреймворк, сделавший это.

**Дебаты об Obsidian** усиливаются. Растущее меньшинство (пост в блоге Hermes Agent, HN-тред о git-native реализации) утверждает, что VS Code + Git достаточно — возможности Obsidian, ценные для людей-заметочников, менее полезны, когда LLM создаёт все связи.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-implementations-landscape]] ([LLM Wiki Implementations Landscape: State of the Ecosystem (May 2026)](../concepts/llm-wiki-implementations-landscape.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[llm-wiki-enterprise-patterns]] ([LLM Wiki for Enterprise and Agents](../agents/llm-wiki-enterprise-patterns.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))
