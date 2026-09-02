---
title: "llms.txt + MCP + Skills — Keeping Agent Docs Current"
title_ru: "llms.txt + MCP + Skills — актуальная документация для агентов"
category: tips
tags: [llms-txt, mcp, skills, documentation, api-docs, agent-context]
aliases: [llms.txt, agent docs mcp, fresh api docs agents]
confidence: medium
updated: 2026-09-01
sources:
  - https://fish.audio/blog/llms-txt-mcp-agent-skills/
---

## Summary
A pattern (described via Fish Audio's implementation) for solving the stale-API-docs failure mode in coding agents: ship three agent-native interfaces — an `llms.txt` sitemap so agents can navigate the docs, an MCP server serving live API reference, and installable skill bundles packaging docs for offline/in-context use in Claude Code and similar tools.

## Key Ideas
- **The problem:** agents trained on older snapshots confidently use outdated APIs; docs sites are tuned for humans (JS-heavy, poor navigation), not for agent context windows.
- **Three-layer fix:**
  1. **`llms.txt`** — machine-readable map of the documentation for agent navigation.
  2. **Docs MCP server** — live, always-current API lookup as a tool call.
  3. **Skill bundles** — packaged docs for offline/in-context use in Claude Code and peers.
- **Generalizable:** any API vendor can adopt the same trio; the pattern is tool-agnostic.
- Complements context-management tactics ([[anthropic-cost-optimization-cookbook]]) — fresh docs reduce retry loops, which reduces cost.

## Details
The deeper principle: an API's "agent surface" (llms.txt + MCP + skills) is becoming as important as its human docs site. Vendors that ship all three get cited and used correctly by agents; vendors that don't get hallucinated API calls. For wiki readers publishing their own APIs, this is a low-cost checklist; for agent users, it's a signal of which providers are agent-friendly.

## Related Entries
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](mcp-tool-schema-bloat-token-cost.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](anthropic-cost-optimization-cookbook.md))
- [[gnosis-mcp]] ([Gnosis MCP](gnosis-mcp.md))

---
- [[geo-optimize-codex-skill]] ([geo-optimize-site Codex Skill](geo-optimize-codex-skill.md))
<!-- RU -->

## Краткое описание
Паттерн (на примере реализации Fish Audio) для решения проблемы устаревшей API-документации у кодинг-агентов: три агент-нативных интерфейса — `llms.txt`-карта для навигации агента, MCP-сервер с живым API-справочником и устанавливаемые skill-бандлы с документацией для офлайн-использования в Claude Code и подобных.

## Ключевые идеи
- **Проблема:** агенты, обученные на старых снапшотах, уверенно используют устаревшие API; сайты документации заточены под людей, а не под контекстные окна агентов.
- **Трёхслойный фикс:**
  1. **`llms.txt`** — машиночитаемая карта документации.
  2. **Docs MCP-сервер** — живой API-справочник как tool call.
  3. **Skill-бандлы** — упакованная документация для офлайн/контекста.
- **Обобщаемо:** любой API-вендор может принять ту же триаду.
- Дополняет тактики управления контекстом ([[anthropic-cost-optimization-cookbook]]) — свежие доки сокращают циклы ретраев и стоимость.

## Подробнее
Глубокий принцип: «агентная поверхность» API (llms.txt + MCP + skills) становится так же важна, как человеческий сайт документации. Вендоры с полной триадой используются агентами корректно; без неё получают галлюцинированные вызовы API. Для публикующих свои API — дешёвый чеклист; для пользователей агентов — сигнал агент-френдли вендора.

## Связанные записи
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](mcp-tool-schema-bloat-token-cost.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](anthropic-cost-optimization-cookbook.md))
- [[gnosis-mcp]] ([Gnosis MCP](gnosis-mcp.md))
