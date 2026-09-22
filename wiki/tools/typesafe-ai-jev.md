---
title: "TypeSafe AI Jev: System One Models — Typed Decisions Instead of Text"
title_ru: "TypeSafe AI Jev: System One модели — типизированные решения вместо текста"
category: tools
tags: [typesafe-ai, jev, system-one-model, structured-outputs, classification, confidence, rlcd, inference, ai-infrastructure, agents]
aliases: [Jev, Jev AI, TypeSafe AI, typesafe.ai, System One Model, System One Models, RLCD]
confidence: high
date: 2026-09-21
updated: 2026-09-21
sources:
  - https://typesafe.ai
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://typesafe.ai/manifesto
  - https://typesafe.ai/team
  - https://docs.typesafe.ai/introduction
  - https://docs.typesafe.ai/confidence
  - https://docs.typesafe.ai/models
  - https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
  - https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711
  - https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/
  - https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/
  - https://news.ycombinator.com/item?id=49717558
  - https://flaviocopes.com/jev/
  - https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew
  - https://en.wikipedia.org/wiki/Jev_(AI_model)
---

## Summary
Jev is the first "System One Model" from TypeSafe AI (typesafe.ai, San Francisco): a hosted API that answers narrow questions about input text with typed, structured decisions — choices, scores, yes/no probabilities — plus a confidence score, instead of generating natural language. Launched from stealth on 2026-09-15 alongside a $40M seed round led by DCVC.

> **Disambiguation:** unrelated to the old "Typesafe" company behind Scala (now Lightbend) or the `typesafe.com` config library. GitHub org: `TypeSafeAI`.

## Key Ideas
- **"Decisions, not strings":** Jev cannot generate text at all. Every output is a typed value with a probability distribution and a 0–1 confidence score, meant to be branched on in code rather than parsed from prose.
- **Three primitives:** Choice (pick from up to 255 options), Score (rate against 2–10 ordered levels), Noul (yes/no probability). Send one `state` plus any number of named questions — all answered in a single parallel pass.
- **New training recipe:** transformer trained exclusively on synthetic data with RLCD (Reinforcement Learning for Calibrated Decisions) and a parallel sampler instead of autoregressive token generation.
- **Headline claims (vendor-run):** 193.6x faster / 444.6x cheaper than LLMs on decision workflows; latency 70–500 ms; $42 per billion input tokens with output tokens free ("238x cheaper than Claude Fable 5.1").
- **Independent checks are positive but smaller:** Vercel reported 5–18x faster classification after replacing an LLM classifier; Every.to reportedly measured ~25x faster / ~580x cheaper on one extraction task.
- **"Zero hallucinations" = schema conformance only.** A wrong-but-valid answer is still possible — the most-criticized marketing claim (The Register, HN, MarkTechPost).
- **Strong organic reception:** the HN launch thread hit 1,941 points / 507 comments, and a clone ecosystem (SemIf, von, mini-jev, CUA-S1) appeared within a week.

## Details
**Company.** TypeSafe AI was founded in 2024 and spent ~2 years in stealth. CEO Diogo Almeida spent ~4 years at OpenAI, where per the team page and TechCrunch he worked on RLHF, InstructGPT, ChatGPT and GPT-4; CTO Erik Gafni is a repeat founder (Ravel); COO Sasha Sheng is ex-Meta/FAIR. Funding: $40M seed led by DCVC at a reported ~$200M valuation (Forbes, via Forkast/Wikipedia). The name is a deliberate pun on type safety — and a live collision with Lightbend's legacy "Typesafe" brand.

**Product.** The API (`POST api.typesafe.ai/v1/systemone`, model `jev-1.13.0`) ingests one `state` (text or JSON, 64k-token context, text-only) and evaluates all questions in parallel and in isolation. Confidence is derived from the shape of the probability distribution; the docs state there are **no calibration guarantees** and prescribe a routing pattern: confidence < 0.5 → human review, > 0.9 required for destructive actions. SDKs: Python, JavaScript/TypeScript, a Vercel AI SDK provider, plus a Claude Code agent skill. The docs candidly list weaknesses: literal reading of negations, no math/counting/date arithmetic, context rot on large states, and adversarial text in the state can steer answers.

**Claims vs. evidence.** The 193.6x/444.6x figures are self-run peaks: benchmark reference answers are the *averaged outputs* of GPT-6 Astra and Claude Fable 5.1 (not ground truth), workflows were authored by TypeSafe's own team, and the company itself admits the numbers are the high end and that early-access pricing "cannot be proven unsubsidized". Field reports land at roughly 18–25x — large, but an order below the peaks. A pre-registered experiment by Bartosz Mikulski (400 Quick-Draw! sketches serialized as SVG text) showed Jev at ~35% vs. ~91% for Sonnet 5 on the actual images — confirming it extracts real signal from text but is bounded by its text-only design. Internally benchmarked accuracy is ~67.8%, claimed comparable to GPT-5.6 Terra.

