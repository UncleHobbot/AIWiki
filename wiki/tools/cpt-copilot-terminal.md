---
title: "cpt: Inline Copilot Chat for Any Terminal"
title_ru: "cpt: встроенный чат Copilot для любого терминала"
category: tools
tags: [github-copilot, terminal, cli, inline-chat, productivity]
updated: 2026-05-15
sources:
  - https://burkeholland.github.io/cpt
  - https://x.com/burkeholland/status/2048230145857589719
---

## Summary
`cpt` adds an inline `ctrl+k` chat shortcut to any terminal, letting you ask GitHub Copilot questions and get shell command suggestions without leaving your current terminal session.

## Key Ideas
- **`ctrl+k` to invoke:** Press the shortcut anywhere in the terminal to open an inline Copilot chat panel — no IDE or browser tab needed.
- **Natural language to commands:** Describe what you want in plain English; Copilot suggests the exact shell command. Example: "what's using port 3000? kill it" → `lsof -ti :3000 | xargs kill -9`.
- **Model selectable:** The interface shows the active model (e.g., `gpt-5.4-mini`) and lets you switch.
- **Works in any terminal:** Not tied to VS Code or a specific shell — runs as an overlay in your existing terminal environment.
- **Created by Burke Holland** (@burkeholland, GitHub) — a lightweight companion to the heavier Copilot CLI for quick ad-hoc queries.

## Details
`cpt` is designed for the friction between "I know roughly what command I need" and "I need to look it up." Rather than switching to a browser or IDE chat, `ctrl+k` opens a minimal inline panel that accepts natural language and outputs a ready-to-run command.

It complements Copilot CLI (which handles full planning and multi-step agentic tasks) by handling quick one-shot lookups — find a process, kill a port, check disk usage, format a file — without the ceremony of starting a full Copilot session.

Install/access from the project page at `burkeholland.github.io/cpt`.

## Related Entries
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[github-copilot-app]] ([GitHub Copilot App: Desktop Agent for Parallel Development](../news/github-copilot-app.md))

---
<!-- RU -->

## Краткое описание
`cpt` добавляет встроенный ярлык `ctrl+k` для чата с Copilot в любом терминале — позволяет задавать вопросы и получать предложения команд, не покидая текущую сессию.

## Ключевые идеи
- **`ctrl+k` для вызова:** Нажмите ярлык в любом месте терминала, чтобы открыть встроенную панель чата Copilot — без IDE или браузера.
- **Естественный язык → команды:** Опишите задачу на обычном языке, Copilot предложит точную команду оболочки. Пример: «что использует порт 3000? убей это» → `lsof -ti :3000 | xargs kill -9`.
- **Выбор модели:** Интерфейс показывает активную модель (например, `gpt-5.4-mini`) с возможностью переключения.
- **Работает в любом терминале:** Не привязан к VS Code или конкретной оболочке — запускается как наложение в существующем терминале.
- **Создан Burke Holland** (@burkeholland, GitHub) — лёгкий компаньон к более тяжёлому Copilot CLI для быстрых разовых запросов.

## Связанные записи
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[github-copilot-app]] ([GitHub Copilot App: Desktop Agent for Parallel Development](../news/github-copilot-app.md))
