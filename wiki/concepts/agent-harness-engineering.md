---
title: "Agent Harness Engineering"
title_ru: "Инженерия агентных жгутов"
category: concepts
tags: [agent, harness, scaffolding, context-assembly, tools, claude-code, github-copilot, vscode, coding-agent]
date: 2026-05-15
updated: 2026-05-17
sources:
  - https://www.oreilly.com/radar/agent-harness-engineering/
  - https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode
---

## Summary
Agent harness engineering is the discipline of designing the scaffolding around a language model — prompts, tools, context policies, hooks, subagents, feedback loops, and recovery paths — that turns a raw model into a working agent. A decent model with a great harness consistently beats a great model with a bad harness.

## Key Ideas
- **Agent = Model + Harness.** The model is one input; the harness is everything else. If you're not the model, you're the harness.
- The harness has four core responsibilities: **context assembly** (what the model sees), **tool exposure** (what it can do), **agent loop** (how it runs and recovers), and **evaluation** (how you know it's working).
- The defining harness engineering principle: *"Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."* — Addy Osmani (O'Reilly Radar)
- In VS Code/GitHub Copilot, the coding harness assembles context before every request: system instructions, user query, workspace structure, conversation history, tool results, custom instructions, and session memory — all filtered and structured by the harness, not by the model.
- Tool exposure is a design decision: the harness declares the tools and their JSON schemas; the model picks from the declared menu. Giving an agent too many tools is as harmful as giving it too few.

## Details

### The Harness vs. The Model Debate

For two years the developer community focused on model comparison: which model is smartest, which hallucinates less, which writes cleaner code. Addy Osmani's 2026 O'Reilly Radar piece argues this misses half the system. The model is stateless; the harness maintains state, decides what context to include in each call, manages recovery when tool calls fail, and encodes the institutional memory of what approaches work.

The practical implication: model upgrades often matter less than harness improvements. Switching from one frontier model to another might yield a 10–15% quality improvement; improving the harness — tightening context assembly, adding a verification loop, defining clearer tool schemas — can yield 30–50%.

### The VS Code Coding Harness

GitHub's May 2026 blog post describes the actual harness behind Copilot in VS Code, written by the VS Code team (Julia Kasper, Megan Rogge, Aaron Munger):

1. **Context assembly**: before any model call, the harness builds a prompt from system instructions + user query + workspace structure (languages, frameworks, open editors) + conversation history + tool results + custom instructions + memory. The harness, not the model, decides what to include. This is the highest-leverage design decision.

2. **Tool exposure**: the harness declares tools (`read_file`, `replace_string_in_file`, `apply_patch`, `run_in_terminal`, `semantic_search`, etc.) with JSON schemas. The model produces tool call arguments; the harness validates, executes, and feeds results back.

3. **Agent loop**: the harness manages the request-response-toolcall cycle. A key harness responsibility is **recovery** — when a tool call fails or a generated diff doesn't apply cleanly, the harness decides whether to retry, explain the failure to the model, or escalate to the user.

4. **Evaluation**: as models change (new releases, fine-tunes), the harness must be re-evaluated against real workflows. The harness is the stable interface; the model underneath can be swapped.

### Harness Engineering in Practice

In Claude Code and similar agentic coding tools, CLAUDE.md files and skills are the practical expression of harness engineering. The CLAUDE.md defines:
- System-level context the model always receives
- Tool usage conventions
- Verification requirements before marking work done
- Recovery patterns for common failures

Skills and hooks are the iterative improvement layer: each skill encodes a lesson from a past failure, making the agent reliably handle that class of problem in the future. This is exactly Osmani's definition: "engineer a solution such that the agent never makes that mistake again."

## Notable Quotes
> "A decent model with a great harness beats a great model with a bad harness." — Addy Osmani

> "The model is one input into a running agent. The rest is the harness." — Addy Osmani, O'Reilly Radar

## Related Entries
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[specs-to-production-ai-agents]] ([From Specs to Production: Building Software with AI Agents End to End](../agents/specs-to-production-ai-agents.md))
- [[acdc-agent-centric-development-cycle]] ([AC/DC — Agent-Centric Development Cycle](../agents/acdc-agent-centric-development-cycle.md))
- [[memory-skills-unified-harness]] ([Memory and Skills Are the Same Harness](../concepts/memory-skills-unified-harness.md))
- [[ab-method-workflow]] ([ab-method: Domain-Grounded Planning Workflow for Claude Code and Codex](../tools/ab-method-workflow.md))
- [[verifier-tax-tool-agent-safety]] ([The Verifier Tax: Safety-Success Tradeoffs in Tool-Using LLM Agents](../concepts/verifier-tax-tool-agent-safety.md))
- [[opensddrag-mcp-harness]] ([OpenSddRag: MCP Server with Persistent Rules Harness for Coding Agents](../tools/opensddrag-mcp-harness.md))
---
<!-- RU -->

## Краткое описание
Инженерия агентных жгутов (harness engineering) — дисциплина проектирования каркаса вокруг языковой модели: промпты, инструменты, политики контекста, хуки, суб-агенты, петли обратной связи и пути восстановления. Всё это превращает «сырую» модель в рабочего агента. Хорошая модель с отличным жгутом стабильно превосходит отличную модель с плохим жгутом.

## Ключевые идеи
- **Агент = Модель + Жгут (Harness).** Модель — один из входных сигналов; жгут — всё остальное. Если вы не модель, вы — жгут.
- У жгута четыре ключевые обязанности: **сборка контекста** (что видит модель), **предоставление инструментов** (что она может делать), **агентный цикл** (как он работает и восстанавливается) и **оценка** (как понять, что всё работает).
- Определяющий принцип: *«Каждый раз, когда агент совершает ошибку, вы находите решение, исключающее повторение этой ошибки»* — Эдди Османи (O'Reilly Radar).
- В VS Code/GitHub Copilot жгут собирает контекст перед каждым запросом: системные инструкции, запрос пользователя, структура рабочего пространства, история разговора, результаты инструментов — всё это фильтрует жгут, а не модель.
- Предоставление инструментов — проектное решение: жгут объявляет инструменты и их JSON-схемы; модель выбирает из предложенного меню. Слишком много инструментов вредит не меньше, чем слишком мало.

## Подробнее

### Жгут против модели

Два года сообщество фокусировалось на сравнении моделей. Статья Эдди Османи 2026 года в O'Reilly Radar указывает: это упускает половину системы. Модель не имеет состояния; жгут поддерживает состояние, решает, какой контекст включить в каждый вызов, управляет восстановлением при сбоях инструментов и кодирует институциональную память об успешных подходах.

Практический вывод: обновления моделей часто важны меньше, чем улучшения жгута. Смена одной frontier-модели на другую даёт 10–15% прироста качества; улучшение жгута — плотная сборка контекста, добавление проверочного цикла, более чёткие схемы инструментов — может дать 30–50%.

### Жгут кодирования в VS Code

Майский блогпост GitHub описывает реальный жгут Copilot в VS Code (Julia Kasper, Megan Rogge, Aaron Munger):

1. **Сборка контекста**: перед каждым вызовом модели жгут собирает промпт из системных инструкций + запроса пользователя + структуры рабочего пространства + истории разговора + результатов инструментов + пользовательских инструкций + памяти сессии.
2. **Предоставление инструментов**: жгут объявляет инструменты (`read_file`, `replace_string_in_file`, `run_in_terminal`, `semantic_search` и др.) с JSON-схемами. Модель генерирует аргументы вызова; жгут валидирует, выполняет, возвращает результаты.
3. **Агентный цикл**: жгут управляет циклом запрос-ответ-вызов инструмента. Ключевая обязанность — **восстановление**: если вызов инструмента не удался или сгенерированный diff не применился, жгут решает — повторить, объяснить ошибку модели или эскалировать пользователю.
4. **Оценка**: при смене моделей жгут переоценивается на реальных рабочих процессах. Жгут — стабильный интерфейс; модель под ним можно заменить.

### На практике в Claude Code

CLAUDE.md и навыки — практическое выражение harness engineering. Каждый навык кодирует урок из прошлой ошибки, заставляя агента надёжно обрабатывать этот класс проблем в будущем. Это и есть принцип Османи: «найти решение, исключающее повторение ошибки».

## Связанные записи
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[specs-to-production-ai-agents]] ([From Specs to Production: Building Software with AI Agents End to End](../agents/specs-to-production-ai-agents.md))
- [[acdc-agent-centric-development-cycle]] ([AC/DC — Agent-Centric Development Cycle](../agents/acdc-agent-centric-development-cycle.md))
- [[memory-skills-unified-harness]] ([Memory and Skills Are the Same Harness](../concepts/memory-skills-unified-harness.md))
- [[ab-method-workflow]] ([ab-method: workflow планирования с привязкой к домену для Claude Code и Codex](../tools/ab-method-workflow.md))
- [[verifier-tax-tool-agent-safety]] ([Verifier Tax: компромисс между безопасностью и успехом у tool-using агентов](../concepts/verifier-tax-tool-agent-safety.md))
- [[opensddrag-mcp-harness]] ([OpenSddRag: MCP-сервер с постоянным движком правил для coding-агентов](../tools/opensddrag-mcp-harness.md))
