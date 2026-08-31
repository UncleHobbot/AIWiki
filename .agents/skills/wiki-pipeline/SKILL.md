# Wiki Pipeline Skill

Run the full LLM Wiki maintenance workflow in canonical order. Each step is
self-contained; if a step produces zero new output that is not an error.
Always use UTF-8 encoding in any Python invocations. Never use /tmp/ paths.

---

## When to invoke this skill

- Triggered by `/wiki-pipeline` in the TUI, or by headless `Codex --print`
- Runs unattended: recover from transient failures silently, log, and continue
- If run interactively, print a one-line status after each step

---

## Step 1 — Scan Reddit (`/wiki-reddit`)

**What it does:** Fetches new posts from all 14 monitored subreddits using
stored cursors, creates bilingual wiki entries for qualifying posts, and queues
any discovered external URLs into `inbox/links.md ## To Read`.

**Inputs required:**
- `.state/reddit_cursor.json` — per-subreddit last-seen post IDs (auto-created if missing)
- `.env` — optional `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET` for OAuth; public API works without them

**Run:**
```
python scripts/fetch_reddit.py <subreddit> --use-cursor --with-comments --min-score 50
```
Run for all 16 subreddits: r/GithubCopilot, r/opencodeCLI, r/opencode,
r/ClaudeCode, r/ZaiGLM, r/kimi, r/AI_Agents, r/LocalLLaMA, r/MachineLearning,
r/singularity, r/ChatGPT, r/ChatGPTCoding, r/ollama, r/vibecoding, r/DeepSeek, r/Qwen_AI

**Success criteria:**
- `.state/reddit_cursor.json` updated with new post IDs for each subreddit
- Any qualifying posts created as `wiki/<category>/<slug>.md` with EN + RU sections
- External URLs from posts appended to `inbox/links.md` under `## To Read`
- `.state/last_run.json` updated with a run summary entry

**Failure handling:** If a subreddit fetch returns a network error or rate-limit,
log it and continue to the next subreddit. Do not abort the pipeline.

---

## Step 2 — Process Inbox (`/wiki-inbox`)

**What it does:** Runs all inbox sub-workflows in sequence:
clippings → links → tweets → posts → youtube → rebuild index → log run.

**Inputs required:**
- `inbox/clippings/` — Obsidian Web Clipper `.md` exports (may be empty)
- `inbox/links.md` — URLs under `## To Read` (may already have URLs from Step 1)
- `inbox/twitter.md` — tweet URLs under `## To Read` (may be empty)
- `inbox/posts.md` — social media post blocks under `## To Process` (may be empty)
- `inbox/youtube.md` — YouTube URLs under `## To Read` (may be empty)

**Run:** Execute each sub-workflow in order:
1. `/wiki-clippings` — process `inbox/clippings/*.md`
2. `/wiki-links` — fetch and process URLs from `inbox/links.md`
3. `/wiki-tweets` — fetch and process tweet URLs from `inbox/twitter.md`
4. `/wiki-posts` — process raw post blocks from `inbox/posts.md`
5. `/wiki-youtube` — fetch transcripts from `inbox/youtube.md`

**Success criteria:**
- All `## To Read` / `## To Process` sections in inbox files are emptied
- Processed items moved to `## Done` sections in their respective inbox files
- Each fetched URL recorded in `.state/processed_urls.json`
- New wiki entries created at `wiki/<category>/<slug>.md` with EN + RU
- `index.md` regenerated to reflect all entries
- `.state/last_run.json` updated

**Failure handling:**
- If `fetch_url.py` is blocked by robots.txt, fall back to the `web-reader` MCP tool
- If a YouTube transcript is unavailable, create a stub entry with metadata only
- If a URL returns 404/5xx, log it to `.state/fetch_errors.json` and skip

**Prefer web-reader MCP over direct HTTP.** Always try `mcp__web-reader__webReader`
first for any URL fetch; only fall back to `python scripts/fetch_url.py` if the MCP fails.

---

## Step 3 — Process Queued Links (`/wiki-links`)

