---
name: "source-command-wiki-links"
description: "Migrated source command `wiki-links`"
---

# source-command-wiki-links

Use this skill when the user asks to run the migrated source command `wiki-links`.

## Command Template

Fetch and process all URLs listed in inbox/links.md.

inbox/links.md format:
  Lines starting with - or * that contain a URL are treated as links.
  Text after <!-- is treated as a comment and ignored.
  Lines under a "## Done" heading are skipped.

Steps:
1. Parse inbox/links.md and collect all unprocessed URLs
2. Load .state/processed_urls.json and skip any URL already listed there
3. For each remaining URL:
   a. Run: python scripts/fetch_url.py "<url>"
   b. If the fetch fails, log the URL and error to .state/fetch_errors.json and continue
   c. Classify the fetched content: concepts / tools / agents / models / news / tips / people
   d. Extract main ideas, key concepts, actionable tips
   e. Generate a slug from the page title
   f. If wiki/<category>/<slug>.md already exists, update it; otherwise create it
   g. The file must contain both English and Russian sections separated by:
      ---
      <!-- RU -->
   h. Append the URL to .state/processed_urls.json
4. Move all processed URLs to a "## Done" section at the bottom of inbox/links.md
5. Rebuild index.md
6. Report: N created, M updated, K failed
7. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-links" "<N created, M updated, K failed. Key items: slug1 (cat), slug2 (cat). Processed URLs: X.>"

Wiki entry format to follow: see AGENTS.md § Wiki Entry Format.