**Intended applications.** Composable decision points inside software: tool-call gating and intent routing for agents, guardrails/jailbreak screening, RAG passage filtering, citation checking, re-ranking, support-ticket and email triage, content moderation, LLM-agent monitoring, and model routing (Armin Ronacher's use cases). Demos include Jev playing Doom from structured game-state text (~10 queries/sec, ~$7/hour) and Wikiracing.

**Reception.** TechCrunch (Tim Fernholz) wrote a largely positive profile quoting customers Vercel and Bryo AI (the latter: Gemini slightly more accurate on email classification but 10–20x more expensive). The Register was skeptical, calling the "hallucination-free" framing unfair. HN criticism focused on eval design (reference = other LLMs' averages; even then Jev trailed Sonnet 5 on accuracy in one plot), apples-to-oranges latency comparisons (LLM side includes long reasoning runs), and the "not an LLM" claim being contradicted by docs imagery suggesting an open-weight base model + RLCD post-training. Within a week, open-source clones appeared (SemIf at ~3,000 stars, von, mini-jev, and CUA-S1 — a 706k-param specialist that beat hosted Jev on its own narrow task), which reads as both flattery and a warning about the moat.

## Notable Quotes
> "Decisions, not strings." — TypeSafe AI, homepage

> "Sure, it can't emit an invalid type, but it can still emit a completely wrong valid value." — HN commenter `jacobgold` on the "zero hallucinations" claim

> Jev "delegates the hallucination problem a little bit to the user" — Armin Ronacher, creator of Flask, to TechCrunch

## Related Entries
- [[minicheck-fact-verification]] ([MiniCheck: Efficient Fact-Checking of LLMs on Grounding Documents](../tools/minicheck-fact-verification.md)) — same thesis: small specialized models beat general LLMs on narrow verification tasks
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent: Anatomy of the AI Agent Brain](../agents/expensive-model-not-smart-agent.md)) — routing decisions between model tiers in agent architectures
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md)) — background on RLHF, the training paradigm Jev's founders helped create and now argue against
- [[llm-hallucination-bixonimania-case]] ([LLM Medical Hallucination: The Bixonimania Case Study](../concepts/llm-hallucination-bixonimania-case.md)) — why hallucination-free framing matters
- [[speculative-decoding]] ([Speculative Decoding](../concepts/speculative-decoding.md)) — contrast: speeding up autoregressive generation vs. abandoning it

---
<!-- RU -->

## Краткое описание
Jev — первая «System One модель» от TypeSafe AI (typesafe.ai, Сан-Франциско): hosted-API, который отвечает на узкие вопросы по входному тексту типизированными структурированными решениями — выбор варианта, оценка, вероятность «да/нет» — вместе с уровнем уверенности, вместо генерации естественного языка. Вышла из стелса 15.09.2026 вместе с раундом в $40 млн под лидерством DCVC.

> **Не путать:** компания не связана со старой Typesafe (Scala, ныне Lightbend) и библиотекой конфигурации `typesafe.com`. GitHub-организация: `TypeSafeAI`.

## Ключевые идеи
- **«Decisions, not strings»:** Jev вообще не генерирует текст. Каждый ответ — типизированное значение с распределением вероятностей и уверенностью 0–1, предназначенное для ветвления в коде, а не для парсинга прозы.
- **Три примитива:** Choice (выбор из до 255 вариантов), Score (оценка по 2–10 упорядоченным уровням), Noul (вероятность «да/нет»). Отправляете один `state` и любое число именованных вопросов — все отвечаются за один параллельный проход.
- **Новая схема обучения:** трансформер, обученный исключительно на синтетических данных с помощью RLCD (Reinforcement Learning for Calibrated Decisions) и параллельного сэмплера вместо авторегрессионной генерации токенов.
- **Заявленные показатели (бенчмарки вендора):** в 193,6 раза быстрее и в 444,6 раза дешевле LLM на задачах-решениях; латентность 70–500 мс; $42 за миллиард входных токенов, выходные токены бесплатны («в 238 раз дешевле Claude Fable 5.1»).
- **Независимые проверки положительны, но скромнее:** Vercel сообщала об ускорении классификации в 5–18 раз после замены LLM-классификатора; Every.to, по пересказам, измерила ~25x по скорости и ~580x по цене на одной задаче извлечения.
- **«Zero hallucinations» = только соответствие схеме.** Неправильный, но валидный ответ по-прежнему возможен — это самая критикуемая маркетинговая формулировка (The Register, HN, MarkTechPost).
- **Мощный органический резонанс:** тред запуска на HN набрал 1941 пункт / 507 комментариев, а за неделю появилась экосистема клонов (SemIf, von, mini-jev, CUA-S1).

