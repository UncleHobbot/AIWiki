---
title: "MathWiki Improvement Plan: Automating a Hand-Crafted Math Knowledge Base"
title_ru: "План улучшения MathWiki: автоматизация рукотворной математической базы знаний"
category: tips
tags: [mathwiki, obsidian, math, knowledge-base, automation, claude-code, grobid, latex, zettelkasten, atomic-notes]
updated: 2026-05-16
sources:
  - https://github.com/Yaro2709/MathWiki
  - https://arxiv.org/abs/2505.13406
  - https://arxiv.org/abs/2404.10774
  - https://grobid.readthedocs.io/en/latest/Introduction/
---

## Summary
`Yaro2709/MathWiki` is a rigorous hand-authored Obsidian vault with 730+ atomic mathematical statements (definitions, theorems, axioms, lemmas) in Russian, structured as a dependency graph via `[[wiki links]]` in `Использует:` fields — but with zero automation, zero LLM integration, and no publishing pipeline. This entry outlines a concrete plan for layering Claude Code agentic automation on top of the existing structure without disrupting what already works.

## Key Ideas
- **The existing structure is sound — don't break it:** The Obsidian Admonition callout format (`[!definition]`, `[!theorem]`, `[!proof]`) with `[!info]` metadata headers is a well-designed atomic note schema. Any automation must preserve this format exactly.
- **No YAML front matter — parse callouts instead:** MathWiki uses no YAML front matter. Metadata (tags, prerequisites, relationships) lives inside `[!info]` callout blocks. Scripts must parse these, not YAML.
- **The dependency graph already exists:** The `Использует:` field in every atomic note is a hand-built prerequisite graph — 730+ nodes with edges. This is the most valuable asset in the vault; automating traversal of this graph unlocks dependency-aware search and learning paths.
- **Phase 1 — automation scripts:** Index builder, link validator, proof-coverage checker, flashcard generator. All read-only or additive; no modification of existing note content.
- **Phase 2 — LLM-assisted content:** Semi-automated generation of missing proof sketches, missing `Смыслы` (geometric/physical meaning) sections, and English summaries for sharing.
- **Phase 3 — paper ingestion pipeline:** GROBID-based ingestion of Russian math textbooks (many available as PDF) and arXiv papers, creating new atomic notes from extracted theorems. Auto-linking new notes to the existing dependency graph.
- **Quartz for publishing:** The vault is Obsidian-native with no web presence. Quartz 4 (quartz.jzhao.cc) converts an Obsidian vault to a static site with KaTeX rendering, graph view, and full-text search — deployable to GitHub Pages in one command.
- **Critical gap — proof coverage:** Most theorem entries have `Ссылки: *-*` (no proof). Generating proof sketches via LLM with MiniCheck verification is the highest-value content addition.

## Details

### What MathWiki Currently Has

Vault structure (September 2025 snapshot): 820 markdown files total — 430 definitions, 171 theorems, 98 axioms, 5 lemmas, 8 concepts, 4 algorithms, 6 examples. Topics: Set Theory, General Algebra, Mathematical Analysis (14 chapters), Topology. Three note types: **atomic** (one claim per file, with `[!info]` + typed callout), **linear/chapter** (textbook-style surveys embedding atomic content), **schema templates** (reference documents, not parsed). Obsidian community plugins: Admonition (custom callouts), metadata-extractor, graph-analysis, obsidian-enhancing-export (Pandoc+LaTeX PDF pipeline).

**What's missing:** no index file, no proof coverage for most theorems, no publishing pipeline, no automation, no English content, no AI integration, plugin JS bundles committed to git (bloat), `tags.json` goes stale without manual re-runs.

### Atomic Note Format (must preserve exactly)

```markdown
> [!info]
> Тэги: #Определение #Общая_алгебра 
> 
> Использует: [[Концепция множества]], [[Концепция функции]]
> Примеры: *-*
> Типы: *-*
> Свойства: *-*
> Конструкции: *-*
> Эквивалентности: *-*
> Обобщения: [[Определение алгебраической операции]]

> [!definition]+ Название определения
> Mathematical statement with $inline LaTeX$ and display math:
> $$formula$$
```

