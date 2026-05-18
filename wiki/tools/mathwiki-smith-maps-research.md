---
title: "AntonIliashenko/MathWiki: Research Wiki for Smith Map Deformation Theory"
title_ru: "AntonIliashenko/MathWiki: исследовательская вики по теории деформаций Smith-отображений"
category: tools
tags: [mathwiki, differential-geometry, smith-maps, calibrated-geometry, obsidian, llm-wiki, opencode, research-tool, knowledge-base]
aliases: [AntonIliashenko MathWiki, Smith map wiki, calibrated geometry wiki]
confidence: high
updated: 2026-05-18
sources:
  - https://github.com/AntonIliashenko/MathWiki
---

## Summary

AntonIliashenko/MathWiki is a citation-first, LLM-maintained research wiki for differential geometry, maintained by Anton Iliashenko (co-author of the 2026 Smith map deformation theory preprint). The central programme is building a deformation theory for Smith maps — calibrated, weakly conformal maps — analogous to the McDuff–Salamon theory of J-holomorphic curves. The wiki is an active reasoning environment, not a static reference: it tracks open problems, records proof corrections, and runs computational experiments via Python scripts.

## Key Ideas

- **Research tool, not textbook.** The wiki is a live scaffold for ongoing original mathematics research — 17 paper summaries, 17 concept pages, 4 answer pages resolving proof errors, 1 active research question — all cross-linked and maintained by opencode skills.
- **Sources as ground truth.** The `sources/` directory holds raw PDFs and extracted text. Wiki pages synthesize; they never overwrite. If a source conflicts with an existing page, the conflict is recorded explicitly in `wiki/contradictions/` rather than silently resolved.
- **Active research programme.** The central question: can one develop a deformation theory for Smith maps ($k > 2$) using the spinorial reformulation to avoid the triviality obstruction ($D_u \equiv 0$ for naive linearisation), and construct smooth moduli spaces and enumerative invariants in calibrated geometry?
- **Proof error tracking.** The `wiki/answers/` section records and corrects mathematical errors discovered during research — including a covering-map error in Proposition 2.9, a chain-rule gap in Theorem 4.2, and an incorrect application of Spencer cohomology.
- **70+ opencode skills.** The wiki is maintained with opencode and a library of domain-specific skills: `math-reasoning`, `academic-deep-research`, `academic-paper`, `academic-paper-reviewer`, `literature-search`, `latex-document`, `novelty-assessment`, `grill-me`, and more.
- **Computational experimentation.** Root-level Python scripts (`find_smith_maps.py`, `verify_smith.py`, `prove_smith.py`) run computational searches for Smith map examples and verify algebraic conditions — connecting the symbolic wiki to numerical evidence.

## Repository Structure

```
sources/          6 papers + 1 book as PDFs and extracted .txt
wiki/
  concepts/       17 pages (Smith Map, Calibration, G₂ Structure, Tractor Calculus, …)
  papers/         17 pages (incl. 3 author's own preprints, McDuff–Salamon, Gover–Peterson, …)
  methods/        3 pages (Moser Iteration, Ambient Metric Construction, Nash-Moser IFT)
  reviews/        1 page (Conformal invariants and geometric PDE)
  answers/        4 pages (proof corrections and resolved ambiguities)
  research-questions/  1 active question (Smith map deformation theory)
  contradictions/ (empty — no inter-source conflicts detected yet)
  _index.md       Top-level navigable index
output/           Exported PDFs and LaTeX files
logs/             Ingestion and maintenance logs
find_smith*.py    Computational search scripts
verify_smith.py   Algebraic verification
prove_smith.py    Proof assistant scripting
AGENTS.md         Wiki rules and conventions
Skills.md         70+ opencode skill catalogue with invocation examples
```

## The Central Research Problem

The core of the wiki's research programme:

**J-holomorphic curves** ($k = 2$, symplectic calibration $\alpha = \omega$) have a well-understood deformation theory: linearisation is Fredholm, transversality is achievable via generic $J$, and moduli spaces are smooth manifolds of the expected dimension. This underpins Gromov–Witten theory, quantum cohomology, and Floer homology.

