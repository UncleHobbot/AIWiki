---
title: "9 Claude Code Mistakes That Waste Tokens and Time"
title_ru: "9 ошибок в Claude Code, которые тратят токены и время"
category: tips
tags: [claude-code, token-optimization, workflow, agent-skills, cost-optimization]
confidence: medium
updated: 2026-05-26
sources:
  - https://www.linkedin.com/posts/brijpandeyji_9-claude-code-mistakes-that-are-quietly-wasting-activity-7440726326036275200-RHVY
  - https://x.com/Mnilax/status/2050261839653556522
---

## Summary
Nine systemic mistakes in Claude Code usage — identified by Boris Cherny (creator of Claude Code) and documented by Brij Kishore Pandey — account for most wasted tokens. The root cause is not the model's cost but bad system design around context, workflows, and structure.

## Key Ideas
- **Single-threading everything:** Running multiple tasks in one thread creates messy context that degrades outputs; use worktrees or separate sessions for isolation
- **Rewriting prompts:** If a prompt repeats, it should become a slash command — persistent, versioned, and shareable across the team
- **Skipping skills:** Without structured skills, you force the model to "figure it out" from scratch every session, burning tokens on rediscovery
- **Context overload:** More tokens ≠ better results; overloading context often reduces accuracy and increases cost
- **Memory as dump folder:** CLAUDE.md and auto-memory should store long-term architectural truth, not temporary noise from the current session
- **No workflow standardization:** Debugging, code reviews, and documentation generation should be repeatable systems, not ad-hoc prompts
- **Ignoring MCP integrations:** Without MCP servers connecting Claude to real tools and data, you limit its capability and force workarounds
- **Missing guardrails and hooks:** Validation, linting, and policy enforcement should run automatically via hooks, not wait for manual checks
- **No iteration loop:** Without checkpoint → rewind → improve cycles, you lose control over output quality and cannot course-correct efficiently

## Details
The analysis by Boris Cherny (who built Claude Code at Anthropic) and popularized by Brij Kishore Pandey reframes the cost conversation: Claude Code is not expensive because of the model — it becomes expensive because of how it is used. Small mistakes in context management, structure, and workflows compound fast.

The meta-pattern across all 9 mistakes is treating Claude Code like a chat tool instead of a programmable system. Each mistake has a clear remediation that maps to a Claude Code feature: threads → worktrees, repeated prompts → commands, ad-hoc thinking → skills, noisy context → curated CLAUDE.md, manual checks → hooks. The Claude Code practitioners reporting the best results are engineers who design their agent environment as carefully as they design their code architecture.

As one commenter noted: "The hidden cost of AI is 'Contextual Debt' — overloading context doesn't just waste tokens; it introduces Semantic Noise that degrades reasoning quality."

## Notable Quotes
> "The real cost is not tokens. The real cost is bad system design. Claude Code rewards engineers who think in: context + workflows + tools + structure. Not prompts." — Brij Kishore Pandey

## Related Entries
- [[claude-code-usage-limits-token-management]] ([10 Ways to Stop Hitting Claude](../tips/claude-code-usage-limits-token-management.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[claude-code-12-setup-tricks]] ([12 Claude Code Setup Tricks](../tips/claude-code-12-setup-tricks.md))
- [[claude-code-prompting-era]] ([The New Prompting Era](../tips/claude-code-prompting-era.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))

---
<!-- RU -->

## Краткое описание
Девять системных ошибок при работе с Claude Code — выявленных Борисом Черни (создателем Claude Code) и задокументированных Бриджем Кишором Пандеем — отвечают за большую часть впустую потраченных токенов. Корневая причина — не стоимость модели, а плохая системная архитектура вокруг контекста, рабочих процессов и структуры.

## Ключевые идеи
- **Всё в одном потоке:** Выполнение нескольких задач в одном потоке создаёт запутанный контекст, ухудшающий результаты; используйте worktree или отдельные сессии для изоляции
- **Переписывание промптов:** Если промпт повторяется, он должен стать slash-командой — постоянной, версионированной и общей для команды
- **Игнорирование навыков:** Без структурированных навыков вы заставляете модель «разбираться с нуля» каждую сессию, тратя токены на переоткрытие
- **Перегрузка контекста:** Больше токенов ≠ лучше результаты; перегрузка контекста часто снижает точность и увеличивает стоимость
- **Память как свалка:** CLAUDE.md и auto-memory должны хранить долгосрочную архитектурную истину, а не временный шум текущей сессии
- **Отсутствие стандартизации рабочих процессов:** Отладка, ревью кода и генерация документации должны быть повторяемыми системами, а не ad-hoc промптами
- **Игнорирование MCP:** Без MCP-серверов, подключающих Claude к реальным инструментам и данным, вы ограничиваете его возможности
- **Отсутствие ограждений и хуков:** Валидация, линтинг и контроль политик должны выполняться автоматически через hooks
- **Нет цикла итераций:** Без циклов checkpoint → rewind → improve вы теряете контроль над качеством вывода

## Подробнее
Анализ Бориса Черни (создавшего Claude Code в Anthropic) и популяризированный Бриджем Кишором Пандеем переформулирует разговор о стоимости: Claude Code дорог не из-за модели — он становится дорогим из-за того, как его используют. Мелкие ошибки в управлении контекстом, структуре и рабочих процессах быстро накапливаются.

Мета-паттерн всех 9 ошибок — отношение к Claude Code как к чат-инструменту, а не как к программируемой системе. Каждая ошибка имеет чёткое исправление, соответствующее функции Claude Code: потоки → worktree, повторяющиеся промпты → команды, ad-hoc мышление → навыки, шумный контекст → кураторский CLAUDE.md, ручные проверки → hooks. Практики Claude Code с лучшими результатами — это инженеры, которые проектируют окружение агента так же тщательно, как архитектуру кода.

Как отметил один из комментаторов: «Скрытая стоимость AI — это 'контекстуальный долг': перегрузка контекста не просто тратит токены, она вносит семантический шум, снижающий качество рассуждений.»

## Примечательные цитаты
> "Настоящая стоимость — не токены. Настоящая стоимость — плохая системная архитектура. Claude Code вознаграждает инженеров, мыслящих категориями: контекст + рабочие процессы + инструменты + структура. А не промптов." — Бридж Кишор Пандей

## Связанные записи
- [[claude-code-usage-limits-token-management]] ([10 Ways to Stop Hitting Claude](../tips/claude-code-usage-limits-token-management.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[claude-code-12-setup-tricks]] ([12 Claude Code Setup Tricks](../tips/claude-code-12-setup-tricks.md))
- [[claude-code-prompting-era]] ([The New Prompting Era](../tips/claude-code-prompting-era.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
