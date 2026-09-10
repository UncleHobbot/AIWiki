---
title: "Budget Flash Models Compared — GPT-5.6 Luna vs GLM-5.3-Flash vs DeepSeek V4.1 Flash"
title_ru: "Сравнение бюджетных Flash-моделей — GPT-5.6 Luna против GLM-5.3-Flash против DeepSeek V4.1 Flash"
category: research
tags: [gpt-5.6-luna, glm-5.3-flash, deepseek-v4-flash, budget-models, pricing, benchmarks, comparison, flash-tier]
aliases: [budget model comparison, luna vs glm flash vs deepseek flash, cheap model comparison 2026]
confidence: medium
updated: 2026-09-10
sources:
  - https://developers.openai.com/api/docs/models/gpt-5.6-luna
  - https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/
  - https://artificialanalysis.ai/articles/gpt-5-6-has-landed
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.z.ai/devpack/notice/usage-revision
  - https://openrouter.ai/z-ai/glm-5.3-flash
  - https://www.reddit.com/r/LocalLLaMA/comments/1vyzzxu/megathread_glm53flash_former_oxalpha/
  - https://news.ycombinator.com/item?id=49450353
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://api-docs.deepseek.com/updates/
  - https://arcprize.org/results/deepseek-v4-flash-0731
  - https://artificialanalysis.ai/models/deepseek-v4-flash
  - https://www.reddit.com/r/DeepSeek/comments/1w4sw05/glm_53_flash_vs_deepseek_v4_flash_0731_on_hermes/
  - https://openrouter.ai/rankings
---

## Summary

Three models now define the "cheap but capable" tier as of September 2026: **GPT-5.6 Luna** (OpenAI's nano-tier, cut 80% to **$0.20/$1.20** per 1M tokens in July), **GLM-5.3-Flash** (Z.ai's 320B-A18B open-weight MoE at **$0.15/$0.50**, launched Aug 26 after a stealth week as "ox-alpha"), and **DeepSeek V4.1 Flash** (launched *today*, Sept 10, at **$0.15/$0.60 off-peak** — a release so strong DeepSeek is retiring its own V4 Pro flagship on Sept 14). All three converge near the same price point but embody three different philosophies: closed reasoning-dials, open-weight token-burning intelligence, and time-of-day commodity pricing. The honest comparison conclusion: **benchmark numbers are not comparable across the three** (different index versions and suites), the price war has made all three absurdly cheap for simple tasks, and the real differentiators are effort settings, token efficiency, and where your hours fall relative to peak windows.

## Key Ideas

