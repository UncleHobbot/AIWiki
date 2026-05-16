---
title: "Claude Code Workflows and Best Practices"
title_ru: "Рабочие процессы и лучшие практики Claude Code"
category: tips
tags: [claude-code, workflow, best-practices, prompting, context-management, anthropic]
updated: 2026-05-16
sources:
  - https://code.claude.com/docs/en/common-workflows
  - https://code.claude.com/docs/en/best-practices
---

## Summary
Getting the most from Claude Code requires treating context as your primary resource, always giving Claude a way to verify its own work, and using parallel sessions and subagents to scale output.

## Key Ideas
- **Context is the primary constraint** — performance degrades as the context window fills; manage it aggressively with `/clear`, `/compact`, and subagents.
- **Give Claude a way to verify** — provide test cases, paste screenshots of expected UI, define what "done" looks like; Claude performs dramatically better with feedback loops.
- **Explore first, then plan, then code** — use plan mode (`Shift+Tab` or `claude --permission-mode plan`) to separate research from execution; review the plan before Claude touches any files.
- **Specific prompts beat vague prompts** — reference exact files, mention constraints, point to existing patterns; include the symptom, likely location, and what "fixed" looks like.
- **Resume or fork sessions** — `claude --continue` picks up the most recent session; `claude --resume` shows a picker; sessions persist locally even after closing the terminal.
- **Worktrees for parallel sessions** — `claude --worktree feature-auth` creates an isolated checkout; run the same in a second terminal for concurrent work without collisions.

## Details
**Prompt anti-patterns to avoid:**
- Kitchen-sink session: mixing unrelated tasks → fix with `/clear` between tasks.
- Correcting over and over (>2 corrections): context polluted with failed attempts → `/clear` and rewrite the prompt incorporating what you learned.
- Over-specified CLAUDE.md (>200 lines): important rules get lost → ruthlessly prune; convert to hooks what must always happen.
- Infinite exploration: asking Claude to "investigate" without scoping → use subagents so exploration doesn't consume main context.

**Common workflow patterns:**
- `git log --oneline -20 | claude -p "summarize these recent commits"` — pipe data directly.
- Writer/Reviewer: Session A implements, Session B reviews with fresh context (no bias toward code it wrote).
- Schedule recurring tasks via Routines (cloud, even when machine is off), Desktop scheduled tasks (local files), GitHub Actions (CI events), or `/loop` (current session).

**Effective CLAUDE.md rules:**
- Include: bash commands Claude can't guess, code style rules differing from defaults, testing instructions, architectural decisions.
- Exclude: things Claude can infer from code, standard language conventions, frequently-changing info, long explanations.

## Notable Quotes
> "If you've corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches. Run `/clear` and start fresh with a more specific prompt that incorporates what you learned." — Claude Code Docs

## Related Entries
- [[claude-code-agentic-loop]]
- [[claude-code-permission-modes]]
- [[claude-code-memory]]
- [[chorus-multi-model-setup]]

---
<!-- RU -->

## Краткое описание
Чтобы получить максимум от Claude Code, нужно воспринимать контекст как основной ресурс, всегда давать Claude возможность проверять свою работу и использовать параллельные сессии и подагентов для масштабирования результата.

## Ключевые идеи
- **Контекст — основное ограничение** — производительность падает по мере заполнения окна контекста; управляйте им активно: `/clear`, `/compact` и подагенты.
- **Дайте Claude возможность проверить работу** — предоставьте тест-кейсы, вставьте скриншот ожидаемого UI, определите, что значит «готово»; Claude работает значительно лучше с циклами обратной связи.
- **Сначала исследование, затем план, потом код** — используйте plan-режим (`Shift+Tab` или `claude --permission-mode plan`) для разделения исследования и выполнения; проверьте план до того, как Claude коснётся файлов.
- **Конкретные промпты лучше расплывчатых** — указывайте точные файлы, упоминайте ограничения, ссылайтесь на существующие паттерны; включайте симптом, вероятное место и то, как выглядит «исправлено».
- **Возобновление или ветвление сессий** — `claude --continue` подхватывает последнюю сессию; `claude --resume` показывает список; сессии сохраняются локально даже после закрытия терминала.
- **Worktrees для параллельных сессий** — `claude --worktree feature-auth` создаёт изолированный checkout; то же во втором терминале для параллельной работы без коллизий.

## Подробнее
**Антипаттерны промптов:**
- Сессия «всё в одном»: смешивание несвязанных задач → `/clear` между задачами.
- Бесконечные исправления (>2 коррекций): контекст засорён провальными попытками → `/clear` и перепишите промпт с учётом выученного.
- Перегруженный CLAUDE.md (>200 строк): важные правила теряются → безжалостно сокращайте; преобразуйте в хуки то, что должно выполняться всегда.
- Бесконечное исследование: просить Claude «исследовать» без рамок → используйте подагентов, чтобы исследование не съедало основной контекст.

**Типичные рабочие паттерны:**
- `git log --oneline -20 | claude -p "summarize these recent commits"` — передача данных через pipe.
- Автор/Рецензент: Сессия A реализует, Сессия B проверяет с чистым контекстом (без предвзятости к только что написанному коду).
- Планирование повторяющихся задач через Routines (в облаке, даже когда машина выключена), Desktop scheduled tasks (локальные файлы), GitHub Actions (события CI) или `/loop` (текущая сессия).

**Правила эффективного CLAUDE.md:**
- Включайте: bash-команды, которые Claude не угадает; правила стиля, отличающиеся от умолчаний; инструкции по тестированию; архитектурные решения.
- Исключайте: то, что Claude может понять из кода; стандартные языковые соглашения; часто меняющуюся информацию; длинные объяснения.

## Примечательные цитаты
> «Если вы поправляли Claude более двух раз по одному и тому же вопросу в одной сессии, контекст замусорен провальными подходами. Запустите `/clear` и начните заново с более конкретным промптом, включающим то, что вы поняли.» — Claude Code Docs

## Связанные записи
- [[claude-code-agentic-loop]]
- [[claude-code-permission-modes]]
- [[claude-code-memory]]
- [[chorus-multi-model-setup]]
