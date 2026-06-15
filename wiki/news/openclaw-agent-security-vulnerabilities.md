---
title: "OpenClaw Agent Security Vulnerabilities: Imperva and Varonis Demos"
title_ru: "Уязвимости агента OpenClaw: демонстрации Imperva и Varonis"
category: news
tags: [openclaw, security, prompt-injection, agent-security, imperva, varonis]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
  - https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html
---

## Summary
Two independent security teams — Imperva and Varonis — demonstrated that OpenClaw, the popular self-hosted AI agent, can be tricked into running attacker-controlled code or leaking sensitive data through ordinary-looking inputs, highlighting a broader class of indirect prompt injection vulnerabilities affecting all AI agents that process untrusted data.

## Key Ideas
- Imperva buried malicious instructions inside shared contacts, vCards, and location pins that OpenClaw executed without the victim seeing them
- Varonis showed agents being phished into leaking real credentials through crafted social engineering prompts
- Both attacks target OpenClaw specifically but the vulnerability class applies broadly to any AI agent that processes untrusted external data
- Demonstrates real-world risk of indirect prompt injection via data the agent ingests as part of normal workflows
- AIRQ 2026 Q2 report found only 11% of production agents pass security tests — this attack validates that statistic

## Details
Imperva's attack vector is particularly insidious: malicious instructions are embedded in data objects the user would never think to inspect — a shared contact card, a vCard attachment, or a location pin dropped on a map. When OpenClaw processes these as part of its normal task flow, it interprets the hidden instructions as commands and executes them. The victim sees only the innocent-looking contact or pin.

Varonis took a different approach, demonstrating that AI agents can be socially engineered into revealing real credentials. By crafting prompts that exploit the agent's helpfulness bias, attackers can extract API keys, database passwords, and other secrets that the agent has access to through its tool integrations.

These demonstrations are part of a growing body of evidence that the current generation of AI agents lacks fundamental input sanitization. Unlike traditional software that treats data and instructions as separate channels, LLM-based agents process everything through the same token stream, making indirect prompt injection an inherent architectural challenge rather than a patchable bug.

## Related Entries
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action Prompt Injection](../news/claude-code-github-action-prompt-injection.md))
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[gemini-android-notification-hijack]] ([Gemini Android Notification Hijack](../news/gemini-android-notification-hijack.md))
- [[chatgpt-lockdown-mode]] ([ChatGPT Lockdown Mode](../news/chatgpt-lockdown-mode.md))
- [[self-replicating-ai-worm-local-models]] ([Self-Replicating AI Worm](../news/self-replicating-ai-worm-local-models.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))
- [[awesome-agent-vault-credentials]] ([Awesome Agent Vault](../tools/awesome-agent-vault-credentials.md))
- [[redactable-pii-protection]] ([Redactable: PII Protection Plugin for OpenCode](../tools/redactable-pii-protection.md))
- [[temenos-agent-sandbox]] ([temenos — Sandbox for Agent-Executed Code](../tools/temenos-agent-sandbox.md))
- [[vibe-coding-security-checklist]] ([Vibe Coding Security Checklist: What AI Skips by Default](../tips/vibe-coding-security-checklist.md))
- [[agentjacking-attack]] ([Agentjacking: Hijacking AI Coding Agents via Fake Sentry Error Reports](../news/agentjacking-attack.md))
- [[langgraph-rce-vulnerability]] ([LangGraph RCE Vulnerability Chain: SQL Injection to Full Code Execution](../news/langgraph-rce-vulnerability.md))
- [[openclaw-free-hosting]] ([OpenClaw Hosting Goes Free](../news/openclaw-free-hosting.md))
- [[verifier-tax-tool-agent-safety]] ([The Verifier Tax: Safety-Success Tradeoffs in Tool-Using LLM Agents](../concepts/verifier-tax-tool-agent-safety.md))

---
<!-- RU -->