- **Price convergence via price war.** Luna's July 30 cut (−80%, "advancing the price-performance frontier") repriced the tier; GLM-5.3-Flash launched at $0.15/$0.50 three weeks later; DeepSeek answered today by cutting Flash below even its own old off-peak rates. For simple tasks, all three now cost pennies per hundred tasks.
- **~$0.15/$0.50–1.20 per 1M tokens is the floor** — roughly 7–25× cheaper than the flagship tiers above them (Sol $4–5/$30; GLM-5.3 $1.40/$4.40; DeepSeek V4 Pro retired).
- **Benchmarks cannot be honestly compared across the three.** Artificial Analysis numbers exist for all — but on *different index versions* (Luna 51 and GLM-Flash 57 on v4.1.x; DeepSeek Flash 35 on an older index). Head-to-head evidence is community-tier only.
- **The "cheap/fast" label is effort-dependent for all three.** Luna is fast at low/medium effort but "smart but slow" at xhigh/max; GLM-5.3-Flash has mandatory thinking (can't be disabled, default effort = max) and burns ~7× more tokens per task than Gemini 3.7 Flash; DeepSeek Flash is flagged "very verbose" by Artificial Analysis.
- **Three pricing philosophies:** Luna = flat + batch 50% + long-context surcharge; GLM = flat + batch half-price + subscription points (0.4× off-peak / 1.2× peak); DeepSeek = electricity-grid peak/off-peak (peak 2×, only ~7h/day weekdays).
- **Open weights: 2 of 3.** GLM-5.3-Flash (320B-A18B, MIT, first open frontier model combining linear+sparse attention, natively multimodal) and DeepSeek V4.1 Flash (284B-A13B, MIT, native vision) are self-hostable; Luna is closed, cloud-only.

## Pricing Compared (per 1M tokens, verified Sept 10, 2026)

| | **GPT-5.6 Luna** | **GLM-5.3-Flash** | **DeepSeek V4.1 Flash** (`deepseek-flash`) |
|---|---|---|---|
| Input | **$0.20** | **$0.15** | **$0.15** off-peak / $0.30 peak |
| Cached input | $0.02 | $0.03 | $0.003 off-peak / $0.006 peak |
| Output | **$1.20** | **$0.50** | **$0.60** off-peak / $1.20 peak |
| Batch | 50% off (~$0.10/$0.60) | half price ($0.075/$0.25) | — (schedule around peak instead) |
| Time-of-day | flat (surcharge >272K ctx: 2×/1.5×) | points: 0.4× off-peak / 1.2× peak | peak 2× (01:00–04:00, 06:00–10:00 UTC Mon–Fri; ~7h/day; weekends off-peak) |
| Flagship multiple | ~20–25× cheaper than Sol ($4/$30) | ~9× cheaper than GLM-5.3 ($1.40/$4.40) | killed its own Pro (retiring Sept 14) |

Notes: Luna cached input at $0.02 is the cheapest cache in the tier (GLM $0.03; DeepSeek's cache-hit $0.003 off-peak is cheaper still — but DeepSeek's cache discount applies to *repeated* content, AA measured 97% cache discount). Luna carries a >272K-token surcharge (2× input / 1.5× output for the whole request); GLM and DeepSeek don't surcharge long context. DeepSeek's concurrency limit is 2,500 (vs V4 Pro's 500) — the highest of the three documented.

## Specs Compared

| | **Luna** | **GLM-5.3-Flash** | **DeepSeek V4.1 Flash** |
|---|---|---|---|
| Context | 1,050,000 (max out 128K) | 1,048,576 (max out 131K) | 1,000,000 (max out 384K) |
| Weights | closed, cloud-only | **MIT open** (320B-A18B MoE; ~331GB FP8) | **MIT open** (284B-A13B MoE) |
| Multimodal in | text + image | **text + image + video** | text + image (native, V4.1) |
| Reasoning | effort dial: none → max | thinking **mandatory** (max/high/low) | low/high/max effort |
| Measured speed | no hard numbers; "fast at medium effort" | ~84 tok/s avg (up to 458 t/s by provider), TTFT 2.55s | **138.7 tok/s**, TTFT 1.74s |
| Knowledge cutoff | Feb 16, 2026 | — (30T multimodal corpus) | — |

## Benchmarks — With the Right Amount of Skepticism

**Do not compare the numbers below directly across rows.** They come from different index versions and different suites; head-to-head data exists only at community tier.

| Metric | Luna | GLM-5.3-Flash | DeepSeek V4.1 Flash |
|---|---|---|---|
| AA Intelligence Index | 51 (v4.1, max) | 57 (v4.1.1, vendor-claimed) / 41.9 (older AA index via OpenRouter) | 35 (older index, #8/112) |
| AA cost per task | $0.21 | $0.045 (discounted, vendor-claimed) | $0.22 (0731, max effort) |
| Terminal-Bench 2.1 | — | 84.3 | **90.6** (0731: 82.7) |
| DeepSWE v1.1 | — (Coding Agent Index 75) | 63.4 | **74.2** (0731: 54.4) |
| GPQA Diamond | — | 91 | **90.9** |
| ARC-AGI-2 (semi-private) | — | — | **61.4%** @ $0.04/task (vs V4 Pro 61.3% @ $0.60) |
| Agents' Last Exam | beats Claude Fable 5 at "~99% lower cost" (OpenAI claim) | 26.3 | 25.2 |

Reading notes:
- **DeepSeek's own table** (V4.1 Flash vs 0731) is the only verified same-suite improvement set: Terminal-Bench 2.1 +7.9, DeepSWE +19.8, CyberGym +11.4 in six weeks.
- **ARC-AGI is the cleanest cross-tier datapoint:** 0731 Flash matched V4 Pro on ARC-AGI-2 (61.4 vs 61.3) at 1/8–1/14 the cost per task.
- **GLM-5.3-Flash's headline** (AA 57 at $0.045/task, "kicked everything between itself and Sol xhigh out of the Pareto frontier" — HN) is vendor-adjacent; OpenRouter's embedded AA metadata for the same model reads 41.9 on an older index. Both are real AA numbers; versions differ.
- **Community head-to-heads (Tier 3):** on 2× DGX Spark, DeepSeek Flash "comes to conclusions faster and more right" than GLM-5.3-Flash; HumanEval community test slightly favors GLM-5.3-Flash (~92%); Hermes-agent beginners prefer DeepSeek ("explains what it's doing"; GLM needed a tool-calling patch and ignored AGENTS.md in that setup).

## Community Reviews Synthesis (Tier 3)

- **Luna:** *"Luna high is fine for 99% of things"*; excellent at retrieval, classification, finding edge cases; weak at decision-making ("is Luna actually pretty stupid?" — good question, answer: it's effort-dependent); *"similar results to pricier models at ~1/15th the cost"* (HN). OpenRouter traffic: ~1.27T tokens/week, ~37% share, **rank #4 globally** — one of only two US models in a China-dominated top list.
- **GLM-5.3-Flash:** the HN Pareto darling (*"better than the latest DeepSeek v4 Pro while being 3× cheaper in cost per task"*); 95–98% cache-hit-rate praise in ZCode; the viral black-hole Minecraft mod demo. The recurring complaint: **it's slow in wall-clock terms** — mandatory max-effort thinking means ~7× longer per task (*"cheaper, if you don't value your time"*); occasional tool-call looping.
- **DeepSeek Flash:** the practitioners' pick — beginners in Hermes find it "more usable" than GLM-5.3-Flash (explains its actions); DGX Spark local users find it faster and more accurate; V4.1 Flash is claimed to "comprehensively outperform V4 Pro." Skepticism thread exists ("massively overhyped" — contents unretrievable). Aug 16's peak-pricing restructure drew "up to 1,100%" press headlines (vs April flat rates); Sept 10's cut mostly mooted it.

## Decision Guide (Simple Tasks)

- **Highest-volume, latency-sensitive, classification/extraction:** **Luna** — flat pricing, cheapest cache among closed models, no time-window planning, effort dial for control. Avoid xhigh/max unless the task truly needs it (cost and latency balloon).
- **Cheapest intelligence per dollar, open weights, multimodal video input:** **GLM-5.3-Flash** — the Pareto pick on vendor numbers; just budget for wall-clock time (mandatory thinking) and watch for tool-call loops in third-party harnesses; best-in-harness inside ZCode.
- **Lowest absolute price with schedule flexibility (or self-hosting):** **DeepSeek V4.1 Flash** — off-peak rates are the floor of the market ($0.15/$0.60, cache-hit $0.003); cron-friendly batch workloads win big; strongest local-model ecosystem of the three (dual DGX Spark runs 1M context); and note its concurrency limit (2,500) is the highest.
- **If you're inside a subscription:** GLM Flash at 0.4× points off-peak on the GLM Coding Plan is effectively a 2.5× larger allowance than GLM-5.3 for the same plan; Luna is ChatGPT's default for free users.

## Honest Gaps

- **Cross-vendor benchmark comparability is broken:** AA index versions differ (41.9 vs 51 vs 57 across pages); no same-suite public evaluation of all three was found.
- **Luna has no published absolute benchmark scores** (no SWE-bench/GPQA/AIME) — only relative cost-performance claims; no official tok/s either.
- **GLM-5.3-Flash's llm2014 "66.52 logic" number in our own wiki could not be re-verified against the leaderboard** during this research.
- **DeepSeek V4.1 Flash is hours old** — all community data refers to 0731; app/chat availability of V4.1 unconfirmed.
- Peak-window definitions differ (DeepSeek ~7h/day UTC; GLM 20h/week SGT) — direct cost simulation depends on your timezone and workload shape.
- Community quotes are Tier 3 (Reddit/HN via search summaries; direct fetches blocked).

## Related Entries

- [[glm-5-3-flash-vs-deepseek-v4-flash]] ([GLM-5.3 Flash vs DeepSeek V4 Flash](../models/glm-5-3-flash-vs-deepseek-v4-flash.md))
- [[deepseek-v4-peak-pricing]] ([DeepSeek V4 Peak Pricing](../news/deepseek-v4-peak-pricing.md))
- [[gpt-5-6-three-tier-workflow]] ([3-Tier GPT-5.6 Workflow](../tips/gpt-5-6-three-tier-workflow.md))
- [[gpt-5-6-pareto-frontier-copilot]] ([GPT-5.6 Pareto Frontier](../models/gpt-5-6-pareto-frontier-copilot.md))
- [[llm2014-llm-benchmark]] ([llm2014 LLM Benchmark](llm2014-llm-benchmark.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](../tips/anthropic-cost-optimization-cookbook.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[glm-5-3-release]] ([GLM-5.3 Release](../models/glm-5-3-release.md))

---
<!-- RU -->

## Краткое описание

Три модели определяют уровень «дёшево, но способно» на сентябрь 2026: **GPT-5.6 Luna** (нано-тир OpenAI, срезан на 80% до **$0.20/$1.20** за 1M токенов в июле), **GLM-5.3-Flash** (открытая MoE 320B-A18B от Z.ai за **$0.15/$0.50**, вышла 26 августа после скрытной недели под именем «ox-alpha») и **DeepSeek V4.1 Flash** (вышла *сегодня*, 10 сентября, за **$0.15/$0.60 внепик** — релиз настолько силён, что DeepSeek 14 сентября списывает собственный флагман V4 Pro). Все три сошлись у одной цены, но воплощают три философии: закрытые ручки reasoning, открытые веса с прожорливым интеллектом и товарное ценообразование по времени суток. Честный вывод сравнения: **бенчмарки трёх моделей несравнимы между собой** (разные версии индексов и наборы), ценовая война сделала все три смехотворно дешёвыми для простых задач, а реальные различители — настройки effort, токенная эффективность и положение ваших часов относительно пиковых окон.

## Ключевые идеи

- **Ценовая конвергенция через войну цен.** Срезание Luna 30 июля (−80%, «двигаем границу цена-качество») перепозиционировало тир; GLM-5.3-Flash вышла тремя неделями позже за $0.15/$0.50; DeepSeek сегодня ответила, опустив Flash ниже собственных старых внепиковых ставок.
- **~$0.15/$0.50–1.20 за 1M токенов — пол рынка**: в 7–25 раз дешевле флагманов над ними (Sol $4–5/$30; GLM-5.3 $1.40/$4.40; DeepSeek V4 Pro — списывается).
- **Бенчмарки нельзя честно сравнивать между тремя.** Числа Artificial Analysis существуют для всех — но на *разных версиях индекса* (Luna 51 и GLM-Flash 57 на v4.1.x; DeepSeek Flash 35 на старой версии). Прямые сравнения — только уровня сообщества.
- **Ярлык «дёшево/быстро» зависит от effort у всех трёх.** Luna быстра на low/medium, но «умная, но медленная» на xhigh/max; у GLM-5.3-Flash мышление обязательно (нельзя отключить, дефолт = max) и она жжёт ~7× больше токенов на задачу, чем Gemini 3.7 Flash; DeepSeek Flash помечена AA как «очень многословная».
- **Три философии ценообразования:** Luna = плоская цена + batch −50% + надбавка за длинный контекст; GLM = плоская + batch за полцены + очковая подписка (0.4× внепик / 1.2× пик); DeepSeek = электросетевой пик/внепик (пик 2×, ~7 ч/день по будням).
- **Открытые веса: 2 из 3.** GLM-5.3-Flash (320B-A18B, MIT, первая открытая фронтир-модель, комбинирующая linear+sparse attention, нативно мультимодальная) и DeepSeek V4.1 Flash (284B-A13B, MIT, нативное зрение) самохостятся; Luna закрыта, только облако.

## Цены в сравнении (за 1M токенов, верифицировано 10 сентября 2026)

| | **GPT-5.6 Luna** | **GLM-5.3-Flash** | **DeepSeek V4.1 Flash** |
|---|---|---|---|
| Вход | **$0.20** | **$0.15** | **$0.15** внепик / $0.30 пик |
| Кэшированный вход | $0.02 | $0.03 | $0.003 внепик / $0.006 пик |
| Выход | **$1.20** | **$0.50** | **$0.60** внепик / $1.20 пик |
| Batch | −50% (~$0.10/$0.60) | за полцены ($0.075/$0.25) | — (планируйте вокруг пика) |
| Время суток | плоско (надбавка >272K ctx: 2×/1.5×) | очки: 0.4× внепик / 1.2× пик | пик 2× (01:00–04:00, 06:00–10:00 UTC пн–пт) |

Кэш-хит DeepSeek вне пика ($0.003) — самый дешёвый в тире; надбавки за длинный контекст нет у GLM и DeepSeek. Лимит конкурентности DeepSeek — 2 500 (у V4 Pro было 500).

## Спецификации в сравнении

Контекст: Luna 1,050,000 (выход 128K) / GLM 1,048,576 (выход 131K) / DeepSeek 1,000,000 (**выход 384K** — максимум тира). Веса: Luna закрыта; GLM MIT 320B-A18B (~331ГБ FP8); DeepSeek MIT 284B-A13B. Мультимодальный вход: Luna текст+изображение; GLM текст+изображение+видео; DeepSeek текст+изображение (V4.1). Скорость (AA): GLM ~84 tok/s (провайдеры до 458), DeepSeek **138.7 tok/s**, TTFT 1.74s; Luna — официальных цифр нет.

## Бенчмарки — с правильной дозой скепсиса

Не сравнивайте числа из таблицы напрямую между строк: разные версии индексов AA, разные наборы. Прямые сравнения существуют только на уровне сообщества (2× DGX Spark: DeepSeek «приходит к выводам быстрее и правильнее»; HumanEval сообщества чуть в пользу GLM ~92%; новичкам в Hermes DeepSeek «понятнее»).

Единственный верифицированный набор «модель против себя» — DeepSeek V4.1 Flash против 0731 за шесть недель: Terminal-Bench 2.1 82.7→**90.6**, DeepSWE 54.4→**74.2**, CyberGym 76.7→**88.1**. Самая чистая точка кросс-тиров — ARC-AGI-2: 0731 Flash сравнялась с V4 Pro (61.4 против 61.3) при цене за задачу в 1/8–1/14.

## Синтез отзывов сообщества (уровень 3)

**Luna:** «Luna high подходит для 99% задач»; отлична в извлечении и классификации, слаба в принятии решений; «похожие результаты с более дорогими моделями за ~1/15 цены» (HN). Трафик OpenRouter: ~1.27T токенов/неделю, ~37% доля, **#4 в мире** — одна из двух американских моделей в топе, доминируемом китайскими.

**GLM-5.3-Flash:** герой Парето на HN («лучше последней DeepSeek v4 Pro, будучи в 3 раза дешевле по цене за задачу»); похвала 95–98% cache-hit в ZCode; вирусный Minecraft-мод с чёрной дырой. Повторяющаяся жалоба: **медленна в настенных часах** — обязательное max-мышление даёт ~7× дольше на задачу («дешевле, если не дорожите своим временем»); периодические зацикливания tool-call.

**DeepSeek Flash:** выбор практиков — новичкам «понятнее», чем GLM-5.3-Flash; локальные пользователи DGX Spark находят её быстрее и точнее; V4.1 Flash заявлена как «исчерпывающе превосходящая V4 Pro». Есть и тред скептики («сильно переоценена»). Августовская реструктуризация пиковых цен наделала шумихи с заголовками «до 1 100%» (против апрельских плоских ставок); сегодняшнее снижение в основном обесценило вопрос.

## Руководство по выбору (простые задачи)

- **Максимальный объём, чувствительность к задержке, классификация/извлечение:** **Luna** — плоская цена, кэш без планирования окон, диск effort для контроля. Избегайте xhigh/max без необходимости.
- **Минимальная цена за единицу интеллекта, открытые веса, видео-вход:** **GLM-5.3-Flash** — Парето-выбор по вендорским цифрам; но закладывайте настенное время (обязательное мышление) и следите за зацикливанием tool-call в сторонних харнесах; лучше всего — внутри ZCode.
- **Абсолютно минимальная цена при гибкости расписания (или селф-хостинг):** **DeepSeek V4.1 Flash** — внепиковые ставки суть пол рынка ($0.15/$0.60, кэш-хит $0.003); cron-нагрузки выигрывают больше всех; сильнейшая локальная экосистема из трёх (1M контекст на паре DGX Spark); лимит конкурентности 2 500 — высший из трёх.
- **Если вы в подписке:** GLM Flash за 0.4× очков вне пика на GLM Coding Plan — фактически в 2.5 раза большая квота, чем GLM-5.3 на том же плане; Luna — дефолт ChatGPT для бесплатных пользователей.

## Честные пробелы

- **Кросс-вендорская сравнимость бенчмарков нарушена:** версии индекса AA различаются (41.9 против 51 против 57); публичной оценки всех трёх в одном наборе не найдено.
- **У Luna нет опубликованных абсолютных бенчмарков** (нет SWE-bench/GPQA/AIME) — только относительные заявления о цене-качестве; официальных tok/s тоже нет.
- **Число llm2014 «66.52 logic» для GLM-5.3-Flash в нашей вики не удалось переверифицировать** по лидерборду в ходе этого исследования.
- **DeepSeek V4.1 Flash существует несколько часов** — все данные сообщества относятся к 0731; доступность V4.1 в приложении не подтверждена.
- Определения пиковых окон различаются (DeepSeek ~7ч/день UTC; GLM 20ч/неделю SGT) — прямой расчёт стоимости зависит от вашего часового пояса и формы нагрузки.
- Цитаты сообщества — уровень 3 (Reddit/HN через поисковые выдержки).

## Связанные записи

- [[glm-5-3-flash-vs-deepseek-v4-flash]] ([GLM-5.3 Flash vs DeepSeek V4 Flash](../models/glm-5-3-flash-vs-deepseek-v4-flash.md))
- [[deepseek-v4-peak-pricing]] ([DeepSeek V4 Peak Pricing](../news/deepseek-v4-peak-pricing.md))
- [[gpt-5-6-three-tier-workflow]] ([3-Tier GPT-5.6 Workflow](../tips/gpt-5-6-three-tier-workflow.md))
- [[gpt-5-6-pareto-frontier-copilot]] ([GPT-5.6 Pareto Frontier](../models/gpt-5-6-pareto-frontier-copilot.md))
- [[llm2014-llm-benchmark]] ([llm2014 LLM Benchmark](llm2014-llm-benchmark.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](../tips/anthropic-cost-optimization-cookbook.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[glm-5-3-release]] ([GLM-5.3 Release](../models/glm-5-3-release.md))
