---
title: "MCP Tool-Schema Bloat — 20K Tokens Wasted on a Single 'Hi'"
title_ru: "Раздувание схемы MCP-инструментов — 20K токенов на одно «привет»"
category: tips
tags: [mcp, token-cost, tool-schema, context-engineering, hermes-agent]
aliases: [tool schema bloat, MCP token waste, schema dedup]
confidence: medium
updated: 2026-07-11
sources:
  - https://www.reddit.com/r/AI_Agents/comments/1ut94sc/my_hermes_agent_burning_20k_tokens_on_a_single_hi/
---

## Summary
A self-hosted Hermes agent was sending ~20,000+ tokens on every request — even a trivial "hi" — because the full JSON schema for every enabled tool/MCP server was attached to every call regardless of need. One scraping MCP tool exposing 8 sub-tools with 50+ enum values (duplicated as both string and array params) was responsible for tens of thousands of tokens before the user's message even counted.

## Key Ideas
- **Root cause:** many agent harnesses send the complete tool-definition payload on every request, not just the tools relevant to that turn.
- **Concrete case:** one MCP-connected scraping tool → 8 sub-tools, each with ~50+ enum values repeated twice (string param + array param) = tens of thousands of tokens of definitions.
- **Impact:** on a free provider tier, a single heavier request blew the entire per-minute input-token quota; retries failed with backoff.
- **Why it matters for MCP:** MCP's value is composing many tools, but naive composition multiplies schema cost linearly — a budget trap.
- **Mitigations:** lazy/on-demand tool loading, schema compression, per-turn tool subsetting, deduplicating enum representations.

## Details
This is the tool-surface analogue of the [[browser-snapshot-format-token-cost]] finding: representation cost dominates, and it compounds. As MCP ecosystems grow (a marketplace of hundreds of tools), harnesses that attach every schema on every turn become unusable on metered tiers. The fix belongs at the harness layer — load tool definitions on demand, or compress the schema — not at the model layer.

## Related Entries
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](../research/browser-snapshot-format-token-cost.md))
- [[headroom-token-saver]] ([Headroom Token Saver](../tools/headroom-token-saver.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))

---
<!-- RU -->

## Краткое описание
Самохостящийся агент Hermes отсылает ~20 000+ токенов на каждый запрос — даже на тривиальное «привет», — потому что полная JSON-схема всех включённых инструментов/MCP-серверов крепится к каждому вызову вне зависимости от необходимости. Один scraping-MCP с 8 подтулами и 50+ enum-значениями ответственен за десятки тысяч токенов до того, как сообщение пользователя вообще посчитается.

## Ключевые идеи
- **Корень:** многие харнесы отсылают полный payload определений инструментов на каждый запрос, а не только нужные в текущем ходу.
- **Конкретика:** один scraping-MCP → 8 подтулов, у каждого ~50+ enum-значений, повторённых дважды (строка + массив).
- **Влияние:** на бесплатном тарифе один запрос сжигал всю минутную квоту входных токенов.
- **Почему важно для MCP:** ценность MCP — композиция множества инструментов, но наивная композиция умножает стоимость схемы линейно.
- **Меры:** ленивая загрузка инструментов, сжатие схем, per-turn subset, дедупликация enum.

## Подробнее
Это tool-surface-аналог находки [[browser-snapshot-format-token-cost]]: стоимость представления доминирует и накапливается. С ростом экосистемы MCP харнесы, крепящие все схемы на каждый ход, становятся непригодными на metered-тарифах. Фикс — на уровне харнеса.

## Связанные записи
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](../research/browser-snapshot-format-token-cost.md))
- [[headroom-token-saver]] ([Headroom Token Saver](../tools/headroom-token-saver.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))