**Smith maps** generalise J-holomorphic curves to higher dimensions: a smooth map $u: (L^k, g) \to (M^n, h)$ is a Smith map if $u^*\alpha = \lambda^k \mathrm{vol}_L$ (calibrated) and $(u^*h)_0 = 0$ (weakly conformal). Special cases include associative/coassociative immersions (G₂), Cayley immersions (Spin(7)), and special Lagrangian immersions.

**The obstruction.** For $k > 2$, the naive linearisation of the Smith equation is identically zero ($D_u \equiv 0$). This is a fundamental analytic obstruction absent in the J-holomorphic case. It stems from the general inequality $u^*\alpha \leq \lambda^k \mathrm{vol}_L$: the Smith equation is the equality case (a maximum), so the first variation vanishes.

**The resolution (spinorial calibrations).** For calibrations arising from a spinor — as in G₂ and Spin(7) — the spinorial decomposition $\theta \cdot s = \alpha_k(\theta)s + \eta(\theta) \cdot s$ allows reformulating the Smith equation as $\eta(\theta) = 0$, which avoids the inequality obstruction. For associative Smith maps (G₂), the *weak Smith equation* $\tilde{F} = C \circ F$ achieves ellipticity, has index 0, and admits transversality. Moduli spaces are smooth manifolds of dimension $\dim(\mathfrak{g})$ (the conformal Killing algebra of $L$) — *Deformation theory of (spinorial) Smith maps* (Iliashenko, 2026).

**Key open problem.** Cayley Smith maps (Spin(7)) and a unified enumerative theory remain open.

## Architectural Decisions Worth Borrowing

