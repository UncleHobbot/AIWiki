---
title: "Gnosis MCP: Documentation Search Server for AI Agents"
title_ru: "Gnosis MCP: сервер поиска документации для AI-агентов"
category: tools
tags: [mcp, documentation, search, rag, sqlite, hybrid-search, claude-code]
aliases: [Gnosis MCP, gnosis, doc search MCP, local documentation search]
confidence: high
updated: 2026-05-15
sources:
  - https://github.com/nicholasglazer/gnosis-mcp
  - https://gnosismcp.com/
  - https://www.pulsemcp.com/servers/gh-nicholasglazer-gnosis
---

## Summary
Gnosis MCP is a zero-config local MCP server that gives AI agents hybrid keyword + semantic search over your documentation, replacing expensive full-file context dumps with 300–800 token ranked excerpts and delivering 10–60× token savings per lookup.

## Key Ideas
- **Solves the LLM doc hallucination problem:** Instead of dumping 3,000–15,000 tokens of full files into context (or letting models hallucinate API signatures), `search_docs` returns ranked, grounded excerpts of 200–500 tokens per call.
- **Zero config — pip install and go:** SQLite by default, no API key required. `pip install gnosis-mcp` → `gnosis-mcp ingest ./docs/` → `gnosis-mcp serve`. Three commands.
- **Hybrid search by default (with embeddings):** Keyword BM25 + semantic ONNX embeddings (23MB local model, no API key), fused via RRF. Enable with `pip install gnosis-mcp[embeddings]`.
- **Measured, not marketed:** Ships BEIR SciFact nDCG@10 = 0.671 (within 1% of Lucene BM25 baseline); on 558 real dev docs with 25 hand-written queries: Hit@5 = 0.92, nDCG@10 = 0.87, MRR = 0.79.
- **Rerankers are off by default — for good reason:** The bundled MS-MARCO cross-encoder drops nDCG@10 by 27 points on dev-doc retrieval and adds 400× latency. BGE-reranker-v2-m3 drops it 31 points at 2400× latency. Test on your corpus before enabling.
- **Git history as searchable context:** `gnosis-mcp ingest-git .` indexes commit messages — agents learn *why* things were built, not just what exists.
- **Web crawl support:** `gnosis-mcp crawl https://docs.stripe.com/ --sitemap` ingests any documentation site. Respects robots.txt, caches incrementally.
- **Track your token savings:** `gnosis-mcp savings --days 7` prints aggregated tokens returned vs. baseline reads across all tool calls.

## Details
**Install options:**
```bash
pip install gnosis-mcp                    # SQLite, keyword-only
pip install gnosis-mcp[embeddings]        # + local semantic search
pip install gnosis-mcp[postgres]          # + PostgreSQL + pgvector at scale
uvx gnosis-mcp ingest ./docs/ && uvx gnosis-mcp serve   # zero-install
docker run -p 8000:8000 -v "$PWD/docs:/docs:ro" -v gnosis-data:/data ghcr.io/nicholasglazer/gnosis-mcp:latest
```

**MCP tools exposed:** `search_docs` (ranked excerpts), `get_doc` (full document), `get_related` (graph neighbours via `relates_to` frontmatter).

**Editor integration** — add to `.claude/mcp.json` (Claude Code), `.cursor/mcp.json`, or `~/.codeium/windsurf/mcp_config.json`:
```json
{"mcpServers": {"docs": {"command": "gnosis-mcp", "args": ["serve"]}}}
```

**Claude Code plugin** (gets slash commands + auto-configured MCP):
```bash
claude plugin marketplace add nicholasglazer/gnosis-mcp
claude plugin install gnosis
```

**Performance numbers:**
- 8.7ms mean MCP round-trip
- Hybrid search p50 < 30ms on 700-doc corpus
- Keyword QPS: 9,463 @ 100 docs → 471 @ 10,000 docs
- Token savings: 10–60× depending on corpus coverage; real example: 224k tokens saved across 142 tool calls in 7 days (32.6× ratio)

