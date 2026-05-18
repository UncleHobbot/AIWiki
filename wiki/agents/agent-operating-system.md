---
title: "Agent Operating System (Agent OS)"
title_ru: "Операционная система для агентов (Agent OS)"
category: agents
tags: [agent-os, ai-agents, memory, orchestration, guardrails, identity, observability, tool-management, infrastructure]
aliases: [Agent OS, AgentOS, operating system for AI agents, agent kernel]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=IVGjBxqygmI
---

## Summary
An Agent Operating System (Agent OS) is infrastructure that manages AI agents the way a computer OS manages applications — handling memory, scheduling, tool access, identity, observability, and guardrails so that agents can operate reliably at scale.

## Key Ideas
- **The goldfish problem:** Current AI agents have no memory between sessions — every conversation starts from zero, making multi-session workflows unreliable.
- **Three-layer architecture:** Top layer = agents (workers); middle layer = Agent OS kernel (management); bottom layer = infrastructure (compute, models, databases).
- **Six kernel components:** Scheduler/orchestrator, memory manager, tool manager, identity manager, observability system, guardrails and governance.
- **Sandbox execution:** Tools run in sandboxes so a coding agent cannot accidentally delete production databases or access secrets outside its permitted scope.
- **Human-in-the-loop governance:** Governance policies define which actions require human approval (e.g., refunds over $50 auto-approved; over $50 needs sign-off).
- **Without Agent OS, teams risk deploying unreliable and fragile agents** — like running a city without traffic lights.

## Details
IBM's framing maps the six kernel components directly onto analogs from traditional OS design:

**Scheduler / Orchestrator** — decides which agent gets compute when multiple agents compete. A live customer-service agent takes priority over a background summarization job.

**Memory Manager** — solves the goldfish problem with three memory tiers: short-term (current conversation), long-term (cross-session history), and episodic (remembering that a past approach failed). Example: an HR agent that recalls you asked about parental leave last month rather than starting from scratch.

**Tool Manager** — maintains a registry of available tools, enforces who can use them, and runs each tool call inside a sandbox. A coding agent can execute Python but only inside a designated folder; it cannot read credentials or reach the internet without explicit permission.

**Identity Manager** — issues short-lived credential tokens to agents acting on behalf of users, creating an audit trail ("this agent acted on behalf of this user"). Analogous to badge-based building access.

**Observability** — logs every decision, tool call, and response. If an agent approves a refund it should not have, the full decision chain can be rewound and audited.

**Guardrails and Governance** — input guardrails filter malicious prompts (prompt injection); output guardrails catch inappropriate or incorrect responses before they reach users; policy layer enforces which actions are automated versus which require human approval.

The architectural argument is that teams already deploying agents without this infrastructure are accumulating technical debt in the form of unreliable, un-debuggable, hard-to-scale systems.

## Video Notes
- [0:00] Opening: AI agents are booking flights and writing code but have no memory of what they did 5 minutes ago
- [3:30] The three-layer cake: agents (top) → Agent OS kernel (middle) → infrastructure (bottom)
- [5:00] Scheduler: prioritizes live customer service over background batch jobs
- [6:30] Memory manager: short-term, long-term, and episodic memory tiers
- [8:00] Tool manager: sandboxed execution — coding agent limited to specific folder
- [9:30] Identity manager: short-lived tokens, audit trail for agent actions
- [10:30] Observability: full decision-chain logging for post-hoc debugging
- [11:30] Guardrails: input filtering (prompt injection), output filtering, human-in-the-loop policies
- [12:30] Conclusion: without Agent OS, agents are "brilliant but unreliable"

## Related Entries
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[llm-wiki-enterprise-patterns]] ([LLM Wiki Enterprise Patterns](../agents/llm-wiki-enterprise-patterns.md))
- [[new-organizational-models-ai-agents]] ([New Organizational Models for AI Agents](../agents/new-organizational-models-ai-agents.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))

---
<!-- RU -->

## Краткое описание
Операционная система для агентов (Agent OS) — это инфраструктурный слой, управляющий AI-агентами так же, как компьютерная ОС управляет приложениями: планирование задач, память, доступ к инструментам, идентификация, наблюдаемость и защитные ограждения.

## Ключевые идеи
- **Проблема золотой рыбки:** у большинства AI-агентов нет памяти между сессиями — каждый разговор начинается с нуля, что делает многосессионные рабочие процессы ненадёжными.
- **Трёхуровневая архитектура:** верхний слой — агенты; средний — ядро Agent OS; нижний — инфраструктура (вычисления, модели, базы данных).
- **Шесть компонентов ядра:** планировщик/оркестратор, менеджер памяти, менеджер инструментов, менеджер идентификации, система наблюдаемости, ограждения и управление.
- **Изолированное выполнение:** инструменты запускаются в sandbox — агент не может случайно удалить production-базу или получить доступ к чужим секретам.
- **Human-in-the-loop:** политика управления определяет, какие действия требуют одобрения человека (например, рефанды до $50 — автоматически; свыше $50 — нужно подтверждение).
- **Без Agent OS команды рискуют развернуть ненадёжных агентов** — как управлять городом без светофоров.

## Подробнее
Шесть компонентов ядра напрямую соответствуют аналогам из традиционного дизайна ОС.

**Планировщик/оркестратор** решает, какой агент получает вычислительные ресурсы, когда несколько агентов конкурируют. Живой агент клиентской поддержки имеет приоритет над фоновым агентом суммаризации.

**Менеджер памяти** решает проблему золотой рыбки через три уровня памяти: краткосрочная (текущий разговор), долгосрочная (история между сессиями) и эпизодическая (помнит, что определённый подход уже провалился). Пример: HR-агент помнит, что в прошлом месяце вы спрашивали о декретном отпуске.

**Менеджер инструментов** ведёт реестр доступных инструментов, контролирует права доступа и запускает каждый вызов инструмента в sandbox. Агент-программист может выполнять Python-код, но только в указанной папке.

**Менеджер идентификации** выдаёт краткосрочные токены агентам, действующим от имени пользователей, создавая цепочку аудита — по аналогии с пропускной системой офиса.

**Наблюдаемость** записывает каждое решение, вызов инструмента и ответ. Если агент одобрил рефанд, которого не должен был, можно отмотать всю цепочку решений назад.

**Ограждения и управление:** входные фильтры блокируют инъекции в prompt; выходные — перехватывают некорректные ответы; политика управления определяет, что автоматизируется, а что требует участия человека.

## Заметки по видео
- [0:00] Открытие: AI-агенты бронируют рейсы и пишут код, но не помнят, что делали 5 минут назад
- [3:30] Трёхслойный торт: агенты → ядро Agent OS → инфраструктура
- [6:30] Менеджер памяти: краткосрочная, долгосрочная и эпизодическая память
- [8:00] Менеджер инструментов: sandbox-выполнение — агент ограничен конкретной папкой
- [11:30] Ограждения: фильтрация входящих (инъекции в prompt), фильтрация исходящих, human-in-the-loop

## Связанные записи
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[llm-wiki-enterprise-patterns]] ([LLM Wiki Enterprise Patterns](../agents/llm-wiki-enterprise-patterns.md))
- [[new-organizational-models-ai-agents]] ([New Organizational Models for AI Agents](../agents/new-organizational-models-ai-agents.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
