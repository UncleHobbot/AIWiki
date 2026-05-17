---
title: "Chinese LLM Models for Building Karpathy's LLM Wiki: DeepSeek, Kimi, GLM, Qwen, MiMo"
title_ru: "Китайские LLM-модели для создания LLM Wiki Карпати: DeepSeek, Kimi, GLM, Qwen, MiMo"
category: models
tags: [deepseek, kimi, glm, qwen, mimo, chinese-llm, benchmarks, llm-wiki, karpathy, lmarena, pricing]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://benchlm.ai/blog/posts/best-chinese-llm
  - https://www.verdent.ai/guides/deepseek-v4-pricing-api-migration-2026
  - https://openrouter.ai/z-ai/glm-5.1
  - https://mimo.xiaomi.com/mimo-v2-pro
  - https://lambda.ai/llm-benchmarks-leaderboard
  - https://www.clickrank.ai/llm-leaderboard/
  - https://www.reddit.com/r/LocalLLaMA/comments/1sjv5f8/top_10_open_weight_models_in_lmarena/
---

## Summary

Comparison of Chinese frontier LLMs evaluated for building Karpathy-style LLM Wiki knowledge bases — covering DeepSeek V4, Kimi K2.6, GLM-5/5.1, Qwen 3.5/3.6, and Xiaomi MiMo-V2.5. Includes BenchLM scores, Arena Code rankings, API pricing, context windows, and suitability for knowledge extraction, bilingual summarization, and agentic wiki workflows.

## Key Ideas

- DeepSeek V4 Pro (Max) leads the Chinese frontier at BenchLM score 87, followed by Kimi K2.6 (84), GLM-5.1 (83), Qwen 3.5 397B (79)
- GLM-5.1 tops the LM Arena Code leaderboard at Elo 1530, demonstrating elite real-world coding performance
- All top Chinese models are open-weight, enabling self-hosting — a structural advantage over Western proprietary APIs
- For LLM Wiki tasks (extraction, summarization, classification, bilingual generation), cost efficiency and long context are the deciding factors
- DeepSeek V4 Flash at $0.14/$0.28 per M tokens offers the best price-performance for high-volume wiki processing
- MiMo-V2.5-Pro excels at long-horizon agentic tasks (multi-hour workflows, thousands of tool calls) — ideal for autonomous wiki maintenance

## Benchmark Comparison

### Overall Scores (BenchLM, May 2026)

| Rank | Model | Creator | Score | Type | Open Weight | Context |
|------|-------|---------|-------|------|-------------|---------|
| 1 | DeepSeek V4 Pro (Max) | DeepSeek | 87 | Reasoning | Yes | 1M |
| 2 | Kimi K2.6 | Moonshot AI | 84 | Non-Reasoning | Yes | 256K |
| 3 | GLM-5 (Reasoning) | Z.AI | 83 | Reasoning | Yes | 200K |
| 4 | GLM-5.1 | Z.AI | 83 | Non-Reasoning | Yes | 203K |
| 5 | DeepSeek V4 Pro (High) | DeepSeek | 83 | Reasoning | Yes | 1M |
| 6 | Qwen3.5 397B (Reasoning) | Alibaba | 79 | Reasoning | Yes | 128K |
| 7 | Kimi K2.5 (Reasoning) | Moonshot AI | 77 | Reasoning | No | 128K |
| 8 | DeepSeek V4 Flash (Max) | DeepSeek | 77 | Reasoning | Yes | 1M |
| 9 | Qwen3.6-27B | Alibaba | 75 | Non-Reasoning | Yes | 262K |
| 10 | MiMo-V2.5-Pro | Xiaomi | ~75* | Non-Reasoning | Yes | 1M |

*Miro score estimated from composite benchmarks; not yet fully ranked on BenchLM.

### LM Arena Code Leaderboard (Open Models, April 2026)

