---
title: "Custom Agent Loop vs Claude Agent SDK: Multi-Tenant Production Considerations"
title_ru: "Собственный цикл агента vs Claude Agent SDK: соображения для мультитенантной продакшн-среды"
category: agents
tags: [agent-loop, claude-agent-sdk, multi-tenant, sse, websocket, fsm, model-routing, production]
aliases: [hand-rolled agent loop, custom vs SDK, agent SDK comparison]
confidence: medium
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://www.reddit.com/r/AI_Agents/comments/1tyjqsw/
---

## Summary
A production comparison of building a custom tool-use loop on the bare Anthropic SDK vs using the Claude Agent SDK — for multi-tenant conversational agents on AWS Fargate, the custom approach wins on control over SSE streams, WebSocket protocol, FSM-based tool scoping, and per-phase model routing.

## Key Ideas
- Custom loop on `@anthropic-ai/sdk` gives full ownership of the SSE stream and WebSocket protocol
- Finite State Machine (FSM) for tool scoping prevents tools from leaking across conversation phases
- Per-phase model routing (e.g., cheap model for intent classification, expensive model for execution) cuts costs significantly
- Claude Agent SDK abstracts away control that multi-tenant production workloads need
- The trade-off: custom loops require more maintenance but provide architectural flexibility the SDK can't match yet

## Details
For a multi-tenant conversational agent running Node/TypeScript on AWS Fargate, the decision to hand-roll a custom tool-use loop rather than use the Claude Agent SDK came down to four concrete requirements: (1) owning the SSE stream end-to-end for custom client-side rendering, (2) a WebSocket protocol that supports tenant isolation and concurrent sessions, (3) FSM-based tool scoping where different conversation phases expose different tool sets, and (4) per-phase model routing that sends classification tasks to cheaper models and execution tasks to more capable ones.

After re-evaluating the Agent SDK docs, the team decided to stay custom. The SDK is excellent for prototyping and single-tenant use cases, but for multi-tenant production workloads where you need fine-grained control over streaming, tenant isolation, and cost optimization, the abstraction layer becomes a constraint rather than an accelerator.

## Notable Quotes
> "Owns SSE stream, custom WebSocket protocol, FSM for tool scoping, per-phase model routing" — Original poster describing their custom architecture

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK](../agents/mcp-vs-adk-agent-connectivity.md))
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration: Multi-Model Frameworks](../agents/agent-orchestration-multi-model-framework.md))

---
<!-- RU -->

## Краткое описание
Сравнение собственного цикла вызова инструментов на базовом Anthropic SDK и Claude Agent SDK для мультитенантных разговорных агентов на AWS Fargate — собственная реализация выигрывает благодаря контролю над SSE-потоками, WebSocket-протоколом, FSM-ограничением инструментов и маршрутизацией моделей по фазам.

## Ключевые идеи
- Собственный цикл на `@anthropic-ai/sdk` даёт полный контроль над SSE-потоком и WebSocket-протоколом
- Конечный автомат (FSM) для ограничения инструментов предотвращает их утечку между фазами разговора
- Маршрутизация моделей по фазам (дешёвая модель для классификации намерений, дорогая для выполнения) значительно снижает затраты
- Claude Agent SDK абстрагирует контроль, необходимый для мультитенантных продакшн-нагрузок
- Компромисс: собственные циклы требуют больше поддержки, но дают архитектурную гибкость, которую SDK пока не может обеспечить

## Подробнее
Для мультитенантного разговорного агента на Node/TypeScript в AWS Fargate решение написать собственный цикл вызова инструментов вместо использования Claude Agent SDK было продиктовано четырьмя конкретными требованиями: (1) полное владение SSE-потоком для кастомного рендеринга на клиенте, (2) WebSocket-протокол с поддержкой изоляции тенантов и параллельных сессий, (3) FSM-ограничение инструментов, при котором разные фазы разговора предоставляют разные наборы инструментов, и (4) маршрутизация моделей по фазам, направляющая задачи классификации на более дешёвые модели, а задачи выполнения — на более мощные.

После повторной оценки документации Agent SDK команда решила остаться на собственной реализации. SDK отлично подходит для прототипирования и однотенантных сценариев, но для мультитенантных продакшн-нагрузок, где нужен детальный контроль над потоковой передачей, изоляцией тенантов и оптимизацией затрат, слой абстракции становится ограничением, а не ускорителем.

## Примечательные цитаты
> «Владеет SSE-потоком, кастомный WebSocket-протокол, FSM для ограничения инструментов, маршрутизация моделей по фазам» — Автор поста, описывая свою архитектуру

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK](../agents/mcp-vs-adk-agent-connectivity.md))
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration: Multi-Model Frameworks](../agents/agent-orchestration-multi-model-framework.md))
