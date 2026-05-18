---
title: "AutoMathKG: Automated Mathematical Knowledge Graph"
title_ru: "AutoMathKG: автоматизированный математический граф знаний"
category: tools
tags: [automathkg, math, knowledge-graph, latex, llm, vector-database, sbert]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://arxiv.org/abs/2505.13406
---

## Summary
AutoMathKG is an automated mathematical knowledge graph that uses LLMs and vector databases to build a high-quality, wide-coverage, multi-dimensional representation of mathematical knowledge. It models mathematics as a vast directed graph of Definition, Theorem, and Problem entities connected by typed reference relationships.

## Key Ideas
- Mathematics is modeled as a directed graph with three core entity types (Definition, Theorem, Problem) and nine typed relation labels: premise, assumption, lemma, definition, conclusion, generalization, specialization, contradiction, exemplifies
- Integrates knowledge from diverse sources: ProofWiki, textbooks, arXiv papers, and TheoremQA
- LLM augmentation via in-context learning with 12 carefully designed templates for data augmentation
- MathVD vector database enables similar entity search using SBERT with two designed embedding strategies
- Two update mechanisms keep the graph current: knowledge completion (Math LLM fills missing proofs/solutions) and knowledge fusion (MathVD retrieves similar entities, LLM decides merge vs add)
- Rule-based regex extraction of typed LaTeX environments (theorem, definition, lemma, proof, algorithm) for structured parsing
- Demonstrates superior reachability query results compared to five baselines
- Enhances mathematical reasoning capabilities in Math LLMs

## Details
AutoMathKG addresses the challenge of organizing mathematical knowledge at scale. Traditional mathematical databases are manually curated, limiting their coverage and update frequency. By leveraging LLMs for extraction, augmentation, and reasoning, AutoMathKG automates the construction and maintenance of a mathematical knowledge graph that rivals manually curated resources in quality while far exceeding them in breadth.

The system extracts structured entities from LaTeX sources using rule-based regex patterns targeting typed environments (theorem, definition, lemma, proof, algorithm). It then enriches this raw extraction through LLM-based in-context learning, applying 12 templates designed for data augmentation. The nine typed relation labels capture nuanced relationships between mathematical objects — for instance, distinguishing between a lemma used in a proof and a generalization of a theorem.

The MathVD vector database, powered by SBERT embeddings with two specialized strategies, enables efficient similarity search across entities. This underpins the two core update mechanisms: knowledge completion, where a Math LLM generates missing proofs or solutions, and knowledge fusion, where similar entities are retrieved via MathVD and an LLM decides whether to merge duplicates or add new entries. Experiments show AutoMathKG achieves superior reachability query performance against five baselines and improves robustness in mathematical reasoning tasks.

## Related Entries
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))

---
<!-- RU -->

## Краткое описание
AutoMathKG — автоматизированный математический граф знаний, использующий LLM и векторные базы данных для построения качественного, широкого и многомерного представления математических знаний. Математика моделируется как направленный граф из сущностей Definition, Theorem и Problem, связанных типизированными ссылочными отношениями.

## Ключевые идеи
- Математика моделируется как направленный граф с тремя базовыми типами сущностей (Definition, Theorem, Problem) и девятью типизированными метками отношений: premise, assumption, lemma, definition, conclusion, generalization, specialization, contradiction, exemplifies
- Интеграция знаний из разнообразных источников: ProofWiki, учебники, статьи arXiv и TheoremQA
- LLM-аугментация через обучение в контексте с 12 тщательно разработанными шаблонами для обогащения данных
- Векторная база данных MathVD обеспечивает поиск похожих сущностей с помощью SBERT и двух разработанных стратегий эмбеддинга
- Два механизма обновления поддерживают актуальность графа: дополнение знаний (Math LLM заполняет недостающие доказательства/решения) и слияние знаний (MathVD находит похожие сущности, LLM решает — объединить или добавить)
- Извлечение типизированных LaTeX-окружений (theorem, definition, lemma, proof, algorithm) на основе регулярных выражений
- Превосходные результаты запросов достижимости по сравнению с пятью базовыми методами
- Повышение надёжности математических рассуждений в Math LLM

## Подробнее
AutoMathKG решает задачу организации математических знаний в масштабе. Традиционные математические базы данных курируются вручную, что ограничивает их покрытие и частоту обновления. Благодаря использованию LLM для извлечения, аугментации и рассуждений, AutoMathKG автоматизирует построение и поддержку математического графа знаний, который по качеству сопоставим с вручную курируемыми ресурсами, но значительно превосходит их по охвату.

Система извлекает структурированные сущности из LaTeX-источников с помощью регулярных выражений, нацеленных на типизированные окружения (theorem, definition, lemma, proof, algorithm). Затем полученные данные обогащаются через LLM-аугментацию в контексте с применением 12 шаблонов. Девять типизированных меток отношений отражают тонкие связи между математическими объектами — например, различают лемму, используемую в доказательстве, и обобщение теоремы.

Векторная база данных MathVD на базе SBERT-эмбеддингов с двумя специализированными стратегиями обеспечивает эффективный поиск похожих сущностей. Это основа двух ключевых механизмов обновления: дополнение знаний, где Math LLM генерирует недостающие доказательства или решения, и слияние знаний, где похожие сущности извлекаются через MathVD, а LLM принимает решение об объединении дубликатов или добавлении новых записей. Эксперименты показывают, что AutoMathKG достигает превосходных результатов по запросам достижимости по сравнению с пятью базовыми методами и повышает надёжность в задачах математического рассуждения.

## Связанные записи
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
