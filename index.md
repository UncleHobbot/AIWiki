# LLM Wiki Index
_Last updated: 2026-05-15 | Total entries: 39_

> Personal AI knowledge base. Bilingual: EN + RU in every entry.
> Powered by Claude Code · Inspired by Andrej Karpathy

---

## 🧠 Concepts (2)

- [[karpathy-deep-dive-llms]] — Andrej Karpathy's comprehensive deep dive into how LLMs like ChatGPT are built — covering the full training pipeline from pre-training through post-training (RLHF/SFT).
- [[llm-wiki-pattern]] — A pattern where an LLM agent incrementally builds and maintains a persistent, structured wiki from raw source documents — rather than re-deriving knowledge from scratch on every query (as in RAG).

---

## 🛠️ Tools (14)

- [[entire-platform]] — Open-source CLI that captures full AI agent sessions as Checkpoints linked to git commits — trace any commit to the session, prompt, and decisions that produced it. $60M seed, MIT.
- [[gnosis-mcp]] — Zero-config MCP server for searchable documentation: hybrid BM25+semantic search, 10–60× token savings per lookup, SQLite default, no API key. Ships with reproducible benchmarks.
- [[cpt-copilot-terminal]] — Inline `ctrl+k` chat shortcut for any terminal, letting you ask GitHub Copilot questions and get shell command suggestions without leaving your session.
- [[freebuff]] — 100% free CLI coding agent with top open models including DeepSeek v4 Pro/Flash, Kimi K2.6, and MiniMax M2.7 — installed with a single npm command.
- [[github-copilot-cli]] — GitHub-aware coding agent in the terminal, moving from natural-language intent to reviewable diffs and pull requests without leaving the command line.
- [[graphify-llm-wiki]] — AI coding assistant skill (21k+ GitHub stars) that applies Karpathy's LLM Wiki pattern to codebases, building a structured knowledge graph of code architecture.
- [[llm-wiki-ecosystem]] — Curated map of open-source implementations of Karpathy's LLM Wiki pattern, from Obsidian-based local wikis to full research lifecycle platforms.
- [[llmwiki-open-source]] — Open-source implementation of the LLM Wiki pattern: FastAPI + Next.js + stdio MCP server for Claude to read sources and write wiki pages automatically.
- [[mcp-financial-data-server]] — Self-hosted, open-source MCP server that scrapes and serves U.S. financial data (SEC filings, 13F, insider trades, FRED, stock prices) via MCP tools.
- [[orthrus-qwen3-acceleration]] — Parallel diffusion attention head for frozen autoregressive transformers, achieving up to 7.8x tokens/forward with identical output distributions.
- [[poetiq-recursive-self-improvement]] — Y Combinator-backed startup using recursive self-improvement to auto-build optimized harnesses around any LLM for new SOTA coding performance.
- [[react-doctor]] — Zero-config CLI tool that catches bad React code written by AI coding agents — works with Next.js, Vite, and React Native.
- [[shokunin-memory-system]] — Local memory system for AI coding agents using ChromaDB to persist session context across conversations, plus 35 domain-specific skills and 3 MCP servers.
- [[wiki-os]] — Free, open-source browser-based interface for LLM Wiki vaults with knowledge graph visualization, vault statistics, and agent activity display.

---

## 🤖 Agents (2)

- [[llm-wiki-enterprise-patterns]] — How the LLM Wiki 3-layer pattern scales from personal knowledge management to production AI agency operations with 20+ specialized agents.
- [[mythos-cybersecurity-agent]] — Claude Mythos Preview: the first AI to autonomously complete a full 32-step simulated corporate network attack, scoring 83.1% on cybersecurity benchmarks.

---

## 🔬 Models (3)

