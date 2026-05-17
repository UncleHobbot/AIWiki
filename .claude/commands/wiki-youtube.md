Fetch transcripts and extract knowledge from YouTube URLs listed in inbox/youtube.md.

inbox/youtube.md format:
  Lines containing a YouTube URL (youtube.com/watch or youtu.be) are processed.
  Text after <!-- is a comment and ignored.

Steps:
1. Parse all YouTube URLs from inbox/youtube.md
2. Load .state/processed_urls.json and skip any URL already listed
3. For each remaining URL:
   a. Run: python scripts/fetch_youtube.py "<url>" --save
      This returns JSON with: title, channel, date, description, transcript, transcript_language
   b. If transcript_available is false: extract knowledge from title and description only,
      and set transcript: unavailable in the entry front matter
   c. Analyze the transcript (or description) for:
      - Main thesis or central topic
      - Key concepts explained
      - Tools, papers, or people mentioned
      - Actionable tips or techniques
      - Short impactful quotes worth preserving
   d. Classify the video: concepts / tools / agents / models / news / tips / people
   e. Generate a slug from the video title
   f. Create or update wiki/<category>/<slug>.md
   g. The English section must include a "## Video Notes" subsection with key points
      and timestamp references where relevant (e.g. [12:34] Key insight here)
   h. The Russian section must include a "## Заметки по видео" subsection
   i. Both sections are in one file, separated by:
      ---
      <!-- RU -->
   j. Append the URL to .state/processed_urls.json
4. Rebuild index.md
5. Report: N entries created, M updated, K failed
6. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-youtube" "<N created, M updated. Key items: slug1 (cat), slug2 (cat). Index: X total.>"

Wiki entry format to follow: see CLAUDE.md § Wiki Entry Format.
