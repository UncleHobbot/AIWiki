Run the wiki quality test suite and auto-fix all failures, iterating up to 5 rounds until the suite is green.

## Overview

This command is a self-healing loop:
1. Run `pytest tests/test_wiki.py -v --tb=short` and capture the output.
2. Parse failures into fix categories.
3. Apply targeted fixes for each category.
4. Re-run pytest.
5. Repeat up to **5 rounds** total.  Stop early if the suite passes.

---

## Step 1 — Run the test suite

```
pytest tests/test_wiki.py -v --tb=short
```

Capture full stdout + stderr. Parse each FAILED line:

```
FAILED tests/test_wiki.py::test_frontmatter_valid[<slug>]
FAILED tests/test_wiki.py::test_has_ru_section[<slug>]
FAILED tests/test_wiki.py::test_wikilinks_resolve[<slug>]
FAILED tests/test_wiki.py::test_index_contains_all_entries
FAILED tests/test_wiki.py::test_index_has_no_ghost_entries
FAILED tests/test_wiki.py::test_no_orphan_pages
```

Group failures by test name. Extract the `<slug>` from parametrised tests.
If zero failures: print "✓ All wiki quality checks passed." and stop.

---

## Step 2 — Apply fixes (order matters — do index last)

Process each failure category below. Within each category, handle all affected
slugs before moving on.

### A. `test_frontmatter_valid[<slug>]`

For each failing slug (`wiki/**/<slug>.md`):

1. Read the file.
2. Parse existing frontmatter (it may be partially present).
3. Fill each missing required field with a sensible value:
   - `title_ru` — translate `title` to natural Russian.
   - `tags` — infer 3-5 tags from the entry content; use lowercase, hyphens.
   - `updated` — set to today's date (YYYY-MM-DD).
   - `sources` — if empty, add `[]` (empty list is invalid — add at least a
     placeholder `- https://example.com  # FIXME: add real source`).
   - `category` — if missing or invalid, infer from content using the
     category decision tree in CLAUDE.md; valid values are:
     concepts | tools | agents | models | news | tips | people
4. Write the corrected frontmatter back.  Do NOT touch the entry body.

### B. `test_has_ru_section[<slug>]`

For each failing slug:

1. Read the file.
2. Check if the `---\n<!-- RU -->` divider is present:
   - **Divider missing:** generate a complete Russian section and append it
     after the last line of the English content:
     ```
     
     ---
     <!-- RU -->
     
     ## Краткое описание
     ...
     ```
   - **Divider present but Russian body < 100 chars or has no Cyrillic headings:**
     remove the old Russian section and regenerate it from scratch.
3. Russian section rules (from CLAUDE.md):
   - Natural Russian, not machine-literal.
   - Keep untranslated: token, prompt, fine-tuning, RAG, agent, pipeline,
     MCP, CLI, SDK, API, LLM, and all code blocks / file paths.
   - Translate headings; keep front-matter keys in English.
   - `## Related Entries` links are identical in both sections.
   - Required headings: Краткое описание, Ключевые идеи, Подробнее,
     and Связанные записи (if the English section has Related Entries).

### C. `test_wikilinks_resolve[<slug>]`

For each failing slug:

1. Read the file.
2. Run `python scripts/obs.py links <slug>` to see which links are marked
   [BROKEN].
3. For each broken `[[target-slug]]`:
   - Check `index.md` — if the topic exists under a different slug, replace
     `[[broken-slug]]` with the correct `[[real-slug]]`.
   - Otherwise, remove the `[[broken-slug]]` from Related Entries in both
     the English and Russian sections.  Do NOT delete wikilinks found in
     body prose — rewrite them as plain text instead.
4. Write the cleaned file.

### D. `test_index_contains_all_entries` or `test_index_has_no_ghost_entries`

Run `/wiki-index` (i.e., follow the instructions in
`.claude/commands/wiki-index.md`) to fully rebuild `index.md`.
This resolves both missing entries and ghost entries in one pass.

### E. `test_no_orphan_pages`

For each orphan slug reported in the failure message:

1. Identify the entry's `category` and `tags` from its frontmatter.
2. Find the 2-3 existing entries most semantically related (same category,
   overlapping tags, or similar title keywords).
3. For each chosen related entry:
   - Append `- [[orphan-slug]]` to the `## Related Entries` section in
     both the English and Russian sections.
4. Also ensure the orphan itself has `## Related Entries` in both sections.

---

## Step 3 — Re-run and iterate

After completing all fixes for this round:

```
pytest tests/test_wiki.py -v --tb=short
```

- If all pass: print summary and stop.
- If failures remain and round < 5: go back to Step 2 with only the
  still-failing tests.
- If round == 5 and failures remain: print a final summary of unfixed
  failures and note that manual intervention is needed.

---

## Step 4 — Final report

Print a summary in this format:

```
wiki-fix complete — X rounds, Y fixes applied.

Fixed:
  frontmatter  N entries
  ru_section   N entries
  wikilinks    N entries
  index        rebuilt once
  orphans      N entries linked

Remaining failures (manual fix needed):
  <list any still-failing test IDs, or "none">
```

Do NOT update `log.md` or `.state/last_run.json` — those are for ingestion
runs, not quality fixes.
