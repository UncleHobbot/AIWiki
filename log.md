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

**14:19 ecosystem update** — Rewrote llm-wiki-ecosystem.md: added GitHub links to all 15 projects, comparison table (AIWiki vs nvk/OmegaWiki/mduongvandinh), 7 ideas-to-steal section. Fixed 6 orphans from other session.

**14:36 research + wiki article** — Created autonomous-personal-agents-openclaw-hermes-zeroclaw (agents): OpenClaw/Hermes/ZeroClaw/NemoClaw/Zo comparison across features, NAS hosting, messenger integrations, personal task automation. Fixed 5 orphans from other sessions. Vault: 109 entries.

**14:45 C:/Program Files/Git/wiki-posts** — 2 posts processed. 1 created: claude-code-12-setup-tricks (tips — 12 env setup practices: CLAUDE.md memory, git worktrees, MCP, subagents, slash commands, CI/CD integration). 1 skipped (trending repos list → 5 URLs queued to links.md: agentmemory, 9router, UI-TARS-desktop, mattpocock/skills, CloakBrowser). Vault: 111 entries.

**14:51 C:/Program Files/Git/wiki-links** — 5 URLs processed: agentmemory (tools — LLM Wiki pattern extension, 95.2% recall R@5, 51 MCP tools, $10/yr), 9router (tools — RTK token saver 20-40%, free AI coding via 40+ providers), ui-tars-desktop (agents — ByteDance GUI agent, books hotels/flights autonomously), mattpocock-skills-repo (tools — 18.3k stars, 14 daily skills), cloakbrowser updated (confidence+aliases). 0 failed. Processed URLs: 290.

---

## 2026-05-18

**06:26 /wiki-reddit** — 14 subs scanned (r/kimi rate-limited), 2 entries created: sparky-offline-edge-ai-robot (tools), llm-git-knowledge-accumulation (tips). Index: 117 total.

**06:50 /wiki-inbox** — 14 created, 2 updated, 5 skipped. Links: learn-harness-engineering-course (concepts). Tweets: memory-skills-unified-harness (concepts), claude-usage-limits-token-management (tips). YT: agent-operating-system, agent-orchestration-multi-model-framework, hermes-agent-llm-wiki-integration, open-source-models-vs-opus-copilot-benchmark, ai-agents-arr-framework-ooda-loop + 5 more. Index: 131 total.

**06:59 /wiki-digest** — 2026-W21 digest generated, 131 entries covered, 17 terms added to memory.json (total 63). Highlights: Mythos cybersecurity AI, Figure AI 03, Copilot pricing exodus, Poetiq SOTA, Orthrus 7.8x, Sparky robot, harness engineering course.

**07:00 /wiki-check** — 0 RU sections needed (all 131 complete), 0 broken links, 0 orphans. Vault fully healthy. 396 tests passed.

**13:19 manual update** — Updated mathwiki-llm-research-automation.md: all 6 gaps now marked DONE (implemented 2026-05-18), added improvement 7 (/wiki-insights), new remaining-gaps section (22 broken links, empty contradictions/, missing method pages, Cayley Section 2.3).

**13:43 C:/Program Files/Git/wiki-hackernews** — 10 articles fetched, 3 qualified. Created: praisonai-cve-2026-44338-agent-auth-bypass (news), microsoft-mdash-agentic-vulnerability-scanner (agents), node-ipc-backdoor-ai-tool-credentials (news). Skipped 7 (no AI angle or vendor puff piece). Index rebuild pending.

**13:43 C:/Program Files/Git/wiki-hackernews** — 10 articles fetched, 3 qualified, 3 entries created. See above.

**20:45 C:/Program Files/Git/wiki-inbox** — All inboxes empty — 0 entries created, 0 updated. Clippings: 0, Links: 0, Tweets: 0, Posts: 0, YouTube: 0. Index: 140 total.

---

## 2026-05-19

**11:08 C:/Program Files/Git/wiki-inbox** — 0 created, 0 updated. All inbox queues empty: clippings/ (0 files), links.md (0 to-read), twitter.md (0 new), posts.md (0 posts), youtube.md (0 new). Index: 135 total.