**What it does:** A second pass on `inbox/links.md` to catch any URLs that
were added to `## To Read` by Step 1 (reddit scan) but not yet processed
(Step 2's wiki-links only processes URLs that existed before it started).

**Inputs required:**
- `inbox/links.md` — check if `## To Read` section is non-empty after Step 2

**Run:**
```
# Check if there are unprocessed links remaining
```
If `## To Read` is empty, skip this step. Otherwise run `/wiki-links` again.

**Success criteria:**
- `inbox/links.md ## To Read` section is empty
- `.state/processed_urls.json` updated

---

## Step 3b — Update Relation Index

**What it does:** Rebuilds the relation index so `/wiki-search` relational
queries stay accurate after new entries are created.

**Run:**
```
python scripts/build_relations.py
```

If only one entry was created or updated, use the faster single-entry update:
```
python scripts/build_relations.py --slug <slug>
```

**Success criteria:**
- `.state/relations/_index.json` updated timestamp matches today
- Entry count in the index matches the wiki file count

**Failure handling:** Non-fatal — log and continue. The index is a cache;
stale data causes search misses, not data corruption.

---

## Step 4 — Check Entry Health (`/wiki-check`)

**What it does:** Audits all wiki entries for missing Russian sections, then
runs `obs.py check` to surface broken links and orphaned entries.

**Run:**
```
python scripts/obs.py broken
python scripts/obs.py orphans
```
Then for any entry missing `<!-- RU -->`, generate and append the Russian section.
For broken links, either fix the reference or note the target as a stub to create.
For orphans, add each to the Related Entries of the most semantically close
non-orphan entry.

**Success criteria:**
- `python scripts/obs.py check` reports `[OK] No broken links` and `[OK] No orphaned entries`
- Every `.md` file in `wiki/` contains the `---\n<!-- RU -->` divider
- No entry has a Russian section shorter than 50 characters

**Failure handling:** If `obs.py check` cannot reach zero issues in one pass,
log the remaining issues to `.state/lint-warnings.json` and continue. Do not block the pipeline.

---

## Step 5 — Rebuild Index (`/wiki-index`)

**What it does:** Regenerates `index.md` from all entries in `wiki/`, including
orphan markers from `obs.py orphans`.

**Run:**
```
python scripts/obs.py orphans   # collect list before writing index
```
Then rebuild `index.md` grouped by category with one-line summaries.
Append `(orphan)` marker to any entry that had no incoming backlinks.

**Success criteria:**
- `index.md` entry count matches `wiki/**/*.md` file count
- Last-updated date is today
- All categories present with correct counts

---

## Step 6 — Weekly Digest (`/wiki-digest`) — CONDITIONAL

**What it does:** Generates the bilingual weekly digest in `digests/YYYY-WNN.md`
covering all entries created or updated in the last 7 days.

**When to run:**
- Run if today is **Monday**, OR
- Run if `digests/<current-ISO-week>.md` does not exist

**Check:**
```powershell
$week = Get-Date -UFormat "%G-W%V"
$exists = Test-Path "digests\$week.md"
$isMonday = (Get-Date).DayOfWeek -eq "Monday"
if ($isMonday -or -not $exists) { # run /wiki-digest }
```

**Success criteria:**
- `digests/YYYY-WNN.md` exists and contains both EN and RU sections
- Both sections include Top News, New Tools, Tips, Concepts, Worth Reading
- The digest covers the correct date range for the ISO week

---

## Step 7 — Log, Commit, and Push

**What it does:** Writes the pipeline summary to log.md, then commits all changes and pushes.

**Run:**
```
# 1. Write pipeline summary to log.md FIRST (before git add)
python scripts/log_run.py "/wiki-pipeline" "reddit: X subs, Y entries. inbox: Z items. links: N processed. health: 0 broken, 0 orphans. digest: <created/skipped>. vault: X entries."

# 2. Commit everything including the freshly updated log.md
git add wiki/ inbox/ index.md digests/ log.md .state/reddit_cursor.json .state/processed_urls.json .state/last_run.json
# Note: .state/relations/ is gitignored — relations are rebuilt from source on each run
git commit -m "<structured message>"
git push
```

**Commit message structure:**
```
Wiki pipeline run YYYY-MM-DD: N new, M updated, K failed

- Reddit: <subreddits scanned> subreddits, <posts> qualifying posts, <new> entries
- Inbox: <links> links, <youtube> videos, <clippings> clippings processed
- Links: <N> queued URLs processed
- Health: <broken> broken links fixed, <orphans> orphans connected
- Digest: <created/skipped>
```

**Success criteria:**
- `git status` shows clean working tree after push
- Push completes without error

**Failure handling:** If push fails (network, auth), commit locally and log
the failure. The next pipeline run will push both commits.

---

## Full Run Summary Output

After all steps complete, print:

```
=== Wiki Pipeline Complete: YYYY-MM-DD ===
Step 1 Reddit:   14 subreddits scanned, N entries created, K URLs queued
Step 2 Inbox:    M entries created (L links, P YouTube, Q clippings)
Step 3 Links:    R additional URLs processed
Step 4 Health:   0 broken links, 0 orphans, 0 missing RU sections
Step 5 Index:    index.md updated (T total entries)
Step 6 Digest:   [created YYYY-WNN | skipped - not Monday]
Step 7 Git:      committed + pushed (X files changed)
Total new entries: N+M+R
```

---

## Notes

- **UTF-8 everywhere.** All Python file I/O uses `encoding='utf-8'`. All script
  output uses ASCII fallbacks for characters outside the ASCII range.
- **No /tmp/ paths.** Use project-relative paths or `%TEMP%` on Windows.
- **Idempotent.** Running twice in a row produces no duplicate entries because
  `processed_urls.json` deduplicates all fetched URLs.
- **Respect robots.txt.** Use web-reader MCP first; do not bypass access restrictions.
