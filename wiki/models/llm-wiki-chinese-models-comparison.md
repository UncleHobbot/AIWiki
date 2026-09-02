---
title: "Chinese LLM Models for Building Karpathy's LLM Wiki: DeepSeek, Kimi, GLM, Qwen, MiMo, MiniMax"
title_ru: "Китайские LLM-модели для создания LLM Wiki Карпати: DeepSeek, Kimi, GLM, Qwen, MiMo, MiniMax"
category: models
tags: [deepseek, kimi, glm, qwen, mimo, minimax, chinese-llm, benchmarks, llm-wiki, karpathy, lmarena, pricing]
date: 2026-05-16
updated: 2026-06-29
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
  - https://huggingface.co/blog/zai-org/glm-52-blog
  - https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost
  - https://www.reddit.com/r/DeepSeek/comments/1uio6yf/deepseek_v4_official_launch_peakoffpeak_pricing/
  - https://www.reddit.com/r/DeepSeek/comments/1uiq1lk/v4_peak_pricing_is_coming_midjuly_heres_how_to/
  - https://platform.minimax.io/docs/guides/pricing-paygo
---

## Summary

Comparison of Chinese frontier LLMs evaluated for building Karpathy-style LLM Wiki knowledge bases — covering DeepSeek V4, Kimi K2.6/K2.7 Code, GLM-5/5.1/5.2, Qwen 3.5/3.7, Xiaomi MiMo-V2.5, and MiniMax-M3. Includes BenchLM scores, LM Arena rankings, Artificial Analysis intelligence indices, API pricing, context windows, and suitability for knowledge extraction, bilingual summarization, and agentic wiki workflows. Updated June 29, 2026: GLM-5.2 full benchmarks published (beats GPT-5.5 on long-horizon coding), DeepSeek V4 peak/valley pricing announced (2× during peak hours, official launch mid-July), and corrected pricing across providers.

## Key Ideas

- **Qwen3.7 Max** is the new Chinese frontier leader at BenchLM 91, ranking #5 globally — a massive 12-point jump over Qwen3.5
- DeepSeek V4 Pro (Max) leads on coding benchmarks (LiveCodeBench 93.5) at BenchLM 87, but is now #2 Chinese model
- MiniMax-M3 enters the frontier tier at Artificial Analysis score 55, priced at just $0.22/M tokens — the cheapest frontier option
- **GLM-5.2** launched June 13, 2026 (753B params) with a **1M-token context window**. Full benchmarks published June 17: it **beats GPT-5.5** on SWE-bench Pro (62.1 vs 58.6), FrontierSWE (74.4 vs 72.6), PostTrainBench, and HLE-w-tools — the **strongest open-source model** globally, ranking #2 on long-horizon tasks behind only Claude Opus 4.8. MIT-licensed, no regional limits
- **DeepSeek V4** official launch mid-July 2026 with new **peak/valley (time-of-day) pricing**: peak hours cost **2× the regular rate** (peak = UTC 01:00–04:00 & 06:00–10:00). DSpark speculative decoding now live for faster inference
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
| 11 | GLM-5.2 | Z.AI | N/A (BenchLM) | Yes (MIT) | 1M |
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
| Qwen3.7 Max | 91.6 | 80.4% | 60.6 | — |
| DeepSeek V4 Flash (Max) | 91.6 | 79.0% | — | — |
| **GLM-5.2** | — | — | **62.1** | — |
| Kimi K2.6 | 89.6 | 80.2% | **58.6%** | — |
| GLM-5.1 | — | — | 58.4% | — |
| Qwen3.5-27B | 80.7 | 72.4% | — | — |
| MiMo-V2.5-Pro | — | 78.9% | — | — |

### Long-Horizon Coding Benchmarks (Z.AI, June 2026)

These benchmarks measure multi-hour autonomous engineering tasks — increasingly relevant for agentic wiki maintenance.

