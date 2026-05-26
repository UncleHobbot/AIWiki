---
title: "Ollama Cloud Quality Concerns"
title_ru: "Проблемы качества Ollama Cloud"
category: news
tags: [ollama, cloud, quality, quantization, llm]
date: 2026-05-26
updated: 2026-05-26
sources:
  - https://www.reddit.com/r/ollama/comments/1teas3p/is_ollama_cloud_using_1bit_quants_this_coherence/
  - https://www.reddit.com/r/ollama/comments/1te861w/i_built_ollamatpscom_to_compare_ollama_cloud/
---

## Summary
Users report severe quality degradation in Ollama Cloud model outputs, with models producing incoherent responses. A community-built benchmarking tool (ollamatps.com) reveals significant performance variability across hosted models.

## Key Ideas
- GLM-5.1 on Ollama Cloud produced completely incoherent output: one word per line, repeating "Wait" and "Actually", unable to maintain a train of thought
- Community suspects aggressive quantization (possibly Q1-level) or fundamental infrastructure issues rather than just quantization
- Users face potential banning for criticizing the service publicly, raising trust concerns
- ollamatps.com benchmarks show GLM-4.7 leading at 93 TPS with good intelligence, while Kimi K2.6 lags at ~32 TPS
- 24h TPS tracking reveals that cloud-hosted LLM services can silently degrade model quality without user transparency

## Details
A Reddit post from r/ollama documented GLM-5.1 outputting one word per line and looping on filler phrases like "Wait" and "Actually." The user questioned whether Ollama Cloud was using extreme 1-bit quantization. Top-voted comments suggested the issue is not merely quantization but something fundamentally broken in the serving infrastructure. One commenter noted a broader risk of LLM cloud hosting: providers can host models at arbitrarily low quantization levels (Q1) without disclosing it.

Separately, a community member built ollamatps.com to track 24-hour tokens-per-second benchmarks across Ollama Cloud models. The data shows wide variance: GLM-4.7 achieves 93 TPS with strong intelligence scores, while Kimi K2.6 runs at ~32 TPS. The tool aims to give users objective performance data for model selection.

These reports highlight a transparency gap in cloud LLM services — users cannot verify what quantization or optimization level is actually being served.

## Notable Quotes
> "You'll be banned for posting the truth about that scam service" — Reddit commenter (10 pts)
> "Something is just broken there; not a quant problem" — Reddit commenter (4 pts)
> "This is the problem with all types of LLM cloud hosting they can just host their models at Q1" — Reddit commenter (1 pt)

## Related Entries
- [[product-ollama]] ([Ollama Cloud](../tools/product-ollama.md))

---
<!-- RU -->

## Краткое описание
Пользователи сообщают о серьёзной деградации качества моделей на Ollama Cloud — модели выдают бессвязные ответы. Созданный сообществом инструмент бенчмаркинга (ollamatps.com) выявляет значительную вариативность производительности среди размещённых моделей.

## Ключевые идеи
- GLM-5.1 на Ollama Cloud выдавал полностью бессвязный вывод: по одному слову на строку, повторение «Wait» и «Actually», неспособность удерживать мысль
- Сообщество подозревает агрессивную квантизацию (возможно, уровня Q1) или фундаментальные проблемы инфраструктуры
- Пользователи сталкиваются с потенциальной блокировкой за публичную критику сервиса, что вызывает вопросы доверия
- Бенчмарки ollamatps.com показывают, что GLM-4.7 лидирует с 93 TPS при хорошем интеллекте, тогда как Kimi K2.6 отстаёт с ~32 TPS
- Мониторинг TPS за 24 часа показывает, что облачные LLM-сервисы могут незаметно снижать качество моделей без информирования пользователей

## Подробнее
Пост на Reddit в r/ollama задокументировал, что GLM-5.1 выдаёт по одному слову на строку и зацикливается на фразах-заполнителях вроде «Wait» и «Actually». Пользователь предположил, что Ollama Cloud использует экстремальную 1-битную квантизацию. Наиболее рейтинговые комментарии указывают, что проблема не только в квантизации, а в чём-то фундаментально сломанном в обслуживающей инфраструктуре. Один из комментаторов отметил более широкий риск облачного хостинга LLM: провайдеры могут размещать модели на произвольно низких уровнях квантизации (Q1), не раскрывая этого.

Отдельно участник сообщества создал ollamatps.com для отслеживания 24-часовых бенчмарков токенов в секунду по моделям Ollama Cloud. Данные показывают значительный разброс: GLM-4.7 достигает 93 TPS с высокими оценками интеллекта, а Kimi K2.6 работает на ~32 TPS. Инструмент призван дать пользователям объективные данные для выбора модели.

Эти сообщения подчёркивают разрыв в прозрачности облачных LLM-сервисов — пользователи не могут проверить, какой уровень квантизации или оптимизации фактически используется.

## Примечательные цитаты
> «Вас забанят за публикацию правды об этом мошенническом сервисе» — комментатор Reddit (10 pts)
> «Там что-то просто сломано; это не проблема квантизации» — комментатор Reddit (4 pts)
> «В этом и проблема всех видов облачного хостинга LLM — они могут просто размещать модели на Q1» — комментатор Reddit (1 pt)

## Связанные записи
- [[product-ollama]] ([Ollama Cloud](../tools/product-ollama.md))
