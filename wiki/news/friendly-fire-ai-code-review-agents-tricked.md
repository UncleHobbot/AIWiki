---
title: "Friendly Fire — AI Code-Review Agents Tricked Into Running Malicious Code"
title_ru: "Friendly Fire — ИИ-агенты ревью кода обманом запускают вредоносный код"
category: news
tags: [prompt-injection, code-review, claude-code, codex, autonomous-approval, security]
aliases: [Friendly Fire, AI Now friendly fire, readme payload injection]
confidence: high
date: 2026-07-11
updated: 2026-07-11
sources:
  - https://thehackernews.com/2026/07/friendly-fire-ai-agents-built-to-catch.html
---

## Summary
AI Now's **Friendly Fire** proof-of-concept shows that AI agents built to *catch* malicious code — Claude Code and Codex — can be tricked into *running* it. When autonomous command approval is enabled, payloads planted in a `README.md` are executed on the host because the agent follows instructions embedded in repository content it is supposed to review.

## Key Ideas
- **The inversion:** agents designed to detect malicious code are turned into execution vectors for that same code.
- **Mechanism:** a payload hidden in a `README.md` (or similar repo content the agent reads) instructs the agent to run a command; with autonomous command approval enabled, it executes on the host without a human gate.
- **Affected:** Claude Code and Codex (named in the PoC) — any agent that both reads repo content and executes commands with auto-approval.
- **Root cause:** the agent conflates *data it reads* (README content) with *instructions it must follow* — the same data/instruction conflation that underlies all prompt injection, but now the "agent" is the code reviewer itself.
- Part of the escalating 2026 pattern: [[duneslide-cursor-sandbox-escape]], [[guardfall-coding-agent-shell-injection]], [[agentjacking-attack]].

## Details
Friendly Fire is the sharpest illustration yet of why autonomous command approval is dangerous for code-review agents. The defender/attacker role reversal is the headline: the very tool a team deploys for security becomes the execution path for the payload. The structural fix is the one this wiki keeps returning to — separate the read context from the act context, and never auto-approve commands derived from untrusted repo content. See [[arc-gate-prompt-injection-proxy]] and [[hard-gates-over-soft-prompts]] for the defense pattern.

## Related Entries
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))

---
<!-- RU -->

## Краткое описание
PoC **Friendly Fire** от AI Now показывает: ИИ-агенты, созданные *ловить* вредоносный код — Claude Code и Codex —可以被 обманом заставить его *выполнять*. При включённом автономном подтверждении команд payload, спрятанный в `README.md`, выполняется на хосте, потому что агент следует инструкциям, встроенным в контент репозитория, который он должен ревьюить.

## Ключевые идеи
- **Инверсия:** агенты для обнаружения вредоносного кода превращаются в вектор его выполнения.
- **Механизм:** payload в `README.md` инструктирует агента запустить команду; при auto-approval она выполняется на хосте без человеческого шлюза.
- **Затронуты:** Claude Code и Codex — любой агент, читающий контент репо и выполняющий команды с auto-approval.
- **Корень:** агент смешивает *данные, которые читает* (контент README), с *инструкциями, которым должен следовать* — та же конфляция данных/инструкций, что лежит в основе prompt injection.
- Часть эскалации 2026: [[duneslide-cursor-sandbox-escape]], [[guardfall-coding-agent-shell-injection]], [[agentjacking-attack]].

## Подробнее
Friendly Fire — ярчайшая иллюстрация опасности автономного подтверждения команд для ревью-агентов. Инверсия ролей защитник/атакующий — заголовок: инструмент, развёрнутый для безопасности, становится путём выполнения payload. Структурный фикс — разделять read-context и act-context и никогда не автоутверждать команды из недоверенного контента репо.

## Связанные записи
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