Any automation script must parse this format and produce output in this format. Adding YAML front matter would be a separate, optional layer that does not touch existing callout blocks.

### Phase 1: Non-Destructive Automation (implement first)

**1a. Index generator** (`scripts/build_index.py`)
Parse all atomic notes, extract: slug, type (definition/theorem/axiom/lemma), tags, `Использует` links. Output: `index.md` grouped by type and topic. Also output `graph.json` mapping slug → [prerequisite slugs] for graph traversal.

**1b. Link validator** (`scripts/validate_links.py`)
Parse all `[[wiki links]]` across the vault, check that target files exist. Report broken links. MathWiki's Obsidian graph view does this visually; a script enables CI checks via GitHub Actions.

**1c. Proof coverage report** (`scripts/proof_coverage.py`)
For each theorem note, check whether `[!proof]` callout exists or `Ссылки:` points to a non-`*-*` target. Output: list of theorems with missing proofs, sorted by how many other notes depend on them (via the reverse dependency graph — highest-value proofs to write first).

**1d. Flashcard generator** (`scripts/gen_flashcards.py`)
For each definition note: generate `Q: What is [term]? A: [statement]`. For each theorem: generate `Q: State [theorem name]. A: [statement]`. Output as Anki-compatible `.apkg` via `genanki`, or as `obsidian-spaced-repetition` inline cards appended to each note's bottom (non-destructively, inside a `%% SR %%` comment block).

**1e. Tags regenerator hook**
The `metadata-extractor` plugin generates `tags.json` manually. Add a `Stop` hook in `.claude/settings.json` that runs `python scripts/regen_tags.py` to keep it current.

### Phase 2: LLM-Assisted Content

**2a. Proof sketch generation**
For each theorem with missing proof (identified by Phase 1c), query Claude with:
- The theorem statement (from the `[!theorem]` callout)
- Its prerequisites (resolved from `Использует:` via the dependency graph)
- The source textbook passage (if available via GROBID-processed PDF)

Output: a `[!proof]-` collapsible callout in the same file. Run MiniCheck against the source to score confidence. Tag low-confidence proofs with a `#proof-needs-review` tag in the `[!info]` block.

**2b. Geometric/Physical meaning generation**
The `Cмыслы/` folder exists but is underpopulated. For definitions and theorems with visual interpretability (limits, continuity, derivatives, compactness), generate a `[!geomean]` callout with an intuitive geometric description and optionally a TikZ source for a diagram.

**2c. English summary layer (for sharing)**
Without modifying existing notes, generate a parallel `wiki-en/<slug>.md` file for each atomic note containing: English title, English summary sentence, LaTeX statement (same), English key ideas. This enables the Karpathy LLM Wiki bilingual pattern without disrupting the Russian vault.

### Phase 3: Paper Ingestion Pipeline

**3a. Russian textbook ingestion**
The vault currently cites: Письменный (Конспект лекций по высшей математике), Выгодский (Справочник по высшей математике), Зорич (Математический анализ) and others. Most exist as PDFs. Process via GROBID to extract chapter structure + theorem/definition environments. Use AutoMathKG's LaTeX regex pipeline for theorem extraction. Queue extracted claims as candidate atomic notes for human review before adding to vault.

**3b. arXiv paper ingestion**
Install `arxiv-mcp-server` globally: `claude mcp add arxiv -s user -- npx -y arxiv-mcp-server`. During a Claude Code session, call `search_papers` for topics in the vault (spectral theory, measure theory, functional analysis) to discover relevant preprints. Process via the standard wiki pipeline with math-typed atomic note output.

**3c. Dependency auto-linking**
After generating a new atomic note, embed the vault's `graph.json` as context and ask Claude: "Which existing notes in this vault does this new definition/theorem depend on? Which existing notes cite or use this claim?" Auto-populate `Использует:` and `Конструкции:` fields.

### Phase 4: Publishing with Quartz

