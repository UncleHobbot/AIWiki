---
title: "Claude Security Plugin: Built-in Vulnerability Review for Agent Code"
title_ru: "Плагин безопасности Claude: встроенная проверка уязвимостей в коде агента"
category: news
tags: [anthropic, claude, security, plugin, code-review, managed-agents, sandbox, vulnerability-detection, agentic]
aliases: [Claude security guidance plugin, Claude code security review, Claude managed agents sandbox]
confidence: high
date: 2026-05-28
updated: 2026-05-28
sources:
  - https://thehackernews.com/2026/05/threatsday-bulletin-claude-security.html
---

## Summary
Anthropic announced two new security features: a self-hosted sandbox for Claude Managed Agents that keeps execution on your own infrastructure, and a security-guidance plugin that makes Claude automatically review its own code changes for common vulnerabilities in the same session they are introduced.

## Key Ideas
- **Security-guidance plugin**: runs automatically once installed — no invocation, no separate command. Reviews each code change Claude produces for injection flaws, unsafe deserialization, and unsafe DOM APIs before the PR is created.
- **Same-session remediation**: when the plugin finds an issue, Claude fixes it in the same session, so vulnerabilities don't reach human reviewers downstream.
- **Self-hosted sandbox for Managed Agents**: described by Red Hat as "outsourcing the 'thinking' while keeping the 'doing' on your own infrastructure." Enterprise teams get Claude's reasoning without sensitive code leaving their environment.
- **Reduces security review load**: the explicit goal is shifting routine vulnerability checks from human code reviewers to the agent itself, freeing reviewers for higher-judgment decisions.
- **Vulnerability classes covered**: injection, unsafe deserialization, unsafe DOM APIs (the announcement mentions common categories; the full list lives in the plugin's own instructions).

## Details
This release reflects a pattern emerging across AI coding tools: the agent that writes code is also responsible for auditing it. Rather than a separate security scan pass after generation, the security-guidance plugin operates inline — Claude reviews what it just wrote before suggesting it.

For enterprise deployments, the self-hosted sandbox addresses a key adoption blocker: regulated industries that cannot send proprietary code to external infrastructure. The "think externally, do locally" architecture lets Claude reason about the codebase via its API while all execution (file reads, test runs, patches) happens on the org's own hardware.

The announcement landed in the same week as a malicious npm package (mouse5212-super-formatter) targeted Claude's `/mnt/user-data` directory, and attackers distributing fake Claude installers via compromised YouTube channels — suggesting an emerging threat landscape specifically targeting Claude AI tool users.

## Related Entries
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[malware-slop-npm-claude-user-directory]] ([Malware-Slop: npm Package Targeting Claude User Directory](../news/malware-slop-npm-claude-user-directory.md))
- [[product-claude-code]] ([Claude Code](../agents/product-claude-code.md))

---
<!-- RU -->

## Краткое описание
Anthropic объявила два новых защитных функции: self-hosted sandbox для Claude Managed Agents и плагин безопасности, который автоматически проверяет код, написанный Claude, на распространённые уязвимости прямо в той же сессии.

## Ключевые идеи
- **Плагин безопасности**: запускается автоматически после установки — без явного вызова. Проверяет каждое изменение кода от Claude на инъекции, небезопасную десериализацию и небезопасные DOM API до создания PR.
- **Исправление в той же сессии**: при обнаружении проблемы Claude исправляет её немедленно, до отправки кода на проверку людям.
- **Self-hosted sandbox для Managed Agents**: позволяет «думать снаружи, делать внутри» — рассуждения Claude через API, вся исполнение (чтение файлов, тесты, патчи) остаётся на инфраструктуре организации.
- **Снижение нагрузки на проверяющих**: цель — перенести рутинные проверки безопасности с людей на агента, оставив людям высокоуровневые решения.
- **Классы уязвимостей**: инъекции, небезопасная десериализация, небезопасные DOM API.

## Подробнее
Этот релиз отражает нарастающую тенденцию в AI-разработке: агент, пишущий код, сам же его и аудирует. Вместо отдельного прогона проверки безопасности после генерации, плагин работает встроенно — Claude проверяет только что написанный код до того, как его предложить.

Объявление совпало по времени с атаками на пользователей Claude: вредоносный npm-пакет нацелился на каталог `/mnt/user-data`, а поддельные установщики Claude распространялись через скомпрометированные YouTube-каналы.

## Связанные записи
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[malware-slop-npm-claude-user-directory]] ([Malware-Slop: npm Package Targeting Claude User Directory](../news/malware-slop-npm-claude-user-directory.md))
- [[product-claude-code]] ([Claude Code](../agents/product-claude-code.md))
