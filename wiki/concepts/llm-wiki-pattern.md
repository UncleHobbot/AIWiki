---
title: "LLM Wiki Pattern"
title_ru: "Паттерн LLM-вики"
category: concepts
tags: [knowledge-base, rag, obsidian, karpathy, agent, personal-wiki, compounding-knowledge]
updated: 2026-05-15
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5
  - https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code
  - https://www.reddit.com/r/AI_Agents/comments/1sqg5ew/spent_a_weekend_actually_understanding_and/
---

## Summary
A pattern proposed by Andrej Karpathy where an LLM agent incrementally builds and maintains a persistent, structured wiki from raw source documents — rather than re-deriving knowledge from scratch on every query (as in RAG).

## Key Ideas
- **Compile, don't retrieve:** Raw docs are "source code"; the wiki is the compiled "binary." The LLM synthesizes sources once and keeps the wiki current — knowledge accumulates instead of being re-derived per query.
- **Three-layer architecture:** (1) Raw sources — immutable ground truth; (2) The wiki — LLM-owned markdown files; (3) The schema — a CLAUDE.md/AGENTS.md that turns the agent into a disciplined wiki maintainer.
- **Three operations:** *Ingest* (new source → LLM reads, writes/updates 10–15 wiki pages), *Query* (LLM reads wiki, synthesizes answer; good answers get filed back as new pages), *Lint* (periodic audit: find contradictions, orphan pages, stale claims).
- **Navigation files:** `index.md` is a content-oriented catalog of all pages; `log.md` is append-only chronological history — together they let the LLM navigate at moderate scale (~100–500 sources) without embedding infrastructure.
- **vs. RAG:** RAG is better for millions of changing documents and precise chunk citations; LLM Wiki is better for bounded curated corpora where synthesis across sources matters more than per-query retrieval.
- **Memex connection:** Realises Vannevar Bush's 1945 Memex vision — private, actively curated knowledge with associative trails — made viable because LLMs handle the bookkeeping humans always abandon.

## Details
Karpathy published the idea on April 2, 2026 as a GitHub Gist titled `llm-wiki.md`, intended as an "idea file" to be pasted into any LLM agent, which then instantiates the pattern for its specific domain.

The core insight is a compilation analogy from software engineering: you don't re-execute source code on every program run — you compile it once into a binary. Similarly, you shouldn't re-read raw documents on every LLM query; you compile them once into a structured wiki and query *that*. The wiki is a persistent, compounding artifact: cross-references are pre-built, contradictions are pre-flagged, and every new source added makes the whole richer.

A key risk of the pattern is that hallucinations can get baked into wiki pages as "facts," then propagate via cross-links. Pure RAG limits hallucinations to a single query; LLM Wiki can spread them. This makes the Lint step non-optional for serious use, and periodic spot-checking against raw sources is recommended.

In Karpathy's own setup: Obsidian is the viewer (IDE), the LLM agent is the programmer, and the wiki is the codebase. The human's role shifts from filing/organizing to curating sources and asking better questions.

