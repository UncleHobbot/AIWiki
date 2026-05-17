---
title: "LLM Wiki Implementations Landscape: State of the Ecosystem (May 2026)"
title_ru: "Ландшафт реализаций LLM-вики: состояние экосистемы (май 2026)"
category: concepts
tags: [llm-wiki, knowledge-base, karpathy, obsidian, second-brain, rag, open-source, academic, ecosystem]
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://arxiv.org/abs/2605.07068
  - https://github.com/topics/llm-wiki-personal-knowledge-base
  - https://llm-wiki.net/
  - https://news.ycombinator.com/item?id=47640875
  - https://pub.towardsai.net/andrej-karpathy-killed-rag-or-did-he-the-llm-wiki-pattern-7824d876e790
---

## Summary
Six weeks after Andrej Karpathy published a 400-line GitHub Gist on April 2, 2026, the LLM Wiki pattern had generated 30+ independent implementations, a peer-reviewed scientific study, a dedicated hub site, and a small SaaS ecosystem — making it one of the fastest-spreading AI architecture ideas of 2026.

## Key Ideas
- The WiCER paper (arXiv:2605.07068) is the only rigorous scientific study: blind LLM Wiki compilation fails catastrophically 53–60% of the time across 17 knowledge domains; most implementations have no quality checks and are unaware of this.
- Two distinct camps have formed: **personal PKM tools** (local-first, Obsidian-centered, single user) and **agent knowledge layers** (multi-agent, structured retrieval APIs, enterprise-grade).
- Hermes Agent (Nous Research) is the only major agent framework to ship the pattern as a built-in skill by default — Claude Code, Codex, and Gemini CLI are used as execution engines but ship no wiki skill out of the box.
- The pattern is converging with "autoresearch" loops: the wiki stores accumulated knowledge from autonomous research cycles, which feed back into the wiki, creating a compounding flywheel.
- The Obsidian dependency is increasingly contested: a growing minority of implementations use plain markdown + Git, arguing Obsidian adds friction without meaningful benefit for machine-maintained wikis.

## Details

### Scale and Speed of Adoption

Karpathy's gist reached an estimated 16–17 million views and 5,000+ stars within weeks. The GitHub topic `llm-wiki-personal-knowledge-base` aggregates 30+ repos; `karpathy-llm-wiki` captures those explicitly crediting the gist. A dedicated ecosystem site (llm-wiki.net) emerged as a skills/plugin registry. VentureBeat covered it as a mainstream architecture story within days of publication.

### The Compilation Gap: The Critical Unsolved Problem

The WiCER paper (Juan M. Huerta, May 2026) is the only peer-reviewed study to directly measure LLM Wiki compilation quality across 17 RepLiQA knowledge domains (6,800 questions). Its core finding: **naive/blind compilation catastrophically fails 53–60% of the time**, compared to a 3.46 baseline RAG failure rate. The paper proposes WiCER (Wiki-memory Compile, Evaluate, Refine) — a CEGAR-inspired iterative loop that closes the gap significantly.

Most community implementations have no systematic quality checks (linting). This is the ecosystem's largest blind spot. The few exceptions are the `llm-wiki-compiler` family of tools and the Hermes Agent implementation, which include health-check passes.

### Personal PKM Implementations (the large camp)

The majority of implementations are personal knowledge base tools following the Obsidian-centered pattern:

- **SamurAIGPT/llm-wiki-agent** (~2,000 stars) — the most cross-platform: works with Claude Code, Codex, OpenCode, Gemini CLI via separate schema files. Notably accepts PDF, DOCX, PPTX, XLSX, EPUB via markitdown conversion, not just markdown.
- **AgriciDaniel/claude-obsidian** (~1,500 stars) — the most feature-complete Obsidian implementation: 10 skills, 2 parallel research agents, hot cache system, `/wiki`, `/save`, and `/autoresearch` slash commands.
- **kytmanov/obsidian-llm-wiki-local** — the privacy-first variant: 100% local using Ollama; no data leaves the machine.
- **NicholasSpisak/second-brain** — clean reference implementation with explicit Obsidian vault structure: `raw/` (inbox), `wiki/` LLM-maintained organized as sources/entities/concepts/synthesis.
- **LLM Wiki v2 gist** (rohitg00) — most substantive published extension of the original pattern: adds memory lifecycle with confidence scoring and retention decay, consolidation tiers (working → procedural memory), and typed knowledge graph.

