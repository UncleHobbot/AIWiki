---
title: "Orkestra: Multi-CLI Studio to Run Claude Code, Codex, and Gemini From One Panel"
title_ru: "Orkestra: мульти-CLI студия для запуска Claude Code, Codex и Gemini из одной панели"
category: tools
tags: [multi-agent, orchestration, claude-code, codex, gemini, subscription, debate]
aliases: [Orkestra, Orkestra-CLI, multi-CLI panel]
confidence: medium
updated: 2026-06-29
sources:
  - https://github.com/burakdemir16/Orkestra-CLI
  - https://www.reddit.com/r/opencodeCLI/comments/1ui3xxa/i_built_orkestra_run_claude_code_codex_gemini/
  - https://www.reddit.com/r/ClaudeCode/comments/1uixwi7/i_built_orkestra_run_claude_code_codex_gemini/
---

## Summary
Orkestra is a local-first studio that drives Claude Code, OpenAI Codex, and Gemini/Antigravity CLIs from a single panel, letting you use the flat subscriptions you already pay for — together — instead of stacking metered per-token API costs. It supports chat, multi-model debate, and parallel team execution with automatic fallback across plans when one hits its limit.

## Key Ideas
- **One login, three plans**: authenticate once with your Claude (Claude Code), ChatGPT (Codex), and Gemini (Antigravity) subscriptions; Orkestra runs all three side by side, tapping each plan's included quota instead of per-token API billing.
- **Automatic plan fallback**: when one plan hits its usage limit, a fallback chain switches to the next plan so work never stops mid-session.
- **Three interaction modes**: Single (one agent), Debate (several agents argue a problem), Team (agents run independent subtasks in parallel).
- **Operator mode**: after a debate, one model synthesizes everyone's views into a shared plan that can be turned into real files.
- **Chat vs Code modes**: plan and debate in Chat mode, then turn the plan into actual files in Code mode.

## Details
Orkestra targets a common pain point: developers who already pay for multiple AI subscriptions (Claude, ChatGPT, Gemini) but keep switching between terminals and still pay extra per-token API costs on top. By driving the CLIs through their subscription auth rather than API keys, it aims to make the combined quota of existing plans usable without metered billing.

The debate/team modes lean on the observation that different frontier models have complementary strengths — having them critique each other's plans before code generation can catch single-model blind spots. The Operator synthesizer role is the mechanism that consolidates divergent agent outputs into one coherent spec.

## Related Entries
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration: Multi-Model Frameworks](../agents/agent-orchestration-multi-model-framework.md))
- [[claude-code]] ([Claude Code](claude-code.md))
- [[9router-free-ai-coding]] ([9router: Free AI Coding Router](9router-free-ai-coding.md))

---
<!-- RU -->

## Краткое описание
Orkestra — local-first студия, управляющая CLI Claude Code, OpenAI Codex и Gemini/Antigravity из одной панели, позволяющая использовать уже оплаченные фиксированные подписки вместе, вместо нагромождения тарифицируемых per-token API-расходов. Поддерживает чат, дебаты нескольких моделей и параллельное командное выполнение с автоматическим резервным переключением между планами.

## Ключевые идеи
- **Один логин, три плана**: авторизуйтесь один раз подписками Claude (Claude Code), ChatGPT (Codex) и Gemini (Antigravity); Orkestra запускает все три параллельно, используя включённые квоты планов вместо per-token биллинга.
- **Автоматический fallback по планам**: при достижении лимита одного плана цепочка резервирования переключается на следующий, чтобы работа не останавливалась.
- **Три режима взаимодействия**: Single (один агент), Debate (несколько агентов спорят над задачей), Team (агенты параллельно ведут независимые подзадачи).
- **Operator mode**: после дебатов одна модель синтезирует взгляды всех в общий план, который превращается в реальные файлы.
- **Режимы Chat и Code**: планируйте и дискутируйте в Chat, затем превращайте план в файлы в Code.

## Подробнее
Orkestra решает частую боль: разработчики платят за несколько AI-подписок, но переключаются между терминалами и доплачивают за per-token API. Управляя CLI через авторизацию подписок, а не API-ключи, инструмент делает совокупную квоту существующих планов пригодной к использованию без метрического биллинга.

Режимы debate/team опираются на то, что разные frontier-модели имеют комплементарные сильные стороны — их взаимная критика планов до генерации кода ловит слепые зоны одной модели.

## Связанные записи
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration: Multi-Model Frameworks](../agents/agent-orchestration-multi-model-framework.md))
- [[claude-code]] ([Claude Code](claude-code.md))
- [[9router-free-ai-coding]] ([9router: Free AI Coding Router](9router-free-ai-coding.md))
