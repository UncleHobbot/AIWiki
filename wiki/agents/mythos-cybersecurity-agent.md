---
title: "Mythos: AI Cybersecurity Agent"
title_ru: "Mythos: ИИ-агент кибербезопасности"
category: agents
tags: [mythos, cybersecurity, hacking, agent, llm]
aliases: [Mythos, Claude Mythos, Mythos Preview, Anthropic cybersecurity model]
confidence: high
date: 2026-05-15
updated: 2026-05-15
sources:
  - https://www.reddit.com/r/singularity/comments/1te51wg/more_evidence_of_mythoss_strength_in/
  - https://www.reddit.com/r/singularity/comments/1tc9dwx/new_mythos_checkpoint_shows_continued_improvement/
  - https://www.reddit.com/r/singularity/comments/1td97gj/the_first_public_macos_kernel_memory_corruption/
  - https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
  - https://blog.calif.io/p/first-public-kernel-memory-corruption
  - https://www.mindstudio.ai/blog/claude-mythos-gpt-5-5-last-ones-cyberattack-benchmark-results/
---

## Summary

Claude Mythos Preview is Anthropic's frontier AI model positioned above Opus in their model hierarchy, and the first AI to autonomously complete a full 32-step simulated corporate network attack. It scores 83.1% on cybersecurity benchmarks and has already helped researchers build the first public macOS kernel exploit on Apple M5 hardware.

## Key Ideas

- First AI to solve AISI's "The Last Ones" (TLO) benchmark end-to-end: a 32-step corporate network attack simulation estimated to take human experts ~20 hours. Mythos completed it in 3 out of 10 attempts initially, and a newer checkpoint achieved 6 out of 10.
- Achieved 18/41 n-day exploits in vulnerability testing, compared to 1/41 for the previous generation (Claude 5.5). Open-source/weight models scored zero.
- Succeeded on 73% of expert-level Capture the Flag (CTF) challenges — tasks that no model could complete before April 2025.
- Helped security researchers at Calif build the first public macOS kernel memory corruption exploit on Apple M5, bypassing Apple's MIE (Memory Integrity Enforcement) hardware mitigation, in just 5 days.
- Found a 27-year-old OpenBSD vulnerability during testing — a bug that survived decades of security audits.
- GPT-5.5 later matched Mythos with 2/10 completions on TLO, confirming Mythos was a leading indicator rather than an anomaly.

## Details

Mythos Preview sits in a new model tier above Opus in Anthropic's lineup (Haiku, Sonnet, Opus, Mythos). Announced April 7, 2026, it was independently evaluated by the UK AI Security Institute (AISI), a government-backed body. AISI found it represents a significant step up over all previous frontier models in cybersecurity capability.

The AISI "The Last Ones" benchmark simulates a full corporate network intrusion: reconnaissance, lateral movement, privilege escalation, and persistence across dozens of hosts and network segments. Mythos completed the entire chain in 3 of 10 attempts. With a newer checkpoint, that rose to 6 of 10. Performance continues to scale with more inference compute, suggesting the limits have not yet been reached. A subsequent reverse-engineering challenge that would take a human ~12 hours was solved by GPT-5.5 in 10 minutes for $1.73, illustrating the collapsing cost of AI-driven attacks.

In real-world impact, security firm Calif used Mythos Preview to help discover and exploit a kernel memory corruption vulnerability on macOS 26.4.1 targeting bare-metal Apple M5 hardware with MIE enabled. The exploit chain — a local privilege escalation from unprivileged user to root — was developed in roughly one week. Mythos identified the bugs quickly because they belonged to known vulnerability classes, then generalized its approach to the new MIE mitigation. The 55-page technical report will be published after Apple ships a fix.

The White House blocked Anthropic's plan to expand Mythos access from ~50 to 120 organizations, citing national security and compute scarcity concerns. Anthropic has disputed the compute limitation, pointing to deals with Amazon, Google, and Broadcom for capacity expansion.

## Notable Quotes

> "This work is a glimpse of what is coming. Apple built MIE in a world before Mythos Preview. We're about to learn how the best mitigation technology on Earth holds up during the first AI bugmageddon." — Calif security researchers

