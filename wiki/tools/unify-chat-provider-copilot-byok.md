---
title: "Unify Chat Provider: Use the VS Code Copilot Harness With Any BYOK Model"
title_ru: "Unify Chat Provider: использование Copilot-харнеса в VS Code с любой BYOK-моделью"
category: tools
tags: [github-copilot, vscode, byok, claude, codex, gemini, opencode, harness]
aliases: [Unify Chat Provider, vscode-unify-chat-provider, Copilot harness BYOK]
confidence: medium
updated: 2026-06-29
sources:
  - https://github.com/smallmain/vscode-unify-chat-provider
  - https://www.reddit.com/r/GithubCopilot/comments/1uj1rq6/using_the_copilot_harness_without_a_copilot/
---

## Summary
Unify Chat Provider is a VS Code extension that lets developers keep using GitHub Copilot's agent harness in VS Code after cancelling their Copilot subscription, by bringing their own keys (BYOK) for Codex, Claude, Gemini, and OpenCode. It targets users who consider the Copilot harness superior to alternatives but no longer find the subscription worthwhile after pricing changes.

## Key Ideas
- **Decouples harness from subscription**: the Copilot team's BYOK work makes it possible to drive the VS Code Copilot harness with external providers; this extension surfaces that capability.
- **Supported providers**: Codex, Claude, Gemini, and Open Code — usable through the same Copilot UI/workflow.
- **Motivation — pricing backlash**: the r/GithubCopilot community reports many users cancelling subscriptions over pricing changes; this lets them keep the harness they prefer.
- **The "harness > model" thesis**: the poster's framing — "the Copilot harness in VS Code is leagues above its competition" — reinforces that the scaffolding around a model often matters more than the model itself.
- **Open gap**: inline autocomplete/suggestions via external providers was not yet well covered at time of posting (the harness's agent/chat mode is the main use case).

## Details
This extension is a symptom of a broader 2026 trend: as subscription prices rise and model quality converges, developers increasingly want to mix and match — keeping the IDE integration/harness they like while supplying the model via whichever provider is cheapest or best at a given moment. BYOK extensions turn a locked-in subscription product into an open harness.

The discussion also highlights that "harness engineering" (the prompts, tools, context policies, and UI affordances around a model) is becoming a differentiator independent of the underlying model — consistent with the agent-harness-engineering thesis documented elsewhere in this wiki.

## Related Entries
- [[github-copilot-cli]] ([GitHub Copilot CLI](github-copilot-cli.md))
- [[product-github-copilot]] ([GitHub Copilot CLI and App](product-github-copilot.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))

---
<!-- RU -->

## Краткое описание
Unify Chat Provider — расширение VS Code, позволяющее разработчикам продолжать использовать agent-харнес GitHub Copilot в VS Code после отмены подписки Copilot, подключая собственные ключи (BYOK) для Codex, Claude, Gemini и OpenCode. Нацелено на тех, кто считает харнес Copilot превосходящим альтернативы, но больше не видит смысла в подписке после изменения цен.

## Ключевые идеи
- **Отвязка харнеса от подписки**: BYOK-работа команды Copilot позволяет управлять харнесом VS Code Copilot внешними провайдерами; расширение делает это доступным.
- **Поддерживаемые провайдеры**: Codex, Claude, Gemini и Open Code — через тот же UI/воркфлоу Copilot.
- **Мотивация — бэклаш из-за цен**: сообщество r/GithubCopilot сообщает о массовых отменах подписок из-за изменения цен; расширение позволяет сохранить любимый харнес.
- **Тезис «харнес важнее модели»**: формулировка автора — «харнес Copilot в VS Code на голову выше конкурентов» — подтверждает, что обвязка вокруг модели часто важнее самой модели.
- **Открытый пробел**: inline-автокомплит через внешних провайдеров на момент поста был слабо покрыт.

## Подробнее
Расширение — симптом более широкого тренда 2026 года: по мере роста цен на подписки и конвергенции качества моделей разработчики всё чаще хотят комбинировать — сохранять любимую IDE-интеграцию/харнес, поставляя модель от самого дешёвого или лучшего провайдера в данный момент. BYOK-расширения превращают залоченный подписочный продукт в открытый харнес.

Дискуссия также подчёркивает, что «harness engineering» (промпты, инструменты, политики контекста и UI вокруг модели) становится дифференциатором, независимым от самой модели.

## Связанные записи
- [[github-copilot-cli]] ([GitHub Copilot CLI](github-copilot-cli.md))
- [[product-github-copilot]] ([GitHub Copilot CLI and App](product-github-copilot.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
