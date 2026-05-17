Process everything in the inbox by running each sub-workflow in sequence.

Steps:
1. Run the wiki-clippings workflow (process all files in inbox/clippings/)
2. Run the wiki-links workflow (process all URLs in inbox/links.md)
3. Run the wiki-tweets workflow (process all URLs in inbox/twitter.md)
4. Run the wiki-posts workflow (process all posts in inbox/posts.md)
5. Run the wiki-youtube workflow (process all URLs in inbox/youtube.md)
6. Rebuild index.md from all wiki/ entries
7. Append a one-line summary of this run to .state/last_run.json
8. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-inbox" "<N created, M updated. Key items: slug1 (cat), slug2 (cat). Index: X total.>"

Report total entries created, updated, and skipped across all sources.
