---
title: "MCP 2026-07-28 Spec — Stateless Core, Standardized Extensions, Hardened Auth"
title_ru: "Спецификация MCP 2026-07-28 — stateless-ядро, стандартизованные расширения, усиленная аутентификация"
category: news
tags: [mcp, protocol, stateless, spec, anthropic, security]
aliases: [MCP 2026-07-28, MCP stateless core, MCP spec update]
confidence: high
date: 2026-08-29
updated: 2026-09-01
sources:
  - https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
  - https://x.com/DailyDoseOfDS_/status/2093632264408273011
  - https://www.anthropic.com/engineering/code-execution-with-mcp
---

## Summary
The Model Context Protocol's 2026-07-28 specification is live and coming to Claude products: it moves MCP to a **stateless core** — with statefulness handled through standardized extensions rather than the protocol itself — alongside hardened authentication. Widely called the biggest MCP update since launch; it reframes the stateful-vs-stateless debate that has run through the MCP community all year.

## Key Ideas
- **Stateless core:** the protocol core drops server-side session state; servers become easier to scale horizontally, restart, and load-balance.
- **Statefulness as an extension:** sessions that need continuity get it via well-defined extensions instead of bespoke implementations — standardizing what every vendor was hand-rolling.
- **Hardened auth:** the spec tightens the authentication story, addressing the token/session weaknesses that recent MCP attack research exploited ([[mcp-tool-poisoning-microsoft]], [[amazon-q-mcp-config-rce]]).
- **Companion engineering guidance:** Anthropic's "code execution with MCP" piece shows agents driving MCP servers through code for token efficiency.
- **Related efficiency work:** MCP Tool Search cuts tool-definition token overhead ~85% — the harness-side fix for the schema-bloat problem ([[mcp-tool-schema-bloat-token-cost]]).

## Details
The stateless-core decision settles the debate framed by the "Stateful vs Stateless MCP" discussion (130K views on X): protocol-level state was MCP's scaling Achilles' heel, and making it optional-via-extension lets simple servers stay simple while stateful workflows (like the ones [[shokunin-memory-system]]-style memory tools need) remain possible. For agent builders, the practical effects are fewer sticky-session bugs and easier server swaps; for the ecosystem, it's a maturity signal — MCP is optimizing for operability, not just capability.

## Related Entries
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](../tips/mcp-tool-schema-bloat-token-cost.md))
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK](../agents/mcp-vs-adk-agent-connectivity.md))
- [[mcpg-postgresql-mcp-server]] ([MCPg PostgreSQL MCP Server](../tools/mcpg-postgresql-mcp-server.md))

---
<!-- RU -->

## Краткое описание
Спецификация Model Context Protocol 2026-07-28 вышла и приходит в продукты Claude: MCP переводится на **stateless-ядро** — состояние реализуется через стандартизованные расширения, а не сам протокол — плюс усиленная аутентификация. Это крупнейшее обновление MCP с момента запуска; оно ставит точку в годовом споре stateful против stateless.

## Ключевые идеи
- **Stateless-ядро:** ядро протокола избавляется от серверного состояния сессий; серверы проще масштабировать, перезапускать и балансировать.
- **Состояние как расширение:** сессиям с непрерывностью — четко определённые расширения вместо кустарных реализаций.
- **Усиленная аутентификация:** спецификация закрывает слабости токенов/сессий, которые эксплуатировал недавний research ([[mcp-tool-poisoning-microsoft]], [[amazon-q-mcp-config-rce]]).
- **Сопроводительное руководство:** «code execution with MCP» от Anthropic — агенты驱动 MCP-серверы через код ради экономии токенов.
- **Связанная оптимизация:** MCP Tool Search снижает оверхед определений инструментов ~85% — фикс проблемы раздувания схем ([[mcp-tool-schema-bloat-token-cost]]).

## Подробнее
Решение о stateless-ядре закрывает дебаты «Stateful vs Stateless MCP» (130K просмотров в X): протокольное состояние было ахиллесовой пятой масштабирования MCP, а опциональность через расширения позволяет простым серверам оставаться простыми, сохраняя stateful-сценарии. Для билдеров агентов — меньше багов sticky-session и легче замена серверов; для экосистемы — сигнал зрелости.

## Связанные записи
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](../tips/mcp-tool-schema-bloat-token-cost.md))
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK](../agents/mcp-vs-adk-agent-connectivity.md))
- [[mcpg-postgresql-mcp-server]] ([MCPg PostgreSQL MCP Server](../tools/mcpg-postgresql-mcp-server.md))
