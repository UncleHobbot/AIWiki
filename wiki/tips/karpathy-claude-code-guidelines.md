---
title: "Karpathy-Inspired Claude Code Guidelines"
title_ru: "Рекомендации для Claude Code по мотивам Карпати"
category: tips
tags: [claude-code, guidelines, prompt-engineering, CLAUDE.md, best-practices, karpathy, simplicity, goal-driven]
updated: 2026-05-16
sources:
  - https://github.com/forrestchang/andrej-karpathy-skills
---

## Summary
A single CLAUDE.md file distilling Andrej Karpathy's observations on LLM coding pitfalls into four actionable principles: Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution.

## Key Ideas
- **Think Before Coding:** LLMs silently pick an interpretation and run — this principle forces explicit assumption-stating, presenting multiple interpretations when ambiguous, and stopping to ask rather than guessing.
- **Simplicity First:** Combat overengineering — no features beyond what was asked, no single-use abstractions, no speculative error handling. If 200 lines could be 50, rewrite it.
- **Surgical Changes:** Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Match existing style even if you'd do it differently. If you notice unrelated dead code, mention it — don't delete it.
- **Goal-Driven Execution:** Transform imperative instructions into declarative goals with verification loops. "Add validation" → "Write tests for invalid inputs, then make them pass." Let the LLM loop independently against specific success criteria.
- **Installable as Claude Code plugin:** Available via the Test Double marketplace (`/plugin marketplace add forrestchang/andrej-karpathy-skills`) — installs once, applies across all projects.
- **Bias toward caution:** These guidelines intentionally trade speed for fewer costly mistakes on non-trivial work. Use judgment for trivial one-liners.

## Details
Karpathy's original critique of coding LLMs: they make wrong assumptions silently, overcomplicate code and APIs, implement 1000 lines when 100 would do, and change/remove code they don't understand as a side effect. This CLAUDE.md directly addresses all four failure modes.

The goal-driven principle is particularly high-leverage. Karpathy noted: "LLMs are exceptionally good at looping until they meet specific goals." Weak success criteria ("make it work") require constant user intervention. Strong criteria ("write a test that reproduces the bug, then make it pass") let the model loop independently. Multi-step tasks should include a brief plan: `1. [Step] → verify: [check]`.

The "surgical changes" principle is equally important for code review health: every changed line should trace directly to the user's request. Drive-by refactoring and adjacent "improvements" pollute diffs and hide the actual changes under review.

The guidelines are designed to compose with project-specific instructions — add them to an existing CLAUDE.md or create a new one. For trivial tasks (obvious one-liners, typo fixes), apply judgment — not every interaction needs the full rigor.

## Notable Quotes
> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should." — Andrej Karpathy

## Related Entries
- [[claude-code-workflows-best-practices]]
- [[spec-driven-development-bmad]]

---
<!-- RU -->

## Краткое описание
Один CLAUDE.md-файл, дистиллирующий наблюдения Андрея Карпати о ловушках кодирования с LLM в четыре практических принципа: «Думай перед кодом», «Простота прежде всего», «Хирургические изменения» и «Целеориентированное выполнение».

## Ключевые идеи
- **Думай перед кодом:** LLM молча выбирает интерпретацию и двигается дальше — этот принцип обязывает явно озвучивать допущения, при двусмысленности предлагать несколько интерпретаций и останавливаться, чтобы уточнить, а не угадывать.
- **Простота прежде всего:** Борьба с оверинжинирингом — никаких фич сверх запрошенного, никаких абстракций для однократного использования, никакой спекулятивной обработки ошибок. Если 200 строк можно сделать 50 — переписать.
- **Хирургические изменения:** Трогайте только то, что необходимо. Не «улучшайте» смежный код, комментарии или форматирование. Придерживайтесь существующего стиля. Если заметили несвязанный мёртвый код — упомяните, не удаляйте.
- **Целеориентированное выполнение:** Превращайте императивные инструкции в декларативные цели с циклами верификации. «Добавь валидацию» → «Напиши тесты для невалидных входных данных, затем сделай их проходящими». Дайте LLM зацикливаться самостоятельно на конкретных критериях успеха.
- **Устанавливается как плагин Claude Code:** Доступно через маркетплейс Test Double (`/plugin marketplace add forrestchang/andrej-karpathy-skills`) — устанавливается один раз, применяется во всех проектах.
- **Уклон в сторону осторожности:** Эти рекомендации намеренно торгуют скоростью на меньшее количество дорогостоящих ошибок при нетривиальной работе.

## Подробнее
Исходная критика Карпати кодирующих LLM: они молча делают неверные предположения, усложняют код и API, реализуют 1000 строк там, где хватило бы 100, и меняют/удаляют код, который не понимают, как побочный эффект. CLAUDE.md напрямую решает все четыре проблемы.

Принцип целеориентированного выполнения особенно эффективен. Карпати отметил: «LLM исключительно хороши в зацикливании до достижения конкретных целей». Слабые критерии успеха («заставь это работать») требуют постоянного вмешательства. Сильные («напиши тест, воспроизводящий баг, затем сделай его проходящим») позволяют модели работать независимо. Многошаговые задачи должны включать краткий план: `1. [Шаг] → проверка: [критерий]`.

Принцип «хирургических изменений» одинаково важен для здоровья код-ревью: каждая изменённая строка должна напрямую соответствовать запросу пользователя. Попутный рефакторинг и соседние «улучшения» загрязняют diff и скрывают реальные изменения.

## Примечательные цитаты
> «Модели делают неверные предположения вместо вас и просто продолжают работать с ними, не проверяя. Они не управляют своей неопределённостью, не уточняют, не обнажают противоречия, не представляют компромиссы, не возражают, когда должны.» — Андрей Карпати

## Связанные записи
- [[claude-code-workflows-best-practices]]
- [[spec-driven-development-bmad]]
