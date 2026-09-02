---
title: "TokenRay — Per-Project, Per-Machine Cost Dashboard for Coding Agents"
title_ru: "TokenRay — дашборд стоимости кодинг-агентов по проектам и машинам"
category: tools
tags: [cost-tracking, dashboard, opencode, claude-code, token-usage, privacy]
aliases: [TokenRay, agent cost dashboard, coding agent cost tracking]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/opencode/comments/1w5amam/i_built_tokenray_a_hosted_dashboard_that_shows/
---

## Summary
**TokenRay** is a hosted dashboard answering "what are my AI coding agents actually costing?" — broken down by day, project, machine, session, and token type (input/output/reasoning/cache). A tiny zero-dependency Node.js local agent reads the coding agent's local database read-only and pushes aggregates up; sync is watermark + batch, idempotent and crash-safe.

## Key Ideas
- **The gap:** provider invoices show one global number; nobody can attribute cost to project/machine/session.
- **Privacy-first design:** prompts, responses, and tool outputs are never collected — only operational metadata (session title, hostname, project, counts/costs).
- **Read-only local ingestion:** parses the agents' local DBs (Claude Code, OpenCode, etc.) rather than proxying API traffic.
- **Crash-safe sync:** watermark + batch with idempotent re-sends — no double counting.
- Pairs with the wiki's cost cluster: [[opencode-12m-token-burn]], [[kimi-code-quota-audit]], [[anthropic-cost-optimization-cookbook]].

## Details
Attribution is the missing half of agent cost management: the cookbook optimizes cost per task, but you first need to know *which* project/machine/session burns the budget. Reading local agent databases instead of proxying keeps it privacy-safe and works retroactively on existing history.

## Related Entries
- [[opencode-12m-token-burn]] ([OpenCode 12M Token Burn](../tips/opencode-12m-token-burn.md))
- [[kimi-code-quota-audit]] ([Kimi Code Quota Audit](../news/kimi-code-quota-audit.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](../tips/anthropic-cost-optimization-cookbook.md))

---
<!-- RU -->

## Краткое описание
**TokenRay** — хостед-дашборд на вопрос «во что реально обходятся мои кодинг-агенты» — с разбивкой по дню, проекту, машине, сессии и типу токенов (вход/выход/reasoning/кэш). Крошечный локальный агент на Node.js (без зависимостей) читает локальную БД кодинг-агента в read-only и отправляет агрегаты наверх; синхронизация watermark + batch, идемпотентная и crash-safe.

## Ключевые идеи
- **Пробел:** счёт провайдера — одно глобальное число; невозможно атрибутировать стоимость проекту/машине/сессии.
- **Privacy-first:** промпты, ответы и выводы инструментов никогда не собираются — только операционные метаданные.
- **Read-only-ингест:** парсит локальные БД агентов (Claude Code, OpenCode), а не проксирует API-трафик.
- **Crash-safe синхронизация:** watermark + batch с идемпотентными повторами — без двойного счёта.
- Дополняет кластер стоимости вики.

## Подробнее
Атрибуция — недостающая половина управления стоимостью агентов: cookbook оптимизирует цену задачи, но сперва нужно знать, *какой* проект/машина/сессия жгут бюджет. Чтение локальных БД вместо проксирования сохраняет приватность и работает ретроактивно на существующей истории.

## Связанные записи
- [[opencode-12m-token-burn]] ([OpenCode 12M Token Burn](../tips/opencode-12m-token-burn.md))
- [[kimi-code-quota-audit]] ([Kimi Code Quota Audit](../news/kimi-code-quota-audit.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](../tips/anthropic-cost-optimization-cookbook.md))
