Find all wiki entries that are missing their Russian section and add it.

Steps:
1. Recursively list all .md files in wiki/
2. For each file, check whether the exact divider is present:
      ---
      <!-- RU -->
   (a horizontal rule followed immediately by the HTML comment on the next line)
3. For files where the divider is missing:
   a. Read the existing English content
   b. Generate a natural Russian translation following the language rules in CLAUDE.md:
      - Use natural Russian, not machine-literal translation
      - Keep English technical terms with no established Russian equivalent
        (token, prompt, fine-tuning, RAG, agent, pipeline, etc.)
      - Translate headings; keep front-matter keys in English
      - Do NOT translate or repeat code blocks, CLI examples, or file paths
      - The ## Related Entries links are identical in both sections
   c. Append the divider and Russian section to the file
4. For files where the divider exists but the Russian section is empty or very short (< 50 chars):
   treat them as missing and regenerate the Russian section
5. Report: N files updated, M files already complete
