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

AntonIliashenko/MathWiki is already a sophisticated LLM-maintained research wiki with 70+ opencode skills, proof error tracking, contradiction directories, and computational verification scripts. This article identifies the **real remaining gaps** — not the basics it already has — and provides ready-to-use prompts and scripts for each one. The focus is on what would make the Smith map deformation theory programme specifically more effective.

## Key Ideas

- **What's already working well:** adversarial proof review, citation-first architecture, `wiki/answers/` for error tracking, `wiki/contradictions/` discipline, `math-reasoning` skill, 70+ domain skills.
- **Gap 1: No automated arXiv scan.** The repo has `literature-search` and `academic-search` skills but runs manually. A weekly GitHub Action for `math.DG`, `math.SG`, `math.AP` would surface relevant new preprints automatically.
- **Gap 2: No broken-link detector.** The wiki uses `[[wikilinks]]` but there's no script scanning for targets that don't exist. Several referenced concepts have no page yet.
- **Gap 3: No typed frontmatter relations.** Semantic dependency between papers and concepts lives in prose, not queryable frontmatter fields — limiting automated context assembly.
- **Gap 4: Single monolithic research-question file.** As the programme expands to Cayley/Spin(7) and enumerative invariants, individual conjecture pages with `status` fields will scale better than one big file.
- **Gap 5: No failed-approaches archive.** `wiki/answers/` captures resolved errors. There's no `wiki/approaches/` for abandoned proof strategies — causing dead-end rediscovery in long-running programmes.
- **Gap 6: No daily research context brief.** Each opencode session starts cold. A `research_context.md` injected via AGENTS.md would carry forward current open questions, recent progress, and active methods without manual re-establishment.

## Baseline: What the Repo Already Has

Before adding anything, these are the capabilities *already in place*:

