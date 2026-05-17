---
title: "Self-Hosted MCP Server for Financial Data"
title_ru: "Самохостящийся MCP-сервер для финансовых данных"
category: tools
tags: [mcp, financial-data, local-llm, open-source, self-hosted]
date: 2026-05-15
updated: 2026-05-15
sources:
  - https://www.reddit.com/r/LocalLLaMA/comments/1te2jko/i_built_a_selfhosted_opensource_mcp_server_that/
  - https://github.com/daniel3303/Equibles
---

## Summary
Equibles is a self-hosted, open-source MCP server that scrapes, stores, and serves U.S. financial data (SEC filings, 13F holdings, insider trades, congressional trades, short data, FRED indicators, stock prices, CFTC futures, CBOE VIX) and exposes it as MCP tools so any MCP-compatible AI assistant can query it directly — no cloud dependency, no API keys required for most data sources.

## Key Ideas
- Fully self-hosted "mini Bloomberg Terminal" for AI agents — runs entirely on your machine via Docker Compose
- Exposes financial data through the Model Context Protocol (MCP), compatible with Claude Desktop, Claude Code, ChatGPT Desktop, Cursor, and any MCP client
- Covers 9 data domains: SEC filings (10-K/10-Q/8-K) with full-text search, 13F institutional holdings, insider Form 3/4 trades, congressional trades, FINRA short volume/interest, SEC fails-to-deliver, FRED economic indicators, CFTC futures positioning, CBOE VIX/put-call ratios, and daily OHLCV stock prices with technical indicators
- Built on .NET 10 / C# with ParadeDB (PostgreSQL + pgvector + pg_search), deployable with a single `docker compose up`
- Optional vector embeddings via Ollama + BGE-M3 enable semantic search over SEC filings
- No telemetry, no cloud dependency — all data scraped from public U.S. government sources and cached locally
- AGPL-3.0 licensed, actively maintained (929 commits, v1.0.0 released May 15, 2026)

## Details
Equibles solves a critical gap for local LLM users: the lack of real-time, structured financial data. When running models like Qwen or Llama locally as agents, they have no access to current market information. Equibles fills this by scraping public U.S. financial data sources (SEC EDGAR, FINRA, FRED, CFTC, CBOE, Yahoo Finance) and exposing structured query tools via the MCP protocol.

The architecture consists of four Docker services: a ParadeDB database (PostgreSQL with full-text search and vector extensions), a web portal for browsing data on port 8080, an MCP server on port 8081 for AI assistant integration, and background worker scrapers that continuously pull data from all configured sources. Data begins populating within minutes of startup.

Connecting to AI clients is straightforward. For Claude Desktop, add the MCP server URL to `claude_desktop_config.json`. For Claude Code, use `claude mcp add equibles --transport http http://localhost:8081/mcp`. ChatGPT Desktop and other MCP clients are also supported. Once connected, you can ask natural-language questions like "Who are the top institutional holders of AAPL?" or "Search Apple's latest 10-K for revenue growth discussion."

FINRA short data and FRED economic indicators require free API keys (available after registration). All other data sources work without any credentials. The system supports ticker filtering to limit syncing to specific stocks and configurable minimum sync dates for faster initial setup.

## Related Entries
- [[shokunin-memory-system]] ([Shokunin: Persistent Memory for Coding Agents](../tools/shokunin-memory-system.md))

---
<!-- RU -->

## Краткое описание
Equibles — самохостящийся open-source MCP-сервер, который собирает, хранит и отдаёт финансовые данные США (отчёты SEC, holdings 13F, инсайдерские сделки, сделки конгрессменов, шорт-данные, индикаторы FRED, котировки акций, фьючерсы CFTC, VIX) и предоставляет их как MCP-инструменты для любых AI-ассистентов с поддержкой MCP — без облачных зависимостей и без API-ключей для большинства источников данных.

## Ключевые идеи
- Полностью самохостящаяся «мини-Bloomberg Terminal» для AI-агентов — работает целиком на вашей машине через Docker Compose
- Отдаёт финансовые данные через Model Context Protocol (MCP), совместим с Claude Desktop, Claude Code, ChatGPT Desktop, Cursor и любым MCP-клиентом
- Покрывает 9 доменов данных: отчёты SEC (10-K/10-Q/8-K) с полнотекстовым поиском, институциональные holdings 13F, инсайдерские сделки Form 3/4, сделки конгрессменов, шорт-объём/interest FINRA, fails-to-deliver SEC, экономические индикаторы FRED, позиционирование фьючерсов CFTC, VIX/put-call CBOE, ежедневные цены акций с техническими индикаторами
- Построен на .NET 10 / C# с ParadeDB (PostgreSQL + pgvector + pg_search), развёртывается одной командой `docker compose up`
- Опциональные векторные эмбеддинги через Ollama + BGE-M3 для семантического поиска по отчётам SEC
- Без телеметрии, без облачных зависимостей — все данные собираются из публичных источников правительства США и кэшируются локально
- Лицензия AGPL-3.0, активно развивается (929 коммитов, v1.0.0 выпущена 15 мая 2026 г.)

## Подробнее
Equibles решает критическую проблему для пользователей локальных LLM: отсутствие доступа к актуальным структурированным финансовым данным. При локальном запуске моделей вроде Qwen или Llama в качестве агентов у них нет информации о текущем состоянии рынка. Equibles заполняет этот пробел, собирая данные из публичных источников (SEC EDGAR, FINRA, FRED, CFTC, CBOE, Yahoo Finance) и предоставляя структурированные инструменты запросов через протокол MCP.

Архитектура состоит из четырёх Docker-сервисов: база данных ParadeDB (PostgreSQL с полнотекстовым поиском и векторными расширениями), веб-портал для просмотра данных на порту 8080, MCP-сервер на порту 8081 для интеграции с AI-ассистентами и фоновые worker-скраперы, непрерывно загружающие данные из всех настроенных источников. Данные начинают поступать в течение нескольких минут после запуска.

Подключение к AI-клиентам несложное. Для Claude Desktop добавьте URL MCP-сервера в `claude_desktop_config.json`. Для Claude Code используйте `claude mcp add equibles --transport http http://localhost:8081/mcp`. ChatGPT Desktop и другие MCP-клиенты также поддерживаются. После подключения можно задавать вопросы на естественном языке, например: «Кто крупнейшие институциональные держатели AAPL?» или «Найди обсуждение роста выручки в последнем 10-K Apple».

Шорт-данные FINRA и экономические индикаторы FRED требуют бесплатных API-ключей (доступных после регистрации). Все остальные источники данных работают без учётных данных. Система поддерживает фильтрацию по тикерам для ограничения синхронизации конкретными акциями и настраиваемую минимальную дату синхронизации для ускорения начальной настройки.

## Связанные записи
- [[shokunin-memory-system]] ([Shokunin: Persistent Memory for Coding Agents](../tools/shokunin-memory-system.md))