### Agent Knowledge Layer Implementations

A smaller, more technically sophisticated camp treats the wiki as a programmable knowledge API for multi-agent systems:

- **nvk/llm-wiki** — parallel multi-agent research mode, thesis-driven investigation, also available as a Claude Code marketplace plugin via llm-wiki.net.
- **ktundwal/librarian** — positions itself as "the personal knowledge layer for coding agents": zero API keys, local-first, CLI-first, emphasis on the coding context use case.
- **skyllwt/OmegaWiki** — the most ambitious scope: full academic research lifecycle from arXiv ingestion through peer review response, 23 Claude Code skills, bilingual (EN/ZH), daily arXiv ingestion via GitHub Actions.

### Scientific and Academic Applications

The pattern scales cleanly to academic knowledge:

- **Philosophy** (Paulo de Assis): 3,000 pages of Continental philosophy (Deleuze, Foucault, posthumanism) compiled into a structured, searchable wiki. Demonstrates the pattern is domain-agnostic.
- **Market intelligence** (Minyang Chen): competitive intelligence and market tracking as the primary use case.
- **Academic research lifecycle** (OmegaWiki): full pipeline from paper reading to peer review response.

No chemistry- or biology-specific implementations were found using the Karpathy pattern specifically, though the WiCER paper's 17-domain evaluation spans science topics.

### The Obsidian Debate

Most implementations use Obsidian as the viewer. A growing minority argues against it:
- The Hermes Agent blog post (J. Song) argues VS Code + Git is simpler and more reliable for machine-maintained wikis.
- The HN "git-native implementation" thread gained significant traction by making the same argument.
- Core objection: the graph view and backlink UI that makes Obsidian valuable for human note-takers are less useful when the LLM is doing all the linking — any markdown viewer plus `git log` is sufficient.

### Productization Wave

Within 6 weeks of the gist, a small commercial ecosystem emerged:
- **llm-wiki.net** — hub site acting as a skills/plugin registry for implementations across Claude Code, Codex, OpenCode, and Gemini CLI.
- Multiple SaaS wrappers (Dume.ai, toolhunter.cc, MindStudio) are building commercial wrappers around the pattern.
- **Hermes Agent** (Nous Research) ships the pattern as a first-class built-in, making it available to all users of the framework by default.

### Critical Analysis: When the Pattern Fails

The Towards AI piece by Mandar Karhade MD PhD ("Karpathy Killed RAG. Or Did He?") provides the best critical analysis. Key conclusions:
- LLM Wiki is **better** than RAG for bounded, curated corpora where synthesis across sources matters more than per-query retrieval.
- RAG is **better** for millions of changing documents and precise chunk citations.
- The pattern degrades at scale: as the wiki grows past ~500–1,000 pages, the navigation and lint operations become expensive, and the context window becomes the limiting factor for both compilation and querying.

The WiCER paper adds a more fundamental concern: compilation itself is unreliable without systematic evaluation, and most implementations skip this entirely.

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))

---
<!-- RU -->

## Краткое описание
Через шесть недель после публикации Андреем Карпатым 400-строчного GitHub Gist 2 апреля 2026 года паттерн LLM-вики породил 30+ независимых реализаций, рецензируемое научное исследование, специализированный хаб-сайт и небольшую SaaS-экосистему — став одной из самых быстро распространившихся AI-архитектурных идей 2026 года.

## Ключевые идеи
- Статья WiCER (arXiv:2605.07068) — единственное строгое научное исследование: слепая компиляция LLM-вики катастрофически отказывает в 53–60% случаев по 17 предметным областям; большинство реализаций не имеют проверок качества и не знают об этом.
- Сформировались два лагеря: **инструменты личного PKM** (локально, Obsidian, один пользователь) и **уровни знаний агента** (мульти-агентный, структурированные retrieval API, корпоративный уровень).
- Hermes Agent (Nous Research) — единственный крупный фреймворк агентов, поставляющий паттерн в качестве встроенного навыка; Claude Code, Codex и Gemini CLI используются как движки выполнения, но не содержат wiki-навыков из коробки.
- Паттерн сближается с «autoresearch»-циклами: вики хранит накопленные знания из автономных исследовательских циклов, которые возвращаются в вики, создавая накопительный маховик.
- Зависимость от Obsidian всё больше оспаривается: растущее меньшинство реализаций использует чистый markdown + Git.

