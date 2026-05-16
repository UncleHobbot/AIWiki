Process all Obsidian Web Clipper exports in inbox/clippings/.

Steps:
1. List all .md files in inbox/clippings/
2. For each file:
   a. Extract the source URL from the front-matter "url:" field (added by Obsidian Web Clipper), or from the first URL found in the file body
   b. Load .state/processed_urls.json — skip this file if the URL is already listed there
   c. Read the full content of the file
   d. Classify the content into the best-fit wiki category: concepts / tools / agents / models / news / tips / people
   e. Extract: main ideas, key concepts, notable quotes, actionable tips
   f. Generate a slug from the title (lowercase, hyphens, max 50 chars)
   g. If wiki/<category>/<slug>.md already exists, update it; otherwise create it
   h. The file must contain both an English section and a Russian section separated by the exact divider:
      ---
      <!-- RU -->
   i. Append the source URL to .state/processed_urls.json
   j. Move the processed clipping to sources/web/<slug>.md
3. Rebuild index.md
4. Report: N created, M updated, K skipped

Wiki entry format to follow: see CLAUDE.md § Wiki Entry Format.
Language rules: see CLAUDE.md § Language Rules for Russian Translation.
