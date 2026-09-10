---
title: "JetBrains as an Agentic Platform — MCP Server, Junie, and the Open-IDE Turn"
title_ru: "JetBrains как агентная платформа — MCP-сервер, Junie и открытие IDE сторонним агентам"
category: research
tags: [jetbrains, mcp, idea, rider, junie, acp, ai-assistant, intellij, agent-tools]
aliases: [JetBrains MCP, JetBrains MCP server, IDEA MCP, Rider MCP, JetBrains agent]
confidence: high
updated: 2026-09-03
sources:
  - https://www.jetbrains.com/help/idea/mcp-server.html
  - https://www.jetbrains.com/help/rider/mcp-server.html
  - https://github.com/JetBrains/mcp-jetbrains
  - https://github.com/JetBrains/mcp-server-plugin
  - https://blog.jetbrains.com/idea/2025/05/intellij-idea-2025-1-model-context-protocol/
  - https://blog.jetbrains.com/ai/2025/09/introducing-claude-agent-in-jetbrains-ides/
  - https://blog.jetbrains.com/ai/2026/01/acp-agent-registry/
  - https://blog.jetbrains.com/ai/2026/06/github-copilot-now-an-integrated-agent/
  - https://blog.jetbrains.com/junie/2026/04/junie-cli-inside-your-jb-ide/
  - https://www.jetbrains.com/help/ai-assistant/junie-agent.html
  - https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html
  - https://youtrack.jetbrains.com/issues/IJPL-200926
  - https://devblogs.microsoft.com/java/unlocking-mcp-in-jetbrains-how-copilot-uses-sampling-prompts-resources-and-elicitation/
  - https://blog.jetbrains.com/idea/2026/08/how-to-use-ai-agents-in-intellij-idea-with-acp/
---

## Summary

JetBrains took a two-sided bet on agentic coding: **expose the IDE itself as an MCP server** so any external agent (Claude Code, Codex, Copilot CLI) can drive IDEA/Rider's deep capabilities — semantic refactoring, IDE-aware error analysis, run configurations, even the debugger — and simultaneously **open the IDE to third-party agents** via the Agent Client Protocol (ACP, co-created with Zed), its own agent (Junie), and BYOK. Since IDE 2025.2 the MCP Server is bundled and enabled in all IntelliJ-based IDEs; since 2025.1 the IDE is also an MCP *client*. The result: a terminal agent pointed at Rider gets the IDE's 25-year code-intelligence investment as tools.

## Key Ideas

- **Two MCP roles.** JetBrains IDEs are both an MCP *client* (AI Assistant consumes external MCP servers, since 2025.1) and an MCP *server* (the IDE exposes ~50 tools to any MCP client, since 2025.2, bundled by default).
- **Architecture evolution:** the 2025.1-era standalone Node proxy (`@jetbrains/mcp-proxy`, now deprecated) translated MCP stdio into plain HTTP against the IDE's built-in webserver (`127.0.0.1:63342/api/mcp/...`, scanning ports 63342–63352 for multiple IDE instances). From 2025.2 the plugin is bundled and speaks SSE/HTTP-stream directly, with a JVM stdio proxy for legacy clients.
- **The tool surface is the differentiator.** Unlike most MCP servers that wrap files and shell, JetBrains exposes *semantic IDE operations*: `rename_refactoring` (true semantic rename vs grep+sed), `get_file_problems` (IDE error analysis, not compiler output), `search_symbol` (semantic symbol search incl. SDK/library symbols), `analyze_calls` (call hierarchy), `build_project` (structured compiler diagnostics), run configurations, and a full **debugger toolset** (`xdebug_*`: breakpoints, stack frames, variable setting, expression evaluation).
- **The strategic turn:** JetBrains stopped fighting terminal agents and invited them in — Claude Agent integrated into AI chat (Sept 2025), Codex as an agent (docs), GitHub Copilot as an "integrated agent" (June 2026), all speaking ACP, with an Agent Registry (Jan 2026) and IDE auto-configuration for Claude Code/Codex/VS Code/Junie/Copilot CLI.
- **Security posture is default-open-but-scary:** the MCP server binds to 127.0.0.1 (after a YouTrack fix that moved it off `0.0.0.0`) but has **no token auth** — any local process can invoke IDE tools including `execute_terminal_command`; per-tool enable/disable, "brave mode," and a "Router-only" scoping are the mitigation knobs.
- **Junie + credits:** JetBrains' own agent shares one AI-credit pool with AI Assistant; agentic use burns credits fast — community reports ~1/12 of an AI Pro monthly quota per task (Tier 3).

