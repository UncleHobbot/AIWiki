---
title: "Open Source Models vs Claude Opus: Real-World Coding Benchmark"
title_ru: "Open source модели vs Claude Opus: реальный бенчмарк написания кода"
category: models
tags: [open-source, claude-opus, kimi-k2, minimax-m2, glm-5, deepseek-v4, qwen, github-copilot, benchmark, cost-comparison]
aliases: [Kimi K2.6 benchmark, MiniMax M2.7 review, GLM 5.1 coding test, open source vs Opus, model cost comparison]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=-yz5GDY3-P0
---

## Summary

An unscientific but practical comparison of five open-source models (Kimi K2.6, MiniMax M2.7, GLM 5.1, DeepSeek V4 Pro, Qwen 3.6 27B) against Claude Opus 4.6 using GitHub Copilot CLI to build a URL-sharing web app. Qwen 3.6 27B emerged as the best value — near-Opus accuracy at $4.90 vs Opus's $40.

## Key Ideas

- **Opus costs $40+ to build a real app** (with prompt caching; $267 without), making it economically unsustainable for many use cases
- **Qwen 3.6 27B wins overall**: 10/10 planning, 10/10 agency, ~9/10 accuracy, $4.90 — and could feasibly run locally on a ~$5,000 machine
- **GLM 5.1 is the top runner-up**: indistinguishable from Opus in planning quality, good accuracy, only $6 per build
- **MiniMax M2.7 is the cheapest** at $1.37 but disappointing accuracy; good for rapid iteration when quality is secondary
- **Kimi K2.6**: strong planning but poor execution accuracy; $11 — poor value proposition
- **No model can one-shot a real app** — all required 2–5 correction rounds; what differs is whether the model gets unstuck quickly

## Details

The test used GitHub Copilot CLI's plan mode → Autopilot → Fleet pipeline (the most token-hungry setup) with a public PRD for a URL-sharing app requiring GitHub authentication, vanity URL support, drag-and-drop reordering, and link publishing. All models used OpenRouter API pricing for comparability.

Scoring was across four dimensions: Planning quality (does it ask clarifying questions and create a detailed plan?), Agency (does it follow through with tool calls effectively?), Accuracy (how functional is the final app?), and Cost.

Opus remains the gold standard at 10/10 across quality dimensions. Its planning and accuracy are noticeably better than any open-source alternative, but the price gap is extreme. GLM 5.1's planning was rated as "indistinguishable from Opus" and its output was visually impressive, though it had a data-persistence bug.

The author notes that all these models have subscription/coding-plan alternatives (e.g., MiniMax's $10/month plan, Alibaba Cloud's $50/month Qwen plan) that make per-token costs even lower in practice.

## Video Notes

- [3:14] Contenders and pricing: Kimi K2.6 ($0.75/$3.50 per M tokens), MiniMax M2.7 ($0.30/$1.20), GLM 5.1 ($1.05/$3.50), DeepSeek V4 Pro ($1.32/$2.78), Qwen 3.6 27B ($0.32/$3.20), Opus 4.6 ($5/$25)
- [7:47] Baseline: Opus 4.6 — excellent planning, ~$40 with caching
- [11:13] Kimi K2.6 — good plan, very poor execution, $11.06
- [13:19] MiniMax M2.7 — weaker planning, great agency, broken UI, $1.37
- [15:31] GLM 5.1 — Opus-level planning, very functional app, $6
- [18:12] DeepSeek V4 Pro — good planning, functional, $8.72
- [20:22] Qwen 3.6 27B — surprisingly strong despite small size, $4.90
- [23:29] Verdict: Qwen wins, GLM is runner-up

## Related Entries

- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 vs Opus vs Kimi](../models/deepseek-v4-vs-opus-kimi.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM 5.1](../models/gpt-vs-glm-5-1-comparison.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))

---
<!-- RU -->

## Краткое описание

Практическое сравнение пяти open source моделей (Kimi K2.6, MiniMax M2.7, GLM 5.1, DeepSeek V4 Pro, Qwen 3.6 27B) с Claude Opus 4.6 в задаче написания реального веб-приложения через GitHub Copilot CLI. Победитель — Qwen 3.6 27B: почти такое же качество как у Opus за $4.90 вместо $40.

## Ключевые идеи

- **Opus стоит $40+ на разработку одного приложения** (с кешированием промптов; $267 без него)
- **Qwen 3.6 27B — лучшее соотношение цены и качества**: 10/10 за планирование, ~9/10 за точность, $4.90; потенциально можно запустить локально
- **GLM 5.1 — ближайший конкурент**: качество планирования неотличимо от Opus, хорошая точность, всего $6
- **MiniMax M2.7 — самый дешёвый** ($1.37), но низкое качество финального кода
- **Ни одна модель не может создать приложение с первой попытки** — все требовали 2–5 итераций исправлений

## Подробнее

Тест проводился через pipeline: plan mode → Autopilot → Fleet в GitHub Copilot CLI с публичным PRD для приложения на основе GitHub-аутентификации, поддержкой ванитных URL, drag-and-drop и публикацией списков ссылок.

Оценка по четырём критериям: качество планирования, агентность (следование инструкциям через вызовы инструментов), точность реализации, стоимость. Opus остаётся золотым стандартом по качеству, но разрыв в цене огромен. GLM 5.1 показал планирование, неотличимое от Opus, и визуально впечатляющий результат, хотя и с багом сохранения данных.

## Заметки по видео

- [3:14] Стоимость API: Kimi K2.6 ($0.75/$3.50 за M токенов), MiniMax M2.7 ($0.30/$1.20), GLM 5.1 ($1.05/$3.50), DeepSeek V4 Pro ($1.32/$2.78), Qwen 27B ($0.32/$3.20), Opus 4.6 ($5/$25)
- [23:29] Итог: победа Qwen, второе место GLM 5.1

## Связанные записи

- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 vs Opus vs Kimi](../models/deepseek-v4-vs-opus-kimi.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM 5.1](../models/gpt-vs-glm-5-1-comparison.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
