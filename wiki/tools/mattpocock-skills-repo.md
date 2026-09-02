---
title: "Matt Pocock's Skills Repo: Engineering Skills for Real Engineers"
title_ru: "Репозиторий навыков Мэтта Покока: навыки для настоящих инженеров"
category: tools
tags: [claude-code, skills, agent-skills, tdd, diagnose, grill-me, grill-with-docs, improve-codebase-architecture, ubiquitous-language, matt-pocock]
aliases: [mattpocock/skills, Matt Pocock skills, skills repo, real engineer skills]
confidence: high
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://github.com/mattpocock/skills
---

## Summary
Matt Pocock's public skills repository (18.3k+ stars) contains the Claude Code agent skills he uses daily for real engineering — not vibe coding — organized around four failure modes: misalignment, verbosity, broken code, and ball-of-mud codebases. Small, composable, and model-agnostic.

## Key Ideas
- **Philosophy over GSD/BMAD**: unlike GSD, BMAD, or Spec-Kit which own the whole process, these skills are small and composable — you stay in control, combining them as needed rather than handing off to a framework.
- **`/grill-me` and `/grill-with-docs`** are the most popular: relentless interviewing before coding starts, grounding the session in your actual domain language (CONTEXT.md + ADRs). Fixes the #1 failure mode: the agent didn't understand what you wanted.
- **`/improve-codebase-architecture`** is the anti-entropy skill: runs every few days on a codebase to find deepening opportunities, informed by domain language. Directly addresses the problem that AI-assisted codebases accumulate entropy faster than human-written ones.
- **`/caveman`** cuts output tokens ~75% by injecting a terse communication mode — technical accuracy preserved, filler stripped. Pairs with 9router's Caveman Mode.
- **30-second setup**: `npx skills@latest add mattpocock/skills`, pick skills, pick agents, run `/setup-matt-pocock-skills` once per repo.

## Details

### The Four Failure Modes These Skills Fix

**#1 — The agent didn't do what you want** (misalignment)
→ `/grill-me`: relentless questioning about a plan or design until every branch of the decision tree is resolved.
→ `/grill-with-docs`: grilling session that simultaneously sharpens your domain terminology and writes it into CONTEXT.md + ADRs. Named concepts compound over sessions.

**#2 — The agent is way too verbose** (shared language deficit)
→ CONTEXT.md is a shared language document. When "materialization cascade" exists as a term, agents use it instead of 20-word explanations. Files are named consistently. The agent spends fewer tokens thinking.
→ `/grill-with-docs` builds this document while grilling you about the plan.

**#3 — The code doesn't work** (feedback loop gaps)
→ `/tdd`: red-green-refactor loop. Agent writes a failing test first, then fixes. Consistent feedback prevents flying blind.
→ `/diagnose`: disciplined debug loop: reproduce → minimise → hypothesise → instrument → fix → regression-test.

**#4 — We built a ball of mud** (entropy)
→ `/to-prd`: quizzes about which modules are being touched before creating a PRD.
→ `/zoom-out`: agent explains code in the context of the whole system first.
→ `/improve-codebase-architecture`: rescue a codebase that became a ball of mud. Run every few days.

### Full Skills List

**Daily engineering skills:**
- `/diagnose` — disciplined diagnosis loop for hard bugs
- `/grill-with-docs` — grilling + builds CONTEXT.md + ADRs
- `/grill-me` — stress-test any plan or design
- `/triage` — issue triage via state machine of roles
- `/improve-codebase-architecture` — find deepening opportunities
- `/setup-matt-pocock-skills` — one-time per-repo scaffold (run first)
- `/tdd` — TDD with red-green-refactor
- `/to-issues` — break any plan into independently-grabbable GitHub issues
- `/to-prd` — synthesize conversation context into a PRD as a GitHub issue
- `/zoom-out` — high-level perspective on unfamiliar code sections
- `/prototype` — throwaway prototype for design/state questions or UI variations
- `/caveman` — ultra-compressed output, ~75% fewer tokens
- `/handoff` — compact current session into a handoff document
- `/write-a-skill` — create new skills with proper structure

**Rarely used:**
- `/git-guardrails-claude-code` — hooks to block dangerous git commands
- `/migrate-to-shoehorn` — test migration helper
- `/scaffold-exercises` — create exercise directories
- `/setup-pre-commit` — Husky + lint-staged + Prettier + type checking + tests

