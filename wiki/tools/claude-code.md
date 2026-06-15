---
title: "Claude Code"
title_ru: "Claude Code"
category: tools
tags: [claude, anthropic, coding-agent, terminal, claude-code]
date: 2026-06-14
updated: 2026-06-14
sources:
  - https://www.anthropic.com/claude-code
  - https://docs.anthropic.com/en/docs/claude-code/overview
---

## Summary

Claude Code is Anthropic's terminal-based AI coding agent powered by Claude models (Sonnet, Opus, Fable). It supports skills, hooks, long-running sessions, and integrates with GitHub. Subject to usage limits and subscription tiers. Recent discussions focus on Fable 5 integration, usage-limit bugs, and hooks/tools like Grind and Ship Skills.

## Key Ideas

- Terminal-native agent that edits files, runs shell commands, searches code, and creates pull requests via natural-language prompts.
- Built on Claude models with configurable model selection (Sonnet for speed, Opus for depth, Fable for extended or research tasks).
- Extensible through Skills (reusable prompt/tool packs) and Hooks (custom triggers and pipeline steps), enabling team-wide and CI-integrated workflows.
- Operates under Anthropic's usage tiers: rate and token limits vary by plan, which has become a frequent topic in community forums.

## Details

Claude Code is designed for deep codebase work. A typical session starts with `/init` or a natural-language task, then Claude reads relevant files, proposes edits, runs tests, and can push commits. It understands Git context, can be constrained by permission modes, and keeps a working memory of session decisions.

Skills let users package repeated instructions, conventions, and tool calls into reusable units. The broader Claude Code ecosystem includes community tools such as Ship Skills (release-pipeline skills) and Grind (non-stop / batch execution mode). Recent releases around Claude Fable 5 have renewed discussion about long-running research tasks, safety restrictions on AI-research use, and occasional "silent nerfing" concerns.

## Notable Quotes

> "Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster." — Anthropic

## Related Entries

- [[ship-skills-claude-code-pipeline]] ([Ship Skills — Claude Code Pipeline](ship-skills-claude-code-pipeline.md))
- [[grind-claude-code-nonstop]] ([Grind — Claude Code Nonstop](grind-claude-code-nonstop.md))
- [[claude-fable-5-mythos-5-release]] ([Claude Fable 5 / Mythos 5 Release](claude-fable-5-mythos-5-release.md))
- [[claude-fable-5-ai-research-restrictions]] ([Claude Fable 5 AI Research Restrictions](claude-fable-5-ai-research-restrictions.md))
- [[yet-another-statusline]] ([Yet Another Statusline (YAS): Claude Code Status Bar Tool](../tools/yet-another-statusline.md))

---
<!-- RU -->

## Краткое описание

Claude Code — терминальный AI-агент для кодинга от Anthropic на базе моделей Claude (Sonnet, Opus, Fable). Поддерживает навыки, хуки, длительные сессии и интеграцию с GitHub. Имеет лимиты использования и подписочные уровни. Недавние обсуждения посвящены интеграции Fable 5, багам с лимитами использования и инструментам/хукам вроде Grind и Ship Skills.

## Ключевые идеи

- Агент, изначально работающий в терминале: редактирует файлы, выполняет shell-команды, ищет по коду и создаёт pull request'ы по запросам на естественном языке.
- Построен на моделях Claude с выбором модели под задачу: Sonnet — скорость, Opus — глубина, Fable — долгие исследовательские задачи.
- Расширяется через Skills (reusable prompt/tool packs) и Hooks (триггеры и шаги пайплайна), что позволяет выстраивать командные и CI-интегрированные workflows.
- Работает в рамках подписочных уровней Anthropic: лимиты на запросы и токены зависят от тарифа, что часто обсуждается в сообществе.

## Подробнее

Claude Code заточен под глубокую работу с кодовой базой. Сессия обычно начинается с `/init` или текстовой задачи; Claude читает нужные файлы, предлагает правки, запускает тесты и может коммитить изменения. Он понимает Git-контекст, ограничивается режимами разрешений и сохраняет память о решениях внутри сессии.

Skills позволяют упаковывать повторяющиеся инструкции, соглашения и вызовы инструментов в reusable-единицы. В экосистеме Claude Code есть community-инструменты: Ship Skills (навыки для release-пайплайна) и Grind (режим непрерывного / batch-выполнения). Релизы Claude Fable 5 обострили дискуссии о долгих исследовательских задачах, ограничениях безопасности для AI-исследований и периодических жалобах на «тихий нерфинг».

## Примечательные цитаты

> "Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster." — Anthropic

## Связанные записи

- [[ship-skills-claude-code-pipeline]] ([Ship Skills — Claude Code Pipeline](ship-skills-claude-code-pipeline.md))
- [[grind-claude-code-nonstop]] ([Grind — Claude Code Nonstop](grind-claude-code-nonstop.md))
- [[claude-fable-5-mythos-5-release]] ([Claude Fable 5 / Mythos 5 Release](claude-fable-5-mythos-5-release.md))
- [[claude-fable-5-ai-research-restrictions]] ([Claude Fable 5 AI Research Restrictions](claude-fable-5-ai-research-restrictions.md))
- [[yet-another-statusline]] ([Yet Another Statusline (YAS): строка статуса для Claude Code](../tools/yet-another-statusline.md))