## The MCP Server Story in Detail

### Architecture: two generations

**Legacy (2025.1 era, deprecated):** `MCP client → stdio → NPM proxy → HTTP → IDE built-in webserver → MCP Server plugin`. The proxy defined zero tools itself — it fetched the tool catalog live from the IDE every 10 seconds and re-emitted `tools/list_changed` when plugins changed it. IDE-side required the MCP Server plugin (Marketplace ID 26071).

**Current (2025.2+):** the MCP Server plugin ships **bundled and enabled** in every IntelliJ-based IDE. Enable via `Settings | Tools | MCP Server` → "Enable MCP Server" (an access dialog discloses what third-party apps get). No Node proxy needed — SSE/HTTP-stream transports are native, with a JVM proxy for stdio clients. Third-party IDE plugins can register additional MCP tools via an extension-point system.

Client onboarding is largely automated: the IDE **auto-configures** Junie, VS Code, Claude Code, Codex, Air, and GitHub Copilot CLI (writes each client's config), and shows terminal-session setup banners when Claude Code/Codex starts in the IDE terminal unconfigured. For other clients there are copy buttons for SSE / Stdio / HTTP-stream configs.

### The tool surface (verified, IDEA/Rider 2026.2 docs)

| Group | Tools |
|---|---|
| Analysis | `get_file_problems`, `build_project`, `analyze_calls`, `lint_files`, `get_project_modules`, `get_project_dependencies` |
| Search | `search_file` (glob), `search_text`, `search_regex`, `search_symbol` (semantic, incl. external SDK symbols), `skill_search` (unified) |
| Read/Write | `read_file` (slice/lines/offsets modes; decompiles jars), `apply_patch` (Codex or unified-diff format), `create_new_file`, `reformat_file`, `open_file_in_editor`, `list_directory_tree` |
| Refactoring | `rename_refactoring` — semantic rename across the index, the flagship vs-text-tools differentiator |
| Run/Exec | `get_run_configurations`, `execute_run_configuration` (one-off arg/env overrides), `execute_terminal_command` (IDE terminal, 2000-line cap, confirmation-gated) |
| Debugger (`xdebug_*`) | `set_breakpoint` (conditions, tracepoints), `control_session` (step/resume), `get_stack`, `get_frame_values`, `set_variable`, `evaluate_expression`, `start_debugger_session` |
| Database (DataGrip-grade) | `introspect_schema`, `execute_sql_query` (CSV results), `preview_table_data`, `list_database_connections`, + 10 more |
| VCS | `get_repositories`, `git_status` |
| Router | `execute_tool` — invoke any IDE MCP tool from a command-line string |
| Inspection SDK | `run_inspection_kts`, `generate_psi_tree`, + Kotlin DSL inspection tooling |

### Rider specifics

Rider ships the identical toolset (docs confirm). For .NET work the high-value tools are `execute_run_configuration` (build/run/test through Rider's run engine instead of raw shell), `get_run_configurations` with `filePath` (discovers "run points" — test/main entry points), and `build_project` (structured compiler diagnostics, not console scraping). Debugger tools use the cross-platform XDebugger API, so `xdebug_*` works in Rider. No Unity-specific MCP tools exist in official docs.

## The Broader Ecosystem: How Agents Use JetBrains Products

### Junie — the in-house agent
Autonomous multi-step agent inside AI Chat (and a standalone **Junie CLI** for terminal/CI; **Junie Local** runs credits-free on an M5 Mac). Reads root `AGENTS.md`, respects `.aiignore`, consumes MCP servers as tools, has a Debug mode that attaches to live debugger sessions (IDEA Ultimate 2026.1.1+). Permission model: confirm-by-default with per-action "Always allow," **Brave mode** (skip all confirmations), and rollback. GA April 2025; out of beta June 2026. Credits: shared pool with AI Assistant; community reports ~1/12 of an AI Pro monthly quota per task (Tier 3).

### AI Assistant + BYOK
Cloud models (Claude/GPT/Gemini historically) + local models (Ollama, LM Studio) + **BYOK live since Dec 2025** (Anthropic, OpenAI, any OpenAI-compatible endpoint). AI credits: Free 3, Pro $20/mo = 20 credits, Ultimate $60/mo = 70 (pricing changed between 2025's $100/$300 annual and 2026's monthly tiers — cite with dates). 1 credit ≈ 10 chat code-gen requests.

### ACP — the "LSP for AI coding agents"
Co-created with Zed: any ACP-implementing agent plugs into JetBrains IDEs (and Zed) without a bespoke plugin. Claude Agent (Sept 2025), Codex, Gemini, GitHub Copilot (June 2026) are integrated agents; the ACP Agent Registry (Jan 2026) is the installable directory. Anthropic also ships a dedicated Claude Code JetBrains plugin (beta) with native diff views.

### Security: the localhost trade-off
YouTrack IJPL-200926 records the move from `0.0.0.0` to `127.0.0.1` binding — the server previously listened on all interfaces (broke WSL2 access as a side effect). But there is **no token authentication**: any local process can hit the endpoint and invoke tools up to `execute_terminal_command` — the exact "untrusted local process" class this wiki tracks in [[mcp-tool-poisoning-microsoft]] and [[amazon-q-mcp-config-rce]]. Mitigations in-product: per-tool enable/disable, confirmation gating (non-brave mode), and Router-only scoping. No CVE specifically against the JetBrains MCP server was found as of this writing.

### vs VS Code
VS Code embeds a native MCP client in the editor; JetBrains' client-side support lives in AI Assistant while its "any agent in any editor" play is ACP (agent↔editor protocol, vs MCP's agent↔tools). Community sentiment (Tier 3) says VS Code/Codex is ahead for pure agentic workflows, while JetBrains' unique asset is *deep IDE semantics* — semantic rename, inspections, PSI analysis — that text-file-based agents can't replicate.

## Notable Quotes

> "A harness for your AI harnesses" describes T3 Code — but "an MCP server for your agents" is what JetBrains shipped for the IDE itself. — this wiki's synthesis

## Honest Gaps

- The current (2025.2+) SSE endpoint URL and port range are not documented; ports 63342–63352 are verified only from the deprecated proxy's source.
- The legacy plugin-era tool list (`get_problem`, `search_in_files`, `replace_file_text`, `execute_action`) is community-sourced; only `get_file_text_by_path` is YouTrack-confirmed.
- JetBrains Air claims rest on secondary sources; no primary JetBrains page was verified.
- "Cursor running inside IDEA 2026.1" is a single Medium post — unverified.
- Per-task credit consumption of Junie is Tier 3 (single-user reports).

## Related Entries

- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))
- [[mcp-stateless-core-spec]] ([MCP 2026-07-28 Spec](../news/mcp-stateless-core-spec.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](../news/amazon-q-mcp-config-rce.md))
- [[mcpg-postgresql-mcp-server]] ([MCPg PostgreSQL MCP Server](../tools/mcpg-postgresql-mcp-server.md))
- [[github-copilot-jetbrains-native]] ([Copilot Natively Integrated into JetBrains](../news/github-copilot-jetbrains-native.md))
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](../news/duneslide-cursor-sandbox-escape.md))
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK](../agents/mcp-vs-adk-agent-connectivity.md))

