---
title: "LLM-Powered Math Research: Ideas to Steal for Your MathWiki"
title_ru: "LLM-инструменты для математических исследований: идеи для вашей MathWiki"
category: tips
tags: [mathwiki, math-research, llm-wiki, omegawiki, knowledge-graph, automation, obsidian, prompts, research-workflow]
aliases: [MathWiki improvements, math research automation, LLM math wiki]
confidence: high
updated: 2026-05-18
sources:
  - https://github.com/AntonIliashenko/MathWiki
  - https://github.com/skyllwt/OmegaWiki
  - https://github.com/Yaro2709/MathWiki
---

## Summary

A concrete playbook for making a personal math research wiki dramatically more efficient by transplanting six ideas from OmegaWiki and the broader LLM Wiki ecosystem onto an Obsidian-based MathWiki (Yaro2709-style atomic-note architecture). Each improvement is explained, ranked by impact, and shipped with a ready-to-paste Claude Code prompt.

## Key Ideas

- **Typed relation graph** — replace the single `Использует:` field with 7 semantic edge types. Unlocks gap detection, generalization search, and adversarial proof review.
- **Gap detector** — scan the vault for `[[links]]` that point to non-existent notes; these are stubs waiting to be written, not errors.
- **Adversarial proof review** — a second model (or a second Claude pass) tries to find a counterexample or logical gap in your proof sketch before you commit it.
- **arXiv daily digest** — morning scan of relevant math areas (math.AG, math.NT, math.CO, cs.LO…) → new papers become wiki entries with auto-extracted key theorems.
- **Conjecture tracker** — a dedicated note type with `status: open|proven|disproven|known` that turns your open problems list into a queryable inventory.
- **Session knowledge capture** — a PostToolUse/session-end hook extracts insights, failed approaches, and new conjectures from each Claude session into the wiki automatically.

## Details

### Baseline: What Yaro2709's Architecture Already Gets Right

The Yaro-style MathWiki uses atomic notes (one claim per file), typed callouts (`[!definition]`, `[!theorem]`, `[!proof]`), and the `Использует:` field to encode prerequisite dependencies as `[[wiki links]]`. This is an excellent substrate. The graph view in Obsidian already surfaces the dependency structure of mathematics in a way no textbook can.

**What's missing** is the LLM automation layer: verification, automation, daily enrichment, and adversarial checks. The improvements below add that layer without changing the note structure.

---

### Improvement 1 — Typed Relation Graph (steal from OmegaWiki)

OmegaWiki uses 9 entity types and semantic edge labels (`builds_on`, `improves_on`, `challenges`, `same_problem_as`). For a math wiki, translate this to 7 edge types stored in frontmatter:

```yaml
uses: [[definition-metric-space]]          # prerequisite
generalizes: [[theorem-bolzano-weierstrass]]  # this is more general
special_case_of: [[theorem-compactness-general]]  # this is narrower
equivalent_to: [[definition-cauchy-sequence]]  # equivalent reformulation
proven_by: [[lemma-triangle-inequality]]      # proof step
open_problem: [[conjecture-riemann-hypothesis]] # related open question
contradicts: []                                 # for approaches that clash
```

This takes ~5 minutes to retrofit existing notes and pays off immediately in the Gap Detector (Improvement 2).

**Prompt: Add typed relations to an existing note**
```
I have a math wiki note about [THEOREM NAME]. Current frontmatter:
---
[paste existing frontmatter]
---
Current body: [paste body]

Existing entries in my wiki (slugs): [paste list of related slugs]

Task: Add 7 typed relation fields to the frontmatter using only slugs from
the existing entries list. Fields: uses, generalizes, special_case_of,
equivalent_to, proven_by, open_problem, contradicts.
Leave a field empty [] if you can't confidently assign a value.
Output: complete updated frontmatter only, no commentary.
```

---

### Improvement 2 — Gap Detector (steal from OmegaWiki + obs.py)

Every `[[link]]` to a note that doesn't exist is a gap — a mathematical concept you've referenced but not yet defined or proved. In a math wiki, these accumulate fast. Run this as a weekly hygiene pass:

```bash
python scripts/obs.py broken
```

Each broken link is a stub to create. Prioritise by in-degree: the concept referenced by the most existing notes is your highest-leverage next note to write.

