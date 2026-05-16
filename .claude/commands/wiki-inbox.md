Process everything in the inbox by running each sub-workflow in sequence.

Steps:
1. Run the wiki-clippings workflow (process all files in inbox/clippings/)
2. Run the wiki-links workflow (process all URLs in inbox/links.md)
3. Run the wiki-tweets workflow (process all files in inbox/tweets/)
4. Run the wiki-youtube workflow (process all URLs in inbox/youtube.md)
5. Rebuild index.md from all wiki/ entries
6. Append a one-line summary of this run to .state/last_run.json

Report total entries created, updated, and skipped across all sources.
