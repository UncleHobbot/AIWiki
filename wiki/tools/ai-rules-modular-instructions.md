---
title: "ai-rules: Modular, Reusable AI Instruction Files Instead of One Giant AGENTS.md"
title_ru: "ai-rules: модульные переиспользуемые файлы инструкций вместо одного гигантского AGENTS.md"
category: tools
tags: [agents-md, instructions, modular, prompt-engineering, claude-code, opencode]
aliases: [ai-rules, SalzDevs/ai-rules, modular AI instructions]
confidence: medium
updated: 2026-06-29
sources:
  - https://github.com/SalzDevs/ai-rules
  - https://www.reddit.com/r/opencode/comments/1ugnoo5/i_got_tired_of_rewriting_the_same_ai_instructions/
---

## Summary
ai-rules is a local-first, Git-friendly tool that breaks the monolithic `AGENTS.md`/`CLAUDE.md`/`GEMINI.md` instruction file into small, reusable, composable rule modules — so you include only the rules relevant to the current task instead of forcing every instruction into every context. It is model- and agent-agnostic.

## Key Ideas
- **The monolith problem**: every project ends up with a massive instruction file where half the rules aren't relevant to the current task, and the same rules get copied between repositories.
- **Modular rules**: small, single-purpose rules (e.g., Rust safety, Go error handling, commit-message style, testing philosophy, architecture preferences) that you compose when prompting, instead of one giant wall of text.
- **Treat instructions as reusable modules**, not as a static blob — closer to how code dependencies work.
- **Local-first and Git-friendly**: no cloud dependency; rules version alongside code. Not tied to any specific model or coding agent.
- **Example composition**: `ai-rules add go/error-handling` pulls just that rule into the active context.

## Details
The tool reflects a maturing view of "context engineering": an agent's behavior is governed by which instructions are loaded, and loading everything all the time wastes context window and dilutes signal. By making rules first-class, addressable units that can be added on demand, ai-rules lets the instruction set scale with the project without bloating every single prompt.

This is conceptually adjacent to the skills/plugins movement (loadable, on-demand capability/context injection) but focused specifically on the prose-instruction layer that typically lives in AGENTS.md-style files.

## Related Entries
- [[memory-skills-unified-harness]] ([Memory and Skills Are the Same Harness](../concepts/memory-skills-unified-harness.md))
- [[stop-slop-skill]] ([stop-slop Skill](stop-slop-skill.md))
- [[dotnet-agent-skills]] ([.NET Agent Skills](dotnet-agent-skills.md))

---
<!-- RU -->

## Краткое описание
ai-rules — local-first, Git-friendly инструмент, разбивающий монолитный файл инструкций `AGENTS.md`/`CLAUDE.md`/`GEMINI.md` на маленькие, переиспользуемые, компонуемые модули-правила, чтобы подключать только релевантные текущей задаче правила вместо заталкивания всех инструкций в каждый контекст. Не зависит от конкретной модели или агента.

## Ключевые идеи
- **Проблема монолита**: в каждом проекте вырастает гигантский файл инструкций, где половина правил не относится к текущей задаче, а одни и те же правила копируются между репозиториями.
- **Модульные правила**: маленькие правила с одной целью (безопасность Rust, обработка ошибок в Go, стиль коммит-сообщений, философия тестирования, архитектурные предпочтения), которые компонуются при промптинге.
- **Отношение к инструкциям как к переиспользуемым модулям**, а не как к статичному куску — ближе к тому, как работают зависимости в коде.
- **Local-first и Git-friendly**: без облачной зависимости; правила версионируются вместе с кодом.
- **Пример композиции**: `ai-rules add go/error-handling` подтягивает только это правило в активный контекст.

## Подробнее
Инструмент отражает взрослеющий взгляд на «context engineering»: поведение агента определяется тем, какие инструкции загружены, а загрузка всего подряд расходует окно контекста и размывает сигнал. Сделав правила полноправными адресуемыми единицами, добавляемыми по требованию, ai-rules позволяет набору инструкций масштабироваться вместе с проектом, не раздувая каждый промпт.

Концептуально это примыкает к движению skills/plugins (загружаемые по требованию capability/context), но сфокусировано именно на уровне прозаических инструкций, обычно живущих в AGENTS.md-файлах.

## Связанные записи
- [[memory-skills-unified-harness]] ([Memory and Skills Are the Same Harness](../concepts/memory-skills-unified-harness.md))
- [[stop-slop-skill]] ([stop-slop Skill](stop-slop-skill.md))
- [[dotnet-agent-skills]] ([.NET Agent Skills](dotnet-agent-skills.md))
