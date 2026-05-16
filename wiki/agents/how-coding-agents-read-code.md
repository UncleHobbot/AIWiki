---
title: "How AI Coding Agents Really Read Code (Inside the Runtime)"
title_ru: "Как AI-агенты на самом деле читают код (внутри среды выполнения)"
category: agents
tags: [coding-agents, runtime, context-assembly, repository-exploration, failure-modes, rag, production-ai]
updated: 2026-05-16
transcript: unavailable
sources:
  - https://youtu.be/YXx4YQnu7Cs
---

## Summary
Leandro Damasio (AI Engineer in financial/legal domains, building production LLM/RAG systems) demystifies how coding agents actually interact with codebases at the runtime level — how they assemble context, navigate repositories, and why they fail on large or legacy systems.

## Key Ideas
- **Agents don't "read" code the way humans do**: they operate through a runtime loop that assembles context, navigates repos via tool calls, retrieves partial information, and makes decisions under strict token constraints.
- **Context assembly is the bottleneck**: the agent must decide what to load into its limited context window; wrong choices cascade into incorrect outputs even with a capable model.
- **Repository navigation is lossy**: agents explore code by sampling rather than full comprehension; they can miss critical files, misread inheritance chains, or fail to find relevant tests.
- **Large and legacy systems are failure-prone**: the longer the codebase, the more the agent has to guess about what it hasn't read; documentation and code structure directly impact agent effectiveness.
- **Engineers can help agents succeed**: understanding how agents read code lets you structure codebases, write documentation, and set up contexts that minimize agent failures.

## Video Notes
- No transcript available (429 Too Many Requests during yt-dlp subtitle fetch).
- Talk from AI Agents Montreal meetup (2026-02-28), speaker Leandro Damasio.
- Speaker background: AI Engineer in financial and legal domains, builds production-grade LLM and RAG systems in highly regulated environments; focus on reliability, observability, and governance.
- ~51 minute talk.

## Related Entries
- [[claude-code-agentic-loop]]
- [[acdc-agent-centric-development-cycle]]
- [[llm-assisted-coding-systems-perspective]]

---
<!-- RU -->

## Краткое описание
Леандро Дамасио (AI-инженер в финансовых и юридических областях, строящий production LLM/RAG-системы) демистифицирует, как агенты кодирования реально взаимодействуют с кодовыми базами на уровне среды выполнения — как они собирают контекст, навигируют по репозиториям и почему терпят неудачу на больших или легаси-системах.

## Ключевые идеи
- **Агенты «читают» код не так, как люди**: они работают через цикл среды выполнения, который собирает контекст, навигирует по репозиторию через вызовы инструментов, извлекает частичную информацию и принимает решения в условиях строгих ограничений по токенам.
- **Сборка контекста — это узкое место**: агент должен решить, что загрузить в ограниченное окно контекста; неверные решения каскадируют в некорректные выходы даже при способной модели.
- **Навигация по репозиторию потерялива**: агенты исследуют код путём семплирования, а не полного понимания; они могут пропустить критические файлы, неправильно прочитать цепочки наследования или не найти релевантные тесты.
- **Большие и легаси-системы склонны к сбоям**: чем длиннее кодовая база, тем больше агент должен угадывать о непрочитанном; документация и структура кода напрямую влияют на эффективность агента.
- **Инженеры могут помочь агентам преуспеть**: понимание того, как агенты читают код, позволяет структурировать кодовые базы, писать документацию и настраивать контексты, минимизирующие сбои агентов.

## Заметки по видео
- Транскрипт недоступен (ошибка 429 Too Many Requests при загрузке субтитров).
- Доклад на AI Agents Montreal meetup (2026-02-28), спикер Леандро Дамасио.
- Биография спикера: AI-инженер в финансовых и юридических областях, строит production LLM и RAG-системы в строго регулируемых средах; фокус на надёжности, наблюдаемости и управлении.
- Доклад ~51 минута.

## Связанные записи
- [[claude-code-agentic-loop]]
- [[acdc-agent-centric-development-cycle]]
- [[llm-assisted-coding-systems-perspective]]
