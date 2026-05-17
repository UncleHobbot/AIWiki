---
title: "LLM Confusion Management: Models Don't Check Assumptions"
title_ru: "Управление замешательством LLM: модели не проверяют предположения"
category: tips
tags: [llm, prompting, confusion-management, assumptions, karpathy, claude-code, verification]
date: 2026-05-16
updated: 2026-05-17
sources:
  - https://x.com/techNmak/status/2055712886790701226
---

## Summary

Andrej Karpathy articulated a critical failure mode in LLM agents that every heavy user has experienced but struggled to name: models make wrong assumptions and run with them without checking — they don't manage their own confusion or stop to verify.

## Key Ideas
- **Assumption propagation:** LLMs silently make incorrect assumptions about user intent, context, or task requirements, then build entire chains of reasoning on that flawed foundation
- **No confusion management:** Unlike humans, models don't recognize when they're uncertain or confused — they just keep generating based on their current (possibly wrong) understanding
- **No self-verification instinct:** Models don't stop to ask clarifying questions or verify assumptions unless explicitly prompted to
- **Practical remedy:** Explicitly instruct the model to "verify assumptions before proceeding" or "stop and ask if anything is unclear" — turn verification into a mandatory step, not a suggestion
- **Agentic implication:** This is why skills, hooks, and structured workflows matter in coding agents — they inject verification checkpoints that models won't create on their own

## Details

The insight, relayed via @techNmak, captures three quotes from Karpathy:

1. "The models make wrong assumptions on your behalf and just run along with them without checking."
2. "They don't manage their confusion."
3. "They don't seek clarification."

This behavior is structural, not a bug. LLMs predict the next token given the current context — they have no intrinsic "uncertainty detector" or "confusion signal." When a premise is ambiguous, the model doesn't flag it — it picks the most probable interpretation and commits.

For agentic workflows (Claude Code, Codex, OpenCode), this failure mode is amplified by tool use. An agent that makes wrong assumptions and has access to file write, terminal, and git can cause cascading damage before the user notices.

### Mitigation Strategies
- **Pre-prompt verification:** Add "Before executing, verify your assumptions about the codebase" to CLAUDE.md/AGENTS.md
- **Hooks/skills that pause:** Use agent skills that intercept before destructive actions and require confirmation
- **Structured task definitions:** Spec-driven development (spec-kit) prevents assumption drift by anchoring all work to explicit requirements
- **Checkpointing:** Tools like Entire (captures agent session state) let you roll back when assumptions turn out wrong

## Notable Quotes

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarification." — Andrej Karpathy (via @techNmak, May 2026)

## Related Entries
- [[karpathy-deep-dive-llms]]
- [[spec-driven-development-bmad]]
- [[claude-code-deferral-behavior]]
- [[claude-code-workflows-best-practices]]
- [[tracer-bullets-agentic-coding]]

---
<!-- RU -->

## Краткое описание

Андрей Карпаты описал критический режим отказов LLM-агентов, который ощущал каждый активный пользователь, но не мог назвать: модели делают неверные предположения и действуют на их основе без проверки — они не управляют собственным замешательством и не останавливаются для верификации.

## Ключевые идеи
- **Распространение предположений:** LLM незаметно делают неверные предположения о намерениях пользователя, контексте или требованиях задачи, а затем строят целые цепочки рассуждений на этом ошибочном фундаменте
- **Отсутствие управления замешательством:** В отличие от людей, модели не распознают, когда они неуверены или запутались — они просто продолжают генерировать на основе своего текущего (возможно, неверного) понимания
- **Нет инстинкта самопроверки:** Модели не останавливаются, чтобы задать уточняющие вопросы или проверить предположения, если их явно не попросить
- **Практическое решение:** Явно инструктируйте модель «проверять предположения перед выполнением» или «остановиться и спросить, если что-то неясно» — превратите верификацию в обязательный шаг, а не предложение
- **Агентное следствие:** Поэтому навыки (skills), хуки и структурированные воркфлоу критически важны в кодинг-агентах — они добавляют контрольные точки верификации, которые модели не создадут сами

## Подробнее

Прозрение, переданное через @techNmak, содержит три цитаты Карпаты:

1. «Модели делают неверные предположения от вашего имени и просто следуют им без проверки.»
2. «Они не управляют своим замешательством.»
3. «Они не ищут уточнений.»

Это поведение структурно, а не баг. LLM предсказывают следующий токен на основе текущего контекста — у них нет встроенного «детектора неуверенности» или «сигнала замешательства.» Когда предпосылка неоднозначна, модель не отмечает это — она выбирает наиболее вероятную интерпретацию и действует.

Для агентных воркфлоу (Claude Code, Codex, OpenCode) этот режим отказов усиливается доступом к инструментам. Агент, делающий неверные предположения и имеющий доступ к записи файлов, терминалу и git, может вызвать каскадный ущерб, прежде чем пользователь заметит.

### Стратегии смягчения
- **Пре-промпт верификация:** Добавьте «Перед выполнением проверь свои предположения о кодовой базе» в CLAUDE.md/AGENTS.md
- **Хуки/навыки с паузой:** Используйте навыки агента, которые перехватывают управление перед деструктивными действиями и требуют подтверждения
- **Структурированные определения задач:** Разработка на основе спецификаций (spec-kit) предотвращает дрейф предположений, привязывая всю работу к явным требованиям
- **Чекпоинтинг:** Инструменты вроде Entire (сохраняет состояние сессии агента) позволяют откатить изменения, когда предположения оказываются неверными

## Примечательные цитаты

> «Модели делают неверные предположения от вашего имени и просто следуют им без проверки. Они не управляют своим замешательством, не ищут уточнений.» — Андрей Карпаты (через @techNmak, май 2026)

## Связанные записи
- [[karpathy-deep-dive-llms]]
- [[spec-driven-development-bmad]]
- [[claude-code-deferral-behavior]]
- [[claude-code-workflows-best-practices]]
- [[claude-code-agentic-loop]]
