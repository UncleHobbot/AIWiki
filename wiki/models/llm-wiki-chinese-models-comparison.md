---
title: "Chinese LLM Models for Building Karpathy's LLM Wiki: DeepSeek, Kimi, GLM, Qwen, MiMo, MiniMax"
title_ru: "Китайские LLM-модели для создания LLM Wiki Карпати: DeepSeek, Kimi, GLM, Qwen, MiMo, MiniMax"
category: models
tags: [deepseek, kimi, glm, qwen, mimo, minimax, chinese-llm, benchmarks, llm-wiki, karpathy, lmarena, pricing]
date: 2026-05-16
updated: 2026-06-14
sources:
  - https://benchlm.ai/blog/posts/best-chinese-llm
  - https://www.verdent.ai/guides/deepseek-v4-pricing-api-migration-2026
  - https://openrouter.ai/z-ai/glm-5.1
  - https://mimo.xiaomi.com/mimo-v2-pro
  - https://lambda.ai/llm-benchmarks-leaderboard
  - https://www.clickrank.ai/llm-leaderboard/
  - https://www.reddit.com/r/LocalLLaMA/comments/1sjv5f8/top_10_open_weight_models_in_lmarena/
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
  - https://openrouter.ai/deepseek/deepseek-v4-pro
  - https://openrouter.ai/moonshotai/kimi-k2.6
  - https://huggingface.co/zai-org/GLM-5.1
  - https://artificialanalysis.ai/leaderboards/models
  - https://lmarena.ai/?leaderboard
  - https://docs.z.ai/devpack/latest-model.md
  - https://huggingface.co/moonshotai/Kimi-K2.7-Code
  - https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart
  - https://openrouter.ai/models/moonshotai/kimi-k2.7-code
  - https://benchlm.ai/models/kimi-k2-7-code
---

## Summary

Comparison of Chinese frontier LLMs evaluated for building Karpathy-style LLM Wiki knowledge bases — covering DeepSeek V4, Kimi K2.6/K2.7 Code, GLM-5/5.1/5.2, Qwen 3.5/3.7, Xiaomi MiMo-V2.5, and MiniMax-M3. Includes BenchLM scores, LM Arena rankings, Artificial Analysis intelligence indices, API pricing, context windows, and suitability for knowledge extraction, bilingual summarization, and agentic wiki workflows. Updated June 2026 with Qwen3.7 Max, MiniMax-M3, GLM-5.2 (1M context), and Kimi K2.7 Code.

## Key Ideas

- **Qwen3.7 Max** is the new Chinese frontier leader at BenchLM 91, ranking #5 globally — a massive 12-point jump over Qwen3.5
- DeepSeek V4 Pro (Max) leads on coding benchmarks (LiveCodeBench 93.5) at BenchLM 87, but is now #2 Chinese model
- MiniMax-M3 enters the frontier tier at Artificial Analysis score 55, priced at just $0.22/M tokens — the cheapest frontier option
- **GLM-5.2** launched June 13, 2026 with a **1M-token context window** and High/Max thinking modes; open weights promised under MIT, but no benchmark scores published yet
- **Kimi K2.7 Code** released June 12, 2026 improves over K2.6 on all six Moonshot coding/agentic benchmarks, but still trails GPT-5.5 and Claude Opus 4.8
- All top Chinese models remain open-weight (MIT/Apache), a structural advantage over Western proprietary APIs
- For LLM Wiki tasks, the cost landscape shifted: MiMo-V2.5-Pro at $0.18/M and MiniMax-M3 at $0.22/M offer frontier quality at budget prices
- Qwen3.5-27B (dense model, not MoE) is the best efficiency play — competitive with models 5-10x its size

## Benchmark Comparison

### Overall Scores (BenchLM, June 2026)

| Rank | Model | Creator | Score | Open Weight | Context |
|------|-------|---------|-------|-------------|---------|
| 1 | Qwen3.7 Max | Alibaba | 91 | No | 1M |
| 2 | DeepSeek V4 Pro (Max) | DeepSeek | 87 | Yes (MIT) | 1M |
| 3 | Kimi K2.6 | Moonshot AI | 84 | Yes (Mod. MIT) | 262K |
| 4 | GLM-5 (Reasoning) | Z.AI | 83 | Yes (MIT) | 200K |
| 5 | GLM-5.1 | Z.AI | 82 | Yes (MIT) | 203K |
| 6 | DeepSeek V4 Pro (High) | DeepSeek | 83 | Yes (MIT) | 1M |
| 7 | Qwen3.5 397B (Reasoning) | Alibaba | 78 | Yes | 128K |
| 8 | Kimi K2.5 (Reasoning) | Moonshot AI | 77 | No | 128K |
| 9 | DeepSeek V4 Flash (Max) | DeepSeek | 77 | Yes (MIT) | 1M |
| 10 | Qwen3.5-27B | Alibaba | 75 | Yes | 262K |
| 11 | GLM-5.2 | Z.AI | N/A | Yes (MIT, pending) | 1M |
| 12 | Kimi K2.7 Code | Moonshot AI | Unranked | Yes (Mod. MIT) | 256K |

### Artificial Analysis Intelligence Index (June 2026)

