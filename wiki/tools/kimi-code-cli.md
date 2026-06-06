---
title: "Kimi Code: Moonshot AI's Terminal Coding Agent"
title_ru: "Kimi Code: терминальный кодинг-агент от Moonshot AI"
category: tools
tags: [kimi, moonshot, coding-agent, cli, terminal, mcp, subagents, hooks, acp, video-input]
aliases: [Kimi Code, kimi-code, MoonshotAI kimi-code, Kimi CLI]
confidence: high
updated: 2026-06-05
sources:
  - https://github.com/MoonshotAI/kimi-code
  - https://www.reddit.com/r/kimi/comments/1tr5sc2/kimi_code/
---

## Summary
Kimi Code is Moonshot AI's official terminal coding agent (1.9k stars, MIT licensed) — a single-binary CLI that reads and edits code, runs shell commands, searches files, and fetches web pages, with native MCP support, subagents, lifecycle hooks, and a notable video-input capability for screen recordings.

## Key Ideas
- **Single-binary, no Node.js**: one-command install (`curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash`), millisecond TUI startup — a deliberate contrast to Node-based agents like Claude Code.
- **Video input**: accepts screen recordings and demos as input — a feature most terminal coding agents lack, useful for reproducing UI bugs or explaining workflows visually.
- **Subagents for parallel work**: ships coder, explore, and plan subagents for focused parallel execution, mirroring the multi-agent direction of Claude Code's dynamic workflows.
- **MCP + plugin marketplace**: AI-native MCP configuration plus a plugin ecosystem with marketplace integration.
- **ACP editor integration**: connects to editors/IDEs via the Agent Client Protocol; lifecycle hooks enable custom automation.
- **Model-flexible**: works out of the box with Moonshot's Kimi models but can be configured for other compatible providers.

## Details
Kimi Code is Moonshot AI's answer to Claude Code and the broader terminal-agent category. The architectural choices signal a direct response to friction points in existing tools: the single-binary distribution eliminates the Node.js dependency chain that complicates Claude Code installs, and the millisecond startup targets the latency complaints common in the agentic CLI space.

The video-input capability is the most distinctive feature — feeding a screen recording of a bug or a demo of desired behavior gives the agent richer context than text alone. This positions Kimi Code well for front-end and UI work where visual reproduction matters.

The subagent design (coder/explore/plan) and lifecycle hooks indicate Moonshot is building toward the same harness-engineering patterns that Claude Code and Codex have converged on — parallel focused agents plus deterministic automation gates. Combined with Moonshot's competitive Kimi models (K2.6), Kimi Code is a credible open-source entrant in the coding-agent race.

## Related Entries
- [[kimi-2-6-vs-glm-5-1-agent-reliability]] ([Kimi 2.6 vs GLM 5.1 Agent Reliability](../models/kimi-2-6-vs-glm-5-1-agent-reliability.md))
- [[product-claude-code]] ([Claude Code](../agents/product-claude-code.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[claude-code-frameworks]] ([Claude Code Frameworks](../tools/claude-code-frameworks.md))

---
<!-- RU -->

## Краткое описание
Kimi Code — официальный терминальный кодинг-агент от Moonshot AI (1.9k звёзд, лицензия MIT): CLI в одном бинарнике, который читает и редактирует код, выполняет shell-команды, ищет файлы и загружает веб-страницы, с нативной поддержкой MCP, субагентами, lifecycle hooks и примечательной возможностью ввода видео.

## Ключевые идеи
- **Один бинарник, без Node.js**: установка одной командой (`curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash`), запуск TUI за миллисекунды — намеренный контраст с агентами на Node вроде Claude Code.
- **Ввод видео**: принимает скринкасты и демо как ввод — функция, которой нет у большинства терминальных агентов; полезна для воспроизведения UI-багов.
- **Субагенты для параллельной работы**: поставляется с субагентами coder, explore и plan для фокусированного параллельного исполнения.
- **MCP + маркетплейс плагинов**: AI-native конфигурация MCP плюс экосистема плагинов с маркетплейсом.
- **Интеграция через ACP**: подключается к редакторам/IDE через Agent Client Protocol; lifecycle hooks для автоматизации.
- **Гибкость моделей**: работает из коробки с моделями Kimi, настраивается на другие совместимые провайдеры.

## Подробнее
Kimi Code — ответ Moonshot AI на Claude Code и более широкую категорию терминальных агентов. Single-binary дистрибуция устраняет цепочку зависимостей Node.js, усложняющую установку Claude Code, а запуск за миллисекунды нацелен на жалобы на задержки в агентных CLI.

Возможность ввода видео — самая отличительная черта: подача скринкаста бага или демо желаемого поведения даёт агенту более богатый контекст, чем текст. Это выгодно позиционирует Kimi Code для фронтенд- и UI-работы.

## Связанные записи
- [[kimi-2-6-vs-glm-5-1-agent-reliability]] ([Kimi 2.6 vs GLM 5.1 Agent Reliability](../models/kimi-2-6-vs-glm-5-1-agent-reliability.md))
- [[product-claude-code]] ([Claude Code](../agents/product-claude-code.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[claude-code-frameworks]] ([Claude Code Frameworks](../tools/claude-code-frameworks.md))
