Fetch and process all tweet URLs listed in inbox/twitter.md.

inbox/twitter.md format:
  Lines starting with - or * that contain a Twitter/X URL are treated as links.
  Text after <!-- is treated as a comment and ignored.
  Lines under a "## Done" heading are skipped.

Steps:
1. Parse inbox/twitter.md and collect all unprocessed tweet URLs
2. Load .state/processed_urls.json and skip any URL already listed there
3. For each remaining URL:
   a. Run: python scripts/fetch_twitter.py "<url>"
      This fetches the tweet text and expands t.co short URLs
   b. If the fetch fails, log the URL and error to .state/fetch_errors.json and continue
   c. Collect all external URLs (non-Twitter/X) found in the tweet
   d. If the tweet text itself contains a notable insight (tip, announcement, research
      finding, tool mention):
      - Classify it: news / tips / concepts / tools / people
      - Create or update the bilingual wiki entry at wiki/<category>/<slug>.md
      - The entry must contain English and Russian sections separated by:
        ---
        <!-- RU -->
   e. Append the tweet URL to .state/processed_urls.json
4. Add all collected external URLs to inbox/links.md under "## To Read"
5. Move all processed URLs to a "## Done" section at the bottom of inbox/twitter.md
6. Report: N tweet insights captured, M URLs queued, K failed
7. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-tweets" "<N insights captured, M URLs queued to links.md. Key items: slug1 (cat).>"

Wiki entry format to follow: see CLAUDE.md § Wiki Entry Format.