## Подробнее
**Компания.** TypeSafe AI основана в 2024 году и около двух лет провела в стелсе. CEO Диогу Алмейда провёл ~4 года в OpenAI, где, по данным страницы команды и TechCrunch, работал над RLHF, InstructGPT, ChatGPT и GPT-4; CTO Эрик Гафни — серийный основатель (Ravel); COO Саша Шэн — из Meta/FAIR. Финансирование: посевной раунд $40 млн под лидерством DCVC при заявленной оценке ~$200 млн (Forbes, через Forkast/Wikipedia). Название — игра слов вокруг type safety, которая живёт бок о бок с наследием бренда «Typesafe» от Lightbend.

**Продукт.** API (`POST api.typesafe.ai/v1/systemone`, модель `jev-1.13.0`) принимает один `state` (текст или JSON, контекст 64k токенов, только текст) и оценивает все вопросы параллельно и изолированно. Уверенность выводится из формы распределения вероятностей; в документации прямо сказано, что **гарантий калибровки нет**, и предписана схема маршрутизации: уверенность < 0.5 — человек, > 0.9 требуется для деструктивных действий. SDK: Python, JavaScript/TypeScript, провайдер для Vercel AI SDK, а также agent skill для Claude Code. Документация честно перечисляет слабости: буквальное прочтение отрицаний, отсутствие арифметики/подсчёта/работы с датами, context rot на больших состояниях, уязвимость к adversarial-тексту во входных данных.

**Заявления против доказательств.** Цифры 193,6x/444,6x — пики из собственных бенчмарков: эталонные ответы там — усреднённые выводы GPT-6 Astra и Claude Fable 5.1 (не ground truth), сценарии написаны собственной командой TypeSafe, и компания сама признаёт, что это верхняя граница, а раннее ценообразование «нельзя доказать что не субсидируется». Полевые отчёты дают примерно 18–25x — много, но на порядок ниже пиков. Пре-регистрированный эксперимент Бартоша Микульского (400 скетчей Quick-Draw! в виде SVG-текста) показал ~35% у Jev против ~91% у Sonnet 5 на самих изображениях — сигнал из текста Jev извлекает реальный, но ограничен текстовым форматом. Внутренняя точность ~67,8%, заявлена как сопоставимая с GPT-5.6 Terra.

**Применения.** Точки принятия решений внутри софта: гейтинг вызова инструментов и маршрутизация интентов для агентов, guardrails/скрининг jailbreak, фильтрация пассажей для RAG, проверка цитирований, ре-ранжирование, маршрутизация тикетов и почты, модерация контента, мониторинг LLM-агентов, model routing (кейсы Армина Ронахера). Демо: Jev играет в Doom по текстовому описанию состояния игры (~10 запросов/сек, ~$7/час) и Wikiracing.

**Реакция.** TechCrunch (Тим Фернхольц) написал в целом позитивный профиль с цитатами клиентов Vercel и Bryo AI (последняя: Gemini чуть точнее на классификации почты, но в 10–20 раз дороже). The Register скептичен и назвал формулировку «без галлюцинаций» нечестной. Критика на HN фокусировалась на дизайне бенчмарков (эталон — среднее чужих LLM; и даже там Jev уступает Sonnet 5 по точности на одном графике), сравнении несравнимой латентности (в базовую сторону включены долгие reasoning-прогоны) и на заявлении «не LLM», противоречащем картинкам в доках с базовой моделью + RLCD. За неделю появились open-source клоны (SemIf ~3000 звёзд, von, mini-jev и CUA-S1 — специалист на 706 тыс. параметров, обгонявший hosted Jev на его же узкой задаче) — это и лесть, и предупреждение о непрочности moat.

## Примечательные цитаты
> "Decisions, not strings." — TypeSafe AI, главная страница

> "Sure, it can't emit an invalid type, but it can still emit a completely wrong valid value." — комментатор HN `jacobgold` о заявлении «zero hallucinations»

> Jev «делегирует проблему галлюцинаций немного пользователю» — Армин Ронахер, создатель Flask, в интервью TechCrunch

## Связанные записи
- [[minicheck-fact-verification]] ([MiniCheck: Efficient Fact-Checking of LLMs on Grounding Documents](../tools/minicheck-fact-verification.md)) — тот же тезис: маленькие специализированные модели бьют универсальные LLM на узких задачах проверки
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent: Anatomy of the AI Agent Brain](../agents/expensive-model-not-smart-agent.md)) — маршрутизация решений между уровнями моделей в агентных архитектурах
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md)) — фон: RLHF, парадигма обучения, которую основатели Jev создавали и теперь оспаривают
- [[llm-hallucination-bixonimania-case]] ([LLM Medical Hallucination: The Bixonimania Case Study](../concepts/llm-hallucination-bixonimania-case.md)) — почему важна точность формулировок про «отсутствие галлюцинаций»
- [[speculative-decoding]] ([Speculative Decoding](../concepts/speculative-decoding.md)) — контраст: ускорение авторегрессии вместо отказа от неё