| Benchmark | GLM-5.2 | GLM-5.1 | DeepSeek V4 Pro | Qwen3.7 Max | GPT-5.5 | Opus 4.8 |
|-----------|---------|---------|-----------------|-------------|---------|----------|
| FrontierSWE (Dominance) | **74.4** | 30.5 | 29.0 | — | 72.6 | **75.1** |
| PostTrainBench | **34.3** | 20.1 | — | — | 28.4 | **37.2** |
| SWE-Marathon | 13.0 | 1.0 | — | — | 12.0 | **26.0** |
| Terminal-Bench 2.1 | **81.0** | 63.5 | 64 | 75 | 84 | **85** |
| MCP-Atlas | **76.8** | 71.8 | 73.6 | 76.4 | 75.3 | **77.8** |
| ProgramBench | **63.7** | 50.9 | 47.8 | — | 70.8 | **71.9** |
| HLE (w/ Tools) | **54.7** | 52.3 | 48.2 | 53.5 | 52.2 | **57.9** |

> GLM-5.2 is the highest-ranked open-source model on every long-horizon benchmark, beating GPT-5.5 on most. It ranks #2 globally behind only Claude Opus 4.8.

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
| **MiMo-V2.5-Pro** (≤256K) | $1.00 | $3.00 | 1M | Standard | Yes |
| **MiMo-V2.5 Flash** | $0.10 | $0.30 | 1M | Standard | Yes |
| **DeepSeek V4 Flash** | $0.14 (miss) / $0.003 (hit) | $0.28 | 1M | 384K | Yes ($0.10/$0.20) |
| **DeepSeek V4 Pro** | $0.435 (miss) / $0.004 (hit) | $0.87 | 1M | 384K | Yes |
| **MiniMax-M3** | $0.30 | $1.20 | — | Standard | Yes |
| **MiniMax-M2.7** | $0.22 | $0.22 | — | Standard | Yes |
| **Qwen3.7 Plus** | $0.40 | $1.60 | 1M | Standard | Yes |
| **Kimi K2.6** | $0.95 | $4.00 | 262K | Standard | Yes |
| **Kimi K2.7 Code** | $0.95 / $0.19 (cache hit) | $4.00 | 262K | Standard | Yes |
| **GLM-5.1** | $0.98 | $3.08 | 203K | 64K | Yes |
| **GLM-5.2** | $1.40 / $0.26 (cache hit) | $4.40 | 1M | 131K | Yes |
| **Qwen3.7 Max** | $1.25 (OpenRouter) / $2.50 (Alibaba) | $3.75 (OR) / $7.50 (Alibaba) | 1M | — | Yes |
| **Qwen3.5-27B** | ~$0.02 | ~$0.06 | 262K | Standard | — |

> **Pricing note:** Prices vary significantly by provider (OpenRouter vs direct API vs Alibaba Cloud/DashScope). The VentureBeat June 2026 snapshot and OpenRouter listings were used where available; prior figures from earlier sources may differ.

### Official Provider Pricing (First-Party APIs)

Prices from each model creator's **own API platform** (not resellers like OpenRouter). DeepSeek prices are regular (off-peak); peak hours will cost 2× starting mid-July 2026.

| Model | Official Provider | Input $/M (cache miss) | Input $/M (cache hit) | Output $/M | Context | Max Output |
|-------|-------------------|------------------------|-----------------------|------------|---------|------------|
| DeepSeek V4 Flash | api.deepseek.com | $0.14 | $0.0028 | $0.28 | 1M | 384K |
| DeepSeek V4 Pro | api.deepseek.com | $0.435 | $0.003625 | $0.87 | 1M | 384K |
| GLM-5.1 | Z.AI API (z.ai) | $1.40 | — | $4.40 | 203K | 64K |
| GLM-5.2 | Z.AI API (z.ai) | $1.40 | $0.26 | $4.40 | 1M | 131K |
| Qwen3.7 Plus | Alibaba DashScope | $0.40 | — | $1.60 | 1M | Standard |
| Qwen3.7 Max | Alibaba DashScope | $2.50 | — | $7.50 | 1M | Standard |
| Kimi K2.6 | Moonshot Platform | $0.95 | — | $4.00 | 262K | Standard |
| Kimi K2.7 Code | Moonshot Platform | $0.95 | $0.19 | $4.00 | 262K | Standard |
| MiMo-V2.5 Flash | Xiaomi Platform | $0.10 | — | $0.30 | 1M | Standard |
| MiMo-V2.5 Pro (≤256K) | Xiaomi Platform | $1.00 | — | $3.00 | 1M | Standard |
| MiniMax-M3 (≤512K) | platform.minimax.io | $0.30 | $0.06 | $1.20 | — | Standard |

