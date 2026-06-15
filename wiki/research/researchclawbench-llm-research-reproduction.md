---
title: "ResearchClawBench: LLMs Score Only ~20-26/100 at Reproducing Scientific Research"
title_ru: "ResearchClawBench: LLM набирают лишь ~20-26/100 при воспроизведении научных исследований"
category: research
tags: [benchmark, claude-opus, research-agents, evaluation, arxiv, limitations]
aliases: [ResearchClawBench]
confidence: medium
updated: 2026-06-14
sources:
  - https://arxiv.org/html/2606.07591v2
  - https://www.reddit.com/r/ClaudeCode/comments/1u5i02h/researchclawbench_we_should_all_humble_down/
---

## Summary
A new benchmark, ResearchClawBench, gives AI systems an expert-prepared package (research question, literature, raw data, tools, executable workspace) and asks them to independently reproduce a hidden paper's core results — Claude Code with Opus 4.6 scored only 21.5/100, and even the best model picked per-task averaged just 26.5/100.

## Key Ideas
- Setup: the AI receives everything a human researcher would need (question, relevant literature, raw data, tools, workspace) but not the target paper, its conclusions, or the correct analytical path.
- The AI must independently choose methods, run analyses, generate evidence/figures, and write a report.
- Scoring (0-100, graded against expert rubrics from the hidden paper): 50 = recovered the target paper's result; below 50 = failed to reach the original; above 50 = found something beyond the original work.
- Reported scores: Claude Code with Opus 4.6 = 21.5; Claude Opus 4.7 in "ResearchHarness" = 20.7; best model selected separately per task = 26.5.
- All scores are far below the 50-point threshold for simply reproducing known results, let alone exceeding them.

## Details
This benchmark targets a capability gap distinct from coding-agent benchmarks (SWE-bench, Agent Arena, etc.): independent scientific reasoning under realistic conditions — given the raw materials but not the answer, can an AI conduct a study the way a competent researcher would? The headline finding is that even frontier models (Claude Opus 4.6/4.7 in agentic harnesses) are far from reliably reproducing established results, scoring roughly 20-26 out of 100 against expert rubrics.

The Reddit poster (r/ClaudeCode, Tier 3 framing of a Tier 1 arXiv source) used this to argue against over-trusting LLM-generated "novel research" claims — if models can't even reliably reproduce known findings when given all the raw materials, claims of producing genuinely new scientific insight should be treated with significant skepticism. This is a useful counterweight to more optimistic framings of "AI researcher" capabilities and is relevant to anyone evaluating AI-assisted research workflows (including this wiki's own research/ entries, which should be held to similar scrutiny).

## Related Entries
- [[claude-agent-sdk-credit-june-2026]] ([Anthropic Agent SDK Credit Change](../news/claude-agent-sdk-credit-june-2026.md))

---
<!-- RU -->

## Краткое описание
Новый бенчмарк ResearchClawBench даёт AI-системам подготовленный экспертами пакет (вопрос исследования, литература, исходные данные, инструменты, рабочее окружение) и просит самостоятельно воспроизвести ключевые результаты скрытой статьи — Claude Code с Opus 4.6 набрал лишь 21.5 из 100, а лучшая модель, выбранная отдельно под каждую задачу, в среднем дала только 26.5.

## Ключевые идеи
- Постановка: AI получает всё, что нужно исследователю-человеку (вопрос, релевантную литературу, исходные данные, инструменты, рабочее окружение), но не саму целевую статью, её выводы или правильный путь анализа.
- AI должен самостоятельно выбрать методы, провести анализ, создать доказательства/графики и написать отчёт.
- Оценка (0-100, по экспертным рубрикам из скрытой статьи): 50 = воспроизведён результат целевой статьи; ниже 50 = не достигнут уровень оригинала; выше 50 = найдено что-то сверх оригинальной работы.
- Полученные оценки: Claude Code с Opus 4.6 = 21.5; Claude Opus 4.7 в "ResearchHarness" = 20.7; лучшая модель, выбранная отдельно под задачу = 26.5.
- Все оценки значительно ниже порога 50 баллов, необходимого даже для простого воспроизведения известных результатов, не говоря уже о превышении.

## Подробнее
Этот бенчмарк нацелен на способность, отличную от бенчмарков coding agent (SWE-bench, Agent Arena и др.) — независимое научное рассуждение в реалистичных условиях: получив исходные материалы, но не ответ, может ли AI провести исследование так, как это сделал бы компетентный исследователь? Главный вывод — даже передовые модели (Claude Opus 4.6/4.7 в агентных harness) далеки от надёжного воспроизведения установленных результатов, набирая примерно 20-26 из 100 по экспертным рубрикам.

Автор поста на Reddit (r/ClaudeCode, tier 3 изложение источника tier 1 — arXiv) использовал это как аргумент против чрезмерного доверия заявлениям о "новых научных открытиях", генерируемых LLM — если модели не могут надёжно воспроизвести даже известные результаты при наличии всех исходных материалов, заявления о получении подлинно новых научных инсайтов следует воспринимать со значительным скептицизмом. Это полезный противовес более оптимистичным трактовкам возможностей "AI-исследователя" и важно для всех, кто оценивает workflow AI-ассистированных исследований (включая собственные записи раздела research/ этой wiki, к которым стоит применять схожую строгость).

## Связанные записи
- [[claude-agent-sdk-credit-june-2026]] ([Изменение Anthropic Agent SDK Credit](../news/claude-agent-sdk-credit-june-2026.md))
