---
title: "OC-Claw — Desktop Pet for Agent Monitoring"
title_ru: "OC-Claw — десктоп-питомец для мониторинга агентов"
category: tools
tags: [agents, desktop, monitoring, opencode, claude-code, tauri, rust]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/rainnoon/oc-claw
  - https://www.reddit.com/r/vibecoding/comments/1u2ym9c/a_little_desktop_pet_that_reacts_to_claude_code/
---

## Summary

Desktop pet built with Tauri v2 + Rust that lives on the screen edge and reacts to AI coding agents in real time — moves when working, naps when idle, pings user when the agent needs input. Works with Claude Code, Cursor, Codex, Gemini CLI, and more.

## Key Ideas

- Desktop pet visualizes agent state in real time: working, idle, waiting for input
- Supports multiple agents: Claude Code, Cursor, Codex, Gemini CLI, Hermes, OpenClaw
- Built with Tauri v2 + Rust for minimal memory and CPU footprint
- Solves the "come back to find agent stopped 5 min ago" problem — user gets pinged when attention is needed
- Open source and extensible — community can add support for new agents

## Details

OC-Claw solves a surprisingly common pain point in agentic coding workflows: the agent runs for minutes at a time, and the user steps away only to return and discover it stopped waiting for input 5 minutes ago. The desktop pet sits on the screen edge and provides ambient awareness of what the agent is doing.

The pet has distinct visual states: active movement when the agent is processing, a resting/napping animation when idle, and an attention-grabbing ping (bounce, sound, notification) when the agent is waiting for user input. This transforms agent monitoring from an active "check the terminal" task into passive peripheral awareness.

The choice of Tauri v2 + Rust is deliberate — a monitoring tool should consume minimal resources. Unlike Electron-based alternatives, OC-Claw uses a fraction of the memory. The Rust backend monitors agent process state and file-system signals to detect what the agent is doing without requiring API integrations.

Support for multiple agents is key. Users often run different coding agents for different tasks, and OC-Claw normalizes the monitoring experience across Claude Code, Cursor, Codex, Gemini CLI, Hermes, and OpenClaw.

## Related Entries

- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[amore-opencode-research-plugin]] ([amore](../tools/amore-opencode-research-plugin.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG](../tools/opencoderag-rag-plugin.md))

---
<!-- RU -->

## Краткое описание

Десктоп-питомец на Tauri v2 + Rust, живущий на краю экрана и реагирующий на AI-агенты кодирования в реальном времени — двигается при работе, спит при простое, уведомляет пользователя, когда агент ждёт ввода. Поддерживает Claude Code, Cursor, Codex, Gemini CLI и другие.

## Ключевые идеи

- Десктоп-питомец визуализирует состояние агента в реальном времени: работа, простой, ожидание ввода
- Поддержка нескольких агентов: Claude Code, Cursor, Codex, Gemini CLI, Hermes, OpenClaw
- Построен на Tauri v2 + Rust для минимального потребления памяти и CPU
- Решает проблему «вернулся и обнаружил, что агент остановился 5 минут назад» — пользователь получает уведомление, когда нужно внимание
- Открытый исходный код и расширяемый — сообщество может добавить поддержку новых агентов

## Подробнее

OC-Claw решает неожиданно распространённую проблему в агентных workflow кодирования: агент работает минутами, пользователь отходит и возвращается, обнаруживая, что тот остановился в ожидании ввода 5 минут назад. Десктоп-питомец располагается на краю экрана и обеспечивает фоновую осведомлённость о действиях агента.

У питомца есть различные визуальные состояния: активное движение при обработке, анимация отдыха/сна при простое и привлекающее внимание уведомление (прыжок, звук, нотификация), когда агент ждёт ввода. Это превращает мониторинг агента из активной задачи «проверь терминал» в пассивную периферийную осведомлённость.

Выбор Tauri v2 + Rust сделан намеренно — инструмент мониторинга должен потреблять минимум ресурсов. В отличие от альтернатив на Electron, OC-Claw использует долю памяти. Бэкенд на Rust отслеживает состояние процессов агента и сигналы файловой системы, определяя действия агента без необходимости API-интеграций.

Поддержка нескольких агентов — ключевой фактор. Пользователи часто запускают разные агенты для разных задач, и OC-Claw унифицирует опыт мониторинга для Claude Code, Cursor, Codex, Gemini CLI, Hermes и OpenClaw.

## Связанные записи

- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[amore-opencode-research-plugin]] ([amore](../tools/amore-opencode-research-plugin.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG](../tools/opencoderag-rag-plugin.md))