**12:05 C:/Program Files/Git/wiki-reddit** — 14 subs, 94 posts scanned, 4 created: programbench-gpt55-first-solve (news), isomorphic-labs-series-b-2b (news), vibe-coding-bundling-what-already-exists (tips), kimi-2-6-vs-glm-5-1-agent-reliability (models). 8 skipped (already exist). Index: 139 total.

**12:08 C:/Program Files/Git/wiki-hackernews** — 30 articles fetched, 2 qualified (score>=2), 1 created: supply-chain-attacks-ai-coding-tools-2026 (news) — Nx Console+Mini Shai-Hulud wave targeting Claude Code. Index: 140 total.

---

## 2026-05-20

**08:18 /wiki-reddit** — 14 subs (12 OK, 2 rate-limited: opencode/opencodeCLI), 91 posts scanned, 2 created: lawzero-scientist-ai-bengio (concepts), gemini-3-1-agent-api-preview (news). Skipped: all singularity/Copilot/kimi/vibecoding posts already exist. Index: 142 total.

**08:57 /wiki-hackernews** — 30 articles fetched, 1 qualified (score=2), 0 created: Trapdoor Android ad fraud skipped (no AI angle, pure malvertising). Index: 142 total.

**21:55 /wiki-reddit** — 14 subs (11 OK, 3 rate-limited: ollama/opencode/opencodeCLI; LocalLLaMA/ML/ChatGPT retried OK), 3 created: gpt55-frontiermath-benchmark-errors (news), japan-autonomous-medicine-lab-aist (news), agentic-coding-addiction-behavioral-changes (tips). Index: 145 total.

**22:14 /wiki-hackernews** — 30 articles fetched, 1 qualified (score=3 from agent keywords), 0 created: RAMPART/Clarity Microsoft AI agent security testing framework skipped — primary subject is security testing, aligns with removed AI Security topic. Index: 139 total.

**22:19 /wiki-reddit** — 14 subs (11 OK, 3 rate-limited: ollama/opencode/opencodeCLI), 92 posts, 0 created, 1 updated: kimi-2-6-vs-glm-5-1-agent-reliability (Z.ai service improvement note). 1 URL queued: Google REPLIQA quantum+AI. Most posts already covered. Index: 139 total.

---

## 2026-05-21

**14:44 /wiki-reddit** — 14 subs (all OK), 101 posts, 1 created: ambient-analog-ai-coding-workflows (tips). Skipped 55 repeats. Claude usage reset posts (182+194pts) skipped — image-only. Index: 140 total.

**16:18 /wiki-inbox** — 3 created, 1 updated. Links: REPLIQA skipped. Tweets: Matt Pocock /tdd insight → updated test-driven-agentic-behaviours; 4 queued to links.md. YT: 3 entries from Claude/IBM channels: claude-code-explore-plan-code-commit (tips), anthropic-agent-memory-dreaming (agents), mcp-vs-adk-agent-connectivity (agents). Index: 143 total.

**16:19 /wiki-hackernews** — 30 articles fetched, 0 qualified (score>=2). Nothing to process. Index: 143 total.

---

## 2026-05-22

**09:17 /wiki-reddit** — 14 subs (11 OK, 3 rate-limited: ollama/opencode/opencodeCLI), 92 posts, 2 created: artificial-analysis-coding-agent-index (news), cola-dlm-bytedance-diffusion-lm (models). Rest repeats. Index: 145 total.

**10:06 /wiki-hackernews** — 30 articles fetched, 0 qualified (score>=2), 0 entries created. 1 queued to links.md: agent-ai-identity (news). 5 malware/no-AI-angle articles skipped. Index: unchanged.

**10:16 /wiki-inbox** — 1 created, 0 updated, 4 skipped. Created: ai-agent-identity-iam-risks (concepts). 4 tweet URLs blocked (web-reader rate-limited until 2026-05-26). Index: 146 total.

**16:40 /wiki-reddit** — 14 subs, 4 entries created: equibles-mcp-financial-data (tools), chorus-multi-llm-code-review (tips), claude-code-usage-reset-may-2026 (news), greg-brockman-openai-product-lead (news). Index: 150 total. Queued 5 URLs to links.md.

---

## 2026-05-24

