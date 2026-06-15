---
title: "Dual DGX Spark Setup for Running DeepSeek V4 Flash Locally"
title_ru: "Связка из двух DGX Spark для локального запуска DeepSeek V4 Flash"
category: tips
tags: [dgx-spark, deepseek, local-llm, hardware, moe, benchmarks, nvidia]
aliases: [dual DGX Spark, DGX Spark cluster]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/LocalLLaMA/comments/1u5g9pr/dual_dgx_sparks_40tks_single_1m_350_tks_agg/
  - https://github.com/elsung/dgx-spark-deepseek-v4-flash
---

## Summary
A community member shared benchmarks and a recipe for running the large DeepSeek V4 Flash MoE model across two NVIDIA DGX Spark units connected via a ConnectX-7 cable, reaching ~40 tok/s single-stream (1M context) and ~350 tok/s aggregate throughput — competitive with an RTX Pro 6000 and Mac Studio M2 Ultra 192GB for agentic workloads.

## Key Ideas
- Running large MoE models like DeepSeek V4 Flash at usable speed on consumer/prosumer hardware requires **two DGX Sparks**, not one — single-unit setups are memory- and bandwidth-limited for this model size.
- A **ConnectX-7 cable** (~$180) providing 200 GB/s interconnect between the two Sparks is the key enabler for the reported speeds; without it, the dual-Spark setup loses most of its advantage.
- Reported numbers: ~40 tok/s decode on a single 1M-context stream, and ~350 tok/s aggregate when running multiple concurrent streams — framed as suitable for agentic/multi-session use.
- Comparison points included in the writeup: RTX Pro 6000 (96GB GDDR7) hit ~46.9 tok/s decode / 344 tok/s prefill but single-stream only; Mac Studio M2 Ultra (192GB) was also benchmarked as a reference.
- The recipes, configs, and full benchmark tables are published as an open GitHub repo (elsung/dgx-spark-deepseek-v4-flash), building on prior community work credited to "Aiden/Antirez" on NVIDIA community threads.

## Details
This is a community report (not vendor-published) describing a practical path to running a frontier-class MoE model (DeepSeek V4 Flash) outside the datacenter. The author frames the result as "in the same playpen as the frontiers" — i.e., DeepSeek V4 Flash inference quality approaching closed frontier models, but runnable on a sub-$10K local hardware budget once you account for two DGX Sparks plus the interconnect cable.

The most actionable detail is the emphasis on interconnect bandwidth: the $180 ConnectX-7 cable enabling 200 GB/s between the two units is called out as "the kicker" — without it, splitting a large MoE model across two Sparks would bottleneck on a much slower link and lose most of the throughput gains. This is a recurring theme in local-LLM hardware discussions: for multi-GPU/multi-node MoE inference, interconnect bandwidth often matters more than raw compute per device.

Given this is a single community benchmark (RSS/Reddit, confidence: low) without independent verification, the absolute numbers should be treated as a starting point rather than a guaranteed result — but the recipe and comparison tables in the linked GitHub repo are useful for anyone evaluating DGX Spark clusters for local MoE inference.

## Related Entries
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](../models/llm-wiki-chinese-models-comparison.md))

---
<!-- RU -->

## Краткое описание
Участник сообщества опубликовал бенчмарки и рецепт запуска большой MoE-модели DeepSeek V4 Flash на двух NVIDIA DGX Spark, соединённых кабелем ConnectX-7, достигнув ~40 ток/с в однопотоковом режиме (контекст 1M) и ~350 ток/с суммарной пропускной способности — на уровне RTX Pro 6000 и Mac Studio M2 Ultra 192GB для агентных нагрузок.

## Ключевые идеи
- Для запуска больших MoE-моделей, таких как DeepSeek V4 Flash, на приемлемой скорости требуются **два DGX Spark**, а не один — одиночные устройства ограничены по памяти и пропускной способности для такого размера модели.
- Ключевой фактор заявленной скорости — **кабель ConnectX-7** (~$180), обеспечивающий межсоединение на 200 ГБ/с между двумя Spark; без него связка из двух устройств теряет большую часть преимущества.
- Заявленные показатели: ~40 ток/с decode для одного потока с контекстом 1M и ~350 ток/с суммарно при нескольких параллельных потоках — автор называет это пригодным для агентных/многосессионных сценариев.
- Для сравнения приведены: RTX Pro 6000 (96GB GDDR7) — ~46.9 ток/с decode / 344 ток/с prefill, но только в однопотоковом режиме; также протестирован Mac Studio M2 Ultra (192GB).
- Рецепты, конфигурации и полные таблицы бенчмарков опубликованы в открытом репозитории на GitHub (elsung/dgx-spark-deepseek-v4-flash), основанном на более ранней работе сообщества, приписываемой «Aiden/Antirez» на форумах NVIDIA.

## Подробнее
Это отчёт сообщества (не от вендора), описывающий практический путь запуска модели уровня frontier (DeepSeek V4 Flash) вне дата-центра. Автор называет результат «в той же лиге, что и frontier-модели» — то есть качество инференса DeepSeek V4 Flash приближается к закрытым frontier-моделям, но работает на локальном оборудовании стоимостью менее $10K с учётом двух DGX Spark и кабеля межсоединения.

Самая практичная деталь — акцент на пропускной способности межсоединения: кабель ConnectX-7 за $180, обеспечивающий 200 ГБ/с между устройствами, назван «ключевым моментом» — без него разделение большой MoE-модели между двумя Spark столкнулось бы с гораздо более медленным каналом и потеряло бы большую часть прироста производительности. Это повторяющаяся тема в обсуждениях локального оборудования для LLM: для multi-GPU/multi-node инференса MoE пропускная способность межсоединения часто важнее, чем чистая вычислительная мощность отдельного устройства.

Поскольку это единичный бенчмарк сообщества (RSS/Reddit, confidence: low) без независимой проверки, абсолютные цифры стоит воспринимать как отправную точку, а не гарантированный результат — но рецепт и сравнительные таблицы в репозитории на GitHub полезны для всех, кто рассматривает кластеры DGX Spark для локального инференса MoE.

## Связанные записи
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