| Model | Intelligence (0-100) | Price $/M in | Speed tok/s | TTFT |
|-------|---------------------|-------------|-------------|------|
| Qwen3.7 Max | 57 | $1.43 | 106 | 2.6s |
| MiniMax-M3 | 55 | $0.22 | 40 | 2.5s |
| Kimi K2.6 | 54 | $0.70 | 44 | 2.2s |
| MiMo-V2.5-Pro | 54 | $0.18 | 44 | 3.8s |
| DeepSeek V4 Pro (Max) | 52 | $0.44 | 53 | 1.8s |
| GLM-5.1 | 51 | $0.90 | 63 | 1.7s |
| DeepSeek V4 Pro (High) | 50 | $0.18 | 47 | 1.9s |
| MiniMax-M2.7 | 50 | $0.22 | 78 | 2.9s |
| DeepSeek V4 Flash (Max) | 47 | — | — | — |

### LM Arena Rankings (June 2026)

| Model | Text Arena | Coding Rank | Agent Arena | WebDev Arena |
|-------|-----------|-------------|-------------|-------------|
| GLM-5.1 | #14 | — | #8 (3.38%) | #8 (Elo 1532) |
| Qwen3.7 Max | #17 | — | — | #7 (Elo 1537) |
| MiMo-V2.5-Pro | #29 | — | — | — |
| Kimi K2.6 | #30 | #13 | #11 (0.56%) | — |
| DeepSeek V4 Pro (Think) | #34 | #21 | #12 (1.88%) | — |
| DeepSeek V4 Pro | #36 | #59 | — | — |
| MiniMax-M3 | #43 | — | — | #9 (Elo 1528) |

### Coding Benchmarks (Selected)

| Model | LiveCodeBench | SWE-bench Verified | SWE-bench Pro | Codeforces |
|-------|--------------|-------------------|---------------|------------|
| DeepSeek V4 Pro (Max) | **93.5** | 80.6% | 55.4% | **3206** |
| Qwen3.7 Max | 91.6 | 80.4% | — | — |
| DeepSeek V4 Flash (Max) | 91.6 | 79.0% | — | — |
| Kimi K2.6 | 89.6 | 80.2% | **58.6%** | — |
| GLM-5.1 | — | — | 58.4% | — |
| Qwen3.5-27B | 80.7 | 72.4% | — | — |
| MiMo-V2.5-Pro | — | 78.9% | — | — |

### Kimi K2.7 Code vs Frontier (Moonshot benchmarks)

| Benchmark | Kimi K2.6 | Kimi K2.7 Code | GPT-5.5 | Claude Opus 4.8 |
|-----------|-----------|----------------|---------|-----------------|
| Kimi Code Bench v2 | 50.9 | 62.0 | 69.0 | 67.4 |
| Program Bench | 48.3 | 53.6 | 69.1 | 63.8 |
| MLS Bench Lite | 26.7 | 35.1 | 35.5 | 42.8 |
| Kimi Claw 24/7 | 42.9 | 46.9 | 52.8 | 50.4 |
| MCP Atlas | 69.4 | 76.0 | 79.4 | 81.3 |
| MCP Mark Verified | 72.8 | 81.1 | 92.9 | 76.4 |

### Global Context (vs Western Frontier)

| Model | BenchLM Score |
|-------|-------------|
| Claude Mythos Preview | 99 |
| Claude Opus 4.8 | 95 |
| Gemini 3.1 Pro | 92 |
| GPT-5.5 | 91 |
| **Qwen3.7 Max** | **91** |
| GPT-5.4 Pro | 91 |
| Claude Opus 4.6 | 87 |
| **DeepSeek V4 Pro (Max)** | **87** |
| **Kimi K2.6** | **84** |
| **GLM-5.1** | **82** |
| **Qwen3.5 397B** | **78** |

## API Pricing Comparison

| Model | Input ($/M tokens) | Output ($/M tokens) | Context | Max Output | OpenRouter |
|-------|--------------------|--------------------|---------|-----------|-----------|
| **MiMo-V2.5-Pro** | $0.18 | $0.36 | 1M | Standard | Yes |
| **DeepSeek V4 Flash** | $0.14 (miss) / $0.003 (hit) | $0.28 | 1M | 384K | Yes ($0.10/$0.20) |
| **DeepSeek V4 Pro** | $0.435 (miss) / $0.004 (hit) | $0.87 | 1M | 384K | Yes |
| **MiniMax-M3** | $0.22 | $0.22 | — | Standard | Yes |
| **MiniMax-M2.7** | $0.22 | $0.22 | — | Standard | Yes |
| **Kimi K2.6** | $0.68 | $3.42 | 262K | Standard | Yes |
| **Kimi K2.7 Code** | $0.95 / $0.19 (cache hit) | $4.00 | 262K | Standard | Yes |
| **GLM-5.1** | $0.98 | $3.08 | 203K | 64K | Yes |
| **GLM-5.2** | Bundled in Coding Plan | Bundled in Coding Plan | 1M | 131K | Yes (pending) |
| **Qwen3.7 Max** | $1.43 | — | — | — | Yes |
| **Qwen3.7 Plus** | $0.25 | — | — | — | Yes |
| **Qwen3.5-27B** | ~$0.02 | ~$0.06 | 262K | Standard | — |

### Detailed Pricing Notes

