---
title: "ab-method: Domain-Grounded Planning Workflow for Claude Code and Codex"
title_ru: "ab-method: workflow планирования с привязкой к домену для Claude Code и Codex"
category: tools
tags: [claude-code, codex, workflow, planning, tdd, spec-driven, domain-model, skills, autonomous]
aliases: [ab-method, ayoubben18/ab-method, ab method workflow]
confidence: high
updated: 2026-06-05
sources:
  - https://github.com/ayoubben18/ab-method
  - https://www.reddit.com/r/ClaudeCode/comments/1tydnr4/ab_method_a_powerful_workflow_for_claude_code/
---

## Summary
ab-method is a workflow system for Claude Code and Codex that "grills" a problem statement into a domain-grounded implementation plan, then either drives it through test-driven missions you review one at a time, or hands it to an autonomous `/goal` loop with verifiable stop conditions.

## Key Ideas
- **Grill-first planning**: like Matt Pocock's `/grill-me`, ab-method interrogates the problem into a domain-grounded plan before any code is written — grounding in ubiquitous language and architecture decisions.
- **Two execution paths**: `/create-task` breaks work into missions you review individually via TDD (human-in-the-loop); `/create-goal` generates a prompt for an autonomous `/goal` loop with verifiable stop conditions (hands-off).
- **Architecture grounding**: `/analyze-project` produces a domain-language glossary and technical docs as the baseline that all later work references.
- **Tangent management**: a handoff mechanism captures side-topics discovered during planning, spinning them into separate tasks — keeping the main task focused.
- **Auto-detecting installer**: `npx ab-method` detects Claude's `.claude/` and/or Codex's `.agents/` directory and deploys the workflow files, helper skills, and docs scaffolding to the right place.

## Details
ab-method sits in the spec-driven-development family alongside BMAD, Spec-Kit, and Matt Pocock's skills, but distinguishes itself with an explicit fork between supervised and autonomous execution. The four-stage workflow — **Baseline → Sharpen → Build → Maintain** — mirrors the harness-engineering principle that the repository should become the system of record.

1. **Baseline**: `/analyze-project` establishes domain language + architecture docs
2. **Sharpen**: `domain-model` refines domain concepts and captures architecture decisions
3. **Build**: `/create-task` (interactive TDD missions) or `/create-goal` (autonomous loop)
4. **Maintain**: `/update-architecture` after significant changes

The autonomous `/goal` loop with verifiable stop conditions addresses one of the central problems in agentic coding — agents declaring victory too early. By requiring verifiable stop conditions up front, ab-method forces the loop to prove completion rather than self-assess it.

The cross-tool design (Claude Code + Codex from one installer) reflects the broader trend of portable, agent-agnostic workflow skills that don't lock users into a single harness.

## Related Entries
- [[mattpocock-skills-repo]] ([Matt Pocock's Skills Repo](../tools/mattpocock-skills-repo.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development: From BMAD to Custom Skills](../tips/spec-driven-development-bmad.md))
- [[dual-brain-agentic-protocol]] ([Dual-Brain: Adversarial Two-Agent Workflow](../tools/dual-brain-agentic-protocol.md))
- [[github-spec-kit]] ([GitHub Spec-Kit](../tools/github-spec-kit.md))

---
<!-- RU -->

## Краткое описание
ab-method — система workflow для Claude Code и Codex, которая «допрашивает» постановку задачи до плана реализации с привязкой к домену, а затем либо проводит её через test-driven миссии, которые вы проверяете по одной, либо передаёт автономному циклу `/goal` с проверяемыми условиями остановки.

## Ключевые идеи
- **Планирование через допрос**: как `/grill-me` Мэтта Покока, ab-method допрашивает задачу до плана с привязкой к домену перед написанием кода.
- **Два пути исполнения**: `/create-task` разбивает работу на миссии для индивидуальной проверки через TDD (human-in-the-loop); `/create-goal` генерирует промпт для автономного цикла `/goal` с проверяемыми условиями остановки.
- **Привязка к архитектуре**: `/analyze-project` создаёт глоссарий доменного языка и техдокументацию как базовую линию.
- **Управление отступлениями**: механизм handoff фиксирует побочные темы, обнаруженные при планировании, превращая их в отдельные задачи.
- **Автоопределяющий установщик**: `npx ab-method` находит каталоги `.claude/` и/или `.agents/` и разворачивает файлы workflow.

## Подробнее
ab-method относится к семейству spec-driven development наряду с BMAD, Spec-Kit и навыками Мэтта Покока, но отличается явной развилкой между контролируемым и автономным исполнением. Четырёхэтапный workflow — **Baseline → Sharpen → Build → Maintain** — отражает принцип harness-инженерии: репозиторий должен стать системой записи.

Автономный цикл `/goal` с проверяемыми условиями остановки решает одну из центральных проблем агентного кодинга — преждевременное объявление победы. Требуя проверяемые условия остановки заранее, ab-method заставляет цикл доказывать завершение, а не оценивать его самостоятельно.

## Связанные записи
- [[mattpocock-skills-repo]] ([Matt Pocock's Skills Repo](../tools/mattpocock-skills-repo.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development: From BMAD to Custom Skills](../tips/spec-driven-development-bmad.md))
- [[dual-brain-agentic-protocol]] ([Dual-Brain: Adversarial Two-Agent Workflow](../tools/dual-brain-agentic-protocol.md))
- [[github-spec-kit]] ([GitHub Spec-Kit](../tools/github-spec-kit.md))
