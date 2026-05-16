Process all tweet dump files in inbox/tweets/.

Accepted file formats:
  - Plain text: tweets separated by lines containing only ---
  - Markdown: each tweet as a blockquote starting with >
  - JSON: array of objects with "text", "author", and optionally "url" fields

Steps:
1. List all files in inbox/tweets/
2. For each file, run: python scripts/fetch_twitter.py "<filepath>"
   This parses the tweets and expands any t.co short URLs.
3. For each parsed tweet:
   a. Collect all external URLs (non-Twitter/X) from the expanded URL list
   b. If the tweet text itself contains a notable insight (tip, announcement, research finding, tool mention):
      - Classify it: news / tips / concepts / tools / people
      - Create or update the matching bilingual wiki entry at wiki/<category>/<slug>.md
      - The entry must contain English and Russian sections separated by:
        ---
        <!-- RU -->
4. Add all collected external URLs to inbox/links.md under "## To Read" for processing by wiki-links
5. Move each processed tweet file to sources/tweets/<original-filename>
6. Report: N tweet insights captured, M URLs queued

Wiki entry format to follow: see CLAUDE.md § Wiki Entry Format.