---
<!-- RU -->

## Краткое описание

JetBrains сделали двухстороннюю ставку на агентный кодинг: **открыть саму IDE как MCP-сервер**, чтобы любой внешний агент (Claude Code, Codex, Copilot CLI) мог управлять глубинными возможностями IDEA/Rider — семантическим рефакторингом, IDE-анализом ошибок, run-конфигурациями и даже отладчиком, — и одновременно **открыть IDE сторонним агентам** через Agent Client Protocol (ACP, создан с Zed), собственного агента Junie и BYOK. Начиная с IDE 2025.2 MCP-сервер предустановлен во всех IDE на IntelliJ; с 2025.1 IDE также является MCP-*клиентом*. Результат: терминальный агент, направленный на Rider, получает 25-летнюю инвестицию JetBrains в кодоинтеллект как набор инструментов.

## Ключевые идеи

- **Две роли MCP.** IDE JetBrains — одновременно MCP-*клиент* (AI Assistant потребляет внешние MCP-серверы, с 2025.1) и MCP-*сервер* (IDE открывает ~50 инструментов любому MCP-клиенту, с 2025.2, предустановлен).
- **Эволюция архитектуры:** отдельный Node-прокси 2025.1 (`@jetbrains/mcp-proxy`, устарел) транслировал MCP stdio в обычный HTTP к встроенному веб-серверу IDE (`127.0.0.1:63342/api/mcp/...`, сканирование портов 63342–63352 для нескольких инстансов IDE). С 2025.2 плагин предустановлен и говорит по SSE/HTTP-stream напрямую.
- **Поверхность инструментов — главный дифференциатор.** В отличие от большинства MCP-серверов, оборачивающих файлы и шелл, JetBrains открывает *семантические операции IDE*: `rename_refactoring` (истинное семантическое переименование против grep+sed), `get_file_problems` (IDE-анализ ошибок), `search_symbol` (семантический поиск, включая SDK-символы), `analyze_calls` (иерархия вызовов), `build_project` (структурированная диагностика компилятора), run-конфигурации и полный **набор отладчика** (`xdebug_*`).
- **Стратегический поворот:** JetBrains перестали воевать с терминальными агентами и пригласили их — Claude Agent в AI-чате (сент. 2025), Codex как агент, GitHub Copilot как «интегрированный агент» (июнь 2026), все через ACP с реестром агентов (янв. 2026) и авто-конфигурацией IDE.
- **Безопасность по умолчанию открыта, но пугает:** сервер привязан к 127.0.0.1 (после фикса YouTrack, ушедшего с `0.0.0.0`), но **без токен-аутентификации** — любой локальный процесс может вызвать инструменты вплоть до `execute_terminal_command`.
- **Junie и кредиты:** собственный агент JetBrains делит пул AI-кредитов с AI Assistant; агентное использование сжигает кредиты быстро (~1/12 месячной квоты AI Pro за задачу — уровень 3).

