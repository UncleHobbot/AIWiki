---
title: "Matt Pocock: AI Hero and Claude Code Skills Author"
title_ru: "Мэтт Покок: AI Hero и автор навыков Claude Code"
category: people
tags: [matt-pocock, claude-code, skills, aihero, coding-agent, typescript, grill-me, tracer-bullets]
updated: 2026-05-17
sources:
  - https://www.aihero.dev/
  - https://www.aihero.dev/5-agent-skills-i-use-every-day
  - https://www.aihero.dev/how-to-make-codebases-ai-agents-love
  - https://www.aihero.dev/tracer-bullets
  - https://www.aihero.dev/my-grill-me-skill-has-gone-viral
  - https://www.youtube.com/watch?v=EJyuu6zlQCg
  - https://www.youtube.com/watch?v=uC44zFz7JSM
  - https://www.youtube.com/watch?v=Ah9p7v7nJWg
---

## Summary
Matt Pocock is a TypeScript educator turned AI coding practitioner whose aihero.dev platform and skills repository (46k+ stars) have become a reference point for Claude Code workflows — most notably the `/grill-me` skill, the "tracer bullets" technique, and the codebase-design-for-AI philosophy built on the "AI is the guy from Memento" insight.

## Key Ideas
- **"AI is the guy from Memento"** — every time you spawn an agent, it enters your codebase with no memory, no context, and has to figure out what it's doing. Your codebase design, not your prompt, is the biggest lever on AI output quality.
- **Tracer bullets**: instead of asking AI to build a complete feature in one shot, ask it to build the smallest possible end-to-end slice first. This forces feedback loops and exposes wrong assumptions before they compound.
- **`/grill-me` skill** (viral, 46k+ stars): "Interview me relentlessly about every aspect of this plan until we reach shared understanding. Walk down each branch of the design tree, resolving dependencies." Used for stress-testing plans before coding starts.
- **Codebase design for AI agents**: three failure modes when a codebase isn't ready for AI — poor feedback loops (AI can't verify its changes worked), hard to navigate (AI can't find files or understand structure), cognitive burnout (AI runs out of context handling complexity). The fix is the same as good software design.
- **7 phases of AI-driven development**: a maturity model from "AI skeptic" → "vibe coding" → "spec-driven development" → "autonomous factory" — each phase requiring more deliberate process and codebase design.

## Details

### The Core Thesis: Software Fundamentals Are More Important, Not Less

Matt Pocock's central argument at aihero.dev runs counter to the "code is cheap, engineering is dead" narrative:

> "Coding agents like Claude Code and Codex ship code faster than any human ever has. But without careful guidance, they make codebases worse. And the worse the codebase, the worse the AI performs. It's a vicious circle. Code isn't cheap. In fact, bad code is the most expensive it's ever been."

His claim: if you can design codebases that agents love, you compound the rewards of AI. If you can't, you compound the costs.

### The /grill-me Skill

The `/grill-me` skill became his most viral contribution (46k+ stars on the skills repo). The principle: before writing any code, have the agent interview you about the plan, following every branch of the decision tree until no ambiguities remain. This converts vague intentions into concrete specifications. He later extended it to `/grill-with-docs` (stress-tests plans against actual documentation) and adapted the pattern for technical writing and design review.

### Tracer Bullets

Borrowed from "The Pragmatic Programmer," Matt Pocock's adaptation for AI: "AI has a natural inclination to sycophancy. It aims to please. In code, this means it wants to produce complete solutions all at once... It doesn't stop to validate assumptions." Tracer bullets force the opposite: build the smallest possible thing that touches every layer end-to-end, verify it works, then expand. This prevents AI from accumulating unverified assumptions across hundreds of lines.

### The AFK Software Factory

His most ambitious concept: structure your work so that AI agents are running autonomously (AFK — Away From Keyboard) on tasks while you work on other things. The precondition is that your codebase and skills are designed well enough that the agent rarely needs intervention. He open-sourced his personal setup for this.

### Codebase Design Principles

From his "How To Make Codebases AI Agents Love" article and "Your Codebase Is NOT Ready for AI" video:
- Testability is the highest-priority codebase property for AI — agents that can verify their changes automatically produce far fewer regressions.
- File structure should be self-describing — agents lose performance when they have to map ambiguous file names to functionality.
- Dependencies should be explicit — implicit global state is the single worst thing for an agent's ability to understand scope.

## Related Entries
- [[claude-code-plugins-guide]]
- [[claude-code-handoff-prototype-skills]]
- [[agent-harness-engineering]]
- [[spec-driven-development-bmad]]

---
<!-- RU -->

## Краткое описание
Мэтт Покок — преподаватель TypeScript, ставший практиком AI-кодирования, чья платформа aihero.dev и репозиторий навыков (46k+ звёзд) стали ориентиром для рабочих процессов Claude Code — в первую очередь благодаря навыку `/grill-me`, технике «tracer bullets» и философии проектирования кодовых баз для AI, построенной на инсайте «AI — это парень из Memento».

## Ключевые идеи
- **«AI — это парень из Memento»** — каждый раз, когда вы запускаете агента, он входит в вашу кодовую базу без памяти и контекста. Дизайн кодовой базы, а не промпт — главный рычаг влияния на качество вывода AI.
- **Tracer bullets**: вместо полного фичи с нуля — минимальный сквозной срез, чтобы принудительно создать петли обратной связи и обнаружить неверные допущения до того, как они накопятся.
- **Навык `/grill-me`** (вирусный, 46k+ звёзд): «Расспрашивай меня безжалостно о каждом аспекте плана, пока мы не достигнем общего понимания. Пройди каждую ветку дерева решений, разрешая зависимости». Используется для стресс-тестирования планов перед кодированием.
- **Проектирование кодовой базы для AI**: три паттерна отказа — слабые петли обратной связи (AI не знает, сработало ли изменение), трудная навигация (AI не может найти файлы), когнитивное выгорание (AI исчерпывает контекст). Исправление то же, что и хороший software design.
- **7 фаз AI-разработки**: от «скептика AI» до «автономной фабрики ПО» — каждая фаза требует более осознанного процесса и проектирования кодовой базы.

## Подробнее

### Центральный тезис: фундаментальные принципы разработки важнее, а не менее важны

Coding-агенты ускоряют разработку, но без тщательного руководства ухудшают кодовые базы. А чем хуже кодовая база, тем хуже AI. Плохой код дороже, чем когда-либо: стоимость поддержки умноженной AI-скоростью катастрофична. Если вы умеете проектировать кодовые базы, которые любят агенты — вы накапливаете выгоды. Если нет — накапливаете долги.

### Навык /grill-me

Самый вирусный вклад: перед написанием кода агент расспрашивает вас о плане по всем ветвям дерева решений, пока не останется неоднозначностей. Конвертирует расплывчатые намерения в конкретные спецификации. Позже развит в `/grill-with-docs` (стресс-тест против реальной документации).

### Tracer Bullets

Адаптация для AI из «Прагматичного программиста»: AI склонен к угодливости и хочет сразу выдать полное решение, не проверяя допущений. Tracer bullets заставляют строить наименьший возможный сквозной срез, верифицировать его, затем расширять. Это предотвращает накопление непроверенных допущений.

### AFK-фабрика программного обеспечения

Наиболее амбициозная концепция: организовать работу так, чтобы AI-агенты работали автономно (AFK — Away From Keyboard) пока вы занимаетесь другим. Предварительное условие — кодовая база и навыки спроектированы достаточно хорошо, чтобы агент редко нуждался во вмешательстве.

## Связанные записи
- [[claude-code-plugins-guide]]
- [[claude-code-handoff-prototype-skills]]
- [[agent-harness-engineering]]
- [[spec-driven-development-bmad]]
