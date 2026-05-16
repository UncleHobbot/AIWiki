---
title: "Claude Code Skill Frameworks: GSD, Superpowers, Ouroboros, Han"
title_ru: "Фреймворки навыков Claude Code: GSD, Superpowers, Ouroboros, Han"
category: tools
tags: [claude-code, skills, frameworks, plugins, superpowers, han, ouroboros, workflow]
updated: 2026-05-16
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1te6oti/whats_the_best_claude_code_framework_and_do_you/
---

## Summary
The Claude Code community has produced several competing skill frameworks (sets of pre-built skills, agents, and workflows packaged as plugins). GSD, Superpowers, and Ouroboros are widely cited; Han (from testdouble) takes a lighter "choose your own adventure" approach. All are optional — only add one when you hit the limits of raw Claude Code.

## Key Ideas
- **When you need a framework**: only if you're hitting the limits of the model + built-in plan/build modes, or if you're constantly typing the same instructions.
- **Frameworks are structured CLAUDE.md**: all skill frameworks are essentially collections of instructions you could manually provide to Claude Code, optimized for specific outcomes.
- **Superpowers**: widely popular, described as "absolute game changers"; opinionated about how work should be done.
- **Ouroboros**: another popular framework with strong following, especially among teams.
- **Han** (github.com/testdouble/han): single plugin with no "rails" — pick and choose any part; standout features include YAGNI-encoded protocols, "iterative plan review" skill, adversarial investigation for root cause analysis, evidence requirements for all output, agent swarms for most skills.
- **GSD** (Get Stuff Done): mentioned as an alternative with its own opinionated approach.
- **Roll your own**: building a few custom skills yourself first is the best way to understand how frameworks work before committing to a published one.

## Details
From community discussion — key framework differentiators:
- **Superpowers**: consistently described as high-impact ("absolute game changers") but requires staying on its rails.
- **Han** distinguishes itself with: (1) adversarial approach to verification, (2) YAGNI directly encoded, (3) "investigate" skill praised for root cause analysis, (4) direct requirement for evidence in all outputs, (5) agent swarms for more accurate results. Trade-off: requires comfort with a more modular, less prescriptive workflow.
- **Sandcastle**: mentioned as an alternative that some find more exciting than markdown-based frameworks.
- **Start minimal**: community consensus is to write a few custom skills first, then adopt a framework if you still need structure — don't over-engineer upfront.

## Notable Quotes
> "All skill frameworks are basically just specifying a bunch of instructions you could otherwise manually tell Claude Code. Each framework is optimized for different results." — r/ClaudeCode community

## Related Entries
- [[claude-code-extensions-overview]]
- [[claude-code-deferral-behavior]]
- [[claude-code-workflows-best-practices]]

---
<!-- RU -->

## Краткое описание
Сообщество Claude Code создало несколько конкурирующих фреймворков навыков (наборы готовых навыков, агентов и рабочих процессов, упакованных как плагины). GSD, Superpowers и Ouroboros широко цитируются; Han (от testdouble) использует более лёгкий подход «выбери своё приключение». Все они опциональны — добавляйте только тогда, когда упираетесь в пределы возможностей сырого Claude Code.

## Ключевые идеи
- **Когда нужен фреймворк**: только если вы упираетесь в пределы модели + встроенных режимов plan/build, или если постоянно вводите одни и те же инструкции.
- **Фреймворки — это структурированные CLAUDE.md**: все фреймворки навыков — это, по сути, наборы инструкций, которые вы могли бы предоставить Claude Code вручную, оптимизированные для конкретных результатов.
- **Superpowers**: широко популярен, описывается как «абсолютный game-changer»; опинионированный в отношении способа работы.
- **Ouroboros**: ещё один популярный фреймворк с сильным сообществом, особенно среди команд.
- **Han** (github.com/testdouble/han): единственный плагин без «рельсов» — выбирайте любую часть; отличительные особенности: YAGNI-закодированные протоколы, навык «итеративного ревью плана», состязательное расследование для анализа первопричин, требования к доказательствам для всех выходных данных, роевые агенты для большинства навыков.
- **GSD** (Get Stuff Done): упоминается как альтернатива со своим опинионированным подходом.
- **Создайте своё**: сначала написать несколько собственных навыков — лучший способ понять, как работают фреймворки, прежде чем переходить к опубликованному.

## Подробнее
Из обсуждения в сообществе — ключевые отличия фреймворков:
- **Superpowers**: неизменно описываются как высокоэффективные («абсолютные game changers»), но требуют следования его правилам.
- **Han** выделяется: (1) состязательный подход к верификации, (2) YAGNI напрямую закодирован, (3) навык «investigate» хвалят за анализ первопричин, (4) прямые требования к доказательствам во всех выходных данных, (5) агентные рои для более точных результатов. Компромисс: требует комфорта с более модульным, менее предписывающим рабочим процессом.
- **Sandcastle**: упоминается как альтернатива, которую некоторые находят более интересной, чем фреймворки на основе markdown.
- **Начинайте минимально**: консенсус сообщества — сначала написать несколько собственных навыков, затем принять фреймворк, если всё ещё нужна структура — не переинженируйте заранее.

## Примечательные цитаты
> «Все фреймворки навыков — это, по сути, просто набор инструкций, которые вы могли бы вручную дать Claude Code. Каждый фреймворк оптимизирован для разных результатов.» — сообщество r/ClaudeCode

## Связанные записи
- [[claude-code-extensions-overview]]
- [[claude-code-deferral-behavior]]
- [[claude-code-workflows-best-practices]]
