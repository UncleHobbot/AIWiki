---
title: "Loop Engineering Hype-Check — Taxonomy, Verdicts, and Failure Modes"
title_ru: "Проверка хайпа loop engineering — таксономия, вердикты и режимы отказа"
category: tips
tags: [agentic-loop, harness-engineering, agent-workflow, critique, stop-conditions]
aliases: [loop engineering, hype check loop engineering, agent loops]
confidence: medium
updated: 2026-09-01
sources:
  - https://woliveiras.com/posts/hype-check-on-loop-engineering/
---

## Summary
William Oliveira's June 2026 essay audits "loop engineering" — designing the control flow that decides when/how/with what context/checks/stopping conditions an agent works — claim by claim, grounded in ReAct/Reflexion, Codex/Claude Code docs, and OWASP. Verdict: the core idea is real (it's the layer above harness engineering), but the hype overstates it; loops are for repetitive, verifiable, low-blast-radius work — not everything.

## Key Ideas
- **Taxonomy:** prompt < workflow < harness ("the agent's operating context") < loop ("the control flow around that context"). Subagents are optional components, not the loop itself.
- **Verdicts on the hype:** "replaces prompt engineering" — exaggerated; "next layer after harness engineering" — the strongest signal; "every task should become a loop" — rejected.
- **Loop anatomy:** trigger, goal, context, action, observation, verifier, state, stop condition. Closed loops are the production default; maker/checker separation mandatory.
- **Stop conditions:** stop on success, on repeated failure, on budget exhaustion, on ambiguous progress.
- **Safety rule:** "Agent autonomy should expand only after the environment is constrained" — worktrees, filesystem + network sandboxing, minimal credentials.
- **Failure-mode catalog:** goal drift, verification theater, scope creep by iteration, self-confirming review, cost blindness.

## Notable Quotes
> "A loop that cannot halt is not autonomy. It is a billing and risk machine." — William Oliveira

## Details
This fills the critical/practical gap between the wiki's structural entries ([[claude-code-agentic-loop]], [[custom-agent-loop-vs-sdk]]): those describe what loops are; this one says when they're a mistake. The stop-condition discipline and the constrained-environment-first rule dovetail with [[hard-gates-over-soft-prompts]] — both argue structure beats exhortation.

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[custom-agent-loop-vs-sdk]] ([Custom Agent Loop vs SDK](../agents/custom-agent-loop-vs-sdk.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](hard-gates-over-soft-prompts.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent](../agents/anatomy-ai-agent-pipeline-loop-tools.md))

---
<!-- RU -->

## Краткое описание
Эссе Уильяма Оливейры (июнь 2026) проверяет «loop engineering» — проектирование control flow, определяющего когда/как/с каким контекстом/проверками/условиями остановки работает агент — тезис за тезисом, опираясь на ReAct/Reflexion, документацию Codex/Claude Code и OWASP. Вердикт: ядро реально (это слой над harness engineering), но хайп преувеличивает; лупы — для повторяемой, проверяемой работы с низким радиусом поражения.

## Ключевые идеи
- **Таксономия:** prompt < workflow < harness («рабочий контекст агента») < loop («control flow вокруг контекста»). Сабагенты — опциональные компоненты, не сам луп.
- **Вердикты:** «заменяет prompt engineering» — преувеличение; «следующий слой после harness engineering» — самый сильный сигнал; «любая задача должна стать лупом» — отвергнуто.
- **Анатомия лупа:** триггер, цель, контекст, действие, наблюдение, верификатор, состояние, условие остановки. Закрытые лупы — production-дефолт; разделение maker/checker обязательно.
- **Условия остановки:** успех, повторный провал, исчерпание бюджета, неоднозначный прогресс.
- **Правило безопасности:** «Автономия агента должна расширяться только после ограничения среды».
- **Каталог отказов:** дрейф цели, театр верификации, расползание объёма итерациями, самоутверждающееся ревью, слепота к стоимости.

## Примечательные цитаты
> «Луп, который не может остановиться, — это не автономия. Это машина выставления счетов и рисков.» — Уильям Оливейра

## Подробнее
Заполняет критический/практический пробел между структурными записями вики: они описывают, что такое лупы; это — когда они ошибочны. Дисциплина условий остановки и правило «сначала ограничь среду» перекликаются с [[hard-gates-over-soft-prompts]] — оба argue, что структура сильнее увещеваний.

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[custom-agent-loop-vs-sdk]] ([Custom Agent Loop vs SDK](../agents/custom-agent-loop-vs-sdk.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](hard-gates-over-soft-prompts.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
