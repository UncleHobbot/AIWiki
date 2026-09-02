---
title: "AnyWebMCP — WebMCP Tools for Sites That Never Added Them"
title_ru: "AnyWebMCP — WebMCP-инструменты для сайтов, которые их не добавляли"
category: tools
tags: [webmcp, browser-agent, token-cost, codex, browser-extension, dom]
aliases: [AnyWebMCP, webmcp extension, web mcp any site]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/codex/comments/1w58mrq/webmcp_support_for_websites_that_havent_added_it/
  - http://anywebmcp.com
---

## Summary
**AnyWebMCP** is a browser extension that adds WebMCP tool support to websites that never implemented it. Context: OpenAI added WebMCP support to Codex on August 25 (the Microsoft/Google-proposed standard lets sites expose tools agents can call directly instead of agents reading and clicking through the DOM) — but almost no sites ship WebMCP tools. AnyWebMCP injects them site-by-site from the client side, claiming ~85% token-usage reduction for agent browsing.

## Key Ideas
- **The cost mechanism:** every agent click = read whole page → act → re-read whole page (DOM changed). On SPAs that's every click — the bulk of context-window consumption during browsing ([[browser-snapshot-format-token-cost]] documented the same effect at 5×).
- **WebMCP fixes it properly:** sites expose tools; the agent calls them directly. Codex has supported this since Aug 25.
- **The adoption gap:** most of the web will never add a new browser standard — unmaintained sites especially.
- **AnyWebMCP's answer:** a browser extension that adds the tools itself, site by site, without site cooperation.
- Works with Codex's WebMCP discovery; frames itself as bridging the gap until (if ever) sites adopt natively.

## Details
This is the client-side workaround for a protocol chicken-and-egg problem: agents got WebMCP support before websites did. If the ~85% claim holds even approximately, it converts agent browsing from a context-burning liability into a first-class tool surface — and sidesteps the per-site DOM-structure fragility documented in the opera-compact research.

## Related Entries
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](../research/browser-snapshot-format-token-cost.md))
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](../tips/mcp-tool-schema-bloat-token-cost.md))
- [[mcp-stateless-core-spec]] ([MCP 2026-07-28 Spec](../news/mcp-stateless-core-spec.md))

---
<!-- RU -->

## Краткое описание
**AnyWebMCP** — браузерное расширение, добавляющее поддержку WebMCP-инструментов сайтам, которые её так и не реализовали. Контекст: 25 августа OpenAI добавила поддержку WebMCP в Codex (стандарт от Microsoft/Google позволяет сайтам открывать инструменты, которые агент вызывает напрямую вместо чтения и кликов по DOM) — но почти ни у каких сайтов нет WebMCP-инструментов. AnyWebMCP внедряет их со стороны клиента, заявляя ~85% экономию токенов при браузинге агентом.

## Ключевые идеи
- **Механизм стоимости:** каждый клик агента = чтение всей страницы → действие → повторное чтение (DOM изменился). На SPA это каждый клик — основная доля потребления контекстного окна ([[browser-snapshot-format-token-cost]] зафиксировала тот же эффект как 5×).
- **WebMCP решает это правильно:** сайт открывает инструменты; агент вызывает их напрямую. Codex поддерживает с 25 августа.
- **Проблема внедрения:** большая часть веба никогда не добавит новый браузерный стандарт.
- **Ответ AnyWebMCP:** расширение, добавляющее инструменты само, сайт за сайтом, без участия сайта.

## Подробнее
Это клиентский обход проблемы «курицы и яйца» протокола: агенты получили поддержку WebMCP раньше сайтов. Если заявка ~85% верна хотя бы приблизительно, браузинг агента превращается из сжигателя контекста в первоклассную поверхность инструментов — и обходит хрупкость DOM-структур, задокументированную в исследовании opera-compact.

## Связанные записи
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](../research/browser-snapshot-format-token-cost.md))
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](../tips/mcp-tool-schema-bloat-token-cost.md))
- [[mcp-stateless-core-spec]] ([MCP 2026-07-28 Spec](../news/mcp-stateless-core-spec.md))
