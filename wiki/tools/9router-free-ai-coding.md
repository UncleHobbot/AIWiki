---
title: "9router: Free AI Coding Router with RTK Token Saver"
title_ru: "9router: бесплатный роутер для AI-кодинга с RTK Token Saver"
category: tools
tags: [coding-agent, token-saving, free-ai, router, claude-code, codex, cursor, opencode, fallback, mcp]
aliases: [9router, 9Router, RTK token saver, free AI coding router]
confidence: medium
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://github.com/decolua/9router
---

## Summary
9router is an open-source local proxy router that connects any AI coding tool (Claude Code, Codex, Cursor, Cline, Copilot, OpenClaw) to 40+ providers including completely free tiers, automatically saves 20–40% of tokens per request via RTK compression, and falls back across tiers (subscription → cheap → free) so you never stop mid-session.

## Key Ideas
- **RTK Token Saver**: auto-compresses `tool_result` content (git diff, grep, find, ls, tree outputs) before sending to the LLM — saves 20–40% input tokens per request. Example: 47K tokens → 28K tokens, same context, same answer.
- **3-tier smart fallback**: Subscription tier (Claude Code Pro, Codex, GitHub Copilot) → Cheap tier (GLM $0.6/1M, MiniMax $0.2/1M) → Free tier (Kiro AI: free Claude unlimited; OpenCode Free: no auth; Vertex AI: $300 GCP credits). Auto-switches when quota runs out or errors occur.
- **Format translation**: seamlessly converts between OpenAI ↔ Claude ↔ Gemini ↔ Cursor ↔ Kiro ↔ Vertex ↔ Ollama ↔ Antigravity formats — any tool that speaks a custom OpenAI endpoint works.
- **Zero-cost path**: RTK + Kiro AI + OpenCode Free = $0/month with 20–40% token savings on top.
- **Caveman Mode**: injects a "be terse and technical" prompt that reduces output tokens by up to 65% while preserving full technical accuracy.

## Details

### Setup (3 steps)

```bash
npm install -g 9router
9router
# Dashboard opens at http://localhost:20128
```

Then in your coding tool, set:
- Endpoint: `http://localhost:20128/v1`
- API Key: (copy from dashboard)
- Model: `kr/claude-sonnet-4.5` (Kiro AI, free)

### How RTK Works

Tool outputs like `git diff`, `grep`, `find`, `ls`, and `tree` often consume 30–50% of prompt budget. RTK detects them and applies lossless compression:

- **Filters**: git-diff, git-status, grep, find, ls, tree, dedup-log, smart-truncate, read-numbered, search-list
- **Auto-detect**: peeks the first 1KB of each tool_result, picks the right filter
- **Safe by design**: if a filter fails, RTK silently keeps the original — errors never break requests
- **Universal**: runs before format translation, works across all provider formats

Without RTK: 47K tokens. With RTK: 28K tokens (40% saved, same answer).

### Free Provider Tiers (May 2026)

| Provider | Cost | Models | Notes |
|---|---|---|---|
| Kiro AI | $0 unlimited | Claude 4.5 + GLM-5 + MiniMax | Best free option |
| OpenCode Free | $0 unlimited | Auto-fetch | No auth required |
| Vertex AI | $300 credits | Gemini 3 Pro + DeepSeek + GLM-5 | New GCP accounts |

### Cost Display Note

The dashboard "costs" are for tracking purposes only — they show what you *would have paid* using paid APIs directly. 9router itself never charges anything. If you're using Kiro AI (free unlimited), your actual cost is $0 even if the dashboard shows hundreds of dollars in "cost."

### Caveman Mode

A unique feature: injects a brief prompt telling the model to reply in compressed, terse, technical language — cuts output tokens by up to 65% while keeping full technical accuracy. Inspired by the community `caveman` skill in the Matt Pocock skills repo.

