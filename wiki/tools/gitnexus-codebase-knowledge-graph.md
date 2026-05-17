---
title: "GitNexus: Codebase Knowledge Graph for Coding Agents"
title_ru: "GitNexus: граф знаний кодовой базы для кодинговых агентов"
category: tools
tags: [gitnexus, knowledge-graph, mcp, codebase-indexing, coding-agents, opencode, claude-code, cursor, tree-sitter, impact-analysis]
date: 2026-05-06
updated: 2026-05-17
sources:
  - https://www.youtube.com/watch?v=bhsd9MXfccg
  - https://github.com/abhigyanpatwari/GitNexus
---

## Summary

GitNexus indexes an entire codebase into a local knowledge graph (LadybugDB) and exposes it to coding agents via MCP. It gives agents architectural awareness — callers, callees, inheritance chains, impact analysis — so they stop making blind edits that silently break production.

## Key Ideas
- **The blind edit problem:** Coding agents read files one at a time; they don't know that 40 other places depend on what a function returns. Edits look clean in the diff but silently fail in production
- **Knowledge graph from code:** Walks file tree, parses with tree-sitter, extracts functions/classes/methods, resolves imports, traces inheritance chains, runs community detection, traces execution flows from entry points to leaf nodes
- **Hybrid search index:** BM25 + semantic embeddings on top of the graph, all local, no network calls
- **11 MCP tools per repo + 5 for repo groups:** query (hybrid search), context (360° symbol view with callers/callees), impact (blast radius analysis with confidence scores), detect_changes (maps git diff to affected processes), rename (multi-file coordinated renames), cypher (raw graph queries)
- **Auto-generated skills:** Creates AGENTS.md, claude.md, and 4 skill files (exploring, debugging, impact analysis, refactoring) that teach agents to use GitNexus tools for specific tasks
- **Supports 14 languages:** TypeScript, JavaScript, Python, Java, Kotlin, C#, Go, Rust, PHP, Ruby, Swift, C, C++, Dart
- **Works with any MCP-compatible agent:** OpenCode, Claude Code, Cursor, Windsurf, Codex
- **Web UI at gitnexus.vercel.app:** Interactive force-directed graph visualization, symbol search, Cypher query editor, chat with codebase via LangChain ReAct agent
- **36K+ GitHub stars**, PolyForm non-commercial license, Docker images signed with cosign, K8s admission policy for signature verification
- **Reindexing:** 30-60 seconds on a medium repo. Claude Code hook auto-detects stale index

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | The blind edit problem: agents see one file, not the dependency graph |
| [0:43] | GitNexus builds a knowledge graph: every call, import, inheritance, execution flow |
| [1:47] | GitNexus vs Graphify — Graphify is a Claude skill (conversation-scoped, ephemeral); GitNexus is industrial (persistent graph DB, MCP server, multi-agent) |
| [2:49] | Install: `npx gitnexus analyze` — tree-sitter parsing, community detection, BM25 + embeddings |
| [3:32] | Auto-generates AGENTS.md + 4 skill files (exploring, debugging, impact analysis, refactoring) |
| [04:32] | MCP setup: add `gitnexus` block to opencode.json, type=local, command=`git nexus mcp` |
| [05:40] | 11 tools: query, context, impact, detect_changes, rename, cypher, etc. |
| [06:06] | Web UI: force-directed graph, symbol search, Cypher queries, chat via LangChain ReAct agent |

## Details

GitNexus addresses a fundamental limitation of current coding agents: they operate file-by-file without understanding cross-file dependencies. When an agent refactors a function, it has no way to know what breaks downstream.

The solution is a precomputed knowledge graph stored locally in a `.gitnexus` folder using LadybugDB (a graph database). The graph captures:
- Function calls and method invocations across files
- Import chains and dependency graphs
- Class inheritance hierarchies
- Community clusters of related code
- Execution flows from entry points to leaf nodes

This graph is then exposed via an MCP server that any compatible agent can query. The key insight: "even smaller models start performing like the big ones because the heavy lifting is done by the precomputed index, not the model's reasoning."

