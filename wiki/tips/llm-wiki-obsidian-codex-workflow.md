---
title: "LLM Wiki: Obsidian + Codex Second Brain Workflow"
title_ru: "LLM-вики: рабочий процесс «второй мозг» на Obsidian + Codex"
category: tips
tags: [llm-wiki, obsidian, codex, openai, second-brain, productivity, knowledge-management, karpathy, automation, cron]
aliases: [Obsidian Codex workflow, Matt Wolfe second brain, second brain OpenAI, personal wiki Codex]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=z_oAi9xdDQs
---

## Summary
A practical workflow combining Obsidian (free markdown-file organizer) and OpenAI Codex (a coding IDE that acts as the LLM agent) to build a personal second brain that automatically cross-links saved content, runs a proactive morning brief, and compounds knowledge over time — inspired by Karpathy's LLM Wiki tweet with 20.8M views.

## Key Ideas
- **Obsidian is a free markdown file organizer** — all notes are plain `.md` files on your local disk, not in any cloud; Codex simply points at the same folder to gain read/write access.
- **The Obsidian Web Clipper browser extension** captures any article or YouTube transcript in one click, dropping it as a markdown file into the `raw/` inbox folder.
- **AGENTS.md is the "secret prompt"** — a file inside the vault that defines how Codex handles each ingest, query, and cross-link operation; you do not need to repeat instructions every session.
- **Codex automations run on a cron schedule** — Codex can be set to process `raw/` at 12:50 AM nightly, so the wiki grows while you sleep with zero manual effort.
- **Proactive morning brief:** a Codex scheduled automation sends a Slack message every morning at 9 AM with recommendations drawn from recently saved wiki content — shifting AI from reactive to proactive.
- **Networking CRM use case:** meeting notes saved to the wiki enable instant recall of conversations weeks or months later ("you met this person here, you discussed X, their dog is named Y").

## Details
The workflow was demonstrated by Matt Wolfe (FutureTools) on the Marketing Against the Grain podcast in May 2026. The system has two main components:

**Obsidian** stores everything as local markdown files. Key folders: `raw/` (unprocessed inbox), `wiki/topics/`, `wiki/entities/`, `sources/` (original content), `journal/` (daily brain dump). The root `index.md` is a generated table of contents of all wiki pages.

**Codex** (OpenAI's coding IDE) is pointed at the same folder. It reads `AGENTS.md` to understand the ingest schema, then processes files on demand or automatically. Codex is described as "ChatGPT's version of Claude Code" — a coding agent with a concise, action-oriented default style rather than ChatGPT's longer conversational style.

**The AGENTS.md file** defines sub-prompts for each operation: *Ingest* (read raw source, deduplicate by URL, create/update topic pages, create/update entity overview pages); *Query* (search wiki, synthesize answer, file good answers back as new wiki pages); *Lint* (find orphans, contradictions, stale pages).

**Practical use cases described:**
1. *Content research:* YouTube transcripts + articles clipped all day, processed at night → wakes up to a fully cross-linked wiki.
2. *Morning brief:* Codex reads recently saved content and sends a Slack message with business recommendations every morning at 9 AM.
3. *Competitive intelligence:* An agent monitors competitor site sitemaps for new pages (workaround for sites without RSS), alerting almost instantly when a new blog post appears on Anthropic, OpenAI, Google, or DeepMind's sites.
4. *Networking CRM:* Conference contacts saved with context (name, location, conversation topics) enable recall months later.
5. *Journaling:* Daily brain dumps filed into Codex's journal cross-reference the wiki, surfacing relevant saved content that contextualizes the journal entry.

**Integrations available in Codex** (as of May 2026): GitHub, Slack, Notion, Gmail, Google Calendar, Google Drive, Chrome (browser control for web automation — new in May 2026).

**Notable quote:**
> "AI is still in single-player mode — but this is going to be transformative for teams as this technology evolves." — Kipp Bodnar

## Video Notes
- [2:00] The Karpathy tweet that started the LLM wiki movement — 20.8M views
- [5:00] Obsidian explained: just a free markdown file organizer, all files local
- [8:00] Obsidian Web Clipper: one-click YouTube transcript and article capture
- [12:00] AGENTS.md: the "secret prompt" that defines all ingest behavior
- [15:00] Codex automations: scheduling nightly processing of raw/ folder
- [18:00] Demo: querying wiki about AEO strategy — concise answer with source citations
- [22:00] Morning brief automation: Slack message at 9 AM with wiki-based recommendations
- [26:00] Competitive intelligence: sitemap monitoring as RSS alternative
- [30:00] Networking CRM use case: recall conversations from 6 months ago
- [35:00] Journaling workflow: daily brain dump cross-referenced with wiki knowledge

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-obsidian-build-guide]] ([Building an LLM Wiki in Obsidian: Step-by-Step Guide](../tips/llm-wiki-obsidian-build-guide.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem](../tools/llm-wiki-ecosystem.md))

