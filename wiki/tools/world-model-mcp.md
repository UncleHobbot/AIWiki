---
title: "World-Model MCP: Predict Before You Execute"
title_ru: "World-Model MCP: предскажи перед выполнением"
category: tools
tags: [mcp, world-model, agent-safety, qwen-agentworld, predict-before-execute]
aliases: [world-model-mcp, world model mcp, verify_action mcp]
confidence: medium
updated: 2026-06-29
sources:
  - https://github.com/Haseebasif7/world-model-mcp
  - https://www.reddit.com/r/Qwen_AI/comments/1ug2a3j/i_built_an_mcp_server_that_gives_coding_agents_a/
---

## Summary
world-model-mcp is an MCP server that gives any coding agent (Claude Code, Cursor, etc.) a "world model oracle." Before the agent executes a consequential action (`git reset --hard`, a force push, `rm -rf`), it calls a single `verify_action` tool, receives a prediction of what the environment will look like afterward, and decides whether to proceed. It wraps the Qwen-AgentWorld concept into a tool any agent can use today.

## Key Ideas
- **Execute-first is the default failure mode**: most agents run a command and deal with consequences after — by then the damage (a wiped file tree, a forced push) is done.
- **A single `verify_action` tool**: the agent supplies state + proposed action; the world model returns the predicted resulting state, letting the agent self-check before acting.
- **Three backends by cost/access**: Groq (free, no credit card), Together AI ($25 free credit, architecturally closer to the real world model), and `Qwen-AgentWorld-35B-A3B` (the purpose-built world model itself).
- **Directly inspired by the Qwen-AgentWorld paper**, which trained a language world model to simulate environment responses across 7 domains.
- **Agent-agnostic**: exposed over MCP, so any MCP-capable agent can call it without bespoke integration.

## Details
The server operationalizes a shift in agent safety: from post-hoc recovery to pre-execution verification. Rather than relying on the agent's own judgment (which is unreliable for destructive ops) or a hard-coded allow/deny list, it delegates "what happens if I do this?" to a model trained specifically on environment dynamics.

Because it runs as an MCP server, adoption is a configuration step rather than a code change — the agent simply gains a new tool it can choose to call before risky actions.

## Related Entries
- [[qwen-agentworld]] ([Qwen-AgentWorld: First World Model](../models/qwen-agentworld.md))
- [[temenos-agent-sandbox]] ([temenos — Sandbox for Agent-Executed Code](temenos-agent-sandbox.md))
- [[gnosis-mcp]] ([Gnosis MCP](gnosis-mcp.md))

---
<!-- RU -->

## Краткое описание
world-model-mcp — MCP-сервер, дающий любому кодинг-агенту (Claude Code, Cursor и др.) «оракул-модель мира». Перед выполнением деструктивного действия (`git reset --hard`, force push, `rm -rf`) агент вызывает единый инструмент `verify_action`, получает предсказание результирующего состояния среды и решает, выполнять ли. Оборачивает концепцию Qwen-AgentWorld в инструмент, доступный любому агенту.

## Ключевые идеи
- **«Сначала выполни» — типичный режим отказа**: большинство агентов запускают команду и разбираются с последствиями после — к тому моменту ущерб уже нанесён.
- **Единый инструмент `verify_action`**: агент передаёт состояние + предложенное действие; модель мира возвращает предсказанное результирующее состояние.
- **Три бэкенда по стоимости/доступу**: Groq (бесплатно), Together AI ($25 бесплатного кредита), `Qwen-AgentWorld-35B-A3B` (самодельная модель мира).
- **Прямо вдохновлён статьёй Qwen-AgentWorld**, обучившей языковую модель мира симулировать ответы среды в 7 доменах.
- **Агент-агностичен**: публикуется через MCP, так что любой MCP-агент может вызывать инструмент без спец-интеграции.

## Подробнее
Сервер операционализирует сдвиг в безопасности агентов: от восстановления «постфактум» к проверке «до выполнения». Вместо полагания на собственное суждение агента (ненадёжное для деструктивных операций) или жёстко заданного списка allow/deny, он делегирует «что будет, если я это сделаю?» модели, обученной именно на динамике сред.

Поскольку это MCP-сервер, внедрение — шаг конфигурации, а не изменение кода: агент просто получает новый инструмент, который может вызывать перед рискованными действиями.

## Связанные записи
- [[qwen-agentworld]] ([Qwen-AgentWorld: First World Model](../models/qwen-agentworld.md))
- [[temenos-agent-sandbox]] ([temenos — Sandbox for Agent-Executed Code](temenos-agent-sandbox.md))
- [[gnosis-mcp]] ([Gnosis MCP](gnosis-mcp.md))
