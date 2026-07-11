---
title: "Clifford — Control-Plane CLI for Local AI Backends"
title_ru: "Clifford — CLI плоскости управления для локальных AI-бэкендов"
category: tools
tags: [local-llm, cli, llama-server, hermes, pi-agent, claude-code, orchestration]
aliases: [Clifford, clifford.bot, control plane local ai]
confidence: medium
updated: 2026-07-11
sources:
  - https://clifford.bot/
  - https://www.reddit.com/r/LocalLLaMA/comments/1ut3z4y/clifford_control_plane_cli_for_local_ai/
---

## Summary
**Clifford** is a CLI daemon that lets you save local AI configurations as named profiles and reload them with one command, then connect the running backend to community-favorite agents (Pi, Hermes, Claude Code). Bring-your-own-backend — officially supports `llama-server` (vLLM coming). Turns a verbose multi-step startup into `clifford load <profile> && clifford pi`.

## Key Ideas
- **Pain point:** starting a local model for agentic work is verbose — long `llama-server` invocations plus manual edits to agent config files (e.g. `~/.pi/agent/models.json`) before you can connect an agent.
- **Solution:** save the full configuration (model path, server flags, agent wiring) as a named profile once; reload with `clifford load <name>`, then `clifford pi` / `clifford hermes` / `clifford claude`.
- **Bring-your-own-backend:** Clifford ships no pre-packaged backends; officially supports `llama-server`, with vLLM planned.
- **Agent connections:** Pi, Hermes, Claude Code — the popular local-agent harnesses.
- CLI-native, ergonomic; positions itself as the missing "control plane" for local AI setups.

## Details
Clifford targets the ergonomic gap in local AI: the model-serving layer (llama.cpp/vLLM) and the agent layer (Pi/Hermes/Claude Code) each have their own config, and wiring them together is manual and repetitive. By treating the full stack (server flags + agent wiring) as a reloadable profile, Clifford makes multi-model local setups switchable in one command.

## Related Entries
- [[ollama]] ([Ollama](ollama.md))
- [[product-hermes-agent]] ([Hermes Agent](../agents/product-hermes-agent.md))
- [[opencode]] ([OpenCode](opencode.md))

---
<!-- RU -->

## Краткое описание
**Clifford** — CLI-демон, позволяющий сохранять локальные AI-конфигурации как именованные профили и перезагружать их одной командой, затем подключая запущенный бэкенд к агентам (Pi, Hermes, Claude Code). Bring-your-own-backend — официально поддерживается `llama-server` (vLLM в планах). Превращает многошаговый запуск в `clifford load <profile> && clifford pi`.

## Ключевые идеи
- **Боль:** запуск локальной модели для агентной работы многословен — длинные вызовы `llama-server` плюс ручные правки конфигов агента.
- **Решение:** сохранить полную конфигурацию как именованный профиль один раз; перезагружать `clifford load <name>`, затем `clifford pi/hermes/claude`.
- **Bring-your-own-backend:** Clifford не поставляет бэкенды; поддерживает `llama-server`, vLLM в планах.
- **Подключение агентов:** Pi, Hermes, Claude Code.
- CLI-native, эргономичный; позиционируется как недостающая «плоскость управления» для локального AI.

## Подробнее
Clifford закрывает эргономический пробел: слой model-serving (llama.cpp/vLLM) и слой агента (Pi/Hermes/Claude Code) имеют каждый свой конфиг, и их связывание вручную повторяется. Трактует весь стек как перезагружаемый профиль.

## Связанные записи
- [[ollama]] ([Ollama](ollama.md))
- [[product-hermes-agent]] ([Hermes Agent](../agents/product-hermes-agent.md))
- [[opencode]] ([OpenCode](opencode.md))
