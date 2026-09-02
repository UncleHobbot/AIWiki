---
title: "geo-optimize-site — Codex Skill for Generative Engine Optimization"
title_ru: "geo-optimize-site — Codex-скилл для генеративной оптимизации поисковых движков"
category: tips
tags: [geo, seo, skill, codex, llms-txt, structured-data, ai-search]
aliases: [GEO, generative engine optimization, geo-optimize-site]
confidence: medium
updated: 2026-09-01
sources:
  - https://github.com/kyliamet/geo-optimize-site
---

## Summary
A Codex skill (SKILL.md format, MIT) for auditing and implementing **Generative Engine Optimization (GEO)** — making websites easier for AI answer engines to discover, understand, quote, and cite, while preserving factual accuracy, accessibility, and conventional SEO. The transferable insight: GEO complements SEO rather than replacing it, and the hard part is *verifying propagation*, not editing pages.

## Key Ideas
- **Coverage:** answer-first page structure, crawlable content, metadata/canonicals, Schema.org JSON-LD, sitemaps, `llms.txt`, crawler policy, internal links, alt text, post-implementation validation (ties into [[llms-txt-mcp-agent-skills]]).
- **Audit-before-edit workflow;** requires explicit user authorization before staging, committing, pushing, or opening PRs.
- **The distinctive part — propagation state taxonomy:** source readiness (`source-not-fixed`, `source-unverified`, `site-fixed`, `crawl-signals-updated`) and engine state (`current-observation`, `engine-stale`, `propagated`, `unable-to-verify`); "propagated" is reserved for a *measured* stale-to-correct transition.
- Install to `~/.codex/skills/` or via `$skill-installer`; no API keys.
- 0-star community project, but the taxonomy and the GEO framing are the substantive content.

## Details
As answer engines (ChatGPT, Perplexity, Claude) replace search traffic, "is my site quotable by AI" becomes an engineering discipline with its own failure mode: you fix the page, but the engine keeps serving the stale answer for weeks. The skill's propagation taxonomy formalizes that gap — a fix isn't done until a *measured* observation confirms the engine updated. That verification rigor is what makes this more than an SEO checklist.

## Related Entries
- [[llms-txt-mcp-agent-skills]] ([llms.txt + MCP + Skills](llms-txt-mcp-agent-skills.md))
- [[stop-slop-skill]] ([stop-slop Skill](stop-slop-skill.md))

---
<!-- RU -->

## Краткое описание
Codex-скилл (формат SKILL.md, MIT) для аудита и внедрения **Generative Engine Optimization (GEO)** — making сайты удобнее для обнаружения, понимания, цитирования ИИ-ответчиками при сохранении фактической точности, доступности и обычного SEO. Переносимая идея: GEO дополняет SEO, а самая сложная часть — *верификация распространения*, а не правка страниц.

## Ключевые идеи
- **Охват:** структура «ответ вперёд», крауляемый контент, метаданные/канонические, Schema.org JSON-LD, sitemaps, `llms.txt`, политика краулеров, внутренние ссылки, alt-текст, валидация (связь с [[llms-txt-mcp-agent-skills]]).
- **Workflow «сначала аудит»;** явная авторизация пользователя перед commit/push/PR.
- **Отличительная часть — таксономия состояний распространения:** готовность источника (`source-not-fixed`, `source-unverified`, `site-fixed`, `crawl-signals-updated`) и состояние движка (`current-observation`, `engine-stale`, `propagated`, `unable-to-verify`); «propagated» — только для *измеренного* перехода.
- Установка в `~/.codex/skills/` или через `$skill-installer`; без API-ключей.

## Подробнее
Пока ответчики (ChatGPT, Perplexity, Claude) заменяют поисковый трафик, «цитируем ли я ИИ» становится инженерной дисциплиной со своим режимом отказа: страницу починили, а движок неделями раздаёт устаревший ответ. Таксономия распространения формализует этот разрыв — фикс не завершён, пока *измеренное* наблюдение не подтвердит обновление движка. Именно эта верификационная строгость отличает скилл от SEO-чеклиста.

## Связанные записи
- [[llms-txt-mcp-agent-skills]] ([llms.txt + MCP + Skills](llms-txt-mcp-agent-skills.md))
- [[stop-slop-skill]] ([stop-slop Skill](stop-slop-skill.md))