## MCP-сервер подробно

### Архитектура: два поколения

**Легаси (2025.1, устарел):** клиент → stdio → NPM-прокси → HTTP → встроенный веб-сервер IDE → плагин MCP Server. Прокси сам не определял ни одного инструмента — каталог получался живьём из IDE каждые 10 секунд. **Актуально (2025.2+):** плагин предустановлен; включается через `Settings | Tools | MCP Server`; сторонние плагины регистрируют свои MCP-инструменты через extension points. IDE **авто-конфигурирует** Junie, VS Code, Claude Code, Codex, Air и GitHub Copilot CLI.

### Поверхность инструментов (верифицировано, доки 2026.2)

Анализ: `get_file_problems`, `build_project`, `analyze_calls`, `lint_files`. Поиск: `search_file`, `search_text`, `search_regex`, `search_symbol` (семантический). Чтение/запись: `read_file` (с декомпиляцией jar), `apply_patch`, `reformat_file`. Рефакторинг: `rename_refactoring` — флагманский инструмент против текстовых утилит. Запуск: `get_run_configurations`, `execute_run_configuration`, `execute_terminal_command`. Отладчик (`xdebug_*`): брейкпоинты с условиями и tracepoints, стек, значения кадров, установка переменных, вычисление выражений. База данных (уровня DataGrip): `introspect_schema`, `execute_sql_query`, `preview_table_data` и ещё 10. VCS: `get_repositories`, `git_status`. Роутер: `execute_tool`.

### Специфика Rider