| Rank | Model | Elo Score | Votes |
|------|-------|-----------|-------|
| 1 | GLM-5.1 | 1530 | 1,046 |
| 2 | GLM-4.7 | 1439 | 4,878 |
| 3 | DeepSeek V4 Pro | ~1420 | High |
| 4 | Qwen-3.5-397B-A17B | ~1400 | High |
| 5 | MiMo-V2-Pro | ~1380 | Growing |

### Coding Benchmarks (Selected)

| Model | Coding Score (BenchLM) | SWE-bench Verified | LiveCodeBench |
|-------|----------------------|--------------------|---------------|
| DeepSeek V4 Pro (Max) | 89.8 | 72%+ | High |
| Kimi K2.6 | 88.7 | 70%+ | High |
| GLM-5.1 | 84.1 | High | High |
| Qwen3.5 397B | 86.7 | 68%+ | 69.5% |
| MiMo-V2-Pro | 81.0 (ClawEval) | 71.7% | — |

### Global Context (vs Western Frontier)

| Model | Score |
|-------|-------|
| Gemini 3.1 Pro | 93 |
| GPT-5.4 Pro | 92 |
| Claude Opus 4.6 | 88 |
| **DeepSeek V4 Pro (Max)** | **87** |
| **Kimi K2.6** | **84** |
| **GLM-5.1** | **83** |
| **Qwen3.5 397B** | **79** |

## API Pricing Comparison

| Model | Input ($/M tokens) | Output ($/M tokens) | Context Window | Max Output |
|-------|--------------------|--------------------|----------------|------------|
| **DeepSeek V4 Flash** | $0.14 | $0.28 | 1M | 384K |
| **DeepSeek V4 Pro** | $1.74 | $3.48 | 1M | 384K |
| **Kimi K2.6** | $0.95 | $2.50 | 256K | Standard |
| **GLM-5** | $1.00 | $4.00 | 200K | Standard |
| **GLM-5.1** | $0.98–$1.40 | $3.08–$4.40 | 203K | 64K |
| **Qwen 3.5 397B** | ~$0.40 | ~$1.20 | 128K | Standard |
| **Qwen 3.5 (small)** | $0.02 | $0.06 | 128K | Standard |
| **MiMo-V2-Pro (≤256K)** | $1.00 | $3.00 | 1M | Standard |
| **MiMo-V2-Pro (256K–1M)** | $2.00 | $6.00 | 1M | Standard |

### Cost for Typical LLM Wiki Workload

Assuming processing 50 wiki entries/day, ~4K input + ~2K output tokens each:

| Model | Daily Cost | Monthly Cost |
|-------|-----------|--------------|
| DeepSeek V4 Flash | $0.01 | $0.30 |
| Qwen 3.5 (small) | $0.001 | $0.03 |
| Kimi K2.6 | $0.05 | $1.50 |
| DeepSeek V4 Pro | $0.17 | $5.10 |
| GLM-5.1 | $0.10 | $3.00 |
| MiMo-V2-Pro | $0.05 | $1.50 |

## Model-by-Model Analysis

### DeepSeek V4 (DeepSeek)

**Strengths:** Highest BenchLM score among Chinese models (87). 1M context window as default floor. MIT-licensed open weights. Two tiers: Flash (ultra-cheap) and Pro (frontier quality). Supports both OpenAI and Anthropic API formats. Hybrid Attention (CSA+HCA) reduces long-context inference cost by 73% vs V3.2.

**Weaknesses:** Pro tier pricing ($1.74/$3.48) is 12x Flash. Legacy API aliases (`deepseek-chat`, `deepseek-reasoner`) retire July 24, 2026 — migration needed.

**Best for LLM Wiki:** Flash tier for high-volume extraction and summarization (best cost-efficiency). Pro tier for complex classification, entity extraction, and quality-sensitive bilingual generation.

### Kimi K2.6 (Moonshot AI)

**Strengths:** Second-strongest Chinese model overall (84). Elite coding score (88.7). Open weight. Strong in agentic coding workflows. K2.5 Reasoning variant available for deeper analysis tasks.

