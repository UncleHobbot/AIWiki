---
title: "z.ai Max Plan — Undisclosed Weekly Token Limit (Community Report)"
title_ru: "Тариф Max от z.ai — нераскрытый недельный лимит токенов (сообщество)"
category: news
tags: [zai, glm, pricing, token-limit, community-report]
aliases: [z.ai max weekly limit, zai lied weekly limit]
confidence: low
date: 2026-06-30
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/ZaiGLM/comments/1uk6b12/well_zai_lied_about_no_weekly_limit_on_the_max_plan/
---

## Summary
A r/ZaiGLM community report alleges that z.ai's Max plan, advertised since mid-February as having no weekly token cap (only a 5-hour rolling cap), silently imposes a ~1B-token weekly limit. The author's coding agent lost connection/authorization upon hitting it, with no customer-service response.

## Key Ideas
- **Marketed:** Max plan = unlimited weekly tokens, 5-hour cap only (since ~mid-Feb 2026).
- **Reported reality:** a ~1B-token weekly ceiling; the coding agent disconnects with auth errors when reached.
- Coding plans reportedly treat "chances tokens" (retry tokens) as normal tokens, accelerating burn.
- Customer support described as non-responsive.
- **Tier 3** single-user report; unverified by z.ai — treat as a community flag, not confirmed policy.

## Details
This matters operationally for anyone running heavy agentic workflows on z.ai's Max plan: budgeting assumptions based on "no weekly cap" may be wrong. Worth cross-referencing with other users before relying on it for production. Consistent with the broader pattern of coding-agent subscription tiers having soft caps that surface only under sustained load.

## Related Entries
- [[product-zai-glm]] ([z.ai / GLM](../models/product-zai-glm.md))
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[claude-code-usage-reset-may-2026]] ([Claude Code Usage Reset](claude-code-usage-reset-may-2026.md))

---
<!-- RU -->

## Краткое описание
Сообщение из r/ZaiGLM: тариф Max от z.ai, рекламируемый с середины февраля как не имеющий недельного лимита токенов (только скользящий 5-часовой cap), негласно накладывает недельный лимит ~1B токенов. Кодинг-агент автора потерял соединение/авторизацию при достижении лимита, ответа от поддержки нет.

## Ключевые идеи
- **Маркетинг:** Max = неограниченные недельные токены, только 5-часовой cap (с ~середины февраля 2026).
- **Сообщённая реальность:** недельный потолок ~1B токенов; при достижении кодинг-агент отключается с ошибками авторизации.
- По сообщению, кодинг-планы считают «chances tokens» (токены повторов) обычными токенами, ускоряя расход.
- Поддержка охарактеризована как неотвечающая.
- **Уровень 3** — рассказ одного пользователя; z.ai не подтверждено; относимся как к флагу сообщества, а не к подтверждённой политике.

## Подробнее
Это операционно важно для всех, кто гоняет тяжёлые агентные процессы на тарифе Max от z.ai: бюджетирование, исходящее из «без недельного cap», может быть ошибочным. Стоит перепроверить у других пользователей перед продакшен-зависимостью. Согласуется с общим паттерном soft-cap'ов в подписках на кодинг-агентов, всплывающих только под длительной нагрузкой.

## Связанные записи
- [[product-zai-glm]] ([z.ai / GLM](../models/product-zai-glm.md))
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[claude-code-usage-reset-may-2026]] ([Claude Code Usage Reset](claude-code-usage-reset-may-2026.md))
