---
title: "GitHub Copilot SDK: Embed Copilot Agent into Any App"
title_ru: "GitHub Copilot SDK: встраивание агента Copilot в любое приложение"
category: tools
tags: [github-copilot, sdk, agent, byok, multi-platform, json-rpc, cli, python, typescript, go, dotnet, java]
aliases: [Copilot SDK, GitHub Copilot Agent SDK, copilot-sdk]
confidence: high
date: 2026-05-24
updated: 2026-05-24
sources:
  - https://github.com/github/copilot-sdk
---

## Summary
The GitHub Copilot SDK (public preview) exposes the same agent runtime that powers Copilot CLI as a programmable SDK for Python, TypeScript, Go, .NET, and Java. Applications define agent behavior; Copilot handles planning, tool invocation, and file edits via JSON-RPC to the CLI server.

## Key Ideas
- **Five languages, one engine**: Python, TypeScript, Go, .NET, Java SDKs — all communicating with the Copilot CLI server via JSON-RPC. Rust SDK available in technical preview.
- **No custom orchestration needed**: the SDK exposes the production-tested Copilot CLI agent runtime — planning, tool invocation, file editing — as library calls.
- **BYOK (Bring Your Own Key)**: configure your own API keys from OpenAI, Azure AI Foundry, or Anthropic to use the SDK without a GitHub subscription. BYOK uses key-based auth only (no Entra ID or managed identities).
- **Multiple auth methods**: GitHub signed-in user (OAuth credentials from Copilot CLI login), OAuth GitHub App, environment variables (`COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN`), or BYOK.
- **Bundled CLI**: Node.js, Python, and .NET SDKs bundle the Copilot CLI automatically. Go and Rust require separate CLI installation.
- **Custom agents and skills**: extend SDK behavior by implementing custom agents, skills, and tool logic.
- **Permission handler**: tool execution is governed by a per-SDK permission handler — applications can approve, deny, or customize tool calls even when all tools are enabled by default.

## Details
The SDK architecture is: `Your Application → SDK Client → JSON-RPC → Copilot CLI (server mode)`. The SDK manages the CLI process lifecycle automatically; you can also connect to an external CLI server for advanced deployments.

BYOK is the key feature for teams that want Copilot agent capabilities without routing traffic through GitHub authentication — useful for enterprise deployments on Azure or Anthropic's API. Standard usage (non-BYOK) counts toward the premium request quota per the Copilot CLI billing model.

The SDK is currently in **public preview** — functional and used in development/testing, but may not be suitable for production use yet.

## Related Entries
- [[github-copilot-app]] ([GitHub Copilot App](../news/github-copilot-app.md))
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration](../agents/agent-orchestration-multi-model-framework.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))

---
<!-- RU -->

## Краткое описание
GitHub Copilot SDK (публичная preview) открывает агентный рантайм Copilot CLI как программируемый SDK для Python, TypeScript, Go, .NET и Java. Приложение задаёт поведение агента; Copilot управляет планированием, вызовом инструментов и редактированием файлов через JSON-RPC.

## Ключевые идеи
- **Пять языков, один движок**: Python, TypeScript, Go, .NET, Java — все общаются с сервером Copilot CLI через JSON-RPC. Rust SDK доступен в technical preview.
- **Без собственной оркестрации**: SDK предоставляет готовый агентный рантайм Copilot CLI как библиотечные вызовы.
- **BYOK (собственные API-ключи)**: настройте ключи OpenAI, Azure AI Foundry или Anthropic — без подписки GitHub. BYOK работает только с ключевой аутентификацией.
- **Несколько методов аутентификации**: OAuth GitHub, переменные окружения, BYOK.
- **Встроенный CLI**: SDK для Node.js, Python и .NET включают Copilot CLI автоматически. Go и Rust требуют отдельной установки.
- **Кастомные агенты и скиллы**: расширяйте поведение SDK своей логикой агентов, скиллов и инструментов.
- **Обработчик прав**: выполнение инструментов контролируется permission handler — приложение может разрешать, запрещать или настраивать вызовы.

## Подробнее
Архитектура: `Приложение → SDK Client → JSON-RPC → Copilot CLI (режим сервера)`. SDK автоматически управляет жизненным циклом процесса CLI.

BYOK — ключевая функция для команд, которые хотят возможности агента Copilot без маршрутизации через аутентификацию GitHub. Стандартное использование учитывается в квоте premium requests по модели тарификации Copilot CLI.

SDK сейчас в **публичной preview** — функционален для разработки и тестирования, но может быть не готов для продакшена.

## Связанные записи
- [[github-copilot-app]] ([GitHub Copilot App](../news/github-copilot-app.md))
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration](../agents/agent-orchestration-multi-model-framework.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