**1. Answer pages as first-class wiki entries.**
When a proof error is discovered (in the author's own papers or in the literature), a dedicated `wiki/answers/` page records: the error, a counterexample, and the corrected argument. This is the wiki-native equivalent of a mathematical errata file. Examples in this repo:
- `fixing-proposition-2-9-covering-map-error.md` — the covering map argument fails because $u(L)$ with subspace topology is not generally a manifold. Corrected conclusion: *density* of injective points, not global injectivity.
- `fixing-theorem-4-2-chain-rule.md` — chain rule gap in the k-Laplacian formula in *Hyperbolicity II*.

**2. Contradictions directory.**
`wiki/contradictions/` is an explicit home for inter-source conflicts. Currently empty — but its existence as a named directory enforces the discipline of tracking conflicts rather than silently overriding them when they appear.

**3. Confidence levels on every page.**
Every wiki page carries `confidence: high|medium|low` in frontmatter. `low` means "tentative, incomplete, or weakly supported" — a signal to the maintainer and any LLM reader that this page needs more evidence before it can be relied upon.

**4. Skills.md as living skill catalogue.**
Rather than relying on implicit skill activation, the repo ships a `Skills.md` with all 70+ opencode skills documented in a table: skill name, purpose, invocation trigger, and example prompts drawn from the actual research workflow. This makes the AI tooling layer as explicit and version-controlled as the mathematical content.

**5. Python scripts for computational verification.**
Five root-level Python scripts (`find_smith_maps.py`, `find_smith_maps_fast.py`, `find_assoc.py`, `verify_smith.py`, `prove_smith.py`) bridge the symbolic wiki to computational experiments. This is unusual in a research wiki and reflects a commitment to grounding abstract theory in concrete examples.

## Coverage: Key Papers and Concepts

**Author's own preprints (in wiki):**
- *k-harmonic maps inducing calibrated fibrations* (Iliashenko–Karigiannis, 2023) — introduces Smith immersion and submersion maps
- *Deformation theory of (spinorial) Smith maps* (Iliashenko, 2026) — full deformation theory for associative Smith maps
- *Hyperbolicity and Schwarz lemmas in calibrated geometry* (Broder–Iliashenko–Madnick, 2026)
- *Hyperbolicity in calibrated geometry II* (Cheng–Iliashenko–Karigiannis–Madnick, 2026)

**Reference literature:**
- McDuff–Salamon: *J-holomorphic curves and symplectic topology* (2nd ed., 2012) — the analogue whose programme is being extended
- Gover–Peterson: conformal invariants and GJMS operators (2002, 2004) — ambient metric construction
- Donaldson–Segal: gauge theory in higher dimensions (2009) — G₂ instantons and associative submanifolds
- Wang–Zhang: gradient estimates for p-harmonic functions (2010)
- Parker: deformations of Z₂-harmonic spinors (2023)

**Concepts documented:** Smith Map, Calibration, Conformal Geometry, Conformal Map, G₂ Structure, Pseudo-holomorphic Map, p-Harmonic Functions, Z₂-Harmonic Spinors, Quasiregular Curves, Quasi-Conformal Convolution, Ambient Metric, Gradient Estimates, Elliptic Edge Operator, Tractor Calculus, Q-Curvature, GJMS Operators, Obstruction Tensor.

## Comparison to Yaro2709/MathWiki

| Dimension | AntonIliashenko/MathWiki | Yaro2709/MathWiki |
|---|---|---|
| Purpose | Active original research | Mathematics education (undergraduate) |
| Domain | Differential geometry (single focused area) | General pure math (set theory, algebra, analysis, topology) |
| Scale | 17 papers, 17 concepts, 4 answers | 820 files, 430 definitions, 171 theorems |
| Authorship | LLM-maintained (opencode) | Entirely hand-crafted, no LLM |
| Note type | Papers + concepts + answers + methods | Atomic statements (one claim per file) |
| Source model | Raw PDFs as ground truth → wiki synthesis | No source layer; notes are primary |
| Error tracking | Explicit `answers/` + `contradictions/` dirs | None |
| Computation | Python verification scripts | None |
| Language | English | Russian only |

Both are Obsidian vaults using `[[wikilinks]]` for cross-linking, but they represent fundamentally different use cases: production research tool vs. structured self-study reference.

## Related Entries

- [[yaro-mathwiki]] ([Yaro2709/MathWiki: Hand-Crafted Math Knowledge Base](./yaro-mathwiki.md))
- [[mathwiki-llm-research-automation]] ([LLM-Powered Math Research: Ideas to Steal for Your MathWiki](../tips/mathwiki-llm-research-automation.md))
- [[omegawiki-research-platform]] ([OmegaWiki: Wiki-Centric AI Research Platform](./omegawiki-research-platform.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[self-guided-self-play]] ([Self-Guided Self-Play for LLMs: SGS Algorithm](../concepts/self-guided-self-play.md))

---
<!-- RU -->

## Краткое описание

AntonIliashenko/MathWiki — это citation-first исследовательская вики по дифференциальной геометрии, поддерживаемая с помощью opencode. Автор — Антон Ильяшенко, соавтор препринта 2026 года по теории деформаций Smith-отображений. Центральная программа: построение теории деформаций для Smith-отображений — калиброванных, слабо конформных отображений — по аналогии с теорией Макдаффа–Саламона для J-голоморфных кривых.

## Ключевые идеи

- **Инструмент исследования, не учебник.** Вики — живой каркас для активных оригинальных математических исследований: 17 обзоров статей, 17 концептуальных страниц, 4 страницы с исправлениями ошибок в доказательствах, 1 активный исследовательский вопрос.
- **Источники как точка истины.** Директория `sources/` содержит исходные PDF и извлечённый текст. Страницы вики синтезируют; они никогда не перезаписывают источники. Конфликты записываются явно в `wiki/contradictions/`.
- **Активная исследовательская программа.** Центральный вопрос: можно ли построить теорию деформаций для Smith-отображений при $k > 2$, используя спинорную переформулировку, чтобы обойти тривиальность линеаризации?
- **Трекинг ошибок в доказательствах.** Раздел `wiki/answers/` фиксирует и исправляет математические ошибки — включая ошибку с накрывающим отображением в Предложении 2.9 и пропуск в формуле правила цепочки в Теореме 4.2.
- **70+ навыков opencode.** Математические рассуждения (`math-reasoning`), глубокий обзор литературы (`academic-deep-research`), рецензирование (`academic-paper-reviewer`), оценка новизны (`novelty-assessment`), LaTeX-компиляция (`latex-document`) и многое другое.
- **Вычислительные эксперименты.** Python-скрипты в корне репозитория (`find_smith_maps.py`, `verify_smith.py`, `prove_smith.py`) связывают символическую вики с численными свидетельствами.

## Структура репозитория

```
sources/        6 статей + 1 книга в PDF и .txt
wiki/
  concepts/     17 страниц (Smith Map, Calibration, G₂ Structure, …)
  papers/       17 страниц (включая 3 собственных препринта автора)
  methods/      3 страницы (итерация Мозера, конструкция ambient-метрики, теорема Нэша-Мозера)
  reviews/      1 страница (конформные инварианты и геометрические PDE)
  answers/      4 страницы (исправления ошибок в доказательствах)
  research-questions/  1 активный вопрос
  contradictions/      (пусто — конфликтов между источниками не обнаружено)
output/         Экспортированные PDF и LaTeX
find_smith*.py  Вычислительный поиск
verify_smith.py Алгебраическая верификация
AGENTS.md       Правила и конвенции вики
Skills.md       Каталог 70+ навыков opencode с примерами промптов
```

## Центральная исследовательская проблема

**J-голоморфные кривые** ($k = 2$) имеют хорошо понятую теорию деформаций: линеаризация фредгольмова, трансверсальность достигается через общее $J$, пространства модулей — гладкие многообразия. Это фундамент теории Громова–Виттена, квантовой когомологии и гомологий Флоэра.

**Smith-отображения** обобщают J-голоморфные кривые на высшие размерности: $u^*\alpha = \lambda^k \mathrm{vol}_L$ (калиброванность) и $(u^*h)_0 = 0$ (слабая конформность). Частные случаи: ассоциативные/коассоциативные погружения (G₂), Cayley-погружения (Spin(7)), специальные лагранжевы погружения.

**Препятствие.** Для $k > 2$ наивная линеаризация уравнения Smith тождественно равна нулю ($D_u \equiv 0$). Это фундаментальное аналитическое препятствие, отсутствующее в случае J-голоморфных кривых.

**Решение (спинорные калибровки).** Для G₂ и Spin(7) спинорное разложение $\theta \cdot s = \alpha_k(\theta)s + \eta(\theta) \cdot s$ позволяет переформулировать уравнение Smith как $\eta(\theta) = 0$, обходя препятствие. Для ассоциативных Smith-отображений *слабое уравнение Smith* $\tilde{F} = C \circ F$ достигает эллиптичности и трансверсальности; пространства модулей — гладкие многообразия размерности $\dim(\mathfrak{g})$.

## Архитектурные решения, достойные заимствования

**1. Страницы ответов как записи первого класса.** При обнаружении ошибки в доказательстве создаётся отдельная страница `wiki/answers/` с: описанием ошибки, контрпримером и исправленным аргументом.

**2. Директория противоречий.** `wiki/contradictions/` — явное место для межисточниковых конфликтов. Пустая сейчас, но её существование дисциплинирует трекинг конфликтов.

**3. Уровни достоверности на каждой странице.** `confidence: high|medium|low` в frontmatter — сигнал поддерживающему и любому LLM-читателю о надёжности содержимого.

**4. Skills.md как версионированный каталог навыков.** 70+ навыков opencode задокументированы в таблице: цель, триггер активации, примеры промптов из реального исследовательского процесса.

**5. Python-скрипты для вычислительной верификации.** Пять скриптов связывают символическую вики с вычислительными экспериментами.

## Сравнение с Yaro2709/MathWiki

| Измерение | AntonIliashenko/MathWiki | Yaro2709/MathWiki |
|---|---|---|
| Цель | Активные оригинальные исследования | Математическое образование (вуз) |
| Область | Дифференциальная геометрия (узкий фокус) | Общая чистая математика |
| Масштаб | 17 статей, 17 концептов, 4 ответа | 820 файлов, 430 определений, 171 теорема |
| Поддержка | LLM (opencode) | Полностью вручную |
| Тип заметок | Статьи + концепты + ответы + методы | Атомарные утверждения |
| Язык | Английский | Только русский |

Оба — хранилища Obsidian с `[[wiki-ссылками]]`, но для принципиально разных задач: производственный исследовательский инструмент vs. структурированный самоучитель.

## Связанные записи

- [[yaro-mathwiki]] ([Yaro2709/MathWiki: рукотворная база математических знаний](./yaro-mathwiki.md))
- [[mathwiki-llm-research-automation]] ([LLM-инструменты для математических исследований](../tips/mathwiki-llm-research-automation.md))
- [[omegawiki-research-platform]] ([OmegaWiki: вики-центрированная платформа для научных исследований](./omegawiki-research-platform.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki для научных исследований и академического письма](../tips/llm-wiki-scientific-research.md))
- [[self-guided-self-play]] ([Самонаправленная самоигра для LLM: алгоритм SGS](../concepts/self-guided-self-play.md))
