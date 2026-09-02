---
title: "NVIDIA to Acquire Hugging Face for $12.9B — Open-Source Neutrality Concerns"
title_ru: "NVIDIA покупает Hugging Face за $12,9 млрд — вопросы нейтральности open source"
category: news
tags: [nvidia, hugging-face, acquisition, open-source, regulation, the-information]
aliases: [nvidia hugging face, HF acquisition, nvidia buys huggingface]
confidence: high
date: 2026-08-26
updated: 2026-09-01
sources:
  - https://www.theinformation.com/articles/nvidia-agrees-buy-open-source-model-repository-hugging-face-12-9-billion
  - https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/
  - https://fortune.com/2026/08/27/nvidia-hugging-face-billion-dollar-deal-open-source-ai/
  - https://news.ycombinator.com/item?id=49458161
  - https://www.reddit.com/r/LocalLLaMA/comments/1vzmqrk/nvidia_buying_hf_isnt_a_good_thing_for_open_source/
---

## Summary
On August 26, 2026, The Information reported — with TechCrunch, Reuters, CNBC, and Fortune confirming — that NVIDIA agreed to acquire Hugging Face, the de facto hub of open-source AI, for **$12.9 billion** (~86× revenue; HF was last valued at $4.5B in 2023). The deal is reported, not closed; antitrust scrutiny is likely. The r/LocalLLaMA thread title is the community verdict: "isn't a good thing for open source."

## Key Ideas
- **Deal size:** $12.9B; first reported Aug 26, 2026; investors in HF included Google, Amazon, Salesforce, AMD — and NVIDIA itself.
- **Strategic logic (TechCrunch):** protects NVIDIA's chip empire (open models already run on NVIDIA hardware) and takes another swing at cloud/software layers.
- **Community concern:** loss of platform neutrality — preferential treatment of NVIDIA-optimized models, vendor lock-in pressure on the hub every open-weight wiki entry links to.
- **The circulating defense:** NVIDIA may have bought HF to keep it away from OpenAI/Anthropic — neutrality preserved by a hardware vendor rather than a model vendor.
- **Regulatory:** not yet closed; combining dominant AI hardware with the dominant open-model platform invites review.

## Details
For this wiki the stake is concrete: the `sources:` front-matter of dozens of entries points at huggingface.co repos, and the local-LLM workflow ([[ollama]], [[unsloth-qwen38-27b-gguf]], [[clifford-control-plane-local-ai]]) assumes a neutral hub. Even if NVIDIA behaves perfectly, the *perception* of a chip vendor owning the commons changes how labs license their weights. Watch for licensing/infra changes and any migration of flagship models to alternative hubs.

## Related Entries
- [[unsloth-qwen38-27b-gguf]] ([Unsloth Qwen3.8-27B GGUF](unsloth-qwen38-27b-gguf.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
- [[closed-vs-open-model-scaffolding-gap]] ([Closed vs Open Scaffolding Gap](../concepts/closed-vs-open-model-scaffolding-gap.md))
- [[cerebras-openai-capacity-lockup]] ([Cerebras × OpenAI Capacity](cerebras-openai-capacity-lockup.md))

---
<!-- RU -->

## Краткое описание
26 августа 2026 The Information сообщила (подтверждено TechCrunch, Reuters, CNBC, Fortune), что NVIDIA договорилась о покупке Hugging Face — фактического хаба open-source ИИ — за **$12,9 млрд** (~86× выручки; HF оценивалась в $4,5 млрд в 2023). Сделка заявлена, но не закрыта; антимонопольный интерес вероятен. Заголовок треда r/LocalLLaMA — вердикт сообщества: «это не хорошо для open source».

## Ключевые идеи
- **Размер:** $12,9 млрд; первым сообщил The Information 26 авг 2026; среди инвесторов HF были Google, Amazon, Salesforce, AMD — и сама NVIDIA.
- **Стратегическая логика (TechCrunch):** защищает империю чипов NVIDIA и делает ещё заход в облачные/софтверные слои.
- **Опасение сообщества:** потеря нейтральности платформы — преференции NVIDIA-оптимизированным моделям, давление вендор-лок-ина на хаб, на который ссылается каждая open-weight запись вики.
- **Циркулирующая защита:** возможно, NVIDIA купила HF, чтобы не досталась OpenAI/Anthropic — нейтральность под охраной вендора железа вместо вендора моделей.
- **Регуляторика:** сделка не закрыта; доминирование в железе + владение главной платформой открытых моделей приглашает к проверке.

## Подробнее
Для этой вики ставка конкретна: `sources:` десятков записей указывают на репозитории huggingface.co, а локально-LLM воркфлоу предполагает нейтральный хаб. Даже при идеальном поведении NVIDIA *восприятие* того, что вендор чипов владеет общим достоянием, меняет то, как лаборатории лицензируют веса. Следить за лицензионными/инфраструктурными изменениями и миграцией флагманских моделей на альтернативные хабы.

## Связанные записи
- [[unsloth-qwen38-27b-gguf]] ([Unsloth Qwen3.8-27B GGUF](unsloth-qwen38-27b-gguf.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
- [[closed-vs-open-model-scaffolding-gap]] ([Closed vs Open Scaffolding Gap](../concepts/closed-vs-open-model-scaffolding-gap.md))
- [[cerebras-openai-capacity-lockup]] ([Cerebras × OpenAI Capacity](cerebras-openai-capacity-lockup.md))
