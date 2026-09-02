---
title: "Tencent Hy4 Preview — 770B Open-Weight MoE with 1M Context"
title_ru: "Tencent Hy4 Preview — открытая MoE-модель на 770B с контекстом 1M"
category: news
tags: [tencent, hunyuan, hy4, open-weights, moe, 1m-context, coding, mtp]
aliases: [Hy4, Hunyuan 4, tencent hy4, hy4 preview]
confidence: high
date: 2026-08-28
updated: 2026-09-01
sources:
  - https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/
  - https://x.com/opencode/status/2093369212068864219
  - https://www.mindstudio.ai/blog/tencent-hy4-preview-open-weight-model
---

## Summary
Tencent released and open-sourced **Hy4 Preview** (Hunyuan 4), a next-generation flagship LLM with 770B total parameters and 49B active (MoE), a 1M+ token context window, and a built-in 10B multi-token-prediction (MTP) speculative-decoding layer. It's positioned for coding and research workloads — and shipped day-one into OpenCode Go as a preview model.

## Key Ideas
- **Architecture:** 770B total / 49B active per token (MoE); FP8 variant ships alongside the main release.
- **1M+ context** — among the largest open-weight context windows, aimed at repo-scale coding sessions.
- **Speculative decoding built in:** a dedicated 10B MTP weight file reduces serving latency out of the box.
- **Coding-first positioning:** Tencent explicitly targets coding and research; available in OpenCode Go (770B/49B, 1M context) per the OpenCode announcement.
- Strengthens the Chinese open-weight lineup alongside GLM-5.x, DeepSeek V4, and Kimi K-series ([[closed-vs-open-model-scaffolding-gap]] for why that matters).

## Details
Hy4 Preview continues the 2026 pattern of Chinese labs shipping huge open-weight MoE models with coding as the lead use case. The MTP layer mirrors the speculative-decoding trend ([[mimo-v25-pro-dflash-1000tps]]); the 1M context mirrors GLM-5.2's playbook. For local/AGPL users the interesting question is quant availability and serving cost — a 770B MoE with 49B active is a multi-GPU proposition regardless of quantization.

## Related Entries
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[mimo-v25-pro-dflash-1000tps]] ([MiMo V2.5 Pro dFlash](mimo-v25-pro-dflash-1000tps.md))
- [[closed-vs-open-model-scaffolding-gap]] ([Closed vs Open Scaffolding Gap](../concepts/closed-vs-open-model-scaffolding-gap.md))

---
- [[unsloth-qwen38-27b-gguf]] ([Unsloth Qwen3.8-27B GGUF](../models/unsloth-qwen38-27b-gguf.md))
<!-- RU -->

## Краткое описание
Tencent выпустила и открыла **Hy4 Preview** (Hunyuan 4) — флагманскую LLM нового поколения с 770B общих параметров и 49B активных (MoE), контекстом 1M+ токенов и встроенным 10B-слоем multi-token prediction (MTP) для спекулятивного декодирования. Позиционируется для кодинга и исследований — и с первого дня доступна в OpenCode Go.

## Ключевые идеи
- **Архитектура:** 770B общих / 49B активных на токен (MoE); рядом выходит FP8-вариант.
- **Контекст 1M+** — один из крупнейших среди открытых весов, для репо-масштабных сессий.
- **Спекулятивное декодирование из коробки:** отдельный файл весов MTP на 10B снижает latency сервинга.
- **Кодинг-фокус:** Tencent явно целится в кодинг и исследования; доступна в OpenCode Go.
- Усиливает линейку китайских открытых весов рядом с GLM-5.x, DeepSeek V4 и Kimi K-серии.

## Подробнее
Hy4 Preview продолжает паттерн 2026 года: китайские лаборатории выпускают огромные открытые MoE-модели с кодингом как ведущим сценарием. Слой MTP повторяет тренд спекулятивного декодирования; контекст 1M повторяет игру GLM-5.2. Для локального запуска вопрос — доступность квантов и стоимость сервинга: 770B MoE с 49B активными — это мульти-GPU в любом случае.

## Связанные записи
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[mimo-v25-pro-dflash-1000tps]] ([MiMo V2.5 Pro dFlash](mimo-v25-pro-dflash-1000tps.md))
- [[closed-vs-open-model-scaffolding-gap]] ([Closed vs Open Scaffolding Gap](../concepts/closed-vs-open-model-scaffolding-gap.md))