**14:55 /wiki-reddit** — 14 subs scanned (kimi retried after 429). 3 entries created: mythos-aisi-cyber-capability-2026 (news), intern-s2-preview (models), llm-hallucination-bixonimania-case (concepts). 8 skipped (already exist: gen-ai-web-traffic, github-copilot-app, deepseek-v4, tabpfn-3, lawzero, isomorphic-labs, fda-ai-clinical-trials, chorus). Index: 153 total.

**14:58 /wiki-hackernews** — 30 articles fetched, 1 qualified (score 1 but high-relevance override). 1 entry created: project-glasswing-anthropic-vulnerability-discovery (news). 1 skipped: laravel-lang supply chain (no AI angle). Index: 154 total.

**15:06 /wiki-inbox** — 5 created, 0 updated, 6 skipped. Created: github-copilot-sdk (tools), microsoft-waza (tools), stop-slop-skill (tools), superpowers-plugin-claude-code (agents), using-git-worktrees-claude-code (tips). Tweets still blocked (retry May 26). Index: 159 total.

**15:07 /wiki-inbox** — Inbox empty — 0 clippings, 0 links (4 rate-limited tweets skipped), 0 tweets, 0 posts, 0 youtube. Index: 159 total.

**15:14 /wiki-check** — 1 RU section added (mythos), 1 broken link fixed (aisi-mythos-cyber self-link → glasswing), 18 orphans connected, 1 duplicate deleted (hermes 1.md). Vault: 159 entries, 0 broken links, 0 orphans.

---

## 2026-05-25

**07:58 /wiki-reddit** — 14 subs scanned (ollama 429 both tries). 3 entries created: claude-code-remote-system-prompt-injection (news), cate-canvas-ide (tools), yet-another-statusline (tools). All other posts already processed. Index: 162 total.

**08:58 /wiki-hackernews** — 30 articles fetched, 1 qualified (score 2), 0 entries created. 1 queued to links.md: NDR + agentic AI (score 2, vendor blog). 9 already in cursor. Index: 162 total.

**08:59 /wiki-inbox** — 0 created, 0 updated, 5 skipped. Clippings/twitter/posts/youtube all empty. 4 tweet URLs still blocked (retry 2026-05-26). THN NDR article skipped (score 2 vendor blog). Index: 162 total.

**08:59 /wiki-links** — 0 created, 0 updated, 4 skipped. All items are X.com tweets — web-reader rate-limited until 2026-05-26 02:29 UTC. Retry tomorrow. Processed URLs: 380.

---

## 2026-05-26

**16:33 /wiki-links** — 4 tweets processed, 3 entries created: claude-code-9-mistakes-wasting-tokens (tips), microsoft-agent-governance-toolkit (tools), dotnet-agent-skills (tools). 1 skipped (already exists: claude-code-prompting-era). Index: 165 total.

**16:53 /wiki-products** — 7 product index pages created: product-github-copilot (tools), product-claude-code (agents), product-zai-glm (models), product-deepseek (models), product-ollama (tools), product-hermes-agent (agents), product-llm-wiki (concepts). Products.md updated with links. Index: 172 total.

**17:05 /wiki-hackernews** — 8 articles fetched, 0 created, 8 skipped (generic cybersecurity). Claude Mythos already in wiki. All URLs marked processed.

**17:05 /wiki-update** — 1 entry updated: github-copilot-pricing-exodus (news) — added 3 Reddit sources ( cost spiral, lawsuit thread, cost projection). 2 new URLs added to processed_urls.json.

**17:08 /wiki-reddit + /wiki-hackernews** — 13 subs scanned. 2 entries created: codex-vs-claude-code-may-2026 (tips), ollama-cloud-quality-concerns (news). 1 entry updated: github-copilot-pricing-exodus (news). HackerNews: 8 articles fetched, 0 new entries (1 already processed, 7 skipped - not AI-relevant). Index: 174 total.

---

## 2026-05-28

**09:15 /wiki-inbox** — 3 links processed, 2 tweets skipped. 2 created: dictionary-of-ai-coding (tools), anthropic-skills-building-guide (tips). 1 updated: claude-code-handoff-prototype-skills (tips, +smart-zone/dumb-zone). Index: 176 total.

**10:38 /wiki-reddit** — 14 subs scanned. 1 entry created: openai-daybreak-cyber-defense (news). 26 posts examined across subs, rest already processed or low-quality. Index: 177 total.

