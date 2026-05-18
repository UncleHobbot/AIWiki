---
title: "Improving AntonIliashenko/MathWiki: What to Add Next"
title_ru: "Улучшение AntonIliashenko/MathWiki: что добавить дальше"
category: research
tags: [mathwiki, differential-geometry, smith-maps, calibrated-geometry, obsidian, llm-wiki, opencode, research-workflow, prompts]
aliases: [MathWiki improvements, AntonIliashenko MathWiki improvements, math research automation]
confidence: high
updated: 2026-05-18
sources:
  - https://github.com/AntonIliashenko/MathWiki
  - https://github.com/skyllwt/OmegaWiki
---

## Summary

AntonIliashenko/MathWiki is a sophisticated LLM-maintained research wiki for Smith map deformation theory. As of 2026-05-18, all six originally planned infrastructure improvements have been implemented: automated arXiv scanning, broken-link detection, typed frontmatter relations, individual conjecture pages, a failed-approaches archive, and a session handoff brief. This article documents what was built, how it was implemented, and the remaining open gaps.

## Key Ideas

- **All 6 planned improvements are done** (implemented 2026-05-18): arXiv scan, link checker, typed relations, conjecture pages, approaches archive, context brief.
- **Bonus improvement 7 was added:** `/wiki-insights` — a retrospective session analysis command that reads git history, `wiki/approaches/`, `wiki/answers/`, and conversation context to surface patterns, failures, and knowledge gaps.
- **Current state (2026-05-18):** 19 papers, 18 concepts, 3 methods, 7 answers, 5 approaches, 5+1 research-question pages, 1 review; 13 scripts in `scripts/`; 7 domain commands; 70+ opencode skills.
- **Remaining gaps after implementation:** 22 broken wiki links (missing concept stubs), empty `wiki/contradictions/` (discipline exists, no entries yet), no method pages for Taubes trick / Spencer theory / Banach manifold IFT, and Cayley Smith map deformation theory (Section 2.3 of the preprint is empty — the active mathematical frontier).
- **OpenCode skills are now project-level** (`.opencode/skills/`) — available to anyone who clones the repo without per-machine installation.

## Baseline: What the Repo Has Now