**Prompt: Prioritise and scaffold stubs from broken links**
```
Here are the broken [[links]] in my math wiki (concepts referenced but not
yet defined):
[paste list from obs.py broken]

For each broken link:
1. Infer from context what type of note it should be (definition/theorem/axiom)
2. Assign a priority score 1-5 (5 = many existing notes depend on this)
3. Generate a stub note scaffold following this structure:

---
title: "..."
category: math
tags: [...]
type: definition|theorem|axiom
status: stub
uses: []
---

## [!definition] / ## [!theorem]
[1-sentence statement from what you can infer about this concept]

## Proof / Derivation
_stub_

Return: prioritised list then all stub files.
```

---

### Improvement 3 — Adversarial Proof Review (steal from OmegaWiki)

OmegaWiki routes a draft paper to a second model for cross-model adversarial review. For a math wiki, apply this to individual proof sketches: one Claude pass writes the proof, a second pass tries to break it.

**Prompt: Adversarial proof review**
```
I have a theorem and a proof sketch. Play devil's advocate: your job is to
find a logical gap, an unverified assumption, a missing lemma, or a
potential counterexample. Do NOT help fix it — only identify weaknesses.

Theorem: [paste theorem statement]

Proof sketch: [paste proof]

Known prerequisites I've verified: [list the [[uses]] links from this note]

Output format:
- VERDICT: [LIKELY CORRECT | HAS GAPS | FLAWED]
- ISSUES: bullet list of specific problems
- MISSING LEMMAS: what sub-results are assumed but not proven
- CANDIDATE COUNTEREXAMPLE: (if verdict is FLAWED) concrete case where the
  claim might fail
```

**Prompt: Lean 4 stub from proof sketch**
```
Convert this informal math proof sketch into a Lean 4 theorem stub with
`sorry` placeholders where the proof is non-trivial. Preserve the logical
structure. Add `-- TODO: needs [lemma name]` comments at each sorry.

Theorem name: [name]
Statement: [LaTeX statement]
Proof sketch: [informal proof]
```

---

### Improvement 4 — Daily arXiv Digest (steal from OmegaWiki)

OmegaWiki runs a GitHub Action at UTC 00:17 to fetch daily arXiv recommendations and compile them into wiki entries. Adapt this for your research areas:

**Script setup** — add to `scripts/fetch_arxiv.py`:
```python
MATH_AREAS = ["math.AG", "math.NT", "math.CO", "math.AT", "cs.LO"]
MAX_PAPERS = 10
```

**Prompt: Extract wiki entry from arXiv paper**
```
I have an arXiv paper abstract and metadata. Extract a wiki entry for my
math research knowledge base.

Paper metadata:
Title: [title]
Authors: [authors]
arXiv ID: [id]
Abstract: [abstract]

My existing wiki topics (for cross-linking): [paste tag list or slug list]

Output a wiki entry following this structure:
---
title: "..."
category: concepts|tools
tags: [3-5 tags]
type: paper-summary
date: [today]
sources:
  - https://arxiv.org/abs/[id]
---

## Summary
[2 sentences: what problem + what result]

## Key Theorems / Results
- [theorem 1 in plain language]
- [theorem 2]

## Methods
- [key technique used]

## Connections to My Wiki
- [[slug]] — [why this paper relates to this existing entry]

## Open Questions Raised
- [what the paper leaves open]
- [[mathwiki-smith-maps-research]] ([AntonIliashenko/MathWiki: Research Wiki for Smith Map Deformation Theory](../tools/mathwiki-smith-maps-research.md))
---
<!-- RU -->
[Russian translation following the same structure]
```

---

### Improvement 5 — Conjecture Tracker (steal from nvk/llm-wiki theses)

nvk/llm-wiki uses `wiki/theses/` entries with `verdict: proven|refuted|contested|open`. For a math wiki, this maps directly onto open problems and conjectures:

**New note type: conjecture**
```yaml
---
title: "Conjecture: [name]"
type: conjecture
status: open|proven|disproven|known  # known = answer known in literature
difficulty: research|graduate|olympiad
related_theorems: [[theorem-X]], [[theorem-Y]]
my_attempts: 1           # how many proof attempts recorded
last_attempt: 2026-05-18
---

## Statement
[precise mathematical statement]

## Evidence For
- [why it seems true]

## Evidence Against / Counterexample Attempts
- [attempt 1: approach, why it failed]

## Related Open Problems
- [connection to known open problems]
```

**Prompt: Generate a conjecture entry from failed proof attempt**
```
I tried to prove [THEOREM/CLAIM] and got stuck. Help me extract a
structured conjecture entry from this failed attempt.

What I was trying to prove: [statement]
Approach I tried: [proof attempt]
Where I got stuck: [sticking point]
What would need to be true for my approach to work: [missing lemma/condition]

Output: a complete conjecture wiki entry (see schema above), including:
- Is this actually an open problem or is the answer known?
- What weaker version IS provable?
- What stronger version is the actual research frontier?
```