**10:44 /wiki-hackernews** — 3 articles fetched, 2 qualified (1 crypto malware skipped). 2 entries created: claude-security-plugin-code-review (news), malware-slop-npm-claude-user-directory (news). Index: 179 total.

**11:22 /wiki-check** — 0 RU sections missing (179/179 complete). 3 broken links fixed: claude-code-usage-limits slug, kytmanov stub replaced, local-rag deduplicated. 3 orphans connected: anthropic-skills-building-guide, dictionary-of-ai-coding, openai-daybreak-cyber-defense. Vault: 179 entries, 0 broken links, 8 orphans remaining.

---

## 2026-06-04

**17:24 /wiki-reddit** — 14 subs scanned, 0 new qualifying posts (cursors current from earlier today). Index: 179 total.

**17:28 /wiki-hackernews** — 5 articles fetched, 2 qualified (2 skipped: vendor piece + geopolitical). 2 entries created: claude-code-github-action-prompt-injection (news), http2-bomb-openai-codex-discovery (news). Index: 181 total.

**17:31 /wiki-reddit** — 14 subs attempted, 0 posts fetched — Reddit API returning 403 (unauthenticated access blocked). OAuth credentials needed in .env. Index: 181 total.

---

## 2026-06-05

**13:20 /wiki-reddit** — 14 subs via RSS fallback (JSON API 403). 1202 posts scanned, 4 entries created: claude-opus-4-8-release (news), agent-lifespan-agingbench (concepts), dual-brain-agentic-protocol (tools), noosphere-ai-memory (tools). 4 URLs queued to inbox/links.md. Index: 185 total.

---

## 2026-06-06

**09:47 /wiki-reddit** — 14 subs via RSS, 2nd 2-week pass. 2 new entries from newer threads: kimi-code-cli (tools), ab-method-workflow (tools). 7 model/tool URLs queued to inbox. Index: 187 total.

**10:05 /wiki-inbox** — 5 entries created: ilnamiqui-session-memory (tools), atomicmemory-semantic-memory (tools), awesome-agent-vault-credentials (tools), nvidia-sol-execbench (concepts), zsh-opencode-plugin (tools). 1 skipped (Supra-50M low quality), 5 Reddit blocked by robots.txt. 0 clippings/tweets/posts/youtube (all already processed). Index: 192 total.

**10:57 /wiki-config** — Added r/DeepSeek and r/Qwen_AI to monitored subreddits (now 16). Updated CLAUDE.md, AGENTS.md, README.md, topics.md, wiki-reddit.md, wiki-pipeline SKILL.md, inbox_coordinator.py. Both verified fetchable via RSS.

**10:57 /wiki-reddit** — 14 subs scanned (RSS), 6 qualifying posts. 4 entries created: redactable-pii-protection (tools), shrimp-coding-agent (tools), llm-wrapper-performance-gap (tips), minimax-m3-coding-model (models). 2 updated: kimi-2-6-vs-glm-5-1-agent-reliability (models), github-copilot-pricing-exodus (news). Index: 196 total.

**10:59 /wiki-reddit** — 14 subs scanned (RSS fallback, JSON API 403). 4 entries created: redactable-pii-protection (tools), shrimp-coding-agent (tools), llm-wrapper-performance-gap (tips), minimax-m3-coding-model (models). 2 updated: kimi-2-6-vs-glm-5-1-agent-reliability (models), github-copilot-pricing-exodus (news). Index: 196 total.

**11:16 /wiki-reddit** — 3 entries created: ashub-deepseek-coding-agent (tools), tool-calling-loop-management (tips), custom-agent-loop-vs-sdk (agents). Index: 199 total.

**11:22 /wiki-hackernews** — 5 entries created: claude-code-github-action-flaw (news), ai-agent-ffmpeg-zero-days (news), chatgpt-lockdown-mode (news), gemini-android-notification-hijack (news), smart-tv-ai-scraping-proxies (news). Index: 204 total.

**11:36 /wiki-update** — Updated llm-wiki-chinese-models-comparison: added Qwen3.7 Max (BenchLM 91), MiniMax-M3, MiMo-V2.5-Pro benchmarks. Corrected pricing, added Art.Analysis scores, LM Arena rankings, 7 new sources.

---

## 2026-06-11

