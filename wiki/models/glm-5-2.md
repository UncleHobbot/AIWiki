---
title: "GLM-5.2: Z.AI's 1M-Context Coding Model"
title_ru: "GLM-5.2: кодинговая модель Z.AI с контекстом 1M"
category: models
tags: [glm, zai, chinese-llm, coding, open-source, 1m-context]
date: 2026-06-13
updated: 2026-07-01
sources:
  - https://docs.z.ai/devpack/latest-model.md
  - https://digg.com/tech/ii9xibgn
  - https://www.ithome.com/0/963/855.htm
  - https://codersera.com/blog/glm-5-2-release-1m-context-coding-2026/
  - https://www.reddit.com/r/opencodeCLI/comments/1u4z06y/glm52_by_zai_is_now_on_opencode/
  - https://www.reddit.com/r/ZaiGLM/comments/1uje356/glm52_failing_with_method_not_allowed_405_in/
  - https://www.reddit.com/r/ZaiGLM/comments/1ujhvpq/is_glm_52_really_that_good_or_too_sugarcoat/
---

## Summary

Z.AI released GLM-5.2 on June 13, 2026, as its newest coding-oriented model with a 1 million token context window and High/Max thinking modes. Open weights under MIT license were promised for the following week. As of launch, no benchmark scores (BenchLM, SWE-bench, LiveCodeBench, math) or architecture details have been published; the main verified improvement over GLM-5.1 is 5× larger context.

## Key Ideas

- **1 million token context window** — 5× larger than GLM-5.1, aimed at long files, multi-repo sessions, and large diffs.
- **Coding-first positioning** — bundled inside GLM Coding Plan tiers rather than the general GLM-5 family.
- **High/Max thinking modes** — users can choose deeper reasoning levels, similar to other recent coding models.
- **Open weights promised** — MIT-licensed weights slated for release the week after launch; not available on day one.
- **No published benchmarks at launch** — BenchLM, SWE-bench, LiveCodeBench, and math scores were not shared, and no architecture paper or technical report accompanied the release.
- **Main upgrade vs GLM-5.1** — context length; all other claims about quality await independent verification.

## Details

GLM-5.2 arrives as Z.AI continues to position the GLM family as a low-cost alternative for coding agents. The 1M context window matches the largest announced context sizes in the market and is the clearest differentiator from GLM-5.1. The model is offered through the GLM Coding Plan subscription tiers, which bundle API access and higher rate limits.

Z.AI committed to releasing open weights under the MIT license "next week," but the exact date and parameter count were not specified at launch. The announcement did not include a technical report, model card, or any benchmark table. Community reception has been cautious: the larger context is welcome, but without SWE-bench or LiveCodeBench scores it is difficult to compare GLM-5.2 with DeepSeek-Coder, Qwen-Coder, Kimi K2.7 Code, or Western models such as GPT-5.5 and Claude Opus 4.8.

## Pricing

GLM-5.2 is bundled with the GLM Coding Plan subscription tiers; there is no separate per-token API price at launch.

| Plan | Monthly Price | Prompts / Week | Notes |
|------|---------------|----------------|-------|
| Lite | ~$18 | ~400 | Entry tier, limited quota |
| Pro | higher | ~2,000 | Mid-tier for active users |
| Max | higher | ~8,000 | Highest individual quota |
| Team | seat-based | organization | Multi-seat billing |

Quota consumption: GLM-5.2 counts as an advanced model at **3× peak / 2× off-peak** prompt quota, but through end of September 2026 it is billed at **1× off-peak** for GLM-5.2 and GLM-5-Turbo. Standalone API pricing and OpenRouter availability are expected after the open-weight release.

Until independent evaluations appear, treat GLM-5.2 as a context expansion release rather than a proven leap in coding capability.

## Adoption Update (June 14, 2026)

GLM-5.2 became available in OpenCode via the Z.ai provider within a day of release. Early community first impressions (r/opencodeCLI, Tier 3 — unverified): "snappy" performance through the Z.ai provider, good results on smaller coding tasks, and the 1M context window cited as a real practical win — though still no formal benchmark comparisons.

## Community Reception (late June 2026)

- **ZCode 405 errors:** multiple r/ZaiGLM users report GLM-5.2 failing in ZCode with a persistent `405 Method Not Allowed` on every request, unresolved by restart/relogin — possibly tied to plan tier (`start-plan`). (Tier 3 community report.)
- **"Is it really that good?":** an r/ZaiGLM thread asks whether GLM-5.2 genuinely reaches Claude Code / Codex-level for serious product engineering, or whether hype is ahead of reality — a signal that real-world verdict is still mixed.
- See also [[closed-vs-open-model-scaffolding-gap]] for the argument that GLM-5.2's benchmark gap vs Claude may partly be a *scaffolding* gap, not a model gap.

## Related Entries

