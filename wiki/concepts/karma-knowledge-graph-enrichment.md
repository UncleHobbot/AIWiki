---
title: "KARMA: Multi-Agent LLMs for Automated Knowledge Graph Enrichment"
title_ru: "KARMA: мультиагентные LLM для автоматического обогащения графов знаний"
category: concepts
tags: [knowledge-graph, multi-agent, llm, entity-extraction, conflict-resolution, pubmed, nlp]
date: 2026-01-11
updated: 2026-05-17
sources:
  - https://arxiv.org/abs/2502.06472
authors: [Yuxing Lu, Wei Wu, Xukai Zhao, Rui Peng, Jinzhong Wang]
venue: "arXiv:2502.06472 (v2 Jan 2026)"
---

## Summary
KARMA is a multi-agent LLM framework that automates knowledge graph enrichment by deploying nine specialized collaborative agents — spanning entity discovery, relation extraction, schema alignment, and conflict resolution — to parse unstructured scientific documents and integrate verified knowledge into existing graph structures.

## Key Ideas
- Nine specialized agents work in sequence: entity discovery, relation extraction, schema alignment, conflict resolution, and verification layers — each with a narrow responsibility rather than one monolithic LLM call.
- Tested on 1,200 PubMed articles across three biomedical domains: discovered up to 38,230 new entities at 83.1% LLM-verified correctness.
- Conflict resolution agents reduce contradicting graph edges by 18.6% through multi-layer consensus — treating contradiction as a first-class problem, not an edge case.
- Domain-specific schema adherence: extracted knowledge must conform to the existing KG schema, preventing schema drift as the graph grows.
- Incremental enrichment model: new documents integrate into the graph without full rebuilds, analogous to LightRAG's incremental update algorithm.

## Details
Manual knowledge graph curation cannot scale with the pace of scientific publishing. KARMA addresses this by decomposing the enrichment task into a pipeline of nine collaborative LLM agents. The division of labour mirrors software engineering principles: entity discovery agents focus solely on identifying candidate entities, relation extraction agents identify how those entities relate, schema alignment agents reconcile extracted facts with the existing ontology, and conflict resolution agents adjudicate when two sources disagree.

The conflict resolution layer is the most technically novel contribution. Rather than accepting the most recent or highest-confidence extraction, KARMA runs a multi-layer assessment: the conflicting claims are independently evaluated by multiple agents, and consensus determines the accepted edge. This reduced conflicting edges by 18.6% in experiments, a significant improvement given that KG inconsistencies compound across queries.

Experiments on PubMed articles demonstrated that KARMA can enrich existing biomedical knowledge graphs with tens of thousands of new entities while maintaining high correctness and low conflict rates. The paper positions KARMA against prior single-agent approaches that process documents in a single pass, showing that the collaborative multi-agent structure catches errors and contradictions that single-pass systems miss.

**Application to personal wikis:** KARMA's conflict resolution architecture is a direct blueprint for a `scripts/check_conflicts.py` tool — extracting core claims from each new wiki entry and flagging contradictions against existing entries in the same category. See [[llm-wiki-academic-applications]] for the full feature design.

## Related Entries
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[lightrag-graph-rag]] ([LightRAG: Graph-Enhanced Retrieval-Augmented Generation](../tools/lightrag-graph-rag.md))
- [[llm4sr-survey]] ([LLM4SR: LLMs for Scientific Research Survey](../concepts/llm4sr-survey.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))

---
<!-- RU -->

## Краткое описание
KARMA — мультиагентный LLM-фреймворк для автоматического обогащения графов знаний: девять специализированных агентов (обнаружение сущностей, извлечение отношений, выравнивание схем, разрешение конфликтов) разбирают неструктурированные научные документы и интегрируют верифицированные знания в существующие графовые структуры.

## Ключевые идеи
- Девять специализированных агентов работают последовательно: обнаружение сущностей, извлечение отношений, выравнивание схем, разрешение конфликтов и верификационные слои — каждый с узкой ответственностью.
- Протестировано на 1200 статьях PubMed в трёх биомедицинских доменах: обнаружено до 38 230 новых сущностей при 83,1% верифицированной LLM корректности.
- Агенты разрешения конфликтов снижают количество противоречащих рёбер графа на 18,6% через многоуровневый консенсус — противоречие рассматривается как первоклассная проблема, а не крайний случай.
- Соответствие предметно-специфической схеме: извлечённые знания должны соответствовать существующей онтологии KG, предотвращая дрейф схемы по мере роста графа.
- Модель инкрементального обогащения: новые документы интегрируются в граф без полного перестроения — аналогично алгоритму инкрементальных обновлений LightRAG.

## Подробнее
Ручное курирование графов знаний не успевает за темпами научных публикаций. KARMA решает эту проблему, разбивая задачу обогащения на конвейер из девяти коллаборативных LLM-агентов. Разделение труда следует принципам разработки ПО: агенты обнаружения сущностей сосредоточены исключительно на идентификации кандидатов, агенты извлечения отношений определяют связи, агенты выравнивания схем согласовывают извлечённые факты с существующей онтологией, а агенты разрешения конфликтов выносят решения при несогласии источников.

Слой разрешения конфликтов — наиболее технически новаторский вклад. Вместо того чтобы принимать наиболее свежее или наиболее достоверное извлечение, KARMA проводит многоуровневую оценку: конфликтующие утверждения независимо оцениваются несколькими агентами, и консенсус определяет принятое ребро. Это снизило количество конфликтующих рёбер на 18,6% в экспериментах.

**Применение к личным вики:** архитектура разрешения конфликтов KARMA — прямой образец для инструмента `scripts/check_conflicts.py`, который извлекает ключевые утверждения из каждой новой записи вики и сигнализирует о противоречиях с существующими записями той же категории. Полный дизайн функции — в [[llm-wiki-academic-applications]].

## Связанные записи
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[lightrag-graph-rag]] ([LightRAG: Graph-Enhanced Retrieval-Augmented Generation](../tools/lightrag-graph-rag.md))
- [[llm4sr-survey]] ([LLM4SR: LLMs for Scientific Research Survey](../concepts/llm4sr-survey.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))
