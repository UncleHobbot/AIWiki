---
title: "SurveyGen-I: Memory-Guided Scientific Survey Generation"
title_ru: "SurveyGen-I: генерация научных обзоров с памятью"
category: concepts
tags: [survey-generation, llm, scientific-writing, rag, memory, consistency, nlp]
date: 2025-01-01
updated: 2026-05-17
sources:
  - https://arxiv.org/abs/2508.14317
authors: [Jing Chen, Zhiheng Yang, Yixian Shen]
venue: "IJCNLP-AIJLP 2025"
---

## Summary
SurveyGen-I generates long-form, internally consistent scientific surveys through a coarse-to-fine retrieval loop combined with a terminology memory mechanism that stores previously written definitions and prevents re-explanation across sections and across subsequent generation runs.

## Key Ideas
- Coarse-to-fine retrieval: first builds a survey-level outline and writing plan, then refines at subsection level by retrieving additional context only when the current context is insufficient.
- Evolving plans: the outline and writing plan are dynamically revised as new sections are written, rather than fixed upfront — accommodating discoveries made mid-generation.
- Memory-guided writing: a terminology memory store tracks all technical terms defined in previously written sections; each new section receives a "do not re-explain these terms" constraint.
- Cross-run memory persistence: the memory store survives between generation sessions, so the second run of a survey tool does not re-define terms the first run already established.
- Outperforms prior systems on content quality, internal consistency, and citation coverage across four scientific domains.

## Details
Long-form scientific survey generation has a fundamental coherence problem: LLMs have no awareness of what they wrote three sections ago. A model explaining "RAG (Retrieval-Augmented Generation)" in the introduction will re-explain it in every subsequent section that uses the term, producing text that reads as assembled from independent fragments rather than as a single document.

SurveyGen-I's memory mechanism directly addresses this. After writing each section, it extracts all defined technical terms and one-line summaries and adds them to a persistent memory store. Before writing the next section, the memory store is injected as a constraint: these terms are known — do not define them again. This produces noticeably more natural, expert-reader-oriented text.

The coarse-to-fine retrieval loop further improves coherence by grounding the outline in retrieved literature before committing to a writing plan, then re-retrieving at subsection granularity when the high-level context is insufficient. The evolving-plans mechanism allows the outline to shift as understanding deepens during writing, rather than forcing the model to honour an upfront plan that may be miscalibrated.

**Application to personal wikis:** the weekly `/wiki-digest` command re-explains the same concepts (RAG, MCP, agents) every run because there is no cross-run memory. Writing `digests/memory.json` after each digest — containing all terms defined that week — and injecting it as a constraint into the next run's Claude prompt would eliminate this problem at near-zero cost. See [[llm-wiki-academic-applications]] for the full design.

## Related Entries
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[llm4sr-survey]] ([LLM4SR: LLMs for Scientific Research Survey](../concepts/llm4sr-survey.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[karma-knowledge-graph-enrichment]] ([KARMA: Multi-Agent LLMs for Automated Knowledge Graph Enrichment](../concepts/karma-knowledge-graph-enrichment.md))

---
<!-- RU -->

## Краткое описание
SurveyGen-I генерирует длинные, внутренне согласованные научные обзоры через цикл поиска от общего к частному в сочетании с механизмом памяти терминологии, который хранит ранее написанные определения и предотвращает их повторное объяснение в разных разделах и в последующих сеансах генерации.

## Ключевые идеи
- Поиск от общего к частному: сначала строится план обзора и структура, затем уточняется на уровне подразделов — дополнительный контекст извлекается только при недостаточности текущего.
- Эволюционирующие планы: структура и план написания динамически пересматриваются по мере написания новых разделов, а не фиксируются заранее.
- Написание с памятью: хранилище терминологии отслеживает все технические термины, определённые в ранее написанных разделах; каждый новый раздел получает ограничение «не объяснять повторно эти термины».
- Сохранение памяти между запусками: хранилище памяти переживает отдельные сеансы генерации, поэтому второй запуск инструмента не переопределяет термины, уже установленные в первом.
- Превосходит предшествующие системы по качеству контента, внутренней согласованности и охвату цитат на четырёх научных доменах.

## Подробнее
Генерация длинных научных обзоров имеет фундаментальную проблему согласованности: LLM не знает, что написал три раздела назад. Модель, объясняющая «RAG (Retrieval-Augmented Generation)» во введении, будет переобъяснять это в каждом последующем разделе, использующем термин, — текст читается как собранный из независимых фрагментов, а не как единый документ.

Механизм памяти SurveyGen-I непосредственно решает эту проблему. После написания каждого раздела система извлекает все определённые технические термины и краткие описания и добавляет их в постоянное хранилище памяти. Перед написанием следующего раздела хранилище памяти вводится как ограничение: эти термины известны — не определять их снова. Результат — заметно более естественный, ориентированный на экспертного читателя текст.

**Применение к личным вики:** команда `/wiki-digest` заново объясняет одни и те же концепции (RAG, MCP, агенты) в каждом запуске, поскольку нет межсессионной памяти. Запись `digests/memory.json` после каждого дайджеста и внедрение его как ограничения в следующий промпт Claude устранит эту проблему практически без затрат. Полный дизайн — в [[llm-wiki-academic-applications]].

## Связанные записи
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[llm4sr-survey]] ([LLM4SR: LLMs for Scientific Research Survey](../concepts/llm4sr-survey.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[karma-knowledge-graph-enrichment]] ([KARMA: Multi-Agent LLMs for Automated Knowledge Graph Enrichment](../concepts/karma-knowledge-graph-enrichment.md))
