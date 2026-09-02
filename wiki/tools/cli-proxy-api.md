---
title: "CLIProxyAPI — Subscription CLIs Exposed as Local OpenAI/Claude/Gemini APIs"
title_ru: "CLIProxyAPI — подписочные CLI как локальные OpenAI/Claude/Gemini API"
category: tools
tags: [proxy, kimi, codex, claude-code, gemini, oauth, load-balancing, self-hosted]
aliases: [CLIProxyAPI, cli proxy api, router-for-me]
confidence: high
updated: 2026-09-01
sources:
  - https://github.com/router-for-me/CLIProxyAPI
---

## Summary
CLIProxyAPI is a Go proxy server (~49.8k stars, very active) that wraps subscription-backed AI CLI tools — Codex, Claude Code, Gemini/Antigravity, Grok Build, and **Kimi** (K3 and K2.7 Code via OAuth) — behind OAuth login and exposes them as local OpenAI-, Gemini-, and Claude-compatible API endpoints. Any compatible client can then use those subscriptions without provider API keys.

## Key Ideas
- **The pitch:** turn subscription entitlements (already paid for) into programmable API endpoints — no per-token API billing.
- **Broad compatibility:** streaming/non-streaming/WebSocket, function calling, image input; multi-account round-robin load balancing; OpenAI-compatible upstreams (e.g. OpenRouter).
- **Kimi inside everything:** explicit Kimi K3 / K2.7 Code support makes it a one-stop proxy for the wiki's monitored Chinese models inside Claude Code/Codex-style tools.
- **Ops maturity:** Docker, Management API, reusable Go SDK, desktop GUI wrapper (EasyCLIProxyAPI); 3.6k commits, MIT.
- **Caveats:** pooling OAuth tokens from personal subscriptions likely violates provider ToS (ban risk); local `auths/` credential storage; aggressive third-party relay sponsorship raises trust questions. Position accordingly.

## Details
CLIProxyAPI is the infrastructure expression of the same arbitrage that tools like [[9router-free-ai-coding]] and similar app-level routers play at the app level. Its scale (50k stars) signals how much demand exists for subscription-as-API. The ToS risk is the honest headline: providers are actively tightening client allow-lists (see [[zai-max-plan-undisclosed-weekly-limit]] and the OpenCode subscription cutoff), and proxies like this sit directly in the blast radius.

## Related Entries
- [[kimi-code-cli]] ([Kimi Code CLI](kimi-code-cli.md))
- [[9router-free-ai-coding]] ([9router](9router-free-ai-coding.md))
- [[unify-chat-provider-copilot-byok]] ([Unify Chat Provider](unify-chat-provider-copilot-byok.md))
- [[zai-max-plan-undisclosed-weekly-limit]] ([z.ai Max Plan Weekly Limit](../news/zai-max-plan-undisclosed-weekly-limit.md))

---
<!-- RU -->

## Краткое описание
CLIProxyAPI — прокси-сервер на Go (~49.8k звёзд, очень активный), который оборачивает подписочные AI CLI-инструменты — Codex, Claude Code, Gemini/Antigravity, Grok Build и **Kimi** (K3 и K2.7 Code через OAuth) — и выставляет их как локальные эндпоинты, совместимые с OpenAI, Gemini и Claude. Любой совместимый клиент может использовать эти подписки без API-ключей провайдера.

## Ключевые идеи
- **Суть:** превратить подписочные права (уже оплаченные) в программируемые API-эндпоинты — без потокенной оплаты API.
- **Широкая совместимость:** streaming/WebSocket, function calling, изображения; round-robin балансировка мультиаккаунтов; OpenAI-совместимые апстримы (OpenRouter).
- **Kimi везде:** явная поддержка Kimi K3 / K2.7 Code делает его универсальным прокси для китайских моделей внутри Claude Code/Codex-подобных инструментов.
- **Зрелость:** Docker, Management API, Go SDK, GUI-обёртка; 3.6k коммитов, MIT.
- **Оговорки:** пулинг OAuth-токенов личных подписок, вероятно, нарушает ToS провайдеров (риск бана); хранение кредов локально; агрессивный спонсорство сторонних релеев поднимает вопросы доверия.

## Подробнее
CLIProxyAPI — инфраструктурное выражение того же арбитража, что инструменты вроде [[9router-free-ai-coding]] играют на уровне приложений. Масштаб (50k звёзд) показывает спрос на «подписку как API». Риск ToS — честный заголовок: провайдеры активно закручивают гайки клиентских allow-list, и такие прокси — прямо в зоне поражения.

## Связанные записи
- [[kimi-code-cli]] ([Kimi Code CLI](kimi-code-cli.md))
- [[9router-free-ai-coding]] ([9router](9router-free-ai-coding.md))
- [[unify-chat-provider-copilot-byok]] ([Unify Chat Provider](unify-chat-provider-copilot-byok.md))
- [[zai-max-plan-undisclosed-weekly-limit]] ([z.ai Max Plan Weekly Limit](../news/zai-max-plan-undisclosed-weekly-limit.md))
