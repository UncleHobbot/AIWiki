---
title: "LLM Wiki for Enterprise and Agents"
title_ru: "LLM-вики для бизнеса и агентных систем"
category: agents
tags: [llm-wiki, enterprise, multi-agent, claude-code, ai-agency, knowledge-management, production]
updated: 2026-05-15
sources:
  - https://www.youtube.com/watch?v=ijBJVzxSBRA
---

## Summary
How the LLM Wiki 3-layer pattern (raw sources → wiki → schema) scales from personal knowledge management to production AI agency operations with 20+ specialized agents handling client work.

## Key Ideas
- **One pattern, business scale:** The same 3-layer pattern Karpathy uses for personal wikis can organize entire AI-first businesses — each "department" or agent plugin gets its own raw/wiki/schema structure.
- **Structured JSON as the wiki layer:** In production, the wiki layer doesn't have to be prose markdown — it can be typed JSON schemas (audit data, storyboard specs) that downstream agents parse deterministically.
- **Per-agent memory files:** Each agent maintains its own running memory file (markdown) that it updates over time; this is lighter-weight than RAG and doesn't require vector database infrastructure.
- **Context injection, not context bloat:** The schema (CLAUDE.md / skill.md) tells the agent exactly where to find specific information — preventing it from scanning everything and bloating the context window unnecessarily.
- **80% time savings demonstrated:** An AI agency (APG Software) reduced client audit processing from ~200 hours to 20–40 hours by applying this pattern to multi-agent audit pipelines fed by meeting transcripts, emails, and calls via Fathom/Twilio/Gmail.
- **Video editor pipeline example:** Raw 4K video → ingest agent (transcribe, create proxy, audio analysis) → storyboard JSON (the "wiki" layer) → Remotion renderer. The storyboard is effectively a wiki telling the AI exactly how to construct the final output.

## Details
Adam Goodyer (APG Software) has been running this architecture across 20+ agents for 6 months in a production client-facing AI agency. The key insight is that the 3-layer pattern solves a scalability problem: as the number of agents, clients, and data sources grows, unstructured information creates context window bloat. The schema layer (CLAUDE.md / skill.md) becomes a navigation map that tells each agent where to look, what format the data is in, and which other agents or tools are available.

**Audit agent example:**
- Raw layer: meeting transcripts (Fathom), emails (Gmail), call recordings (Twilio)
- Wiki layer: structured JSON capturing for each business process — who does it, how long it takes, how often, what tools they use, pain points
- Schema: skill.md file that tells the audit agent where the data lives, what the JSON schema looks like, and which downstream agents can consume it

**Video editor pipeline:**
- Raw layer: raw 4K video files dropped into an ingest folder
- Wiki layer: storyboard JSON specifying timestamps, transcript segments, zoom effects, motion graphics
- Schema: skill.md for long-form video, referencing pacing rules, templates, and the Remotion skill
- Result: fully AI-edited videos without human involvement in the editing step

**Why this beats RAG for agents:**
Setting up and maintaining a vector database is overkill for many agentic use cases. Structured JSON/markdown with a navigation schema is lighter, cheaper, more deterministic, and easier to debug. The agent knows exactly where to look rather than doing semantic search over everything.

**Key principle — controlled context injection:** Structure information so agents receive only the context relevant to their current task. This preserves context window space and improves response accuracy at scale.

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))

---
<!-- RU -->

## Краткое описание
Как паттерн LLM-вики с тремя уровнями (сырые источники → вики → схема) масштабируется от личного управления знаниями до продакшн-операций AI-агентства с 20+ специализированными агентами.

## Ключевые идеи
- **Один паттерн — бизнес-масштаб:** Та же трёхуровневая структура, которую Карпаты использует для личных вики, организует целые AI-first-бизнесы — каждый «отдел» или плагин-агент получает свои raw/wiki/schema.
- **Типизированный JSON как уровень вики:** В продакшн-среде уровень вики не обязан быть прозаическим markdown — это может быть типизированный JSON (данные аудита, спецификации сторибордов), который нижестоящие агенты парсят детерминированно.
- **Персональные файлы памяти агента:** Каждый агент ведёт собственный running-файл памяти (markdown), обновляемый со временем — это легче, чем RAG, и не требует векторной базы данных.
- **Инъекция контекста, а не его раздувание:** Схема (CLAUDE.md / skill.md) указывает агенту, где именно искать нужную информацию — предотвращая сканирование всего подряд и раздувание контекстного окна.
- **Экономия времени 80%:** AI-агентство (APG Software) сократило обработку клиентских аудитов с ~200 часов до 20–40, применив этот паттерн к многоагентным пайплайнам на основе транскриптов встреч, писем и звонков через Fathom/Twilio/Gmail.
- **Пример пайплайна видеоредактора:** Сырое 4K-видео → агент инжеста (транскрипция, прокси, аудиоанализ) → стрибоард JSON (уровень «вики») → рендерер Remotion. Стрибоард фактически является вики, указывающей ИИ, как собрать финальный результат.

## Подробнее
Адам Гудьер (APG Software) использует эту архитектуру на 20+ агентах в продакшн AI-агентстве уже 6 месяцев. Ключевое открытие: трёхуровневый паттерн решает проблему масштабируемости. По мере роста числа агентов, клиентов и источников данных неструктурированная информация раздувает контекстные окна. Уровень схемы (CLAUDE.md / skill.md) становится навигационной картой, указывающей каждому агенту, куда смотреть, в каком формате данные, и какие другие агенты или инструменты доступны.

**Почему это лучше RAG для агентов:**
Настройка и поддержка векторной базы данных избыточны для многих агентных задач. Структурированный JSON/markdown с навигационной схемой легче, дешевле, более детерминирован и проще в отладке. Агент знает, где именно искать, вместо семантического поиска по всему.

**Ключевой принцип — управляемая инъекция контекста:** Структурируйте информацию так, чтобы агенты получали только контекст, релевантный их текущей задаче. Это сохраняет пространство контекстного окна и повышает точность ответов при масштабировании.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