- [[kimi-k2-7-code]] ([Kimi K2.7 Code](./kimi-k2-7-code.md))
- [[glm-5-1]] ([GLM-5.1](glm-5-1.md))
- [[closed-vs-open-model-scaffolding-gap]] ([Closed vs Open Scaffolding Gap](../concepts/closed-vs-open-model-scaffolding-gap.md))
- [[zcode-zai-agentic-development-environment]] ([ZCode — Z.ai's Agentic Development Environment](../research/zcode-zai-agentic-development-environment.md))
- GLM Coding Plan ([Z.AI GLM Coding Plan](../tools/zai-glm-coding-plan.md))

---
- [[glm-5-2-nested-tool-call-bug]] ([GLM-5.2 Nested Tool-Call Bug](../news/glm-5-2-nested-tool-call-bug.md))
- [[llm2014-llm-benchmark]] ([llm2014 LLM Benchmark](../research/llm2014-llm-benchmark.md))
<!-- RU -->

## Краткое описание

Z.AI выпустила GLM-5.2 13 июня 2026 года — новейшую модель, ориентированную на кодинг, с контекстным окном 1 миллион токенов и режимами рассуждения High/Max. Открытые веса по лицензии MIT обещаны на следующей неделе. На момент запуска не опубликованы оценки бенчмарков (BenchLM, SWE-bench, LiveCodeBench, математика) и детали архитектуры; главное подтверждённое улучшение по сравнению с GLM-5.1 — контекст в 5 раз больше.

## Ключевые идеи

- **Контекстное окно 1 миллион токенов** — в 5 раз больше, чем у GLM-5.1, для длинных файлов, мультирепозиторных сессий и больших diff.
- **Позиционирование как кодинговая модель** — входит в тарифы GLM Coding Plan, а не в общую линейку GLM-5.
- **Режимы рассуждения High/Max** — пользователь может выбрать более глубокий уровень reasoning, как в других недавних кодинговых моделях.
- **Открытые веса обещаны** — веса под лицензией MIT планируются на неделю после запуска; в день релиза недоступны.
- **Нет опубликованных бенчмарков** — не представлены оценки BenchLM, SWE-bench, LiveCodeBench и математики, а также технический отчёт или архитектурные детали.
- **Главное улучшение по сравнению с GLM-5.1** — длина контекста; все остальные заявления о качестве требуют независимой проверки.

## Подробнее

GLM-5.2 появляется на фоне продолжающейся игры Z.AI по позиционированию семейства GLM как недорогой альтернативы для coding-агентов. Контекстное окно 1M приравнивается к крупнейшим заявленным размерам на рынке и является самым явным отличием от GLM-5.1. Модель предлагается через подписочные тарифы GLM Coding Plan, которые включают доступ к API и повышенные лимиты.

Z.AI обязалась выпустить открытые веса под лицензией MIT «на следующей неделе», но точная дата и размер модели в день запуска не названы. Анонс не содержал технического отчёта, карточки модели или таблицы бенчмарков. Реакция сообщества осторожная: увеличенный контекст приветствуется, но без оценок SWE-bench и LiveCodeBench сложно сравнить GLM-5.2 с DeepSeek-Coder, Qwen-Coder, Kimi K2.7 Code или западными моделями вроде GPT-5.5 и Claude Opus 4.8.

## Ценообразование

GLM-5.2 входит в подписочные тарифы GLM Coding Plan; отдельной цены за токены API на старте нет.

| Тариф | Цена в месяц | Количество промптов / неделю | Примечания |
|-------|---------------|----------------|-------|
| Lite | ~$18 | ~400 | Стартовый уровень, ограниченная квота |
| Pro | выше | ~2,000 | Средний уровень для активных пользователей |
| Max | выше | ~8,000 | Максимальная индивидуальная квота |
| Team | за место | организация | Многопользовательское биллирование |

Потребление квоты: GLM-5.2 считается продвинутой моделью с расходом **3× в пик / 2× вне пика**, но до конца сентября 2026 года для GLM-5.2 и GLM-5-Turbo действует тариф **1× вне пика**. Автономное API-ценообразование и появление на OpenRouter ожидаются после выпуска открытых весей.

До появления независимых оценок GLM-5.2 стоит рассматривать как релиз расширения контекста, а не доказанный скачок в кодинговых способностях.

## Обновление по внедрению (14 июня 2026)

GLM-5.2 стала доступна в OpenCode через провайдера Z.ai в течение суток после релиза. Первые впечатления сообщества (r/opencodeCLI, tier 3 — не проверено): "отзывчивая" работа через провайдера Z.ai, хорошие результаты на небольших задачах кодинга, контекст 1M токенов отмечен как реальное практическое преимущество — хотя формальных бенчмарк-сравнений пока нет.

## Реакция сообщества (конец июня 2026)

- **Ошибки 405 в ZCode:** несколько пользователей r/ZaiGLM сообщают, что GLM-5.2 в ZCode падает с постоянной `405 Method Not Allowed` на каждый запрос, не чинится перезапуском/перелогином — возможно, привязано к тарифу (`start-plan`). (Уровень 3, сообщество.)
- **«Действительно ли она так хороша?»:** тред в r/ZaiGLM спрашивает, действительно ли GLM-5.2 дотягивает до уровня Claude Code / Codex для серьёзной продуктовой разработки, или хайп опережает реальность — сигнал, что реальный вердикт пока смешанный.
- См. также [[closed-vs-open-model-scaffolding-gap]] — аргумент, что разрыв GLM-5.2 vs Claude в бенчмарках может быть частично разрывом в *scaffolding*, а не в модели.

## Связанные записи

- [[kimi-k2-7-code]] ([Kimi K2.7 Code](./kimi-k2-7-code.md))
- [[glm-5-1]] ([GLM-5.1](glm-5-1.md))
- GLM Coding Plan ([Z.AI GLM Coding Plan](../tools/zai-glm-coding-plan.md))
