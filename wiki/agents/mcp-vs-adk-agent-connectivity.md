---
title: "MCP vs ADK: Two Different Problems in AI Agent Architecture"
title_ru: "MCP против ADK: две разные задачи в архитектуре AI-агентов"
category: agents
tags: [mcp, adk, google, anthropic, agent-architecture, connectivity, orchestration, model-context-protocol, agent-development-kit]
aliases: [MCP vs ADK, Agent Development Kit, Google ADK, ADK vs MCP]
confidence: high
date: 2026-05-21
updated: 2026-05-21
sources:
  - https://www.youtube.com/watch?v=BedAaB1RKgE
---

## Summary

MCP (Model Context Protocol) and ADK (Google's Agent Development Kit) are often compared as competing technologies — but they solve fundamentally different problems and are complementary: MCP answers *how an agent talks to external tools*, ADK answers *how to build and orchestrate the agent itself*.

## Key Ideas

- **Two distinct questions:** Building AI agents raises two independent problems: (1) how does my agent connect to external tools and data? (2) how do I build, orchestrate, and manage the agent itself? MCP addresses the first; ADK addresses the second.
- **MCP = connectivity standard.** Created by Anthropic, MCP is a *protocol* — a standardised interface for how an AI client (your agent) communicates with external servers (databases, APIs, file systems, third-party tools). It eliminates custom glue code for every tool integration.
- **ADK = orchestration framework.** Created by Google, ADK provides the structure for building agents: defining agent behaviour, managing session state, memory across sessions, multi-agent coordination, and testing agent reliability.
- **Model-agnostic vs Google-native.** MCP works with any LLM that speaks the protocol (Claude, GPT, Gemini, local models). ADK is Google's framework, optimised for Gemini but technically usable with other models.
- **Not competing — complementary.** A production agent might use ADK to manage its architecture and orchestration, while also using MCP servers to connect to GitHub, Slack, Postgres, or other external resources.
- **Ecosystem momentum for MCP.** MCP servers already exist for GitHub, Slack, Google Drive, Postgres, Jira, Figma, and many more. The ecosystem is growing rapidly because any tool can become an MCP server once.

## Details

### Before MCP: The Custom Glue Problem

Before MCP, every team building an AI agent wrote custom integration code for every external tool — a Slack connector, a database adapter, a web scraper. Multiple teams at the same company, let alone across companies, were all solving the same connectivity problems with bespoke code. This "custom glue code" made agents fragile, slow to build, and hard to maintain.

MCP standardised this interface. A tool that exposes an MCP server can be used by *any* MCP-compatible agent, regardless of which LLM it uses. The protocol defines how requests and responses are structured, how authentication works, and how the agent discovers what the server can do.

### How MCP Works (Simplified)

```
Agent (MCP Client) ←→ MCP Protocol ←→ MCP Server (GitHub, Slack, DB, ...)
```

- **Client:** the LLM agent, or the software hosting it
- **Server:** any service that exposes tools/data via the MCP standard
- **Benefits:** write the MCP server once; all compatible agents can use it

### What ADK Adds

While MCP solves "how do I connect to things," ADK solves "how do I structure my agent." ADK provides:

- **Agent definition:** declarative specification of agent capabilities and behaviour
- **Session state:** short-term working memory within a single conversation
- **Long-term memory:** what the agent retains across sessions (user preferences, learned context)
- **Multi-agent coordination:** orchestrating sub-agents, managing dependencies
- **Testing and observability:** making agent behaviour predictable and verifiable

The key insight from the IBM video: without a framework like ADK, developers must hand-roll session state, memory management, and multi-agent coordination — the hardest parts of building production agents.

### When to Use Which

| Need | Use |
|---|---|
| Connect agent to GitHub, Slack, Postgres | MCP server |
| Define how your agent behaves and plans | ADK (or similar framework) |
| Make agent model-agnostic across Claude/GPT/local | MCP |
| Build on Google Cloud with Gemini | ADK |
| Reuse community-built tool integrations | MCP ecosystem |
| Manage session state and long-term memory | ADK |

Both can — and often should — be used together: ADK for the agent's structure, MCP for its external connections.

## Related Entries

- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[agent-operating-system]] ([Agent Operating System](../agents/agent-operating-system.md))
- [[mcp-financial-data-server]] ([MCP Financial Data Server](../tools/mcp-financial-data-server.md))
- [[gnosis-mcp-vs-llm-wiki-pattern]] ([Gnosis MCP vs LLM Wiki Pattern](../concepts/gnosis-mcp-vs-llm-wiki-pattern.md))
- [[anthropic-agent-memory-dreaming]] ([Anthropic Agent Memory and Dreaming](../agents/anthropic-agent-memory-dreaming.md))
- [[opensddrag-mcp-harness]] ([OpenSddRag: MCP Server with Persistent Rules Harness for Coding Agents](../tools/opensddrag-mcp-harness.md))

