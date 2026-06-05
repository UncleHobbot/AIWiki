---
title: "Dual-Brain: Adversarial Two-Agent Workflow with Tiered Project Memory"
title_ru: "Dual-Brain: состязательный двухагентный workflow с многоуровневой памятью проекта"
category: tools
tags: [claude-code, codex, agents, multi-agent, memory, skills, workflow, adversarial, hallucination-prevention]
aliases: [dual-brain, Dual-Brain protocol, sleeplesshan/dual-brain, right brain left brain agent]
confidence: high
updated: 2026-06-05
sources:
  - https://github.com/sleeplesshan/dual-brain
  - https://www.reddit.com/r/vibecoding/comments/1txlkuu/dual_brain_an_agentic_workflow_protocol/
---

## Summary
Dual-Brain is a portable Claude Code / Codex skill that routes hard tasks through two specialized debating sub-agents — a Right Brain that interrogates assumptions and a Left Brain that verifies claims against real code — preventing the three main single-agent failure modes: taking requests at face value, drowning in detail, and forgetting the project.

## Key Ideas
- **Structured adversarial debate**: Right Brain interrogates the request and grills unstated assumptions first; Left Brain then cross-checks every claim against actual code, docs, and project memory. Neither can skip the other.
- **Tiered project memory (MEMORY.md)**: Hot/Warm/Cold/Archived tiers weighted by recency and reference count. Hot Memory loads every session; Warm loads when relevant; Cold only on explicit need. Avoids stale decisions competing equally with active constraints.
- **Memory is advisory, not authoritative**: current code and official docs beat memory. Left Brain verifies memory against reality before using it — stale items get challenged and updated or demoted.
- **Auto-compaction**: when MEMORY.md gets noisy, Dual-Brain compacts it automatically — promoting active items, demoting stale ones, archiving superseded decisions, merging duplicates.
- **Install via SkillsGate**: `npx skillsgate add sleeplesshan/dual-brain -g` — works identically with Codex CLI and Claude Code.

## Details

### The Three Failure Modes It Fixes

| Failure mode | Symptom | Dual-Brain fix |
|---|---|---|
| Takes request at face value | Builds the wrong thing confidently, hallucinates APIs | Right Brain grills every assumption before anything is built |
| Drowns in detail | Gets lost in syntax, misses the smarter path | Right Brain holds the macro view; Left Brain does the syntax |
| Forgets the project | Re-litigates settled decisions every session | MEMORY.md persists durable decisions with tier weights |

### The 7-Step Cycle
1. **Memory intake** — load MEMORY.md, read Hot tier fully, Warm tier when relevant
2. **Orchestrator frames** — distill request into one shared paragraph with relevant memory
3. **Right Brain grills** — interrogates assumptions, defines ambiguous terms, flags stale memory
4. **Left Brain verifies** — cross-checks against codebase, docs, and memory; catches hallucinations
5. **Mediation (if needed)** — if verification refutes a core premise, Right Brain realigns (≤1 round, no loops)
6. **Dual synthesis** — single production-ready deliverable with documentation
7. **Auto-save memory** — update MEMORY.md, compact, ask user to review

### Memory Tier Format
```
## Hot Memory
- [decision][refs:3][last_referenced:2026-05-30] Use unified notification dispatcher.

## Warm Memory
- [constraint][refs:1][last_referenced:2026-05-12] Keep public API backward-compatible.

## Cold Memory
- [open-question][refs:0][last_referenced:2026-02-10] Should admin alerts use same dispatcher?

## Archived Decisions
- [superseded][archived:2026-05-30] Old "no webhook retries" constraint is obsolete.
```

### Benchmark Snapshot (Codex, 5-case suite)
| Metric | Single-agent | Dual-Brain |
|---|---|---|
| Pass rate | 3/5 | 4/5 |
| First-pass correctness | 1/5 | 3/5 |
| Human repair prompts | 2 | 1 |
| Memory regressions | 2/2 | 1/2 |

Dual-Brain is slower per attempt; it reduces the follow-up prompts needed after sloppy agent work.

### When to Use
Best for: vague or under-specified requests, unfamiliar API integration, architecture decisions, refactors with subtle correctness risks. Overkill for one-liners, renaming, pure boilerplate.

## Related Entries
- [[mattpocock-skills-repo]] ([Matt Pocock's Skills Repo](../tools/mattpocock-skills-repo.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin for Claude Code](../agents/superpowers-plugin-claude-code.md))
- [[memory-skills-unified-harness]] ([Memory and Skills as a Unified Harness](../concepts/memory-skills-unified-harness.md))
- [[agent-lifespan-agingbench]] ([Agent Lifespan Engineering: AgingBench](../concepts/agent-lifespan-agingbench.md))

---
<!-- RU -->

## Краткое описание
Dual-Brain — портативный skill для Claude Code и Codex, который направляет сложные задачи через двух специализированных агентов-оппонентов: Right Brain допрашивает допущения, Left Brain проверяет утверждения по реальному коду, предотвращая три главных режима сбоя одиночного агента.

## Ключевые идеи
- **Структурированный состязательный дебат**: Right Brain сначала допрашивает запрос и невысказанные допущения; Left Brain затем перекрёстно проверяет каждое утверждение по реальному коду, документации и памяти проекта.
- **Многоуровневая память проекта (MEMORY.md)**: уровни Hot/Warm/Cold/Archived, взвешенные по давности и счётчику обращений. Горячая память загружается каждую сессию; тёплая — по релевантности; холодная — только при явной необходимости.
- **Память совещательна, не авторитарна**: текущий код и официальная документация важнее памяти. Left Brain проверяет память по реальности перед использованием.
- **Автоматическая компакция**: при засорении MEMORY.md Dual-Brain сам её компактирует — продвигает активные записи, демотирует устаревшие, архивирует замещённые решения.
- **Установка через SkillsGate**: `npx skillsgate add sleeplesshan/dual-brain -g` — работает одинаково с Codex CLI и Claude Code.

## Подробнее

**7-шаговый цикл**: загрузка памяти → фреймирование оркестратором → допрос Right Brain → верификация Left Brain → медиация (при необходимости) → двойной синтез → авто-сохранение памяти.

**Бенчмарк (Codex, 5 кейсов):** Pass rate 3/5 → 4/5; first-pass correctness 1/5 → 3/5; prompts на исправление 2 → 1; memory regressions 2/2 → 1/2. Dual-Brain медленнее за попытку, но сокращает объём последующих правок от пользователя.

## Связанные записи
- [[mattpocock-skills-repo]] ([Matt Pocock's Skills Repo](../tools/mattpocock-skills-repo.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin для Claude Code](../agents/superpowers-plugin-claude-code.md))
- [[memory-skills-unified-harness]] ([Memory and Skills as a Unified Harness](../concepts/memory-skills-unified-harness.md))
- [[agent-lifespan-agingbench]] ([Agent Lifespan Engineering: AgingBench](../concepts/agent-lifespan-agingbench.md))