> "The cost of failure is zero. The cost of success is whatever the attacker wanted." — MindStudio analysis of AISI benchmark results

## Related Entries

- [[apple-m5-kernel-exploit-ai]]

---
<!-- RU -->

## Краткое описание

Claude Mythos Preview — флагманская модель Anthropic нового класса (выше Opus), ставшая первым ИИ, автономно завершившим полноцепочную 32-шаговую симуляцию атаки на корпоративную сеть. Набирает 83,1% на бенчмарках по кибербезопасности и уже помогла исследователям создать первый публичный kernel-эксплойт для macOS на процессоре Apple M5.

## Ключевые идеи

- Первый ИИ, решивший бенчмарк AISI «The Last Ones» (TLO) от начала до конца: 32-шаговая симуляция атаки на корпоративную сеть, на которую у человека-эксперта уходит ~20 часов. Mythos завершил её в 3 из 10 попыток изначально, а новый checkpoint — в 6 из 10.
- Получил 18/41 n-day эксплойтов при тестировании уязвимостей, против 1/41 у предыдущего поколения (Claude 5.5). Открытые модели — ноль.
- Успешно справился с 73% экспертных CTF-задач (Capture the Flag) — задач, с которыми ни одна модель не могла справиться до апреля 2025 года.
- Помог исследователям безопасности из Calif создать первый публичный kernel-эксплойт memory corruption для macOS на Apple M5, обойдя аппаратную защиту MIE (Memory Integrity Enforcement), всего за 5 дней.
- Обнаружил 27-летнюю уязвимость в OpenBSD — баг, который пережил десятилетия аудитов безопасности.
- GPT-5.5 впоследствии повторил результат Mythos (2/10 на TLO), подтвердив, что Mythos был индикатором тренда, а не аномалией.

## Подробнее

Mythos Preview занимает новый уровень в линейке Anthropic — выше Opus (Haiku, Sonnet, Opus, Mythos). Модель, анонсированная 7 апреля 2026 года, прошла независимую оценку в британском AISI (AI Security Institute) — правительственном институте безопасности ИИ. AISI установил, что модель представляет существенный скачок по сравнению со всеми предыдущими frontier-моделями в кибер-возможностях.

Бенчмарк AISI «The Last Ones» симулирует полномасштабное вторжение в корпоративную сеть: разведка, латеральное перемещение, повышение привилегий и закрепление на десятках хостов и сетевых сегментов. Mythos завершил полную цепочку в 3 из 10 попыток; с новым checkpoint — 6 из 10. Производительность продолжает расти с увеличением inference-вычислений, что говорит о том, что предел ещё не достигнут. Последующая задача по reverse engineering, занявшая бы у человека ~12 часов, была решена GPT-5.5 за 10 минут за $1,73 — наглядная иллюстрация обрушения стоимости ИИ-атак.

В реальном применении компания Calif использовала Mythos Preview для обнаружения и эксплуатации уязвимости kernel memory corruption в macOS 26.4.1 на «железе» Apple M5 с включённой защитой MIE. Цепочка эксплойта — локальное повышение привилегий от обычного пользователя до root — была разработана примерно за неделю. Mythos быстро обнаружил баги, поскольку они относились к известным классам уязвимостей, а затем обобщил свой подход к новой защите MIE. Полный 55-страничный технический отчёт будет опубликован после выпуска исправления от Apple.

Белый дом заблокировал план Anthropic по расширению доступа к Mythos с ~50 до 120 организаций, сославшись на вопросы национальной безопасности и дефицит вычислительных мощностей. Anthropic оспорил утверждение о нехватке compute, указав на соглашения с Amazon, Google и Broadcom о наращивании мощностей.

## Примечательные цитаты

> «Эта работа — проблеск того, что грядёт. Apple создала MIE в мире до Mythos Preview. Нам предстоит узнать, как лучшая на Земле технология защиты выдержит первый ИИ-багмагеддон.» — Исследователи безопасности Calif

> «Стоимость неудачи — ноль. Стоимость успеха — всё, что хотел атакующий.» — Анализ MindStudio результатов бенчмарка AISI

## Связанные записи

- [[apple-m5-kernel-exploit-ai]]