---
<!-- RU -->

## Краткое описание
Практический рабочий процесс на базе Obsidian и OpenAI Codex для построения персонального «второго мозга» — автоматическое перекрёстное связывание сохранённого контента, утренний брифинг с рекомендациями и накопление знаний без ручного труда, вдохновлённое твитом Karpathy с 20,8 млн просмотров.

## Ключевые идеи
- **Obsidian — бесплатный органайзер markdown-файлов** — все заметки хранятся в виде обычных `.md`-файлов на вашем диске; Codex просто указывает на ту же папку для получения доступа.
- **Расширение Obsidian Web Clipper** захватывает статьи и транскрипты YouTube одним кликом, помещая их в папку `raw/`.
- **AGENTS.md — «секретный prompt»**: файл внутри хранилища, определяющий, как Codex обрабатывает каждую операцию ingest, query и cross-link.
- **Автоматизация по расписанию (cron):** Codex можно настроить на обработку `raw/` в 00:50 каждую ночь — вики растёт, пока вы спите.
- **Проактивный утренний брифинг:** автоматизация отправляет сообщение в Slack каждое утро в 9:00 с рекомендациями на основе недавно сохранённого контента.
- **CRM для нетворкинга:** заметки о встречах позволяют мгновенно вспомнить разговоры, состоявшиеся месяцы назад.

## Подробнее
Рабочий процесс продемонстрирован Мэттом Вулфом (FutureTools) в подкасте Marketing Against the Grain в мае 2026 года.

**Obsidian** хранит всё в виде локальных markdown-файлов. Ключевые папки: `raw/` (необработанные входящие), `wiki/topics/`, `wiki/entities/`, `sources/`, `journal/`. Корневой `index.md` — это автогенерируемое оглавление всех страниц вики.

**Codex** (IDE OpenAI) указывается на ту же папку. Он читает `AGENTS.md`, чтобы понять схему ingest, и обрабатывает файлы по запросу или автоматически. Codex — это «версия Claude Code от ChatGPT»: лаконичный, ориентированный на действие стиль.

**Файл AGENTS.md** определяет подпромпты для каждой операции: ingest (читать источник, дедублировать, создавать/обновлять страницы тем и сущностей), query (искать по вики, синтезировать ответ, сохранять хорошие ответы как новые страницы), lint (искать изолированные страницы, противоречия, устаревший контент).

**Практические сценарии:** транскрипты YouTube + статьи весь день → обработка ночью; утренние рекомендации в Slack; мониторинг конкурентов через sitemap вместо RSS; журнал с перекрёстными ссылками на вики.

## Заметки по видео
- [2:00] Твит Karpathy, запустивший движение LLM Wiki — 20,8 млн просмотров
- [5:00] Obsidian: бесплатный органайзер markdown-файлов, все файлы локально
- [8:00] Obsidian Web Clipper: захват транскриптов YouTube и статей одним кликом
- [12:00] AGENTS.md: «секретный prompt», определяющий всё поведение при ingest
- [15:00] Автоматизация Codex: ночная обработка папки raw/ по расписанию
- [18:00] Демо: запрос к вики о стратегии AEO — лаконичный ответ с цитатами источников
- [22:00] Утренний брифинг: сообщение в Slack в 9:00 с рекомендациями
- [26:00] Конкурентная разведка: мониторинг sitemap вместо RSS
- [30:00] CRM для нетворкинга: вспомнить разговор 6-месячной давности

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-obsidian-build-guide]] ([Building an LLM Wiki in Obsidian: Step-by-Step Guide](../tips/llm-wiki-obsidian-build-guide.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem](../tools/llm-wiki-ecosystem.md))