**Weaknesses:** 256K context (smaller than DeepSeek/MiMo 1M). Pricing higher than DeepSeek Flash. Less mature tool ecosystem compared to DeepSeek.

**Best for LLM Wiki:** Code-heavy wiki maintenance scripts, transcript analysis from YouTube coding videos, processing technical content with code examples.

### GLM-5 / GLM-5.1 (Z.AI / Zhipu AI)

**Strengths:** GLM-5.1 tops LM Arena Code leaderboard (Elo 1530). GLM-5 (Reasoning) is strongest Chinese model for math/reasoning. 200-203K context. Open weights. Native bilingual (Chinese/English) capabilities — built by a Chinese lab with strong multilingual training. GLM-5.1 supports up to 8 hours of continuous autonomous work on a single task.

**Weaknesses:** GLM-5.1 pricing is 2.5x GLM-5. Smaller context window than DeepSeek V4. API ecosystem less mature.

**Best for LLM Wiki:** Best choice for bilingual EN/RU generation quality. GLM-5 (Reasoning) for complex classification and knowledge graph construction. GLM-5.1 for long-form autonomous wiki maintenance tasks.

### Qwen 3.5 / 3.6 (Alibaba)

**Strengths:** Broadest model family with sizes from 0.8B to 397B. Qwen3.6-27B is an excellent efficiency/quality tradeoff at score 75. Strong multilingual support including Russian. Well-documented API. Multiple quantization options for self-hosting. Qwen3.6 offers 262K context in the 27B variant.

**Weaknesses:** Top Qwen model (397B Reasoning) scores 79 — 8 points behind DeepSeek V4 Pro. 128K context for flagship variant. Requires choosing the right variant from a large family.

**Best for LLM Wiki:** Qwen3.5-397B for high-quality bilingual generation. Qwen3.6-27B for cost-effective bulk processing and self-hosting. Small variants (0.8B) for edge deployment or real-time classification.

### Xiaomi MiMo-V2.5-Pro (Xiaomi)

**Strengths:** 1T parameter MoE with 42B active — efficient inference. 1M token context window. MIT license. Excels at long-horizon agentic tasks: hundreds to thousands of tool calls, multi-hour workflows. Token-efficient: achieves similar performance using 40-60% fewer tokens. ClawEval score 81.0, approaching Claude Opus 4.6 (81.5). Integrated with OpenClaw, OpenCode, KiloCode, Blackbox, Cline.

**Weaknesses:** Newer entrant with smaller community. BenchLM ranking not yet fully established. API ecosystem still maturing. Miro-V2-Flash at score 63 is not competitive.

**Best for LLM Wiki:** Autonomous wiki maintenance agents that run multi-hour batch processing. Scanning entire wiki directories, cross-referencing entries, identifying gaps, and auto-generating updates. Best for the "agentic loop" pattern described in Karpathy's LLM OS concept.

## Suitability for Karpathy's LLM Wiki

### Task-by-Task Model Recommendations

| Wiki Task | Primary Choice | Budget Choice | Quality Choice |
|-----------|---------------|---------------|----------------|
| URL content extraction | DeepSeek V4 Flash | Qwen 3.5 small | DeepSeek V4 Pro |
| Article summarization | DeepSeek V4 Flash | Qwen 3.6-27B | Kimi K2.6 |
| Bilingual (EN/RU) generation | GLM-5.1 | Qwen 3.5 397B | DeepSeek V4 Pro |
| Content classification | Qwen 3.6-27B | DeepSeek V4 Flash | GLM-5 (Reasoning) |
| YouTube transcript analysis | Kimi K2.6 | DeepSeek V4 Flash | DeepSeek V4 Pro |
| Reddit post processing | DeepSeek V4 Flash | Qwen 3.6-27B | Kimi K2.6 |
| Wiki index generation | DeepSeek V4 Flash | Qwen 3.5 small | GLM-5.1 |
| Quality checking (RU section) | GLM-5.1 | Qwen 3.5 397B | DeepSeek V4 Pro |
| Autonomous batch agent | MiMo-V2.5-Pro | DeepSeek V4 Flash | GLM-5.1 |
| Knowledge graph construction | GLM-5 (Reasoning) | Qwen 3.6-27B | DeepSeek V4 Pro |

