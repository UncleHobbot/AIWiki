---
title: "Microsoft Waza: CLI for Evaluating AI Agent Skills"
title_ru: "Microsoft Waza: CLI для оценки скиллов AI-агентов"
category: tools
tags: [microsoft, waza, agent-skills, evaluation, benchmarks, cli, github-copilot, testing]
aliases: [Waza CLI, waza, microsoft/waza, agent skill evaluator]
confidence: high
date: 2026-05-24
updated: 2026-05-24
sources:
  - https://github.com/microsoft/waza
---

## Summary
Waza is Microsoft's open-source Go CLI for creating, testing, measuring, and improving AI agent skills. It scaffolds eval suites, runs benchmarks, compares results across models, and integrates with CI/CD — designed to bring software engineering rigor to the emerging skill ecosystem.

## Key Ideas
- **Core workflow**: `waza init` → `waza new skill` → `waza new eval` → `waza run` → `waza compare` — from scaffolding to benchmark comparison in one CLI.
- **Record-from-prompt**: `waza new task from-prompt "<prompt>" <path>` runs a prompt through Copilot and generates a reusable task YAML with auto-inferred validators (response text, tool usage, invoked skills).
- **A/B testing mode** (`--baseline`): runs each task twice — without skill (baseline) and with skill (normal) — and computes improvement scores.
- **Multi-model comparison**: `waza run --model gpt4 --model sonnet` runs the same eval against multiple models; `waza compare` shows side-by-side results.
- **Auto skill discovery** (`--discover`): walks the directory tree for `SKILL.md` + `eval.yaml` pairs; `--strict` fails CI if any skill lacks coverage.
- **CI/CD integration**: `waza init` generates `.github/workflows/eval.yml` — evals run on every PR.
- **Token analysis**: `waza tokens count skills/` and `waza tokens suggest` identify token-heavy skills and suggest optimizations.
- **Available as Azure Developer CLI (azd) extension**.

## Details
Waza addresses a real gap in the agent skill ecosystem: skills are easy to write but hard to measure. The eval format is a YAML spec file referencing task definitions (prompts + expected validators) and a fixture directory. Tasks can be positive triggers (skill should activate) or negative triggers (skill should not activate).

The `waza check` command assesses skill readiness for submission — verifying frontmatter, trigger quality, and eval coverage. `waza suggest` uses Copilot to generate an eval suite from an existing `SKILL.md` based on its `USE FOR` / `DO NOT USE FOR` metadata.

Result caching (`--cache`) speeds up re-runs when only some tasks changed. Parallel execution (`--parallel --workers N`) is available for large eval suites.

**Project structure** (project mode):
```
project/
├── skills/{skill-name}/SKILL.md
└── evals/{skill-name}/
    ├── eval.yaml
    ├── tasks/*.yaml
    └── fixtures/
```

## Related Entries
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[github-copilot-sdk]] ([GitHub Copilot SDK](../tools/github-copilot-sdk.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))

---
<!-- RU -->

## Краткое описание
Waza — open-source Go CLI от Microsoft для создания, тестирования, измерения и улучшения скиллов AI-агентов. Генерирует eval-suite, запускает бенчмарки, сравнивает результаты по моделям и интегрируется с CI/CD.

## Ключевые идеи
- **Основной воркфлоу**: `waza init` → `waza new skill` → `waza new eval` → `waza run` → `waza compare`.
- **Запись из промпта**: `waza new task from-prompt` запускает промпт через Copilot и генерирует переиспользуемый task YAML с авто-валидаторами.
- **A/B-тестирование** (`--baseline`): каждая задача выполняется дважды — без скилла и со скиллом — и вычисляется прирост.
- **Multi-model сравнение**: запуск одних и тех же eval на нескольких моделях с сопоставлением результатов.
- **Авто-обнаружение скиллов** (`--discover`): сканирование дерева каталогов; `--strict` ломает CI, если у скилла нет покрытия.
- **CI/CD**: `waza init` генерирует `.github/workflows/eval.yml` — eval запускаются на каждый PR.
- **Анализ токенов**: `waza tokens count` и `waza tokens suggest` находят тяжёлые скиллы и предлагают оптимизации.

## Подробнее
Waza закрывает реальный пробел: скиллы легко написать, но сложно измерить. Формат eval — YAML-файл с задачами (промпт + ожидаемые валидаторы) и директорией fixtures. Задачи могут быть позитивными триггерами (скилл должен активироваться) или негативными (не должен).

`waza check` проверяет готовность скилла к публикации. `waza suggest` использует Copilot для генерации eval-suite из существующего `SKILL.md` на основе метаданных `USE FOR` / `DO NOT USE FOR`.

## Связанные записи
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[github-copilot-sdk]] ([GitHub Copilot SDK](../tools/github-copilot-sdk.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))
