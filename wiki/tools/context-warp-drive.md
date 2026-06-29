---
title: "Context Warp Drive: Deterministic Folding for LLM Agent Continuity"
title_ru: "Context Warp Drive: детерминированная свёртка для непрерывности LLM-агентов"
category: tools
tags: [context-management, agent-continuity, compaction, prompt-cache, llm-agent]
aliases: [Context Warp Drive, context-warp-drive, deterministic folding]
confidence: medium
updated: 2026-06-29
sources:
  - https://github.com/dogtorjonah/context-warp-drive
  - https://www.reddit.com/r/ClaudeCode/comments/1uiz5fj/deterministic_folding_for_llm_agents_continuity/
---

## Summary
Context Warp Drive is an open-source continuity engine for LLM agents that replaces lossy LLM-based "compaction" (summarization) with **deterministic folding** — older context is compressed into deterministic skeletons so the active context "sawtooths" (builds up, then drops back to a clean floor) without losing continuity or trashing the provider prompt cache.

## Key Ideas
- **Two bad incumbents it replaces**: (1) riding a giant 1M–2M context window until it fills, and (2) using an LLM to summarize older messages ("compaction").
- **Why compaction fails**: LLM summaries are inconsistent, cost an extra model round-trip, quietly drop the exact identifiers an agent needs (UUIDs, paths, hashes), and constantly rewrite the prefix — which invalidates the provider's prompt cache.
- **Deterministic folding**: as the agent works, older context is folded into deterministic skeletons. The active context sawtooths — building up efficiently, then dropping back down — without losing continuity.
- **Cache-friendly**: because folding is deterministic (not re-generated prose), the stable prefix preserves prompt-cache hits, avoiding repeated reprocessing costs.
- **The 95% insight**: ~95% of what an agent carries on a long task isn't needed verbatim — it can be represented compactly while preserving the identifiers and structure the agent depends on.

## Details
The core argument is that agent long-horizon reliability is a context-management problem, not a context-window-size problem. Throwing a bigger window at it keeps everything but pays linear cost and still eventually overflows; LLM summarization keeps the window small but is lossy in exactly the ways that break agents (dropped identifiers, rewritten prefixes that bust caching).

Deterministic folding sits between these: it keeps the high-value, identifier-bearing structure intact while discarding redundant verbosity, using rules rather than a model call to produce the compressed representation. The sawtooth pattern means the agent operates near a constant active-context floor instead of creeping toward the ceiling.

## Notable Quotes
> "LLM summaries ... quietly drop the exact identifiers your agent needs (UUIDs, paths, hashes), and worst of all, they constantly rewrite the prefix — which trashes your provider prompt cache." — repo author

## Related Entries
- [[memory-skills-unified-harness]] ([Memory and Skills Are the Same Harness](../concepts/memory-skills-unified-harness.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))

---
<!-- RU -->

## Краткое описание
Context Warp Drive — open-source движок непрерывности для LLM-агентов, который заменяет теряющий данные LLM-based «compaction» (суммаризацию) на **детерминированную свёртку**: старый контекст сжимается в детерминированные «скелеты», так что активный контент «пилит» (нарастает, затем падает до чистого пола) без потери непрерывности и без инвалидации prompt-кэша провайдера.

## Ключевые идеи
- **Два плохих предшественника**: (1) ехать на гигантском окне 1M–2M до заполнения, и (2) суммаризировать старые сообщения через LLM («compaction»).
- **Почему compaction ломается**: LLM-суммари нестабильны, стоят лишний модельный round-trip, незаметно теряют именно те идентификаторы, что нужны агенту (UUID, пути, хэши), и постоянно переписывают префикс — что инвалидирует prompt-кэш провайдера.
- **Детерминированная свёртка**: по мере работы агента старый контент сворачивается в детерминированные скелеты. Активный контекст пилит — нарастает, затем падает обратно — без потери непрерывности.
- **Дружелюбность к кэшу**: поскольку свёртка детерминирована (не регенерируемая проза), стабильный префикс сохраняет попадания prompt-кэша.
- **Инсайт про 95%**: ~95% того, что агент несёт на длинной задаче, не нужно дословно — это можно представить компактно, сохранив нужные агенту идентификаторы и структуру.

## Подробнее
Главный тезис: надёжность агента на длинной дистанции — это проблема управления контекстом, а не размера окна. Большее окно сохраняет всё, но платит линейную цену и в итоге переполняется; LLM-суммаризация держит окно малым, но теряет данные именно теми способами, что ломают агентов.

Детерминированная свёртка — золотая середина: высокоценная структура с идентификаторами остаётся нетронутой, а избыточная многословность отбрасывается по правилам, а не через вызов модели. Пилообразный паттерн означает, что агент работает у постоянного «пола» активного контекста, а не ползёт к потолку.

## Связанные записи
- [[memory-skills-unified-harness]] ([Memory and Skills Are the Same Harness](../concepts/memory-skills-unified-harness.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))
