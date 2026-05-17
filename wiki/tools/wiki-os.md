---
title: "Wiki OS: Browser UI for LLM Wiki"
title_ru: "Wiki OS: браузерный UI для LLM-вики"
category: tools
tags: [llm-wiki, ui, browser, open-source, obsidian-alternative, knowledge-graph]
updated: 2026-05-15
sources:
  - https://www.youtube.com/watch?v=gexxq4VbPfs
---

## Summary
Wiki OS is a free, open-source browser-based interface for LLM Wiki vaults that displays article graphs, vault statistics, and agent activity — addressing the missing UI layer that Obsidian partially fills but with a web-accessible alternative.

## Key Ideas
- **The missing UI layer:** LLM agents can navigate and read wiki articles, but without a visual interface you can't see what they're doing or understand the knowledge structure. Wiki OS solves this.
- **Knowledge graph visualization:** Shows how articles are connected to each other in a web/graph view, making the compounding structure of the wiki visible.
- **Vault statistics:** Displays metrics about your wiki — number of pages, connections, growth over time.
- **Browser-based:** Runs in the browser, no Obsidian installation required — alternative for those who want a web UI over a desktop app.
- **Single-command install:** Install via a simple script; point at your vault directory.
- **Free and open-source:** Created by Ansub Khan (@Ansub Khan on YouTube).

## Details
Created in April 2026 by Ansub Khan as a response to the LLM Wiki explosion following Karpathy's gist. The core argument is that the existing viewer options (primarily Obsidian) work well but require installation, are desktop-only, and don't show agent activity in a purpose-built way.

Wiki OS provides a purpose-built interface that makes the LLM Wiki pattern more accessible and observable — you can watch pages being created, see the graph grow, and get statistics about your knowledge base without leaving the browser.

The tool addresses a real gap: once your wiki has hundreds of pages, understanding its structure through a file browser or even Obsidian's graph view can become unwieldy. A statistics dashboard and filterable graph are more practical at scale.

## Video Notes
- Ansub Khan's video "I Made Karpathy's LLM Wiki Actually Usable" (Apr 13, 2026)
- Demo shows: graph of article connections, vault stats panel
- Install: paste a single command in terminal, point at your vault directory

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))

---
<!-- RU -->

## Краткое описание
Wiki OS — бесплатный браузерный интерфейс с открытым исходным кодом для вики-хранилищ LLM, отображающий граф статей, статистику хранилища и активность агентов — восполняет отсутствующий UI-слой, который Obsidian закрывает лишь частично.

## Ключевые идеи
- **Отсутствующий UI-слой:** LLM-агенты могут читать и редактировать вики-статьи, но без визуального интерфейса непонятно, что они делают и какова структура знаний. Wiki OS решает это.
- **Визуализация графа знаний:** Показывает связи между статьями в виде сети/графа, делая компаундирующую структуру вики видимой.
- **Статистика хранилища:** Отображает метрики — количество страниц, связей, рост со временем.
- **На основе браузера:** Работает в браузере, не требует установки Obsidian — альтернатива для тех, кто предпочитает веб-интерфейс.
- **Установка одной командой:** Установите через простой скрипт; укажите на папку с хранилищем.
- **Бесплатно и открытый исходный код:** Создан Ansub Khan.

## Подробнее
Создан в апреле 2026 года Ansub Khan в ответ на взрывной интерес к LLM-вики после публикации гиста Карпатого. Основной аргумент: существующие просмотрщики (прежде всего Obsidian) работают хорошо, но требуют установки, являются только десктопными и не показывают активность агентов в специализированном виде.

Wiki OS предоставляет целевой интерфейс, делающий паттерн LLM-вики более доступным и наблюдаемым — можно наблюдать за созданием страниц, ростом графа и получать статистику о базе знаний прямо в браузере.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
