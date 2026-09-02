---
title: "Kimi K3 Regression — Reasoning History No Longer Accepted via Chat Completions"
title_ru: "Регрессия Kimi K3 — reasoning-история больше не принимается через Chat Completions"
category: news
tags: [kimi, k3, reasoning, regression, opencode, api, multimodal]
aliases: [kimi k3 reasoning history, kimi reasoning regression]
confidence: medium
date: 2026-09-01
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/opencode/comments/1w5d1y0/kimi_k3_no_longer_accepts_reasoning_history_very/
---

## Summary
A breaking API-behavior change reported on r/opencode: a few days before the post, **Kimi K3 (via OpenCode's chat-completions-style API) stopped accepting reasoning content from previous turns** — the model forgets what it was thinking in all prior turns, degrading performance in agentic loops. Worse: with chat-completions, multimodal tool outputs are displayed as user messages, so *viewing an image within a turn erases the reasonings even within that turn* — and PDF reading (pages rendered to PNGs) forgets reasoning with every new page request.

## Key Ideas
- **What broke:** reasoning-history replay — prior turns' thinking content no longer accepted/returned in context.
- **Why it matters disproportionately for agents:** agentic loops depend on the model's own prior reasoning to stay consistent across steps; dropping it degrades multi-step coherence.
- **The multimodal compounding:** image/PDF tool outputs arriving as user messages flush within-turn reasoning — a structural interaction bug between chat-completions-shaped APIs and reasoning models.
- **Harness-side plea:** "Please OpenCode, figure it out with Kimi, it was working well until a week ago" — a vendor-side regression, not a harness bug.
- Connects to [[toolhound-tool-call-failure-taxonomy]] (format/compliance layer) and the reasoning-trace questions in [[closed-vs-open-model-scaffolding-gap]].

## Details
Reasoning-history handling is becoming a real compatibility axis for reasoning models served through chat-completions APIs: OpenAI-style `reasoning_content` replay, Anthropic-style thinking blocks, and vendors dropping support mid-flight. For harness builders the lesson is to pin API behavior versions and add contract tests for reasoning replay; for users, sudden quality drops in a stable harness may be the provider, not the prompt.

## Related Entries
- [[kimi-k2-7-code]] ([Kimi K2.7 Code](../models/kimi-k2-7-code.md))
- [[kimi-code-quota-audit]] ([Kimi Code Quota Audit](kimi-code-quota-audit.md))
- [[chinese-code-harness-comparison]] ([Chinese Code Harness Comparison](../models/chinese-code-harness-comparison.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))

---
- [[kimi-k4-nvidia-chips-rumor]] ([Kimi K4 Rumor](kimi-k4-nvidia-chips-rumor.md))
<!-- RU -->

## Краткое описание
Ломающее изменение поведения API: за несколько дней до поста **Kimi K3 (через API OpenCode в стиле chat-completions) перестала принимать reasoning-контент из предыдущих ходов** — модель забывает, о чём думала ранее, что деградирует агентные циклы. Хуже: при chat-completions мультимодальные выводы инструментов показываются как user-сообщения, поэтому *просмотр изображения внутри хода стирает reasoning даже внутри этого хода* — а чтение PDF (страницы как PNG) забывает reasoning с каждым новым запросом страницы.

## Ключевые идеи
- **Что сломалось:** повтор reasoning-истории — thinking-контент предыдущих ходов больше не принимается/не возвращается в контексте.
- **Почему критично для агентов:** агентные циклы зависят от собственного prior-reasoning модели для согласованности между шагами.
- **Мультимодальное усугубление:** выводы инструментов с изображениями, приходящие как user-сообщения, затирают reasoning внутри хода — структурный баг взаимодействия chat-completions-API и reasoning-моделей.
- **Обращение к харнесу:** «OpenCode, разберитесь с Kimi — неделю назад всё работало» — регрессия на стороне вендора.
- Связано с [[toolhound-tool-call-failure-taxonomy]] и вопросами reasoning-трейсов в [[closed-vs-open-model-scaffolding-gap]].

## Подробнее
Обработка reasoning-истории становится реальной осью совместимости для reasoning-моделей через chat-completions API: replay в стиле OpenAI, thinking-блоки в стиле Anthropic, и вендоры, отключающие поддержку на лету. Для билдеров харнесов — фиксировать версии поведения API и добавлять контрактные тесты на reasoning-replay; для пользователей — внезапное падение качества в стабильном харнесе может быть провайдером, а не промптом.

## Связанные записи
- [[kimi-k2-7-code]] ([Kimi K2.7 Code](../models/kimi-k2-7-code.md))
- [[kimi-code-quota-audit]] ([Kimi Code Quota Audit](kimi-code-quota-audit.md))
- [[chinese-code-harness-comparison]] ([Chinese Code Harness Comparison](../models/chinese-code-harness-comparison.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
