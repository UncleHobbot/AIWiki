---
title: "TabPFN-3: Pre-trained Tabular Foundation Model"
title_ru: "TabPFN-3: Предобученная табличная фундаментальная модель"
category: models
tags: [tabpfn, tabular, foundation-model, machine-learning, sklearn]
date: 2026-05-15
updated: 2026-05-15
sources:
  - https://www.reddit.com/r/MachineLearning/comments/1tb3fh5/tabpfn3_just_released_a_pretrained_tabular/
  - https://priorlabs.ai/technical-reports/tabpfn-3
  - https://siliconangle.com/2025/12/01/prior-labs-debuts-tabular-ai-foundation-model-scales-10-million-rows/
---

## Summary
TabPFN-3 is the latest generation of Prior Labs' tabular foundation model, scaling to 1M training rows on a single H100 GPU with a single forward pass — no training, no hyperparameter tuning required. It achieves a 93% win rate over classical ML on the TabArena benchmark and introduces test-time compute scaling ("Thinking Mode") for even higher accuracy.

## Key Ideas
- Single forward pass prediction on tabular data — no iterative training or hyperparameter search
- Scales to 1M rows with ~8GB KV cache per million rows per estimator on a single H100
- Thinking Mode (TabPFN-3-Plus) uses test-time compute to beat all non-TabPFN methods by 200+ Elo on TabArena, surpassing 4-hour-tuned AutoGluon 1.5 extreme
- 10x–1000x faster inference than previous versions; SHAP computation is 120x faster via KV caching
- Native many-class support (up to 160 classes) with non-parametric retrieval decoder
- Calibrated quantile regression in a single forward pass via bar-distribution regression head
- Pre-trained exclusively on synthetic data — no real data, no LLMs, no internet search involved
- Three deployment paths: API, enterprise licensing (on-prem, AWS SageMaker, Azure AI Foundry), and open-source weights (TABPFN-3.0 License v1.0)

## Details
TabPFN-3 builds on the lineage of TabPFN v1 (1K rows), TabPFN v2 (10K rows, published in Nature), and TabPFN-2.5 (100K rows). Each generation has expanded scale while maintaining the core innovation: approximating Bayesian inference through a transformer pre-trained on synthetic datasets. The TabPFN family has accumulated over 3M PyPI downloads and 200+ published applications across domains including time-series forecasting, causal inference, Bayesian optimization, and reinforcement learning.

The architecture introduces a reduced KV cache with row-chunked inference, making 1M-row datasets practical on a single GPU. A specialized checkpoint, TabPFN-TS-3, ranks 2nd on the time-series benchmark fev-bench. The model also achieves new SOTA on relational benchmarks (RelBenchV1) and tabular-text datasets (TabSTAR via TabPFN-3-Plus). On the largest-data subset of TabArena (10K–100K samples), TabPFN-3-Plus outperforms AutoGluon 1.5 extreme — a complex ensemble tuned for 4 hours — while being 10x faster.

Prior Labs, founded by Frank Hutter and backed by €9M in seed funding from Balderton Capital, XTX Markets, and others, reports enterprise adoption by Hitachi (predictive maintenance for rail networks) and Oxford Cancer Analytics (lung disease detection). The model is released under a permissive license for research and internal evaluation, with commercial API and enterprise licensing available.

## Related Entries
- [[llm4sr-survey]]
- [[dynamic-compute-budget-local-llm]]

---
<!-- RU -->

## Краткое описание
TabPFN-3 — новейшее поколение табличной фундаментальной модели от Prior Labs, способное обрабатывать до 1M строк обучающих данных на одном GPU H100 за один forward pass — без обучения, без подбора гиперпараметров. Модель демонстрирует 93% долю побед над классическим ML на бенчмарке TabArena и впервые вводит масштабирование вычислений на этапе вывода (Thinking Mode).

## Ключевые идеи
- Предсказание на табличных данных за один forward pass — без итеративного обучения или поиска гиперпараметров
- Масштабирование до 1M строк с KV-кэшем ~8 ГБ на миллион строк на одном H100
- Thinking Mode (TabPFN-3-Plus) использует test-time compute и превосходит все не-TabPFN методы на 200+ Elo на TabArena, обгоняя AutoGluon 1.5 extreme с 4-часовой настройкой
- Инференс в 10x–1000x быстрее предыдущих версий; вычисление SHAP ускорено в 120x благодаря KV-кешированию
- Нативная поддержка многих классов (до 160) с непараметрическим retrieval-декодером
- Калиброванная квантильная регрессия за один forward pass через bar-distribution regression head
- Предобучена исключительно на синтетических данных — без реальных данных, LLM или доступа к интернету
- Три варианта развёртывания: API, коммерческая лицензия (on-prem, AWS SageMaker, Azure AI Foundry) и открытые веса (лицензия TABPFN-3.0 License v1.0)

## Подробнее
TabPFN-3 продолжает линейку моделей: TabPFN v1 (1K строк), TabPFN v2 (10K строк, опубликована в Nature) и TabPFN-2.5 (100K строк). Каждое поколение расширяет масштаб, сохраняя ключевую инновацию — аппроксимацию байесовского вывода через transformer, предобученный на синтетических наборах данных. Семейство TabPFN накопило свыше 3M загрузок через PyPI и более 200 опубликованных применений в доменах прогнозирования временных рядов, причинно-следственного анализа, байесовской оптимизации и обучения с подкреплением.

Архитектура использует сокращённый KV-кэш с построчной (row-chunked) инференс-стратегией, что делает работу с наборами данных из 1M строк на одном GPU практичной. Специализированный чекпойнт TabPFN-TS-3 занимает 2-е место на временном бенчмарке fev-bench. Модель также достигает нового SOTA на реляционных бенчмарках (RelBenchV1) и таблично-текстовых датасетах (TabSTAR через TabPFN-3-Plus). На подмножестве TabArena с наибольшими данными (10K–100K образцов) TabPFN-3-Plus превосходит AutoGluon 1.5 extreme — сложный ансамбль с 4-часовой настройкой — при этом работая в 10 раз быстрее.

Prior Labs, основанная Фрэнком Хуттером и получившая €9M посевных инвестиций от Balderton Capital, XTX Markets и других инвесторов, сообщает о корпоративном внедрении компанией Hitachi (предиктивное обслуживание железнодорожных сетей) и Oxford Cancer Analytics (обнаружение заболеваний лёгких). Модель выпущена под пермиссивной лицензией для исследований и внутренней оценки; коммерческие API и корпоративные лицензии доступны отдельно.

## Связанные записи
- [[llm4sr-survey]]
- [[dynamic-compute-budget-local-llm]]