Rider несёт идентичный набор инструментов. Для .NET наиболее ценные: `execute_run_configuration` (сборка/запуск/тесты через run-движок Rider вместо сырого шелла), `get_run_configurations` с `filePath` (находит «run points» — точки входа тестов и main), `build_project` (структурированная диагностика компилятора). Инструменты отладчика используют кроссплатформенный XDebugger API, поэтому `xdebug_*` работает и в Rider. Unity-специфичных MCP-инструментов в официальных доках нет.

## Экосистема: как агенты используют продукты JetBrains

### Junie — собственный агент
Автономный многошаговый агент внутри AI-чата (+ отдельный Junie CLI для терминала/CI; Junie Local — без кредитов на M5 Mac). Читает `AGENTS.md`, соблюдает `.aiignore`, потребляет MCP-серверы как инструменты, есть режим отладки с подключением к живой сессии. Разрешения: подтверждение по умолчанию, Brave mode, откат изменений. GA в апреле 2025; из беты — июнь 2026. Кредиты: общий пул с AI Assistant.

### AI Assistant + BYOK
Облачные модели (Claude/GPT/Gemini) + локальные (Ollama, LM Studio) + **BYOK с декабря 2025**. Кредиты: Free 3, Pro $20/мес = 20 кредитов, Ultimate $60/мес = 70 (цены менялись между 2025 и 2026 — цитировать с датами).

### ACP — «LSP для ИИ-кодинг-агентов»
Создан с Zed: любой ACP-совместимый агент подключается к JetBrains IDE без специализированного плагина. Claude Agent (сент. 2025), Codex, Gemini, GitHub Copilot (июнь 2026) — интегрированные агенты; реестр агентов ACP — с января 2026. У Anthropic есть и отдельный плагин Claude Code для JetBrains (бета) с нативным просмотром диффов.

### Безопасность: компромисс localhost
YouTrack IJPL-200926 фиксирует переход с `0.0.0.0` на `127.0.0.1` — сервер ранее слушал все интерфейсы (заодно сломав WSL2). Но **токен-аутентификации нет**: любой локальный процесс может дёрнуть инструменты вплоть до `execute_terminal_command` — тот же класс «недоверенный локальный процесс», что в [[mcp-tool-poisoning-microsoft]] и [[amazon-q-mcp-config-rce]]. Смягчения в продукте: отключение инструментов, гейты подтверждений, Router-only скоупинг. Специфичного для JetBrains MCP-сервера CVE не найдено.

### против VS Code
VS Code встроил нативный MCP-клиент в редактор; клиентская поддержка JetBrains живёт в AI Assistant, а ставка «любой агент в любом редакторе» — это ACP. Оценки сообщества (уровень 3) отдают VS Code/Codex впереди в чисто агентных воркфлоу, но уникальный актив JetBrains — *глубокая семантика IDE*, которую текстовые агенты не повторят.

## Честные пробелы

- Актуальный (2025.2+) URL и порт SSE-эндпоинта не документированы; диапазон 63342–63352 верифицирован только по исходникам устаревшего прокси.
- Легаси-список инструментов (`get_problem`, `search_in_files` и др.) — из сообщества; подтверждён YouTrack'ом только `get_file_text_by_path`.
- Заявления о JetBrains Air опираются на вторичные источники.
- «Cursor внутри IDEA 2026.1» — единичный пост на Medium, не верифицирован.
- Расход кредитов Junie за задачу — уровень 3 (единичные сообщения).

## Связанные записи

- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))
- [[mcp-stateless-core-spec]] ([MCP 2026-07-28 Spec](../news/mcp-stateless-core-spec.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](../news/amazon-q-mcp-config-rce.md))
- [[mcpg-postgresql-mcp-server]] ([MCPg PostgreSQL MCP Server](../tools/mcpg-postgresql-mcp-server.md))
- [[github-copilot-jetbrains-native]] ([Copilot Natively Integrated into JetBrains](../news/github-copilot-jetbrains-native.md))
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](../news/duneslide-cursor-sandbox-escape.md))
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK](../agents/mcp-vs-adk-agent-connectivity.md))