## Подробнее

### Масштаб и скорость принятия

Gist Карпатого набрал около 16–17 миллионов просмотров и 5000+ звёзд за несколько недель. GitHub-тема `llm-wiki-personal-knowledge-base` агрегирует 30+ репозиториев; `karpathy-llm-wiki` охватывает те, что явно ссылаются на gist. Появился специализированный экосистемный сайт (llm-wiki.net). VentureBeat осветил его как серьёзную архитектурную историю через несколько дней после публикации.

### Пробел компиляции: главная нерешённая проблема

Статья WiCER (Хуан М. Уэрта, май 2026) — единственное рецензируемое исследование, напрямую измеряющее качество компиляции LLM-вики по 17 доменам RepLiQA (6800 вопросов). Ключевой вывод: **наивная компиляция катастрофически отказывает в 53–60% случаев** по сравнению с базовым уровнем отказов RAG в 3,46. Статья предлагает WiCER — итерационный цикл, вдохновлённый CEGAR, который существенно закрывает этот разрыв.

Большинство реализаций сообщества не имеют систематических проверок качества (lint). Это крупнейшее слепое пятно экосистемы. Немногие исключения — семейство инструментов `llm-wiki-compiler` и реализация Hermes Agent.

### Персональные PKM-реализации

- **SamurAIGPT/llm-wiki-agent** (~2000 звёзд) — наиболее кроссплатформенный: работает с Claude Code, Codex, OpenCode, Gemini CLI; принимает PDF, DOCX, PPTX, XLSX, EPUB через markitdown.
- **AgriciDaniel/claude-obsidian** (~1500 звёзд) — наиболее полная реализация для Obsidian: 10 навыков, 2 параллельных агента, горячий кэш, команды `/wiki`, `/save`, `/autoresearch`.
- **kytmanov/obsidian-llm-wiki-local** — privacy-first: 100% локально через Ollama, данные не покидают машину.
- **LLM Wiki v2 gist** (rohitg00) — наиболее существенное расширение: добавляет жизненный цикл памяти с оценкой уверенности и затуханием, уровни консолидации (рабочая → процедурная память), типизированный граф знаний.

### Агентные слои знаний

- **nvk/llm-wiki** — параллельный мультиагентный режим, тезисно-ориентированное исследование, marketplace-плагин Claude Code через llm-wiki.net.
- **ktundwal/librarian** — «персональный уровень знаний для coding agents»: нулевые API-ключи, локально, CLI-first.
- **skyllwt/OmegaWiki** — самый амбициозный охват: от загрузки arXiv до ответов рецензентам, 23 навыка Claude Code, двуязычный (EN/ZH), ежедневная загрузка arXiv через GitHub Actions.

### Научные и академические применения

Паттерн чисто масштабируется на академические знания: философия (3000 страниц Делёза/Фуко/постгуманизма), конкурентная разведка (рыночная аналитика), полный цикл академических исследований (OmegaWiki). Специфических реализаций для химии или биологии с использованием именно паттерна Карпатого не обнаружено.

### Дискуссия об Obsidian

Большинство реализаций используют Obsidian в качестве просмотрщика. Растущее меньшинство выступает против: VS Code + Git проще и надёжнее для вики, обслуживаемых машиной. Ключевой довод: возможности Obsidian (граф, бэклинки), ценные для людей-заметочников, менее полезны когда все связи создаёт LLM — достаточно любого markdown-просмотрщика и `git log`.

### Критический анализ: когда паттерн не работает

Лучший критический анализ (Mандар Кархаде, Towards AI): LLM-вики **лучше** RAG для ограниченных курируемых корпусов (синтез важнее точного извлечения). RAG **лучше** для миллионов меняющихся документов и точных цитат фрагментов. Паттерн деградирует при масштабировании: свыше ~500–1000 страниц операции навигации и lint становятся дорогостоящими, контекстное окно — узким местом.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))