---

### Improvement 6 — Session Knowledge Capture (steal from claude-memory-compiler)

The claude-memory-compiler project hooks into Claude Code's session end to extract decisions, insights, and lessons. For math research, this means: every session where you work with Claude on a proof or definition automatically produces a knowledge artifact.

**CLAUDE.md hook addition:**
```markdown
## Session End Protocol
After any math research session, run:
python scripts/capture_session.py --session "$(date +%Y-%m-%d)"

This extracts:
- Any new definitions or theorems discussed
- Failed proof approaches (annotated with WHY they fail)
- New conjectures raised
- Cross-links to existing wiki notes discovered
```

**Prompt: Session debrief extraction**
```
We just finished a math research session. Extract structured knowledge
from our conversation.

Session transcript summary: [paste or describe what was discussed]

Extract into these categories:

NEW KNOWLEDGE (create as wiki stubs):
- Definitions formulated: [name, statement]
- Theorems proven or sketched: [name, statement, confidence]
- Useful lemmas: [name, statement]

FAILED APPROACHES (add to relevant conjecture entries):
- Approach: [description] — Why it failed: [reason]

NEW OPEN QUESTIONS (create as conjecture stubs):
- [question]

CROSS-LINKS DISCOVERED:
- [[existing-slug]] connects to [[existing-slug]] because [reason]

Output: structured JSON following the above schema, ready to file.
```

---

## Quick-Win Priority Order

| # | Improvement | Effort | Impact | Do first? |
|---|---|---|---|---|
| 1 | Run `obs.py broken` and create stubs | 15 min | High | **Yes** |
| 2 | Add typed relation fields to 10 highest-linked notes | 1 hr | High | **Yes** |
| 3 | Adversarial proof review prompt (paste into any session) | 0 | High | **Yes** |
| 4 | Conjecture tracker for open problems | 2 hr | Medium | Soon |
| 5 | Session debrief protocol (add to CLAUDE.md) | 30 min | Medium | Soon |
| 6 | Daily arXiv digest (requires fetch_arxiv.py) | 4 hr | High (ongoing) | Next sprint |

The first three cost nothing beyond copying a prompt. Start there.

## Related Entries

