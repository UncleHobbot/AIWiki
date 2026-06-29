---
title: "MoE-Watcher-Modifier: Visualizing and Editing Expert Routing in MoE Models"
title_ru: "MoE-Watcher-Modifier: визуализация и правка маршрутизации экспертов в MoE-моделях"
category: tools
tags: [moe, expert-routing, visualization, qwen, interpretability, llm-internals]
aliases: [MoE-Watcher-Modifier, MoE Watcher, expert routing visualizer]
confidence: medium
updated: 2026-06-29
sources:
  - https://github.com/dibyapp/MoE-Watcher-Modifier
  - https://www.reddit.com/r/Qwen_AI/comments/1ufdyfi/i_visualized_qwen3moes_expert_routing_and_some/
---

## Summary
MoE-Watcher-Modifier is an open-source tool for monitoring and modifying Mixture-of-Experts (MoE) models. By running a few thousand prompts through Qwen3-MoE and tracking expert-selection patterns, it reveals that a small subset of experts handles most traffic while others are rarely activated — and lets you modify routing behaviour.

## Key Ideas
- **Expert utilization is highly skewed**: a small subset of experts handles most of the traffic; many experts are rarely activated. This is visible in the activation heatmap and utilization distribution the tool produces.
- **Monitoring**: track which experts fire across prompts to understand what the model is actually doing internally.
- **Modification**: beyond watching, the tool can modify MoE routing — useful for research into pruning under-used experts or steering behavior.
- **Interpretability angle**: makes the opaque routing decision inside MoE models inspectable, supporting research into whether "barely used" experts are dead weight or carry specialized, rarely-triggered knowledge.
- **Runs against Qwen3-MoE** out of the box; the methodology generalizes to other MoE architectures.

## Details
The skewed-utilization finding matters for efficiency research: if many experts rarely fire, there may be opportunity to prune them for a smaller footprint — or, conversely, those low-activation experts may encode important but rarely-needed capabilities that pruning would silently remove. Making routing visible is the prerequisite to answering that question rigorously.

## Related Entries
- [[qwen-agentworld]] ([Qwen-AgentWorld: First World Model](../models/qwen-agentworld.md))
- [[nvidia-sol-execbench]] ([NVIDIA SOL-ExecBench](../concepts/nvidia-sol-execbench.md))

---
<!-- RU -->

## Краткое описание
MoE-Watcher-Modifier — open-source инструмент для мониторинга и модификации Mixture-of-Experts (MoE)-моделей. Прогнав несколько тысяч промптов через Qwen3-MoE и отследив паттерны выбора экспертов, инструмент показывает, что небольшое подмножество экспертов обрабатывает большую часть трафика, тогда как другие активируются редко — и позволяет модифицировать поведение маршрутизации.

## Ключевые идеи
- **Утилизация экспертов сильно скошена**: небольшое подмножество экспертов обрабатывает большую часть трафика; многие активируются редко. Это видно на тепловой карте активаций и распределении утилизации.
- **Мониторинг**: отслеживание, какие эксперты срабатывают по промптам, чтобы понять, что модель делает внутри.
- **Модификация**: помимо наблюдения, инструмент умеет менять маршрутизацию MoE — полезно для исследований по прунингу малоиспользуемых экспертов.
- **Угол интерпретируемости**: делает непрозрачное решение о маршрутизации внутри MoE проверяемым.
- **Работает с Qwen3-MoE** из коробки; методология обобщается на другие MoE-архитектуры.

## Подробнее
Вывод о скошенной утилизации важен для исследований эффективности: если многие эксперты срабатывают редко, их, возможно, можно прунить для меньшего footprint — либо, наоборот, эти малоактивные эксперты кодируют важные, но редко нужные возможности, чей прунинг молча их удалит. Видимая маршрутизация — предпосылка для строгого ответа на этот вопрос.

## Связанные записи
- [[qwen-agentworld]] ([Qwen-AgentWorld: First World Model](../models/qwen-agentworld.md))
- [[nvidia-sol-execbench]] ([NVIDIA SOL-ExecBench](../concepts/nvidia-sol-execbench.md))