Quartz 4 (quartz.jzhao.cc) is the recommended static site generator for Obsidian vaults:
- Native KaTeX math rendering (same LaTeX as Obsidian)
- Admonition callout rendering (matches MathWiki's custom callout types via CSS)
- Interactive graph view in the browser
- Full-text search (Flexsearch)
- GitHub Pages deployment: `npx quartz sync` pushes to `gh-pages` branch

Config needed: register custom callout types (`definition`, `theorem`, `axiom`, `lemma`, `proof`, `geomean`, `phymean`) in `quartz.config.ts`; import the existing `custom_callouts_math.css` snippet. The result: a browsable, searchable, graph-navigable math wiki accessible without Obsidian.

### CLAUDE.md to Add to MathWiki

```markdown
## Entry Format
- One mathematical claim per file (atomic notes)
- Always use [!info] header + typed callout ([!definition], [!theorem], [!lemma], [!proof])
- Использует: field must list ALL prerequisites as [[wikilinks]]
- Proof callouts are collapsible: [!proof]-
- Never modify existing callout structure when adding content — only append

## Automation
- scripts/build_index.py — regenerate index.md
- scripts/validate_links.py — check for broken [[links]]
- scripts/proof_coverage.py — find theorems without proofs
- Run all three after any batch of new notes
```

## Notable Quotes
> "Mathematics is a graph-like structure — not a linear textbook — and standard textbooks fail to expose all the interconnections between definitions and theorems." — MathWiki README philosophy

## Related Entries
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))
- [[yaro-mathwiki]] ([Yaro2709/MathWiki: Hand-Crafted Math Knowledge Base](../tools/yaro-mathwiki.md))
- [[automathkg]] ([AutoMathKG: Automated Mathematical Knowledge Graph](../tools/automathkg.md))

---
<!-- RU -->

## Краткое описание
`Yaro2709/MathWiki` — строгое рукотворное Obsidian-хранилище с 730+ атомарными математическими утверждениями (определения, теоремы, аксиомы, леммы) на русском языке, структурированное как граф зависимостей через `[[ссылки]]` в полях `Использует:`. При этом в нём нет автоматизации, нет интеграции с LLM и нет пайплайна публикации. Этот документ описывает конкретный план наслоения агентной автоматизации Claude Code на существующую структуру без разрушения того, что уже работает.

## Ключевые идеи
- **Существующая структура правильная — не ломать:** Формат каллаутов Obsidian Admonition (`[!definition]`, `[!theorem]`, `[!proof]`) с заголовком `[!info]` — хорошо продуманная схема атомарных записей. Любая автоматизация должна строго сохранять этот формат.
- **Нет YAML front matter — парсить каллауты:** В MathWiki нет YAML-метаданных. Метаданные (теги, пресуппозиции, связи) живут внутри блоков `[!info]`. Скрипты должны парсить именно их.
- **Граф зависимостей уже существует:** Поле `Использует:` в каждой атомарной записи — это рукотворный граф пресуппозиций: 730+ узлов с рёбрами. Это самый ценный актив хранилища; автоматизация обхода графа открывает зависимо-осведомлённый поиск и образовательные траектории.
- **Фаза 1 — скрипты автоматизации:** Построитель индекса, валидатор ссылок, инспектор покрытия доказательствами, генератор карточек для повторений. Только чтение или добавление; без изменения существующего контента.
- **Фаза 2 — контент с помощью LLM:** Полуавтоматическая генерация недостающих набросков доказательств, разделов `Смыслы` (геометрический/физический смысл) и англоязычных аннотаций для публичного доступа.
- **Фаза 3 — пайплайн загрузки статей:** Загрузка через GROBID российских учебников по математике (многие доступны в PDF) и arXiv-препринтов с созданием новых атомарных записей из извлечённых теорем.
- **Quartz для публикации:** Хранилище — только для Obsidian, веб-присутствия нет. Quartz 4 конвертирует Obsidian-хранилище в статический сайт с рендерингом KaTeX, графом связей и полнотекстовым поиском — разворачивается на GitHub Pages одной командой.
- **Критический пробел — покрытие доказательствами:** Большинство записей теорем имеют `Ссылки: *-*` (нет доказательства). Генерация набросков доказательств через LLM с верификацией MiniCheck — наиболее ценное дополнение контента.

