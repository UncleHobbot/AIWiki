# LLM Wiki — Activity Log

## 2026-05-15

**12:00 /wiki-reddit** — Scanned 12 subreddits, 52 qualifying posts, 7 entries created: orthrus-qwen3-acceleration (tools), arxiv-llm-ban-policy (news), figure-ai-03-robot-30-hours (news), deepseek-v4-vs-opus-kimi (models), shokunin-memory-system (tools), gen-ai-web-traffic-may-2026 (news), github-copilot-pricing-exodus (news). Also fixed fetch_reddit.py OAuth fallback + UTF-8 encoding.

**14:30 /wiki-reddit (run 2)** — Scanned 12 subreddits incrementally, 109 posts fetched, 69 qualifying (66 new). 12 entries created: poetiq-recursive-self-improvement (tools), openai-100-dollar-tier (news), tabpfn-3-tabular-foundation-model (models), mythos-cybersecurity-agent (agents), roo-code-shutdown-roomote (news), apple-m5-kernel-exploit-ai (news), figure-ai-team-robots-livestream (news), cline-roo-alternatives (tips), chorus-multi-model-setup (tips), fda-ai-clinical-trials (news), mcp-financial-data-server (tools), gpt-vs-glm-5-1-comparison (models). Index rebuilt: 37 entries total. State updated: 156 processed URLs, 12 subreddit cursors.

**13:00 /wiki-inbox** — 6 links + 8 YouTube videos processed. 5 entries created: llm-wiki-pattern (concepts), github-copilot-cli (tools), llmwiki-open-source (tools), llm-wiki-setup-guide (tips), llm-wiki-enterprise-patterns (agents). YouTube: 8 LLM Wiki tutorial videos, 2 entries from full transcripts. Index: 12 entries total.

**14:00 /wiki-inbox** — 4 links processed. 3 entries created: copilot-cli-telegram-bridge (tips), cpt-copilot-terminal (tools), llm-wiki-ecosystem (tools). 1 updated: github-copilot-app (added official README details). Index: 21 entries.

---

## 2026-05-16

**00:00 /wiki-inbox** — 8 Claude Code doc pages + 10 YouTube talks processed. 16 entries created: claude-code-agentic-loop, claude-code-extensions-overview, claude-code-directory, claude-code-memory, claude-code-permission-modes, claude-code-workflows-best-practices (agents/tips); 10 AI Agents Montreal talks (8 with full yt-dlp transcripts, 2 description-only due to rate limiting). Index: 55 entries.

**01:00 /wiki-reddit** — Scanned 12 subreddits (incremental). 2 entries created: claude-code-deferral-behavior (tips — Opus 4.7 task-skipping pattern), claude-code-frameworks (tips — GSD/Superpowers/Ouroboros/Han guide). Queued github.com/testdouble/han to links.md. Index: 57 entries.

**12:00 /wiki-inbox** — 4 links processed. 3 entries created: dotnet-claude-kit (tools — .NET 10 expert layer for Claude Code), awesome-agent-skills (tools — 1000+ curated agent skills), visual-explainer (tools — HTML diagram skill). 1 skipped: AntonIliashenko/MathWiki (404). Index: 73 entries.

**13:00 /wiki-reddit** — Scanned 14 subreddits (added r/ollama, r/vibecoding). 350 posts, 77 qualifying. 2 entries created: self-guided-self-play (concepts — SGS algorithm, 7B beats 671B on Lean4), dynamic-compute-budget-local-llm (tips — DCA gets Qwen-35B to 39.9% on HLE). Queued 5 URLs to links.md. Index: 75 entries.

**14:00 /wiki-links** — 5 URLs processed. 2 created: agi-impossibility-proof-debunked (concepts — Guerzhoy 2026 debunks Van Rooij Ingenia Theorem), github-spec-kit (tools — spec-driven dev toolkit, 30+ agents). 1 updated: self-guided-self-play (added authors Bailey et al. + arXiv sources). Index: 77 entries. Processed URLs: 204.

