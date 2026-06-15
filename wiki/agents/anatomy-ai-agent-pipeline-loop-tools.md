---
title: "Anatomy of an AI Agent: Pipeline, Loop, Tools, and Traps"
title_ru: "Анатомия AI-агента: pipeline, цикл, инструменты и ловушки"
category: agents
tags: [ai-agent, agent-architecture, pipeline, agent-loop, mcp, tools-design, guardrails, workflow-vs-agent]
date: 2026-04-03
updated: 2026-05-17
transcript: unavailable
sources:
  - https://www.youtube.com/watch?v=rN4_Y67Tr8I
---

## Summary

Senior-level dissection of AI agent internals: workflow vs agent (7 levels from single LLM call to multi-agent system), 12-stage request processing pipeline, context as the agent's bloodstream (and three errors that kill KV-cache), the agent loop as the most dangerous component, tool design pitfalls with MCP, and system prompts as architectural contracts.

## Key Ideas
- **Workflow vs Agent — 7 levels:** From single LLM call → prompt chaining → routing → parallel → orchestrator-worker → hierarchical → multi-agent. Most teams only need workflow (level 3-4)
- **12-stage request pipeline:** Full processing chain from user input to response, covering validation, routing, context assembly, tool selection, execution, and response synthesis
- **Context as bloodstream:** Three critical errors that kill KV-cache efficiency: oversized context, redundant information, wrong ordering
- **Agent loop is the most dangerous component:** The autonomous reasoning-execution cycle where agents can spiral. Guardrails must be in code, not in prompts
- **Tool design and MCP traps:** Automatic wrapping of functions as MCP tools creates hidden failure modes. Tool interfaces need deliberate design
- **System prompt as architectural contract:** Defines role, priorities, output format, and behavioral examples — not just instructions

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | Workflow vs Agent: 7 levels from simple to multi-agent |
| [~8:00] | Pipeline: 12 stages of request processing |
| [~15:00] | Context as bloodstream — KV-cache errors |
| [~20:00] | Agent loop: the most dangerous component |
| [~25:00] | Tool design and MCP pitfalls |
| [~30:00] | System prompt as architectural contract |

## Details

This video targets senior engineers, tech leads, and architects who want to build AI agents with full awareness of each component rather than blindly trusting frameworks. The "Agent-Barista" example (a coffee-ordering agent) illustrates the same architecture used in coding assistants, DevOps agents, and customer support bots.

The key insight on guardrails: "put them in code, not in prompts." Prompt-based constraints are suggestions the model can ignore; code-level constraints (max iterations, timeout limits, output validation) are guarantees.

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering for AI Agents: From Research to Production Code](../tips/context-engineering-ai-agents-pipeline.md))
- [[agent-operating-system]] ([Agent Operating System](../agents/agent-operating-system.md))
- [[japan-autonomous-medicine-lab-aist]] ([Japan Autonomous Medicine Lab](../news/japan-autonomous-medicine-lab-aist.md))
- [[tool-calling-loop-management]] ([Managing Agentic Tool-Calling Loops: Hard Caps and Model Behavior](../tips/tool-calling-loop-management.md))
---
<!-- RU -->

## Краткое описание

Вскрытие AI-агента по частям для сеньоров: workflow vs agent (7 уровней), 12-stage pipeline обработки запроса, контекст как кровеносная система (три ошибки, убивающие KV-cache), agent loop как самый опасный компонент, ловушки проектирования инструментов в MCP, system prompt как архитектурный контракт.

## Ключевые идеи
- **Workflow vs Agent — 7 уровней:** От одного вызова LLM → мультиагентная система. Большинству команд нужен workflow (уровень 3-4)
- **12-stage pipeline:** Полная цепочка обработки запроса от ввода до ответа
- **Контекст как кровеносная система:** Три критические ошибки, убивающие KV-cache
- **Agent loop — самый опасный компонент:** Guardrails должны быть в коде, а не в промптах
- **Ловушки MCP:** Автоматическая обёртка функций в MCP-инструменты создаёт скрытые режимы отказа
- **System prompt как архитектурный контракт:** Роль, приоритеты, формат, примеры поведения

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [~8:00] | Pipeline: 12 стадий обработки запроса |
| [~15:00] | Контекст как кровеносная система — ошибки KV-cache |
| [~20:00] | Agent loop: самый опасный компонент |
| [~25:00] | Проектирование инструментов и ловушки MCP |
| [~30:00] | System prompt как архитектурный контракт |

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering for AI Agents: From Research to Production Code](../tips/context-engineering-ai-agents-pipeline.md))
- [[agent-operating-system]] ([Agent Operating System](../agents/agent-operating-system.md))
- [[japan-autonomous-medicine-lab-aist]] ([Japan Autonomous Medicine Lab](../news/japan-autonomous-medicine-lab-aist.md))
- [[tool-calling-loop-management]] ([Управление циклами вызова инструментов в агентах: жёсткие ограничения и поведение моделей](../tips/tool-calling-loop-management.md))
