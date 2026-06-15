---
title: "temenos — Sandbox for Agent-Executed Code"
title_ru: "temenos — песочница для кода, выполняемого агентами"
category: tools
tags: [sandbox, agents, gvisor, security, code-execution]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/vitalops/temenos
---

## Summary
Sandbox environment for AI agent-executed code using gVisor. Lets agents run arbitrary code safely without risking the host system. The sandbox constrains the executed code, not the agent itself — allowing full agent autonomy while preventing system damage.

## Key Ideas
- Uses gVisor (Google's application kernel) as the isolation mechanism
- Constrains executed code, not the agent — agent retains full autonomy
- Prevents agent-generated code from damaging the host system
- Critical for production agent deployments where code execution is required
- Addresses the security concern of letting autonomous agents run arbitrary code

## Details
As AI agents become more autonomous and are tasked with writing and executing code, the risk of unintended system damage grows. A coding agent might write a script that accidentally deletes files, opens network connections, or consumes all system resources. Temenos provides a containment layer.

Built on gVisor, it creates a lightweight sandbox that intercepts system calls from the executed code. The agent itself runs normally on the host, but any code it generates and runs is constrained within the sandbox. This separation means the agent can still access tools and context, while the code it runs cannot escape.

The name comes from the Greek word for a sacred, separated space — fitting for a tool that creates a boundary between the agent and the host system.

## Related Entries
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
- AI agents overview ([AI Agents Overview](../agents/ai-agents-overview.md))

---
<!-- RU -->

## Краткое описание
Среда-песочница для кода, выполняемого AI-агентами, на базе gVisor. Позволяет агентам безопасно выполнять произвольный код без риска для хост-системы. Песочница ограничивает выполняемый код, а не самого агента — обеспечивая полную автономность агента при предотвращении повреждения системы.

## Ключевые идеи
- Использует gVisor (прикладное ядро от Google) как механизм изоляции
- Ограничивает выполняемый код, а не агента — агент сохраняет полную автономность
- Предотвращает повреждение хост-системы кодом, сгенерированным агентом
- Критически важно для продакшен-развёртываний агентов, где требуется выполнение кода
- Решает проблему безопасности при разрешении автономным агентам выполнять произвольный код

## Подробнее
По мере того как AI-агенты становятся более автономными и получают задачи по написанию и выполнению кода, растёт риск непреднамеренного повреждения системы. Кодирующий агент может написать скрипт, который случайно удалит файлы, откроет сетевые соединения или потребит все системные ресурсы. Temenos обеспечивает слой изоляции.

Построенный на gVisor, он создаёт легковесную песочницу, которая перехватывает системные вызовы от выполняемого кода. Сам агент работает нормально на хосте, но любой код, который он генерирует и запускает, ограничен в пределах песочницы. Это разделение означает, что агент по-прежнему имеет доступ к инструментам и контексту, в то время как запускаемый им код не может выйти за пределы.

Название происходит от греческого слова, означающего священное, отделённое пространство — что подходит для инструмента, создающего границу между агентом и хост-системой.

## Связанные записи
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
- AI agents overview ([AI Agents Overview](../agents/ai-agents-overview.md))
