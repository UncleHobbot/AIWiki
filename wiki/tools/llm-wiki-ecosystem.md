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
A curated map of open-source implementations of Karpathy's LLM Wiki pattern, updated to reflect the May 2026 ecosystem: 30+ repos, a peer-reviewed scientific benchmark (WiCER), a dedicated hub site, and two distinct camps — personal PKM tools and agent knowledge layers. Includes a direct comparison with AIWiki and a list of ideas worth borrowing.

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
| [**SamurAIGPT/llm-wiki-agent**](https://github.com/SamurAIGPT/llm-wiki-agent) | ~2,000 | Cross-platform: Claude Code, Codex, OpenCode, Gemini CLI. Accepts PDF, DOCX, PPTX, XLSX, EPUB via markitdown |
| [**AgriciDaniel/claude-obsidian**](https://github.com/AgriciDaniel/claude-obsidian) | ~1,500 | 10 skills, 2 parallel research agents, hot cache, `/wiki` `/save` `/autoresearch` commands |
| [**memoriki**](https://github.com/AyanbekDos/memoriki) | — | LLM Wiki + [MemPalace MCP server](https://github.com/AyanbekDos/memoriki) (29 MCP tools: palace reads/writes, KG ops, agent diaries). Semantic search over verbatim stored text — no summarization |
| [**kytmanov/obsidian-llm-wiki-local**](https://github.com/kytmanov/obsidian-llm-wiki-local) | — | 100% local via Ollama; no data leaves the machine |
| [**NicholasSpisak/second-brain**](https://github.com/NicholasSpisak/second-brain) | — | Clean vault structure: `raw/` inbox → `wiki/` with sources/entities/concepts/synthesis sub-layers |
| [**llmwiki**](https://github.com/lucasastorian/llmwiki) (lucasastorian) | — | FastAPI + Next.js + stdio MCP, SQLite FTS5, hosted at [llmwiki.app](https://llmwiki.app) |

### Agent Knowledge Layers (multi-agent / API-first)

| Project | Key features |
|---|---|
| [**nvk/llm-wiki**](https://github.com/nvk/llm-wiki) | Parallel multi-agent research, thesis-driven investigation, topic archive, confidence scoring, Claude Code marketplace plugin via [llm-wiki.net](https://llm-wiki.net/) |
| [**ktundwal/librarian**](https://github.com/ktundwal/librarian) | "Personal knowledge layer for coding agents." Zero API keys, CLI-first, local. Associative recall by semantic connection, not just keywords |
| [**skyllwt/OmegaWiki**](https://github.com/skyllwt/OmegaWiki) | Most ambitious: arXiv ingest → KG (9 entity types) → gap detection → idea generation → paper writing → peer review. 23 Claude Code skills, bilingual EN/ZH, daily GitHub Actions (arXiv at UTC 00:17 → SMTP digest) |
| [**OpenKB**](https://github.com/VectifyAI/OpenKB) | CLI by VectifyAI; uses [PageIndex](https://github.com/VectifyAI/PageIndex) for long PDFs (hierarchical tree, no vector DB). Structure: sources/ → summaries/ → concepts/ → explorations/ → reports/ |
| [**claude-memory-compiler**](https://github.com/coleam00/claude-memory-compiler) | Captures Claude Code sessions via hooks → Claude Agent SDK extracts decisions/lessons → compiles to cross-referenced wiki. Auto-compiles at end of day if daily log changed |
| [**mduongvandinh/llm-wiki**](https://github.com/mduongvandinh/llm-wiki) | Auto-discovery (`/discover` finds new sources from the web); built-in Reddit scanning + GitHub tracking; ready-made variants for book companion, competitive intel, job search |

### Extensions of the Original Pattern

| Resource | What it adds |
|---|---|
| [**LLM Wiki v2 gist**](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) (rohitg00) | Memory lifecycle: confidence scoring, retention decay, consolidation tiers (working → procedural), typed knowledge graph |
| [**Hermes Agent skill**](https://github.com/NousResearch/hermes-agent/tree/main/skills/research/llm-wiki) (Nous Research) | Only major agent framework to ship LLM Wiki as a built-in; [SKILL.md](https://github.com/NousResearch/hermes-agent/blob/main/skills/research/llm-wiki/SKILL.md) includes ingest/query/lint |
| [**llm-wiki.net**](https://llm-wiki.net/) | Hub site and plugin registry for implementations across Claude Code, Codex, OpenCode, Gemini CLI |
| [**awesome-llm-wiki**](https://github.com/tjiahen/awesome-llm-wiki) (tjiahen) | Community-maintained curated list of all implementations |
| [**WiCER benchmark**](https://arxiv.org/abs/2605.07068) (Huerta 2026) | Only peer-reviewed quality benchmark: 53–60% blind compilation failure rate across 17 domains |

---

## Comparison with AIWiki

AIWiki (this project) is most architecturally similar to **nvk/llm-wiki** and **skyllwt/OmegaWiki**. The table shows where AIWiki leads, matches, and lags.

| Feature | AIWiki | nvk/llm-wiki | OmegaWiki | mduongvandinh |
|---|---|---|---|---|
| Bilingual output | **EN + RU (unique)** | EN only | EN + ZH | VI + EN |
| Windows-first | **Yes (unique)** | macOS-first | Linux/macOS | macOS-first |
| Reddit scanning | **14 subreddits** | None | None | Built-in |
| Source types | Reddit, YouTube, links, tweets, clips, posts | Links, web | arXiv only | Reddit, GitHub, web |
| Parallel fetch | **ThreadPoolExecutor** | Multi-agent | GitHub Actions | Sequential |
| Quality tests | **pytest + pre-commit (unique)** | None found | None found | None found |
| Vault analysis | **obsidiantools + obs.py** | None | None | None |
| Relation index | **by_tag + by_alias + by_category** | None | None | None |
| Digest memory | **digests/memory.json** | None | SMTP digest | None |
| Confidence field | Yes (just added) | Yes (built-in) | No | No |
| Topic archive | No | **Yes** | No | No |
| Thesis articles | No | **Yes** | Partial | No |
| Inventory tracking | No | **Yes** | No | No |
| Scheduled automation | **Windows Task Scheduler** | cron | GitHub Actions | Manual |
| Entries | **~105 (active)** | User-dependent | Auto-growing | User-dependent |

**Where AIWiki is unique among all known implementations:**
- Only EN+RU bilingual implementation
- Only Windows-native implementation
- Only project with a pytest entry-validation suite + pre-commit hooks
- Only project with `obs.py` obsidiantools-backed backlink/orphan analysis
- Only project with a relational search index (`by_alias`, `by_tag`)

**Where nvk/llm-wiki leads AIWiki:**
- Topic archive (`.archive/` for old interests — keeps context clean)
- Thesis articles (`wiki/theses/`) with `verdict: proven|refuted|contested`
- Inventory tracking (durable items, candidates, entities with status/priority)
- Directory-level `_index.md` files (every subdirectory has its own navigable index)
- Multi-wiki peek (cross-topic queries)

**Where OmegaWiki leads AIWiki:**
- Daily automated arXiv ingestion via GitHub Actions (no manual trigger needed)
- SMTP digest delivery (push, not pull — digest arrives in your inbox)
- Novelty check against existing wiki before writing new entries (avoids duplication proactively)
- Full academic lifecycle in a single coherent system

---

## What Ideas We Can Steal

Concrete features from other implementations worth adapting to AIWiki's architecture:

**1. Auto-discovery (`/wiki-discover`) — from mduongvandinh/llm-wiki**
Rather than waiting for URLs to appear in `inbox/links.md`, a discover command proactively finds new relevant sources: given a topic or tag, search the web for recent articles, papers, and repos and propose them for ingestion. We already scan Reddit; this would extend to the broader web.

**2. Session knowledge capture — from claude-memory-compiler**
After each Claude Code session (on session end or auto-compact), a hook extracts key decisions, patterns, and lessons into a daily log entry, which gets compiled into wiki entries. We already log runs in `log.md`; the missing piece is extracting *knowledge* from session transcripts automatically, not just activity metadata.

**3. Directory-level `_index.md` — from nvk/llm-wiki**
Every `wiki/<category>/` directory gets its own `_index.md` with a contents table, category stats, and recent changes. This replaces the single monolithic `index.md` with navigable per-category indexes. Better for large vaults and more informative for agents starting in an unfamiliar category.

**4. SMTP daily digest — from OmegaWiki**
Instead of generating a digest that you have to go find, push it to an email address (or Telegram) automatically after the daily pipeline run. One webhook + SMTP call appended to `wiki-pipeline-run.ps1`.

**5. Novelty check before compile — from OmegaWiki**
Before writing a new wiki entry, run a quick similarity search against existing entries (by title, tags, or key phrases). Flag near-duplicates for human review rather than silently creating a second entry on the same topic. Our `obs.py` backlinks already detect explicit cross-links; this would catch semantic duplicates from different source paths.

**6. Thesis articles (`wiki/theses/`) — from nvk/llm-wiki**
A dedicated article type with `verdict: proven|refuted|contested|open` frontmatter for contentious questions ("Does vibe coding improve or hurt code quality?", "Is LLM Wiki compilation safe without lint?"). Currently we handle this with `## Debate` sections in regular entries; a proper thesis type makes evidence tracking first-class.

**7. PageIndex for long PDFs — from OpenKB/VectifyAI**
Our current YouTube/PDF ingestion reads transcripts as flat text. For papers longer than ~20 pages, a hierarchical page-tree index (PageIndex) lets the LLM navigate efficiently without chunking. Relevant once the research paper inbox grows.

---

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
- [[gnosis-mcp-vs-llm-wiki-pattern]] ([Gnosis MCP vs. LLM Wiki Pattern](../concepts/gnosis-mcp-vs-llm-wiki-pattern.md))
- [[hermes-agent-llm-wiki-integration]] ([Hermes Agent + LLM Wiki](../agents/hermes-agent-llm-wiki-integration.md))
---
<!-- RU -->

## Краткое описание
Кураторская карта реализаций паттерна LLM-вики Карпатого (май 2026): 30+ репозиториев, рецензируемый бенчмарк WiCER, хаб-сайт и два лагеря — персональный PKM и агентный слой знаний. Включает прямое сравнение с AIWiki и список идей для заимствования.

## Ключевые идеи
- **Паттерн — это подложка, не продукт.** Каждый проект по-своему реализует одну трёхуровневую архитектуру: сырые источники → LLM-вики → схема.
- **Два лагеря:** персональные базы знаний (Obsidian, локально) и агентные слои знаний (мультиагентные, structured API, lint).
- **Пробел компиляции — главная нерешённая проблема.** WiCER: 53–60% отказов при слепой компиляции. Большинство реализаций не имеют проверок качества.
- **Поиск без RAG.** Простой index.md + LLM-навигация вместо векторной БД — достаточно для корпусов до ~500 документов.
- **Запросы пополняют вики.** Зрелые реализации сохраняют ценные ответы обратно как страницы вики.

## Ключевые реализации

### Персональные базы знаний (Obsidian-центрированные)

| Проект | Звёзды | Ключевые особенности |
|---|---|---|
| [**SamurAIGPT/llm-wiki-agent**](https://github.com/SamurAIGPT/llm-wiki-agent) | ~2000 | Кросс-платформенный: Claude Code, Codex, OpenCode, Gemini CLI; принимает PDF, DOCX, PPTX, XLSX, EPUB |
| [**AgriciDaniel/claude-obsidian**](https://github.com/AgriciDaniel/claude-obsidian) | ~1500 | 10 навыков, 2 параллельных агента, горячий кэш, команды `/wiki` `/save` `/autoresearch` |
| [**memoriki**](https://github.com/AyanbekDos/memoriki) | — | LLM Wiki + MCP-сервер MemPalace (29 MCP-инструментов). Семантический поиск по дословно сохранённому тексту |
| [**kytmanov/obsidian-llm-wiki-local**](https://github.com/kytmanov/obsidian-llm-wiki-local) | — | 100% локально через Ollama; данные не покидают машину |
| [**NicholasSpisak/second-brain**](https://github.com/NicholasSpisak/second-brain) | — | Структура: `raw/` inbox → `wiki/` с подслоями sources/entities/concepts/synthesis |
| [**llmwiki**](https://github.com/lucasastorian/llmwiki) (lucasastorian) | — | FastAPI + Next.js + stdio MCP, SQLite FTS5, хостируемая версия на [llmwiki.app](https://llmwiki.app) |

### Агентные слои знаний

| Проект | Ключевые особенности |
|---|---|
| [**nvk/llm-wiki**](https://github.com/nvk/llm-wiki) | Параллельный мульти-агент, тезисное исследование, архив тем, confidence scoring, marketplace-плагин Claude Code |
| [**ktundwal/librarian**](https://github.com/ktundwal/librarian) | Нулевые API-ключи, CLI-first, локально; ассоциативный поиск по семантической связи |
| [**skyllwt/OmegaWiki**](https://github.com/skyllwt/OmegaWiki) | arXiv → граф знаний → генерация идей → написание статей → рецензии. 23 навыка Claude Code, двуязычный EN/ZH, ежедневные GitHub Actions |
| [**OpenKB**](https://github.com/VectifyAI/OpenKB) | PageIndex для длинных PDF без векторной БД. Структура: sources/ → summaries/ → concepts/ → explorations/ |
| [**claude-memory-compiler**](https://github.com/coleam00/claude-memory-compiler) | Захватывает сессии Claude Code → компилирует решения/уроки в вики. Авто-компиляция в конце дня |
| [**mduongvandinh/llm-wiki**](https://github.com/mduongvandinh/llm-wiki) | Авто-обнаружение источников (`/discover`); сканирование Reddit и отслеживание GitHub; варианты для конкурентной разведки |

### Расширения оригинального паттерна

| Ресурс | Что добавляет |
|---|---|
| [**LLM Wiki v2 gist**](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) (rohitg00) | Жизненный цикл памяти: затухание, уровни консолидации, типизированный граф знаний |
| [**Hermes Agent**](https://github.com/NousResearch/hermes-agent/tree/main/skills/research/llm-wiki) (Nous Research) | Единственный крупный фреймворк со встроенным LLM Wiki |
| [**llm-wiki.net**](https://llm-wiki.net/) | Хаб и реестр плагинов |
| [**awesome-llm-wiki**](https://github.com/tjiahen/awesome-llm-wiki) | Community-maintained список всех реализаций |
| [**WiCER**](https://arxiv.org/abs/2605.07068) (Huerta 2026) | Единственный рецензируемый бенчмарк: 53–60% отказов слепой компиляции |

---

## Сравнение с AIWiki

AIWiki архитектурно ближе всего к nvk/llm-wiki и skyllwt/OmegaWiki.

**Уникальные возможности AIWiki среди всех известных реализаций:**
- Единственная EN+RU двуязычная реализация
- Единственная Windows-native реализация
- Единственный проект с pytest-валидацией записей + pre-commit хуками
- Единственный с `obs.py` (obsidiantools) для анализа обратных ссылок/сирот
- Единственный с реляционным индексом поиска (`by_alias`, `by_tag`, `by_category`)

**Где nvk/llm-wiki опережает AIWiki:** архив тем, тезисные статьи, отслеживание инвентаря, директориальные `_index.md`, мульти-вики peering.

**Где OmegaWiki опережает AIWiki:** ежедневная автоматическая загрузка arXiv, SMTP-рассылка дайджеста, проверка новизны перед компиляцией.

## Что можно позаимствовать

1. **Авто-обнаружение источников** (mduongvandinh) — команда `/discover`, которая находит новые релевантные источники в интернете по тегу или теме, не дожидаясь ручного добавления в inbox.

2. **Захват знаний из сессий** (claude-memory-compiler) — хук извлекает ключевые решения и паттерны из транскриптов Claude Code и компилирует их в статьи вики.

3. **Директориальные `_index.md`** (nvk/llm-wiki) — каждая `wiki/<категория>/` получает собственный индекс с таблицей содержимого и статистикой.

4. **SMTP-рассылка дайджеста** (OmegaWiki) — после ежедневного запуска пайплайна дайджест отправляется на email или в Telegram.

5. **Проверка новизны перед компиляцией** (OmegaWiki) — быстрый поиск по существующим записям перед созданием новой, чтобы не плодить дубликаты.

6. **Тезисные статьи** (nvk/llm-wiki) — тип записи `wiki/theses/` с полем `verdict: proven|refuted|contested|open` для спорных вопросов.

7. **PageIndex для длинных PDF** (OpenKB) — иерархический индекс страниц вместо плоской нарезки для документов длиннее 20 страниц.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-implementations-landscape]] ([LLM Wiki Implementations Landscape: State of the Ecosystem (May 2026)](../concepts/llm-wiki-implementations-landscape.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[llm-wiki-enterprise-patterns]] ([LLM Wiki for Enterprise and Agents](../agents/llm-wiki-enterprise-patterns.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))
- [[gnosis-mcp-vs-llm-wiki-pattern]] ([Gnosis MCP vs. LLM Wiki Pattern](../concepts/gnosis-mcp-vs-llm-wiki-pattern.md))
- [[hermes-agent-llm-wiki-integration]] ([Hermes Agent + LLM Wiki](../agents/hermes-agent-llm-wiki-integration.md))
