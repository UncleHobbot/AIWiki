---
title: "Amazon Q Developer MCP Config Flaw — Repo to AWS Credential Theft (CVE-2026-12957)"
title_ru: "Уязвимость MCP-конфига Amazon Q Developer — от репо к краже AWS-ключей (CVE-2026-12957)"
category: news
tags: [amazon-q, mcp, aws, credential-theft, cve, supply-chain, security]
aliases: [CVE-2026-12957, amazon q mcp flaw, amazonq mcp.json]
confidence: high
date: 2026-06-26
updated: 2026-07-01
sources:
  - https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html
---

## Summary
A high-severity flaw (CVE-2026-12957, CVSS 8.5) in Amazon Q Developer let a single `.amazonq/mcp.json` file dropped in a cloned repository run arbitrary commands with the developer's live AWS session attached — going from `git clone` to cloud compromise with no separate consent for MCP servers. Found by Wiz Research; patched in Language Servers for AWS 1.65.0 (AWS advises 1.69.0).

## Key Ideas
- **Attack path:** Amazon Q read `.amazonq/mcp.json` from the open workspace and launched the MCP servers it defined — each a local process inheriting the developer's full environment (AWS keys, CLI tokens, SSH agent sockets).
- **Wiz PoC:** the file ran `aws sts get-caller-identity` and shipped the output to an attacker server, capturing the active AWS session.
- **The patch** adds an untrusted-MCP-server flag so the developer can reject the command before it runs.
- Affects the Language Servers for AWS runtime across VS Code, JetBrains, Eclipse, and Visual Studio plugins.
- **Part of a pattern:** Claude Code (CVE-2025-59536), Cursor (CVE-2025-54136), and Windsurf (CVE-2026-30615) all had project-level MCP config leading to command execution — repo-carried config is untrusted input.
- Second issue CVE-2026-12958 (missing symlink check → arbitrary file writes) also closed in 1.69.0.

## Details
The convenience of letting a project folder configure an AI agent is also the attack surface. AWS and Wiz frame the consent step differently — Amazon says the user trusts the workspace when prompted; Wiz reported no separate consent for the MCP servers before the fix. The throughline across vendors: turning repo config into a running process should require an explicit yes.

## Related Entries
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[package-hallucination-mcp]] ([Package Hallucination MCP](../tools/package-hallucination-mcp.md))

---
<!-- RU -->

## Краткое описание
Высокая уязвимость (CVE-2026-12957, CVSS 8.5) в Amazon Q Developer позволяла одному файлу `.amazonq/mcp.json`, положенному в склонированный репозиторий, запускать произвольные команды с активной AWS-сессией разработчика — от `git clone` до компрометации облака без отдельного согласия на MCP-серверы. Нашла Wiz Research; исправлено в Language Servers for AWS 1.65.0 (AWS рекомендует 1.69.0).

## Ключевые идеи
- **Путь атаки:** Amazon Q читает `.amazonq/mcp.json` из открытого воркспейса и запускает описанные MCP-серверы — локальные процессы, наследующие полное окружение разработчика (AWS-ключи, CLI-токены, SSH-агент).
- **PoC от Wiz:** файл запускал `aws sts get-caller-identity` и отправлял вывод атакующему, захватывая активную AWS-сессию.
- **Патч** добавляет флаг недоверенного MCP-сервера, позволяя разработчику отклонить команду.
- Часть паттерна: Claude Code (CVE-2025-59536), Cursor (CVE-2025-54136), Windsurf (CVE-2026-30615) — конфиг MCP на уровне проекта ведёт к выполнению команд; конфиг из репо — это недоверенный ввод.

## Подробнее
Удобство настройки AI-агента папкой проекта — оно же поверхность атаки. AWS и Wiz по-разному описывают шаг согласия: Amazon — пользователь доверяет воркспейсу; Wiz — до фикса отдельного согласия на MCP-серверы не было. Общий вывод: превращение конфига репо в запущенный процесс должно требовать явного согласия.

## Связанные записи
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[package-hallucination-mcp]] ([Package Hallucination MCP](../tools/package-hallucination-mcp.md))