| Capability | Implementation |
|---|---|
| Adversarial proof review | `academic-paper-reviewer` (EIC + 3 peers + Devil's Advocate), `grill-me`, `paper-audit` |
| Proof error tracking | `wiki/answers/` — 7 entries (Prop 2.9, Thm 4.2, Spencer cohomology, weak Smith eq., deg-3 harmonics, role of L, spherical coords) |
| Contradiction tracking | `wiki/contradictions/` — directory established, **0 entries yet** |
| Failed-approaches archive | `wiki/approaches/` — 5 entries (all targeting `smith-map-def-theory`) |
| Literature search | `literature-search`, `academic-search`, `deep-research` |
| arXiv scanning | `/wiki-arxiv` + `scripts/fetch_arxiv.py` — weekly scan, math.DG/SG/AP/CV, 25+ keywords |
| Broken-link detection | `/wiki-checklinks` + `scripts/check_links.py` — near-miss detection, 3 buckets |
| Typed frontmatter relations | `/wiki-relations` + `scripts/add_relations.py` — all 19 papers have `builds_on`, `resolves`, `uses`, etc. |
| Individual conjecture pages | `wiki/research-questions/` — 5 focused pages + hub + `_index.md` with dependency graph |
| Session handoff brief | `research_context.md` + `/wiki-context` + `scripts/generate_context.py` |
| Retrospective analysis | `/wiki-insights` + `scripts/analyze_sessions.py` |
| Mathematical reasoning | `math-reasoning` with LaTeX output |
| Computational verification | `find_smith_maps.py`, `verify_smith.py`, `prove_smith.py` (all in `scripts/`) |
| Relation graph queries | `scripts/wiki_graph.py --resolves --builds-on SLUG --dot` |
| LaTeX output | `latex-document`, `latex-paper-en`, `paper-compilation`; 30+ PDFs in `output/` |
| Confidence labelling | Every page has `confidence: high|medium|low` |
| Session analysis | `scripts/analyze_sessions.py [--git] [--gaps] [--failures] [--json]` |

---

## Improvement 1 — Automated Weekly arXiv Scan ✅ DONE

**Status:** Implemented 2026-05-18. Commit `fe2a5bc`.

`/wiki-arxiv` fetches the last 14 days of submissions from arXiv (math.DG, math.SG, math.AP, math.CV), filters by 25+ keywords specific to Smith map / calibrated geometry research, presents ranked results (RELEVANT / BORDERLINE / SKIP), and creates `wiki/papers/` entries for confirmed papers. Also writes a scan log to `logs/arxiv-scan-YYYY-MM-DD.md`, flags concepts in abstracts without wiki pages, and checks whether a paper advances the active research question.

**Standalone:** `python scripts/fetch_arxiv.py [--days N] [--cat math.DG] [--json]`

**Prompt: Extract paper wiki entry from arXiv abstract**
```
New arXiv paper relevant to my Smith map / calibrated geometry research.

Title: [title]
Authors: [authors]
arXiv ID: [id]  (https://arxiv.org/abs/[id])
Abstract: [abstract]

My existing wiki papers (for cross-linking):
[paste list from wiki/papers/]

My existing concepts (for cross-linking):
[paste list from wiki/concepts/]

Create a wiki entry following wiki/papers/ conventions:
---
type: paper
status: reading|read
updated: [today]
confidence: medium
builds_on: []
resolves: []
uses: []
open_problems: []
---

# [Title]

## Key Results
- [theorem or result 1 — stated precisely]

## Methods Used
- [technique from wiki/methods/ if applicable]

## Connections to My Research
- [[Smith Map]] — [how this relates]

## Open Questions It Raises
- [question 1]

Flag if any results: (a) contradict existing wiki pages, (b) resolve or
advance the active research question, (c) introduce a method worth adding
to wiki/methods/.
```

---

## Improvement 2 — Broken-Link Detector ✅ DONE

**Status:** Implemented 2026-05-18. Commit `e6bce7b`.

`/wiki-checklinks` scans every `[[wikilink]]` against the page index with near-miss detection (Jaccard word-similarity), classifying results into three buckets:
- **Bucket A** — typo/near-miss (e.g. `[[Elliptic Edge Operators]]` → `Elliptic Edge Operator`)
- **Bucket B** — links pointing at answer or research-question pages instead of concept pages
- **Bucket C** — genuinely missing concept stubs

**Current state:** 22 broken links (primarily Bucket C: Laplacian, Ricci Curvature, Weyl Curvature, Dirac Operator, Comass Norm, and ~15 others). Run `/wiki-checklinks` and choose `stubs all` to scaffold them.

**Standalone:** `python scripts/check_links.py [--broken-only] [--orphans-only] [--json]`

**Prompt: Scaffold missing concept pages**
```
These concept pages are referenced in my differential geometry wiki but
don't exist yet. For each one, generate a stub following wiki/concepts/
conventions.

My research focus: Smith maps (calibrated + weakly conformal maps),
G₂/Spin(7) special holonomy, conformal geometry, deformation theory.

Missing concepts: [paste output from check_links.py --broken-only]

For each concept, create:
---
type: concept
status: stub
updated: [today]
confidence: low
---

# [Concept Name]

## Definition
[1-3 sentence definition appropriate for differential geometry research]

## Why It Appears in My Wiki
[1 sentence: which paper/method uses this concept]

## Related Concepts
- [[related-concept]]

Mark concepts you're unsure about with `confidence: low` and add a note
`# unverified — needs source citation`.
```

---

## Improvement 3 — Typed Frontmatter Relations ✅ DONE

**Status:** Implemented 2026-05-18. Commit `3d9dc90`. All 19 paper pages updated via `scripts/add_relations.py`.

**Current graph state:**
- 25 `builds_on` edges
- 5 `improves_on` edges
- 1 `resolves` edge (the 2026 deformation theory preprint resolves `smith-map-def-theory`)
- 7 `uses` edges
- 2 `open_problems` edges
- 0 `challenges` edges (no confirmed contradictions yet)

**Schema (all paper pages):**
```yaml
builds_on:      # paper slugs this work foundationally depends on
improves_on:    # papers this work directly supersedes
challenges:     # papers whose claims this contradicts
resolves:       # research-question slugs this advances
uses:           # method page names
open_problems:  # research-question slugs left open
```

**Query:** `python scripts/wiki_graph.py [--resolves] [--builds-on SLUG] [--dot]`

**Constraint enforced by `/wiki-relations`:** `challenges` entries require a `wiki/contradictions/` page; all slug references must exist as actual files.

---

## Improvement 4 — Individual Conjecture Pages ✅ DONE

**Status:** Implemented 2026-05-18. Commit `340b6db`. Monolithic `smith-map-deformation-theory.md` split into five focused pages.

**Current research-question pages:**

| Page | Status | Difficulty | Notes |
|---|---|---|---|
| `smith-map-def-theory` | in-progress | foundational | Associative G₂ case; Prop 2.9 + polynomial non-existence proved; attempts: 7 |
| `cayley-smith-moduli` | open | tractable | Spin(7) case — **current frontier** |
| `compactness-smith-maps` | open | foundational | Blocks enumerative theory |
| `enumerative-invariants-calibrated` | open | speculative | Long-term programme |
| `z2-spinors-connection` | open | speculative | No precise conjecture yet |

The original `smith-map-deformation-theory.md` is preserved as a hub page to avoid breaking existing links. `wiki/research-questions/_index.md` has a dependency table and graph.

**Dependency chain:** `smith-map-def-theory` → `cayley-smith-moduli` → `compactness-smith-maps` → `enumerative-invariants-calibrated`

---

## Improvement 5 — Failed-Approaches Archive ✅ DONE

**Status:** Implemented 2026-05-18. Commit `7fbe236`. Five entries documented in `wiki/approaches/`.

| Entry | Method | Status | Core obstacle |
|---|---|---|---|
| `covering-map-injectivity` | Covering space argument | failed | `u(L)` need not be a manifold |
| `naive-linearisation-smith-equation` | Direct linearisation | failed | `D_u ≡ 0` — equality case of a maximum; fundamental obstruction for all k > 2 |
| `direct-fredholm-spinorial-equation` | IFT on spinorial equation | partial | Overdetermined: rank(domain) < rank(codomain) |
| `polynomial-smith-map-existence` | Polynomial ansatz (SymPy + NumPy) | failed | Conformality forces nonlinear Jacobian to zero |
| `submanifold-rigidity-parametrization` | Submanifold rigidity decomposition | failed | No Liouville-type uniqueness for conformal immersions |

**Prompt: Extract a failed-approach entry from a session**
```
I just spent a session trying to prove [STATEMENT] using [APPROACH] and
got stuck. Extract a structured failed-approach entry.

Research question targeted: [slug from wiki/research-questions/]
Method attempted: [approach]
Sticking point: [where exactly things broke down — be precise]
Key insight gained: [what you learned even though it didn't work]
Reason the approach fundamentally fails (if known): [why]
What would need to be true for this approach to work: [missing condition]

Output: complete wiki/approaches/ entry in the schema above.
Also: does this failure suggest a contradiction with any existing wiki
entry? If so, draft a `wiki/contradictions/` entry.
```

---

## Improvement 6 — Daily Research Context Brief ✅ DONE

**Status:** Implemented 2026-05-18. Commit `f550037`. `research_context.md` committed and active; referenced from AGENTS.md.

**Current brief excerpt (2026-05-18):**
> **Frontier:** Cayley (Spin(7)) Smith map deformation theory — Section 2.3 of the deformation theory preprint is empty. **Dead ends — do not retry:** naive linearisation (`D_u ≡ 0`); direct Fredholm on spinorial equation (overdetermined). **Next session:** construct `F̃_Cay = C ∘ F_Cay` by direct analogy with Section 2.1.

**Regenerate:** `/wiki-context` or `python scripts/generate_context.py --brief`

---

## Improvement 7 — Session Retrospective Analysis ✅ DONE (Bonus)

**Status:** Implemented 2026-05-18. Commit `6d90567`. Not in the original plan — added as a result of recognising the need for meta-level session analysis.

`/wiki-insights` reads git history, `wiki/approaches/`, `wiki/answers/`, memory files, CLAUDE.md Red Flags, and the current conversation to produce a structured report across six sections:

1. Working style patterns
2. Success history
3. **Failure history** *(enforced as the longest section)*
4. Process improvements
5. Knowledge to extract as wiki documents
6. Immediate actions (ranked by impact, exact file paths)

Every observation must cite evidence by slug, commit, or conversation moment. Reports save to `wiki/insights/YYYY-MM-DD-insights.md` on request.

**Standalone:** `python scripts/analyze_sessions.py [--git] [--gaps] [--failures] [--json]`

---

## Remaining Gaps (Post-Implementation)

These items were identified in the 2026-05-18 session but not addressed:

### Gap A — 22 Broken Wiki Links

`/wiki-checklinks` reports 22 broken `[[links]]`, primarily Bucket C (genuinely missing concept stubs). Key missing pages:

- `Laplacian`, `Ricci Curvature`, `Weyl Curvature` — basic differential geometry concepts referenced across many papers but never given stub pages
- `Dirac Operator` — required for the spinorial formulation of Smith maps
- `Comass Norm` — used in calibration theory definition

**Fix:** Run `/wiki-checklinks`, then `stubs all` to scaffold the ~19 missing stubs.

### Gap B — Empty `wiki/contradictions/`

The discipline is established (the directory exists, the `challenges:` frontmatter field is enforced). No entries have been created yet despite several near-conflicts being documented in `wiki/answers/`:
- The original Prop 2.9 proof (covering-map argument) is contradicted by `fixing-proposition-2-9-covering-map-error.md`
- Theorem 4.2 (`fixing-theorem-4-2-chain-rule.md`) has `confidence: low` — the required gradient estimate is an open problem

**Fix:** Cross-reference `wiki/answers/` entries into `wiki/contradictions/` pages using the `challenges:` field.

### Gap C — Missing Method Pages

Three methods are used across multiple papers and the deformation theory proof but have no `wiki/methods/` pages:
- **Taubes trick** — used in moduli space compactness arguments
- **Overdetermined Elliptic PDE / Spencer Theory** — the theoretical backbone of the deformation theory proof
- **Banach Manifold IFT** — used in the smooth structure theorem (Theorem 2.28)

**Fix:** Create stubs, then fill with material from `sources/Deformations.pdf`.

### Gap D — Cayley Smith Map Deformation Theory (Mathematical)

Section 2.3 of the 2026 preprint (`output/smith-map-deformation-theory.pdf`) is empty. The associative blueprint (spinorial reformulation `η(θ) = 0` → weak Smith equation `F̃ = C ∘ F`) transfers to k = 4, but has not been executed.

**Fix:** Write Section 2.3 using `/wiki-conjecture` to track progress against `wiki/research-questions/cayley-smith-moduli.md`. Use `grill-me` to stress-test the spinorial decomposition before committing to the preprint.

---

## What Is Already Excellent (Do Not Rebuild)

- **`academic-paper-reviewer`** already simulates 5 reviewers including Devil's Advocate — better than OmegaWiki's cross-model review. Use it.
- **`grill-me`** is a strong adversarial proof checker. Run on every new proof before filing in the wiki.
- **`novelty-assessment`** does systematic novelty search — do not re-implement.
- **`wiki/contradictions/`** discipline is established. When populated, the `challenges:` field makes it queryable.
- **Python scripts** (`find_smith_maps.py`, `verify_smith.py`, `prove_smith.py`) are ahead of OmegaWiki's feature set.
- **`wiki/approaches/`** prevents dead-end rediscovery. Always check it before starting a new proof strategy.

## Priority Table

| # | Item | Effort | Impact | When |
|---|---|---|---|---|
| 1 | Fill `wiki/contradictions/` from existing `wiki/answers/` | 30 min | High | **Now** |
| 2 | Scaffold 22 missing concept stubs via `/wiki-checklinks stubs all` | 20 min | High | **Now** |
| 3 | Write Cayley Smith map deformation theory (Section 2.3) | weeks | Very high | Active frontier |
| 4 | Add method pages: Taubes trick, Spencer theory, Banach manifold IFT | 2 hr | Medium | This week |
| 5 | Resolve Theorem 4.2 (`confidence: low`) once gradient estimate is established | depends | High | After Gap D progress |

## Related Entries

- [[mathwiki-smith-maps-research]] ([AntonIliashenko/MathWiki: Research Wiki for Smith Map Deformation Theory](./mathwiki-smith-maps-research.md))
- [[omegawiki-research-platform]] ([OmegaWiki: Wiki-Centric AI Research Platform](../tools/omegawiki-research-platform.md))
- [[yaro-mathwiki]] ([Yaro2709/MathWiki: Hand-Crafted Math Knowledge Base](../tools/yaro-mathwiki.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llm-git-knowledge-accumulation]] ([LLM Project Memory via Git: Plan-Execute-Distill Loop](../tips/llm-git-knowledge-accumulation.md))

---
<!-- RU -->

## Краткое описание

AntonIliashenko/MathWiki — зрелая LLM-поддерживаемая исследовательская вики для теории деформаций Smith-отображений. По состоянию на 2026-05-18 все шесть запланированных инфраструктурных улучшений реализованы: автоматическое сканирование arXiv, детектор сломанных ссылок, типизированные поля frontmatter, отдельные страницы гипотез, архив неудачных подходов и бриф о текущем состоянии сессии. Статья документирует, что было построено, как это реализовано и какие пробелы остаются.

## Ключевые идеи

- **Все 6 запланированных улучшений реализованы** (2026-05-18): сканирование arXiv, детектор ссылок, типизированные отношения, страницы гипотез, архив подходов, бриф контекста.
- **Добавлено бонусное улучшение 7:** `/wiki-insights` — ретроспективный анализ сессий: читает историю git, `wiki/approaches/`, `wiki/answers/` и контекст беседы, чтобы выявить паттерны, ошибки и пробелы знаний.
- **Текущее состояние (2026-05-18):** 19 статей, 18 концептов, 3 метода, 7 ответов, 5 подходов, 5+1 страниц исследовательских вопросов, 1 обзор; 13 скриптов в `scripts/`; 7 доменных команд.
- **Оставшиеся пробелы:** 22 сломанные ссылки (нужны заготовки концептов), пустой `wiki/contradictions/`, нет страниц методов для трюка Таубса / теории Спенсера / ТФН Банаха–Пикара, Section 2.3 препринта пуста (теория деформаций Cayley Smith-отображений).
- **Навыки OpenCode теперь на уровне проекта** (`.opencode/skills/`) — доступны всем при клонировании репозитория.

## Базовый уровень: что есть сейчас

| Возможность | Реализация |
|---|---|
| Состязательная рецензия | `academic-paper-reviewer` (5 рецензентов), `grill-me`, `paper-audit` |
| Трекинг ошибок | `wiki/answers/` — 7 записей |
| Трекинг противоречий | `wiki/contradictions/` — 0 записей (дисциплина установлена) |
| Архив неудачных подходов | `wiki/approaches/` — 5 записей |
| Поиск литературы | `literature-search`, `academic-search`, `deep-research` |
| Сканирование arXiv | `/wiki-arxiv` + `scripts/fetch_arxiv.py` |
| Детектор ссылок | `/wiki-checklinks` + `scripts/check_links.py` |
| Типизированные отношения | `/wiki-relations` + `scripts/add_relations.py`, 19 статей обновлены |
| Страницы гипотез | 5 сфокусированных страниц + hub + `_index.md` с графом зависимостей |
| Бриф сессии | `research_context.md` + `/wiki-context` + `scripts/generate_context.py` |
| Ретроспективный анализ | `/wiki-insights` + `scripts/analyze_sessions.py` |
| Запросы к графу отношений | `scripts/wiki_graph.py --resolves --builds-on SLUG --dot` |

## Реализованные улучшения

### Улучшение 1 — arXiv-сканирование ✅ Готово

`/wiki-arxiv` получает последние 14 дней подач с arXiv (math.DG, math.SG, math.AP, math.CV), фильтрует по 25+ ключевым словам, ранжирует результаты (RELEVANT / BORDERLINE / SKIP) и создаёт записи `wiki/papers/`. Пишет лог в `logs/arxiv-scan-YYYY-MM-DD.md`. Отдельный скрипт: `python scripts/fetch_arxiv.py [--days N] [--json]`.

### Улучшение 2 — Детектор сломанных ссылок ✅ Готово

`/wiki-checklinks` сканирует все `[[wikilinks]]` с нечётким поиском (сходство Жаккара), разбивает по 3 корзинам. **Текущее состояние:** 22 сломанные ссылки. Запустите `/wiki-checklinks`, затем `stubs all` для создания заготовок.

### Улучшение 3 — Типизированные поля frontmatter ✅ Готово

Все 19 страниц статей обновлены через `scripts/add_relations.py`. Граф: 25 рёбер `builds_on`, 1 ребро `resolves`, 7 рёбер `uses`. Запросы: `python scripts/wiki_graph.py --resolves --dot`.

### Улучшение 4 — Отдельные страницы гипотез ✅ Готово

Монолитный файл разбит на 5 страниц с dependency-графом: `smith-map-def-theory` → `cayley-smith-moduli` → `compactness-smith-maps` → `enumerative-invariants-calibrated`. Текущий фронтир: теория деформаций Cayley (Spin(7)).

### Улучшение 5 — Архив неудачных подходов ✅ Готово

`wiki/approaches/` содержит 5 записей. Ключевые тупики: наивная линеаризация уравнения Smith (`D_u ≡ 0`), прямой метод Фредгольма на спинорном уравнении (переопределённость). Всегда проверяйте этот архив перед началом нового доказательства.

### Улучшение 6 — Бриф текущего состояния ✅ Готово

`research_context.md` создан и закоммичен; читается в начале каждой сессии через AGENTS.md. Текущий фронтир: Section 2.3 препринта пуста — нужно построить `F̃_Cay = C ∘ F_Cay`. Регенерация: `/wiki-context`.

### Улучшение 7 — Ретроспективный анализ сессий ✅ Готово (бонус)

`/wiki-insights` читает историю git, `wiki/approaches/`, `wiki/answers/` и контекст, выдавая структурированный отчёт по 6 разделам. Акцент на разделе **Failure history** — намеренно самый длинный. Отчёты сохраняются в `wiki/insights/YYYY-MM-DD-insights.md`.

---

## Оставшиеся пробелы

### Пробел A — 22 сломанные ссылки (заготовки концептов)

Нужны: `Laplacian`, `Ricci Curvature`, `Weyl Curvature`, `Dirac Operator`, `Comass Norm` и ещё ~15 концептов. Исправление: `/wiki-checklinks` → `stubs all`.

### Пробел B — Пустой `wiki/contradictions/`

Дисциплина установлена; записей нет. Перекрёстные ссылки `wiki/answers/` (Пред. 2.9, Теор. 4.2) должны стать страницами в `wiki/contradictions/`.

### Пробел C — Нет страниц методов

Отсутствуют: трюк Таубса, переопределённые эллиптические PDE / теория Спенсера, ТФН Банаха–Пикара. Все три используются в доказательстве теоремы деформации.

### Пробел D — Теория деформаций Cayley (математический фронтир)

Section 2.3 препринта пуста. Следующий шаг: написать спинорное разложение для Spin(7) и построить слабое уравнение Cayley Smith по аналогии с Section 2.1.

## Приоритет

| # | Задача | Усилие | Влияние | Когда |
|---|---|---|---|---|
| 1 | Заполнить `wiki/contradictions/` из `wiki/answers/` | 30 мин | Высокое | **Сейчас** |
| 2 | Заготовки 22 концептов через `/wiki-checklinks stubs all` | 20 мин | Высокое | **Сейчас** |
| 3 | Написать теорию деформаций Cayley (Section 2.3) | недели | Очень высокое | Активный фронтир |
| 4 | Страницы методов: трюк Таубса, теория Спенсера, ТФН Банаха | 2 часа | Среднее | На этой неделе |
| 5 | Закрыть Теорему 4.2 (`confidence: low`) | зависит от Gap D | Высокое | После прогресса в Gap D |

## Связанные записи

- [[mathwiki-smith-maps-research]] ([AntonIliashenko/MathWiki: исследовательская вики](./mathwiki-smith-maps-research.md))
- [[omegawiki-research-platform]] ([OmegaWiki: вики-центрированная платформа](../tools/omegawiki-research-platform.md))
- [[yaro-mathwiki]] ([Yaro2709/MathWiki: рукотворная база математических знаний](../tools/yaro-mathwiki.md))
- [[llm-wiki-ecosystem]] ([Экосистема LLM Wiki](../tools/llm-wiki-ecosystem.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki для научных исследований](../tips/llm-wiki-scientific-research.md))
- [[llm-git-knowledge-accumulation]] ([LLM Project Memory via Git](../tips/llm-git-knowledge-accumulation.md))
