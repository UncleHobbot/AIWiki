---
title: "GROBID: Machine Learning PDF Parser for Scientific Documents"
title_ru: "GROBID: ML-парсер PDF для научных документов"
category: tools
tags: [grobid, pdf, parsing, scientific, extraction, tei-xml, bibliography, nlp]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://grobid.readthedocs.io/en/latest/Introduction/
  - https://github.com/kermitt2/grobid
---

## Summary
GROBID (GeneRation Of BIbliographic Data) is a machine learning library for extracting, parsing, and restructuring raw documents — especially scientific PDFs — into structured TEI XML. Created by Patrice Lopez in 2008 and open-sourced in 2011, it is the de facto standard for scholarly document processing in production systems worldwide.

## Key Ideas
- Header extraction achieves ~0.90 F1-score; reference parsing reaches ~0.87 F1 on PubMed Central and ~0.90 on bioRxiv
- Processes 36 PDF/sec for headers, 2.5 PDF/sec for full text — up to 915,000 PDFs/day on a 16-CPU machine
- Used in production by ResearchGate, Semantic Scholar, CERN, Internet Archive Scholar, European Patent Office, Mendeley, and others
- Output is TEI-encoded XML with >55 structural labels covering full text, figures, tables, and affiliations
- Combines CRF models with Deep Learning via DeLFT; supports CJK and Arabic languages
- DOI/PMID resolution exceeds 0.95 F1-score through biblio-glutton or Crossref API
- Licensed under Apache 2.0, written in Java, with ready-to-use Docker images

## Details
GROBID is built around a modular pipeline architecture where each extraction task — header metadata, references, full text, citation contexts, affiliation addresses — is handled by a dedicated model. The original models use Conditional Random Fields (CRFs) trained on manually annotated corpora, while newer Deep Learning models are powered by DeLFT (Deep Learning Framework for Text), which supports architectures like BidLSTM-CRF and transformer-based approaches. This hybrid strategy lets GROBID maintain both high accuracy and practical throughput.

The system converts raw PDF into TEI XML, a standard encoding for textual scholarship. The TEI output captures document structure at a granular level: title, authors, affiliations, abstract, sections, paragraphs, figures, tables, formulas, and bibliographic references with resolved identifiers. Citation context resolution — identifying where in the text a reference is invoked — operates at 0.76–0.91 F1-score, enabling downstream tasks like citation graph construction and literature review automation.

At scale, GROBID is a cornerstone infrastructure component. ResearchGate uses it for millions of uploaded papers; Semantic Scholar relies on it for corpus ingestion; CERN's Invenio platform and the Internet Archive Scholar project depend on it for metadata extraction. The tool is available as a RESTful web service, a Java library, and Docker containers, making integration straightforward for both research prototypes and production pipelines.

## Notable Quotes
> "GROBID is a machine learning library for extracting, parsing, and restructuring raw documents into structured XML/TEI encoded documents." — Patrice Lopez, GROBID Documentation

## Related Entries
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))

---
<!-- RU -->

## Краткое описание
GROBID (GeneRation Of BIbliographic Data) — библиотека машинного обучения для извлечения, парсинга и реструктуризации сырых документов (особенно PDF научных статей) в структурированный TEI XML. Создана Патрисом Лопесом в 2008 году, открыта в 2011 году; де-факто стандарт для обработки научных документов в продакшн-системах по всему миру.

## Ключевые идеи
- Извлечение заголовков: ~0.90 F1; парсинг ссылок: ~0.87 F1 на PubMed Central, ~0.90 на bioRxiv
- Скорость: 36 PDF/сек для заголовков, 2.5 PDF/сек полный разбор — до 915 000 PDF/день на 16 CPU
- Используется в продакшене ResearchGate, Semantic Scholar, CERN, Internet Archive Scholar, Европейским патентным ведомством, Mendeley и другими
- Результат — TEI XML с >55 структурными метками: полный текст, формулы, таблицы, аффилиации
- Гибрид моделей CRF и Deep Learning через DeLFT; поддержка китайского, японского, корейского и арабского языков
- Резолвинг DOI/PMID с F1 > 0.95 через biblio-glutton или Crossref API
- Лицензия Apache 2.0, написан на Java, Docker-образы доступны

## Подробнее
GROBID построен на модульной пайплайн-архитектуре, где каждая задача извлечения — метаданные заголовка, ссылки, полный текст, контексты цитирования, адреса аффилиаций — обрабатывается отдельной моделью. Оригинальные модели используют Conditional Random Fields (CRF), обученные на вручную размеченных корпусах, а более новые модели глубокого обучения работают через DeLFT (Deep Learning Framework for Text), поддерживающий архитектуры BidLSTM-CRF и трансформеры. Такая гибридная стратегия обеспечивает одновременно высокую точность и практичную пропускную способность.

Система конвертирует сырые PDF в TEI XML — стандартную кодировку для текстологических исследований. TEI-вывод фиксирует структуру документа на детальном уровне: заголовок, авторы, аффилиации, аннотация, разделы, параграфы, иллюстрации, таблицы, формулы и библиографические ссылки с разрешёнными идентификаторами. Определение контекста цитирования — где именно в тексте вызывается ссылка — работает с F1 0.76–0.91, что позволяет строить графы цитирования и автоматизировать обзоры литературы.

В масштабе GROBID является ключевой инфраструктурной компонентой. ResearchGate использует его для миллионов загруженных статей; Semantic Scholar полагается на него при обработке корпуса; платформа Invenio в CERN и проект Internet Archive Scholar зависят от него при извлечении метаданных. Инструмент доступен как RESTful веб-сервис, Java-библиотека и Docker-контейнеры, что упрощает интеграцию как в исследовательских прототипах, так и в продакшн-пайплайнах.

## Примечательные цитаты
> «GROBID — это библиотека машинного обучения для извлечения, парсинга и реструктуризации сырых документов в структурированные XML/TEI документы.» — Патрис Лопес, документация GROBID

## Связанные записи
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
