---
title: "Yaro2709/MathWiki: Hand-Crafted Math Knowledge Base"
title_ru: "Yaro2709/MathWiki: рукотворная база математических знаний"
category: tools
tags: [mathwiki, obsidian, math, knowledge-base, zettelkasten, atomic-notes, russian]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://github.com/Yaro2709/MathWiki
---

## Summary
Yaro2709/MathWiki is a hand-curated Obsidian vault containing 730+ atomic mathematical statements (definitions, theorems, axioms, lemmas) written entirely in Russian and structured as a navigable dependency graph. It applies Zettelkasten principles to undergraduate-level pure mathematics across Set Theory, Algebra, Analysis, and Topology.

## Key Ideas
- 820 markdown files broken into 430 definitions, 171 theorems, 98 axioms, 5 lemmas, 8 concepts, 4 algorithms, and 6 examples — all hand-authored with no automation or LLM involvement
- Three note types: atomic (one claim per file), linear/chapter (textbook-style surveys), and systematic (tables and schemas for structural overviews)
- Dependency graph encoded via `Использует:` field inside `[!info]` callout blocks, using `[[wiki links]]` to reference prerequisites
- Obsidian Admonition callouts (`[!definition]`, `[!theorem]`, `[!proof]`, `[!info]`) replace YAML front matter for all metadata
- Structured schemas for cross-linking: definitions follow Использует/Примеры/Типы/Свойства/Конструкции/Эквивалентности/Обобщения; theorems follow Использует/Примеры/Ссылки/Эквивалентности/Обобщения
- Coverage spans Set Theory, General Algebra, 14 chapters of Mathematical Analysis, and Topology — referencing textbooks by Письменный, Выгодский, Зорич and others
- No English content, no publishing pipeline, no automated build — purely a local Obsidian vault
- Plugin JS bundles are committed to git, contributing to repository bloat

## Details
MathWiki treats mathematical knowledge as a directed graph rather than a linear narrative. Each atomic note represents a single mathematical statement — one definition, one theorem, or one axiom — stored in its own file. The `Использует:` (Uses) field inside `[!info]` callouts creates explicit prerequisite edges between notes, allowing Obsidian's graph view to reveal the true dependency structure of mathematics. This approach surfaces connections that textbooks, constrained by linear chapter ordering, necessarily obscure.

The schema for definition notes includes dedicated sections for types, properties, constructions, equivalences, and generalizations — each populated with `[[wiki links]]` to other atomic notes. Theorem notes follow a similar but distinct schema with sections for examples, references, equivalences, and generalizations. This disciplined linking creates a dense, navigable network where any concept can be reached through multiple paths, mirroring how mathematicians actually think about their subject.

Notable gaps include the absence of English content, no LLM integration for generation or verification, no automated testing of logical consistency, and no publishing pipeline beyond the GitHub repository. The vault also carries plugin JS bundles in git, which inflates repository size. Despite these limitations, MathWiki represents one of the most ambitious hand-crafted mathematical knowledge bases in a personal-wiki format and serves as a compelling reference architecture for similar projects.

## Notable Quotes
> "Mathematics is a graph-like structure — not a linear textbook — and standard textbooks fail to expose all the interconnections between definitions and theorems." — MathWiki README

## Related Entries
- [[mathwiki-improvement-plan]] ([MathWiki Improvement Plan: Automating a Hand-Crafted Math Knowledge Base](../tips/mathwiki-improvement-plan.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[automathkg]] ([AutoMathKG: Automated Mathematical Knowledge Graph](../tools/automathkg.md))

---
<!-- RU -->

## Краткое описание
Yaro2709/MathWiki — это рукотворное хранилище Obsidian с 730+ атомарными математическими утверждениями (определения, теоремы, аксиомы, леммы), полностью на русском языке, организованными в виде навигируемого графа зависимостей. Проект применяет принципы Zettelkasten к чистой математике университетского уровня.

## Ключевые идеи
- 820 markdown-файлов: 430 определений, 171 теорема, 98 аксиом, 5 лемм, 8 концептов, 4 алгоритма и 6 примеров — все написаны вручную без автоматизации или участия LLM
- Три типа заметок: атомарные (одно утверждение на файл), линейные/главные (обзоры в стиле учебника) и систематические (таблицы и схемы для структурных обзоров)
- Граф зависимостей закодирован через поле `Использует:` внутри callout-блоков `[!info]`, используя `[[wiki-ссылки]]` для указания необходимых предварительных знаний
- Admonition-callouts Obsidian (`[!definition]`, `[!theorem]`, `[!proof]`, `[!info]`) заменяют YAML front matter для всех метаданных
- Структурированные схемы перекрёстных ссылок: определения следуют схеме Использует/Примеры/Типы/Свойства/Конструкции/Эквивалентности/Обобщения; теоремы — Использует/Примеры/Ссылки/Эквивалентности/Обобщения
- Охватывает теорию множеств, общую алгебру, 14 глав математического анализа и топологию — с ссылками на учебники Письменного, Выгодского, Зорича и других
- Нет английского контента, нет конвейера публикации, нет автоматической сборки — исключительно локальное хранилище Obsidian
- JS-бандлы плагинов добавлены в git, что раздувает объём репозитория

## Подробнее
MathWiki рассматривает математические знания как ориентированный граф, а не линейное повествование. Каждая атомарная заметка представляет собой одно математическое утверждение — определение, теорему или аксиому — в отдельном файле. Поле `Использует:` внутри callout-блоков `[!info]` создаёт явные рёбра зависимостей между заметками, позволяя графовому представлению Obsidian раскрыть истинную структуру зависимостей математики. Этот подход выявляет связи, которые учебники, ограниченные линейным порядком глав, неизбежно скрывают.

Схема для заметок-определений включает специализированные разделы для типов, свойств, конструкций, эквивалентностей и обобщений — каждый заполнен `[[wiki-ссылками]]` на другие атомарные заметки. Заметки с теоремами следуют аналогичной, но отличающейся схеме с разделами для примеров, ссылок, эквивалентностей и обобщений. Такая дисциплинированная система ссылок создаёт плотную навигируемую сеть, где любой концепт достижим через множество путей, отражая то, как математики реально мыслят о своём предмете.

Заметные пробелы: отсутствие английского контента, отсутствие интеграции с LLM для генерации или верификации, отсутствие автоматической проверки логической непротиворечивости и отсутствие конвейера публикации за пределами GitHub-репозитория. В хранилище также включены JS-бандлы плагинов в git, что увеличивает размер репозитория. Несмотря на эти ограничения, MathWiki представляет одну из самых амбициозных рукотворных баз математических знаний в формате личной вики и служит убедительной референсной архитектурой для аналогичных проектов.

## Примечательные цитаты
> «Математика — это граф, а не линейный учебник: стандартные учебники не показывают все связи между определениями и теоремами.» — MathWiki README

## Связанные записи
- [[mathwiki-improvement-plan]] ([MathWiki Improvement Plan: Automating a Hand-Crafted Math Knowledge Base](../tips/mathwiki-improvement-plan.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[automathkg]] ([AutoMathKG: Automated Mathematical Knowledge Graph](../tools/automathkg.md))