> GLM-5.2 matches GLM-5.1's official Z.AI rates ($1.40/$4.40). OpenRouter resells GLM-5.1 at a lower $0.98/$3.08 — the discount varies by reseller. DeepSeek's cache-hit pricing ($0.0028–$0.0036/M) is the most aggressive in the industry, making repeated context-heavy queries nearly free.

### Detailed Pricing Notes

- **DeepSeek V4** uses aggressive cache-hit pricing: $0.003/M input and $0.004/M output, making repeated queries nearly free.
- **DeepSeek V4 peak/valley pricing** (announced June 26, effective mid-July): peak hours cost **2× the regular rate**. Peak = UTC 01:00–04:00 and 06:00–10:00 (Beijing 09:00–12:00, 14:00–18:00). V4-Flash: 0.02/1.00/2.00 RMB → 0.04 RMB peak. V4-Pro output at peak: RMB 12/M. 2× applies to all token billing. This signals LLM APIs becoming a schedulable, electricity-grid-style compute market.
- **Kimi K2.7 Code** cache-hit input on Kimi Platform is $0.19/M; OpenRouter flat rate is $0.75/$3.50.
- **GLM-5.2** API: $1.40/M input, $4.40/M output (matching GLM-5.1 rates); cached input $0.26/M. Also available via GLM Coding Plan tiers (annual billing): Lite $12.60/mo, Pro $50.40/mo, Max $112.00/mo. Quota consumption: 3× peak (14:00–18:00 Beijing), 2× off-peak; limited-time promo: off-peak billed at 1× through end of September.
- **Qwen3.7 Max** and **Qwen3.7 Plus** use Alibaba Cloud/DashScope; Plus is $0.40/M input, $1.60/M output and includes vision. Max is $2.50/$7.50 on Alibaba direct or $1.25/$3.75 via OpenRouter. Open weights still not released as of June 29.

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

**Strengths:** Highest coding benchmark among all models globally (LiveCodeBench 93.5, Codeforces 3206). 1M context window. MIT-licensed open weights. Three reasoning modes: Non-Think, Think High, Think Max. Hybrid Attention (CSA+HCA) reduces long-context inference cost by 73% vs V3.2. DSpark speculative decoding now live for faster inference. Cache-hit pricing at $0.003/$0.004 per M tokens — effectively free for repeated queries.

**Weaknesses:** BenchLM 87 now trails Qwen3.7 Max by 4 points. **Peak/valley pricing** (mid-July): peak hours cost 2× — teams in certain time zones will feel this disproportionately. Legacy API aliases (`deepseek-chat`, `deepseek-reasoner`) retire July 24, 2026. Pro pricing is 3× Flash.

**Best for LLM Wiki:** Flash tier for high-volume extraction and summarization. Pro tier for complex classification and coding-heavy wiki maintenance scripts. Cache-hit pricing makes repeated index rebuilds nearly free.

### Qwen3.7 Max / Qwen3.5 (Alibaba)

**Strengths:** Qwen3.7 Max at BenchLM 91 is the strongest Chinese model ever tested, ranking #5 globally. Artificial Analysis score **56.6** (4.8 points above Qwen3.6 Max Preview). Full benchmark scores now available: HLE 41.4, HLE-w-tools 53.5, AIME 2026 97, GPQA-Diamond 90, SWE-bench Pro 60.6, Terminal-Bench 2.1 75, MCP-Atlas 76.4. Qwen3.5-27B dense model (not MoE) punches far above its weight — SWE-bench 72.4%, LiveCodeBench 80.7, competitive with models 5-10x larger. Gated DeltaNet architecture (linear attention at 16:1 ratio) is more efficient than pure transformers. Qwen3.7 Max ranks #7 on WebDev Arena (Elo 1537). 262K context for Qwen3.5 sizes.

