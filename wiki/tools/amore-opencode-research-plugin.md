---
title: "amore — OpenCode Plugin for Researchers"
title_ru: "amore — плагин OpenCode для исследователей"
category: tools
tags: [opencode, research, obsidian, literature-wiki, plugin]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/lubludrova/ah-my-openresearch
  - https://www.reddit.com/r/opencodeCLI/comments/1u2udn5/i_built_amore_ahmyopenresearch_an_opencode_plugin/
---

## Summary

OpenCode plugin that turns the coding agent into a research lab environment with 6 research personas, bundled skills, optional Obsidian literature-wiki support, and a project-local `lab/` directory for claims, ideas, experiments, and provenance tracking.

## Key Ideas

- 6 specialized research personas that shape how the agent approaches academic work
- Project-local `lab/` directory structure for claims, ideas, experiment notes, provenance, and handoffs
- Optional Markdown/Obsidian literature-wiki integration for knowledge graph building
- Bundled skills tailored for literature review, hypothesis generation, and experiment design
- Bridges the gap between coding agents and research workflows — OpenCode becomes a research companion, not just a code assistant

## Details

amore (ah-my-openresearch) addresses a gap in the OpenCode ecosystem: most plugins target software engineering, but researchers who code need different workflows. The plugin ships 6 research personas — each one configures the agent's system prompt, tone, and approach for different research phases (e.g., literature review, hypothesis formulation, experiment design, writing).

The `lab/` directory is the plugin's core contribution. Created inside the project root, it provides a structured place for research artifacts: claim files (assertions backed by evidence), idea files (hypotheses and open questions), experiment notes (results and parameters), provenance records (where did this claim come from?), and handoff documents (state of research for the next session).

The optional Obsidian integration means the plugin can write literature notes directly into an Obsidian vault, complete with wikilinks and frontmatter. This is particularly useful for researchers who already maintain a Zettelkasten or literature-wiki in Obsidian and want the agent to contribute to it rather than produce throwaway notes.

## Related Entries

- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG](../tools/opencoderag-rag-plugin.md))
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo-Code](../tools/mimo-code-xiaomi-opencode-fork.md))

---
<!-- RU -->

## Краткое описание

Плагин OpenCode, превращающий агент кодирования в исследовательскую лабораторию с 6 исследовательскими персонами, встроенными навыками, опциональной интеграцией с Obsidian literature-wiki и локальной директорией `lab/` для утверждений, идей, экспериментов и отслеживания происхождения данных.

## Ключевые идеи

- 6 специализированных исследовательских персон, определяющих подход агента к академической работе
- Локальная директория `lab/` со структурой для утверждений (claims), идей, записей экспериментов, происхождения (provenance) и передачи контекста (handoffs)
- Опциональная интеграция с Markdown/Obsidian literature-wiki для построения графа знаний
- Встроенные навыки для обзора литературы, генерации гипотез и планирования экспериментов
- Мост между агентами кодирования и исследовательскими workflow — OpenCode становится исследовательским компаньоном, а не только помощником в коде

## Подробнее

amore (ah-my-openresearch) заполняет пробел в экосистеме OpenCode: большинство плагинов нацелены на программную инженерию, но исследователи, пишущие код, нуждаются в других рабочих процессах. Плагин включает 6 исследовательских персон — каждая настраивает системный промпт, тон и подход агента для разных фаз исследования (обзор литературы, формулировка гипотез, планирование экспериментов, написание).

Директория `lab/` — ключевой вклад плагина. Создаваемая в корне проекта, она предоставляет структурированное место для исследовательских артефактов: файлы утверждений (claims, подкреплённые доказательствами), файлы идей (гипотезы и открытые вопросы), записи экспериментов (результаты и параметры), записи происхождения (откуда взялось утверждение?) и документы передачи контекста (состояние исследования для следующей сессии).

Опциональная интеграция с Obsidian означает, что плагин может записывать заметки по литературе напрямую в хранилище Obsidian с wikilinks и frontmatter. Это особенно полезно для исследователей, которые уже ведут Zettelkasten или literature-wiki в Obsidian и хотят, чтобы агент пополнял его, а не создавал одноразовые заметки.

## Связанные записи

- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG](../tools/opencoderag-rag-plugin.md))
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo-Code](../tools/mimo-code-xiaomi-opencode-fork.md))
