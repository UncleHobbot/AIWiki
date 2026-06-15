---
title: "Anthropic Splits Off a Separate 'Agent SDK Credit' for Headless/Programmatic Usage (June 15, 2026)"
title_ru: "Anthropic выделяет отдельный 'Agent SDK credit' для headless/программного использования (15 июня 2026)"
category: news
tags: [anthropic, claude-code, agent-sdk, billing, usage-limits, headless]
aliases: [Agent SDK credit, claude -p billing change]
confidence: low
date: 2026-06-15
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1u5jq8x/did_anyone_actually_understand_anthropics_new/
  - https://www.reddit.com/r/ClaudeCode/comments/1u5jqvj/estce_que_quelquun_a_réellement_compris_le/
---

## Summary
Starting June 15, 2026, Anthropic separates programmatic/non-interactive Claude usage (headless mode, Agent SDK, GitHub Actions, third-party Agent SDK apps) from normal Claude Code subscription limits, drawing instead from a new monthly dollar-denominated "Agent SDK credit."

## Key Ideas
- Affected usage: `claude -p` / headless mode, the Claude Agent SDK, Claude Code GitHub Actions, and third-party Agent SDK apps authenticated via a Claude subscription.
- Unaffected usage: interactive Claude chat, Claude Code in the terminal/IDE, and Cowork remain on normal subscription limits, apparently unchanged.
- New monthly Agent SDK credit amounts (per the original poster's understanding): Pro = $20/month, Max 5x = $100/month, Max 20x = $200/month.
- The credit resets with the billing cycle and does not roll over.
- Once the Agent SDK credit is exhausted, behavior depends on whether "usage credits" are enabled — if so, the agent keeps running with additional charges; the exact fallback if not enabled was unclear to the poster.
- The change generated confusion in the community — the same user posted nearly identical threads in English and French asking for clarification, suggesting Anthropic's announcement/documentation was not clear to non-technical users.

## Details
This entry captures an early, community-sourced (and partly self-uncertain) read of an Anthropic billing change taking effect June 15, 2026. The core idea is a split between "interactive" Claude usage (chat, Claude Code CLI/IDE sessions, Cowork) — which stays on the existing Pro/Max subscription quota — and "programmatic/automated" usage (headless `-p` mode, Agent SDK-based agents, CI/CD via GitHub Actions) — which now draws from a separate dollar-denominated monthly credit pool tied to the subscription tier.

This is directly relevant to anyone running scheduled/automated Claude Code workflows (e.g. this wiki's own pipeline commands run via `claude -p` or similar headless invocations) — such usage may now be metered against the new Agent SDK credit rather than the normal session-based limits. Given the source is two near-duplicate Reddit posts asking for clarification (Tier 3, low confidence, no official Anthropic documentation linked), the specific dollar figures and fallback behavior should be verified against Anthropic's official pricing/docs before being treated as authoritative.

## Related Entries
- [[claude-code-usage-reset-may-2026]] ([Anthropic Resets All Claude Code Usage Limits Globally](../news/claude-code-usage-reset-may-2026.md))
- [[claude-usage-limits-token-management]] ([10 Ways to Stop Hitting Claude's Usage Limits](../tips/claude-usage-limits-token-management.md))
- [[custom-agent-loop-vs-sdk]] ([Custom Agent Loop vs Claude Agent SDK](../agents/custom-agent-loop-vs-sdk.md))

---
<!-- RU -->

## Краткое описание
С 15 июня 2026 года Anthropic выделяет программное/неинтерактивное использование Claude (headless-режим, Agent SDK, GitHub Actions, сторонние приложения на Agent SDK) из обычных лимитов подписки Claude Code в новый ежемесячный долларовый "Agent SDK credit".

## Ключевые идеи
- Затронутое использование: `claude -p` / headless-режим, Claude Agent SDK, Claude Code GitHub Actions и сторонние Agent SDK-приложения, авторизованные через подписку Claude.
- Не затронутое использование: интерактивный чат Claude, Claude Code в терминале/IDE и Cowork остаются на обычных лимитах подписки без изменений.
- Новые суммы ежемесячного Agent SDK credit (по пониманию автора поста): Pro — $20/мес, Max 5x — $100/мес, Max 20x — $200/мес.
- Credit обновляется с биллинг-циклом и не переносится на следующий месяц.
- После исчерпания Agent SDK credit поведение зависит от того, включены ли "usage credits" — если да, агент продолжает работать с дополнительной оплатой; точное поведение при отключённых credits автору осталось неясным.
- Изменение вызвало путаницу в сообществе — один и тот же пользователь опубликовал почти одинаковые треды на английском и французском с просьбой объяснить, что говорит о неясности анонса/документации Anthropic для нетехнических пользователей.

## Подробнее
Эта запись фиксирует раннее, основанное на сообществе (и местами неуверенное) понимание изменения биллинга Anthropic, вступающего в силу 15 июня 2026 года. Суть — разделение между "интерактивным" использованием Claude (чат, сессии Claude Code в CLI/IDE, Cowork), которое остаётся в рамках существующей квоты подписки Pro/Max, и "программным/автоматизированным" использованием (headless `-p` режим, агенты на Agent SDK, CI/CD через GitHub Actions), которое теперь расходует отдельный долларовый ежемесячный пул credit, привязанный к тарифу подписки.

Это напрямую касается всех, кто запускает запланированные/автоматизированные workflow на Claude Code (например, собственные pipeline-команды этой wiki, запускаемые через `claude -p` или аналогичные headless-вызовы) — такое использование теперь может учитываться против нового Agent SDK credit, а не обычных лимитов на основе сессий. Поскольку источник — два почти идентичных поста на Reddit с просьбой о разъяснении (tier 3, низкая достоверность, без ссылки на официальную документацию Anthropic), конкретные суммы и поведение при исчерпании credit нужно проверить по официальной документации/прайсингу Anthropic перед использованием как авторитетных данных.

## Связанные записи
- [[claude-code-usage-reset-may-2026]] ([Anthropic Resets All Claude Code Usage Limits Globally](../news/claude-code-usage-reset-may-2026.md))
- [[claude-usage-limits-token-management]] ([10 Ways to Stop Hitting Claude's Usage Limits](../tips/claude-usage-limits-token-management.md))
- [[custom-agent-loop-vs-sdk]] ([Custom Agent Loop vs Claude Agent SDK](../agents/custom-agent-loop-vs-sdk.md))
