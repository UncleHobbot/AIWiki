---
title: "Equibles: Self-Hosted MCP Server for U.S. Financial Data"
title_ru: "Equibles: Самостоятельно размещаемый MCP-сервер для финансовых данных США"
category: tools
tags: [mcp, financial-data, local-llm, open-source, self-hosted]
confidence: medium
updated: 2026-05-22
sources:
  - https://github.com/daniel3303/Equibles
  - https://www.reddit.com/r/LocalLLaMA/comments/1te2jko/i_built_a_selfhosted_opensource_mcp_server_that/
---

## Summary

Equibles is a self-hosted, open-source MCP server that scrapes and serves public U.S. financial data — SEC filings, 13F institutional holdings, insider and congressional trades, short data, and FRED economic indicators — exposing it as MCP tools for any MCP-capable agent (Claude Code, Cursor, local model agent loops).

## Key Ideas

- No cloud dependency, no API keys, no telemetry — runs entirely on your machine
- Serves SEC filings (10-K/10-Q/8-K) with full-text search
- 13F institutional holdings, insider (Form 3/4) and congressional trades
- FINRA short volume / short interest, SEC fails-to-deliver
- FRED economic indicators, CFTC futures positioning, CBOE VIX/put-call
- Daily prices + technical indicators
- Aimed at bridging the gap between local LLM agents and real, current financial data

## Details

Built by DanielAPO, Equibles addresses a key gap for local AI agents: access to real, current data. Most local models lack the ability to query live financial datasets because they require API keys, cloud services, or web scraping that's hard to manage within an agent loop. Equibles runs a self-hosted MCP server that scrapes public data sources and serves structured financial information as MCP tools. Any MCP-capable client (Claude Code, Claude Desktop, Cursor, or custom agent loops) can call these tools directly.

The project gained significant community attention on r/LocalLLaMA (155 upvotes, 45 comments) where users praised its architecture and suggested adding a provenance layer — every answer should carry accession_number, filing date, source URL, and retrieval timestamp to prevent the LLM from mixing data sources into a false narrative.

## Related Entries
- [[gnosis-mcp]] ([Gnosis MCP](../tools/gnosis-mcp.md))
- [[mcp-financial-data-server]] ([Self-Hosted MCP Server for Financial Data](../tools/mcp-financial-data-server.md))

---
<!-- RU -->

## Краткое описание

Equibles — это открытый MCP-сервер для самостоятельного размещения, который собирает и предоставляет публичные финансовые данные США (отчёты SEC, институциональные владения 13F, инсайдерские сделки, данные по коротким позициям, экономические индикаторы FRED) через MCP-инструменты для любых AI-агентов, поддерживающих MCP.

## Ключевые идеи

- Нет зависимости от облака, API-ключей или телеметрии — всё работает на вашей машине
- Отчёты SEC (10-K/10-Q/8-K) с полнотекстовым поиском
- Институциональные владения 13F, инсайдерские сделки (Form 3/4) и сделки конгресса
- Данные FINRA по коротким объёмам/процентам, SEC fails-to-deliver
- Экономические индикаторы FRED, позиционирование CFTC, CBOE VIX/put-call
- Дневные цены + технические индикаторы
- Решает проблему доступа локальных LLM-агентов к реальным финансовым данным

## Подробнее

Equibles решает ключевую проблему локальных AI-агентов: доступ к реальным актуальным данным. Большинство локальных моделей не могут запрашивать живые финансовые наборы данных. Сервер собирает данные из публичных источников и предоставляет их как MCP-инструменты. Проект получил положительный отклик сообщества; пользователи предложили добавить слой происхождения данных для предотвращения смешивания источников.

## Связанные записи
- [[gnosis-mcp]] ([Gnosis MCP](../tools/gnosis-mcp.md))
- [[mcp-financial-data-server]] ([Self-Hosted MCP Server for Financial Data](../tools/mcp-financial-data-server.md))
