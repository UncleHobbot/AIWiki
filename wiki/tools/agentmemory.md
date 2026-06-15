---
title: "agentmemory: Persistent Memory for AI Coding Agents"
title_ru: "agentmemory: персистентная память для AI coding-агентов"
category: tools
tags: [memory, mcp, claude-code, persistent-memory, knowledge-graph, hybrid-search, llm-wiki, iii-engine, coding-agent]
aliases: [agentmemory, agent memory, rohitg00 memory, LLM Wiki memory extension]
confidence: high
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://github.com/rohitg00/agentmemory
  - https://agent-memory.dev
---

## Summary
agentmemory is an open-source persistent memory server for AI coding agents — extending Karpathy's LLM Wiki pattern with confidence scoring, memory lifecycle (decay + auto-forget), knowledge graphs, and hybrid BM25+vector+graph search — that silently captures what agents do across sessions and injects the right context when the next session starts.

## Key Ideas
- **Zero-config capture**: 12 hooks for Claude Code (or 6 for Codex) automatically record every session without any manual `add()` calls — the agent just works while memory builds silently in the background.
- **Benchmark-backed**: LongMemEval-S (ICLR 2025, 500 questions): R@5 = **95.2%** vs BM25-only 86.2%, MRR = 88.2%. Compared against mem0 (68.5%), Letta/MemGPT (83.2%), and built-in CLAUDE.md (no recall metric).
- **Token-efficient**: ~170K tokens/year vs LLM-summarized ~650K — because it retrieves relevant context rather than dumping everything, annual cost is ~$10 with cloud embeddings or **$0 with local** (all-MiniLM-L6-v2, 23MB, no API key).
- **MCP-native**: 51 MCP tools exposed (`memory_smart_search`, `memory_save`, `memory_sessions`, `memory_governance_delete`, etc.) accessible to any MCP client — one server shared across Claude Code, Codex, Cursor, OpenClaw, Hermes, Pi, and more.
- **4-tier memory lifecycle**: working memory → episodic → semantic → procedural, with configurable confidence decay and auto-forget for stale knowledge — inspired by the LLM Wiki v2 gist's memory lifecycle proposal.

## Details

### The Core Problem It Solves

> "You explain the same architecture every session. You re-discover the same bugs. You re-teach the same preferences. Built-in memory (CLAUDE.md, .cursorrules) caps out at 200 lines and goes stale."

Session 1: set up JWT auth using `jose` over `jsonwebtoken` for Edge compatibility, tests in `src/middleware/auth.ts`. Session 2: ask for rate limiting. Without agentmemory, you re-explain everything. With it, the agent already knows — because it captured session 1 automatically.

### Architecture

agentmemory is built on the **iii-engine** (a Rust-based knowledge engine). It runs as a local server on port 3111 and exposes:
- A real-time viewer on port 3113
- 51 MCP tools via `@agentmemory/mcp` stdio server
- REST API for agents without MCP support (e.g. Aider)

The hybrid search (BM25 + vector + graph, fused via RRF) finds "N+1 query fix" when you search "database performance optimization" — keyword matching alone can't do that.

### Installation

```bash
# Start the memory server
npx @agentmemory/agentmemory

# Connect to Claude Code (registers 12 hooks + MCP + 4 skills)
/plugin marketplace add rohitg00/agentmemory
/plugin install agentmemory

# Verify
curl http://localhost:3111/agentmemory/health
```

### Competitive Position

| | agentmemory | mem0 (53k★) | Letta/MemGPT (22k★) | CLAUDE.md |
|---|---|---|---|---|
| Auto-capture | 12 hooks (zero effort) | Manual add() | Agent self-edits | Manual |
| Recall R@5 | **95.2%** | 68.5% | 83.2% | N/A |
| Search | BM25+Vector+Graph | Vector+Graph | Vector | Grep |
| Tokens/session | ~1,900 ($10/yr) | Varies | 22K+ (full context) | Full context |
| Self-hosted | Yes | Optional | Optional | Yes |
| Multi-agent | MCP + REST + leases | API | Letta only | Per-agent files |

