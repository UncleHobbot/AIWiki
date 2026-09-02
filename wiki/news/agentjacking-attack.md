---
title: "Agentjacking: Hijacking AI Coding Agents via Fake Sentry Error Reports"
title_ru: "Agentjacking: перехват AI-кодинг-агентов через фальшивые отчёты об ошибках Sentry"
category: news
tags: [agentjacking, security, ai-agents, coding-agents, sentry, prompt-injection, tenet-security]
date: 2026-06-14
updated: 2026-06-14
sources:
  - https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html
---

## Summary
Tenet Security disclosed "Agentjacking" — a new class of attack that tricks AI coding agents into running arbitrary malicious code on developer machines. The payload is delivered through a fake error report crafted using Sentry, the open-source error-tracking platform. When the coding agent ingests the report to debug an issue, the embedded malicious instructions execute — hijacking an agent the developer already trusts.

## Key Ideas
- New attack class named "Agentjacking," coined after carjacking — stealing an agent that the developer already trusts
- Uses Sentry-formatted fake error reports as the delivery vector, exploiting an error-handling workflow agents assume is safe
- Exploits the implicit trust relationship between developer and coding agent: agents run attacker code believing they are merely debugging
- Demonstrates supply-chain risk in agent–tool integrations, where any tool output an agent ingests becomes a potential instruction channel
- Highlights that debugging context is not sanitized as untrusted input in current coding-agent harnesses

## Details
The name Agentjacking is a deliberate reference to carjacking: the attacker does not build their own agent or breach the model — they steal control of an agent that is already running, already authenticated, and already trusted by the developer. The attack is elegant in its misuse of a benign workflow. Sentry error reports are a normal part of how engineering teams surface and fix bugs, and AI coding agents are routinely pointed at such reports so they can diagnose and patch the underlying issue.

The abuse path is simple: an attacker crafts a Sentry-style error report that contains, inside its stack trace or metadata, prompt-injection instructions. When the coding agent ingests the report to investigate, it treats the embedded text as part of its task context rather than as hostile data. The agent then executes the injected instructions — installing packages, reading files, or running shell commands — under the developer's own privileges, all while believing it is debugging.

The deeper lesson is about trust boundaries in agent harnesses. Coding agents already have broad, often unsandboxed access to the developer's machine, and they process many kinds of tool output — logs, error reports, search results, web pages — as part of normal work. Agentjacking shows that every one of those ingestion channels is a potential instruction surface, and that error/debugging context specifically is not yet being treated as untrusted input.

## Related Entries
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[openclaw-agent-security-vulnerabilities]] ([OpenClaw Agent Security Vulnerabilities](../news/openclaw-agent-security-vulnerabilities.md))
- [[malware-slop-npm-claude-user-directory]] ([Malware-Slop: npm Package Targeting Claude](../news/malware-slop-npm-claude-user-directory.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))
- [[self-replicating-ai-worm-local-models]] ([Self-Replicating AI Worm](../news/self-replicating-ai-worm-local-models.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate — Prompt-Injection Defense Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[bioshocking-ai-browser-credential-leak]] ([BioShocking — AI Browser Credential Leak](bioshocking-ai-browser-credential-leak.md))

---
- [[agentic-safety-vs-textual-safety-mcp-attacks]] ([Agentic Safety vs Textual Safety](../research/agentic-safety-vs-textual-safety-mcp-attacks.md))
- [[ai-coding-agents-triggering-edr-rules]] ([AI Coding Agents Triggering EDR Rules](ai-coding-agents-triggering-edr-rules.md))
- [[openai-cursor-model-winddown]] ([OpenAI Winds Down Cursor Access](openai-cursor-model-winddown.md))
- [[ai-agents-top-attack-vector-aug-2026]] ([AI Agents #1 Attack Vector (Aug 2026)](ai-agents-top-attack-vector-aug-2026.md))
<!-- RU -->

## Краткое описание
Tenet Security раскрыла «Agentjacking» — новый класс атак, при котором AI-кодинг-агентов обманом заставляют выполнять произвольный вредоносный код на машинах разработчиков. Пейлоад доставляется через фальшивый отчёт об ошибке, созданный с помощью Sentry — open-source-платформы трекинга ошибок. Когда кодинг-агент обрабатывает отчёт для отладки, встроенные вредоносные инструкции выполняются — происходит перехват агента, которому разработчик уже доверяет.

## Ключевые идеи
- Новый класс атак под названием «Agentjacking», названный по аналогии с carjacking — кражей уже доверенного агентом
- Использует фальшивые отчёты об ошибках в формате Sentry как вектор доставки, эксплуатируя workflow обработки ошибок, который агенты считают безопасным
- Эксплуатирует неявное отношение доверия между разработчиком и кодинг-агентом: агенты выполняют код атакующего, полагая, что просто отлаживают
- Демонстрирует риск цепочки поставок в интеграциях агент–инструмент, где любой вывод инструмента, который поглощает агент, становится потенциальным каналом инструкций
- Подчёркивает, что отладочный контекст не санитизируется как недоверенный ввод в текущих харнессах кодинг-агентов

## Подробнее
Название Agentjacking — намеренная отсылка к carjacking: атакующий не строит собственного агента и не взламывает модель — он перехватывает контроль над агентом, который уже запущен, уже аутентифицирован и уже доверяем разработчиком. Атака изящна в своём злоупотреблении безобидным рабочим процессом. Отчёты об ошибках Sentry — нормальная часть того, как инженерные команды обнаруживают и исправляют баги, а AI-кодинг-агентов routinely направляют на такие отчёты, чтобы они диагностировали и закрывали underlying-проблемы.

Путь злоупотребления прост: атакующий создаёт отчёт об ошибке в стиле Sentry, содержащий внутри stack trace или метаданных инструкции prompt injection. Когда кодинг-агент поглощает отчёт для исследования, он воспринимает встроенный текст как часть контекста задачи, а не как враждебные данные. Затем агент выполняет внедрённые инструкции — устанавливает пакеты, читает файлы или запускает shell-команды — под собственными привилегиями разработчика, всё это время полагая, что занимается отладкой.

Более глубокий урок — о границах доверия в харнессах агентов. Кодинг-агенты уже имеют широкий, часто несэндбоксенный доступ к машине разработчика и обрабатывают множество видов вывода инструментов — логи, отчёты об ошибках, результаты поиска, веб-страницы — как часть обычной работы. Agentjacking показывает, что каждый из этих каналов поглощения — потенциальная поверхность инструкций, и что контекст ошибок/отладки пока не рассматривается как недоверенный ввод.

## Связанные записи
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[openclaw-agent-security-vulnerabilities]] ([OpenClaw Agent Security Vulnerabilities](../news/openclaw-agent-security-vulnerabilities.md))
- [[malware-slop-npm-claude-user-directory]] ([Malware-Slop: npm Package Targeting Claude](../news/malware-slop-npm-claude-user-directory.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))
- [[self-replicating-ai-worm-local-models]] ([Self-Replicating AI Worm](../news/self-replicating-ai-worm-local-models.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate — Prompt-Injection Defense Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[bioshocking-ai-browser-credential-leak]] ([BioShocking — AI Browser Credential Leak](bioshocking-ai-browser-credential-leak.md))