**09:22 /wiki-reddit** — 16 subs scanned, 10 entries created: claude-fable-5-ai-research-restrictions (news), huawei-deepseek-v4-ascend-training (news), opencoderag-rag-plugin (tools), mimo-code-xiaomi-opencode-fork (tools), amore-opencode-research-plugin (tools), oc-claw-agent-monitor (tools), self-improving-gui-agent (agents), openclaw-free-hosting (news), small-models-clean-architecture (tips), mtp-hardware-dependent-speedup (tips). 8 URLs queued. Index: 214 total.

**09:32 /wiki-hackernews** — 9 articles fetched, 2 qualified, 2 entries created: claude-fable-5-mythos-5-release (news), self-replicating-ai-worm-local-models (news). Index: 216 total.

**20:24 /wiki-reddit** — 16 subs scanned (2 rate-limited), 302 posts fetched, 6 entries created: ship-skills-claude-code-pipeline (tools), grind-claude-code-nonstop (tools), turbo-graph-rag-memory (tools), temenos-agent-sandbox (tools), nex-n2-pro-mini-qwen-finetune (models), pyrecall-catastrophic-forgetting (tools). Index: 222 total.

**20:26 /wiki-hackernews** — 12 articles fetched, 2 new qualified, 1 entry created: openclaw-agent-security-vulnerabilities (news). 10 skipped (already processed or no AI angle). Index: 223 total.

---

## 2026-06-14

**09:55 /wiki-update** — Added GLM-5.2 and Kimi K2.7 Code entries; updated llm-wiki-chinese-models-comparison with new context, pricing, benchmark tables. Index: X total.

**09:57 /wiki-create-core-stubs** — Created 4 bilingual entries: opencode (tools), claude-code (tools), glm-5-1 (models), kimi-k2-6 (models). Added 9 source URLs to processed_urls.json; critical broken links resolved.

**10:14 /wiki-update** — Added detailed pricing sections to GLM-5.2 and Kimi K2.7 Code entries; enriched pricing tables and notes in llm-wiki-chinese-models-comparison (EN+RU).

**10:44 /wiki-reddit** — 16 subs (RSS fallback, score-filter applied manually), 20 entries created: heimdall-ai-security-scanner (tools), claude-agent-sdk-credit-june-2026 (news), glm-5-2-release (news), kimi-k2-7-code-release (news), fable5-mythos5-export-control-suspension (news), verifier-tax-tool-agent-safety (concepts), turbo-llm-launcher (tools), opensddrag-mcp-harness (tools); 5 updated. 8 URLs queued. Index: 249.

**10:44 /wiki-index** — index.md rebuilt (249 entries, 38 orphans flagged), 4 topic indexes regenerated, relations rebuilt for 249 entries.

**10:55 /wiki-hackernews** — 30 articles fetched, 5 qualified, 3 entries created: langgraph-rce-vulnerability (news), agentjacking-attack (news), google-gemini-smishing-lawsuit (news). 2 already processed. Index: 252 total.

**17:30 /wiki-check** — 0 RU sections missing (all complete), 24 broken links fixed (7 entries created + 10 rewritten as plain text), 39 orphans connected (40→1). Vault: 252+ entries.

---

## 2026-06-29

**16:04 /wiki-reddit** — 16 subreddits scanned (all via RSS fallback; JSON API 403). 12 entries created: deepseek-v4-peak-pricing (news), dspark-speculative-decoding (concepts), qwen-agentworld (models), context-warp-drive (tools), world-model-mcp (tools), moe-watcher-modifier (tools), orkestra-multi-cli (tools), oxidellm-ollama-gateway (tools), unify-chat-provider-copilot-byok (tools), ai-rules-modular-instructions (tools), deepseek-flash-glm-advisor-config (tips), dual-gpu-subagent-parallelism (tips). 15 external URLs queued to inbox/links.md. Cursors updated for all 16 subs. Index: 271 total.

**16:11 /wiki-hackernews** — 30 articles fetched, 2 qualified (score>=2). 1 entry created: guardian-agents-identity-governance (concepts) — autonomous control layer for AI agent identity governance. 1 skipped: DirtyClone Linux kernel CVE (no AI angle; spurious 'rag' substring match). 0 queued. Cursor + processed_urls updated. Index: 272 total. Topic indexes rebuilt (ai-agents: 95).

