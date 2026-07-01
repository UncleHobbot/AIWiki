---
title: "Enterprise GPU Underutilization: 5% Average Rates as AI Costs Rise"
title_ru: "Недозагрузка корпоративных GPU: средний уровень использования 5% при росте затрат на ИИ"
category: news
tags: [gpu, enterprise, utilization, inference, cost, infrastructure, ai-infrastructure, nvidia]
date: 2026-05-11
updated: 2026-05-17
sources:
  - https://winbuzzer.com/2026/05/11/enterprises-face-underused-gpu-fleets-as-ai-costs-rise-xcxwbn
  - https://www.reddit.com/r/singularity/comments/1tc8j8f/behind_millions_of_dollars_of_funding_in_ai_sit/
---

## Summary

Enterprises sitting on millions in GPU investments are averaging just 5% utilization rates, while inference costs plus cost of ownership have risen from 34% to 41% of total AI spend. The technology designed for efficiency has its own massive infrastructure inefficiency problem.

## Key Ideas
- **5% average GPU utilization:** Companies rushed to buy fleets after ChatGPT launched but most hardware sits idle or poorly scheduled
- **Inference cost + TCO rose to 41%** from 34%, driven by operational overhead rather than raw compute demand
- **Bottleneck is data movement, not compute:** GPUs idle while waiting for data — HBM bandwidth is the hidden constraint
- **Frontier labs excluded:** The 5% figure applies to enterprises, not AI labs (OpenAI, Anthropic, Google) which run near 100%
- **Scheduling, routing, governance** are the real problems — allocation of hardware eats majority of budget
- **Selling unused compute to frontier labs** is emerging as a recovery strategy (Anthropic buying SpaceX colocation capacity)

## Details

After ChatGPT triggered a gold rush of GPU purchasing in 2023-2024, enterprises now face a "build it and they will come" hangover. The irony is structural: the technology meant to optimize everything has its own optimization crisis.

Key factors behind the 5% number:
- **Scheduling fragmentation:** Jobs aren't batched efficiently; GPUs wait between inference requests
- **Memory bandwidth ceiling:** Even with HBM, moving model weights and KV caches creates idle cycles
- **Over-provisioning for peaks:** Fleets sized for worst-case demand sit idle at average load
- **Multi-tenant complexity:** Governance, routing, and access control add layers of latency

Implication for developers: local models on consumer GPUs (e.g., RTX 3090/4090 running Qwen 3.6 27B at Q4) are often more cost-efficient per effective token than enterprise-grade hardware, because they have zero scheduling overhead.

## Related Entries
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget Allocation for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3: Diffusion Attention for 7.8x LLM Speedup](../tools/orthrus-qwen3-acceleration.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models for Building Karpathy's LLM Wiki: DeepSeek, Kimi, GLM, Qwen, MiMo](../models/llm-wiki-chinese-models-comparison.md))
- [[nvidia-sol-execbench]] ([NVIDIA SOL-ExecBench](../concepts/nvidia-sol-execbench.md))
- [[cerebras-openai-capacity-lockup]] ([Cerebras × OpenAI Capacity Deal](cerebras-openai-capacity-lockup.md))

---
<!-- RU -->

## Краткое описание

Предприятия с миллионными инвестициями в GPU в среднем используют лишь 5% мощностей, в то время как затраты на инференс и стоимость владения выросли с 34% до 41% от общих расходов на ИИ. Технология, созданная для оптимизации, страдает от собственной инфраструктурной неэффективности.

## Ключевые идеи
- **5% средняя загрузка GPU:** Компании бросились закупать GPU-парки после запуска ChatGPT, но большая часть оборудования простаивает
- **Затраты на инференс + стоимость владения выросли до 41%** с 34% из-за операционных накладных расходов, а не спроса на вычисления
- **Узкое место — перемещение данных, а не вычисления:** GPU простаивают в ожидании данных — пропускная способность HBM является скрытым ограничением
- **Передовые лаборатории исключены:** показатель 5% относится к предприятиям, а не ИИ-лабораториям (OpenAI, Anthropic, Google), которые работают с загрузкой, близкой к 100%
- **Планирование, маршрутизация, управление** — вот реальные проблемы; распределение оборудования съедает большую часть бюджета
- **Продажа неиспользуемых мощностей передовым лабораториям** становится стратегией восстановления (Anthropic покупает мощности у SpaceX)

## Подробнее

После того как ChatGPT вызвал золотую лихорадку закупок GPU в 2023-2024 годах, предприятия столкнулись с похмельем «построил — и они придут». Ирония структурна: технология, призванная всё оптимизировать, имеет собственный кризис оптимизации.

Ключевые факторы за цифрой в 5%:
- **Фрагментация планирования:** задачи не пакетируются эффективно; GPU ждут между запросами инференса
- **Ограничение пропускной способности памяти:** даже с HBM перемещение весов моделей и KV-кэшей создаёт циклы простоя
- **Избыточное обеспечение для пиков:** парки, рассчитанные на худший спрос, простаивают при средней нагрузке
- **Сложность мультиарендности:** управление, маршрутизация и контроль доступа добавляют слои задержки

Следствие для разработчиков: локальные модели на потребительских GPU (например, RTX 3090/4090 с Qwen 3.6 27B на Q4) часто более экономичны на эффективный токен, чем оборудование корпоративного класса, из-за нулевых накладных расходов на планирование.

## Связанные записи
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget Allocation for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3: Diffusion Attention for 7.8x LLM Speedup](../tools/orthrus-qwen3-acceleration.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models for Building Karpathy's LLM Wiki: DeepSeek, Kimi, GLM, Qwen, MiMo](../models/llm-wiki-chinese-models-comparison.md))
- [[nvidia-sol-execbench]] ([NVIDIA SOL-ExecBench](../concepts/nvidia-sol-execbench.md))
- [[cerebras-openai-capacity-lockup]] ([Cerebras × OpenAI Capacity Deal](cerebras-openai-capacity-lockup.md))