- [[omegawiki-research-platform]] ([OmegaWiki: Wiki-Centric AI Research Platform](./omegawiki-research-platform.md))
- [[yaro-mathwiki]] ([Yaro2709/MathWiki: Hand-Crafted Math Knowledge Base](./yaro-mathwiki.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](./llm-wiki-ecosystem.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[self-guided-self-play]] ([Self-Guided Self-Play for LLMs: SGS Algorithm](../concepts/self-guided-self-play.md))
- [[llm-git-knowledge-accumulation]] ([LLM Project Memory via Git: Plan-Execute-Distill Loop](../tips/llm-git-knowledge-accumulation.md))

---
<!-- RU -->

## Краткое описание

Конкретный план действий для повышения эффективности персональной математической вики за счёт шести идей из OmegaWiki и экосистемы LLM Wiki. Каждое улучшение объяснено, отранжировано по влиянию и снабжено готовым промптом для Claude Code.

## Ключевые идеи

- **Типизированный граф связей** — замените единственное поле `Использует:` на 7 типов семантических рёбер. Открывает детектор пробелов, поиск обобщений и состязательную рецензию доказательств.
- **Детектор пробелов** — сканирует хранилище на `[[ссылки]]` на несуществующие заметки; это заготовки для написания, а не ошибки.
- **Состязательная рецензия доказательств** — вторая модель (или второй проход Claude) ищет контрпример или логическую брешь в вашем набросках доказательства.
- **Ежедневный дайджест arXiv** — утреннее сканирование разделов математики → новые статьи становятся записями вики с автоматически извлечёнными теоремами.
- **Трекер гипотез** — отдельный тип заметок с полем `status: open|proven|disproven|known`, превращающий список открытых задач в запрашиваемый инвентарь.
- **Захват знаний сессии** — хук PostToolUse извлекает инсайты, неудачные подходы и новые гипотезы из каждой сессии Claude в вики автоматически.

## Подробнее

### Базовый уровень: что архитектура Yaro уже делает правильно

Стиль MathWiki по Yaro использует атомарные заметки (одно утверждение на файл), типизированные callouts (`[!definition]`, `[!theorem]`, `[!proof]`) и поле `Использует:` для кодирования предпосылочных зависимостей через `[[wiki-ссылки]]`. Это отличный фундамент. Граф Obsidian уже раскрывает структуру зависимостей математики так, как ни один учебник не способен.

**Чего не хватает** — слой LLM-автоматизации: верификация, обогащение, ежедневное пополнение и состязательные проверки. Описанные ниже улучшения добавляют этот слой, не изменяя структуру заметок.

---

### Улучшение 1 — Типизированный граф связей (из OmegaWiki)

Замените `Использует:` на 7 полей в YAML frontmatter:

```yaml
uses: [[определение-метрическое-пространство]]
generalizes: [[теорема-больцано-вейерштрасс]]
special_case_of: [[теорема-компактность-общая]]
equivalent_to: [[определение-последовательность-коши]]
proven_by: [[лемма-неравенство-треугольника]]
open_problem: [[гипотеза-римана]]
contradicts: []
```

**Промпт: добавить типизированные связи к существующей заметке**
```
У меня есть заметка о [НАЗВАНИЕ ТЕОРЕМЫ]. Существующий frontmatter:
---
[вставить frontmatter]
---
Тело заметки: [вставить тело]

Существующие записи в вики (слаги): [вставить список]

Задача: добавить 7 полей типизированных связей в frontmatter, используя
только слаги из списка существующих записей. Поля: uses, generalizes,
special_case_of, equivalent_to, proven_by, open_problem, contradicts.
Оставьте поле пустым [], если не можете уверенно назначить значение.
Вывод: только обновлённый frontmatter, без комментариев.
```

---

### Улучшение 2 — Детектор пробелов (из OmegaWiki + obs.py)

Каждая `[[ссылка]]` на несуществующую заметку — это пробел: математический концепт, на который вы сослались, но ещё не определили или не доказали.

```bash
python scripts/obs.py broken
```

Каждая сломанная ссылка — заготовка для создания. Приоритизируйте по входящей степени: концепт, на который ссылается больше всего существующих заметок — следующий высокоприоритетный кандидат для написания.

**Промпт: приоритизация и создание заготовок из сломанных ссылок**
```
Вот сломанные [[ссылки]] в моей математической вики:
[вставить список из obs.py broken]

Для каждой сломанной ссылки:
1. Выведите из контекста, какой тип заметки это должен быть (definition/theorem/axiom)
2. Назначьте приоритет 1-5 (5 = на это зависит много заметок)
3. Создайте заготовку заметки по структуре:

---
title: "..."
type: definition|theorem|axiom
status: stub
uses: []
---

## [!definition] / ## [!theorem]
[1 предложение — утверждение исходя из контекста]

## Доказательство / Вывод
_stub_
```

---

### Улучшение 3 — Состязательная рецензия доказательства (из OmegaWiki)

OmegaWiki направляет черновик статьи второй модели на состязательную рецензию. Для математической вики применяйте это к наброскам доказательств.

**Промпт: состязательная рецензия доказательства**
```
У меня есть теорема и набросок доказательства. Сыграйте роль критика:
ваша задача — найти логическую брешь, непроверенное допущение, отсутствующую
лемму или потенциальный контрпример. НЕ помогайте исправить — только
выявляйте слабости.

Теорема: [вставить]
Набросок доказательства: [вставить]
Известные предпосылки (проверенные): [список uses-ссылок]

Формат вывода:
- ВЕРДИКТ: [ВЕРОЯТНО ВЕРНО | ЕСТЬ ПРОБЕЛЫ | ОШИБОЧНО]
- ПРОБЛЕМЫ: список конкретных вопросов
- ОТСУТСТВУЮЩИЕ ЛЕММЫ: что предполагается, но не доказано
- КАНДИДАТ НА КОНТРПРИМЕР: (если ОШИБОЧНО) конкретный случай
```

**Промпт: заготовка Lean 4 из наброска**
```
Преобразуйте этот неформальный набросок доказательства в заготовку теоремы
Lean 4 с плейсхолдерами `sorry`. Добавьте комментарии
`-- TODO: нужна [название леммы]` в каждом sorry.

Теорема: [название и LaTeX-утверждение]
Набросок: [неформальное доказательство]
```

---

### Улучшение 4 — Ежедневный дайджест arXiv (из OmegaWiki)

OmegaWiki запускает GitHub Action для ежедневного получения рекомендаций arXiv. Настройте для ваших областей: `math.AG`, `math.NT`, `math.CO`, `math.AT`, `cs.LO`.

**Промпт: извлечение записи вики из статьи arXiv**
```
У меня есть аннотация и метаданные статьи arXiv. Создайте запись вики
для моей математической базы знаний.

Метаданные: Title, Authors, arXiv ID, Abstract.
Существующие темы вики для перекрёстных ссылок: [список тегов или слагов]

Структура вывода:
---
title: "..."
category: concepts
type: paper-summary
date: [сегодня]
sources:
  - https://arxiv.org/abs/[id]
---

## Краткое описание [Summary]
[2 предложения: задача + результат]

## Ключевые теоремы / результаты
## Методы
## Связи с моей вики
- [[slug]] — [почему статья связана с этой записью]
## Открытые вопросы
```

---

### Улучшение 5 — Трекер гипотез (из nvk/llm-wiki)

Выделенный тип заметок для открытых задач и гипотез:

```yaml
---
title: "Гипотеза: [название]"
type: conjecture
status: open|proven|disproven|known
difficulty: research|graduate|olympiad
related_theorems: [[theorem-X]]
my_attempts: 1
last_attempt: 2026-05-18
---
```

**Промпт: создать запись гипотезы из неудачной попытки**
```
Я пытался доказать [УТВЕРЖДЕНИЕ] и застрял. Помогите извлечь структурированную
запись гипотезы из этой неудачной попытки.

Что я пытался доказать: [утверждение]
Подход: [попытка доказательства]
Где застрял: [место]
Что нужно было бы для работы подхода: [отсутствующая лемма/условие]

Вывод: полная запись гипотезы, включая:
- Это реально открытая задача или ответ известен?
- Какую более слабую версию МОЖНО доказать?
- Какая более сильная версия — реальный исследовательский фронтир?
```

---

### Улучшение 6 — Захват знаний сессии (из claude-memory-compiler)

Добавьте в CLAUDE.md протокол завершения сессии, автоматически извлекающий знания:

**Промпт: дебриф сессии**
```
Мы только что завершили математическую исследовательскую сессию. Извлеките
структурированные знания из нашего разговора.

Краткое содержание сессии: [описание]

Категории для извлечения:

НОВЫЕ ЗНАНИЯ (создать как заготовки):
- Сформулированные определения: [название, утверждение]
- Доказанные или обрисованные теоремы: [название, доверие]
- Полезные леммы: [название, утверждение]

НЕУДАЧНЫЕ ПОДХОДЫ (добавить в записи гипотез):
- Подход: [описание] — Почему не сработал: [причина]

НОВЫЕ ОТКРЫТЫЕ ВОПРОСЫ:
- [вопрос]

ОБНАРУЖЕННЫЕ ПЕРЕКРЁСТНЫЕ СВЯЗИ:
- [[существующий-слаг]] связан с [[существующий-слаг]] потому что [причина]

Вывод: структурированный JSON, готовый для подачи.
```

---

## Приоритет быстрых побед

| # | Улучшение | Усилие | Влияние | Сделать первым? |
|---|---|---|---|---|
| 1 | `obs.py broken` + создать заготовки | 15 мин | Высокое | **Да** |
| 2 | Типизированные связи для 10 самых ссылаемых заметок | 1 час | Высокое | **Да** |
| 3 | Состязательная рецензия (промпт в любую сессию) | 0 | Высокое | **Да** |
| 4 | Трекер гипотез для открытых задач | 2 часа | Среднее | Скоро |
| 5 | Протокол дебрифа сессии (добавить в CLAUDE.md) | 30 мин | Среднее | Скоро |
| 6 | Ежедневный дайджест arXiv (требует fetch_arxiv.py) | 4 часа | Высокое (регулярно) | Следующий спринт |

## Связанные записи

- [[omegawiki-research-platform]] ([OmegaWiki: Wiki-Centric AI Research Platform](./omegawiki-research-platform.md))
- [[yaro-mathwiki]] ([Yaro2709/MathWiki: Hand-Crafted Math Knowledge Base](./yaro-mathwiki.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](./llm-wiki-ecosystem.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[self-guided-self-play]] ([Self-Guided Self-Play for LLMs: SGS Algorithm](../concepts/self-guided-self-play.md))
- [[llm-git-knowledge-accumulation]] ([LLM Project Memory via Git: Plan-Execute-Distill Loop](../tips/llm-git-knowledge-accumulation.md))
- [[mathwiki-smith-maps-research]] ([AntonIliashenko/MathWiki: Research Wiki for Smith Map Deformation Theory](../tools/mathwiki-smith-maps-research.md))