- **DeepSeek V4** uses aggressive cache-hit pricing: $0.003/M input and $0.004/M output, making repeated queries nearly free.
- **Kimi K2.7 Code** cache-hit input on Kimi Platform is $0.19/M; OpenRouter flat rate is $0.75/$3.50.
- **GLM-5.2** is subscription-only at launch; no per-token API price. GLM Coding Plan Lite starts around $18/month for ~400 prompts/week.
- **Qwen3.7 Max** and **Qwen3.7 Plus** use Alibaba Cloud/DashScope; Plus is $0.25/M input, Max is $1.43/M input. Output pricing is not publicly listed.

### Cost for Typical LLM Wiki Workload

Assuming processing 50 wiki entries/day, ~4K input + ~2K output tokens each:

| Model | Daily Cost | Monthly Cost |
|-------|-----------|--------------|
| MiMo-V2.5-Pro | $0.008 | $0.24 |
| DeepSeek V4 Flash | $0.006 | $0.18 |
| MiniMax-M3 | $0.009 | $0.27 |
| Qwen3.5-27B (small) | $0.001 | $0.03 |
| DeepSeek V4 Pro | $0.04 | $1.20 |
| Kimi K2.6 | $0.05 | $1.50 |
| Kimi K2.7 Code | $0.06 | $1.80 |
| GLM-5.1 | $0.10 | $3.00 |
| GLM-5.2 | bundled | bundled |
| Qwen3.7 Max | $0.07 | $2.10 |

## Model-by-Model Analysis

### DeepSeek V4 (DeepSeek)

**Strengths:** Highest coding benchmark among all models globally (LiveCodeBench 93.5, Codeforces 3206). 1M context window. MIT-licensed open weights. Three reasoning modes: Non-Think, Think High, Think Max. Hybrid Attention (CSA+HCA) reduces long-context inference cost by 73% vs V3.2. Anthropic API compatibility. Cache-hit pricing at $0.003/$0.004 per M tokens — effectively free for repeated queries.

**Weaknesses:** BenchLM 87 now trails Qwen3.7 Max by 4 points. Legacy API aliases (`deepseek-chat`, `deepseek-reasoner`) retire July 24, 2026. Pro pricing is 3x Flash.

**Best for LLM Wiki:** Flash tier for high-volume extraction and summarization. Pro tier for complex classification and coding-heavy wiki maintenance scripts. Cache-hit pricing makes repeated index rebuilds nearly free.

### Qwen3.7 Max / Qwen3.5 (Alibaba)

**Strengths:** Qwen3.7 Max at BenchLM 91 is the strongest Chinese model ever tested, ranking #5 globally. Qwen3.5-27B dense model (not MoE) punches far above its weight — SWE-bench 72.4%, LiveCodeBench 80.7, competitive with models 5-10x larger. Gated DeltaNet architecture (linear attention at 16:1 ratio) is more efficient than pure transformers. Qwen3.7 Max ranks #7 on WebDev Arena (Elo 1537). 262K context for Qwen3.5 sizes.

**Weaknesses:** Qwen3.7 Max is not open-weight (closed). Qwen3.5-397B scores 78 — 13 points behind Qwen3.7 Max. Requires choosing from a large model family. No Qwen 4 announced yet.

**Best for LLM Wiki:** Qwen3.7 Max for frontier-quality bilingual generation via API. Qwen3.5-27B for cost-effective self-hosted deployment. Qwen3.7 Plus at $0.25/M for mid-tier quality. Small variants for real-time classification.

### Kimi K2.6 / K2.7 Code (Moonshot AI)

**K2.6 strengths:** BenchLM 84. Elite coding (LiveCodeBench 89.6, SWE-bench Pro 58.6 — best among Chinese models). Open weight (Modified MIT). Strong agentic coding: Agent Swarm scaled to 300 sub-agents and 4,000 coordinated steps. Multimodal (image + video via MoonViT). Kimi Code CLI, Kimi Claw, Kimi Work product ecosystem.

**K2.7 Code:** Released June 12, 2026 as a coding-specialized successor with the same 1T/32B MoE architecture as K2.6 and 256K context. Always runs in thinking mode; reduces thinking tokens by ~30% vs K2.6. Beats K2.6 on all six Moonshot coding/agentic benchmarks (Kimi Code Bench 62.0 vs 50.9, MCP Atlas 76.0 vs 69.4, MCP Mark Verified 81.1 vs 72.8) but still trails GPT-5.5 and Claude Opus 4.8 on most tests. Not ranked on BenchLM or LM Arena yet. No general-text or math scores published.