**Weaknesses:** Qwen3.7 Max is **not open-weight** (closed) — community actively requesting open weights as of June 29. Qwen3.5-397B scores 78 — 13 points behind Qwen3.7 Max. Requires choosing from a large model family. No Qwen 4 announced yet.

**Best for LLM Wiki:** Qwen3.7 Max for frontier-quality bilingual generation via API. Qwen3.5-27B for cost-effective self-hosted deployment. Qwen3.7 Plus at $0.40/$1.60 with vision for mid-tier quality and multimodal tasks. Small variants for real-time classification.

### Kimi K2.6 / K2.7 Code (Moonshot AI)

**K2.6 strengths:** BenchLM 84. Elite coding (LiveCodeBench 89.6, SWE-bench Pro 58.6 — best among Chinese models). Open weight (Modified MIT). Strong agentic coding: Agent Swarm scaled to 300 sub-agents and 4,000 coordinated steps. Multimodal (image + video via MoonViT). Kimi Code CLI, Kimi Claw, Kimi Work product ecosystem.

**K2.7 Code:** Released June 12, 2026 as a coding-specialized successor with the same 1T/32B MoE architecture as K2.6 and 256K context. Always runs in thinking mode; reduces thinking tokens by ~30% vs K2.6. Beats K2.6 on all six Moonshot coding/agentic benchmarks (Kimi Code Bench 62.0 vs 50.9, MCP Atlas 76.0 vs 69.4, MCP Mark Verified 81.1 vs 72.8) but still trails GPT-5.5 and Claude Opus 4.8 on most tests. Not ranked on BenchLM or LM Arena yet. No general-text or math scores published.