### Recommended Architecture for LLM Wiki

For a Karpathy-style three-layer wiki system:

1. **Extraction layer (Layer 1 → Layer 2):** DeepSeek V4 Flash for 90% of content processing. It handles URL fetching, article extraction, and initial classification at $0.14/$0.28 per M tokens. For a wiki processing 50-100 sources/day, this costs under $1/month.

2. **Distillation layer (wiki entry generation):** GLM-5.1 for bilingual generation quality. Its Arena Code Elo 1530 and native multilingual strength make it the best choice for producing high-quality EN/RU wiki entries.

3. **Autonomous maintenance layer:** MiMo-V2.5-Pro for long-running wiki maintenance agents. Its ability to handle multi-hour workflows with thousands of tool calls makes it ideal for periodic batch operations (index rebuilding, cross-reference checking, gap analysis).

4. **Fallback/overflow:** Qwen 3.6-27B for self-hosted deployment when API costs need to be zero, or for real-time tasks that don't require frontier quality.

## Notable Quotes

> "The Chinese frontier is stronger and more crowded than the old GLM-vs-Qwen-vs-DeepSeek framing suggests." — BenchLM, 2026

> "V4-Flash at $0.28/M output is roughly 90-100x cheaper than GPT-5.5. Whether the quality tradeoff is acceptable for your specific workload is the variable." — Verdent AI

> "The open-weight advantage: if you need downloadable weights, self-hosting, or deeper control of the inference stack, the Chinese frontier is still structurally stronger than the closed Western API tier." — BenchLM

## Related Entries
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 Pro vs Claude Opus 4.7 vs Kimi K2.6 Benchmark](../models/deepseek-v4-vs-opus-kimi.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1: Side-by-Side Coding Comparison](../models/gpt-vs-glm-5-1-comparison.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))

---
<!-- RU -->

## Краткое описание

Сравнение китайских передовых LLM-моделей для создания базы знаний в стиле LLM Wiki Карпати — охватывает DeepSeek V4, Kimi K2.6, GLM-5/5.1, Qwen 3.5/3.6 и Xiaomi MiMo-V2.5. Включает оценки BenchLM, рейтинги Arena Code, цены API, размеры контекстного окна и применимость для извлечения знаний, двуязычного реферирования и агентных вики-воркфлоу.

## Ключевые идеи

- DeepSeek V4 Pro (Max) лидирует среди китайских моделей с оценкой BenchLM 87, за ним следуют Kimi K2.6 (84), GLM-5.1 (83), Qwen 3.5 397B (79)
- GLM-5.1 возглавляет рейтинг LM Arena Code с Elo 1530, демонстрируя элитное качество кодинга в реальных задачах
- Все ведущие китайские модели имеют открытые веса, что позволяет самохостинг — структурное преимущество перед западными проприетарными API
- Для задач LLM Wiki (извлечение, реферирование, классификация, двуязычная генерация) решающими факторами являются стоимость и размер контекста
- DeepSeek V4 Flash за $0.14/$0.28 за М токенов предлагает лучшее соотношение цена/качество для высокоинтенсивной обработки
- MiMo-V2.5-Pro превосходит в задачах агентной автоматизации (многочасовые воркфлоу, тысячи вызовов инструментов) — идеально для автономного обслуживания вики

## Сравнение бенчмарков

### Общие оценки (BenchLM, май 2026)

