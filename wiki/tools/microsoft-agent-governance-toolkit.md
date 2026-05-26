---
title: "Microsoft Agent Governance Toolkit: Policy Enforcement for AI Agents"
title_ru: "Microsoft Agent Governance Toolkit: контроль политик для AI-агентов"
category: tools
tags: [governance, microsoft, agent-safety, owasp, policy-enforcement, security]
confidence: high
updated: 2026-05-26
sources:
  - https://github.com/microsoft/agent-governance-toolkit
  - https://x.com/bibryam/status/2057126955388993990
---

## Summary
Microsoft's open-source toolkit provides deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous AI agents — covering all 10 OWASP Agentic Top 10 risks with 992 conformance tests.

## Key Ideas
- Application-layer governance replaces prompt-based safety: prompt-based approaches show 26.67% policy violation rates in red-team testing; AGT's deterministic enforcement achieves 0.00%
- One-line API wraps any tool function: `govern(my_tool, policy="policy.yaml")` evaluates YAML policies on every call, logs decisions, and raises `GovernanceDenied` for blocked actions
- 8 modular packages covering the full governance stack: Agent OS (policy engine), Agent Mesh (identity/trust), Agent Runtime (sandboxing with 4 privilege rings), Agent SRE (kill switch/SLOs), Agent Compliance (OWASP verification), Agent Marketplace, Agent Lightning (RL governance), Agent Hypervisor (execution audit)
- Multi-language SDKs: Python, TypeScript, .NET, Rust, Go — with first-party Copilot CLI and Claude Code integrations
- Framework-agnostic: supports Semantic Kernel, AutoGen, LangGraph, CrewAI, OpenAI Agents SDK, Google ADK, LlamaIndex, Haystack, and more
- Standards compliance: OWASP Agentic AI Top 10 (all 10 risks), NIST AI RMF 1.0, EU AI Act, SOC 2 — with automated evidence generation

## Details
The Agent Governance Toolkit (AGT) addresses the core governance gap in autonomous AI agents: once deployed, agents make decisions independently, and traditional IAM/OAuth scopes only control which services an agent can reach — not what it does once connected. AGT adds three missing layers: "Is this action allowed?", "Which agent did this?", and "Can you prove what happened?"

The architecture follows a layered approach where every layer is optional. Teams typically start with `govern()` for policy enforcement + audit logging and add identity, sandboxing, and SRE layers as their risk profile grows. The toolkit includes CLI tools for installation checks (`agt doctor`), OWASP compliance verification (`agt verify --evidence`), prompt injection auditing (`agt red-team scan`), and policy validation (`agt lint-policy`).

The 992 conformance tests are backed by 10 formal RFC 2119 specifications and 25 Architecture Decision Records, making this one of the most thoroughly specified open-source governance frameworks for AI agents.

## Related Entries
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))
- [[claude-code-frameworks]] ([Claude Code Frameworks](../tools/claude-code-frameworks.md))
- [[microsoft-waza]] ([Microsoft Waza](../tools/microsoft-waza.md))

---
<!-- RU -->

## Краткое описание
Открытый инструментарий Microsoft обеспечивает детерминированное исполнение политик, идентификацию с нулевым доверием, песочницу выполнения и SRE для автономных AI-агентов — покрывая все 10 рисков OWASP Agentic Top 10 с 992 тестами соответствия.

## Ключевые идеи
- Управление на уровне приложения заменяет безопасность через промпты: подходы на основе промптов показывают 26,67% нарушений политик при red-team тестировании; детерминированное исполнение AGT — 0,00%
- Однострочный API обёртывает любую функцию-инструмент: `govern(my_tool, policy="policy.yaml")` проверяет YAML-политики при каждом вызове, логирует решения и выбрасывает `GovernanceDenied` для заблокированных действий
- 8 модульных пакетов покрывают весь стек управления: Agent OS (движок политик), Agent Mesh (идентификация/доверие), Agent Runtime (песочница с 4 кольцами привилегий), Agent SRE (kill switch/SLO), Agent Compliance (проверка OWASP), Agent Marketplace, Agent Lightning (управление RL), Agent Hypervisor (аудит выполнения)
- SDK для нескольких языков: Python, TypeScript, .NET, Rust, Go — с первичной поддержкой Copilot CLI и Claude Code
- Не зависит от фреймворка: поддерживает Semantic Kernel, AutoGen, LangGraph, CrewAI, OpenAI Agents SDK, Google ADK, LlamaIndex и другие
- Соответствие стандартам: OWASP Agentic AI Top 10 (все 10 рисков), NIST AI RMF 1.0, EU AI Act, SOC 2 — с автоматической генерацией свидетельств

## Подробнее
Agent Governance Toolkit (AGT) закрывает основной пробел в управлении автономными AI-агентами: после развёртывания агенты принимают решения самостоятельно, а традиционные IAM/OAuth-области контролируют только доступ к сервисам — не то, что агент делает после подключения. AGT добавляет три недостающих слоя: «Разрешено ли это действие?», «Какой агент это сделал?» и «Можете ли вы доказать, что произошло?»

Архитектура следует многоуровневому подходу, где каждый слой опционален. Команды обычно начинают с `govern()` для исполнения политик + аудитного логирования и добавляют идентификацию, песочницу и SRE по мере роста рисков. Инструментарий включает CLI-утилиты для проверки установки (`agt doctor`), верификации соответствия OWASP (`agt verify --evidence`), аудита prompt injection (`agt red-team scan`) и валидации политик (`agt lint-policy`).

992 теста соответствия подкреплены 10 формальными спецификациями RFC 2119 и 25 Architecture Decision Records, что делает AGT одним из наиболее тщательно специфицированных open-source фреймворков управления AI-агентами.

## Связанные записи
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))
- [[claude-code-frameworks]] ([Claude Code Frameworks](../tools/claude-code-frameworks.md))
- [[microsoft-waza]] ([Microsoft Waza](../tools/microsoft-waza.md))