**16:15 /wiki-check** — 272 entries scanned: 0 missing RU sections, 0 short RU sections. 0 broken links. 8 orphans found, 8 connected via backlinks to semantically close entries (ai-rules<-memory-skills, context-warp-drive<-agent-harness-engineering, orkestra+dual-gpu<-agent-orchestration, guardian-agents<-iam-risks, oxidellm<-product-ollama, product-llm-wiki<-llm-wiki-pattern, unify-chat-provider<-github-copilot-cli). Vault now: 0 orphans, 0 broken, 0 isolated. Index: 272.

**16:45 /research** — Updated llm-wiki-chinese-models-comparison: GLM-5.2 full benchmarks now published (753B params, beats GPT-5.5 on SWE-bench Pro 62.1, FrontierSWE 74.4, Terminal-Bench 81.0 — strongest open-source model globally). Added DeepSeek V4 peak/valley pricing (2x peak hours, mid-July launch). Corrected pricing across providers (MiniMax-M3, Kimi K2.6, GLM-5.2 API, Qwen3.7). Added Qwen3.7 Max full benchmark scores. New long-horizon benchmarks subsection. EN+RU both updated. Index: 272.

**16:49 /edit** — llm-wiki-chinese-models-comparison: added 'Official Provider Pricing (First-Party APIs)' table with confirmed prices from each model creator's own API (DeepSeek api.deepseek.com, Z.AI, Alibaba DashScope, Moonshot, Xiaomi, MiniMax platform.minimax.io). Includes cache-hit rates and context/max-output columns. EN+RU. Index: 272.

---

## 2026-07-01

**15:01 /wiki-reddit** — 16 subs (RSS fallback — JSON API 403, OAuth creds invalid). 12 entries created, 1 updated (glm-5-2). Key items: agentplugins-cross-harness (tools), arc-gate-prompt-injection-proxy (tools), 10x-coding-agent-methodology (tools), opencode-rate-limiter-plugin (tools), browser-snapshot-format-token-cost (research), mothrag-graph-free-multihop (research), reap-coding-agent-benchmark-curation (research), closed-vs-open-model-scaffolding-gap (concepts), local-agentic-web-research-stack (tips), opencode-12m-token-burn (tips), github-copilot-jetbrains-native (news), cerebras-openai-capacity-lockup (news), zai-max-plan-undisclosed-weekly-limit (news). Index: 285 total. 0 orphans, 0 broken links. 22 URLs marked processed (562->584).

**15:11 /wiki-hackernews** — 50 articles fetched, 8 AI/agent-relevant processed. 7 entries created, 1 updated (fable5 export-control lift). Key items: duneslide-cursor-sandbox-escape (news), mcp-tool-poisoning-microsoft (news), guardfall-coding-agent-shell-injection (news), amazon-q-mcp-config-rce (news), bioshocking-ai-browser-credential-leak (news), gpt-5-6-sol-preview (news), deepseek-generated-browser-ransomware (news). Index: 292 total. 0 orphans, 0 broken. 8 URLs marked processed (584->592).

**16:50 research** — Created zcode-zai-agentic-development-environment (research) — deep-dive on Z.ai's desktop ADE: form factor, models/providers, execution modes, AGENTS.md config, pricing, community reception, version history. Bilingual. Researched from official docs (zcode.z.ai) + r/ZaiGLM + HN. Backlinked from product-zai-glm and glm-5-2. Index: 293 total. 0 orphans, 0 broken.

---

## 2026-07-11

**09:12 /wiki-reddit** — 16 subs (RSS fallback). 12 entries created. Key items: hard-gates-over-soft-prompts (tips), mcp-tool-schema-bloat-token-cost (tips), aethereum-multi-session-coordination (tools), packmind-local-second-brain (tools), clifford-control-plane-local-ai (tools), mcpg-postgresql-mcp-server (tools), toolhound-tool-call-failure-taxonomy (research), agentic-safety-vs-textual-safety-mcp-attacks (research), gpt-5-6-pareto-frontier-copilot (models), kimi-k2-5-vs-k2-6-vs-k2-7-code (models), glm-5-2-nested-tool-call-bug (news), skill-md-supply-chain-risks (news). Index: 305 total. 0 orphans, 0 broken. 18 URLs marked processed (592->610).

