---
title: "GuardFall — Shell Injection Bypasses Safety Checks in 10 of 11 AI Coding Agents"
title_ru: "GuardFall — shell-инъекция обходит защиту в 10 из 11 AI-кодинг-агентов"
category: news
tags: [shell-injection, coding-agent, security, adversa-ai, bash, guardfall]
aliases: [GuardFall, guardfall shell injection]
confidence: medium
date: 2026-06-27
updated: 2026-07-01
sources:
  - https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html
---

## Summary
Adversa AI's **GuardFall** research bypassed safety checks in 10 of 11 open-source AI coding agents by exploiting how Bash rewrites commands before execution — a decades-old shell injection class that modern agent guardrails fail to catch.

## Key Ideas
- **10 of 11** open-source AI coding agents had their safety checks bypassed by GuardFall.
- **Root cause:** how Bash rewrites/expands commands before execution — classic shell injection (metacharacters, aliasing, expansion) that agents' command-validation layers don't model correctly.
- The attack class is decades old; the finding is that bolting AI onto a shell does not automatically inherit the hard-won lessons of shell security.
- Adversa AI is the research firm; Tier 2 source (vendor research, reputable).
- Implication: coding-agent command execution is a live attack surface that pre-AI shell-security work already mapped — agents need to relearn it.

## Details
GuardFall frames the problem as a disconnect: agents generate and execute shell commands, but their safety layers reason about commands as plain strings, ignoring Bash's rewriting semantics (expansion, aliasing, quoting, history substitution). An attacker who controls part of the command (e.g. via prompt injection from a file or web page) can craft a payload that looks benign to the validator but expands into something dangerous at execution. This is the same class of bug that has plagued CGI scripts and `system()` calls for decades.

## Related Entries
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[package-hallucination-mcp]] ([Package Hallucination MCP](../tools/package-hallucination-mcp.md))

---
<!-- RU -->

## Краткое описание
Исследование **GuardFall** от Adversa AI обошло защиту в 10 из 11 open-source AI-кодинг-агентов, эксплуатируя то, как Bash переписывает команды перед выполнением — десятилетиями известный класс shell-инъекций, который современные ограждения агентов не ловят.

## Ключевые идеи
- **10 из 11** open-source AI-кодинг-агентов пропустили атаку GuardFall.
- **Корень:** Bash переписывает/раскрывает команды перед выполнением; слои валидации агента рассуждают о командах как о строках, игнорируя семантику Bash.
- Классу атак десятилетия; вывод: навешивание AI на шелл не наследует автоматически уроки безопасности шелла.
- Adversa AI — исследовательская фирма; уровень 2 (авторитетный vendor research).

## Подробнее
GuardFall формулирует проблему как разрыв: агенты генерируют и выполняют shell-команды, но их слои безопасности рассуждают о командах как о строках, игнорируя семантику переписывания Bash (раскрытие, aliasing, квотирование, history substitution). Атакующий, контролирующий часть команды (через prompt injection), создает payload, выглядящий безопасно для валидатора, но разворачивающийся в опасное при выполнении. Это тот же класс багов, что преследует CGI-скрипты и `system()` десятилетиями.

## Связанные записи
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[package-hallucination-mcp]] ([Package Hallucination MCP](../tools/package-hallucination-mcp.md))
