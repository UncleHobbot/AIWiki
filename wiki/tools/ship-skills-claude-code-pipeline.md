---
title: "Ship Skills — Claude Code PR Pipeline"
title_ru: "Ship Skills — конвейер PR для Claude Code"
category: tools
tags: [claude-code, skills, code-review, deployment, automation, pr]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/leighstillard/ship-skills
  - https://www.reddit.com/r/ClaudeCode/comments/1u3f58r/
---

## Summary
Open-source set of 5 Claude Code skills that drive a code change through a full pipeline: /ship orchestrates /verify → /design-check → /pr → /babysit. Treats invariants as preconditions — no PR without a VERIFIED verdict with concrete evidence, no merge without independent review.

## Key Ideas
- Pipeline is `/ship` → `/verify` → `/design-check` → `/pr` → `/babysit`, each stage gated by the previous one
- Invariants enforced as hard preconditions: tests must pass, evidence must be concrete, review must be independent
- Inspired by an Anthropic video on structured agent workflows
- Eliminates the need to babysit code review cycles manually
- Designed as drop-in skills for Claude Code's skill system

## Details
Ship Skills addresses a common frustration with AI-assisted coding: the gap between "code written" and "code merged." Even after an agent writes working code, the path through testing, review, and deployment still requires human hand-holding. This tool automates that entire path.

The `/verify` stage runs tests and collects evidence. `/design-check` validates architectural decisions. `/pr` creates a pull request only after both pass. `/babysit` monitors the review cycle. The orchestrator `/ship` ties them all together, enforcing that no stage runs without its preconditions met.

This is part of a broader trend of structured agent workflows where AI tools operate within guardrails rather than generating unconstrained output.

## Related Entries
- [[grind-claude-code-nonstop]] ([Grind](../tools/grind-claude-code-nonstop.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))

---
<!-- RU -->

## Краткое описание
Набор из 5 навыков (skills) для Claude Code с открытым исходным кодом, который проводит изменение кода через полный конвейер: /ship управляет /verify → /design-check → /pr → /babysit. Инварианты используются как предусловия — никаких PR без вердикта VERIFIED с конкретными доказательствами, никакого слияния без независимой проверки.

## Ключевые идеи
- Конвейер: `/ship` → `/verify` → `/design-check` → `/pr` → `/babysit`, каждый этап зависит от предыдущего
- Инварианты — жёсткие предусловия: тесты должны пройти, доказательства должны быть конкретными, проверка — независимой
- Вдохновлено видео Anthropic о структурированных агентных рабочих процессах
- Устраняет необходимость ручного контроля циклов код-ревью
- Разработано как подключаемые навыки для системы skills в Claude Code

## Подробнее
Ship Skills решает распространённую проблему AI-кодирования: разрыв между «код написан» и «код влит». Даже после того, как агент написал рабочий код, путь через тестирование, ревью и развёртывание всё ещё требует ручного контроля. Этот инструмент автоматизирует весь этот путь.

Этап `/verify` запускает тесты и собирает доказательства. `/design-check` проверяет архитектурные решения. `/pr` создаёт pull request только после успешного прохождения обоих. `/babysit` контролирует цикл ревью. Оркестратор `/ship` связывает всё вместе, гарантируя, что ни один этап не запускается без выполнения предусловий.

Это часть более широкой тенденции структурированных агентных рабочих процессов, где AI-инструменты работают в рамках ограничений, а не генерируют неограниченный вывод.

## Связанные записи
- [[grind-claude-code-nonstop]] ([Grind](../tools/grind-claude-code-nonstop.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
