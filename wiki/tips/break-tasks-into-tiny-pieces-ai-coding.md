---
title: "Break It Into Tiny Pieces: The Real Lesson from a Month-Long AI-Coded Game"
title_ru: "Разбивай на мелкие части: главный урок месячного проекта с AI-кодингом"
category: tips
tags: [vibe-coding, claude-code, codex, workflow, task-decomposition]
aliases: [tiny self-contained pieces, AI coding decomposition]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/vibecoding/comments/1u5jfrq/built_a_lights_outstyle_puzzle_game_mostly_with/
---

## Summary
A developer spent a month building a Lights Out-style puzzle game (~70% ChatGPT Codex, ~30% Claude Code) and found the single biggest factor in output quality wasn't the AI's raw capability — it was whether the work was broken into tiny, self-contained pieces versus asked for as a whole "product."

## Key Ideas
- Asking AI tools to "build the product" as a single ask produced poor results, even with capable models (Codex, Claude Code).
- Breaking the same work into tiny, self-contained pieces produced surprisingly good results — "surprisingly far" for a non-professional solo project.
- The project (Darkenn) is a non-trivial full-stack app: JS/CSS frontend, Supabase + Edge Functions backend with RLS, Google OAuth/Twitch auth, Cloudflare hosting/CDN, GitHub version control.
- The game logic itself involves real math (linear algebra over GF(2)) with a solver computing minimum-move solutions — not a toy example.
- Different AI tools were used for different layers: ChatGPT Codex for most of the code, Claude Code for the remainder, plus ChatGPT for custom icon assets.

## Details
This is a small but concrete data point in the recurring "how to actually get good output from AI coding agents" discussion. The author frames it explicitly as a before/after: large, vague asks ("build the product") degraded quickly, while decomposing the same overall scope into small, independently-completable, self-contained tasks let the agents perform much closer to their ceiling. This aligns with the general spec-driven development pattern (propose → spec → design → tasks → apply) seen elsewhere in this wiki — the "tasks" step being exactly this decomposition.

Notably, the project mixed two different agentic coding tools (Codex and Claude Code) across the same codebase without apparent friction, suggesting tool-switching by task type is viable as long as the underlying task units are small and well-scoped. The full stack (Supabase RLS, OAuth, Cloudflare CDN, GF(2) linear algebra solver) indicates this wasn't a trivial CRUD app — making the "small tasks work, big asks don't" lesson more credible than it would be from a toy example.

## Related Entries
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World](../tips/spec-driven-development-bmad.md))
- [[github-spec-kit]] ([GitHub Spec-Kit: Spec-Driven Development Toolkit](../tools/github-spec-kit.md))
- [[specs-to-production-ai-agents]] ([From Specs to Production: Building Software with AI Agents End to End](../agents/specs-to-production-ai-agents.md))

---
<!-- RU -->

## Краткое описание
Разработчик потратил месяц на создание игры-головоломки в стиле Lights Out (~70% ChatGPT Codex, ~30% Claude Code) и обнаружил, что главным фактором качества результата была не сырая способность AI, а то, разбита ли работа на мелкие самодостаточные части или запрошена как единый "продукт".

## Ключевые идеи
- Запрос к AI-инструментам "построить продукт" целиком давал плохие результаты, даже с мощными моделями (Codex, Claude Code).
- Разбивка той же работы на мелкие самодостаточные части дала удивительно хорошие результаты — "удивительно далеко" для непрофессионального соло-проекта.
- Проект (Darkenn) — нетривиальное full-stack приложение: фронтенд на JS/CSS, бэкенд Supabase + Edge Functions с RLS, авторизация Google OAuth/Twitch, хостинг и CDN на Cloudflare, версионирование в GitHub.
- Сама игровая логика основана на реальной математике (линейная алгебра над GF(2)), а решатель вычисляет решение с минимальным числом ходов — не игрушечный пример.
- Разные AI-инструменты использовались для разных слоёв: ChatGPT Codex — для основной части кода, Claude Code — для остального, ChatGPT — для кастомных иконок.

## Подробнее
Это небольшой, но конкретный пример в продолжающейся дискуссии "как на самом деле получить хороший результат от AI coding-агентов". Автор явно описывает это как "до и после": крупные, размытые запросы ("построй продукт") быстро ухудшали качество, а разбивка того же общего объёма работы на мелкие, независимо выполнимые, самодостаточные задачи позволила агентам работать значительно ближе к своему потолку. Это согласуется с общим паттерном spec-driven development (propose → spec → design → tasks → apply), встречающимся в других записях этой wiki — шаг "tasks" и есть именно эта декомпозиция.

Примечательно, что проект использовал два разных агентных coding-инструмента (Codex и Claude Code) в одной кодовой базе без видимых проблем — это говорит о том, что переключение инструментов по типу задачи работоспособно, если базовые единицы задач остаются маленькими и хорошо определёнными. Полный стек (Supabase RLS, OAuth, Cloudflare CDN, решатель линейной алгебры над GF(2)) показывает, что это не было тривиальное CRUD-приложение — что делает урок "маленькие задачи работают, большие запросы — нет" более убедительным, чем на игрушечном примере.

## Связанные записи
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World](../tips/spec-driven-development-bmad.md))
- [[github-spec-kit]] ([GitHub Spec-Kit: Spec-Driven Development Toolkit](../tools/github-spec-kit.md))
- [[specs-to-production-ai-agents]] ([From Specs to Production: Building Software with AI Agents End to End](../agents/specs-to-production-ai-agents.md))
