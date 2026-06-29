---
title: "Qwen-AgentWorld: Qwen's First Language World Model for Agent Simulation"
title_ru: "Qwen-AgentWorld: первая языковая модель мира от Qwen для симуляции агентов"
category: models
tags: [qwen, world-model, agent-simulation, qwen3.5, moe]
aliases: [Qwen-AgentWorld, AgentWorld, Qwen world model, Qwen-AgentWorld-35B-A3B]
confidence: medium
updated: 2026-06-29
sources:
  - https://www.reddit.com/r/Qwen_AI/comments/1ufzml2/has_anyone_else_played_with_qwenagentworld_its/
  - https://www.reddit.com/r/Qwen_AI/comments/1ug2a3j/i_built_an_mcp_server_that_gives_coding_agents_a/
  - https://www.reddit.com/r/Qwen_AI/comments/1ug022d/qwen_agent_world/
  - https://www.reddit.com/r/Qwen_AI/comments/1ufzml2/
---

## Summary
Qwen-AgentWorld is Qwen's first **language world model** — a fine-tune of Qwen3.5-35B-A3B (trained on the AgentWorldBench dataset) that simulates environment responses to agent actions. Instead of a user/assistant chat template, it uses a `State → Action → Next Observation` format, letting you predict what an environment will look like after an agent acts.

## Key Ideas
- **World model, not chatbot**: given a current state and a proposed action, it predicts the resulting observation — simulating an environment rather than holding a conversation.
- **`State → Action → Next Observation` template**: you provide state + action; the model generates the next observation. This is used primarily to test/evaluate agents against simulated environments across multiple domains.
- **Base**: a fine-tune of Qwen3.5-35B-A3B-Base trained on Qwen/AgentWorldBench; it does **not** carry Qwen 3.6 DNA or MTP (multi-token prediction).
- **Simulation ≠ hallucination**: the model is trained on data about environments, so its predictions reflect learned dynamics rather than unconstrained invention — an important distinction for agent evaluation.
- **Practical wrap**: the community built a `world-model-mcp` MCP server exposing a `verify_action` tool, so any coding agent (Claude Code, Cursor, etc.) can call a world-model oracle to predict outcomes **before** executing a destructive action (e.g., `git reset --hard`, `rm -rf`).

## Details
AgentWorld reframes agent safety/evaluation: instead of letting an agent execute first and observe consequences, you ask a world model what would happen, then decide whether to proceed. A security-testing example: given "an agent uploads raw logs containing customer emails to a public paste service," the world model predicts the resulting breach — letting you catch the bad action before it runs.

The model covers seven domains out of the box and can run via Groq (free), Together AI, or self-hosted as `Qwen-AgentWorld-35B-A3B`. Because it is based on Qwen3.5 rather than 3.6, community members have suggested re-finetuning the newer Qwen3.6-35B-A3B-MTP base on AgentWorldBench for potentially better results.

## Related Entries
- [[world-model-mcp]] ([World-Model MCP: Predict Before You Execute](../tools/world-model-mcp.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[moe-watcher-modifier]] ([MoE-Watcher: Visualizing Expert Routing](../tools/moe-watcher-modifier.md))

---
<!-- RU -->

## Краткое описание
Qwen-AgentWorld — первая **языковая модель мира** от Qwen, файн-тюн Qwen3.5-35B-A3B (обученный на датасете AgentWorldBench), который симулирует реакции среды на действия агента. Вместо шаблона user/assistant используется формат `State → Action → Next Observation`: модель предсказывает, какой станет среда после действия агента.

## Ключевые идеи
- **Модель мира, а не чат-бот**: по текущему состоянию и предложенному действию модель предсказывает результирующее наблюдение — симулирует среду, а не ведёт беседу.
- **Шаблон `State → Action → Next Observation`**: вы передаёте состояние + действие; модель генерирует следующее наблюдение. Используется в основном для тестирования/оценки агентов в симулированных средах.
- **База**: файн-тюн Qwen3.5-35B-A3B-Base, обученный на Qwen/AgentWorldBench; не несёт DNA Qwen 3.6 или MTP (мульти-токенное предсказание).
- **Симуляция ≠ галлюцинация**: модель обучена на данных о средах, поэтому её предсказания отражают изученную динамику, а не бесконтрольное выдумывание.
- **Практическая обёртка**: сообщество создало MCP-сервер `world-model-mcp` с инструментом `verify_action`, чтобы любой кодинг-агент мог обращаться к оракулу-модели мира и предсказывать результат **до** выполнения деструктивного действия.

## Подробнее
AgentWorld переформулирует безопасность/оценку агентов: вместо того чтобы агент сначала выполнил действие, а потом наблюдал последствия, вы спрашиваете модель мира, что произойдёт, и лишь потом решаете, выполнять ли. Пример из тестирования безопасности: при «загрузке агентом сырых логов с email клиентов в публичный пастebin» модель мира предсказывает утечку — позволяя перехватить плохое действие до запуска.

Модель покрывает семь доменов и работает через Groq (бесплатно), Together AI или в self-hosted-режиме как `Qwen-AgentWorld-35B-A3B`.

## Связанные записи
- [[world-model-mcp]] ([World-Model MCP: Predict Before You Execute](../tools/world-model-mcp.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[moe-watcher-modifier]] ([MoE-Watcher: Visualizing Expert Routing](../tools/moe-watcher-modifier.md))