## Подробнее

### Что уже есть в MathWiki

820 markdown-файлов: 430 определений, 171 теорема, 98 аксиом, 5 лемм, 8 концепций, 4 алгоритма, 6 примеров. Темы: теория множеств, общая алгебра, математический анализ (14 глав), топология. Три типа записей: **атомарные** (одно утверждение + `[!info]` + типизированный каллаут), **линейные/главные** (обзоры в стиле учебника), **шаблоны схем** (справочные документы).

**Чего не хватает:** нет индексного файла, нет покрытия доказательствами для большинства теорем, нет пайплайна публикации, нет автоматизации, нет английского контента, JS-бандлы плагинов закоммичены в репозиторий, `tags.json` устаревает без ручного перезапуска.

### Фаза 1: Неразрушающая автоматизация

- **Построитель индекса:** парсинг атомарных записей → `index.md` по типу и теме + `graph.json` с картой пресуппозиций.
- **Валидатор ссылок:** парсинг всех `[[wikilinks]]` → список битых ссылок → запуск в GitHub Actions.
- **Инспектор доказательств:** для каждой теоремы проверяем наличие `[!proof]` или непустое `Ссылки:` → список теорем без доказательства, отсортированный по количеству зависящих от них записей (наиболее ценные доказательства — в первую очередь).
- **Генератор карточек для повторений:** из определений → `Q: Что такое [термин]? A: [утверждение]`; из теорем → `Q: Сформулируйте [теорему]. A: [утверждение]`. Экспорт в Anki (`.apkg` через `genanki`) или как встроенные SR-карточки в конце каждой записи.

### Фаза 2: Контент с помощью LLM

**Наброски доказательств:** для каждой теоремы без доказательства — запрос Claude с утверждением теоремы, её пресуппозициями (из графа `Использует:`) и, при наличии, отрывком из учебника (через GROBID). Вывод: каллаут `[!proof]-` в том же файле. Верификация через MiniCheck; низкая уверенность → тег `#proof-needs-review`.

**Геометрический/физический смысл:** папка `Смыслы/` существует, но мало заполнена. Для наглядно интерпретируемых понятий (предел, непрерывность, производная, компактность) — каллаут `[!geomean]` с интуитивным описанием и опционально TikZ-исходником для диаграммы.

**Английский слой:** без изменения существующих записей создать параллельные файлы `wiki-en/<slug>.md` с английским заголовком, аннотацией и теми же LaTeX-формулами — для публичного доступа и интеграции с паттерном LLM Wiki.

### Фаза 3: Пайплайн загрузки статей

Обработка PDF российских учебников (Письменный, Выгодский, Зорич) через GROBID → извлечение LaTeX-окружений regex-методом → LLM-обогащение атрибутов → кандидаты на новые атомарные записи для проверки человеком. Параллельно — поиск релевантных препринтов arXiv через `arxiv-mcp-server` с автоматической перелинковкой к существующему графу зависимостей.

### Фаза 4: Публикация через Quartz

Quartz 4 конвертирует Obsidian-хранилище в статический сайт: нативный рендеринг KaTeX, поддержка каллаутов Admonition, интерактивный граф, полнотекстовый поиск (Flexsearch), деплой на GitHub Pages командой `npx quartz sync`. Необходимо зарегистрировать кастомные типы каллаутов (`definition`, `theorem`, `axiom`, `lemma`, `proof`, `geomean`, `phymean`) в `quartz.config.ts` и импортировать существующий `custom_callouts_math.css`.

## Примечательные цитаты
> «Математика — это граф, а не линейный учебник: стандартные учебники не показывают все связи между определениями и теоремами.» — философия MathWiki README

## Связанные записи
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))
- [[yaro-mathwiki]] ([Yaro2709/MathWiki: Hand-Crafted Math Knowledge Base](../tools/yaro-mathwiki.md))
- [[automathkg]] ([AutoMathKG: Automated Mathematical Knowledge Graph](../tools/automathkg.md))