**12:10 /wiki-hackernews** — 49 articles fetched, 8 AI/agent-relevant entries created. Key items: friendly-fire-ai-code-review-agents-tricked (news), ghostapproval-symlink-coding-agent-flaw (news), ai-coding-agents-triggering-edr-rules (news), github-copilot-dual-behavior-code-bypass (news), gitlost-github-agentic-workflow-leak (news), hallusquatting-ai-hallucination-botnet (news), writer-ai-agent-builder-tenant-token-leak (news), rogue-agent-dialogflow-cx-xss (news). Index: 313 total. 0 orphans, 0 broken. 8 URLs marked processed (610->618).

---

## 2026-08-31

**16:35 /wiki-inbox** — 4 created, 0 updated. Key items: rag-simpler-than-you-think (concepts), mcp-vs-direct-api-debate (concepts), ai-engineer-notebooks (tools), skill-doctor (tools). Clippings/posts/youtube empty; 4 tweets + 8 links blocked by robots.txt/X, requeued. Index: 317 total.

**17:05 /wiki-reddit** — 16/16 subs via RSS (rate-limit retry added to fetch_reddit.py). 1564 posts scanned, 4 entries created: qwen-3-8-flash-next (models), glm-5-3-release (models), openai-huggingface-sandbox-escape (news), openusage-subscription-tracker (tools). 12 URLs queued. Index: 321 total.

---

## 2026-09-02

**07:32 /wiki-inbox** — Full inbox pass (5 parallel research agents). 21 entries created, 1 updated (github-copilot-sdk v0.3.0). clippings: empty. links: 12 fresh + 7 stale backlog processed (4 skips: FastContext withdrawn, cognitor deleted, Memgram stale, sysai off-topic). twitter: 9 queued (2 skips: thin signals). posts: 3 stuck posts moved to Done. youtube: DHH Lex Fridman #501 → dhh-agentic-programming-lex-fridman (people), transcript saved. Key items: anthropic-cost-optimization-cookbook (tips), openai-cursor-model-winddown (news), nvidia-hugging-face-acquisition (news), claude-opus-5-backlash (models), altman-agi-by-end-of-2026 (news), tencent-hy4-preview (news), mcp-stateless-core-spec (news), claude-code-weekly-limits-sep-raise (news), hillock-neurosymbolic-memory (tools), cli-proxy-api (tools). Index: 345 total. 0 orphans, 0 broken links. 38 URLs marked processed (645->680).

**13:06 /wiki-inbox** — Inbox empty — all 5 queues (clippings/links/twitter/posts/youtube) already cleared by previous run. 0 created, 0 updated, 0 skipped. Index: 345 total.

**13:40 /wiki-reddit** — 17 subs (incl. new r/Codex), 140 candidates. 15 entries created. Key items: anywebmcp-webmcp-any-site (tools), polyglot-tolerant-tool-calls (tools), tokenray-cost-dashboard (tools), evoundo-recoverability-self-evolution (research), model-diversity-multi-agent-verification (research), qwen25-coder-mql5-finetune (research), free-api-tiers-coding-agents (research), glm-5-3-flash-vs-deepseek-v4-flash (models), chinese-code-harness-comparison (models), gpt-5-6-three-tier-workflow (tips), qwen38-27b-rtx-5080-tuning (tips), kimi-code-quota-audit (news), ai-agents-top-attack-vector-aug-2026 (news), claude-fable-5-1-ga (news), kimi-k3-reasoning-history-regression (news), kimi-k4-nvidia-chips-rumor (news). Index: 361 total. 0 orphans, 0 broken. 28 URLs marked processed (680->708). 10 URLs queued to links.md.

**16:45 research** — T3 Code article created (tools) + ZCode deep-dive refreshed with September update. t3-code: Theo Browne/Ping.gg 'agent harness control surface' — free OSS GUI+mobile for orchestrating existing agent CLIs (Claude Code, Codex, Gemini CLI, OpenCode), 20k stars in a month, launched Jul 28 2026. ZCode: added v3.3→v3.10.2 changelog (GLM-5.3 era from Aug 14, GLM-5.3-Flash multimodal Aug 26, Goal mode, Remote Control, points-based quota, community sentiment flip), version history + RU sections updated. Index: 362 total. 0 orphans, 0 broken.