---
<!-- RU -->

## Краткое описание

MCP (Model Context Protocol) и ADK (Agent Development Kit от Google) часто сравнивают как конкурирующие технологии — но они решают принципиально разные задачи и являются взаимодополняющими: MCP отвечает на вопрос *как агент общается с внешними инструментами*, ADK — на вопрос *как строить и оркестрировать сам агент*.

## Ключевые идеи

- **Два разных вопроса:** Разработка AI-агентов ставит две независимые задачи: (1) как агент подключается к внешним инструментам и данным? (2) как строить, оркестрировать и управлять самим агентом? MCP решает первую, ADK — вторую.
- **MCP = стандарт подключения.** Создан Anthropic. Стандартизированный интерфейс для общения AI-клиента (вашего агента) с внешними серверами (базами данных, API, файловыми системами). Устраняет необходимость писать кастомный связующий код для каждой интеграции.
- **ADK = фреймворк оркестрации.** Создан Google. Предоставляет структуру для построения агентов: определение поведения, управление состоянием сессии, памятью между сессиями, мультиагентной координацией.
- **Независимость от модели vs Google-нативность.** MCP работает с любым LLM (Claude, GPT, Gemini, локальные модели). ADK оптимизирован для Gemini и Google Cloud.
- **Не конкуренты — взаимодополнение.** Production-агент может использовать ADK для структуры и оркестрации, параллельно используя MCP-серверы для подключения к GitHub, Slack, Postgres.
- **Экосистема MCP растёт.** MCP-серверы уже существуют для GitHub, Slack, Google Drive, Postgres, Jira, Figma и многих других сервисов.

## Подробнее

### До MCP: проблема кастомного связующего кода

До MCP каждая команда, строящая AI-агента, писала кастомный код интеграции для каждого внешнего инструмента. MCP стандартизировал этот интерфейс. Инструмент, выставляющий MCP-сервер, может использоваться *любым* совместимым агентом независимо от LLM.

### Когда использовать что

| Потребность | Инструмент |
|---|---|
| Подключить агент к GitHub, Slack, Postgres | MCP-сервер |
| Определить поведение и планирование агента | ADK (или аналог) |
| Независимость агента от модели | MCP |
| Разработка на Google Cloud с Gemini | ADK |
| Использовать готовые интеграции сообщества | экосистема MCP |
| Управлять состоянием сессии и долгосрочной памятью | ADK |

## Связанные записи

- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[agent-operating-system]] ([Agent Operating System](../agents/agent-operating-system.md))
- [[mcp-financial-data-server]] ([MCP Financial Data Server](../tools/mcp-financial-data-server.md))
- [[gnosis-mcp-vs-llm-wiki-pattern]] ([Gnosis MCP vs LLM Wiki Pattern](../concepts/gnosis-mcp-vs-llm-wiki-pattern.md))
- [[anthropic-agent-memory-dreaming]] ([Anthropic Agent Memory and Dreaming](../agents/anthropic-agent-memory-dreaming.md))
- [[opensddrag-mcp-harness]] ([OpenSddRag: MCP-сервер с постоянным движком правил для coding-агентов](../tools/opensddrag-mcp-harness.md))
