Search all wiki entries for the query passed as arguments to this command.

The search query is: $ARGUMENTS

Steps:
1. If $ARGUMENTS is empty, ask the user what they want to search for
2. Search across all .md files in wiki/ for $ARGUMENTS:
   - Exact title match (highest relevance)
   - Tag match in front matter
   - Match in the English section body
3. Return results sorted by relevance, showing for each match:
   - Entry title and category
   - File path
   - A 2-sentence excerpt from the English section containing the match
   - The matching tags (if any)
4. If no results found, suggest related terms or nearby entries

Limit results to 10 matches. If more exist, say so.
