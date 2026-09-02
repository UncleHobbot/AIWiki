---
title: "relay-dsh-plugin-codex — Codex as a Native Backend Inside DeepSeek Harness"
title_ru: "relay-dsh-plugin-codex — Codex как нативный бэкенд внутри DeepSeek Harness"
category: tools
tags: [codex, deepseek, dsh, plugin, app-server, harness]
aliases: [relay dsh plugin, dsh codex plugin, deepseek harness codex]
confidence: medium
updated: 2026-09-01
sources:
  - https://github.com/yangbobo2021/relay-dsh-plugin-codex
  - https://www.npmjs.com/package/relay-dsh-plugin-codex
---

## Summary
A plugin that adds OpenAI Codex as a native conversation backend inside the DeepSeek Harness (DSH) Web UI — each DSH session continues one Codex App Server thread, so users keep DSH's workspace, history, and approvals instead of switching interfaces. The plugin bundles a pinned `@openai/codex` runtime with native binaries for macOS/Windows/Linux (x64 + arm64).

## Key Ideas
- **Backend-agnostic harness direction:** DSH stays the front-end (workspace, composer, approvals, questions); Codex becomes a swappable conversation engine — the same "harness hosts many backends" pattern as [[agentplugins-cross-harness]] and [[orkestra-multi-cli]].
- **Bundled pinned runtime:** no global `codex` install needed; versioned compatibility tracking (plugin 0.2.1 ↔ DSH 0.1.2-alpha.x / 0.1.1-rc.2); release channels `latest` and `next`.
- **Feature pass-through:** Codex models, reasoning-effort control, images, interruption, and DSH-contributed tools work in the same conversation.
- **Install:** `npx @deepseek-ai/dsh plugin --profile web add relay-dsh-plugin-codex` (Node 22.13+, pnpm); npm-published with verified provenance; bilingual EN/中文 README.
- A sibling Relay plugin adds Claude Code as a backend — the author is building a multi-backend relay family for DSH.

## Details
Notable less for the plugin itself than for what it signals: harnesses are becoming shells that host competing model-agent backends behind a uniform workspace. DSH (a developer preview) + relay plugins means a team can standardize on one review/approval surface while mixing Codex and Claude engines per task. Watch the compatibility matrix — DSH's pre-GA churn is the main operational risk.

## Related Entries
- [[agentplugins-cross-harness]] ([AgentPlugins](agentplugins-cross-harness.md))
- [[orkestra-multi-cli]] ([Orkestra Multi-CLI](orkestra-multi-cli.md))
- [[product-deepseek]] ([DeepSeek](../models/product-deepseek.md))
- [[claude-code]] ([Claude Code](claude-code.md))

---
<!-- RU -->

## Краткое описание
Плагин, добавляющий OpenAI Codex как нативный бэкенд разговоров внутри Web UI DeepSeek Harness (DSH) — каждая DSH-сессия ведёт один поток Codex App Server, поэтому пользователь сохраняет воркспейс, историю и подтверждения DSH вместо переключения интерфейсов. Плагин вешает зафиксированный рантайм `@openai/codex` с нативными бинарниками macOS/Windows/Linux (x64 + arm64).

## Ключевые идеи
- **Направление «харнес безразличен к бэкенду»:** DSH остаётся фронтендом; Codex — сменяемый разговорный движок — тот же паттерн, что [[agentplugins-cross-harness]] и [[orkestra-multi-cli]].
- **Встроенный зафиксированный рантайм:** глобальный `codex` не нужен; отслеживание совместимости версий; каналы `latest` и `next`.
- **Прохождение фич:** модели Codex, reasoning-effort, изображения, прерывание и DSH-инструменты работают в одном разговоре.
- **Установка:** `npx @deepseek-ai/dsh plugin --profile web add relay-dsh-plugin-codex` (Node 22.13+, pnpm); npm с verified provenance; двуязычный README.
- Сиблинг-плагин Relay добавляет Claude Code — автор строит мульти-бэкендное семейство для DSH.

## Подробнее
Значимость не столько в самом плагине, сколько в сигнале: харнесы становятся оболочками, хостящими конкурирующие модель-агентные бэкенды за единым воркспейсом. DSH + relay-плагины позволяют команде стандартизовать одну поверхность ревью/подтверждений, смешивая движки Codex и Claude под задачу. Следить за матрицей совместимости — pre-GA churn DSH является главным операционным риском.

## Связанные записи
- [[agentplugins-cross-harness]] ([AgentPlugins](agentplugins-cross-harness.md))
- [[orkestra-multi-cli]] ([Orkestra Multi-CLI](orkestra-multi-cli.md))
- [[product-deepseek]] ([DeepSeek](../models/product-deepseek.md))
- [[claude-code]] ([Claude Code](claude-code.md))
