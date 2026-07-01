---
title: "opencode-rate-limiter-plugin — Per-Provider Rate Limiting for OpenCode"
title_ru: "opencode-rate-limiter-plugin — рейт-лимиты по провайдеру для OpenCode"
category: tools
tags: [opencode, plugin, rate-limiting, concurrency, fibers]
aliases: [opencode-rate-limiter, opencode fiber limit]
confidence: medium
updated: 2026-07-01
sources:
  - https://github.com/tmogeid/opencode-rate-limiter-plugin
  - https://www.reddit.com/r/opencode/comments/1ujwats/i_ended_up_creating_my_first_opencode_plugin/
---

## Summary
opencode-rate-limiter-plugin is a community OpenCode plugin that adds per-provider rate limiting (sliding window) and a global concurrency semaphore across workspaces. It was written to work around OpenCode's hard internal limit of 32 fibers shared across all open workspaces, which surfaces as `ResourceExhausted: Worker local total request limit reached`.

## Key Ideas
- **Problem solved:** OpenCode (as of v1.17.11) has a hardcoded internal limit of 32 fibers (lightweight threads) shared across all open workspaces, with no config to change it.
- **Symptom:** with many workspaces open (e.g. 8), requests fail with `ResourceExhausted: Worker local total request limit reached (X/32)`.
- **Solution:** the plugin adds (1) a per-provider sliding-window rate limiter and (2) a global concurrency semaphore across workspaces, preventing OpenCode from firing more requests than it can handle internally.
- Documents a real, undocumented OpenCode internal constraint useful for anyone running many parallel workspaces.

## Details
The plugin is a practical workaround for a quota that isn't exposed in OpenCode's config. Beyond its immediate function, it documents the 32-fiber ceiling — useful operational knowledge for teams running OpenCode with multiple concurrent workspaces against a single provider.

## Related Entries
- [[opencode]] ([OpenCode](opencode.md))
- [[opencode-agents-sync-plugin]] ([OpenCode Agents Sync Plugin](opencode-agents-sync-plugin.md))
- [[headroom-token-saver]] ([Headroom Token Saver](headroom-token-saver.md))

---
<!-- RU -->

## Краткое описание
opencode-rate-limiter-plugin — пользовательский плагин для OpenCode, добавляющий рейт-лимитинг по провайдеру (sliding window) и глобальный семафор конкурентности между воркспейсами. Написан, чтобы обойти жёсткий внутренний лимит OpenCode в 32 fiber'а на все открытые воркспейсы, проявляющийся как `ResourceExhausted: Worker local total request limit reached`.

## Ключевые идеи
- **Решаемая проблема:** OpenCode (на v1.17.11) имеет захардкоженный лимит в 32 fiber'а (легковесных потока) на все открытые воркспейсы, без возможности настройки.
- **Симптом:** при большом числе воркспейсов (например, 8) запросы падают с `ResourceExhausted: Worker local total request limit reached (X/32)`.
- **Решение:** плагин добавляет (1) per-provider sliding-window рейт-лимитер и (2) глобальный семафор конкурентности между воркспейсами, не позволяя OpenCode стрелять больше запросов, чем он может переварить.
- Документирует реальное недокументированное ограничение OpenCode — полезно всем, кто запускает много параллельных воркспейсов.

## Подробнее
Плагин — практический обход квоты, не expos'ящейся в конфиге OpenCode. Помимо прямой функции, он фиксирует потолок в 32 fiber'а — полезное операционное знание для команд, запускающих OpenCode с несколькими конкурентными воркспейсами на одного провайдера.

## Связанные записи
- [[opencode]] ([OpenCode](opencode.md))
- [[opencode-agents-sync-plugin]] ([OpenCode Agents Sync Plugin](opencode-agents-sync-plugin.md))
- [[headroom-token-saver]] ([Headroom Token Saver](headroom-token-saver.md))