### Installation

```bash
npx skills@latest add mattpocock/skills
# Pick skills, pick agents, then run:
/setup-matt-pocock-skills   # once per repo
```

Works with Claude Code, Codex, and any agent that supports skills/instructions.

## Related Entries
- [[matt-pocock-aihero]] ([Matt Pocock: AI Hero and Claude Code Skills Author](../people/matt-pocock-aihero.md))
- [[dictionary-of-ai-coding]] ([Dictionary of AI Coding](../tools/dictionary-of-ai-coding.md))
- [[anthropic-skills-building-guide]] ([Anthropic's Complete Guide to Building Skills for Claude](../tips/anthropic-skills-building-guide.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[claude-code-handoff-prototype-skills]] ([Claude Code Skills: /handoff, /prototype, and improve-codebase-architecture](../tips/claude-code-handoff-prototype-skills.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World: From BMAD to Custom Skills](../tips/spec-driven-development-bmad.md))
- [[9router-free-ai-coding]] ([9router: Free AI Coding Router with RTK Token Saver](../tools/9router-free-ai-coding.md))

---
- [[skill-doctor]] ([Skill Doctor](skill-doctor.md))
- [[kindle-highlights-recovery-claude-skill]] ([Kindle Highlights Recovery Skill](kindle-highlights-recovery-claude-skill.md))
<!-- RU -->

## Краткое описание
Публичный репозиторий навыков Мэтта Покока (18.3k+ звёзд) содержит agent skills для Claude Code, которые он использует ежедневно для реального инжиниринга — не вайб-кодинга — организованные вокруг четырёх режимов отказа: несоответствие ожиданий, многословность, нерабочий код и «шарик грязи». Маленькие, компонуемые, не зависящие от модели.

## Ключевые идеи
- **Философия против GSD/BMAD**: в отличие от GSD, BMAD или Spec-Kit, которые берут весь процесс под управление, эти навыки маленькие и компонуемые — вы остаётесь в управлении.
- **`/grill-me` и `/grill-with-docs`** — самые популярные: беспощадный допрос перед кодингом, создание общего языка домена в CONTEXT.md + ADR.
- **`/improve-codebase-architecture`** — антиэнтропийный навык: запускайте раз в несколько дней для поиска возможностей «углубления» архитектуры.
- **`/caveman`** сокращает выходные токены ~на 75%, сохраняя техническую точность.
- **30-секундная установка**: `npx skills@latest add mattpocock/skills`, выберите навыки и агентов, один раз выполните `/setup-matt-pocock-skills`.

## Подробнее

**Четыре режима отказа и их исправление:**

1. **Агент не сделал то, что вы хотели** → `/grill-me`, `/grill-with-docs`: устанавливает выравнивание до кодинга, строит общий язык.

2. **Агент слишком многословен** → CONTEXT.md с общим языком. Когда термин «materialization cascade» существует, агент использует его вместо 20 слов. Файлы именуются согласованно.

3. **Код не работает** → `/tdd` (red-green-refactor), `/diagnose` (воспроизведи → минимизируй → гипотеза → инструментируй → исправь → регрессионный тест).

4. **Построили шарик грязи** → `/improve-codebase-architecture` раз в несколько дней, `/zoom-out` перед правкой незнакомого кода.

## Связанные записи
- [[matt-pocock-aihero]] ([Matt Pocock: AI Hero and Claude Code Skills Author](../people/matt-pocock-aihero.md))
- [[dictionary-of-ai-coding]] ([Dictionary of AI Coding](../tools/dictionary-of-ai-coding.md))
- [[anthropic-skills-building-guide]] ([Anthropic's Complete Guide to Building Skills for Claude](../tips/anthropic-skills-building-guide.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[claude-code-handoff-prototype-skills]] ([Claude Code Skills: /handoff, /prototype, and improve-codebase-architecture](../tips/claude-code-handoff-prototype-skills.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World: From BMAD to Custom Skills](../tips/spec-driven-development-bmad.md))
- [[9router-free-ai-coding]] ([9router: Free AI Coding Router with RTK Token Saver](../tools/9router-free-ai-coding.md))
