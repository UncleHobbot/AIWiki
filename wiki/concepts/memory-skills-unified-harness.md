---
title: "Memory and Skills Are the Same Harness"
title_ru: "Память и навыки — это один жгут"
category: concepts
tags: [agent, harness, memory, skills, plugins, claude-code, architecture, context-assembly]
aliases: [memory is not a plugin, skills harness, unified harness]
confidence: medium
updated: 2026-05-18
sources:
  - https://x.com/tricalt/status/2055876832797581406
  - https://towardsdatascience.com/unified-agentic-memory-across-harnesses-using-hooks/
  - https://mcpmarket.com/tools/skills/harness-memory-manager
---

## Summary
Memory and skills are not bolt-on plugins layered on top of an agent harness — they are the harness itself, expressed through the same underlying mechanism: structured markdown context files, hooks, and tool schemas that the agent loop reads at invocation time.

## Key Ideas
- The common mental model — "add a memory plugin, add a skills plugin" — treats memory and skills as optional extras. The more accurate model is that they are the same harness layer, differing only in what they persist (state vs. behavior).
- **Memory** = harness state: what the agent knows about the current user, project, or session, written as markdown and injected into context.
- **Skills** = harness behavior: what the agent knows how to do, written as markdown instructions and injected into context at invocation.
- Both use the same underlying format (CLAUDE.md-style markdown with YAML frontmatter), the same injection path (system prompt or context prepend), and the same hook mechanism — making them interchangeable layers of the same harness.
- This has a practical consequence: memory and skills can be made **harness-agnostic**. The same markdown files work across Claude Code, Codex, Cursor, and Opencode because the harness contract is just "inject these files."
- Treating them as separate plugins creates unnecessary abstraction; treating them as one harness makes the architecture simpler and more portable.

## Details

### Why the Plugin Mental Model Fails

When memory and skills are framed as plugins, they imply a host system that you extend. This leads to per-harness implementations that are not portable, and to architectures where the agent "loads" memory from a database at runtime rather than having memory baked into its context assembly.

The alternative view: the harness is the full assembly of everything the model sees and can do. Memory files (e.g. `profile/role.md`, `project/context.md`) and skill files (e.g. `.claude/commands/wiki-reddit.md`) are both just files that the harness injects. Separating them into "core" vs. "plugin" is a naming convention, not an architectural boundary.

### Unified Harness Format in Practice

Projects like `everything-claude-code` demonstrate this principle: memory and skills share the same markdown wiki format with semantic paths and YAML frontmatter. The path determines the injection order and scope; the content determines whether it reads as state (memory) or instruction (skill). The harness loop treats them identically.

This architecture also enables **harness-agnostic memory**: the same `profile/role.md` works in Claude Code and Opencode without conversion, because both harnesses implement the same context-injection contract.

### Consequence for Harness Design

If memory and skills are the same layer, harness design simplifies to one question: *what should be in context at each invocation?* The answer includes both persistent state (memory) and persistent behavior (skills), managed together as a single context assembly problem rather than two separate plugin systems.

## Related Entries
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[claude-code-frameworks]] ([Claude Code Skill Frameworks](../tools/claude-code-frameworks.md))
- [[opensddrag-mcp-harness]] ([OpenSddRag: MCP Server with Persistent Rules Harness for Coding Agents](../tools/opensddrag-mcp-harness.md))
- [[ai-rules-modular-instructions]] ([ai-rules: Modular, Reusable AI Instruction Files Instead of One Giant AGENTS.md](../tools/ai-rules-modular-instructions.md))

---
<!-- RU -->

## Краткое описание
Память и навыки агента — это не плагины поверх жгута (harness), а сам жгут, выраженный через один и тот же механизм: структурированные markdown-файлы, хуки и схемы инструментов, которые агентный цикл читает при вызове.

## Ключевые идеи
- Распространённая ментальная модель «добавить плагин памяти, добавить плагин навыков» рассматривает их как необязательные надстройки. Более точная модель: это один и тот же слой жгута, отличающийся лишь тем, что сохраняется — состояние (память) или поведение (навыки).
- **Память** = состояние жгута: что агент знает о пользователе, проекте или сессии — записано как markdown и подставляется в контекст.
- **Навыки** = поведение жгута: что агент умеет делать — записано как markdown-инструкции и подставляется в контекст при вызове.
- Оба используют одинаковый формат (markdown в стиле CLAUDE.md с YAML frontmatter), один путь инъекции (системный промпт или prepend контекста) и один механизм хуков — что делает их взаимозаменяемыми слоями одного жгута.
- Практическое следствие: память и навыки можно сделать **агностичными к жгуту**. Одни и те же markdown-файлы работают в Claude Code, Codex, Cursor и Opencode, поскольку контракт жгута — просто «инъецировать эти файлы».
- Трактовка их как отдельных плагинов создаёт лишнюю абстракцию; трактовка как единого жгута упрощает архитектуру и делает её переносимой.

## Подробнее

### Почему модель плагинов не работает

Когда память и навыки оформляются как плагины, подразумевается хост-система, которую расширяют. Это ведёт к per-harness-реализациям без переносимости и к архитектурам, где агент «загружает» память из базы данных во время выполнения, а не получает её в сборке контекста.

Альтернативный взгляд: жгут — это полная сборка всего, что модель видит и может делать. Файлы памяти (`profile/role.md`, `project/context.md`) и файлы навыков (`.claude/commands/wiki-reddit.md`) — просто файлы, которые жгут инъецирует. Разделение на «ядро» и «плагин» — соглашение об именовании, а не архитектурная граница.

### Единый формат жгута на практике

Проекты вроде `everything-claude-code` демонстрируют этот принцип: память и навыки используют один markdown-формат с семантическими путями и YAML frontmatter. Путь определяет порядок инъекции и область видимости; содержимое определяет, читается ли файл как состояние (память) или инструкция (навык). Цикл жгута обрабатывает их одинаково.

Эта архитектура также обеспечивает **агностичную память**: один и тот же `profile/role.md` работает в Claude Code и Opencode без конвертации, поскольку оба реализуют один контракт инъекции контекста.

### Следствие для проектирования жгута

Если память и навыки — один слой, проектирование жгута сводится к одному вопросу: *что должно быть в контексте при каждом вызове?* Ответ включает как постоянное состояние (память), так и постоянное поведение (навыки), управляемые вместе как единая задача сборки контекста, а не две отдельные системы плагинов.

## Связанные записи
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[claude-code-frameworks]] ([Claude Code Skill Frameworks](../tools/claude-code-frameworks.md))
- [[opensddrag-mcp-harness]] ([OpenSddRag: MCP-сервер с постоянным движком правил для coding-агентов](../tools/opensddrag-mcp-harness.md))
- [[ai-rules-modular-instructions]] ([ai-rules: Modular, Reusable AI Instruction Files Instead of One Giant AGENTS.md](../tools/ai-rules-modular-instructions.md))