| Место | Модель | Создатель | Оценка | Тип | Открытые веса | Контекст |
|-------|--------|-----------|--------|-----|---------------|----------|
| 1 | DeepSeek V4 Pro (Max) | DeepSeek | 87 | Рассуждение | Да | 1M |
| 2 | Kimi K2.6 | Moonshot AI | 84 | Без рассуждения | Да | 256K |
| 3 | GLM-5 (Reasoning) | Z.AI | 83 | Рассуждение | Да | 200K |
| 4 | GLM-5.1 | Z.AI | 83 | Без рассуждения | Да | 203K |
| 5 | DeepSeek V4 Pro (High) | DeepSeek | 83 | Рассуждение | Да | 1M |
| 6 | Qwen3.5 397B (Reasoning) | Alibaba | 79 | Рассуждение | Да | 128K |
| 7 | Kimi K2.5 (Reasoning) | Moonshot AI | 77 | Рассуждение | Нет | 128K |
| 8 | DeepSeek V4 Flash (Max) | DeepSeek | 77 | Рассуждение | Да | 1M |
| 9 | Qwen3.6-27B | Alibaba | 75 | Без рассуждения | Да | 262K |
| 10 | MiMo-V2.5-Pro | Xiaomi | ~75* | Без рассуждения | Да | 1M |

### Рейтинг LM Arena Code (открытые модели, апрель 2026)

| Место | Модель | Elo | Голоса |
|-------|--------|-----|--------|
| 1 | GLM-5.1 | 1530 | 1,046 |
| 2 | GLM-4.7 | 1439 | 4,878 |
| 3 | DeepSeek V4 Pro | ~1420 | Высокий |
| 4 | Qwen-3.5-397B-A17B | ~1400 | Высокий |
| 5 | MiMo-V2-Pro | ~1380 | Растёт |

### Глобальный контекст (vs западный фронтир)

| Модель | Оценка |
|--------|--------|
| Gemini 3.1 Pro | 93 |
| GPT-5.4 Pro | 92 |
| Claude Opus 4.6 | 88 |
| **DeepSeek V4 Pro (Max)** | **87** |
| **Kimi K2.6** | **84** |
| **GLM-5.1** | **83** |
| **Qwen3.5 397B** | **79** |

## Сравнение цен API

| Модель | Ввод ($/М токенов) | Вывод ($/М токенов) | Контекст | Макс. вывод |
|--------|--------------------|--------------------|----------|-------------|
| **DeepSeek V4 Flash** | $0.14 | $0.28 | 1M | 384K |
| **DeepSeek V4 Pro** | $1.74 | $3.48 | 1M | 384K |
| **Kimi K2.6** | $0.95 | $2.50 | 256K | Стандартный |
| **GLM-5** | $1.00 | $4.00 | 200K | Стандартный |
| **GLM-5.1** | $0.98–$1.40 | $3.08–$4.40 | 203K | 64K |
| **Qwen 3.5 397B** | ~$0.40 | ~$1.20 | 128K | Стандартный |
| **Qwen 3.5 (малая)** | $0.02 | $0.06 | 128K | Стандартный |
| **MiMo-V2-Pro (≤256K)** | $1.00 | $3.00 | 1M | Стандартный |
| **MiMo-V2-Pro (256K–1M)** | $2.00 | $6.00 | 1M | Стандартный |

### Стоимость типичной нагрузки LLM Wiki

При обработке 50 статей/день, ~4K входных + ~2K выходных токенов каждая:

| Модель | Стоимость/день | Стоимость/месяц |
|--------|---------------|-----------------|
| DeepSeek V4 Flash | $0.01 | $0.30 |
| Qwen 3.5 (малая) | $0.001 | $0.03 |
| Kimi K2.6 | $0.05 | $1.50 |
| DeepSeek V4 Pro | $0.17 | $5.10 |
| GLM-5.1 | $0.10 | $3.00 |
| MiMo-V2-Pro | $0.05 | $1.50 |

## Анализ по моделям

### DeepSeek V4 (DeepSeek)

