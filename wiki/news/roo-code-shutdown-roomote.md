---
title: "Roo Code Shuts Down After 3M Installs, Pivots to Roomote"
title_ru: "Roo Code закрывается после 3 млн установок, переходит на Roomote"
category: news
tags: [roo-code, roomote, coding-agent, shutdown, pivot]
date: 2026-05-15
updated: 2026-05-15
sources:
  - https://www.reddit.com/r/ChatGPTCoding/comments/1sru5zr/roo_code_hit_3_million_installs_were_shutting_it/
  - https://x.com/mattrubens/status/2046636598859559114
  - https://thenewstack.io/roo-code-cloud-ides-ai-coding/
---

## Summary
Roo Code, the popular VS Code coding agent extension that reached 3 million installs, is shutting down on May 15, 2026. Founder Matt Rubens announced the team is pivoting entirely to Roomote, a cloud-based autonomous coding agent that lives in Slack and acts as a "teammate" rather than an IDE tool.

## Key Ideas
- Roo Code reached 3 million installs and 23K GitHub stars before being shut down on May 15, 2026
- The pivot was driven by the team's internal shift to running Roo Code headlessly in cloud containers, finding the IDE-based model no longer optimal
- Roomote is a Slack-native cloud agent that integrates with Linear, GitHub, Sentry and verifies its own work with screenshots
- The shutdown is not a failure — the team concluded that the IDE extension market was converging and being commoditized by first-party tools and forks
- Cline has absorbed many Roo Code features and is recommended as the migration path for extension users

## Details
Roo Code started in late 2024 as a fork of Cline, adding features like dangerously-skip-permissions and agentic coding workflows. It quickly gained traction, reaching 3 million installs and building a passionate community. However, by Fall 2025 the team noticed their own internal workflow had shifted fundamentally: they were running Roo Code headlessly in cloud containers with full auto-approve, parallelizing work across hundreds of PRs and issues. The pattern became "prompt in, high-quality PR out" — removing the need for IDE interaction entirely.

Matt Rubens explained that the IDE extension space was becoming commoditized. Models improved, interfaces converged, first-party tools became "discount token ATMs," and forks redistributed Roo Code's work as fast as they shipped it. Rather than compete in a shrinking differentiation window, the team chose to go all-in on their cloud-first approach.

Roomote, the successor product, is a cloud-based agent that lives in Slack alongside the rest of the team. It integrates with tools like Linear, GitHub, and Sentry, runs whichever frontier model fits the job, and verifies its own work using screenshots and a full local environment. Notably, Roomote targets not just engineers but also PMs, support teams, ops, marketers, and founders — anyone who can describe a task and get a real PR back.

The Roo Code GitHub repo was archived on May 15, 2026, with unused paid service balances refunded. Users needing an IDE extension are directed to Cline, which has incorporated many Roo Code features.

## Related Entries
- [[cline-roo-alternatives]]
- [[github-copilot-pricing-exodus]]

---
<!-- RU -->

## Краткое описание
Roo Code, популярное расширение VS Code для coding agent с 3 млн установок, закрывается 15 мая 2026 года. Основатель Мэтт Рубенс объявил о полном переходе команды на Roomote — облачного автономного coding agent, работающего в Slack как «чаймейт», а не как инструмент в IDE.

## Ключевые идеи
- Roo Code достиг 3 млн установок и 23K звёзд на GitHub перед закрытием 15 мая 2026
- Pivot обусловлен внутренним переходом команды на headless-режим в облачных контейнерах — IDE-модель перестала быть оптимальной
- Roomote — облачный agent в Slack, интегрируется с Linear, GitHub, Sentry и верифицирует свою работу скриншотами
- Закрытие не является провалом — команда пришла к выводу, что рынок IDE-расширений коммодитизируется первичными инструментами и форками
- Cline поглотил многие функции Roo Code и рекомендован как путь миграции для пользователей расширения

## Подробнее
Roo Code появился в конце 2024 года как форк Cline, добавив функции вроде dangerously-skip-permissions и agentic-режима работы. Расширение быстро набрало популярность — 3 млн установок и преданное сообщество. Однако к осени 2025 года команда обнаружила, что их собственный рабочий процесс кардинально изменился: они запускали Roo Code headless в облачных контейнерах с полным auto-approve, распараллеливая работу по сотням PR и issues. Паттерн стал «prompt на входе — качественный PR на выходе», что полностью исключило необходимость взаимодействия через IDE.

Мэтт Рубенс пояснил, что пространство IDE-расширений коммодитизируется. Модели улучшаются, интерфейсы конвергируют, первичные инструменты превращаются в «дискаунт-автоматы для токенов», а форки распространяют наработки Roo Code быстрее, чем команда успевала их выпускать. Вместо конкуренции в сужающемся окне дифференциации, команда решила вложить все ресурсы в облачный подход.

Roomote — продукт-наследник, облачный coding agent, работающий прямо в Slack рядом с остальной командой. Он интегрируется с Linear, GitHub, Sentry, запускает подходящую frontier-модель и верифицирует свою работу через скриншоты и полную локальную среду. Важно, что Roomote нацелен не только на инженеров, но и на продакт-менеджеров, саппорт, ops, маркетологов и основателей — любой, кто может описать задачу, получает готовый PR.

Репозиторий Roo Code на GitHub был архивирован 15 мая 2026 года, неиспользованные балансы платных сервисов возвращены. Пользователям, нуждающимся в IDE-расширении, рекомендуется Cline, который перенял множество функций Roo Code.

## Связанные записи
- [[cline-roo-alternatives]]
- [[github-copilot-pricing-exodus]]