**Weaknesses:** 256–262K context (smaller than DeepSeek/MiMo 1M). Pricing higher than DeepSeek Flash or MiMo. K2.6 Agent Arena net improvement only 0.56% (lags GLM-5.1's 3.38%). K2.7 Code is coding-only; no MMLU/GPQA/AIME coverage.

**Best for LLM Wiki:** K2.6 for code-heavy wiki maintenance, transcript analysis, and processing technical content. K2.7 Code for coding-agent-specific tasks where it improves over K2.6; not suitable for general bilingual generation.

### GLM-5 / GLM-5.1 / GLM-5.2 (Z.AI / Zhipu AI)

**GLM-5.1 strengths:** Leads Chinese models on Agent Arena (#8, 3.38% net improvement) and WebDev Arena (Elo 1532). BenchLM 82. GLM-5 (Reasoning) BenchLM 83, excels at math/reasoning and cybersecurity (CyberGym 68.7). 8+ hours continuous autonomous work on a single task. MIT license. Supports vLLM, SGLang, KTransformers.

**GLM-5.2:** Released June 13, 2026 with a **1M-token context window** (5× GLM-5.1's 203K), High/Max thinking modes, and **131K max output**. Bundled in GLM Coding Plan tiers; open weights under MIT promised for the following week. As of launch, **no benchmark scores** have been published for coding, text, or math. The main verified improvement is context size; architecture and performance remain unverified by third parties. By June 14, it was already available in OpenCode via the Z.ai provider with early positive first impressions (see [[glm-5-2]]).

**Weaknesses:** GLM-5.1: 203K context (smallest among frontier tier), premium $3.08/M output pricing. GLM-5.2: no public benchmarks yet; standalone API pricing not available at launch.

**Best for LLM Wiki:** GLM-5.1 best for autonomous wiki maintenance agents. GLM-5 (Reasoning) for complex classification and knowledge graph construction. GLM-5.2 is promising for long-document wiki generation once benchmarks confirm quality; currently a context-size bet.

### Xiaomi MiMo-V2.5-Pro (Xiaomi)

**Strengths:** 1T params MoE with 42B active. 1M context. MIT license. Artificial Analysis score 54 at just $0.18/M — best price/performance in the frontier tier. Excels at long-horizon agentic tasks: built a full SysY compiler (233/233 tests, 672 tool calls, 4.3 hours) and a video editor (8,192 lines, 1,868 tool calls, 11.5 hours). Token-efficient: 40-60% fewer tokens than Claude Opus 4.6 on ClawEval. Integrated with OpenClaw, OpenCode, KiloCode.

**Weaknesses:** No BenchLM score yet. Community smaller than DeepSeek/Qwen. API ecosystem still maturing. WebDev Arena ranking unknown.

**Best for LLM Wiki:** The best budget frontier model for autonomous wiki maintenance. Multi-hour batch processing, cross-referencing, gap analysis. At $0.18/$0.36 per M tokens, it costs less than DeepSeek Flash for comparable quality.

### MiniMax-M3 (MiniMax)

**Strengths:** Artificial Analysis intelligence score 55 at just $0.22/M — cheapest frontier model available. WebDev Arena Elo 1528 (#9 globally). Rapid iteration cycle: M2.0 (Dec 2025) → M2.7 (Apr 2026) → M3 (June 2026). Active community (2.47M HuggingFace downloads for M2.7). MoE architecture.

**Weaknesses:** Newest entrant — limited benchmark data. No BenchLM score. BenchLM Text Arena rank #43. Smaller ecosystem than DeepSeek/Qwen/GLM. Limited third-party integrations.

**Best for LLM Wiki:** Budget alternative to DeepSeek V4 Flash for bulk extraction and summarization. Worth testing for cost-sensitive deployments where frontier quality is acceptable but not critical.

## Suitability for Karpathy's LLM Wiki

### Task-by-Task Model Recommendations

| Wiki Task | Primary Choice | Budget Choice | Quality Choice |
|-----------|---------------|---------------|----------------|
| URL content extraction | DeepSeek V4 Flash | MiniMax-M3 | DeepSeek V4 Pro |
| Article summarization | DeepSeek V4 Flash | MiMo-V2.5-Pro | Qwen3.7 Max |
| Bilingual (EN/RU) generation | GLM-5.1 | Qwen3.5-27B | Qwen3.7 Max |
| Content classification | Qwen3.5-27B | DeepSeek V4 Flash | GLM-5 (Reasoning) |
| YouTube transcript analysis | Kimi K2.6 | DeepSeek V4 Flash | Qwen3.7 Max |
| Reddit post processing | DeepSeek V4 Flash | MiniMax-M3 | Kimi K2.6 |
| Wiki index generation | DeepSeek V4 Flash | MiMo-V2.5-Pro | Qwen3.7 Max |
| Quality checking (RU section) | GLM-5.1 | Qwen3.5-27B | Qwen3.7 Max |
| Autonomous batch agent | GLM-5.1 | MiMo-V2.5-Pro | Kimi K2.6 |
| Knowledge graph construction | GLM-5 (Reasoning) | Qwen3.5-27B | DeepSeek V4 Pro |

### Recommended Architecture for LLM Wiki

For a Karpathy-style three-layer wiki system:

1. **Extraction layer (Layer 1 → Layer 2):** DeepSeek V4 Flash for 90% of content processing. At $0.14/$0.28 per M tokens (or $0.10/$0.20 via OpenRouter), it handles URL fetching, article extraction, and initial classification. Cache-hit pricing at $0.003/M makes repeated operations nearly free. For a wiki processing 50-100 sources/day, this costs under $0.20/month.

2. **Distillation layer (wiki entry generation):** Qwen3.7 Max for frontier-quality bilingual generation (BenchLM 91). GLM-5.1 as fallback for autonomous generation tasks (8+ hours continuous work). For budget deployments, Qwen3.5-27B self-hosted.

3. **Autonomous maintenance layer:** MiMo-V2.5-Pro for long-running wiki maintenance agents at $0.18/$0.36 per M tokens — best price/performance. GLM-5.1 as alternative when Agent Arena performance matters (rank #8 globally).

4. **Budget/overflow:** MiniMax-M3 for bulk processing at $0.22/M. Qwen3.5-27B for self-hosted deployment when API costs must be zero.

## Notable Quotes

> "Qwen3.7 Max at BenchLM 91 is the strongest Chinese model ever — for the first time, a Chinese model enters the global top 5." — BenchLM, June 2026

> "V4-Flash at $0.28/M output is roughly 90-100x cheaper than GPT-5.5. Whether the quality tradeoff is acceptable for your specific workload is the variable." — Verdent AI

> "MiMo-V2.5-Pro at $0.18/$0.36 delivers frontier-tier intelligence at prices that make 24/7 autonomous agents economically viable." — Artificial Analysis

## Related Entries
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 Pro vs Claude Opus 4.7 vs Kimi K2.6 Benchmark](../models/deepseek-v4-vs-opus-kimi.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1: Side-by-Side Coding Comparison](../models/gpt-vs-glm-5-1-comparison.md))
- [[minimax-m3-coding-model]] ([MiniMax M3 Coding Model](../models/minimax-m3-coding-model.md))
- [[glm-5-2]] ([GLM-5.2: Z.AI's 1M-Context Coding Model](../models/glm-5-2.md))
- [[kimi-k2-7-code]] ([Kimi K2.7 Code: Moonshot's Coding-Optimized K2.6 Successor](../models/kimi-k2-7-code.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[mimo-v25-pro-dflash-1000tps]] ([Xiaomi Serves MiMo V2.5 Pro at 1000-3000 tok/s with DFlash + Persistent Kernel](../news/mimo-v25-pro-dflash-1000tps.md))
- [[huawei-deepseek-v4-ascend-training]] ([Huawei Post-Trains DeepSeek V4 on Domestic Chips](../news/huawei-deepseek-v4-ascend-training.md))

---
<!-- RU -->

## Краткое описание

Сравнение китайских передовых LLM-моделей для создания базы знаний в стиле LLM Wiki Карпати — охватывает DeepSeek V4, Kimi K2.6/K2.7 Code, GLM-5/5.1/5.2, Qwen 3.5/3.7, Xiaomi MiMo-V2.5 и MiniMax-M3. Включает оценки BenchLM, рейтинги LM Arena, индексы интеллекта Artificial Analysis, цены API, размеры контекстного окна и применимость для извлечения знаний, двуязычного реферирования и агентных вики-воркфлоу. Обновлено в июне 2026: Qwen3.7 Max, MiniMax-M3, GLM-5.2 (контекст 1M) и Kimi K2.7 Code.

## Ключевые идеи

- **Qwen3.7 Max** — новый лидер китайского фронтира с оценкой BenchLM 91, занимая 5-е место в мире — скачок на 12 очков по сравнению с Qwen3.5
- DeepSeek V4 Pro (Max) лидирует в кодинговых бенчмарках (LiveCodeBench 93.5) при оценке BenchLM 87, но теперь лишь второй среди китайских моделей
- MiniMax-M3 выходит на фронтир-уровень с оценкой Artificial Analysis 55 по цене всего $0.22/М токенов — самый дешёвый вариант фронтира
- **GLM-5.2** выпущена 13 июня 2026 года с **контекстом 1M токенов** и режимами рассуждения High/Max; открытые веса обещаны по MIT, но бенчмарки ещё не опубликованы
- **Kimi K2.7 Code** выпущена 12 июня 2026 года и превосходит K2.6 по всем шести кодинговым/агентным бенчмаркам Moonshot, но всё ещё отстаёт от GPT-5.5 и Claude Opus 4.8
- Все ведущие китайские модели остаются с открытыми весами (MIT/Apache) — структурное преимущество перед западными проприетарными API
- Для задач LLM Wiki ценовой ландшафт изменился: MiMo-V2.5-Pro за $0.18/М и MiniMax-M3 за $0.22/М предлагают качество фронтира по бюджетным ценам
- Qwen3.5-27B (плотная модель, не MoE) — лучший выбор по эффективности, конкурентоспособна с моделями в 5-10 раз большего размера

## Сравнение бенчмарков

### Общие оценки (BenchLM, июнь 2026)

| Место | Модель | Создатель | Оценка | Открытые веса | Контекст |
|-------|--------|-----------|--------|---------------|----------|
| 1 | Qwen3.7 Max | Alibaba | 91 | Нет | 1M |
| 2 | DeepSeek V4 Pro (Max) | DeepSeek | 87 | Да (MIT) | 1M |
| 3 | Kimi K2.6 | Moonshot AI | 84 | Да (Mod. MIT) | 262K |
| 4 | GLM-5 (Reasoning) | Z.AI | 83 | Да (MIT) | 200K |
| 5 | GLM-5.1 | Z.AI | 82 | Да (MIT) | 203K |
| 6 | DeepSeek V4 Pro (High) | DeepSeek | 83 | Да (MIT) | 1M |
| 7 | Qwen3.5 397B (Reasoning) | Alibaba | 78 | Да | 128K |
| 8 | Kimi K2.5 (Reasoning) | Moonshot AI | 77 | Нет | 128K |
| 9 | DeepSeek V4 Flash (Max) | DeepSeek | 77 | Да (MIT) | 1M |
| 10 | Qwen3.5-27B | Alibaba | 75 | Да | 262K |
| 11 | GLM-5.2 | Z.AI | N/A | Да (MIT, в ожидании) | 1M |
| 12 | Kimi K2.7 Code | Moonshot AI | Unranked | Да (Mod. MIT) | 256K |

### Индекс интеллекта Artificial Analysis (июнь 2026)

| Модель | Интеллект (0-100) | Цена $/М вх. | Скорость tok/s |
|--------|-------------------|-------------|---------------|
| Qwen3.7 Max | 57 | $1.43 | 106 |
| MiniMax-M3 | 55 | $0.22 | 40 |
| Kimi K2.6 | 54 | $0.70 | 44 |
| MiMo-V2.5-Pro | 54 | $0.18 | 44 |
| DeepSeek V4 Pro (Max) | 52 | $0.44 | 53 |
| GLM-5.1 | 51 | $0.90 | 63 |
| DeepSeek V4 Pro (High) | 50 | $0.18 | 47 |
| MiniMax-M2.7 | 50 | $0.22 | 78 |

### Рейтинг LM Arena (июнь 2026)

| Модель | Text Arena | Agent Arena | WebDev Arena |
|--------|-----------|-------------|-------------|
| GLM-5.1 | #14 | #8 (3.38%) | #8 (Elo 1532) |
| Qwen3.7 Max | #17 | — | #7 (Elo 1537) |
| MiMo-V2.5-Pro | #29 | — | — |
| Kimi K2.6 | #30 | #11 (0.56%) | — |
| DeepSeek V4 Pro (Think) | #34 | #12 (1.88%) | — |
| MiniMax-M3 | #43 | — | #9 (Elo 1528) |

### Глобальный контекст (vs западный фронтир)

| Модель | Оценка BenchLM |
|--------|---------------|
| Claude Mythos Preview | 99 |
| Claude Opus 4.8 | 95 |
| Gemini 3.1 Pro | 92 |
| GPT-5.5 | 91 |
| **Qwen3.7 Max** | **91** |
| GPT-5.4 Pro | 91 |
| Claude Opus 4.6 | 87 |
| **DeepSeek V4 Pro (Max)** | **87** |
| **Kimi K2.6** | **84** |
| **GLM-5.1** | **82** |
| **Qwen3.5 397B** | **78** |

## Сравнение цен API

| Модель | Ввод ($/М токенов) | Вывод ($/М токенов) | Контекст |
|--------|--------------------|--------------------|----------|
| **MiMo-V2.5-Pro** | $0.18 | $0.36 | 1M |
| **DeepSeek V4 Flash** | $0.14 | $0.28 | 1M |
| **MiniMax-M3** | $0.22 | $0.22 | — |
| **DeepSeek V4 Pro** | $0.435 | $0.87 | 1M |
| **Kimi K2.6** | $0.68 | $3.42 | 262K |
| **Kimi K2.7 Code** | $0.95 / $0.19 (cache hit) | $4.00 | 262K |
| **GLM-5.1** | $0.98 | $3.08 | 203K |
| **GLM-5.2** | Bundled in Coding Plan | Bundled in Coding Plan | 1M |
| **Qwen3.7 Max** | $1.43 | — | — |

### Детали ценообразования

- **DeepSeek V4** использует агрессивное cache-hit ценообразование: $0.003/М на ввод и $0.004/М на вывод, что делает повторные запросы почти бесплатными.
- **Kimi K2.7 Code** на Kimi Platform: cache-hit ввод $0.19/М; OpenRouter предлагает фlat-рейт $0.75/$3.50.
- **GLM-5.2** на старте только по подписке; отдельной цены за токены нет. Lite-тариф GLM Coding Plan начинается примерно с $18/месяц за ~400 промптов/неделю.
- **Qwen3.7 Max** и **Qwen3.7 Plus** работают через Alibaba Cloud/DashScope; Plus — $0.25/М ввод, Max — $1.43/М ввод. Цены на вывод публично не указаны.

### Стоимость типичной нагрузки LLM Wiki

При обработке 50 статей/день, ~4K входных + ~2K выходных токенов каждая:

| Модель | Стоимость/день | Стоимость/месяц |
|--------|---------------|-----------------|
| MiMo-V2.5-Pro | $0.008 | $0.24 |
| DeepSeek V4 Flash | $0.006 | $0.18 |
| MiniMax-M3 | $0.009 | $0.27 |
| Qwen3.5-27B | $0.001 | $0.03 |
| DeepSeek V4 Pro | $0.04 | $1.20 |
| Kimi K2.6 | $0.05 | $1.50 |
| Kimi K2.7 Code | $0.06 | $1.80 |
| GLM-5.1 | $0.10 | $3.00 |
| GLM-5.2 | bundled | bundled |
| Qwen3.7 Max | $0.07 | $2.10 |

## Анализ по моделям

### DeepSeek V4 (DeepSeek)

**Сильные стороны:** Наивысший кодинговый бенчмарк среди всех моделей мира (LiveCodeBench 93.5, Codeforces 3206). Контекст 1M. Открытые веса MIT. Три режима рассуждений: без размышлений, Think High, Think Max. Гибридное внимание снижает стоимость на 73%. Совместимость с API Anthropic. Цены с попаданием в кэш $0.003/$0.004 за М токенов — фактически бесплатно.

**Слабые стороны:** BenchLM 87 теперь отстаёт от Qwen3.7 Max на 4 очка. Устаревшие API-алиасы отключаются 24 июля 2026. Pro в 3 раза дороже Flash.

**Лучше всего для LLM Wiki:** Уровень Flash для высокоинтенсивного извлечения и реферирования. Уровень Pro для сложной классификации и обслуживания вики-скриптов. Кэширование делает повторные перестроения индекса почти бесплатными.

### Qwen3.7 Max / Qwen3.5 (Alibaba)

**Сильные стороны:** Qwen3.7 Max с BenchLM 91 — сильнейшая китайская модель, 5-е место в мире. Qwen3.5-27B (плотная модель) превосходит ожидания — SWE-bench 72.4%, конкурентоспособна с моделями в 5-10 раз больше. Архитектура Gated DeltaNet эффективнее чистых трансформеров. WebDev Arena Elo 1537 (#7). 262K контекст для вариантов Qwen3.5.

**Слабые стороны:** Qwen3.7 Max не имеет открытых весов. Qwen3.5-397B набирает 78 — на 13 очков меньше Qwen3.7 Max. Qwen 4 ещё не анонсирована.

**Лучше всего для LLM Wiki:** Qwen3.7 Max для генерации качества фронтира через API. Qwen3.5-27B для экономичного самохостинга. Qwen3.7 Plus за $0.25/М для среднего уровня.

### Kimi K2.6 / K2.7 Code (Moonshot AI)

**K2.6:** BenchLM 84. Элитный кодинг (LiveCodeBench 89.6, SWE-bench Pro 58.6 — лучший среди китайских моделей). Открытые веса. Agent Swarm: 300 подагентов и 4,000 координированных шагов. Мультимодальность. Экосистема Kimi Code CLI, Kimi Claw, Kimi Work.

**K2.7 Code:** Выпущена 12 июня 2026 года как специализированная для кодинга преемница с той же архитектурой MoE 1T/32B и контекстом 256K. Всегда работает в режиме рассуждений; на ~30% меньше thinking-токенов, чем у K2.6. Превосходит K2.6 по всем шести кодинговым/агентным бенчмаркам Moonshot (Kimi Code Bench 62.0 vs 50.9, MCP Atlas 76.0 vs 69.4, MCP Mark Verified 81.1 vs 72.8), но всё ещё отстаёт от GPT-5.5 и Claude Opus 4.8. Пока не ранжирована на BenchLM и LM Arena. Оценки MMLU/GPQA/AIME не опубликованы.

**Слабые стороны:** Контекст 256–262K (меньше, чем 1M у DeepSeek/MiMo). K2.6: Agent Arena лишь 0.56%. K2.7 Code — только кодинг, не универсальная модель.

**Лучше всего для LLM Wiki:** K2.6 для обслуживания вики с упором на код, анализа транскриптов YouTube и обработки технического контента. K2.7 Code для специфических кодинговых агентских задач; не подходит для общей двуязычной генерации.

### GLM-5 / GLM-5.1 / GLM-5.2 (Z.AI / Zhipu AI)

**GLM-5.1:** Лидирует среди китайских моделей в Agent Arena (#8, 3.38%) и WebDev Arena (Elo 1532). BenchLM 82. GLM-5 (Reasoning) BenchLM 83, силён в математике и кибербезопасности (CyberGym 68.7). 8+ часов автономной работы. Лицензия MIT.

**GLM-5.2:** Выпущена 13 июня 2026 года с **контекстом 1M токенов** (в 5 раз больше, чем у GLM-5.1), режимами рассуждения High/Max и **максимальным выводом 131K**. Входит в GLM Coding Plan; открытые веса по MIT обещаны на следующей неделе. На момент запуска **не опубликованы оценки бенчмарков** по кодингу, тексту и математике. Главное подтверждённое улучшение — размер контекста; архитектура и производительность пока не проверены третьими сторонами. К 14 июня модель уже была доступна в OpenCode через провайдера Z.ai с положительными первыми впечатлениями сообщества (см. [[glm-5-2]]).

**Слабые стороны:** GLM-5.1: контекст 203K (наименьший среди фронтира), премиальный вывод $3.08/М. GLM-5.2: нет публичных бенчмарков; отдельное API-ценообразование пока недоступно.

**Лучше всего для LLM Wiki:** GLM-5.1 — лучший выбор для автономных агентов обслуживания вики. GLM-5 (Reasoning) для классификации и графов знаний. GLM-5.2 перспективна для генерации длинных документов вики, как только бенчмарки подтвердят качество; сейчас это ставка на размер контекста.

### Xiaomi MiMo-V2.5-Pro (Xiaomi)

**Сильные стороны:** MoE 1T с 42B активных. Контекст 1M. MIT. Artificial Analysis 54 при $0.18/М — лучшая цена/производительность во фронтире. Превосходит в агентных задачах: построение компилятора (672 вызова, 4.3 часа) и видеоредактора (1,868 вызовов, 11.5 часов). На 40-60% меньше токенов, чем Claude Opus 4.6.

**Слабые стороны:** Нет оценки BenchLM. Сообщество меньше, чем у DeepSeek/Qwen. Экосистема API формируется.

**Лучше всего для LLM Wiki:** Лучший бюджетный фронтир для автономного обслуживания вики. Многочасовая пакетная обработка, перекрёстные ссылки, анализ пробелов. При $0.18/$0.36 за М токенов дешевле DeepSeek Flash при сопоставимом качестве.

### MiniMax-M3 (MiniMax)

**Сильные стороны:** Artificial Analysis 55 при $0.22/М — самый дешёвый фронтир. WebDev Arena Elo 1528 (#9). Быстрый цикл итераций: M2.0 (декабрь 2025) → M2.7 (апрель 2026) → M3 (июнь 2026). Активное сообщество (2.47M загрузок M2.7 на HuggingFace).

**Слабые стороны:** Новейший участник — ограниченные данные бенчмарков. Нет оценки BenchLM. Text Arena #43. Меньшая экосистема.

**Лучше всего для LLM Wiki:** Бюджетная альтернатива DeepSeek V4 Flash для массового извлечения и реферирования. Стоит протестировать для экономичных развёртываний.

## Применимость для LLM Wiki Карпати

### Рекомендации по задачам

| Задача вики | Основной выбор | Бюджетный выбор | Выбор качества |
|-------------|---------------|-----------------|----------------|
| Извлечение контента из URL | DeepSeek V4 Flash | MiniMax-M3 | DeepSeek V4 Pro |
| Реферирование статей | DeepSeek V4 Flash | MiMo-V2.5-Pro | Qwen3.7 Max |
| Двуязычная генерация (EN/RU) | GLM-5.1 | Qwen3.5-27B | Qwen3.7 Max |
| Классификация контента | Qwen3.5-27B | DeepSeek V4 Flash | GLM-5 (Reasoning) |
| Анализ транскриптов YouTube | Kimi K2.6 | DeepSeek V4 Flash | Qwen3.7 Max |
| Обработка постов Reddit | DeepSeek V4 Flash | MiniMax-M3 | Kimi K2.6 |
| Генерация индекса вики | DeepSeek V4 Flash | MiMo-V2.5-Pro | Qwen3.7 Max |
| Проверка качества (RU раздел) | GLM-5.1 | Qwen3.5-27B | Qwen3.7 Max |
| Автономный пакетный агент | GLM-5.1 | MiMo-V2.5-Pro | Kimi K2.6 |
| Построение графа знаний | GLM-5 (Reasoning) | Qwen3.5-27B | DeepSeek V4 Pro |

### Рекомендуемая архитектура для LLM Wiki

Для трёхуровневой вики-системы в стиле Карпати:

1. **Уровень извлечения (Слой 1 → Слой 2):** DeepSeek V4 Flash для 90% обработки. При $0.14/$0.28 за М токенов (или $0.10/$0.20 через OpenRouter). Кэширование $0.003/М делает повторные операции почти бесплатными. Для 50-100 источников/день — менее $0.20/месяц.

2. **Уровень дистилляции (генерация статей):** Qwen3.7 Max для генерации качества фронтира (BenchLM 91). GLM-5.1 как резерв для автономной генерации (8+ часов непрерывной работы). Для бюджетных развёртываний — самохостинг Qwen3.5-27B.

3. **Уровень автономного обслуживания:** MiMo-V2.5-Pro для длительных агентов при $0.18/$0.36 за М токенов — лучшая цена/производительность. GLM-5.1 как альтернатива, когда важна производительность Agent Arena (#8 в мире).

4. **Резерв/переполнение:** MiniMax-M3 для массовой обработки при $0.22/М. Qwen3.5-27B для самохостинга с нулевыми затратами на API.

## Примечательные цитаты

> «Qwen3.7 Max с оценкой BenchLM 91 — сильнейшая китайская модель. Впервые китайская модель входит в глобальную пятёрку.» — BenchLM, июнь 2026

> «MiMo-V2.5-Pro за $0.18/$0.36 обеспечивает интеллект уровня фронтира по ценам, делающим 24/7 автономных агентов экономически целесообразными.» — Artificial Analysis

## Связанные записи
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 Pro vs Claude Opus 4.7 vs Kimi K2.6 Benchmark](../models/deepseek-v4-vs-opus-kimi.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1: Side-by-Side Coding Comparison](../models/gpt-vs-glm-5-1-comparison.md))
- [[minimax-m3-coding-model]] ([MiniMax M3 Coding Model](../models/minimax-m3-coding-model.md))
- [[glm-5-2]] ([GLM-5.2: Z.AI's 1M-Context Coding Model](../models/glm-5-2.md))
- [[kimi-k2-7-code]] ([Kimi K2.7 Code: Moonshot's Coding-Optimized K2.6 Successor](../models/kimi-k2-7-code.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[mimo-v25-pro-dflash-1000tps]] ([Xiaomi обслуживает MiMo V2.5 Pro со скоростью 1000-3000 ток/с с DFlash и Persistent Kernel](../news/mimo-v25-pro-dflash-1000tps.md))
- [[huawei-deepseek-v4-ascend-training]] ([Huawei дообучила DeepSeek V4 на отечественных чипах](../news/huawei-deepseek-v4-ascend-training.md))
