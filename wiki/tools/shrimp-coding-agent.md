---
title: "Shrimp: Coding Agent for Ollama with Streaming TUI"
title_ru: "Shrimp: кодинговый агент для Ollama со стриминговым TUI"
category: tools
tags: [ollama, coding-agent, tui, local-llm, tree-sitter, streaming]
aliases: [shrimp agent, shrimp ollama]
confidence: medium
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://www.reddit.com/r/ollama/comments/1tyih7j/
---

## Summary

Shrimp is an open-source coding agent built for Ollama featuring a streaming TUI with syntax highlighting, tree-sitter repo indexing, and a full tool suite (read/write/patch/bash/search/symbol lookup). Supports both Ollama and LM Studio backends.

## Key Ideas

- **Streaming TUI with syntax highlighting:** Real-time display of model output with proper code formatting, not raw terminal text
- **Tree-sitter repo indexing:** Parses the entire codebase into an AST-based index for fast symbol lookup and structural navigation
- **Full tool suite:** read, write, patch, bash, search, and symbol lookup — covering the standard coding agent toolkit
- **Headless mode:** Can run without the TUI for automation and scripting scenarios
- **Undo support:** Built-in undo mechanism for reverting agent changes
- **Model picker:** Interactive model selection from available Ollama/LM Studio models
- **Dual backend:** Works with both Ollama and LM Studio, giving flexibility in local inference setup

## Details

Shrimp fills the gap between raw Ollama CLI usage and full cloud-based coding agents. The tree-sitter indexing is notable — it gives the agent structural awareness of the codebase (function signatures, class hierarchies, import graphs) without sending entire files to the model. This is particularly valuable for local LLMs with smaller context windows.

The tool represents a growing ecosystem of local-first coding agents. Where cloud agents (Claude Code, Copilot CLI) optimize for frontier models with large context, tools like Shrimp optimize for constrained local models by being smarter about context assembly.

Tier 3 community tool (single Reddit post, repo URL truncated). The feature set is concrete and verifiable from the description.

## Related Entries

- [[product-ollama]] ([Ollama Cloud](../tools/product-ollama.md))
- [[freebuff]] ([freebuff: Free Coding Agent with Top Open Models](../tools/freebuff.md))
- [[choose-llm-api-self-host-hybrid]] ([How to Choose an LLM for Your AI Agent: API, Self-Host, or Hybrid](../tips/choose-llm-api-self-host-hybrid.md))

---
<!-- RU -->

## Краткое описание

Shrimp — агент кодирования с открытым исходным кодом для Ollama со стриминговым TUI-интерфейсом, подсветкой синтаксиса, индексированием репозитория через tree-sitter и полным набором инструментов (чтение/запись/патч/bash/поиск/поиск символов). Поддерживает Ollama и LM Studio.

## Ключевые идеи

- **Стриминговый TUI с подсветкой синтаксиса:** Отображение вывода модели в реальном времени с форматированием кода
- **Индексирование через tree-sitter:** Парсинг кодовой базы в AST-индекс для быстрого поиска символов и навигации
- **Полный набор инструментов:** read, write, patch, bash, search, symbol lookup
- **Безголовый режим:** Запуск без TUI для автоматизации и скриптинга
- **Поддержка отмены:** Встроенный механизм отката изменений агента
- **Выбор модели:** Интерактивный выбор из доступных моделей Ollama/LM Studio
- **Двойной бэкенд:** Работает с Ollama и LM Studio

## Подробнее

Shrimp заполняет нишу между базовым использованием Ollama CLI и облачными агентами. Индексирование через tree-sitter примечательно: даёт агенту структурное понимание кодовой базы без отправки целых файлов модели — особенно ценно для локальных LLM с ограниченным контекстным окном. Представляет растущую экосистему локальных агентов кодирования.

## Связанные записи

- [[product-ollama]] ([Ollama Cloud](../tools/product-ollama.md))
- [[freebuff]] ([freebuff: Free Coding Agent with Top Open Models](../tools/freebuff.md))
- [[choose-llm-api-self-host-hybrid]] ([How to Choose an LLM for Your AI Agent: API, Self-Host, or Hybrid](../tips/choose-llm-api-self-host-hybrid.md))