For search at scale beyond `index.md`, [qmd](https://github.com/qmd-lab/qmd) is recommended — a local markdown search engine with hybrid BM25/vector search and an MCP server, usable by the LLM as a native tool.

## Debate
The LLM Wiki pattern has attracted both enthusiasm and critique since Karpathy published the gist (41,000+ bookmarks in the first week).

**Critique (community voices):**
- *Hallucinations bake in permanently:* In pure RAG, a hallucination affects one answer. In LLM Wiki, a misunderstood source can get written into a wiki page as "fact" and propagate via cross-links to other pages before anyone notices. This makes the Lint step non-optional.
- *Not production-ready at scale:* The pattern is designed for ~100–500 curated sources. For larger, rapidly changing corpora, the cost of re-ingesting updates and maintaining consistency grows faster than the benefit.
- *High per-ingest LLM cost:* Writing and updating 10–15 wiki pages per new source is expensive at scale. For a team ingesting dozens of sources daily, the token costs compound.
- *Context layer design matters:* Nate B Jones ("Open Brain") argues that LLM Wiki and Open Brain solve the same problem differently — choosing your "context layer" architecture is "one of the single most important things you can do in 2026." Neither is universally superior.

**Industry validation:**
Pinecone — the company that built the market-leading vector database powering most RAG systems — independently converged on the same compiled-knowledge-layer concept with their "Nexus" product launch (May 2026), citing 85% of agent effort wasted on retrieval and 50–60% task completion rates with agentic RAG. See [[pinecone-nexus]].

## Notable Quotes
> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass." — Andrej Karpathy

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." — Andrej Karpathy

## Related Entries
- [[llmwiki-open-source]]
- [[llm-wiki-ecosystem]]
- [[pinecone-nexus]]
- [[karpathy-deep-dive-llms]]
- [[github-copilot-cli]]

---
<!-- RU -->

## Краткое описание
Паттерн, предложенный Андреем Карпатым: LLM-агент инкрементально строит и поддерживает постоянную структурированную вики из сырых источников — вместо того чтобы заново извлекать знания при каждом запросе (как в RAG).

## Ключевые идеи
- **Компиляция вместо поиска:** Сырые документы — это «исходный код»; вики — скомпилированный «бинарник». LLM синтезирует источники один раз и поддерживает вики актуальной — знания накапливаются, а не деривируются заново на каждый запрос.
- **Трёхуровневая архитектура:** (1) Сырые источники — неизменяемая база истины; (2) Вики — markdown-файлы, которыми владеет LLM; (3) Схема — файл CLAUDE.md/AGENTS.md, превращающий агента в дисциплинированного редактора вики.
- **Три операции:** *Ingest* (новый источник → LLM читает, создаёт/обновляет 10–15 страниц), *Query* (LLM читает вики, синтезирует ответ; хорошие ответы сохраняются как новые страницы), *Lint* (периодический аудит: поиск противоречий, страниц-сирот, устаревших утверждений).
- **Навигационные файлы:** `index.md` — каталог всех страниц с описаниями; `log.md` — хронологическая история операций — вместе позволяют LLM ориентироваться без инфраструктуры векторного поиска (до ~100–500 источников).
- **LLM-вики vs. RAG:** RAG лучше для миллионов постоянно меняющихся документов и точных ссылок на фрагменты; LLM-вики лучше для ограниченных кураторских корпусов, где важен синтез по нескольким источникам.
- **Связь с Memex:** Реализует идею Мемекса Ваннивара Буша (1945) — личная, активно курируемая база знаний с ассоциативными связями — ставшую реальной благодаря тому, что LLM берут на себя рутинное обслуживание, от которого люди всегда отказываются.

## Подробнее
Карпатый опубликовал идею 2 апреля 2026 года в виде GitHub Gist под названием `llm-wiki.md` — «файла-идеи», предназначенного для вставки в любой LLM-агент, который затем конкретизирует паттерн под конкретный домен.

В основе — аналогия с компиляцией из разработки ПО: вы не перезапускаете исходный код при каждом вызове программы — вы компилируете его однажды в бинарник. Аналогично, не нужно перечитывать сырые документы при каждом запросе к LLM; их компилируют один раз в структурированную вики и запрашивают уже её. Вики — это постоянный и накапливающийся артефакт: перекрёстные ссылки уже построены, противоречия уже обнаружены, и каждый новый источник обогащает всю систему.

Ключевой риск паттерна: галлюцинации могут «запечься» в страницах вики как «факты» и распространиться через перекрёстные ссылки. В чистом RAG галлюцинация ограничена одним ответом; в LLM-вики она может распространяться. Поэтому операция Lint является обязательной, а периодическая ручная сверка со страницами против сырых источников настоятельно рекомендуется.

В собственной реализации Карпатого: Obsidian — это просмотрщик (IDE), LLM-агент — программист, вики — кодовая база. Роль человека смещается от организации и хранения к курированию источников и формулировке более глубоких вопросов.

## Примечательные цитаты
> «Скучная часть ведения базы знаний — не чтение и не мышление, а рутина. Люди бросают вики, потому что бремя обслуживания растёт быстрее ценности. LLM не скучают, не забывают обновить перекрёстную ссылку и могут затронуть 15 файлов за один проход.» — Андрей Карпаты

> «Obsidian — это IDE; LLM — программист; вики — кодовая база.» — Андрей Карпаты

## Связанные записи
- [[llmwiki-open-source]]
- [[github-copilot-cli]]
