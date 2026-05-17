Run the inbox-to-wiki pipeline using parallel subagents: one coordinator groups
items by source type, four specialized fetch workers run concurrently, then a
merge step resolves conflicts and updates the index.

---

## Phase 1 — Coordinate (read & group inbox)

Run:
    python scripts/inbox_coordinator.py --json

Read the JSON manifest from stdout (also saved to .state/inbox_manifest.json).
Report the item count per group:
  - link      → blog posts, articles
  - paper     → academic papers (arxiv, semanticscholar, openreview, etc.)
  - youtube   → YouTube videos
  - twitter   → tweets (twitter.com / x.com)
  - clipping  → Obsidian Web Clipper exports in inbox/clippings/
  - post      → raw social-media text blocks in inbox/posts.md
  - reddit    → subreddit scans (always 14 subreddits; cursor-deduped)

If the total is 0 across all groups, report "Inbox is empty." and stop.

---

## Phase 2 — Parallel fetch (all source types concurrently)

Run:
    python scripts/parallel_fetch.py --workers 8

This fetches ALL item types simultaneously using a thread pool. Progress is
logged to stderr by the script. When it finishes, read
.state/fetch_results.json and report:

  Fetched: N/M items in X.Xs wall time (Y from cache, Z failed)

If any items failed, list the failing URLs and continue — don't abort.

Each fetched item is cached at .state/fetch_cache/<type>/<hash>.json so
re-runs skip already-fetched content instantly.

---

## Phase 3 — Specialized processing (write wiki entries)

Process each source-type group in this order (fastest first so partial
failures don't block quick wins):

### 3a. Posts (no network — instant)
For each post block in .state/fetch_results.json where type == "post":
  - Extract: source, author, date from the <!-- metadata --> comment if present
  - Classify using the category decision tree in CLAUDE.md
  - Create or update wiki/<category>/<slug>.md (bilingual: EN + RU)

### 3b. Clippings (local files — fast)
For each clipping item:
  - Content is already in the fetch cache (the raw .md text)
  - Extract the source URL from the front-matter `url:` field
  - Classify, extract key ideas, write bilingual entry
  - Move processed file from inbox/clippings/ to sources/web/<slug>.md

### 3c. Academic papers (clippings from arxiv/openreview — careful extraction)
For each paper item:
  - Treat the same as a link, but:
    - Always categorise as concepts/ (default) or models/ if it evaluates a model
    - Add a ## Abstract section before ## Key Ideas, quoting the paper abstract
    - Include arXiv ID in tags if URL contains arxiv.org
  - Classify, write bilingual entry

### 3d. Links / articles (web-fetched)
For each link item (content already cached):
  - Use cached content from .state/fetch_cache/link/<hash>.json
  - Classify, extract, write bilingual entry

### 3e. Twitter
For each twitter item (content already cached):
  - Parse JSON content: text, author, urls (expanded)
  - If tweet contains a non-twitter URL, queue it in inbox/links.md ## To Read
  - Write a compact bilingual entry with the tweet insight
  - If tweet is < 100 chars with no novel insight, skip it

### 3f. YouTube
For each youtube item (transcript already cached):
  - Parse JSON content: title, channel, date, description, transcript
  - Write bilingual entry with ## Video Notes / ## Заметки по видео sections
  - Include timestamp references where the transcript supports them

### 3g. Reddit
For each reddit item (posts already cached):
  - Posts are in the `posts` array of .state/fetch_cache/reddit/<hash>.json
  - Filter: score >= 50 OR comment_count >= 20
  - For qualifying posts, classify and write bilingual entry
  - Any external URLs found → append to inbox/links.md ## To Read
  - Update .state/reddit_cursor.json with newest post IDs

After writing each entry:
  - Record the source URL in .state/processed_urls.json
  - Note the slug for the merge step

---

## Phase 4 — Merge & conflict resolution

After all entries are written:

1. **Slug deduplication**: if two newly written entries have the same slug,
   compare their sources. Merge the shorter into the longer one — append
   its key ideas and sources rather than creating a duplicate file.

2. **Backlink healing**: run
       python scripts/obs.py broken
   For each broken [[link]] that matches a newly created slug, the link is
   automatically valid — no action needed. Report any remaining broken links.

3. **Orphan check**: run
       python scripts/obs.py orphans
   For each orphaned entry (no incoming backlinks), find the 2 most
   semantically related entries and add the orphan to their ## Related Entries
   section (English AND Russian). Do not add more than 2 new backlinks per pass.

4. **Backlink conflict**: if two new entries each reference each other AND both
   were created this run, this is normal — leave both links in place.

---

## Phase 5 — Index & state

1. Rebuild index.md:
       python scripts/obs.py check   (vault health report)
   Then regenerate index.md grouped by category, one line per entry.

2. Log run to .state/last_run.json:
   {
     "command": "wiki-inbox-parallel",
     "timestamp": "<ISO-8601>",
     "wall_fetch_s": <from fetch_results.json>,
     "created": <count>,
     "updated": <count>,
     "skipped": <count>,
     "failed": <count>
   }

---

## Final report

Print a summary table:

  Phase 1 Coordinate  : N items grouped
  Phase 2 Fetch       : N/M fetched in X.Xs  (Y cached, Z failed)
  Phase 3 Write       : C created, U updated, S skipped, F failed
  Phase 4 Merge       : D duplicates resolved, B broken links, O orphans linked
  Phase 5 Index       : index.md rebuilt, run logged

  Wall time (fetch phase): X.Xs
  Entries written this run: C+U

If the --benchmark flag is passed as $ARGUMENTS, also run:
    python scripts/benchmark_inbox.py --items 20 --workers 8 --runs 3
and append the speedup table to the final report.

**Write to log.md after completing** (required — do not skip):
   python scripts/log_run.py "/wiki-inbox-parallel" "<fetch: N/M in X.Xs. C created, U updated, S skipped, F failed. Key items: slug1 (cat). Vault: X entries.>"
