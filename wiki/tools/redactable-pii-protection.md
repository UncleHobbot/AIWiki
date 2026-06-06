---
title: "Redactable: PII Protection Plugin for OpenCode"
title_ru: "Redactable: защита PII для OpenCode"
category: tools
tags: [opencode, pii, privacy, message-transform, redaction, security]
aliases: [redactable, PII redaction opencode]
confidence: medium
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://www.reddit.com/r/opencode/comments/1tyi73a/
  - https://github.com/PraneelBhatia/redactable
---

## Summary

Redactable is an open-source OpenCode plugin that hooks the message transform pipeline to replace PII (phone numbers, emails, credit card numbers) with deterministic placeholders on outgoing messages and restore real values in replies — no LLM involved in the redaction path.

## Key Ideas

- **Deterministic-first detection:** Uses regex patterns plus checksum validators (Luhn for cards, MOD-97 for IBAN) rather than LLM-based NER, ensuring zero false negatives on known formats
- **Bidirectional transform:** Outgoing messages have PII replaced with placeholders (e.g., `[PHONE_1]`); incoming replies have placeholders restored to real values
- **Optional encoder NER:** An additional neural entity recognizer can be enabled for broader coverage beyond regex-detectable patterns
- **Zero LLM in redaction path:** Privacy guarantees don't depend on model behavior — the transforms are pure code
- **Hooks into OpenCode's message transform API:** Demonstrates the extensibility of OpenCode's hook system for security-critical middleware

## Details

The plugin addresses a real concern for teams using cloud-hosted LLMs: prompts often contain sensitive data (API keys in stack traces, customer emails in bug reports, payment details in logs). Redactable intercepts messages before they leave the local environment.

The architecture is intentionally simple: regex + checksum matching is fast, deterministic, and auditable. The optional NER encoder handles edge cases where PII doesn't match standard patterns (e.g., custom ID formats). The placeholder system is reversible because the mapping is stored locally for the session duration.

This is a Tier 3 community tool (single Reddit post, no benchmarks), but the approach — deterministic security middleware in the agent pipeline — is a pattern worth tracking as coding agents handle increasingly sensitive codebases.

## Related Entries

- [[agent-lifecycle-hooks-copilot-vscode]] ([Agent Lifecycle Hooks in Copilot CLI and Claude Code](../tips/agent-lifecycle-hooks-copilot-vscode.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))

---
<!-- RU -->

## Краткое описание

Redactable — плагин с открытым исходным кодом для OpenCode, который перехватывает исходящие сообщения и заменяет PII (номера телефонов, email, номера карт) детерминированными плейсхолдерами, восстанавливая реальные значения в ответах — без участия LLM.

## Ключевые идеи

- **Детерминированное обнаружение:** Регулярные выражения и валидаторы контрольных сумм (Luhn для карт, MOD-97 для IBAN), а не LLM-based NER
- **Двунаправленный трансформ:** Исходящие сообщения содержат плейсхолдеры, входящие ответы — восстановленные реальные значения
- **Опциональный NER-энкодер:** Нейронный распознаватель сущностей для случаев, не покрываемых регулярными выражениями
- **LLM не участвует в редукции:** Гарантии приватности зависят только от кода, а не от поведения модели
- **Использует API трансформации сообщений OpenCode:** Демонстрирует расширяемость системы хуков для критичного посредника безопасности

## Подробнее

Плагин решает реальную проблему команд, использующих облачные LLM: промпты часто содержат чувствительные данные (API-ключи в трассировке стека, email клиентов в баг-репортах). Redactable перехватывает сообщения до их отправки. Архитектура намеренно проста: regex + контрольные суммы — быстро, детерминированно и аудируемо. Опциональный NER обрабатывает краевые случаи. Паттерн — детерминированный security-middleware в агентном конвейере — заслуживает внимания.

## Связанные записи

- [[agent-lifecycle-hooks-copilot-vscode]] ([Agent Lifecycle Hooks in Copilot CLI and Claude Code](../tips/agent-lifecycle-hooks-copilot-vscode.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
