---
title: "Fully Local Agentic Web Research Stack (No Cloud APIs)"
title_ru: "Полностью локальный стек агентного веб-исследования (без облачных API)"
category: tips
tags: [agentic-web, local-llm, searxng, camoufox, mcp, reranker, self-hosted]
aliases: [local web research stack, kmarble local agent stack]
confidence: medium
updated: 2026-07-01
sources:
  - https://kmarble.dev/posts/completely-local-agentic-web-research/
  - https://www.reddit.com/r/LocalLLaMA/comments/1ukpd5y/whats_your_actual_agentic_web_research_stack/
---

## Summary
A practitioner's reference architecture for a fully local agentic web-research pipeline — search, fetch, render, cache, and relevance-score the real web without any cloud API calls, all exposed to the agent through a single MCP server.

## Key Ideas
- **Search:** self-hosted **SearXNG** (metasearch across dozens of engines).
- **Cache/index layer:** **Hister** — stores every fetched page so sessions are reproducible and content that later disappears is preserved.
- **HTTP fetch:** **rnet** (now **wreq**) — TLS-fingerprinted requests that bypass basic anti-bot checks.
- **Browser fallback:** **camofox** (wrapping Camoufox) — headless browser for JS-heavy pages and managed Cloudflare challenges.
- **Relevance scoring:** local **qwen3-reranker-4b**.
- **Surface:** one MCP server ties the layers together; no cloud API in the chain.
- Hard-won notes: Reddit 403s on Firefox fingerprints from datacenter IPs but Safari passes; managed Cloudflare challenges require full browser render regardless of fingerprint.

## Details
The inference layer gets most attention, but getting an agent to actually browse the real web reliably is its own engineering problem. This stack treats it as a layered pipeline where each stage has a fallback, and where a persistent cache absorbs the fact that pages mutate or vanish between sessions. The fingerprint-vs-CDN notes are the kind of operational detail that only surfaces from running the pipeline in production.

## Related Entries
- [[cloakbrowser-stealth-chromium]] ([CloakBrowser Stealth Chromium](../tools/cloakbrowser-stealth-chromium.md))
- [[world-model-mcp]] ([World Model MCP](../tools/world-model-mcp.md))
- [[ollama]] ([Ollama](../tools/ollama.md))

---
<!-- RU -->

## Краткое описание
Референс-архитектура практиков для полностью локального пайплайна агентного веб-исследования: поиск, fetch, рендер, кэш и оценка релевантности настоящего веба без единого облачного API, всё подключается к агенту через один MCP-сервер.

## Ключевые идеи
- **Поиск:** self-hosted **SearXNG** (метапоиск по десяткам движков).
- **Слой кэша/индекса:** **Hister** — хранит каждую загруженную страницу, что делает сессии воспроизводимыми и сохраняет исчезающий контент.
- **HTTP-fetch:** **rnet** (ныне **wreq**) — запросы с TLS-fingerprint, обходящие базовые антибот-проверки.
- **Браузерный fallback:** **camofox** (поверх Camoufox) — headless-браузер для JS-тяжёлых страниц и managed Cloudflare challenges.
- **Оценка релевантности:** локальный **qwen3-reranker-4b**.
- **Поверхность:** один MCP-сервер связывает слои; ни одного облачного API в цепочке.
- Проверенные на практике нюансы: Reddit отдаёт 403 на Firefox-fingerprint с datacenter IP, но пропускает Safari; managed Cloudflare challenges требуют полного рендера браузера вне зависимости от fingerprint.

## Подробнее
Слой инференса привлекает больше всего внимания, но заставить агента реально и надёжно браузить веб — отдельная инженерная задача. Этот栈 рассматривает её как многослойный пайплайн, где у каждого этапа есть fallback, а постоянный кэш компенсирует изменение или исчезновение страниц между сессиями. Нюансы про fingerprint-vs-CDN — операционная деталь, всплывающая только в продакшене.

## Связанные записи
- [[cloakbrowser-stealth-chromium]] ([CloakBrowser Stealth Chromium](../tools/cloakbrowser-stealth-chromium.md))
- [[world-model-mcp]] ([World Model MCP](../tools/world-model-mcp.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