Compared to Graphify (another codebase graphing tool), GitNexus is deeper: it uses a real graph database, persists to disk, serves over MCP to any agent, and supports hybrid search (BM25 + semantic). Graphify lives in the conversation context and is ephemeral.

## Notable Quotes

> "Most agents fail on big refactors because they only see the file they're editing. With these tools, they can ask the graph first, plan the change, and then execute." — AI Stack Engineer

> "Even smaller models start performing like the big ones because the heavy lifting is done by the precomputed index, not the model's reasoning." — AI Stack Engineer

## Related Entries
- [[graphify-llm-wiki]]
- [[gnosis-mcp]]
- [[agentic-ai-coding-patterns-tornhill]]
- [[claude-code-agentic-loop]]

---
<!-- RU -->

## Краткое описание

GitNexus индексирует всю кодовую базу в локальный граф знаний (LadybugDB) и предоставляет его кодинговым агентам через MCP. Даёт агентам архитектурную осведомлённость — вызовы, наследование, анализ влияния — чтобы они перестали делать слепые правки, молчаливо ломающие продакшен.

## Ключевые идеи
- **Проблема слепых правок:** Кодинговые агенты читают файлы по одному; не знают, что 40 других мест зависят от результата функции. Правки выглядят чисто в диффе, но молча ломаются в продакшене
- **Граф знаний из кода:** Обходит дерево файлов, парсит tree-sitter'ом, извлекает функции/классы, разрешает импорты, трассирует наследование, запускает detection сообществ, отслеживает потоки выполнения
- **Гибридный поисковый индекс:** BM25 + семантические эмбеддинги поверх графа, всё локально, без сетевых вызовов
- **11 MCP-инструментов на репозиторий + 5 для групп репозиториев:** query, context (360° обзор символа), impact (анализ радиуса поражения), detect_changes, rename, cypher
- **Автогенерация навыков:** Создаёт AGENTS.md, claude.md и 4 файла навыков (exploring, debugging, impact analysis, refactoring)
- **Поддержка 14 языков:** TypeScript, JavaScript, Python, Java, Kotlin, C#, Go, Rust, PHP, Ruby, Swift, C, C++, Dart
- **Работает с любым MCP-совместимым агентом:** OpenCode, Claude Code, Cursor, Windsurf, Codex
- **Web UI:** Интерактивный граф, поиск символов, Cypher-запросы, чат с кодовой базой через LangChain ReAct
- **36K+ звёзд на GitHub**, лицензия PolyForm non-commercial, Docker-образы подписаны cosign
- **Переиндексация:** 30-60 секунд на среднем репозитории

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [0:00] | Проблема слепых правок: агенты видят один файл, не граф зависимостей |
| [0:43] | GitNexus строит граф знаний: все вызовы, импорты, наследование, потоки выполнения |
| [1:47] | GitNexus vs Graphify — Graphify — навык Claude (в контексте разговора), GitNexus — промышленный (постоянная БД, MCP, мультиагентный) |
| [2:49] | Установка: `npx gitnexus analyze` — tree-sitter, community detection, BM25 + эмбеддинги |
| [3:32] | Автогенерация AGENTS.md + 4 файла навыков |
| [04:32] | Настройка MCP: блок `gitnexus` в opencode.json, type=local |
| [05:40] | 11 инструментов: query, context, impact, detect_changes, rename, cypher |
| [06:06] | Web UI: граф, поиск, Cypher-запросы, чат через LangChain ReAct |

## Подробнее

GitNexus решает фундаментальное ограничение текущих кодинговых агентов: они работают файл за файлом без понимания межфайловых зависимостей. Ключевое наблюдение: «даже маленькие модели начинают работать как большие, потому что основная нагрузка ложится на предвычисленный индекс, а не на рассуждения модели».

## Примечательные цитаты

> «Большинство агентов проваливают большие рефакторинги, потому что видят только редактируемый файл. С этими инструментами они могут сначала спросить граф, спланировать изменение и затем выполнить» — AI Stack Engineer

## Связанные записи
- [[graphify-llm-wiki]]
- [[gnosis-mcp]]
- [[agentic-ai-coding-patterns-tornhill]]
- [[claude-code-agentic-loop]]