- [[deepseek-v4-vs-opus-kimi]] — DeepSeek V4 Pro scored 77/100 on a complex workflow backend, landing between Claude Opus 4.7 (91) and Kimi K2.6 (68) in Kilo CLI benchmarks.
- [[gpt-vs-glm-5-1-comparison]] — GPT and GLM-5.1 produce near-indistinguishable coding output for everyday tasks; GLM-5.1 reaches 94.6% of Claude Opus 4.6's coding score at a fraction of the cost.
- [[tabpfn-3-tabular-foundation-model]] — Tabular foundation model scaling to 1M training rows on a single H100 with a single forward pass — no training or hyperparameter tuning required.

---

## 📰 News (11)

- 2026-05-15 [[apple-m5-kernel-exploit-ai]] — First public macOS kernel memory corruption exploit on Apple M5 silicon built with Mythos Preview AI assistance in just five days.
- 2026-05-15 [[arxiv-llm-ban-policy]] — arXiv imposes a 1-year ban on authors whose submissions contain incontrovertible evidence of unchecked LLM-generated content.
- 2026-05-15 [[fda-ai-clinical-trials]] — FDA announced a first-of-its-kind initiative using causal AI to monitor clinical trial data in real time, potentially reducing trial timelines by 20–40%.
- 2026-05-15 [[figure-ai-03-robot-30-hours]] — Figure AI's humanoid robot 03 demonstrated continuous autonomous operation for over 30 hours on a factory floor, including self-charging.
- 2026-05-15 [[gen-ai-web-traffic-may-2026]] — ChatGPT declining from 77.6% to ~50% market share over 12 months, while Gemini surged to 26.7% and Claude grew to 7.95%.
- 2026-05-15 [[github-copilot-pricing-exodus]] — GitHub Copilot's switch to usage-based pricing leaves users facing 15x cost increases, triggering mass migration to alternatives.
- 2026-05-15 [[openai-100-dollar-tier]] — OpenAI introduced a $100/month ChatGPT Pro tier with 5x Codex usage over Plus, directly competing with Anthropic's Claude Max.
- 2026-05-15 [[roo-code-shutdown-roomote]] — Roo Code shuts down after 3 million installs, pivoting to Roomote — a Slack-native cloud-based autonomous coding agent.
- 2026-05-14 [[github-copilot-app]] — GitHub released a standalone desktop app for agent-driven development with parallel workstreams and full PR lifecycle management.
- 2026-05-13 [[figure-ai-team-robots-livestream]] — Figure AI live-streamed three F.03 humanoid robots sorting packages for 8 hours at human-parity speed (~2.6s per package).
- 2026-05-07 [[pinecone-nexus]] — Pinecone launched Nexus, a "compiled knowledge engine" for agents — directly paralleling Karpathy's LLM Wiki concept at production scale.

---

## 💡 Tips (7)

- [[chorus-multi-model-setup]] — Open-source tool orchestrating 2–4 AI coding assistants to review the same code in parallel, catching bugs any single model would miss.
- [[claude-code-handoff-prototype-skills]] — Three high-value Claude Code skills: /handoff compacts sessions, /prototype scaffolds UI/backend, improve-codebase-architecture enables daily PR improvement.
- [[claude-code-plugins-guide]] — Curated ranking of the most useful Claude Code plugins across marketplace, community, and partner categories — sweet spot of 3–5 active plugins.
- [[claude-code-prompting-era]] — Claude Opus 4.7 became more literal while GPT-5.5 became more autonomous — both mean the prompt writer is now the bottleneck, not the model.
- [[cline-roo-alternatives]] — Community guide to alternatives for Cline and Roo Code: Claude Code is the top recommendation, followed by Kilo Code and OpenCode.
- [[copilot-cli-telegram-bridge]] — Send prompts to a running Copilot CLI session from your phone via Telegram for real coding agent work without a terminal.
- [[llm-wiki-setup-guide]] — Step-by-step guide to building Karpathy's LLM Wiki from scratch: tools, folder structure, schema writing, and source ingestion.

---

## 👤 People (0)

_No entries yet._

---

## 📅 Digests

_No digests yet. Run `/wiki-digest` to generate the weekly digest._

---

_Generated by `/wiki-index` on 2026-05-15_
