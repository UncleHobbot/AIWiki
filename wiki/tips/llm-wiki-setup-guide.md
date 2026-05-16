---
title: "LLM Wiki: Practical Setup Guide"
title_ru: "LLM-вики: практическое руководство по настройке"
category: tips
tags: [llm-wiki, obsidian, claude-code, setup, knowledge-base, karpathy]
updated: 2026-05-15
sources:
  - https://www.youtube.com/watch?v=iXd0t60YmMw
  - https://www.youtube.com/watch?v=4SB3T1reCHw
  - https://www.youtube.com/watch?v=FR9USL0yj3I
  - https://www.youtube.com/watch?v=zVEb19AwkqM
  - https://www.youtube.com/watch?v=3sx3viLjR8Q
  - https://www.youtube.com/watch?v=VjxzsCurQ-0
---

## Summary
Step-by-step guide to building Karpathy's LLM Wiki from scratch: what tools you need, how to structure folders, how to write a schema, and how to ingest sources and run maintenance.

## Key Ideas
- **Start narrow:** Pick a single well-defined topic (AI research, trip planning, nutrition). 5–10 initial sources is enough; add more as you go.
- **Folder structure:** Three folders in an Obsidian vault — `raw/` (immutable sources), `wiki/` (LLM-written pages), `templates/` (optional). Schema file `claude.md` goes in the vault root — if it's moved to a subfolder the agent loses its instructions.
- **Schema is the key file:** The `claude.md` (or `AGENTS.md` for Codex) tells the LLM how to structure pages, how to link concepts, and what to do when ingesting a source. Only one line needs customizing per topic: the purpose/domain statement.
- **Ingest command:** `"I just added a new source to the raw folder. Please read it and update the Wiki."` — works for both markdown clips and PDFs (Claude Code reads PDFs natively).
- **Lint command:** `"Please lint the wiki."` — LLM checks for broken links, orphan pages, missing cross-references, and stale claims. Run after every batch of ingests.
- **Obsidian Web Clipper:** Browser extension that converts web articles to markdown. Install it → clip an article → save to `raw/` → ingest. Eliminates copy-paste friction entirely.
- **Graph view:** Obsidian's graph view shows the growing knowledge network visually — nodes are pages, edges are LLM-added links. One document becomes a connected cluster within minutes.
- **Scale limit:** Works best at personal scale up to ~100–200 articles without embedding infrastructure. Beyond that, add [qmd](https://github.com/qmd-lab/qmd) for hybrid BM25/vector search.

## Details
**Minimum viable setup:**
1. Install Obsidian (free) and create a new vault at your chosen folder.
2. Create three subfolders: `raw/`, `wiki/`, `templates/`.
3. Paste Karpathy's gist into Claude Code and ask it to create `claude.md` tailored to your domain. Answer its clarifying questions (topic, source types, rough scale, page types wanted).
4. Drop your first source into `raw/` (markdown, PDF, or text file).
5. Run the ingest command. Claude reads the source, writes ~5–15 wiki pages, updates `index.md`, and logs the run.
6. Open Obsidian's graph view to see the knowledge structure forming.
7. Repeat: add more sources, periodically lint, and ask synthesis questions.

**Key agents to use:** Claude Code (file read/write), OpenAI Codex, Cursor, or any agent that reads and writes files on your machine. Obsidian itself is the viewer — it is not an AI tool.

**Good use cases:** PhD literature reviews, Japan trip planning, nutrition research, trading strategy development, competitive analysis, reading companion for books. The pattern works anywhere knowledge accumulates over weeks or months and synthesis across sources matters.

**Limitations to know upfront:**
- Garbage in, garbage out — source quality determines wiki quality
- The AI may miscategorize or miss connections, especially early on; review output before fully trusting it
- Not a real-time search tool — for breaking news use standard search, not an LLM Wiki
- Initial ingest of a large existing collection (50+ docs) can take hours

## Related Entries
- [[llm-wiki-pattern]]
- [[llmwiki-open-source]]
- [[llm-wiki-enterprise-patterns]]

---
<!-- RU -->

## Краткое описание
Пошаговое руководство по созданию LLM-вики по методу Карпатого: какие инструменты нужны, как организовать папки, написать схему и загружать источники.

## Ключевые идеи
- **Начинайте с узкой темы:** Возьмите одну хорошо определённую область (ИИ-исследования, планирование поездки, нутрициология). 5–10 начальных источников — достаточно; добавляйте больше по мере роста.
- **Структура папок:** Три папки в хранилище Obsidian — `raw/` (неизменяемые источники), `wiki/` (страницы, созданные LLM), `templates/` (опционально). Файл схемы `claude.md` кладётся в корень хранилища — если переместить его в подпапку, агент потеряет инструкции.
- **Схема — ключевой файл:** `claude.md` (или `AGENTS.md` для Codex) сообщает LLM, как структурировать страницы, как связывать концепции и что делать при загрузке источника. Под каждую тему меняется только одна строка — описание домена/цели вики.
- **Команда загрузки:** `"I just added a new source to the raw folder. Please read it and update the Wiki."` — работает как для markdown-файлов, так и для PDF (Claude Code читает PDF нативно).
- **Команда линтинга:** `"Please lint the wiki."` — LLM проверяет сломанные ссылки, страницы-сироты, отсутствующие перекрёстные ссылки и устаревшие утверждения. Запускайте после каждой пачки загрузок.
- **Obsidian Web Clipper:** Расширение браузера, конвертирующее статьи в markdown. Установите → сохраните статью → положите в `raw/` → загрузите. Полностью убирает необходимость копировать вручную.
- **Graph view:** Граф Obsidian показывает сеть знаний визуально — узлы это страницы, рёбра это ссылки, добавленные LLM. Один документ становится связанным кластером за несколько минут.
- **Предел масштаба:** Хорошо работает как личный инструмент до ~100–200 источников без эмбеддинг-инфраструктуры. Дальше добавляйте [qmd](https://github.com/qmd-lab/qmd) с гибридным BM25/vector-поиском.

## Подробнее
**Минимально рабочая конфигурация:**
1. Установите Obsidian (бесплатно) и создайте новое хранилище в выбранной папке.
2. Создайте три подпапки: `raw/`, `wiki/`, `templates/`.
3. Вставьте гист Карпатого в Claude Code и попросите создать `claude.md` под вашу область. Ответьте на уточняющие вопросы (тема, типы источников, примерный масштаб, какие типы страниц нужны).
4. Положите первый источник в `raw/` (markdown, PDF или текстовый файл).
5. Выполните команду загрузки. Claude читает источник, создаёт ~5–15 страниц вики, обновляет `index.md` и записывает лог.
6. Откройте граф Obsidian, чтобы увидеть формирующуюся структуру знаний.
7. Повторяйте: добавляйте источники, периодически запускайте lint, задавайте синтезирующие вопросы.

**Подходящие агенты:** Claude Code (чтение/запись файлов), OpenAI Codex, Cursor или любой агент, который читает и пишет файлы на вашей машине. Obsidian — это просмотрщик, а не AI-инструмент.

**Ограничения, о которых стоит знать заранее:**
- Качество вики определяется качеством источников; плохие источники → плохая вики
- ИИ может неверно классифицировать материал или пропустить связи, особенно в начале — проверяйте результат
- Инструмент не для поиска в реальном времени — для свежих новостей используйте стандартный поиск
- Первоначальная загрузка большой коллекции (50+ документов) может занять несколько часов

## Связанные записи
- [[llm-wiki-pattern]]
- [[llmwiki-open-source]]
- [[llm-wiki-enterprise-patterns]]