## Краткое описание
Две независимые команды безопасности — Imperva и Varonis — продемонстрировали, что OpenClaw, популярный самохостящийся AI-агент, можно обманом заставить выполнить контролируемый атакующим код или утечь конфиденциальные данные через обычные входные данные. Это подчёркивает более широкий класс уязвимостей непрямой инъекции промптов, затрагивающий все AI-агенты, обрабатывающие недоверенные данные.

## Ключевые идеи
- Imperva спрятала вредоносные инструкции внутри общих контактов, vCard и геолокационных меток — OpenClaw выполнял их без ведома жертвы
- Varonis показала фишинг агентов с утечкой реальных учётных данных через целенаправленные промпты социальной инженерии
- Обе атаки нацелены на OpenClaw, но класс уязвимостей применим к любому AI-агенту, обрабатывающему недоверенные внешние данные
- Демонстрирует реальный риск непрямой инъекции промптов через данные, которые агент обрабатывает в рамках обычных рабочих процессов
- Отчёт AIRQ за Q2 2026 показал, что только 11% продакшен-агентов проходят тесты безопасности — эта атака подтверждает статистику

## Подробнее
Вектор атаки Imperva особенно коварен: вредоносные инструкции встраиваются в объекты данных, которые пользователь никогда не подумает проверять — общая карточка контакта, вложение vCard или метка на карте. Когда OpenClaw обрабатывает их как часть обычного потока задач, он интерпретирует скрытые инструкции как команды и выполняет их. Жертва видит только безобидный контакт или метку.

Varonis использовала другой подход, продемонстрировав, что AI-агентов можно подвергнуть социальной инженерии для раскрытия реальных учётных данных. Создавая промпты, эксплуатирующие склонность агента к помощи, атакующие могут извлечь API-ключи, пароли баз данных и другие секреты, к которым агент имеет доступ через свои интеграции с инструментами.

Эти демонстрации — часть растущего объёма свидетельств того, что текущее поколение AI-агентов лишено фундаментальной санитизации входных данных. В отличие от традиционного ПО, где данные и инструкции разделены, LLM-агенты обрабатывают всё через один и тот же поток токенов, что делает непрямую инъекцию промптов не исправляемым багом, а архитектурной проблемой.

## Связанные записи
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action Prompt Injection](../news/claude-code-github-action-prompt-injection.md))
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[gemini-android-notification-hijack]] ([Gemini Android Notification Hijack](../news/gemini-android-notification-hijack.md))
- [[chatgpt-lockdown-mode]] ([ChatGPT Lockdown Mode](../news/chatgpt-lockdown-mode.md))
- [[self-replicating-ai-worm-local-models]] ([Self-Replicating AI Worm](../news/self-replicating-ai-worm-local-models.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))
- [[awesome-agent-vault-credentials]] ([Awesome Agent Vault](../tools/awesome-agent-vault-credentials.md))
- [[redactable-pii-protection]] ([Redactable: защита PII для OpenCode](../tools/redactable-pii-protection.md))
- [[temenos-agent-sandbox]] ([temenos — песочница для кода, выполняемого агентами](../tools/temenos-agent-sandbox.md))
- [[vibe-coding-security-checklist]] ([Чек-лист безопасности для vibe coding: что AI пропускает по умолчанию](../tips/vibe-coding-security-checklist.md))
- [[agentjacking-attack]] ([Agentjacking: перехват AI-кодинг-агентов через фальшивые отчёты об ошибках Sentry](../news/agentjacking-attack.md))
- [[langgraph-rce-vulnerability]] ([Цепочка уязвимостей LangGraph: от SQL-инъекции до полного RCE](../news/langgraph-rce-vulnerability.md))
- [[openclaw-free-hosting]] ([Хостинг OpenClaw стал бесплатным](../news/openclaw-free-hosting.md))
- [[verifier-tax-tool-agent-safety]] ([Verifier Tax: компромисс между безопасностью и успехом у tool-using агентов](../concepts/verifier-tax-tool-agent-safety.md))
