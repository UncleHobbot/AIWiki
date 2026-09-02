---
title: "Polyglot — Fault-Tolerant Tool Calls for Small Local Models"
title_ru: "Polyglot — отказоустойчивые вызовы инструментов для малых локальных моделей"
category: tools
tags: [ollama, tool-calling, parser, small-models, terminal-agent, mcp, local-llm]
aliases: [Polyglot, polyglot cli, tolerant tool call parser]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/ollama/comments/1w4nnwm/point_an_agent_at_your_ollama_server_and_have_the/
  - https://github.com/giuseppe-sirigu/polyglot
---

## Summary
**Polyglot** is a terminal coding agent built to survive the tool-call formatting mistakes of 3B–8B local models. Instead of relying on a provider's native function-calling API, it treats a tool call as *text*: tools are described in the system prompt, and a fault-tolerant streaming parser extracts and repairs calls from the raw output — trailing commas, single quotes, near-miss names (`read_files` vs `read_file`), OpenAI-style wrappers. Same parser + executor + permission gate regardless of model.

## Key Ideas
- **The problem:** small local models reason fine but improvise the tool-call envelope; most agents are built around native function-calling APIs and simply stall on malformed output.
- **The approach:** prompt-described tools + text-level parsing with repair, streamed (fixes applied as tokens arrive).
- **Model-agnostic executor:** one parser/executor/permission-gate for any OpenAI-compatible endpoint.
- **Setup:** `POLYGLOT_PROVIDER=openai-compatible`, `POLYGLOT_BASE_URL=http://localhost:11434/v1`, `npm i -g @usepolyglot/cli`; MCP supported.

## Details
This complements the [[toolhound-tool-call-failure-taxonomy]] finding that small-model tool-call *syntax* is "basically solved" — solved at ~1.00 for parse/schema on *current-gen* models, but the long tail of local 3B–8B models still misformats. Polyglot attacks it at the harness layer (repair instead of reject), which is exactly where the taxonomy says harness-side fixes belong.

## Related Entries
- [[toolhound-tool-call-failure-taxonomy]] ([ToolHound Failure Taxonomy](../research/toolhound-tool-call-failure-taxonomy.md))
- [[ollama]] ([Ollama](ollama.md))
- [[clifford-control-plane-local-ai]] ([Clifford](clifford-control-plane-local-ai.md))
- [[glm-5-2-nested-tool-call-bug]] ([GLM-5.2 Nested Tool-Call Bug](../news/glm-5-2-nested-tool-call-bug.md))

---
- [[anywebmcp-webmcp-any-site]] ([AnyWebMCP](anywebmcp-webmcp-any-site.md))
<!-- RU -->

## Краткое описание
**Polyglot** — терминальный кодинг-агент, созданный, чтобы переживать ошибки форматирования tool-call'ов малых локальных моделей 3B–8B. Вместо опоры на нативный function-calling API провайдера он трактует вызов инструмента как *текст*: инструменты описаны в системном промпте, а отказоустойчивый стриминг-парсер извлекает и чинит вызовы из сырого вывода — висячие запятые, одинарные кавычки, почти-попадания в имена, обёртки в стиле OpenAI. Один парсер + исполнитель + шлюз разрешений для любой модели.

## Ключевые идеи
- **Проблема:** малые локальные модели хорошо рассуждают, но импровизируют с конвертом tool-call; большинство агентов построены вокруг нативных API и просто зависают на битом выводе.
- **Подход:** инструменты через промпт + парсинг на уровне текста с починкой, стримингово.
- **Исполнитель без привязки к модели:** один парсер/исполнитель/шлюз для любого OpenAI-совместимого эндпоинта.
- **Установка:** три переменные окружения + `npm i -g @usepolyglot/cli`; MCP поддерживается.

## Подробнее
Дополняет находку [[toolhound-tool-call-failure-taxonomy]] о том, что синтаксис tool-call у малых моделей «в основном решён» — решён для *текущего поколения*, но длинный хвост локальных 3B–8B всё ещё сбивается. Polyglot атакует это на уровне харнеса (чинить, а не отвергать) — ровно там, где по таксономии и должен быть фикс.

## Связанные записи
- [[toolhound-tool-call-failure-taxonomy]] ([ToolHound Failure Taxonomy](../research/toolhound-tool-call-failure-taxonomy.md))
- [[ollama]] ([Ollama](ollama.md))
- [[clifford-control-plane-local-ai]] ([Clifford](clifford-control-plane-local-ai.md))
- [[glm-5-2-nested-tool-call-bug]] ([GLM-5.2 Nested Tool-Call Bug](../news/glm-5-2-nested-tool-call-bug.md))
