---
title: "MCP vs Direct APIs: Why Add a Protocol Layer at All?"
title_ru: "MCP против прямых API: зачем вообще нужен слой протокола?"
category: concepts
tags: [mcp, model-context-protocol, api, cli, agent-architecture, tool-use, protocol, debate]
aliases: [why MCP, MCP vs API, MCP vs CLI, do we need MCP]
confidence: medium
date: 2026-08-30
updated: 2026-08-30
sources:
  - https://news.ycombinator.com/item?id=49488654
  - https://www.reddit.com/r/AI_Agents/comments/1lq3w0d/why_use_mcp_when_agents_can_useapis_directly/
---

## Summary
A recurring community debate: if an agent can already read API documentation and chain HTTP calls, what does MCP actually add? The strongest answer is protocol uniformity — one interface an agent already knows how to discover and crawl, regardless of whether the backend is REST, OpenAPI, or GraphQL.

## Key Ideas
- **The skeptic's case**: publish your API docs and let the agent chain the calls. As one HN poster put it, you could repurpose MCP so the only response it ever produces is API documentation — no protocol needed.
- **The protocol argument**: MCP and APIs are "extremely similar," but MCP gives every agent one common protocol to follow. An agent knows how to discover and crawl any MCP server, so shipping an MCP tool means the agent can develop a usage pattern without bespoke integration work per backend.
- **CLI tools as the third option**: several practitioners report replacing MCP servers entirely with CLI tools — Git, Atlassian ACLI, Metabase, plus custom shell scripts — and finding this works well. Agents are already good at shell, and CLIs are self-documenting via `--help`.
- **Cost and safety framing**: the CLI/direct-API approach "probably covers most use cases and is a lot cheaper and safer" — fewer moving parts, no extra server process, no additional attack surface.
- **Nobody is forcing adoption**: the pragmatic reply that recurs in these threads — MCP is optional infrastructure, and teams whose integration needs are already met by CLIs or direct calls have no obligation to add it.

## Details

### Where MCP Earns Its Place
The uniformity argument is strongest at ecosystem scale. If you are a vendor shipping an integration that thousands of unknown agents will consume, a protocol they all already understand beats documentation each of them must interpret independently. Discovery is the concrete win: an agent can enumerate an MCP server's tools programmatically, whereas parsing prose API docs is inference that can go wrong.

### Where It Is Overhead
For a single team wiring up their own known set of tools, the protocol layer may be pure cost. The CLI approach in particular has real advantages that MCP advocates tend to underweight: shell tools compose, they are already installed, they produce plain text an LLM handles natively, and they require no additional running process. The trade-off is that CLI output is unstructured, so the agent must parse it — which is exactly the class of error MCP's typed schemas eliminate.

### The Token-Cost Dimension
This debate connects directly to the tool-schema bloat problem: MCP servers that attach full JSON schemas for every tool on every request can burn tens of thousands of tokens before the user's message is even counted. A CLI invoked on demand has no such standing cost. That practical consideration frequently decides the question for cost-sensitive deployments.

### Note on Sourcing
The Hacker News thread is small (12 points, several comments flagged); the larger r/AI_Agents discussion (187 upvotes, 146 comments) could not be fetched directly due to robots.txt. Treat this entry as a Tier-3 community synthesis rather than a settled architectural conclusion.

## Related Entries
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK: Two Different Problems](../agents/mcp-vs-adk-agent-connectivity.md))
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](../tips/mcp-tool-schema-bloat-token-cost.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))

---
<!-- RU -->

## Краткое описание
Повторяющаяся дискуссия в сообществе: если агент и так умеет читать документацию API и связывать HTTP-вызовы, что именно добавляет MCP? Наиболее убедительный ответ — единообразие протокола: один интерфейс, который агент уже умеет обнаруживать и обходить, независимо от того, что за бэкенд — REST, OpenAPI или GraphQL.

## Ключевые идеи
- **Позиция скептика**: опубликуйте документацию API и позвольте агенту связать вызовы. Как выразился один участник HN, можно переделать MCP так, чтобы единственным ответом была документация API — без всякого протокола.
- **Аргумент протокола**: MCP и API «крайне похожи», но MCP даёт всем агентам единый протокол. Агент умеет обнаруживать и обходить любой MCP-сервер, поэтому поставка MCP-инструмента позволяет ему выработать паттерн использования без индивидуальной интеграции под каждый бэкенд.
- **CLI-инструменты как третий вариант**: ряд практиков сообщает о полной замене MCP-серверов на CLI — Git, Atlassian ACLI, Metabase плюс собственные shell-скрипты — и считает это вполне работающим. Агенты хорошо владеют shell, а CLI самодокументируются через `--help`.
- **Стоимость и безопасность**: подход через CLI/прямые API «вероятно, покрывает большинство сценариев и заметно дешевле и безопаснее» — меньше движущихся частей, нет отдельного процесса-сервера, меньше поверхность атаки.
- **Никто не принуждает**: прагматичный ответ, регулярно всплывающий в таких обсуждениях — MCP является опциональной инфраструктурой.

## Подробнее

**Где MCP оправдан.** Аргумент единообразия сильнее всего на масштабе экосистемы. Если вы поставляете интеграцию, которую будут потреблять тысячи неизвестных агентов, протокол, понятный всем, выигрывает у документации, которую каждый должен интерпретировать самостоятельно. Конкретная победа — обнаружение: агент может программно перечислить инструменты MCP-сервера, тогда как разбор текстовой документации — это вывод, который может пойти не так.

**Где это накладные расходы.** Для одной команды, подключающей собственный известный набор инструментов, слой протокола может быть чистой издержкой. У подхода через CLI есть реальные преимущества: shell-инструменты компонуются, уже установлены, выдают простой текст, который LLM обрабатывает нативно, и не требуют дополнительного процесса. Компромисс в том, что вывод CLI неструктурирован, и агент должен его разбирать — а это как раз тот класс ошибок, который устраняют типизированные схемы MCP.

**Измерение стоимости токенов.** Дискуссия напрямую связана с проблемой раздувания схем: MCP-серверы, прикрепляющие полные JSON-схемы всех инструментов к каждому запросу, могут сжигать десятки тысяч токенов ещё до учёта сообщения пользователя.

**О качестве источников**: тред на Hacker News небольшой (12 баллов, часть комментариев скрыта); более крупное обсуждение в r/AI_Agents не удалось загрузить из-за robots.txt. Считать эту запись синтезом сообщества уровня Tier 3, а не устоявшимся архитектурным выводом.

## Связанные записи
- [[mcp-vs-adk-agent-connectivity]] ([MCP vs ADK: две разные задачи](../agents/mcp-vs-adk-agent-connectivity.md))
- [[mcp-tool-schema-bloat-token-cost]] ([Раздувание схемы MCP-инструментов](../tips/mcp-tool-schema-bloat-token-cost.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
