Process all social media text posts in inbox/posts.md.

inbox/posts.md format:
  Posts are separated by lines containing only ---.
  Each post block may optionally start with a metadata comment:
    <!-- Source: Platform | Author: name | Date: YYYY-MM-DD -->
  The rest of the block is the raw post text.
  Posts under a "## Done" heading are skipped.

Steps:
1. Read inbox/posts.md
2. Split the "## To Process" section into individual post blocks on --- separators
3. For each post block:
   a. Extract metadata from the optional <!-- Source: ... --> comment (platform, author, date)
   b. Read the post text
   c. Skip blocks that are empty or contain only whitespace
   d. Collect any URLs found in the post text and add them to inbox/links.md under "## To Read"
   e. Analyze the post text for notable insights:
      - Tips, techniques, or best practices
      - Tool announcements or releases
      - Research findings or benchmarks
      - Opinions from notable people in AI/tech
   f. If the post contains extractable knowledge:
      - Classify: news / tips / concepts / tools / models / agents / people
      - Generate a slug from the insight title
      - Create or update wiki/<category>/<slug>.md
      - The entry must contain English and Russian sections separated by:
        ---
        <!-- RU -->
      - Set sources: to the author's profile URL if known, or note as "community post"
   g. If the post is opinion/discussion without clear extractable knowledge, skip it
4. Move processed post blocks to a "## Done" section at the bottom of inbox/posts.md
5. Report: N entries created, M updated, K skipped (no notable insight)

Wiki entry format to follow: see CLAUDE.md § Wiki Entry Format.
