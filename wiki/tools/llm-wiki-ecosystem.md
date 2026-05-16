---
title: "LLM Wiki Ecosystem: Implementations and Variants"
title_ru: "Экосистема LLM-вики: реализации и варианты"
category: tools
tags: [llm-wiki, knowledge-base, obsidian, mcp, open-source, second-brain, karpathy]
updated: 2026-05-15
sources:
  - https://github.com/andysingal/LLMops/blob/main/LLM_Knowledge_bases.md
---

## Summary
A curated map of open-source implementations of Karpathy's LLM Wiki pattern — from simple Obsidian-based local wikis to full research lifecycle platforms — plus a knowledge-base architecture diagram used across AI agent stacks.

## Key Ideas
- **The core pattern is a substrate, not a product:** Raw sources → LLM-managed wiki → schema/instructions. Every project below instantiates this same three-layer architecture differently.
- **Two camps have emerged:** *Personal knowledge bases* (single user, local-first, Obsidian/markdown) and *agent knowledge layers* (multi-agent, structured JSON/markdown, explicit retrieval APIs).
- **Retrieval without RAG:** Most implementations use a simple index file + LLM navigation rather than vector embeddings, sidestepping the infrastructure cost of a vector DB for collections under ~500 documents.
- **Queries compound the wiki:** All mature implementations file valuable query answers back as wiki pages — the compounding property that distinguishes this pattern from RAG.

## Key Implementations

### Personal Knowledge Bases
| Project | Key features |
|---|---|
| **memoriki** | LLM Wiki + MemPalace MCP server for real memory. `pip install mempalace` + `claude mcp add mempalace` |
| **obsidian-llm-wiki** | Local-first, 100% Ollama by default, also works with any OpenAI-compatible endpoint (Groq, LM Studio, Azure, vLLM) |
| **llmwiki** (lucasastorian) | FastAPI + Next.js + stdio MCP, SQLite FTS5, hosted version at llmwiki.app |
| **second-brain** | Continuously indexes files, searches web when local knowledge insufficient, lives in terminal + Telegram |

### Research & Enterprise Platforms
| Project | Key features |
|---|---|
| **OmegaWiki (ΩmegaWiki)** | Full research lifecycle: paper ingest → knowledge graph → gap detection → idea generation → experiment design → paper writing → peer review. 24 Claude Code skills, all centered on one wiki as source of truth. |
| **OpenKB** | CLI-based; uses PageIndex for long-document retrieval without vector DB. Structure: sources/ → summaries/ → concepts/ (cross-document synthesis) → explorations/ → reports/ |
| **claude-memory-compiler** | Captures Claude Code sessions via hooks when session ends/auto-compacts → extracts decisions, lessons, patterns via Claude Agent SDK → appends to daily log → compiles to structured wiki articles |

### Architecture Pattern (used across agent stacks)
```
YOUR AGENTS
(writer, researcher, strategist, analyst)
        ↓ reads from          ↓ reads from
KNOWLEDGE BASE LAYER    BRAND FOUNDATION
(dynamic, agent-         (static, human-edited:
maintained, grows)       voice, rules, positioning)
        ↑ compiles from
    raw/ inbox
(tweets, articles, bookmarks, PDFs, notes)
```

## Details
The `claude-memory-compiler` project is particularly notable because it applies the LLM Wiki pattern to something often overlooked: **the sessions themselves as a source.** When Claude Code ends or auto-compacts, a hook spawns a background process that extracts decisions, lessons, and patterns from the transcript and appends them to a daily log. Those logs are then compiled into a structured, cross-referenced wiki — meaning your Claude Code usage history itself becomes a knowledge base without any manual note-taking.

**OmegaWiki** represents the most ambitious scope: it treats the wiki as the single source of truth for an entire academic research lifecycle, from reading the first paper to responding to journal reviewers. 24 Claude Code skills orchestrate each phase.

**OpenKB** addresses a real scaling problem: long PDFs that exceed what can be read in one pass. It uses PageIndex (a tree-structured document index) to let the LLM navigate large documents without chunking them into arbitrary embedding-sized pieces.

## Related Entries
- [[llm-wiki-pattern]]
- [[llmwiki-open-source]]
- [[llm-wiki-enterprise-patterns]]
- [[llm-wiki-setup-guide]]

---
<!-- RU -->

## Краткое описание
Кураторская карта реализаций паттерна LLM-вики Карпатого с открытым исходным кодом — от простых локальных вики на основе Obsidian до полноценных платформ для исследовательского жизненного цикла.

## Ключевые идеи
- **Паттерн — это подложка, не продукт:** Сырые источники → вики, управляемая LLM → схема/инструкции. Каждый проект ниже реализует одну и ту же трёхуровневую архитектуру по-своему.
- **Сложились два лагеря:** *Персональные базы знаний* (один пользователь, локально, Obsidian/markdown) и *уровень знаний агента* (мульти-агентный, структурированный JSON/markdown, явные API поиска).
- **Поиск без RAG:** Большинство реализаций используют простой индексный файл + навигацию LLM вместо векторных эмбеддингов, обходя стороной инфраструктурные затраты векторной БД для коллекций до ~500 документов.
- **Запросы пополняют вики:** Все зрелые реализации сохраняют ценные ответы на запросы обратно как страницы вики.

## Ключевые реализации

### Персональные базы знаний
| Проект | Ключевые особенности |
|---|---|
| **memoriki** | LLM Wiki + MCP-сервер MemPalace для настоящей памяти |
| **obsidian-llm-wiki** | Локально, Ollama по умолчанию, совместим с любым OpenAI-совместимым эндпоинтом |
| **llmwiki** (lucasastorian) | FastAPI + Next.js + stdio MCP, SQLite FTS5, хостируемая версия на llmwiki.app |
| **second-brain** | Непрерывно индексирует файлы, ищет в веб при нехватке локальных знаний, работает в терминале + Telegram |

### Исследовательские и корпоративные платформы
| Проект | Ключевые особенности |
|---|---|
| **OmegaWiki (ΩmegaWiki)** | Полный цикл: загрузка статей → граф знаний → обнаружение пробелов → генерация идей → дизайн экспериментов → написание статей → ответы рецензентам. 24 навыка Claude Code. |
| **OpenKB** | CLI; использует PageIndex для длинных документов без векторной БД |
| **claude-memory-compiler** | Захватывает сессии Claude Code через хуки → извлекает решения/уроки/паттерны → компилирует в вики |

## Подробнее
Проект `claude-memory-compiler` особенно примечателен применением паттерна LLM-вики к самим сессиям как источнику. Когда Claude Code завершается или авто-компактируется, хук запускает фоновый процесс, извлекающий решения, уроки и паттерны из транскрипта и добавляющий их в ежедневный журнал. Журналы компилируются в структурированную перекрёстно-ссылочную вики — история использования Claude Code сама становится базой знаний без каких-либо ручных записей.

## Связанные записи
- [[llm-wiki-pattern]]
- [[llmwiki-open-source]]
- [[llm-wiki-enterprise-patterns]]
- [[llm-wiki-setup-guide]]