**Formats:** `.md` `.txt` `.ipynb` `.toml` `.csv` `.json` + optional `.rst` `.pdf`. Git commit history. Crawled web pages.

**PostgreSQL mode** (production scale): set `GNOSIS_MCP_DATABASE_URL=postgresql://...`, run `gnosis-mcp init-db`, then `gnosis-mcp ingest ./docs/`. Adds tsvector + pgvector hybrid, HNSW index, multi-table search.

## Related Entries
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[gnosis-mcp-vs-llm-wiki-pattern]] ([Gnosis MCP vs. LLM Wiki Pattern: Use Cases, Trade-offs, and When to Combine](../concepts/gnosis-mcp-vs-llm-wiki-pattern.md))

---
<!-- RU -->

## Краткое описание
Gnosis MCP — локальный MCP-сервер с нулевой конфигурацией, дающий AI-агентам гибридный (ключевые слова + семантика) поиск по документации. Заменяет дорогостоящие дампы полных файлов в контекст на ранжированные выдержки в 300–800 токенов с экономией 10–60× токенов на запрос.

## Ключевые идеи
- **Решает проблему галлюцинаций LLM в документации:** Вместо загрузки 3 000–15 000 токенов полных файлов в контекст, `search_docs` возвращает ранжированные, обоснованные выдержки по 200–500 токенов за вызов.
- **Нулевая конфигурация:** SQLite по умолчанию, API-ключ не требуется. `pip install gnosis-mcp` → `gnosis-mcp ingest ./docs/` → `gnosis-mcp serve`. Три команды.
- **Гибридный поиск (с эмбеддингами):** BM25 по ключевым словам + семантические ONNX-эмбеддинги (локальная модель 23MB, без API-ключа), объединённые через RRF. Включается через `pip install gnosis-mcp[embeddings]`.
- **Измерено, а не рекламировано:** BEIR SciFact nDCG@10 = 0.671 (в пределах 1% от базового Lucene BM25); на 558 реальных документах с 25 вручную написанными запросами: Hit@5 = 0.92, nDCG@10 = 0.87, MRR = 0.79.
- **Ранжировщики выключены по умолчанию — и не зря:** Встроенный MS-MARCO cross-encoder снижает nDCG@10 на 27 пунктов для документации и добавляет 400× задержку. BGE-reranker-v2-m3 — 31 пункт при 2400×. Проверяйте на своём корпусе перед включением.
- **История git как поисковый контекст:** `gnosis-mcp ingest-git .` индексирует сообщения коммитов — агенты узнают *почему* что-то построено, а не только *что* существует.
- **Отслеживание экономии токенов:** `gnosis-mcp savings --days 7` выводит агрегированные токены, возвращённые vs базовое чтение файлов.

## Подробнее
**MCP-инструменты:** `search_docs` (ранжированные выдержки), `get_doc` (полный документ), `get_related` (связанные документы через frontmatter `relates_to`).

**Интеграция с редактором** — добавьте в `.claude/mcp.json` (Claude Code), `.cursor/mcp.json` или `~/.codeium/windsurf/mcp_config.json`:
```json
{"mcpServers": {"docs": {"command": "gnosis-mcp", "args": ["serve"]}}}
```

**Плагин Claude Code** (с slash-командами и авто-настройкой MCP):
```bash
claude plugin marketplace add nicholasglazer/gnosis-mcp
claude plugin install gnosis
```

**Режим PostgreSQL** (продакшн-масштаб): задайте `GNOSIS_MCP_DATABASE_URL=postgresql://...`, выполните `gnosis-mcp init-db`, затем `gnosis-mcp ingest ./docs/`. Добавляет tsvector + pgvector, HNSW-индекс, multi-table поиск.

## Связанные записи
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[llmwiki-open-source]] ([llmwiki (Open-Source Implementation)](../tools/llmwiki-open-source.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[gnosis-mcp-vs-llm-wiki-pattern]] ([Gnosis MCP vs. LLM Wiki Pattern: Use Cases, Trade-offs, and When to Combine](../concepts/gnosis-mcp-vs-llm-wiki-pattern.md))
