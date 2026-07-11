---
title: "OpenCode"
title_ru: "OpenCode"
category: tools
tags: [opencode, coding-agent, terminal, cli, open-source]
date: 2026-06-14
updated: 2026-06-14
sources:
  - https://opencode.ai/
  - https://github.com/opencode-ai/opencode
---

## Summary

OpenCode is an open-source terminal-based AI coding agent and CLI. It manages multi-turn sessions, tools, skills, and subagents, and supports local/remote LLM providers. It has a growing plugin ecosystem (RAG, skills, desktop pets, research plugins).

## Key Ideas

- Open-source coding agent that runs in the terminal, similar to Claude Code or GitHub Copilot CLI, but fully auditable and extensible.
- Architecture built around sessions, a tool registry, skills (reusable prompt/tool packs), and subagents for parallel or delegated work.
- Provider-agnostic by design: works with local models via Ollama/vLLM and remote APIs such as OpenAI, Anthropic, Moonshot, Z.AI, and others.
- Skills and plugins are first-class: users install community skill packs and plugins for RAG, memory, research, or even desktop-pet-style UI companions.

## Details

OpenCode positions itself as a user-owned alternative to closed coding agents. Everything is driven through a command-line interface, with commands to start a session, attach skills, run a subagent swarm, or inspect tool calls. The configuration lives in `opencode.json` and can declare default models, permission levels, MCP servers, and skill search paths.

Because the project is open-source, most advanced behavior is added by the community. Examples include OpenCodeRAG (self-hosted retrieval), Amore (research plugin), MiMo Code (a Xiaomi fork), and OC Claw (a desktop pet / agent monitor). The plugin model makes it possible to tailor OpenCode to local-first, enterprise, or hobbyist workflows without waiting for vendor updates.

## Notable Quotes

> "OpenCode is the open-source AI coding agent that lives in your terminal." — opencode.ai

## Related Entries

- [[opencoderag-rag-plugin]] ([OpenCodeRAG RAG Plugin](opencoderag-rag-plugin.md))
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo Code — Xiaomi OpenCode Fork](mimo-code-xiaomi-opencode-fork.md))
- [[amore-opencode-research-plugin]] ([Amore — OpenCode Research Plugin](amore-opencode-research-plugin.md))
- [[oc-claw-agent-monitor]] ([OC Claw — Agent Monitor](oc-claw-agent-monitor.md))
- [[redactable-pii-protection]] ([Redactable: PII Protection Plugin for OpenCode](../tools/redactable-pii-protection.md))
- [[zsh-opencode-plugin]] ([zsh-opencode-plugin](../tools/zsh-opencode-plugin.md))
- [[codeboarding-architecture-diagrams]] ([CodeBoarding: Live Architecture Diagrams That Track Agent Changes](../tools/codeboarding-architecture-diagrams.md))
- [[opencode-rate-limiter-plugin]] ([opencode-rate-limiter-plugin](opencode-rate-limiter-plugin.md))
- [[opencode-12m-token-burn]] ([Burning 12M Tokens in a Few Prompts](../tips/opencode-12m-token-burn.md))

---
- [[aethereum-multi-session-coordination]] ([aethereum](aethereum-multi-session-coordination.md))
<!-- RU -->

## Краткое описание

OpenCode — открытый терминальный AI-агент для кодинга и CLI. Управляет многоходовыми сессиями, инструментами, навыками и подагентами, поддерживает локальные и удалённые LLM-провайдеры. Имеет растущую экосистему плагинов (RAG, навыки, десктоп-питомцы, исследовательские плагины).

## Ключевые идеи

- Открытый агент для кодинга, работающий в терминале: похож на Claude Code или GitHub Copilot CLI, но полностью прозрачен и расширяем.
- Архитектура построена вокруг сессий, реестра инструментов, навыков ( reusable prompt/tool packs) и подагентов для параллельной или делегированной работы.
- Независим от провайдера: поддерживает локальные модели через Ollama/vLLM и удалённые API — OpenAI, Anthropic, Moonshot, Z.AI и другие.
- Навыки и плагины — полноправные сущности: пользователи устанавливают community-пакеты для RAG, памяти, исследований и даже десктоп-питомцев.

## Подробнее

OpenCode позиционируется как агент для кодинга, которым владеет пользователь, а не вендор. Весь интерфейс — командная строка: команды запускают сессию, подключают навыки, запускают рой подагентов или показывают вызовы инструментов. Конфигурация живёт в `opencode.json`, где задаются модели по умолчанию, уровни разрешений, MCP-серверы и пути поиска навыков.

Благодаря открытому коду продвинутые функции добавляются сообществом. Примеры: OpenCodeRAG (self-hosted retrieval), Amore (исследовательский плагин), MiMo Code (форк от Xiaomi) и OC Claw (десктоп-питомец / монитор агента). Модель плагинов позволяет адаптировать OpenCode под локальные, корпоративные или любительские workflows без ожидания обновлений вендора.

## Примечательные цитаты

> "OpenCode is the open-source AI coding agent that lives in your terminal." — opencode.ai

## Связанные записи

- [[opencoderag-rag-plugin]] ([OpenCodeRAG RAG Plugin](opencoderag-rag-plugin.md))
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo Code — Xiaomi OpenCode Fork](mimo-code-xiaomi-opencode-fork.md))
- [[amore-opencode-research-plugin]] ([Amore — OpenCode Research Plugin](amore-opencode-research-plugin.md))
- [[oc-claw-agent-monitor]] ([OC Claw — Agent Monitor](oc-claw-agent-monitor.md))
- [[redactable-pii-protection]] ([Redactable: защита PII для OpenCode](../tools/redactable-pii-protection.md))
- [[zsh-opencode-plugin]] ([zsh-opencode-plugin](../tools/zsh-opencode-plugin.md))
- [[codeboarding-architecture-diagrams]] ([CodeBoarding: живые архитектурные диаграммы, отслеживающие изменения агента](../tools/codeboarding-architecture-diagrams.md))
