Run the full wiki maintenance pipeline in canonical order.

Loads and executes the wiki-pipeline skill at .claude/skills/wiki-pipeline/SKILL.md.

Steps (in order):
1. wiki-reddit  — scan 14 subreddits, queue discovered URLs to inbox/links.md
2. wiki-inbox   — process all inbox sources (clippings, links, tweets, posts, youtube)
3. wiki-links   — second pass to drain any URLs queued by Step 1
4. wiki-check   — audit Russian sections + run obs.py broken/orphans health check
5. wiki-index   — rebuild index.md with orphan markers from obs.py
6. wiki-digest  — generate bilingual digest (only if Monday or current week missing)
7. git commit + push — structured commit message with per-step counts

See .claude/skills/wiki-pipeline/SKILL.md for full input specifications,
success criteria, and error-handling rules for each step.

Print a one-line status after each step and a full summary table at the end.
