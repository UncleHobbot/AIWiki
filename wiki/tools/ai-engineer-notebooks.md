---
title: "AI Engineer Notebooks: Framework-Free Colab Curriculum"
title_ru: "AI Engineer Notebooks: учебный курс на Colab без фреймворков"
category: tools
tags: [education, rag, agents, evals, colab, notebooks, framework-free, llmops, fine-tuning, groq]
aliases: [ai-engineer-notebooks, calmrocks notebooks, AI engineer curriculum]
confidence: high
date: 2026-08-30
updated: 2026-08-30
sources:
  - https://github.com/calmrocks/ai-engineer-notebooks
  - https://news.ycombinator.com/item?id=49471714
---

## Summary
A free, framework-free curriculum of hands-on Colab notebooks (568 stars) covering the applied AI engineer skill set across 12 progressive sections — RAG, agents, evals, fine-tuning, security, and LLMOps — built on raw API calls rather than LangChain-style abstractions, and running entirely on the free Groq API with no credit card required.

## Key Ideas
- **"Patterns are durable; wrappers churn"**: the deliberate design principle. Learners build agents and retrieval systems from raw API calls first, producing portable understanding before reaching for a framework.
- **Evals as the spine**: evaluation is threaded through every section rather than bolted on at the end — the goal is making "measure before you optimize" an installed habit rather than a later discipline.
- **Retrieval is the bottleneck**: the RAG material emphasizes that retrieval quality, not generation capability, is what typically limits system performance.
- **Zero cost to run**: everything executes on the free Groq API tier in Colab — no credit card, no local GPU.
- **12 sections**: model APIs and prompting, structured output and tool calling, RAG (retrieval/embeddings/chunking/hybrid), evaluation and LLM-as-judge, agent loops and tool design, fine-tuning vs LoRA, security and prompt injection, LLMOps and observability, serving and inference optimization, ML system design, and real-world case studies.

## Details
The framework-free stance is the distinguishing choice. Most AI engineering tutorials teach LangChain or LlamaIndex idioms, which means learners acquire knowledge of an abstraction layer that may not survive the next release cycle. By teaching the underlying HTTP calls and control flow directly, this curriculum aims at knowledge that transfers to whatever framework a team eventually adopts — or to no framework at all.

The agent-design section notably moves past the simplistic chatbot pattern to cover the decision loop, tool specification, guardrails, and budgeting — the same harness-engineering concerns that Claude Code and Codex practitioners have converged on.

Community reception on Hacker News was broadly positive, particularly on the decision to prioritize evaluation from the start; one commenter noted the common failure pattern of "throwing together a RAG pipeline on the knee and judging the metrics by eye, skimming three responses in the terminal." A recurring critique was that the material reads as LLM-generated, though several readers noted it arrived at the same conclusions they had reached through independent trial and error.

## Related Entries
- [[rag-simpler-than-you-think]] ([RAG Is Simpler Than You Think](../concepts/rag-simpler-than-you-think.md))
- [[microsoft-ai-agents-beginners-course]] ([Microsoft AI Agents for Beginners](../tools/microsoft-ai-agents-beginners-course.md))
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))
- [[anthropic-academy-courses-review]] ([Anthropic Academy Courses Review](../tips/anthropic-academy-courses-review.md))

---
<!-- RU -->

## Краткое описание
Бесплатный учебный курс из практических Colab-ноутбуков без фреймворков (568 звёзд), охватывающий прикладные навыки AI-инженера в 12 последовательных разделах — RAG, агенты, оценка, файн-тюнинг, безопасность и LLMOps — построенный на сырых вызовах API вместо абстракций уровня LangChain и работающий целиком на бесплатном Groq API без привязки карты.

## Ключевые идеи
- **«Паттерны долговечны; обёртки текучи»**: осознанный принцип проектирования. Учащиеся строят агентов и системы поиска из сырых вызовов API, получая переносимое понимание до обращения к фреймворкам.
- **Оценка как позвоночник**: evaluation проходит через каждый раздел, а не пристёгнута в конце — цель в том, чтобы «измеряй до оптимизации» стало встроенной привычкой.
- **Узкое место — поиск**: материал по RAG подчёркивает, что производительность системы обычно ограничивает качество поиска, а не способности генерации.
- **Нулевая стоимость запуска**: всё работает на бесплатном уровне Groq API в Colab — без карты и без локального GPU.
- **12 разделов**: API моделей и промптинг, структурированный вывод и tool calling, RAG, оценка и LLM-as-judge, циклы агентов и дизайн инструментов, файн-тюнинг vs LoRA, безопасность и prompt injection, LLMOps, оптимизация инференса, дизайн ML-систем и разбор реальных кейсов.

## Подробнее
Отказ от фреймворков — ключевое отличие. Большинство обучающих материалов преподают идиомы LangChain или LlamaIndex, из-за чего учащиеся осваивают слой абстракции, который может не пережить следующий цикл релизов. Обучая напрямую нижележащим HTTP-вызовам и потоку управления, курс нацелен на знания, переносимые на любой фреймворк, который команда выберет позже — или на работу вовсе без фреймворка.

Раздел о дизайне агентов заметно выходит за рамки простого чат-бота, охватывая цикл принятия решений, спецификацию инструментов, guardrails и бюджетирование — те же вопросы harness-инженерии, к которым пришли практики Claude Code и Codex.

## Связанные записи
- [[rag-simpler-than-you-think]] ([RAG Is Simpler Than You Think](../concepts/rag-simpler-than-you-think.md))
- [[microsoft-ai-agents-beginners-course]] ([Microsoft AI Agents for Beginners](../tools/microsoft-ai-agents-beginners-course.md))
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))
- [[anthropic-academy-courses-review]] ([Anthropic Academy Courses Review](../tips/anthropic-academy-courses-review.md))
