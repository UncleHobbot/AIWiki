---
title: "AC/DC — Agent-Centric Development Cycle"
title_ru: "AC/DC — Агентно-ориентированный цикл разработки"
category: agents
tags: [ai-agents, sdlc, developer-experience, sonar, agent-centric, dev-cycle]
updated: 2026-05-16
sources:
  - https://youtu.be/YXXFjebvfNc
---

## Summary
Edgar Kussberg (Product Director at SonarQube, former AI strategy lead at SNIK) presents the Agent-Centric Development Cycle (AC/DC) — a framework for restructuring the entire SDLC around AI agents rather than treating agents as add-ons to existing workflows.

## Key Ideas
- **AC/DC reframes the SDLC**: instead of inserting AI tools into an existing developer workflow, the entire development cycle is redesigned around what AI agents can and cannot do reliably.
- **Trust and verify is non-negotiable**: AI is not AGI — it can confidently produce wrong answers (e.g., "yes there's a recipe for gasoline-infused spaghetti"). Verification gates must be built into the workflow.
- **Adoption is still early**: many companies say "we use AI" but mean "we gave everyone Copilot" — actual agentic cloud usage remains a next frontier most organizations haven't crossed.
- **Developer experience → Agent experience**: as agents become first-class participants in development, the tools and feedback loops traditionally designed for humans need to evolve for agents too.
- **SonarQube in the AI era**: code quality gates that used to serve developers now also serve as verification signals for agents — "is the output of this agent any good?"

## Video Notes
- [~5:00] Historical arc: personal PCs hosting websites → cloud computing → orchestration (Docker, K8s) → AI dev tooling. Each step reduced friction; agentic cloud is the next step.
- [~8:00] Edgar distinguishes "gave everyone Copilot" from actually using agents in automated pipelines — a meaningful gap in sophistication.
- Talk from AI Agents Montreal meetup (2026-04-14), speaker Edgar Kussberg (Switzerland).
- Edgar works on MCP, CLI, and IDE tooling — everything at the intersection of developer/agent experience.

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[llm-assisted-coding-systems-perspective]] ([LLM-Assisted Coding: A Systems Perspective](../tips/llm-assisted-coding-systems-perspective.md))
- [[nwave-ai-refactoring-framework]] ([nWave: AI-Guided Refactoring Framework for Legacy Code](../tools/nwave-ai-refactoring-framework.md))
- [[new-organizational-models-ai-agents]] ([New Organizational Models for the Age of AI Agents](../agents/new-organizational-models-ai-agents.md))

---
<!-- RU -->

## Краткое описание
Эдгар Кусберг (Product Director в SonarQube, бывший руководитель AI-стратегии в SNIK) представляет Agent-Centric Development Cycle (AC/DC) — фреймворк для перестройки всего SDLC вокруг AI-агентов, а не добавления агентов как надстройки к существующим процессам.

## Ключевые идеи
- **AC/DC переосмысляет SDLC**: вместо встраивания AI-инструментов в существующий рабочий процесс разработчика весь цикл разработки перепроектируется с учётом того, что AI-агенты могут и не могут делать надёжно.
- **Доверяй и проверяй — обязательно**: AI — это не AGI; он может уверенно давать неправильные ответы. В рабочий процесс должны быть встроены этапы верификации.
- **Принятие всё ещё на раннем этапе**: многие компании говорят «мы используем AI», имея в виду «мы раздали всем Copilot» — реальное использование агентов в облаке остаётся следующим рубежом, которого большинство организаций не достигло.
- **Опыт разработчика → опыт агента**: по мере того, как агенты становятся полноправными участниками разработки, инструменты и петли обратной связи, традиционно разработанные для людей, должны эволюционировать и для агентов.
- **SonarQube в эпоху AI**: шлюзы качества кода, которые раньше служили разработчикам, теперь также служат сигналами верификации для агентов — «хорош ли выход этого агента?»

## Заметки по видео
- [~5:00] Историческая дуга: личные ПК с хостингом сайтов → облачные вычисления → оркестрация (Docker, K8s) → AI-инструменты для разработки. Каждый шаг снижал трение; агентное облако — следующий шаг.
- [~8:00] Эдгар различает «раздал всем Copilot» и реальное использование агентов в автоматизированных пайплайнах — существенная разница в зрелости.
- Доклад на AI Agents Montreal meetup (2026-04-14), спикер Эдгар Кусберг (Швейцария).
- Работает с MCP, CLI и IDE-инструментарием — всем, что находится на пересечении опыта разработчика и агента.

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[llm-assisted-coding-systems-perspective]] ([LLM-Assisted Coding: A Systems Perspective](../tips/llm-assisted-coding-systems-perspective.md))
- [[nwave-ai-refactoring-framework]] ([nWave: AI-Guided Refactoring Framework for Legacy Code](../tools/nwave-ai-refactoring-framework.md))
- [[new-organizational-models-ai-agents]] ([New Organizational Models for the Age of AI Agents](../agents/new-organizational-models-ai-agents.md))