**15:00 /wiki-digest** — Inaugural bilingual digest generated: digests/2026-W20.md. Covers all 77 entries (wiki launched this week). Categories: 11 news, 27 tools, 20 tips, 11 agents, 5 concepts, 3 models. Top story: Mythos cybersecurity agent (32-step network attack benchmark).

**16:00 vault lint** — `python scripts/obs.py check` run after installing obsidiantools 0.11.0. Fixed: 7 broken [[links]] (resolved to existing entries or removed), 32 orphaned entries (connected via Related Entries edits across 17 files). Also fixed EN/RU divergence in llm-wiki-pattern (RU had 2 related entries vs 5 in EN). Final state: 0 broken, 0 orphans, 0 isolated across 78 entries.

**17:00 tooling** — Installed obsidiantools 0.11.0. Created scripts/obs.py (Obsidian vault CLI: backlinks, orphans, broken links, top-linked, full health check). Created requirements.txt. Updated CLAUDE.md with Windows Environment, Editing Conventions, and Network Fetching sections. Updated wiki-check and wiki-index commands to run obs.py.

**17:30 wiki-pipeline skill** — Extracted canonical 7-step maintenance sequence from 6 session transcripts. Created .claude/skills/wiki-pipeline/SKILL.md, .claude/commands/wiki-pipeline.md, wiki-pipeline-task.xml, wiki-pipeline-run.ps1. Task Scheduler trigger: daily 08:00, logs to .state/pipeline.log.

---

## 2026-05-17

**09:00 scripts/_template.py** — Created Python boilerplate with UTF-8 stdout reconfigure, read/write helpers with explicit encoding='utf-8', ASCII-safe log() helper, and parse_ytdlp_json() / parse_ytdlp_json_stream() for yt-dlp output parsing. Updated CLAUDE.md to mandate all new Python scripts start from this template.

**10:00 research** — Task agent researched academic applications of LLM-powered personal wikis. Found 5 key papers: KARMA (NeurIPS 2025), SurveyGen-I (IJCNLP-AIJLP 2025), LightRAG (EMNLP 2025), PARNESS (2026), LLM4SR (2025). Identified 3 feature gaps: contradiction detector, relation index, digest terminology memory.

**10:30 /wiki-links (queued)** — 4 arXiv sources from research added to inbox/links.md: arXiv:2502.06472 (KARMA), arXiv:2508.14317 (SurveyGen-I), arXiv:2410.05779 (LightRAG), arXiv:2605.05258 (PARNESS). LLM4SR (2501.04306) skipped — already processed.

**10:45 wiki entry** — Created wiki/concepts/llm-wiki-academic-applications.md: bilingual survey entry covering 5 papers, 3 feature ideas, 200-word executive summary. Linked from llm-wiki-pattern and llm4sr-survey. Vault: 79 entries, 0 broken links, 0 orphans.

**11:30 /wiki-links** — 4 arXiv papers processed. 3 created: karma-knowledge-graph-enrichment (concepts — 9-agent KG enrichment, 83.1% correctness, NeurIPS 2025), surveygen-i-scientific-survey (concepts — memory-guided survey generation, IJCNLP-AIJLP 2025), parness-automated-scientific-research (tools — DAG kernel + scenario-typed KG retrieval, arXiv 2026). 1 updated: lightrag-graph-rag (added cross-links to new entries). Vault: 82 entries, 0 broken links, 0 orphans. Processed URLs: 208.