**Weaknesses:** 256–262K context (smaller than DeepSeek/MiMo 1M). Pricing higher than DeepSeek Flash or MiMo. K2.6 Agent Arena net improvement only 0.56% (lags GLM-5.1's 3.38%). K2.7 Code is coding-only; no MMLU/GPQA/AIME coverage.

**Best for LLM Wiki:** K2.6 for code-heavy wiki maintenance, transcript analysis, and processing technical content. K2.7 Code for coding-agent-specific tasks where it improves over K2.6; not suitable for general bilingual generation.

### GLM-5 / GLM-5.1 / GLM-5.2 (Z.AI / Zhipu AI)

**GLM-5.1 strengths:** Leads Chinese models on Agent Arena (#8, 3.38% net improvement) and WebDev Arena (Elo 1532). BenchLM 82. GLM-5 (Reasoning) BenchLM 83, excels at math/reasoning and cybersecurity (CyberGym 68.7). 8+ hours continuous autonomous work on a single task. MIT license. Supports vLLM, SGLang, KTransformers.

**GLM-5.2:** Released June 13, 2026 — a **753B-parameter** flagship engineered for long-horizon autonomous coding, with a **solid 1M-token context** that stably sustains multi-hour engineering trajectories. **Full benchmarks published June 17** (via Z.AI HuggingFace blog): it is the **strongest open-source model** globally and **beats GPT-5.5** on most long-horizon coding tasks — SWE-bench Pro 62.1 (vs GPT-5.5 58.6), FrontierSWE Dominance 74.4 (vs 72.6), Terminal-Bench 2.1 81.0 (vs 84), PostTrainBench 34.3 (vs 28.4), HLE-w-tools 54.7 (vs 52.2), MCP-Atlas 76.8 (vs 75.3). It ranks **#2 globally** on long-horizon tasks, behind only Claude Opus 4.8. Also won **Design Arena** (#1, ELO 1360), beating Claude Fable 5.

**Architecture:** IndexShare (reuses one indexer across every 4 sparse-attention layers → **2.9× fewer FLOPs** at 1M context); improved MTP speculative decoding (+20% acceptance length via IndexShare + KVShare + rejection sampling + end-to-end TV loss); `slime` agentic-RL framework; critic-based PPO for long-horizon tasks; anti-hack module that blocks reward-hacking tool calls (e.g., `curl`-ing eval artifacts) during RL training. Flexible effort modes: **High** (balances performance/latency, ~halves token output) and **Max** (peak intelligence, ~85k output tokens/task).

**Pricing:** API $1.40/M input, $4.40/M output, cached input $0.26/M. GLM Coding Plan tiers (annual): Lite $12.60/mo, Pro $50.40/mo, Max $112.00/mo. Quota: 3× peak, 2× off-peak; promo: off-peak 1× through September. MIT license — **no regional limits**. Day-one integrations: Claude Code, OpenCode, ZCode, Cline, Kilo Code, OpenClaw, Crush, Factory.

**Weaknesses:** Trails Claude Opus 4.8 by 1–13% on long-horizon benchmarks. SWE-Marathon (13.0) still far behind Opus 4.8 (26.0). Not yet ranked on BenchLM or LM Arena. Higher per-token cost than DeepSeek V4 Flash or MiMo.

**Best for LLM Wiki:** GLM-5.1 best for autonomous wiki maintenance agents. GLM-5 (Reasoning) for complex classification and knowledge graph construction. GLM-5.2 is now the top choice for long-document wiki generation and long-horizon autonomous coding — confirmed benchmarks show it beats GPT-5.5 on most agentic coding tasks at ~1/6th the cost.

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

> "GLM-5.2 is the first open-weights model to cross 80% on Terminal-Bench, and beats every other open model available. It also beats Gemini, making it a frontier-level model for a fraction of the cost. Open weights is back." — Cline IDE, on GLM-5.2 day-one integration

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
- [[chinese-code-harness-comparison]] ([Chinese Code Harness Comparison](chinese-code-harness-comparison.md))
<!-- RU -->

## Краткое описание

Сравнение китайских передовых LLM-моделей для создания базы знаний в стиле LLM Wiki Карпати — охватывает DeepSeek V4, Kimi K2.6/K2.7 Code, GLM-5/5.1/5.2, Qwen 3.5/3.7, Xiaomi MiMo-V2.5 и MiniMax-M3. Включает оценки BenchLM, рейтинги LM Arena, индексы интеллекта Artificial Analysis, цены API, размеры контекстного окна и применимость для извлечения знаний, двуязычного реферирования и агентных вики-воркфлоу. Обновлено 29 июня 2026: опубликованы полные бенчмарки GLM-5.2 (превосходит GPT-5.5 на длинных кодинговых задачах), анонсировано пиковое/внепиковое ценообразование DeepSeek V4 (2× в пиковые часы, официальный запуск в середине июля), исправлены цены по провайдерам.

## Ключевые идеи

- **Qwen3.7 Max** — новый лидер китайского фронтира с оценкой BenchLM 91, занимая 5-е место в мире — скачок на 12 очков по сравнению с Qwen3.5
- DeepSeek V4 Pro (Max) лидирует в кодинговых бенчмарках (LiveCodeBench 93.5) при оценке BenchLM 87, но теперь лишь второй среди китайских моделей
- MiniMax-M3 выходит на фронтир-уровень с оценкой Artificial Analysis 55 по цене всего $0.22/М токенов — самый дешёвый вариант фронтира
- **GLM-5.2** выпущена 13 июня 2026 (753 млрд параметров) с **контекстом 1M токенов**. Полные бенчмарки опубликованы 17 июня: **превосходит GPT-5.5** на SWE-bench Pro (62.1 vs 58.6), FrontierSWE (74.4 vs 72.6), PostTrainBench и HLE-w-tools — **сильнейшая open-source модель** в мире, #2 на длинных задачах после Claude Opus 4.8. Лицензия MIT, без региональных ограничений
- **DeepSeek V4** — официальный запуск в середине июля 2026 с новым **пиковым/внепиковым (повременным) ценообразованием**: пиковые часы стоят **в 2 раза дороже** (пик = UTC 01:00–04:00 и 06:00–10:00). DSpark (спекулятивное декодирование) теперь работает для ускорения инференса
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
| 11 | GLM-5.2 | Z.AI | N/A (BenchLM) | Да (MIT) | 1M |
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
| **MiMo-V2.5 Flash** | $0.10 | $0.30 | 1M |
| **DeepSeek V4 Flash** | $0.14 | $0.28 | 1M |
| **MiniMax-M3** | $0.30 | $1.20 | — |
| **DeepSeek V4 Pro** | $0.435 | $0.87 | 1M |
| **Qwen3.7 Plus** | $0.40 | $1.60 | 1M |
| **Kimi K2.6** | $0.95 | $4.00 | 262K |
| **Kimi K2.7 Code** | $0.95 / $0.19 (cache hit) | $4.00 | 262K |
| **GLM-5.1** | $0.98 | $3.08 | 203K |
| **GLM-5.2** | $1.40 / $0.26 (cache hit) | $4.40 | 1M |
| **Qwen3.7 Max** | $1.25 (OpenRouter) / $2.50 (Alibaba) | $3.75 (OR) / $7.50 (Alibaba) | 1M |

> **Примечание о ценах:** цены существенно зависят от провайдера (OpenRouter vs прямой API vs Alibaba Cloud/DashScope). Использованы данные VentureBeat (июнь 2026) и OpenRouter; цифры из более ранних источников могут отличаться.

### Цены официальных провайдеров (first-party API)

Цены от **собственных API-платформ** создателей моделей (не реселлеры вроде OpenRouter). Цены DeepSeek — обычные (внепиковые); с середины июля пиковые часы будут стоить 2×.

| Модель | Официальный провайдер | Ввод $/М (cache miss) | Ввод $/М (cache hit) | Вывод $/М | Контекст | Макс. вывод |
|--------|----------------------|------------------------|-----------------------|------------|---------|-------------|
| DeepSeek V4 Flash | api.deepseek.com | $0.14 | $0.0028 | $0.28 | 1M | 384K |
| DeepSeek V4 Pro | api.deepseek.com | $0.435 | $0.003625 | $0.87 | 1M | 384K |
| GLM-5.1 | Z.AI API (z.ai) | $1.40 | — | $4.40 | 203K | 64K |
| GLM-5.2 | Z.AI API (z.ai) | $1.40 | $0.26 | $4.40 | 1M | 131K |
| Qwen3.7 Plus | Alibaba DashScope | $0.40 | — | $1.60 | 1M | Standard |
| Qwen3.7 Max | Alibaba DashScope | $2.50 | — | $7.50 | 1M | Standard |
| Kimi K2.6 | Moonshot Platform | $0.95 | — | $4.00 | 262K | Standard |
| Kimi K2.7 Code | Moonshot Platform | $0.95 | $0.19 | $4.00 | 262K | Standard |
| MiMo-V2.5 Flash | Xiaomi Platform | $0.10 | — | $0.30 | 1M | Standard |
| MiMo-V2.5 Pro (≤256K) | Xiaomi Platform | $1.00 | — | $3.00 | 1M | Standard |
| MiniMax-M3 (≤512K) | platform.minimax.io | $0.30 | $0.06 | $1.20 | — | Standard |

> GLM-5.2 соответствует официальным тарифам GLM-5.1 от Z.AI ($1.40/$4.40). OpenRouter перепродаёт GLM-5.1 дешевле — $0.98/$3.08; скидка зависит от реселлера. Cache-hit ценообразование DeepSeek ($0.0028–$0.0036/М) — самое агрессивное в индустрии, делая повторные запросы с тяжёлым контекстом почти бесплатными.

### Детали ценообразования

- **DeepSeek V4** использует агрессивное cache-hit ценообразование: $0.003/М на ввод и $0.004/М на вывод, что делает повторные запросы почти бесплатными.
- **Пиковое/внепиковое ценообразование DeepSeek V4** (анонсировано 26 июня, действует с середины июля): пиковые часы стоят **в 2 раза дороже**. Пик = UTC 01:00–04:00 и 06:00–10:00 (по Пекину 09:00–12:00, 14:00–18:00). V4-Flash: 0.02/1.00/2.00 RMB → 0.04 RMB в пик. Вывод V4-Pro в пик: RMB 12/М. 2× применяется ко всей биллинговой статистике. Это сигнал, что LLM API становятся планируемым рынком вычислительных ресурсов по типу электротариффа.
- **Kimi K2.7 Code** на Kimi Platform: cache-hit ввод $0.19/М; OpenRouter предлагает flat-рейт $0.75/$3.50.
- **GLM-5.2** API: $1.40/М ввод, $4.40/М вывод (на уровне GLM-5.1); кэшированный ввод $0.26/М. Также доступна через тарифы GLM Coding Plan (годовая оплата): Lite $12.60/мес, Pro $50.40/мес, Max $112.00/мес. Квота: 3× в пик (14:00–18:00 по Пекину), 2× внепик; промо: внепик 1× до конца сентября.
- **Qwen3.7 Max** и **Qwen3.7 Plus** работают через Alibaba Cloud/DashScope; Plus — $0.40/М ввод, $1.60/М вывод, включает vision. Max — $2.50/$7.50 напрямую у Alibaba или $1.25/$3.75 через OpenRouter. Открытые веса всё ещё не выпущены по состоянию на 29 июня.

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

**Сильные стороны:** Наивысший кодинговый бенчмарк среди всех моделей мира (LiveCodeBench 93.5, Codeforces 3206). Контекст 1M. Открытые веса MIT. Три режима рассуждений: без размышлений, Think High, Think Max. Гибридное внимание снижает стоимость на 73%. DSpark (спекулятивное декодирование) теперь работает для ускорения инференса. Цены с попаданием в кэш $0.003/$0.004 за М токенов — фактически бесплатно.

**Слабые стороны:** BenchLM 87 теперь отстаёт от Qwen3.7 Max на 4 очка. **Пиковое/внепиковое ценообразование** (с середины июля): пиковые часы 2× — команды в определённых часовых поясах почувствуют это сильнее. Устаревшие API-алиасы отключаются 24 июля 2026. Pro в 3 раза дороже Flash.

**Лучше всего для LLM Wiki:** Уровень Flash для высокоинтенсивного извлечения и реферирования. Уровень Pro для сложной классификации и обслуживания вики-скриптов. Кэширование делает повторные перестроения индекса почти бесплатными.

### Qwen3.7 Max / Qwen3.5 (Alibaba)

**Сильные стороны:** Qwen3.7 Max с BenchLM 91 — сильнейшая китайская модель, 5-е место в мире. Индекс Artificial Analysis **56.6** (на 4.8 очка выше Qwen3.6 Max Preview). Полные оценки бенчмарков теперь доступны: HLE 41.4, HLE-w-tools 53.5, AIME 2026 97, GPQA-Diamond 90, SWE-bench Pro 60.6, Terminal-Bench 2.1 75, MCP-Atlas 76.4. Qwen3.5-27B (плотная модель) превосходит ожидания — SWE-bench 72.4%, конкурентоспособна с моделями в 5-10 раз больше. Архитектура Gated DeltaNet эффективнее чистых трансформеров. WebDev Arena Elo 1537 (#7). 262K контекст для вариантов Qwen3.5.

**Слабые стороны:** Qwen3.7 Max **не имеет открытых весов** — сообщество активно запрашивает открытие весов по состоянию на 29 июня. Qwen3.5-397B набирает 78 — на 13 очков меньше Qwen3.7 Max. Qwen 4 ещё не анонсирована.

**Лучше всего для LLM Wiki:** Qwen3.7 Max для генерации качества фронтира через API. Qwen3.5-27B для экономичного самохостинга. Qwen3.7 Plus за $0.40/$1.60 с vision для среднего уровня и мультимодальных задач. Маленькие варианты для реалтайм-классификации.

### Kimi K2.6 / K2.7 Code (Moonshot AI)

**K2.6:** BenchLM 84. Элитный кодинг (LiveCodeBench 89.6, SWE-bench Pro 58.6 — лучший среди китайских моделей). Открытые веса. Agent Swarm: 300 подагентов и 4,000 координированных шагов. Мультимодальность. Экосистема Kimi Code CLI, Kimi Claw, Kimi Work.

**K2.7 Code:** Выпущена 12 июня 2026 года как специализированная для кодинга преемница с той же архитектурой MoE 1T/32B и контекстом 256K. Всегда работает в режиме рассуждений; на ~30% меньше thinking-токенов, чем у K2.6. Превосходит K2.6 по всем шести кодинговым/агентным бенчмаркам Moonshot (Kimi Code Bench 62.0 vs 50.9, MCP Atlas 76.0 vs 69.4, MCP Mark Verified 81.1 vs 72.8), но всё ещё отстаёт от GPT-5.5 и Claude Opus 4.8. Пока не ранжирована на BenchLM и LM Arena. Оценки MMLU/GPQA/AIME не опубликованы.

**Слабые стороны:** Контекст 256–262K (меньше, чем 1M у DeepSeek/MiMo). K2.6: Agent Arena лишь 0.56%. K2.7 Code — только кодинг, не универсальная модель.

**Лучше всего для LLM Wiki:** K2.6 для обслуживания вики с упором на код, анализа транскриптов YouTube и обработки технического контента. K2.7 Code для специфических кодинговых агентских задач; не подходит для общей двуязычной генерации.

### GLM-5 / GLM-5.1 / GLM-5.2 (Z.AI / Zhipu AI)

**GLM-5.1:** Лидирует среди китайских моделей в Agent Arena (#8, 3.38%) и WebDev Arena (Elo 1532). BenchLM 82. GLM-5 (Reasoning) BenchLM 83, силён в математике и кибербезопасности (CyberGym 68.7). 8+ часов автономной работы. Лицензия MIT.

**GLM-5.2:** Выпущена 13 июня 2026 — флагман на **753 млрд параметров**, созданный для длинных автономных кодинговых задач, со **стабильным контекстом 1M токенов**. **Полные бенчмарки опубликованы 17 июня** (блог Z.AI на HuggingFace): это **сильнейшая open-source модель** в мире, **превосходящая GPT-5.5** на большинстве длинных кодинговых задач — SWE-bench Pro 62.1 (vs GPT-5.5 58.6), FrontierSWE Dominance 74.4 (vs 72.6), Terminal-Bench 2.1 81.0 (vs 84), PostTrainBench 34.3 (vs 28.4), HLE-w-tools 54.7 (vs 52.2), MCP-Atlas 76.8 (vs 75.3). Занимает **#2 в мире** на длинных задачах, уступая только Claude Opus 4.8. Также победила в **Design Arena** (#1, ELO 1360), обогнав Claude Fable 5.

**Архитектура:** IndexShare (повторное использование одного индексера на каждые 4 слоя sparse-внимания → **в 2.9× меньше FLOPs** при контексте 1M); улучшенный MTP для спекулятивного декодирования (+20% к длине принятия); фреймворк `slime` для агентного RL; critic-based PPO для длинных задач; anti-hack модуль, блокирующий reward-hacking вызовы инструментов во время RL-обучения. Гибкие режимы усилия: **High** (баланс производительности/задержки, примерно вдвое меньше токенов вывода) и **Max** (пиковый интеллект, ~85k токенов вывода на задачу).

**Цены:** API $1.40/М ввод, $4.40/М вывод (на уровне GLM-5.1), кэшированный ввод $0.26/М. Тарифы GLM Coding Plan (годовая оплата): Lite $12.60/мес, Pro $50.40/мес, Max $112.00/мес. Квота: 3× пик, 2× внепик; промо: внепик 1× до конца сентября. Лицензия MIT — **без региональных ограничений**. Интеграции первого дня: Claude Code, OpenCode, ZCode, Cline, Kilo Code, OpenClaw, Crush, Factory.

**Слабые стороны:** Отстаёт от Claude Opus 4.8 на 1–13% на длинных бенчмарках. SWE-Marathon (13.0) ещё далеко до Opus 4.8 (26.0). Пока не ранжирована на BenchLM и LM Arena. Выше стоимость за токен, чем у DeepSeek V4 Flash или MiMo.

**Лучше всего для LLM Wiki:** GLM-5.1 — лучший выбор для автономных агентов обслуживания вики. GLM-5 (Reasoning) для классификации и графов знаний. GLM-5.2 — теперь топовый выбор для генерации длинных документов вики и длинных автономных кодинговых задач — подтверждённые бенчмарки показывают, что она превосходит GPT-5.5 на большинстве агентных кодинговых задач примерно за 1/6 стоимости.

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

> «GLM-5.2 — первая модель с открытыми весами, преодолевшая 80% на Terminal-Bench, и она превосходит все остальные open-модели. Также обходит Gemini, делая её моделью фронтир-уровня за малую долю стоимости. Open weights возвращаются.» — Cline IDE, об интеграции GLM-5.2 в первый день

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
