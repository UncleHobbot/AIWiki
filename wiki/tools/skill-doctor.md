---
title: "Skill Doctor: A Skill That Diagnoses and Improves Your Skills"
title_ru: "Skill Doctor: навык, который диагностирует и улучшает ваши навыки"
category: tools
tags: [claude-code, skills, meta-tooling, evaluation, audit, codex, warp, skill-quality, plugin]
aliases: [skill-doctor, /skill-doctor, Skill Doctor plugin]
confidence: high
date: 2026-08-30
updated: 2026-08-30
sources:
  - https://github.com/JoaquinCampo/skill-doctor
  - https://x.com/BHolmesDev/status/2093370341418582346
  - https://www.warp.dev/skill-doctor
---

## Summary
Skill Doctor is a meta-skill that audits your other Claude Code skills — crawling past Claude Code, Codex, or Warp conversations, scoring them for efficiency and code quality, and proposing concrete diffs to the skill files that caused failures.

## Key Ideas
- **Learns from your actual transcripts**: rather than reviewing skills in the abstract, it crawls real past conversations and identifies where the agent needed human intervention or had to course-correct around bad instructions.
- **Two runtime rubrics (0–1 scale)**: *efficiency* (did the agent require extra human intervention or course-correct around bad docs?) and *code quality* (does the output follow the codebase's architecture standards?). It then filters to failed cases and looks for patterns a skill patch could fix.
- **Nine static audit criteria**: avoids stating the obvious · has a Gotchas section · uses progressive disclosure · avoids railroading · description optimized for triggering · setup/config pattern · includes scripts/code · on-demand hooks · memory/data storage.
- **Subagent batching**: conversations are split across subagent batches for parallel scoring — a practical use of the parallel-subagent pattern.
- **Tiered verdicts**: skills are classified and assigned a tier (Minimal / Standard / Rich); verdicts range from "Strong" (no high-severity findings) to "Needs Work". Inapplicable criteria get N/A rather than a penalty.

## Details
Skill Doctor closes a real gap in the skills ecosystem: skill authoring guidance exists (Anthropic's official guide, community conventions), but nothing measured whether a given skill actually helped in practice. By scoring transcripts rather than the skill text alone, Skill Doctor grounds its recommendations in observed failures.

The two-mode design is what makes it useful. **Audit mode** is static: it walks skill directories, examines every file (docs, references, scripts, config), runs structural checks via bundled bash scripts, and reports findings with `file:line` evidence. **Transcript mode** is empirical: it scores real sessions and traces failures back to the skill that should have prevented them.

The nine criteria encode the emerging consensus on what separates a good skill from a mediocre one — particularly *avoids railroading* (a skill that over-prescribes fails on variations) and *description optimized for triggering* (the single most common reason a skill never loads, matching Anthropic's own guidance that vague descriptions are the top failure mode).

### Installation
```
/plugin marketplace add JoaquinCampo/skill-doctor
/plugin install skill-doctor@skill-doctor-marketplace
```
Restart Claude Code, then `/skill-doctor` becomes available.

## Related Entries
- [[anthropic-skills-building-guide]] ([Anthropic's Complete Guide to Building Skills](../tips/anthropic-skills-building-guide.md))
- [[mattpocock-skills-repo]] ([Matt Pocock's Skills Repo](../tools/mattpocock-skills-repo.md))
- [[microsoft-waza]] ([Microsoft Waza: CLI for Evaluating Agent Skills](../tools/microsoft-waza.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))

---
<!-- RU -->

## Краткое описание
Skill Doctor — мета-навык, который проверяет остальные ваши навыки Claude Code: обходит прошлые диалоги Claude Code, Codex или Warp, оценивает их по эффективности и качеству кода и предлагает конкретные диффы к файлам навыков, вызвавших сбои.

## Ключевые идеи
- **Учится на ваших реальных транскриптах**: вместо абстрактной проверки навыков он обходит настоящие прошлые диалоги и находит места, где агенту потребовалось вмешательство человека или коррекция курса из-за плохих инструкций.
- **Две рабочие рубрики (шкала 0–1)**: *эффективность* (потребовалось ли вмешательство человека?) и *качество кода* (соответствует ли вывод архитектурным стандартам кодовой базы). Затем фильтрует неуспешные случаи и ищет паттерны, которые исправит патч навыка.
- **Девять критериев статического аудита**: не констатирует очевидное · есть раздел Gotchas · использует прогрессивное раскрытие · не загоняет в рельсы · описание оптимизировано под срабатывание · паттерн настройки · содержит скрипты · hooks по требованию · хранение памяти/данных.
- **Батчинг субагентов**: диалоги распределяются по батчам субагентов для параллельной оценки.
- **Многоуровневые вердикты**: навыкам присваивается уровень (Minimal / Standard / Rich); вердикты — от «Strong» (нет находок высокой серьёзности) до «Needs Work».

## Подробнее
Skill Doctor закрывает реальный пробел в экосистеме навыков: руководства по написанию навыков существуют, но ничто не измеряло, помог ли конкретный навык на практике. Оценивая транскрипты, а не только текст навыка, Skill Doctor обосновывает рекомендации наблюдаемыми сбоями.

Полезной его делает двухрежимная конструкция. **Режим аудита** статичен: обход каталогов навыков, проверка всех файлов, структурные проверки через встроенные bash-скрипты, отчёт с доказательствами вида `file:line`. **Режим транскриптов** эмпиричен: оценка реальных сессий и трассировка сбоев обратно к навыку, который должен был их предотвратить.

Девять критериев кодифицируют складывающийся консенсус о том, что отличает хороший навык — особенно *не загоняет в рельсы* (чрезмерно предписывающий навык ломается на вариациях) и *описание оптимизировано под срабатывание* (самая частая причина, по которой навык вообще не загружается).

## Связанные записи
- [[anthropic-skills-building-guide]] ([Полное руководство Anthropic по созданию навыков](../tips/anthropic-skills-building-guide.md))
- [[mattpocock-skills-repo]] ([Репозиторий навыков Мэтта Покока](../tools/mattpocock-skills-repo.md))
- [[microsoft-waza]] ([Microsoft Waza: CLI для оценки навыков агентов](../tools/microsoft-waza.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))