**Сильные стороны:** Наивысшая оценка BenchLM среди китайских моделей (87). Контекстное окно 1M по умолчанию. Открытые веса по лицензии MIT. Два уровня: Flash (ультра-дешёвый) и Pro (качество фронтира). Поддержка форматов API OpenAI и Anthropic. Гибридное внимание (CSA+HCA) снижает стоимость вывода на 73% по сравнению с V3.2.

**Слабые стороны:** Ценовой уровень Pro ($1.74/$3.48) в 12 раз выше Flash. Устаревшие API-алиасы (`deepseek-chat`, `deepseek-reasoner`) будут отключены 24 июля 2026 — необходима миграция.

**Лучше всего для LLM Wiki:** Уровень Flash для высокоинтенсивного извлечения и реферирования (лучшая экономическая эффективность). Уровень Pro для сложной классификации, извлечения сущностей и чувствительной к качеству двуязычной генерации.

### Kimi K2.6 (Moonshot AI)

**Сильные стороны:** Вторая по силе китайская модель (84). Элитный кодинг (88.7). Открытые веса. Сильна в агентных кодинговых воркфлоу. Доступен вариант K2.5 Reasoning для более глубокого анализа.

**Слабые стороны:** Контекст 256K (меньше, чем 1M у DeepSeek/MiMo). Цены выше, чем у DeepSeek Flash. Менее зрелая экосистема инструментов.

**Лучше всего для LLM Wiki:** Скрипты обслуживания вики, анализ транскриптов YouTube, обработка технического контента с примерами кода.

### GLM-5 / GLM-5.1 (Z.AI / Zhipu AI)

**Сильные стороны:** GLM-5.1 возглавляет рейтинг Arena Code (Elo 1530). GLM-5 (Reasoning) — сильнейшая китайская модель для математики и рассуждений. Контекст 200-203K. Открытые веса. Нативная двуязычность (китайский/английский) — разработана китайской лабораторией с сильной многоязычной подготовкой. GLM-5.1 поддерживает до 8 часов непрерывной автономной работы над одной задачей.

**Слабые стороны:** Цены GLM-5.1 в 2.5 раза выше GLM-5. Контекстное окно меньше, чем у DeepSeek V4. Экосистема API менее зрелая.

**Лучше всего для LLM Wiki:** Лучший выбор для качества двуязычной (EN/RU) генерации. GLM-5 (Reasoning) для сложной классификации и построения графов знаний. GLM-5.1 для длительных автономных задач обслуживания вики.

### Qwen 3.5 / 3.6 (Alibaba)

**Сильные стороны:** Самое широкое семейство моделей с размерами от 0.8B до 397B. Qwen3.6-27B — отличный баланс эффективность/качество при оценке 75. Сильная многоязычная поддержка, включая русский. Хорошо документированный API. Множество вариантов квантизации для самохостинга.

**Слабые стороны:** Лучшая модель Qwen (397B Reasoning) набирает 79 — на 8 очков меньше DeepSeek V4 Pro. Контекст 128K для флагманского варианта. Необходимо выбирать правильный вариант из большого семейства.

**Лучше всего для LLM Wiki:** Qwen3.5-397B для высококачественной двуязычной генерации. Qwen3.6-27B для экономичной массовой обработки и самохостинга. Малые варианты (0.8B) для развёртывания на краю или классификации в реальном времени.

### Xiaomi MiMo-V2.5-Pro (Xiaomi)

**Сильные стороны:** MoE на 1T параметров с 42B активных — эффективный вывод. Контекстное окно 1M токенов. Лицензия MIT. Превосходит в задачах агентной автоматизации: сотни и тысячи вызовов инструментов, многочасовые воркфлоу. Эффективность токенов: достигает аналогичного качества, используя на 40-60% меньше токенов. ClawEval 81.0, приближаясь к Claude Opus 4.6 (81.5). Интегрирована с OpenClaw, OpenCode, KiloCode, Blackbox, Cline.

