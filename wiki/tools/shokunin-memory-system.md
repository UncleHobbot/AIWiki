---
title: "Shokunin: Persistent Memory for Coding Agents"
title_ru: "Shokunin: Персистентная память для кодинговых агентов"
category: tools
tags: [memory, coding-agents, chromadb, skills, opencode]
updated: 2026-05-15
sources:
  - https://www.reddit.com/r/opencode/comments/1tcazbs/35_skills_3_mcp_servers_persistent_memory_i_built/
  - https://github.com/EliasOulkadi/shokunin
---

## Summary

Shokunin is a local memory system for AI coding agents that uses ChromaDB to persist session context across conversations, along with 35 domain-specific skills and 3 MCP servers.

## Key Ideas
- Local Python server backed by ChromaDB (vector DB) stores session summaries
- Data persists as ~400 KB SQLite3 file — survives reboots and power outages
- 35 skills covering infrastructure, backend, frontend, mobile, content, business
- Skills include error handling tables, production checklists, OWASP-referenced auth guides
- 3 MCP servers + subagents with Ollama fallback for offline use
- Installer available: `irm https://raw.githubusercontent.com/EliasOulkadi/shokunin/master/install.ps1 | iex`
- Key insight: instructions like "MANDATORY" in agent config work better than polite suggestions for consistent memory save/search behavior

## Details

The system addresses the "blank slate" problem: every time a coding agent session starts, there is no memory of previous work. The ChromaDB integration saves task summaries when the agent finishes and retrieves relevant context when a new session begins.

The main engineering challenge was not the database integration (that took an afternoon) but getting the agent to consistently save and search memory across sessions. Explicit commands in agent configuration proved far more effective than natural language suggestions.

The skill system grew from the memory project into a comprehensive agent knowledge base. Skills contain executable scripts, error handling patterns, and production-grade checklists. The auth skill cites OWASP standards; the database skill includes real EXPLAIN ANALYZE examples.

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[tencent-db-agent-memory]] ([TencentDB Agent Memory: Local Long-Term Memory for AI Agents](../tools/tencent-db-agent-memory.md))
- [[agentmemory]] ([agentmemory: Persistent Memory for AI Coding Agents](../tools/agentmemory.md))

---
<!-- RU -->

## Краткое описание

Shokunin — локальная система памяти для ИИ-кодинговых агентов, использующая ChromaDB для сохранения контекста между сессиями, а также 35 предметных навыков и 3 MCP-сервера.

## Ключевые идеи
- Локальный Python-сервер на базе ChromaDB (векторная БД) хранит сводки сессий
- Данные хранятся как файл SQLite3 ~400 КБ — переживают перезагрузки и отключения питания
- 35 навыков: инфраструктура, бэкенд, фронтенд, мобильная разработка, контент, бизнес
- Навыки включают таблицы обработки ошибок, production-чеклисты, руководства по авторизации с ссылками на OWASP
- 3 MCP-сервера + субагенты с фоллбэком на Ollama для офлайн-работы
- Ключевое наблюдение: явные команды «MANDATORY» в конфигурации агента работают лучше вежливых предложений

## Подробнее

Система решает проблему «чистого листа»: при каждом запуске сессии кодингового агента нет памяти о предыдущей работе. Интеграция с ChromaDB сохраняет сводки задач по завершении и извлекает релевантный контекст при начале новой сессии.

Основная инженерная сложность заключилась не в интеграции с БД, а в обеспечении стабильного сохранения и поиска памяти агентом. Явные команды в конфигурации оказались значительно эффективнее вежливых предложений на естественном языке.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[tencent-db-agent-memory]] ([TencentDB Agent Memory: Local Long-Term Memory for AI Agents](../tools/tencent-db-agent-memory.md))
