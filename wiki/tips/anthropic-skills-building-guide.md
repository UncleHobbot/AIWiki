---
title: "Anthropic's Complete Guide to Building Skills for Claude"
title_ru: "Полное руководство Anthropic по созданию навыков для Claude"
category: tips
tags: [claude-skills, anthropic, skill-building, mcp, agent-sdk, progressive-disclosure, testing, distribution]
aliases: [building skills for claude, claude skills guide, skills building guide, SKILL.md guide]
confidence: high
updated: 2026-05-28
sources:
  - https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
---

## Summary
Anthropic's official 32-page guide covering the full lifecycle of building Claude skills — from SKILL.md structure and YAML frontmatter through testing frameworks, distribution patterns, and five orchestration patterns. The definitive reference for skill authors.

## Key Ideas
- **Progressive disclosure architecture**: frontmatter (always loaded) → SKILL.md body (loaded when relevant) → linked files (loaded on demand). Minimizes token usage while maintaining specialized expertise.
- **`SKILL.md` is case-sensitive** — exact name required; `skill.md` or `SKILL.MD` will fail to load.
- **Description field is the most critical part** — it must include both *what the skill does* and *when to use it* (trigger phrases); vague descriptions cause skills to never load.
- **Three use case categories**: Document & Asset Creation, Workflow Automation, and MCP Enhancement (workflow guidance on top of MCP tool access).
- **Skills work across all Claude surfaces** — Claude.ai, Claude Code, and API without modification (if dependencies are met).

## Details

### YAML Frontmatter Requirements

```yaml
---
name: skill-name-in-kebab-case       # required, kebab-case only
description: What it does. Use when user asks to [phrases].  # required, max 1024 chars
license: MIT                          # optional
metadata:
  author: YourName
  version: 1.0.0
  mcp-server: server-name             # optional
---
```

**Forbidden in frontmatter**: XML angle brackets (`< >`), skills named with "claude" or "anthropic" prefix (reserved).

### The Description Field

Must contain both the **what** and the **when**. The system uses this to decide whether to load the skill at all — if it's vague, the skill never activates.

Good: `"Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for 'design specs', or 'design-to-code handoff'."`

Bad: `"Helps with projects."` — too vague, won't trigger.

**Debugging undertriggering**: Ask Claude "When would you use the [skill name] skill?" — it will quote the description back, revealing what's missing.

### Five Orchestration Patterns

1. **Sequential workflow** — explicit step ordering with validation gates and rollback instructions
2. **Multi-MCP coordination** — data passing between multiple MCP servers with clear phase separation
3. **Iterative refinement** — quality check → fix loop with explicit stopping criteria
4. **Context-aware tool selection** — decision tree for picking the right tool per scenario
5. **Domain-specific intelligence** — embeds compliance rules, audit trails, or governance logic directly in the skill

### Testing Framework

- **Triggering tests** (90% trigger rate goal on relevant queries)
- **Functional tests** (verify outputs, API calls, edge cases)
- **Performance comparison** — measure tokens consumed and back-and-forth messages with vs. without the skill

Baseline example: same task without skill = 15 messages, 12k tokens; with skill = 2 clarifying questions, 6k tokens.

### Distribution Model

1. Host on GitHub (public repo, clear README — **separate** from skill folder, which should not contain README.md)
2. Document in your MCP repo with a link and quick-start guide
3. Admins can deploy org-wide via Claude.ai Console (since December 2025)
4. API: `/v1/skills` endpoint + `container.skills` parameter in Messages API (requires Code Execution Tool beta)

### Skills + MCP "Kitchen Analogy"

MCP = professional kitchen (tools, ingredients, access). Skills = recipes (step-by-step instructions). Together they enable complex workflows without users needing to know every step.

## Notable Quotes
> "Skills are living documents. Plan to iterate based on undertriggering signals, overtriggering signals, and execution issues." — Anthropic

## Related Entries
- [[mattpocock-skills-repo]] ([Matt Pocock's Skills Repo](../tools/mattpocock-skills-repo.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills Collection](../tools/awesome-agent-skills.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide](../tips/claude-code-plugins-guide.md))
- [[memory-skills-unified-harness]] ([Memory and Skills as a Unified Harness](../concepts/memory-skills-unified-harness.md))

---
<!-- RU -->

## Краткое описание
Официальное руководство Anthropic на 32 страницах, охватывающее полный цикл создания навыков для Claude — от структуры SKILL.md и YAML frontmatter до фреймворков тестирования, паттернов дистрибуции и пяти паттернов оркестрации.

## Ключевые идеи
- **Архитектура прогрессивного раскрытия**: frontmatter (всегда загружается) → тело SKILL.md (загружается при необходимости) → связанные файлы (загружаются по требованию). Минимизирует использование токенов.
- **`SKILL.md` чувствителен к регистру** — требуется точное написание; `skill.md` или `SKILL.MD` не будут загружены.
- **Поле description — самая критичная часть** — должно содержать и *что делает навык*, и *когда его использовать* (фразы-триггеры).
- **Три категории use case**: создание документов и артефактов, автоматизация рабочих процессов и улучшение MCP (руководство по workflow поверх инструментов MCP).
- **Навыки работают на всех платформах Claude** — Claude.ai, Claude Code и API без изменений.

## Подробнее

**Пять паттернов оркестрации:**
1. **Последовательный workflow** — явный порядок шагов с контрольными точками валидации
2. **Координация нескольких MCP** — передача данных между MCP-серверами с чёткими фазами
3. **Итеративное улучшение** — цикл проверки качества с явным критерием остановки
4. **Выбор инструмента по контексту** — дерево решений для выбора правильного инструмента
5. **Встроенная доменная экспертиза** — правила compliance, аудит-трейлы, governance прямо в навыке

**Отладка срабатывания**: если навык не загружается, спросите Claude «Когда ты бы использовал навык [название]?» — он процитирует описание и покажет, чего не хватает.

**Аналогия кухни**: MCP = профессиональная кухня (инструменты, доступ). Навыки = рецепты (пошаговые инструкции). Вместе они позволяют выполнять сложные задачи без необходимости объяснять каждый шаг.

## Связанные записи
- [[mattpocock-skills-repo]] ([Matt Pocock's Skills Repo](../tools/mattpocock-skills-repo.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills Collection](../tools/awesome-agent-skills.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide](../tips/claude-code-plugins-guide.md))
- [[memory-skills-unified-harness]] ([Memory and Skills as a Unified Harness](../concepts/memory-skills-unified-harness.md))
