---
title: "rag-access-check — Test Whether Your RAG Enforces Document-Level Access"
title_ru: "rag-access-check — проверка документного разграничения доступа в RAG"
category: tools
tags: [rag, security, access-control, authorization, testing, python]
aliases: [rag access check, rag authorization testing, retrieve before authorize]
confidence: medium
updated: 2026-09-01
sources:
  - https://github.com/InfraGuard-Labs/rag-access-check
---

## Summary
A lightweight open-source Python tool that tests whether RAG applications actually enforce document-level access controls — i.e., whether one user can retrieve documents belonging to another user, team, or security boundary. Targets the "retrieve before authorize" failure pattern: the retriever fetches by similarity first, and authorization (if any) happens too late or not at all.

## Key Ideas
- **Checks for:** cross-user document retrieval, missing document-level authorization, retrieval-before-authorization, boundary failures, retrieval of restricted docs.
- **Two modes:** offline (JSON of users / allowed docs / retrieved docs) and live API mode (hits a configured RAG endpoint, captures returned document IDs, diffs against the user's allowed set; bearer-token auth via env var).
- **Single-script usage:** `python rag_access_check.py`, plain-text FAIL/PASS report with per-user unauthorized-doc listing.
- Tiny (1 star, new), but the topic — document-level authz in RAG — is genuinely under-tested in the wild; most RAG security work focuses on prompt injection, not tenancy leaks.

## Details
This fills the gap between RAG functionality and RAG security: embedding similarity doesn't know about permissions, so without a post-retrieval authorization filter, every retrieval is a potential tenancy breach. The tool operationalizes the check the same way [[arc-gate-prompt-injection-proxy]] operationalizes injection defense — as a testable boundary, not a hope.

## Related Entries
- [[lightrag-graph-rag]] ([LightRAG](lightrag-graph-rag.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate](arc-gate-prompt-injection-proxy.md))
- [[rag-simpler-than-you-think]] ([RAG Is Simpler Than You Think](../concepts/rag-simpler-than-you-think.md))

---
<!-- RU -->

## Краткое описание
Лёгкий открытый Python-инструмент, проверяющий, применяют ли RAG-приложения документный контроль доступа — то есть может ли один пользователь извлечь документы другого пользователя, команды или границы безопасности. Мишень — паттерн «сначала извлечение, потом авторизация»: ретривер ищет по сходству, а проверка прав (если есть) происходит слишком поздно или не происходит вовсе.

## Ключевые идеи
- **Проверяет:** кросс-пользовательское извлечение, отсутствие документной авторизации, «извлечение до авторизации», нарушения границ, извлечение ограниченных документов.
- **Два режима:** офлайн (JSON пользователей/разрешённых/полученных документов) и live API (запрос к RAG-эндпоинту, сверка ID документов с разрешённым набором; bearer-токен через env).
- **Использование:** один скрипт `python rag_access_check.py`, текстовый отчёт PASS/FAIL со списком несанкционированных документов по пользователям.
- Крошечный (1 звезда), но тема — документная авторизация в RAG — реально недотестирована; большинство работ по безопасности RAG сфокусировано на prompt injection, а не на утечках тенантов.

## Подробнее
Инструмент закрывает разрыв между функциональностью RAG и безопасностью RAG: эмбеддинг-сходство ничего не знает о правах, поэтому без пост-ретривальной авторизации каждое извлечение — потенциальная утечка тенанта. Инструмент превращает проверку в тестируемую границу — как [[arc-gate-prompt-injection-proxy]] делает для инъекций.

## Связанные записи
- [[lightrag-graph-rag]] ([LightRAG](lightrag-graph-rag.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate](arc-gate-prompt-injection-proxy.md))
- [[rag-simpler-than-you-think]] ([RAG Is Simpler Than You Think](../concepts/rag-simpler-than-you-think.md))
