---
title: "Visual Explainer"
title_ru: "Visual Explainer"
category: tools
tags: [claude-code, agent-skills, html, diagrams, visualization, codex, opencode]
updated: 2026-05-16
sources:
  - https://github.com/nicobailon/visual-explainer
---

## Summary
An agent skill that replaces ASCII art and terminal tables with styled, self-contained HTML pages featuring real typography, dark/light themes, interactive Mermaid diagrams, and Chart.js dashboards — no build step required.

## Key Ideas
- Generates rich HTML output instead of box-drawing characters when you ask for diagrams, diffs, plan reviews, or data tables (auto-triggers for tables with 4+ rows or 3+ columns).
- Core commands: `/generate-web-diagram`, `/diff-review`, `/plan-review`, `/project-recap`, `/generate-slides`, `/fact-check`, `/share-page`.
- All generated HTML is self-contained and saved to `~/.agent/diagrams/` then opened in the browser automatically.
- Compatible with: Claude Code (marketplace plugin), Pi, Codex CLI, OpenCode, Cursor (rules-based), and OpenClaw.
- Add `--slides` to any command to generate a magazine-quality slide deck instead of a web page.

## Details
Every coding agent defaults to ASCII art for diagrams and monospace tables for data comparisons. For non-trivial structures, these break down: 15-row comparison tables become unreadable walls of pipes and dashes. Visual Explainer intercepts those cases and generates real HTML instead.

The skill routes output to the right renderer automatically: Mermaid for flowcharts (with interactive zoom/pan), CSS Grid for architecture overviews, HTML tables for structured data, Chart.js for dashboards. The generated pages support dark/light OS theme switching.

Installation varies by harness:
- **Claude Code**: `/plugin marketplace add nicobailon/visual-explainer` then `/plugin install visual-explainer@visual-explainer-marketplace`
- **Pi**: `pi install git:github.com/nicobailon/visual-explainer`
- **Codex / OpenCode**: manual copy of `plugins/visual-explainer/` to the harness skill directory

The `/share-page` command deploys the generated HTML to Vercel and returns a live URL (requires a `vercel-deploy` Pi skill).

## Related Entries
- [[claude-code-plugins-guide]]
- [[claude-code-extensions-overview]]
- [[awesome-agent-skills]]

---
<!-- RU -->

## Краткое описание
Agent skill, заменяющий ASCII-арт и терминальные таблицы стилизованными самодостаточными HTML-страницами с реальной типографикой, тёмной/светлой темой, интерактивными диаграммами Mermaid и дашбордами Chart.js — без шага сборки.

## Ключевые идеи
- Генерирует HTML-вывод вместо символов рисования рамок при запросе диаграмм, diff-обзоров, планов или таблиц данных (автоматически срабатывает для таблиц с 4+ строками или 3+ столбцами).
- Основные команды: `/generate-web-diagram`, `/diff-review`, `/plan-review`, `/project-recap`, `/generate-slides`, `/fact-check`, `/share-page`.
- Весь сгенерированный HTML самодостаточен, сохраняется в `~/.agent/diagrams/` и автоматически открывается в браузере.
- Совместим с: Claude Code (marketplace плагин), Pi, Codex CLI, OpenCode, Cursor (на основе правил), OpenClaw.
- Добавьте `--slides` к любой команде, чтобы получить качественную слайд-деку вместо веб-страницы.

## Подробнее
Все агенты по умолчанию используют ASCII-арт для диаграмм и монопространственные таблицы для данных. При сложных структурах это плохо работает: таблицы сравнения на 15 строк превращаются в нечитаемые стены символов. Visual Explainer перехватывает такие случаи и генерирует HTML.

Навык автоматически выбирает подходящий рендерер: Mermaid для блок-схем (с интерактивным зумом), CSS Grid для обзора архитектуры, HTML-таблицы для структурированных данных, Chart.js для дашбордов. Страницы поддерживают переключение тёмной/светлой темы ОС.

Установка зависит от агента:
- **Claude Code**: `/plugin marketplace add nicobailon/visual-explainer`, затем `/plugin install visual-explainer@visual-explainer-marketplace`
- **Pi**: `pi install git:github.com/nicobailon/visual-explainer`
- **Codex / OpenCode**: ручное копирование `plugins/visual-explainer/` в директорию навыков агента

Команда `/share-page` деплоит HTML на Vercel и возвращает живую ссылку (требует навык `vercel-deploy` для Pi).

## Связанные записи
- [[claude-code-plugins-guide]]
- [[claude-code-extensions-overview]]
- [[awesome-agent-skills]]
