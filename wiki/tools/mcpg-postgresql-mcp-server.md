---
title: "MCPg — Safe-by-Default PostgreSQL MCP Server"
title_ru: "MCPg — безопасный по умолчанию PostgreSQL MCP-сервер"
category: tools
tags: [mcp, postgresql, database, sql-validation, read-only, agent-tools]
aliases: [MCPg, postgres mcp server, devopam MCPg]
confidence: medium
updated: 2026-07-11
sources:
  - https://github.com/devopam/MCPg
  - https://www.reddit.com/r/Qwen_AI/comments/1uon7yv/using_qwen_inference_on_a_postgresql_mcp_server/
---

## Summary
**MCPg** is an open-source PostgreSQL MCP server for AI agents and database workflows. It is safe-by-default (read-only first, guarded execution paths, SQL validation), supports both stdio and HTTP transports, and works with Claude, Cursor, and other MCP clients.

## Key Ideas
- **Read-only first:** default behavior is non-destructive; write paths are guarded.
- **SQL validation and safety checks:** prevents the obvious footguns when an LLM generates SQL against a live database.
- **Both transports:** stdio (local) and HTTP (remote), covering local-agent and service deployments.
- **Observability and operational tooling** for PostgreSQL workflows — not just raw query execution.
- Works with Claude, Cursor, and other MCP clients; tested with Qwen inference.
- Addresses a real concern: giving an agent raw DB access without guardrails is a known antipattern (see [[mcp-tool-poisoning-microsoft]]).

## Details
MCPg sits in the growing niche of database-aware MCP servers that add a safety layer between the agent and the database. The design principle — read-only first, guarded writes, validation — matches the broader agent-safety direction of treating tool access as privileged. This matters because SQL-generating agents can trivially destroy data if the tool surface has no guardrails.

## Related Entries
- [[equibles-mcp-financial-data]] ([Equibles MCP Financial Data](equibles-mcp-financial-data.md))
- [[world-model-mcp]] ([World Model MCP](world-model-mcp.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))

---
<!-- RU -->

## Краткое описание
**MCPg** — открытый PostgreSQL MCP-сервер для ИИ-агентов и работы с БД. Безопасен по умолчанию (сначала read-only, защищённые пути выполнения, валидация SQL), поддерживает stdio и HTTP, работает с Claude, Cursor и другими MCP-клиентами.

## Ключевые идеи
- **Сначала read-only:** поведение по умолчанию неразрушающее; пути записи защищены.
- **Валидация SQL и проверки безопасности:** предотвращает очевидные ошибки при генерации SQL агентом.
- **Оба транспорта:** stdio (локально) и HTTP (удалённо).
- **Наблюдаемость и операционный инструментарий** для рабочих процессов PostgreSQL.
- Работает с Claude, Cursor и др.; тестировалось с Qwen.
- Решает реальную проблему: давать агенту сырой доступ к БД без ограждений — известный антипаттерн.

## Подробнее
MCPg занимает растущую нишу database-aware MCP-серверов, добавляющих слой безопасности между агентом и БД. Принцип — read-only first, защищённая запись, валидация — соответствует направлению agent-safety.

## Связанные записи
- [[equibles-mcp-financial-data]] ([Equibles MCP Financial Data](equibles-mcp-financial-data.md))
- [[world-model-mcp]] ([World Model MCP](world-model-mcp.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))
