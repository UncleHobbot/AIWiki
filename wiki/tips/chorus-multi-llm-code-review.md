---
title: "CHORUS: Multi-LLM Code Review with Parallel Agents"
title_ru: "CHORUS: Многомодельное ревью кода с параллельными агентами"
category: tips
tags: [code-review, multi-model, chorus, parallel-agents, consensus]
confidence: medium
updated: 2026-05-22
sources:
  - https://www.reddit.com/r/kimi/comments/1t6xog7/kimi_claude_codex_gemini_opencode_chorus/
---

## Summary

CHORUS is a multi-LLM code review system that runs parallel reviews across Claude Code, Codex, Gemini CLI, OpenCode, and Kimi simultaneously, using tmux or headless sessions, then aggregates results via unanimous or majority consensus with optional persona assignments per reviewer.

## Key Ideas

- Fires up multiple code reviews in parallel using tmux or headless CLI sessions of existing subscriptions
- No extra API bills — piggybacks on CLI subscriptions you already pay for
- Supports unanimous or majority consensus to aggregate findings
- Assignable personas per LLM (security, architecture drift, edge cases, etc.)
- Fallback: if one LLM is out of quota, retries with another
- Built by 99xAgency, fully open source with a UI for visualization
- Real-world example: Opus approved a PR clean, Kimi flagged a missing tenant check, Gemini caught a race condition — three reviewers, three bugs, one PR

## Details

The core insight behind CHORUS is that relying on a single LLM for code review is insufficient. Even frontier models like Opus 4.7 at max effort make mistakes. By running the same review prompt through multiple models and cross-referencing their outputs, CHORUS catches bugs that any single model misses. Users can set personas per model (e.g., one focuses on security, another on architecture drift) and the system outputs a consolidated review with consensus level. The tool supports MCP commands so reviews can be kicked off from inside any CLI agent session.

## Related Entries
- [[chorus-multi-model-setup]] ([CHORUS: Multi-Model Coding Setup](../tips/chorus-multi-model-setup.md))

---
<!-- RU -->

## Краткое описание

CHORUS — это система многомодельного ревью кода, которая запускает параллельные проверки через Claude Code, Codex, Gemini CLI, OpenCode и Kimi, используя tmux или headless-сессии, и агрегирует результаты через консенсус (единогласный или мажоритарный) с опциональным назначением ролей каждому ревьюеру.

## Ключевые идеи

- Параллельный запуск нескольких LLM для ревью кода через tmux или headless-сессии
- Без дополнительных расходов на API — использует существующие подписки
- Единогласный или мажоритарный консенсус для агрегации результатов
- Назначаемые роли каждой LLM (безопасность, архитектура, граничные случаи)
- Резервное копирование: если одна LLM исчерпала квоту, запрос перенаправляется другой
- Полностью открытый исходный код с UI для визуализации

## Подробнее

CHORUS решает фундаментальную проблему: даже лучшие LLM-модели допускают ошибки при ревью кода. Запуская одну задачу через несколько моделей и сравнивая результаты, система находит ошибки, которые пропускает любая отдельная модель.

## Связанные записи
- [[chorus-multi-model-setup]] ([CHORUS: Multi-Model Coding Setup](../tips/chorus-multi-model-setup.md))
