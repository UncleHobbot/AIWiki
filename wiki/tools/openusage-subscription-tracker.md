---
title: "OpenUsage: Menu-Bar Tracker for 10 AI Coding Subscriptions"
title_ru: "OpenUsage: трекер 10 подписок на AI-кодинг в строке меню"
category: tools
tags: [cost-optimization, usage-tracking, macos, claude-code, codex, copilot, cursor, opencode, zai, monitoring]
aliases: [openusage, OpenUsage, robinebers/openusage, AI subscription tracker]
confidence: high
date: 2026-08-31
updated: 2026-08-31
sources:
  - https://github.com/robinebers/openusage
  - https://www.reddit.com/r/ZaiGLM/comments/1vzxzi1/
---

## Summary
OpenUsage is a native macOS menu-bar app (4,000+ stars) that tracks quota and spend across ten AI coding subscriptions — Antigravity, Claude, Codex, Copilot, Cursor, Devin, Grok, OpenCode, OpenRouter, and Z.ai — by reading credentials already on your system rather than requiring separate logins.

## Key Ideas
- **Ten providers in one view**: each integration surfaces that provider's own metric shape — session limits, weekly quotas, credit balances, or raw spend — rather than forcing a single artificial unit.
- **Uses existing credentials**: reads from keychain and local auth files, so no additional login flow. Only OpenRouter and Z.ai need explicit API keys, because they store no local credentials.
- **Menu-bar pins**: pin the specific metrics you care about to the menu bar with customizable formatting, plus a dashboard popover organized by provider with live countdown timers to quota reset.
- **Scriptable**: ships a CLI and a local HTTP API, so usage data can feed into your own tooling — status lines, dashboards, or automated alerts.
- **5-minute refresh with cached display**: shows instantly from cache while refreshing in the background.

## Details
The multi-subscription problem OpenUsage solves is a direct consequence of how the agentic coding market fragmented. Practitioners commonly hold several subscriptions simultaneously — a Claude Max plan, a Copilot seat, a Z.ai coding plan, OpenRouter credits — each with a different quota model, reset cadence, and billing page. Before something like this, answering "which subscription am I about to exhaust?" meant checking four or five separate dashboards.

The design decision that makes it practical is reading existing local credentials. Requiring users to generate and paste API keys for ten providers would have made setup cost exceed the benefit for most people; leaning on the keychain and the auth files these CLIs already write reduces setup to launching the app.

The CLI and local HTTP API are the extension point worth noting for this wiki's purposes: they make usage data available to Claude Code status lines and hooks, so quota awareness can be surfaced inside the agent session rather than in a separate app.

**Platform limitation**: macOS only — it is a native menu-bar application, with no Windows or Linux equivalent.

## Related Entries
- [[claude-usage-limits-token-management]] ([Claude Usage Limits and Token Management](../tips/claude-usage-limits-token-management.md))
- [[claude-code-9-mistakes-wasting-tokens]] ([9 Claude Code Mistakes That Waste Tokens](../tips/claude-code-9-mistakes-wasting-tokens.md))
- [[zai-max-plan-undisclosed-weekly-limit]] ([Z.ai Max Plan Undisclosed Weekly Limit](../news/zai-max-plan-undisclosed-weekly-limit.md))
- [[github-copilot-pricing-exodus]] ([GitHub Copilot Pricing Exodus](../news/github-copilot-pricing-exodus.md))

---
<!-- RU -->

## Краткое описание
OpenUsage — нативное macOS-приложение для строки меню (4000+ звёзд), отслеживающее квоты и расходы по десяти подпискам на AI-кодинг: Antigravity, Claude, Codex, Copilot, Cursor, Devin, Grok, OpenCode, OpenRouter и Z.ai — считывая уже имеющиеся в системе учётные данные вместо отдельного входа.

## Ключевые идеи
- **Десять провайдеров в одном окне**: каждая интеграция показывает метрику в том виде, в каком её ведёт сам провайдер — лимиты сессий, недельные квоты, баланс кредитов или расходы.
- **Использует существующие учётные данные**: читает из keychain и локальных файлов авторизации. Только OpenRouter и Z.ai требуют явных API-ключей, поскольку не хранят учётные данные локально.
- **Пины в строке меню**: закрепление нужных метрик с настраиваемым форматом плюс всплывающая панель по провайдерам с живым отсчётом до сброса квоты.
- **Пригодно для скриптов**: есть CLI и локальный HTTP API, поэтому данные об использовании можно передавать в собственные инструменты.
- **Обновление раз в 5 минут с кешем**: мгновенное отображение из кеша с фоновым обновлением.

## Подробнее
Проблема множественных подписок, которую решает OpenUsage, — прямое следствие фрагментации рынка агентного кодинга. Практики часто держат несколько подписок одновременно, у каждой свои модель квот, периодичность сброса и страница биллинга. До появления подобных инструментов ответ на вопрос «какая подписка у меня вот-вот закончится?» требовал проверки четырёх-пяти отдельных панелей.

Ключевое проектное решение — чтение существующих локальных учётных данных. Требование сгенерировать и вставить API-ключи для десяти провайдеров сделало бы затраты на настройку выше пользы.

CLI и локальный HTTP API — та точка расширения, которая интересна для этой вики: они делают данные об использовании доступными для status line и hooks в Claude Code.

**Ограничение платформы**: только macOS.

## Связанные записи
- [[claude-usage-limits-token-management]] ([Лимиты использования Claude](../tips/claude-usage-limits-token-management.md))
- [[claude-code-9-mistakes-wasting-tokens]] ([9 ошибок Claude Code, тратящих токены](../tips/claude-code-9-mistakes-wasting-tokens.md))
- [[zai-max-plan-undisclosed-weekly-limit]] ([Скрытый недельный лимит Z.ai Max](../news/zai-max-plan-undisclosed-weekly-limit.md))
- [[github-copilot-pricing-exodus]] ([Исход из-за цен GitHub Copilot](../news/github-copilot-pricing-exodus.md))