| Capability | How it's implemented |
|---|---|
| Adversarial proof review | `academic-paper-reviewer` (5 reviewers: EIC + 3 peers + Devil's Advocate), `grill-me`, `paper-audit` |
| Proof error tracking | `wiki/answers/` — 4 entries already (Prop 2.9, Thm 4.2, Spencer cohomology, weak Smith equation) |
| Contradiction tracking | `wiki/contradictions/` directory (currently empty; discipline is established) |
| Literature search | `literature-search` (Semantic Scholar/arXiv/OpenAlex), `academic-search`, `deep-research` |
| Mathematical reasoning | `math-reasoning` skill with LaTeX output |
| Computational verification | `find_smith_maps.py`, `verify_smith.py`, `prove_smith.py` |
| LaTeX output | `latex-document`, `latex-paper-en`, `paper-compilation` |
| Confidence labelling | Every page has `confidence: high|medium|low` in frontmatter |
| Citation management | `citation-management`, `bib-search-citation` |
| Novelty checking | `novelty-assessment` skill |

Do **not** add these — they're already covered.

---

## Improvement 1 — Automated Weekly arXiv Scan (steal from OmegaWiki)

OmegaWiki runs a GitHub Action daily for arXiv. For Smith map research, the relevant sections are:
- `math.DG` (Differential Geometry) — Smith maps, calibrated submanifolds, special holonomy
- `math.SG` (Symplectic Geometry) — J-holomorphic curves, Gromov-Witten theory
- `math.AP` (Analysis of PDEs) — elliptic PDE, p-harmonic functions, gradient estimates
- `math.CV` (Complex Variables) — quasiregular maps, Schwarz lemmas

**Add `fetch_arxiv.py` to the repo root:**

```python
# fetch_arxiv.py — weekly arXiv scanner for Smith map research
import urllib.request, json, datetime
from pathlib import Path

AREAS = ["math.DG", "math.SG", "math.AP", "math.CV"]
KEYWORDS = ["smith map", "calibrated", "associative", "G2 structure",
            "Spin(7)", "J-holomorphic", "conformal immersion", "p-harmonic"]
MAX_RESULTS = 20

def fetch_recent(area):
    base = "https://export.arxiv.org/api/query"
    query = f"search_query=cat:{area}&sortBy=submittedDate&sortOrder=descending&max_results={MAX_RESULTS}"
    url = f"{base}?{query}"
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode("utf-8")

def is_relevant(title, abstract):
    text = (title + " " + abstract).lower()
    return any(kw in text for kw in KEYWORDS)
```

**Add to GitHub Actions (`.github/workflows/arxiv-scan.yml`):**

```yaml
name: Weekly arXiv Scan
on:
  schedule:
    - cron: '0 8 * * 1'  # Every Monday 08:00 UTC
  workflow_dispatch:

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: '3.11'}
      - run: python fetch_arxiv.py
      - run: |
          git config user.email "bot@mathwiki"
          git config user.name "arxiv-bot"
          git add wiki/papers/ logs/
          git commit -m "arxiv-scan: $(date +%Y-%m-%d)" || echo "no new papers"
          git push
```

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
---

# [Title]

## Key Results
- [theorem or result 1 — stated precisely]
- [theorem or result 2]

## Methods Used
- [technique from wiki/methods/ if applicable]

## Connections to My Research
- [[Smith Map]] — [how this relates]
- [[research-question: smith-map-deformation-theory]] — [relevance]

## Open Questions It Raises
- [question 1]

## Quotes Worth Keeping
> "[exact quote]" — p. [N]

Flag if any results: (a) contradict existing wiki pages, (b) resolve or
advance the active research question, (c) introduce a method worth adding
to wiki/methods/.
```

---

## Improvement 2 — Broken-Link Detector

The wiki uses `[[Smith Map]]`, `[[Calibration]]`, etc. throughout, but there's no script to check which referenced pages don't exist. This matters especially as new papers reference concepts not yet documented.

**Add `check_links.py` to the repo root:**

```python
# check_links.py — find [[links]] with no target page
import re
from pathlib import Path
from collections import defaultdict

WIKI = Path("wiki")
WIKILINK_RE = re.compile(r"\[\[([^\]|#\n]+?)(?:[|#][^\]]+)?\]\]")

# Build index of all existing page names (case-insensitive)
existing = set()
for p in WIKI.rglob("*.md"):
    existing.add(p.stem.lower())
    existing.add(p.stem)  # exact case too

# Scan for broken links
broken = defaultdict(list)
for p in sorted(WIKI.rglob("*.md")):
    text = p.read_text(encoding="utf-8")
    for link in WIKILINK_RE.findall(text):
        target = link.strip()
        if target.lower() not in existing and target not in existing:
            broken[target].append(p.name)

print(f"Broken links: {len(broken)}")
for target, sources in sorted(broken.items(), key=lambda x: -len(x[1])):
    print(f"  [[{target}]] — referenced in: {', '.join(sources)}")
```

Run weekly: `python check_links.py`. Each broken link is a concept page to create.

**Prompt: Scaffold missing concept pages**
```
These concept pages are referenced in my differential geometry wiki but
don't exist yet. For each one, generate a stub following wiki/concepts/
conventions.

My research focus: Smith maps (calibrated + weakly conformal maps),
G₂/Spin(7) special holonomy, conformal geometry, deformation theory.

Missing concepts: [paste output from check_links.py]

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

## Improvement 3 — Typed Frontmatter Relations

Currently cross-links live in body text as `[[wikilinks]]` and in `## Connections` sections. This is readable but not machine-queryable. Adding structured frontmatter fields enables:
- "What papers does this result depend on?" (automated context injection)
- "What does this paper contradict?" (contradiction detector)
- "What research questions does this settle?" (progress tracking)

**Proposed schema for paper pages:**
```yaml
builds_on:
  - 2012-mcduff-salamon-j-holomorphic-symplectic-topology  # foundational reference
improves_on: []  # direct improvement on a specific prior result
challenges: []   # papers this result contradicts or weakens
resolves:
  - smith-map-deformation-theory  # research question this advances
uses:
  - Nash-Moser Implicit Function Theorem  # method page
  - Moser Iteration Technique
open_problems:
  - cayley-smith-map-moduli  # leaves open (create stub if needed)
```

**Prompt: Add typed relations to existing paper pages**
```
I have a paper wiki entry for my differential geometry research. Add
typed frontmatter relation fields to it.

Paper entry: [paste full page]

Available pages for cross-linking:
  Papers: [list from wiki/papers/]
  Concepts: [list from wiki/concepts/]
  Methods: [list from wiki/methods/]
  Research questions: [list from wiki/research-questions/]

Add these frontmatter fields (leave empty [] if genuinely not applicable):
  builds_on: [paper slugs this result requires]
  improves_on: [paper slugs this directly supersedes]
  challenges: [paper slugs this contradicts]
  resolves: [research-question slugs this advances]
  uses: [method page names]
  open_problems: [new stubs to create]

Return: complete updated frontmatter block only.
If any `challenges` entries exist, also draft a one-paragraph entry for
wiki/contradictions/ explaining the conflict.
```

---

## Improvement 4 — Individual Conjecture Pages

`wiki/research-questions/smith-map-deformation-theory.md` is a single 300+ line file covering the entire deformation theory programme. As the programme expands (Cayley case, enumerative invariants, Z₂-harmonic spinors connections), this won't scale.

**Proposed structure:**
```
wiki/research-questions/
  _index.md               # overview + links to all questions
  smith-map-def-theory.md # the associative case (current, mostly settled)
  cayley-smith-moduli.md  # Spin(7) case — open
  enumerative-invariants.md # long-term programme — open
  z2-spinors-connection.md  # connection to Z₂-harmonic spinors — speculative
```

**Frontmatter for a conjecture page:**
```yaml
---
type: research-question
status: open|in-progress|settled|abandoned
difficulty: foundational|tractable|speculative
last_worked: 2026-05-18
attempts: 2
depends_on:
  - smith-map-deformation-theory  # must be settled first
blocks:
  - enumerative-invariants        # this blocks the longer programme
---
```

**Prompt: Split the current research-question page**
```
I have a single large research-question page covering multiple distinct
sub-problems. Help me split it into individual conjecture pages.

Current page: [paste smith-map-deformation-theory.md]

Proposed sub-pages:
1. smith-map-def-theory (associative G₂ case — largely settled in 2026 preprint)
2. cayley-smith-moduli (Spin(7) case — fully open)
3. enumerative-invariants-calibrated (long-term programme — speculative)

For each sub-page:
- Summarize the specific question (≤ 3 sentences)
- List "What Is Already Known" (draw from the current page)
- List "Key Obstacles" (what makes this hard)
- Set `status:` correctly
- Set `depends_on:` and `blocks:` relations
- Preserve all existing proof details in the relevant sub-page

Return all three complete pages.
```

---

## Improvement 5 — Failed-Approaches Archive

`wiki/answers/` records *resolved* errors (the covering-map mistake, the chain-rule gap). There's no parallel record of *abandoned proof strategies* — approaches that were tried, seemed promising, then hit an obstacle. For a long programme like Cayley Smith map deformation theory, not recording these means rediscovering dead ends months later.

**Add `wiki/approaches/` with this schema:**
```yaml
---
type: proof-attempt
target: cayley-smith-moduli   # which research question
status: failed|partial|abandoned|promising
method: Nash-Moser Implicit Function Theorem
date_attempted: 2026-05-18
---

# Attempt: Nash-Moser for Cayley Smith Maps

## Strategy
[What the approach tried to do]

## Where It Got Stuck
[The exact obstacle — be precise enough that future-you won't retry it]

## Why It Might Still Work With Modifications
[If applicable: what would need to change]

## Alternative Suggested
[Next approach to try instead]
```

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

## Improvement 6 — Daily Research Context Brief

Every opencode session starts cold. The AGENTS.md currently provides domain rules and a repository map. Add a generated `research_context.md` — updated after each session — that primes the agent with the current state of the programme:

**Add to AGENTS.md:**
```markdown
## Current Research Context
See `research_context.md` (regenerate after each session).

The active research question is: wiki/research-questions/smith-map-deformation-theory.md
Current blockers: [list from approaches/ with status=abandoned or stuck]
Most recent results: [last 3 entries in wiki/answers/]
Papers read this month: [from logs/]
```

**Prompt: Generate a fresh research context brief**
```
Generate a concise research context brief for injection into my opencode
AGENTS.md. This will be read at the start of every session.

Current programme: deformation theory of Smith maps (calibrated, weakly
conformal maps) — developing moduli spaces analogous to J-holomorphic curves.

Source material:
- Active research question: [paste smith-map-deformation-theory.md summary]
- Recent answers/: [list last 3 answer pages and their resolutions]
- Recent approaches/: [list any abandoned approaches with reasons]
- Papers added this month: [list]

Output: a 150-word brief in this structure:

## Research Context (updated [date])
**Programme:** [1 sentence]
**Current frontier:** [1 sentence — what's the next open problem]
**Recent progress:** [2-3 bullet points]
**Active dead ends:** [1-2 bullet points — approaches NOT to retry]
**Next session should focus on:** [1 sentence recommendation]

This should read like a handoff note from your past self to your future self.
```

---

## What Is Already Excellent (Do Not Rebuild)

- **`academic-paper-reviewer`** already simulates 5 reviewers including Devil's Advocate — this is better than OmegaWiki's cross-model review. Use it.
- **`grill-me`** is a strong adversarial proof checker. Run it on every new proof before filing in the wiki.
- **`novelty-assessment`** replaces the "novelty check before compile" idea from OmegaWiki — it already does a systematic search.
- **`wiki/contradictions/`** already encodes the discipline of tracking conflicts. When it gets populated, the `challenges:` frontmatter field (Improvement 3) will make it queryable.
- **Python scripts** (`find_smith_maps.py` etc.) are already doing computational grounding. These are ahead of OmegaWiki's feature set.

## Priority Table

| # | Improvement | Effort | Impact | When |
|---|---|---|---|---|
| 1 | Add `check_links.py` + run it | 20 min | High | **Now** |
| 2 | Split research-question page into sub-pages | 1 hr | High | **Now** |
| 3 | Add typed frontmatter relations to 5 key paper pages | 1 hr | Medium | This week |
| 4 | Start `wiki/approaches/` — file 2-3 past dead ends | 30 min | High | This week |
| 5 | Generate and commit `research_context.md` | 15 min | High | **Now** |
| 6 | `fetch_arxiv.py` + GitHub Action | 3 hr | High (ongoing) | Next sprint |

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

AntonIliashenko/MathWiki — уже зрелая LLM-поддерживаемая исследовательская вики с 70+ навыками opencode, трекером ошибок в доказательствах и вычислительными скриптами. Эта статья определяет реальные оставшиеся пробелы и предоставляет готовые промпты и скрипты для каждого из них.

## Ключевые идеи

- **Что уже работает хорошо:** состязательная рецензия доказательств, citation-first архитектура, `wiki/answers/` для трекинга ошибок, дисциплина `wiki/contradictions/`, навык `math-reasoning`, 70+ доменных навыков.
- **Пробел 1: нет автоматического сканирования arXiv.** `literature-search` и `academic-search` работают вручную. Еженедельный GitHub Action для `math.DG`, `math.SG`, `math.AP` выявит релевантные новые препринты автоматически.
- **Пробел 2: нет детектора сломанных ссылок.** Несколько концептов, на которые ссылается вики, не имеют страниц.
- **Пробел 3: нет типизированных полей в frontmatter.** Семантические зависимости между статьями и концептами живут в тексте, а не в запрашиваемых полях frontmatter.
- **Пробел 4: монолитный файл исследовательского вопроса.** По мере расширения программы (случай Cayley/Spin(7), перечислительные инварианты) нужны отдельные страницы гипотез со статусами.
- **Пробел 5: нет архива неудачных подходов.** `wiki/answers/` фиксирует ошибки. Нет `wiki/approaches/` для стратегий, которые были опробованы и оставлены — это приводит к повторному открытию тупиков.
- **Пробел 6: нет ежедневного брифа о текущем состоянии исследования.** Каждая сессия opencode начинается с нуля. `research_context.md`, внедрённый через AGENTS.md, передаст контекст от прошлого «я» будущему.

## Базовый уровень: что уже есть в репозитории

| Возможность | Реализация |
|---|---|
| Состязательная рецензия | `academic-paper-reviewer` (5 рецензентов), `grill-me`, `paper-audit` |
| Трекинг ошибок в доказательствах | `wiki/answers/` — 4 записи (Предл. 2.9, Теор. 4.2, когомологии Спенсера, слабое уравнение Smith) |
| Трекинг противоречий | Директория `wiki/contradictions/` (пока пустая) |
| Поиск литературы | `literature-search`, `academic-search`, `deep-research` |
| Математические рассуждения | Навык `math-reasoning` с LaTeX-выводом |
| Вычислительная верификация | `find_smith_maps.py`, `verify_smith.py`, `prove_smith.py` |
| LaTeX-экспорт | `latex-document`, `latex-paper-en`, `paper-compilation` |
| Метки достоверности | Каждая страница имеет `confidence: high|medium|low` |

**Не добавляйте** — всё это уже покрыто.

---

## Улучшение 1 — Автоматическое еженедельное сканирование arXiv

Релевантные разделы для Smith map-исследований:
- `math.DG` (Дифференциальная геометрия) — Smith-отображения, калиброванные подмногообразия, специальная голономия
- `math.SG` (Симплектическая геометрия) — J-голоморфные кривые, теория Громова-Виттена
- `math.AP` (Анализ PDE) — эллиптические PDE, p-гармонические функции, оценки градиентов
- `math.CV` (Комплексный анализ) — квазирегулярные кривые, леммы Шварца

Добавьте `fetch_arxiv.py` + GitHub Action `.github/workflows/arxiv-scan.yml` (ежепонедельный запуск UTC 08:00). Подробнее — в английской версии выше.

**Промпт: извлечение записи вики из аннотации arXiv**
```
Новая статья на arXiv, релевантная моей исследовательской программе по
Smith-отображениям / калиброванной геометрии.

Title, Authors, arXiv ID, Abstract: [вставить]
Существующие статьи в вики (для перекрёстных ссылок): [список из wiki/papers/]
Существующие концепты: [список из wiki/concepts/]

Создайте запись вики по конвенциям wiki/papers/.
Отметьте, если результаты: (а) противоречат существующим страницам,
(б) продвигают активный исследовательский вопрос, (в) вводят метод
для wiki/methods/.
```

---

## Улучшение 2 — Детектор сломанных ссылок

Добавьте `check_links.py` в корень репозитория (код — в английской версии). Запускайте еженедельно: `python check_links.py`. Каждая сломанная ссылка — страница концепта, которую нужно создать.

**Промпт: создание заготовок для отсутствующих концептов**
```
Эти страницы концептов упоминаются в моей вики по дифференциальной
геометрии, но не существуют. Создайте заготовки по конвенциям wiki/concepts/.

Фокус: Smith-отображения, G₂/Spin(7), конформная геометрия, теория деформаций.
Отсутствующие концепты: [вывод check_links.py]
```

---

## Улучшение 3 — Типизированные поля frontmatter

Добавьте к страницам статей структурированные поля зависимостей:
```yaml
builds_on: [слаг-статьи]
improves_on: []
challenges: []
resolves: [слаг-исследовательского-вопроса]
uses: [название-метода]
open_problems: [новые-заготовки]
```

---

## Улучшение 4 — Отдельные страницы гипотез

Разбейте `smith-map-deformation-theory.md` на:
- `smith-map-def-theory.md` (ассоциативный случай G₂ — в основном решён)
- `cayley-smith-moduli.md` (случай Spin(7) — полностью открыт)
- `enumerative-invariants-calibrated.md` (долгосрочная программа — спекулятивно)

Frontmatter: `status: open|in-progress|settled|abandoned`, `depends_on:`, `blocks:`.

---

## Улучшение 5 — Архив неудачных подходов

Создайте `wiki/approaches/` для стратегий доказательства, которые были опробованы и оставлены. Schema:
```yaml
type: proof-attempt
target: cayley-smith-moduli
status: failed|partial|abandoned|promising
method: Nash-Moser Implicit Function Theorem
date_attempted: 2026-05-18
```

**Промпт: запись неудавшегося подхода**
```
Я провёл сессию, пытаясь доказать [УТВЕРЖДЕНИЕ] с помощью [ПОДХОД] и
застрял. Извлеките структурированную запись неудавшегося подхода.

Цель: [слаг из wiki/research-questions/]
Метод: [подход]
Точка остановки: [где именно]
Ключевой инсайт: [что узнали, даже если не сработало]
Причина фундаментального провала (если известна): [почему]

Вывод: полная запись wiki/approaches/ по схеме выше.
```

---

## Улучшение 6 — Ежедневный бриф о текущем состоянии

Добавьте в AGENTS.md ссылку на `research_context.md` — генерируйте его после каждой сессии. Это «записка от прошлого себя будущему себе»: текущий фронтир, недавний прогресс, тупики которых следует избегать.

---

## Что уже отлично (не перестраивайте)

- **`academic-paper-reviewer`** — лучше, чем перекрёстная рецензия OmegaWiki. Используйте.
- **`grill-me`** — сильная состязательная проверка. Запускайте на каждое новое доказательство.
- **`novelty-assessment`** — уже делает систематический поиск новизны.
- **Python-скрипты** — уже опережают возможности OmegaWiki.

## Приоритет

| # | Улучшение | Усилие | Влияние | Когда |
|---|---|---|---|---|
| 1 | `check_links.py` + запустить | 20 мин | Высокое | **Сейчас** |
| 2 | Разбить файл исследовательского вопроса | 1 час | Высокое | **Сейчас** |
| 3 | Добавить типизированные связи к 5 ключевым статьям | 1 час | Среднее | На этой неделе |
| 4 | Начать `wiki/approaches/` — записать 2-3 тупика | 30 мин | Высокое | На этой неделе |
| 5 | Сгенерировать и закоммитить `research_context.md` | 15 мин | Высокое | **Сейчас** |
| 6 | `fetch_arxiv.py` + GitHub Action | 3 часа | Высокое (регулярно) | Следующий спринт |

## Связанные записи

- [[mathwiki-smith-maps-research]] ([AntonIliashenko/MathWiki: исследовательская вики](./mathwiki-smith-maps-research.md))
- [[omegawiki-research-platform]] ([OmegaWiki: вики-центрированная платформа](../tools/omegawiki-research-platform.md))
- [[yaro-mathwiki]] ([Yaro2709/MathWiki: рукотворная база математических знаний](../tools/yaro-mathwiki.md))
- [[llm-wiki-ecosystem]] ([Экосистема LLM Wiki](../tools/llm-wiki-ecosystem.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki для научных исследований](../tips/llm-wiki-scientific-research.md))
- [[llm-git-knowledge-accumulation]] ([LLM Project Memory via Git](../tips/llm-git-knowledge-accumulation.md))
