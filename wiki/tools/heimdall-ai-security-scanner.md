---
title: "Heimdall: AI-Powered Multi-Agent CLI Security Scanner"
title_ru: "Heimdall: AI-сканер безопасности с поддержкой нескольких CLI-агентов"
category: tools
tags: [security, cli, claude-code, opencode, codex, gemini-cli, vulnerability-scanning, sarif]
aliases: [Heimdall scanner, daniel-rrapi/heimdall]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/opencodeCLI/comments/1u5jqyr/my_cli_security_scanner_compatible_with_opencode/
  - https://www.reddit.com/r/opencodeCLI/comments/1u4x56u/heimdall_aipowered_security_scanner_that_works/
  - https://www.reddit.com/r/ClaudeCode/comments/1u5jous/my_cli_security_scanner_compatible_with_claude/
  - https://github.com/daniel-rrapi/heimdall
---

## Summary
Heimdall is an open-source CLI security scanner that drives whichever local AI coding agent you already have installed (Claude Code, Codex, Gemini CLI, or OpenCode) to scan source code for vulnerabilities and produce structured reports in JSON, Markdown, or SARIF.

## Key Ideas
- Language-agnostic: works across JS, Python, Go, Java, Rust, C#, PHP, etc., without framework-specific rules.
- "Bring your own AI" — Heimdall doesn't call any API itself; it shells out to local agent CLIs (Claude Code, Gemini, Codex, OpenCode), so code never leaves the machine.
- Can run multiple backends in parallel; the author notes Claude and Gemini often catch different issues, improving coverage.
- Built-in deduplication merges duplicate findings both across backends and across repeated runs.
- On a real production backend microservice (36 files), it reportedly found 407 vulnerabilities, 4 classified as critical.
- Install via a single Bash command on Linux/macOS; Windows users clone the repo and run commands via npm.

## Details
The author (u/Junk94_) open-sourced the project a few days before posting and cross-posted to r/opencodeCLI and r/ClaudeCode, framing it as a way to get a "second opinion" security audit using whatever coding agent a developer already has configured — no separate API keys or accounts needed. Output formats (JSON, Markdown, SARIF) make it straightforward to feed into CI pipelines or code-review tooling.

This is an early-stage community project (Tier 3 — Reddit self-promotion); no independent verification of the 407-vulnerability claim is available, but the architecture (agent-CLI-as-scanner-backend, with cross-backend dedup) is a reusable pattern worth noting for anyone building similar audit tooling on top of Claude Code/OpenCode/Codex.

## Related Entries
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo Code](../tools/mimo-code-xiaomi-opencode-fork.md))

---
<!-- RU -->

## Краткое описание
Heimdall — это open-source CLI-сканер безопасности, который использует уже установленный у пользователя AI coding agent (Claude Code, Codex, Gemini CLI или OpenCode) для поиска уязвимостей в коде и формирования отчётов в JSON, Markdown или SARIF.

## Ключевые идеи
- Language-agnostic: работает с JS, Python, Go, Java, Rust, C#, PHP и др. без специфичных для фреймворков правил.
- Принцип "bring your own AI" — Heimdall сам не обращается к API, а запускает локальные CLI-агенты (Claude Code, Gemini, Codex, OpenCode), поэтому код не покидает машину.
- Поддерживает параллельный запуск нескольких backend-агентов; автор отмечает, что Claude и Gemini часто находят разные проблемы, что повышает покрытие.
- Встроенная дедупликация объединяет повторяющиеся находки как между backend-ами, так и между повторными запусками.
- На реальном production-микросервисе (36 файлов) сканер якобы нашёл 407 уязвимостей, 4 из которых критические.
- Устанавливается одной Bash-командой на Linux/macOS; пользователи Windows клонируют репозиторий и запускают команды через npm.

## Подробнее
Автор (u/Junk94_) открыл исходный код проекта за несколько дней до публикации и опубликовал пост сразу в r/opencodeCLI и r/ClaudeCode, представив инструмент как способ получить "второе мнение" по безопасности с помощью уже настроенного coding agent — без отдельных API-ключей или аккаунтов. Форматы вывода (JSON, Markdown, SARIF) удобны для интеграции в CI или код-ревью.

Это раннестадийный community-проект (источник tier 3 — самопродвижение на Reddit); независимой проверки заявления о 407 уязвимостях нет, но сама архитектура (CLI-агент в роли backend-сканера с дедупликацией между backend-ами) — полезный паттерн для тех, кто строит похожие инструменты аудита на базе Claude Code/OpenCode/Codex.

## Связанные записи
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo Code](../tools/mimo-code-xiaomi-opencode-fork.md))
