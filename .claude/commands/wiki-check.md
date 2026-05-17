Find all wiki entries that are missing their Russian section and add it. Also run vault link health checks.

Steps:
1. Run the Obsidian vault analysis to surface link issues:
   a. python scripts/obs.py broken
      → lists [[links]] whose target .md file doesn't exist yet; note these as stubs to create
   b. python scripts/obs.py orphans
      → lists entries with no incoming backlinks; add them to Related Entries of semantically close entries
2. Recursively list all .md files in wiki/
3. For each file, check whether the exact divider is present:
      ---
      <!-- RU -->
   (a horizontal rule followed immediately by the HTML comment on the next line)
4. For files where the divider is missing:
   a. Read the existing English content
   b. Generate a natural Russian translation following the language rules in CLAUDE.md:
      - Use natural Russian, not machine-literal translation
      - Keep English technical terms with no established Russian equivalent
        (token, prompt, fine-tuning, RAG, agent, pipeline, etc.)
      - Translate headings; keep front-matter keys in English
      - Do NOT translate or repeat code blocks, CLI examples, or file paths
      - The ## Related Entries links are identical in both sections
   c. Append the divider and Russian section to the file
5. For files where the divider exists but the Russian section is empty or very short (< 50 chars):
   treat them as missing and regenerate the Russian section
6. Report: N files updated, M files already complete, K broken links, J orphans
7. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-check" "<N RU sections added, K broken links fixed, J orphans connected. Vault: X entries.>"