### Replay Mode
Every captured session is replayable — scrub through prompts, tool calls, tool results, and responses with play/pause, speed control (0.5×–4×), and keyboard shortcuts. Existing Claude Code JSONL transcripts can be imported (`agentmemory import-jsonl`).

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[tencent-db-agent-memory]] ([TencentDB Agent Memory: Local Long-Term Memory for AI Agents](../tools/tencent-db-agent-memory.md))
- [[shokunin-memory-system]] ([Shokunin: Persistent Memory for Coding Agents](../tools/shokunin-memory-system.md))
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[atomicmemory-semantic-memory]] ([AtomicMemory](../tools/atomicmemory-semantic-memory.md))
- [[noosphere-ai-memory]] ([Noosphere: Auditable Human-AI Shared Memory Layer](../tools/noosphere-ai-memory.md))

---
<!-- RU -->

## Краткое описание
agentmemory — open-source сервер персистентной памяти для AI coding-агентов: расширяет паттерн LLM Wiki Карпатого confidence scoring, жизненным циклом памяти (затухание + авто-забывание), графами знаний и гибридным поиском BM25+вектор+граф. Автоматически захватывает действия агентов между сессиями и внедряет нужный контекст при следующем запуске.

## Ключевые идеи
- **Захват без настройки**: 12 хуков для Claude Code (или 6 для Codex) автоматически записывают каждую сессию без ручных вызовов `add()` — агент работает, пока память строится в фоне.
- **Подкреплено бенчмарками**: LongMemEval-S (ICLR 2025): R@5 = **95.2%** против BM25-only 86.2%; превосходит mem0 (68.5%) и Letta/MemGPT (83.2%).
- **Токено-эффективно**: ~170K токенов/год против ~650K при LLM-суммаризации. Стоимость: ~$10/год или **$0** с локальными эмбеддингами (all-MiniLM-L6-v2, 23 МБ, без API-ключа).
- **MCP-нативный**: 51 MCP-инструмент, доступный любому MCP-клиенту — один сервер, общая память для Claude Code, Codex, Cursor, OpenClaw, Hermes, Pi и других.
- **4-уровневый жизненный цикл памяти**: рабочая → эпизодическая → семантическая → процедурная, с настраиваемым затуханием уверенности и авто-забыванием устаревших знаний.

## Подробнее

Основная решаемая проблема: вы объясняете одну и ту же архитектуру в каждой сессии, заново обнаруживаете одни и те же баги, переучиваете свои предпочтения. CLAUDE.md ограничен ~200 строками и устаревает. agentmemory решает это: Сессия 1 — настройка JWT-аутентификации через `jose` в `src/middleware/auth.ts`. Сессия 2 — запрос rate limiting. Агент уже знает всё из сессии 1.

**Установка:**
```bash
npx @agentmemory/agentmemory          # запуск сервера памяти
/plugin marketplace add rohitg00/agentmemory   # Claude Code plugin
/plugin install agentmemory
```

**Режим воспроизведения**: каждая захваченная сессия воспроизводима с управлением скоростью (0.5×–4×). Существующие JSONL-транскрипты Claude Code импортируются через `agentmemory import-jsonl`.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[tencent-db-agent-memory]] ([TencentDB Agent Memory: Local Long-Term Memory for AI Agents](../tools/tencent-db-agent-memory.md))
- [[shokunin-memory-system]] ([Shokunin: Persistent Memory for Coding Agents](../tools/shokunin-memory-system.md))
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[atomicmemory-semantic-memory]] ([AtomicMemory](../tools/atomicmemory-semantic-memory.md))
- [[noosphere-ai-memory]] ([Noosphere: проверяемый общий слой памяти для людей и AI](../tools/noosphere-ai-memory.md))