**Слабые стороны:** Новый участник с меньшим сообществом. Рейтинг BenchLM ещё не полностью установлен. Экосистема API всё ещё формируется.

**Лучше всего для LLM Wiki:** Автономные агенты обслуживания вики, выполняющие многочасовую пакетную обработку. Сканирование всех каталогов вики, перекрёстные ссылки, выявление пробелов и автоматическая генерация обновлений. Идеально для паттерна «агентный цикл», описанного в концепции LLM OS Карпати.

## Применимость для LLM Wiki Карпати

### Рекомендации по задачам

| Задача вики | Основной выбор | Бюджетный выбор | Выбор качества |
|-------------|---------------|-----------------|----------------|
| Извлечение контента из URL | DeepSeek V4 Flash | Qwen 3.5 малая | DeepSeek V4 Pro |
| Реферирование статей | DeepSeek V4 Flash | Qwen 3.6-27B | Kimi K2.6 |
| Двуязычная генерация (EN/RU) | GLM-5.1 | Qwen 3.5 397B | DeepSeek V4 Pro |
| Классификация контента | Qwen 3.6-27B | DeepSeek V4 Flash | GLM-5 (Reasoning) |
| Анализ транскриптов YouTube | Kimi K2.6 | DeepSeek V4 Flash | DeepSeek V4 Pro |
| Обработка постов Reddit | DeepSeek V4 Flash | Qwen 3.6-27B | Kimi K2.6 |
| Генерация индекса вики | DeepSeek V4 Flash | Qwen 3.5 малая | GLM-5.1 |
| Проверка качества (RU раздел) | GLM-5.1 | Qwen 3.5 397B | DeepSeek V4 Pro |
| Автономный пакетный агент | MiMo-V2.5-Pro | DeepSeek V4 Flash | GLM-5.1 |
| Построение графа знаний | GLM-5 (Reasoning) | Qwen 3.6-27B | DeepSeek V4 Pro |

### Рекомендуемая архитектура для LLM Wiki

Для трёхуровневой вики-системы в стиле Карпати:

1. **Уровень извлечения (Слой 1 → Слой 2):** DeepSeek V4 Flash для 90% обработки контента. Обрабатывает получение URL, извлечение статей и начальную классификацию по цене $0.14/$0.28 за М токенов. Для вики, обрабатывающей 50-100 источников/день, это стоит менее $1/месяц.

2. **Уровень дистилляции (генерация статей вики):** GLM-5.1 для качества двуязычной генерации. Arena Code Elo 1530 и нативная многоязычная сила делают его лучшим выбором для создания высококачественных EN/RU записей.

3. **Уровень автономного обслуживания:** MiMo-V2.5-Pro для длительных агентов обслуживания вики. Способность обрабатывать многочасовые воркфлоу с тысячами вызовов инструментов делает его идеальным для периодических пакетных операций (перестроение индекса, проверка перекрёстных ссылок, анализ пробелов).

4. **Резерв/переполнение:** Qwen 3.6-27B для самохостинга, когда затраты на API должны быть нулевыми, или для задач реального времени, не требующих качества фронтира.

## Примечательные цитаты

> «Китайский фронтир сильнее и более переполнен, чем предполагает старая рамка GLM-против-Qwen-против-DeepSeek.» — BenchLM, 2026

> «V4-Flash за $0.28/М вывода примерно в 90-100 раз дешевле GPT-5.5. Приемлем ли компромисс в качестве для вашей конкретной нагрузки — это переменная.» — Verdent AI

> «Преимущество открытых весов: если вам нужны загружаемые веса, самохостинг или более глубокий контроль над стеком вывода, китайский фронтир структурно сильнее закрытого западного API-уровня.» — BenchLM

## Связанные записи
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 Pro vs Claude Opus 4.7 vs Kimi K2.6 Benchmark](../models/deepseek-v4-vs-opus-kimi.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1: Side-by-Side Coding Comparison](../models/gpt-vs-glm-5-1-comparison.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