**12:30 features** — Implemented 2 of 3 research feature ideas (#1 contradiction detector deferred — overkill at 82 entries). #2: digest terminology memory (digests/memory.json seeded with 55 terms from W20; wiki-digest command updated to load/save memory). #3: incremental relation index (scripts/build_relations.py — 82 entries, 308 unique tags; wiki-search command extended with relational mode; relational queries verified: "tools using RAG" → 3 results, "concepts about knowledge-graph" → 2 results).

**13:30 /wiki-inbox-parallel** — First parallel pipeline run. Fixed: processed_urls.json format mismatch (flat list vs dict) in utils.py and inbox_coordinator.py; posts.md template header false-positive in scan_posts; utcnow() deprecation. Phase 2 fetch: 14 subreddits in 29.1s wall time (parallel). Phase 3: 46 qualifying posts, 2 new entries created: codex-on-mobile (news — Codex on iOS/Android), package-hallucination-mcp (tools — MCP that catches ~20% hallucinated npm/PyPI package names). Vault: 84 entries, 0 broken, 0 orphans.

**14:00 /wiki-fix** — pytest suite ran (first run after test suite was added). 254 passed, 1 failed: [[github-copilot-cli]] missing from index.md Tools section. Fixed, re-ran: 255 passed, 0 failed.

**15:00 research + wiki entries** — Task agent researched LLM Wiki ecosystem implementations (35 web sources, 27 tool calls). Findings: 30+ repos on GitHub, WiCER paper (53–60% blind compilation failure rate), two camps (personal PKM vs agent knowledge layer), Obsidian debate, productization wave. 2 entries created: llm-wiki-implementations-landscape (concepts — full ecosystem map), llm-wiki-ecosystem.md fully rewritten with new tables, star counts, and cross-links. 22 URLs queued to inbox/links.md (WiCER, SamurAIGPT, claude-obsidian, nvk/llm-wiki, OmegaWiki, librarian, awesome-llm-wiki, LLM Wiki v2 gist, HN threads, llm-wiki.net, blog analyses). Vault: 85 entries.

**16:30 /wiki-inbox-parallel (run 2)** — 72-item batch: 38 links, 13 YouTube (all Matt Pocock / aihero.dev), 7 Twitter (all failed — no auth), 14 Reddit (cached). Fetch: 65/72 OK in 11.9s wall time. 3 robots.txt blocks (Axios, TowardsDS, MLMastery). 3 entries created: agent-harness-engineering (concepts — O'Reilly Radar + VS Code blog: Agent = Model + Harness), tencent-db-agent-memory (tools — Tencent local 4-tier memory, −61% tokens, +51% pass rate), matt-pocock-aihero (people — first people entry; /grill-me skill 46k stars, tracer bullets, codebase-design-for-AI; 13 YouTube videos consolidated). Vault: 89 entries, 0 broken, 0 orphans. Processed URLs: 266.

**17:30 research + wiki entry** — Task agent researched Gnosis MCP vs LLM Wiki pattern comparison (35 web sources). Created gnosis-mcp-vs-llm-wiki-pattern (concepts): token economics table, failure modes for each tool, 3 hybrid architectures, WiCER benchmark finding (53–60% blind compilation failure). Key verdict: complementary — Gnosis for factual lookup over large/volatile corpora, LLM Wiki for cross-doc synthesis over small/stable corpora. 5 new source URLs queued (particula.tech, pasqualepillitteri.it, atlan.com, gnosismcp.com, local-rag repo). Vault: 94 entries (4 new from another session also integrated: andrej-karpathy people entry, github-agentic-developer-certification news, enterprise-gpu-underutilization news, llm-assumption-propagation tips). All broken links from other session fixed.

**18:30 /wiki-fix** — pytest: 285 passed, 1 failed (llm-assumption-propagation missing from index.md Tips section). Fixed in 1 round. Final: 285 passed, 0 failed.

**19:00 maintenance** — Updated README.md: 61→94 entries, added parallel pipeline, scheduled automation, quality assurance, full scripts table, OpenCode support sections. Committed opencode.json model assignments (deepseek-v4-flash for ingestion, kimi-k2.6 for YouTube/pipeline, glm-5.1 for check/fix).