## Related Entries
- [[github-copilot-pricing-exodus]] ([GitHub Copilot Usage-Based Pricing Triggers User Exodus](../news/github-copilot-pricing-exodus.md))
- [[freebuff]] ([freebuff: Free Coding Agent with Top Open Models](../tools/freebuff.md))
- [[claude-code-frameworks]] ([Claude Code Skill Frameworks: GSD, Superpowers, Ouroboros, Han](../tools/claude-code-frameworks.md))
- [[choose-llm-api-self-host-hybrid]] ([How to Choose an LLM for Your AI Agent: API, Self-Host, or Hybrid](../tips/choose-llm-api-self-host-hybrid.md))

---
- [[cli-proxy-api]] ([CLIProxyAPI](cli-proxy-api.md))
- [[openusage-subscription-tracker]] ([OpenUsage Subscription Tracker](openusage-subscription-tracker.md))
<!-- RU -->

## Краткое описание
9router — open-source локальный прокси-роутер, который подключает любой AI coding-инструмент (Claude Code, Codex, Cursor, Cline, Copilot, OpenClaw) к 40+ провайдерам, включая полностью бесплатные тиры, автоматически экономит 20–40% токенов через сжатие RTK и переключается между тирами (подписка → дешёвый → бесплатный), чтобы работа не прерывалась.

## Ключевые идеи
- **RTK Token Saver**: автоматически сжимает содержимое `tool_result` (git diff, grep, find, ls, tree) перед отправкой в LLM — экономия 20–40% входных токенов на запрос. Пример: 47K токенов → 28K, тот же контекст, тот же ответ.
- **3-уровневый умный fallback**: подписка (Claude Code Pro, Codex, Copilot) → дёшево (GLM $0,6/1M, MiniMax $0,2/1M) → бесплатно (Kiro AI: бесплатный Claude unlimited; OpenCode Free: без авторизации; Vertex AI: $300 кредитов GCP).
- **Трансляция форматов**: бесшовная конвертация между OpenAI ↔ Claude ↔ Gemini ↔ Cursor ↔ Kiro ↔ Vertex ↔ Ollama ↔ Antigravity — работает с любым инструментом, поддерживающим кастомный OpenAI endpoint.
- **Нулевой путь**: RTK + Kiro AI + OpenCode Free = $0/месяц при экономии 20–40% токенов.
- **Caveman Mode**: внедряет промпт «будь кратким и техническим» — сокращает выходные токены до 65% при сохранении полной технической точности.

## Подробнее

**Установка (3 шага):**
```bash
npm install -g 9router
9router   # Дашборд на http://localhost:20128
```
В своём инструменте укажи: Endpoint `http://localhost:20128/v1`, API Key с дашборда, Model `kr/claude-sonnet-4.5` (Kiro AI, бесплатно).

**Как работает RTK:** инструментные выводы (`git diff`, `grep`, `find`, `ls`, `tree`) часто съедают 30–50% бюджета промпта. RTK определяет их, применяет безопасное сжатие. Если фильтр не срабатывает — молча сохраняет оригинал, ошибки не ломают запросы.

**«Стоимость» на дашборде** — только для отслеживания. 9router никогда ничего не списывает. Если вы используете Kiro AI (бесплатно), реальные расходы = $0, даже если дашборд показывает сотни долларов «экономии».

## Связанные записи
- [[github-copilot-pricing-exodus]] ([GitHub Copilot Usage-Based Pricing Triggers User Exodus](../news/github-copilot-pricing-exodus.md))
- [[freebuff]] ([freebuff: Free Coding Agent with Top Open Models](../tools/freebuff.md))
- [[claude-code-frameworks]] ([Claude Code Skill Frameworks: GSD, Superpowers, Ouroboros, Han](../tools/claude-code-frameworks.md))
- [[choose-llm-api-self-host-hybrid]] ([How to Choose an LLM for Your AI Agent: API, Self-Host, or Hybrid](../tips/choose-llm-api-self-host-hybrid.md))
