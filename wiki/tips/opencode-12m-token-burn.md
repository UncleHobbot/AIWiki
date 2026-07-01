---
title: "Burning 12M Input Tokens in a Few Prompts (OpenCode Cautionary Tale)"
title_ru: "Сожжено 12M входных токенов за несколько промптов (кейс OpenCode)"
category: tips
tags: [opencode, token-usage, cost-control, vibecoding, cautionary]
aliases: [opencode 12M tokens, token burn opencode]
confidence: medium
date: 2026-06-30
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/opencodeCLI/comments/1uk2ztx/burning_12m_input_tokens_in_few_prompts/
---

## Summary
A new agentic-coding user on OpenCode (Flatpak build, DeepSeek V3.2 via a third-party provider) burned ~12 million input tokens in a handful of prompts on an existing vibe-coded codebase within minutes — draining a prepaid wallet. A concrete data point on how fast context re-injection compounds in agent loops on large codebases.

## Key Ideas
- **Setup:** OpenCode (Flatpak) + DeepSeek V3.2 via a regional provider, prompts against an already-existing vibe-coded codebase.
- **Outcome:** ~12M input tokens consumed in minutes across a few prompts; wallet dried up before the user noticed.
- **Mechanism:** agentic loops re-inject the full file/codebase context on each turn, so cost scales with (context size × turns) — not prompt count.
- **Lesson:** set spend caps/usage guards before pointing an agent at a large existing repo; verify the model's context handling and disable auto-compaction surprises.
- Useful calibration for newcomers transitioning into agentic coding.

## Details
This is a community data point (Tier 3), valuable less for precision than for the pattern it illustrates: agent token cost is dominated by repeated context re-injection, not by the user's typing. On a large pre-existing codebase, a few turns can rack up millions of input tokens. Practical mitigations: scope the agent to relevant files, use a spend cap, monitor the provider dashboard, and prefer providers/tools that show live token counts.

## Related Entries
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[headroom-token-saver]] ([Headroom Token Saver](../tools/headroom-token-saver.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[opencode-rate-limiter-plugin]] ([OpenCode Rate Limiter Plugin](../tools/opencode-rate-limiter-plugin.md))

---
<!-- RU -->

## Краткое описание
Новый пользователь agentic-кодинга в OpenCode (сборка Flatpak, DeepSeek V3.2 через стороннего провайдера) сжёг ~12 миллионов входных токенов за несколько промптов на существующей vibe-coded кодовой базе за минуты — опустошив предоплаченный кошелёк. Конкретная точка данных о том, как быстро накапливается реинъекция контекста в агентных циклах на больших репозиториях.

## Ключевые идеи
- **Условия:** OpenCode (Flatpak) + DeepSeek V3.2 через регионального провайдера, промпты к уже существующей vibe-coded кодовой базе.
- **Результат:** ~12M входных токенов за минуты и несколько промптов; кошелёк истощился до того, как пользователь заметил.
- **Механизм:** агентные циклы реинжектят полный контекст файла/репозитория на каждом ходу, поэтому стоимость растёт как (размер контекста × ходы), а не по числу промптов.
- **Урок:** ставьте лимиты расходов перед тем, как натравливать агента на большой существующий репозиторий.
- Полезная калибровка для новичков, переходящих в agentic-кодинг.

## Подробнее
Это точка данных от сообщества (уровень 3), ценная скорее иллюстрацией паттерна, чем точностью: стоимость в токенах у агента определяется повторной реинъекцией контекста, а не вводом пользователя. На крупном существующем репозитории несколько ходов могут дать миллионы входных токенов. Практические меры: ограничить область агента нужными файлами, поставить лимит расходов, следить за дашбордом провайдера, предпочитать инструменты с live-счётчиком токенов.

## Связанные записи
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[headroom-token-saver]] ([Headroom Token Saver](../tools/headroom-token-saver.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[opencode-rate-limiter-plugin]] ([OpenCode Rate Limiter Plugin](../tools/opencode-rate-limiter-plugin.md))
