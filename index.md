# LLM Wiki Index
_Last updated: 2026-05-17 | Total entries: 94_

---

## 🧠 Concepts (11)
- [[agent-harness-engineering]] — Agent = Model + Harness: the discipline of designing the scaffolding (prompts, tools, context policies, hooks, recovery paths) around an LLM; a great harness beats a great model with a bad one (O'Reilly 2026, VS Code blog).
- [[agi-impossibility-proof-debunked]] — Guerzhoy (2026) shows Van Rooij et al.'s "Ingenia Theorem" is irreparably broken: the proof's core assumption is unjustified and substituting ImageNet labels produces the same absurd result.
- [[karma-knowledge-graph-enrichment]] — Nine collaborative LLM agents automate KG enrichment: 38,230 entities at 83.1% correctness across 1,200 PubMed articles, 18.6% conflict-edge reduction via multi-layer consensus (NeurIPS 2025).
- [[karpathy-deep-dive-llms]] — Andrej Karpathy's comprehensive, general-audience deep dive into how large language models like ChatGPT are built.
- [[llm-wiki-academic-applications]] — Survey of 5 key papers (KARMA, SurveyGen-I, LightRAG, PARNESS, LLM4SR) showing where academic LLM knowledge-base research stands, where a personal wiki already leads, and 3 concrete feature gaps to close.
- [[llm-wiki-implementations-landscape]] — State of the LLM Wiki ecosystem (May 2026): 30+ implementations, WiCER benchmark finding 53–60% compilation failure rate, two camps (personal PKM vs agent layer), Obsidian debate, productization wave.
- [[llm-wiki-pattern]] — A pattern proposed by Andrej Karpathy where an LLM agent incrementally builds and maintains a persistent, structured knowledge base.
- [[llm4sr-survey]] — LLM4SR is the first systematic survey examining how large language models are transforming the full scientific research lifecycle.
- [[self-guided-self-play]] — SGS adds a Guide role to LLM self-play that prevents Conjecturer collapse; a 7B model after 200 rounds beat a 671B baseline on Lean4 theorem proving.
- [[surveygen-i-scientific-survey]] — Memory-guided long-form survey generation: a terminology memory store prevents re-explaining defined terms across sections and across weekly runs (IJCNLP-AIJLP 2025).
- [[gnosis-mcp-vs-llm-wiki-pattern]] -- Deep comparison: Gnosis MCP (local RAG search, fast factual lookup) vs LLM Wiki (compiled synthesis, small stable corpora) -- token economics, failure modes, hybrid architectures.

---

## 🛠️ Tools (31)
- [[automathkg]] — AutoMathKG is an automated mathematical knowledge graph that uses LLMs and vector databases to build a high-quality, large-scale math KG.
- [[package-hallucination-mcp]] — MCP server that intercepts LLM package recommendations before install runs; catches the ~20% of AI-suggested packages that don't exist on npm/PyPI and are increasingly pre-registered by attackers.
- [[parness-automated-scientific-research]] — End-to-end autonomous scientific research: DAG workflow kernel (YAML-editable), full-text PDF + code-repo indexing, scenario-typed KG retrieval (similar/contradictory/cross-domain/counter-intuitive), Claude Code integration (arXiv 2026).
- [[awesome-agent-skills]] — A community-curated collection of 1000+ agent skills from official engineering teams (Anthropic, Google, Vercel, Cloudflare, Sentry, and more).
- [[claude-code-frameworks]] — The Claude Code community has produced several competing skill frameworks (GSD, Superpowers, Ouroboros, Han) with pre-built skills, agents, and workflows.
- [[cpt-copilot-terminal]] — `cpt` adds an inline `ctrl+k` chat shortcut to any terminal, letting you ask GitHub Copilot questions and get shell commands inline.
- [[dotnet-claude-kit]] — A curated knowledge and action layer that turns Claude Code into a senior .NET 10 / C# 14 expert with 47 skills, 10 agents, and 15 Roslyn MCP tools.
- [[entire-platform]] — Entire is an open-source CLI that hooks into your git workflow and captures full AI agent sessions as "Checkpoints."
- [[freebuff]] — `freebuff` is a 100% free CLI coding agent that lets you choose from top open models including DeepSeek v4 Pro/Flash.
- [[github-copilot-cli]] — GitHub Copilot CLI is a GitHub-aware coding agent that lives in the terminal, letting you move from natural-language requests to pull requests without leaving the command line.
- [[github-spec-kit]] — GitHub's open-source Spec-Driven Development toolkit: constitution → specify → plan → tasks → implement workflow for 30+ AI coding agents.
- [[gnosis-mcp]] — Gnosis MCP is a zero-config local MCP server that gives AI agents hybrid keyword + semantic search over your documentation.
- [[goai-graph-of-ideas]] — GoAI is a system that constructs educational knowledge graphs from AI research papers, capturing prerequisite knowledge paths.
- [[graphify-llm-wiki]] — Graphify is an AI coding assistant skill that applies Karpathy's LLM Wiki pattern to codebases — building a living knowledge graph of any repository.
- [[grobid-pdf-parser]] — GROBID (GeneRation Of BIbliographic Data) is a machine learning library for extracting, parsing, and restructuring raw scientific PDF documents.
- [[han-claude-code-plugin]] — Han is a Claude Code plugin by Test Double that gives solo or small-team engineers access to a swarm of specialist AI subagents.
- [[lightrag-graph-rag]] — LightRAG is a graph-enhanced RAG system that integrates knowledge graph structures into text indexing and retrieval.
- [[llm-wiki-ecosystem]] — A curated map of open-source implementations of Karpathy's LLM Wiki pattern — from simple Obsidian-based local wikis to full agentic pipelines.
- [[llmwiki-open-source]] — An open-source implementation of Karpathy's LLM Wiki pattern: point it at a folder of research files and the local MCP server writes your wiki.
- [[mcp-financial-data-server]] — Equibles is a self-hosted, open-source MCP server that scrapes, stores, and serves financial data to AI agents.
- [[minicheck-fact-verification]] — MiniCheck is an efficient fact-checking system that builds small models (770M parameters) matching GPT-4-level accuracy on grounding verification.
- [[nwave-ai-refactoring-framework]] — nWave is an AI-guided refactoring framework for safely modernizing legacy code in structured micro-steps.
- [[omegawiki-research-platform]] — OmegaWiki is an open-source, wiki-centric full-lifecycle AI research platform by DAIR Lab at Peking University.
- [[orthrus-qwen3-acceleration]] — Orthrus-Qwen3: diffusion attention mechanism achieving up to 7.8× LLM token generation speedup on Qwen3-8B.
- [[poetiq-recursive-self-improvement]] — Poetiq is a Y Combinator-backed startup whose Meta-System uses recursive self-improvement to build and refine coding agents.
- [[react-doctor]] — React Doctor v2 is a zero-config CLI tool that catches bad React code written by AI coding agents.
- [[shokunin-memory-system]] — Shokunin is a persistent memory system for coding agents, maintaining context across sessions.
- [[tencent-db-agent-memory]] — Fully local 4-tier agent memory (symbolic short-term + layered long-term); cuts token use 61% and improves pass rate 51% vs flat vector stores (Tencent, 2026).
- [[visual-explainer]] — An agent skill that replaces ASCII art and terminal tables with styled, self-contained HTML pages with interactive Mermaid diagrams.
- [[wiki-os]] — Wiki OS is a free, open-source browser-based interface for LLM Wiki vaults that displays article graphs, vault statistics, and bilingual entries.
- [[yaro-mathwiki]] — Yaro2709/MathWiki is a hand-curated Obsidian vault containing 730+ atomic mathematical statements (definitions, theorems, proofs).

---

## 🤖 Agents (11)
- [[acdc-agent-centric-development-cycle]] — AC/DC (Agent-Centric Development Cycle) is a framework for restructuring the entire SDLC around AI agents rather than treating agents as add-ons.
- [[claude-code-agentic-loop]] — Claude Code is an agentic assistant built on a three-phase loop — gather context, take action, verify results — powered by Claude models and built-in tools.
- [[claude-code-directory]] — Claude Code reads all configuration — CLAUDE.md, settings, skills, hooks, subagents, rules, and auto memory — from `.claude/` directories.
- [[claude-code-extensions-overview]] — Claude Code's extension layer: persistent context (CLAUDE.md), reusable workflows (Skills), external services (MCP), isolated workers (Subagents), and event automation (Hooks).
- [[claude-code-memory]] — Claude Code persists knowledge across sessions through CLAUDE.md (explicit instructions) and Auto Memory (automatic file-based memory).
- [[claude-code-permission-modes]] — Claude Code's permission modes control how often it pauses to ask approval before editing files or running commands.
- [[how-coding-agents-read-code]] — How AI coding agents actually read code: context window mechanics, chunking strategies, and token budgets in production systems.
- [[llm-wiki-enterprise-patterns]] — How the LLM Wiki 3-layer pattern (raw sources → wiki → schema) scales from personal knowledge management to production enterprise systems.
- [[mythos-cybersecurity-agent]] — Mythos: an AI cybersecurity agent for automated security research and vulnerability analysis.
- [[new-organizational-models-ai-agents]] — Explores how organizations must restructure around AI agents, moving from human-centric hierarchies to human-AI hybrid operating models.
- [[specs-to-production-ai-agents]] — End-to-end workflow for going from a product specification to production software using AI agents as primary implementers.

---

## 🔬 Models (5)
- [[deepseek-v4-vs-opus-kimi]] — Benchmark comparison of DeepSeek V4 Pro, Claude Opus 4.7, and Kimi K2.6 across coding and reasoning tasks.
- [[llm-wiki-chinese-models-comparison]] — Comparison of Chinese LLMs (DeepSeek, Kimi, GLM, Qwen, MiMo) for building Karpathy-style personal knowledge bases, with benchmark scores and pricing.
- [[gpt-vs-glm-5-1-comparison]] — A side-by-side coding comparison of GPT and GLM-5.1 on real tasks, comparing output quality and cost.
- [[llm-wiki-chinese-models-comparison]] — Comparison of Chinese frontier LLMs (DeepSeek V4, Kimi K2.6, GLM-5.1, Qwen 3.5, MiMo-V2.5) for building Karpathy's LLM Wiki: benchmarks, pricing, and task-specific recommendations.
- [[tabpfn-3-tabular-foundation-model]] — TabPFN-3 is the latest generation of Prior Labs' tabular foundation model, scaling to 1M training rows on a single H100.

---

## 📰 News (15, sorted by date descending)
- 2026-05-17 [[codex-on-mobile]] — OpenAI's Codex coding agent became available on iOS and Android, extending agentic coding sessions to mobile devices.
- 2026-05-16 [[github-agentic-developer-certification]] — GitHub announced GH-600 certification for "agentic AI developer" covering multi-agent orchestration, state management, and system design. Launches July 2026.
- 2026-05-15 [[apple-m5-kernel-exploit-ai]] — Security researchers built the first public macOS kernel memory corruption exploit on Apple M5 silicon using AI assistance.
- 2026-05-15 [[arxiv-llm-ban-policy]] — arXiv implements a 1-year submission ban for papers with unchecked LLM-generated errors.
- 2026-05-15 [[fda-ai-clinical-trials]] — FDA uses AI to shorten clinical trial timelines and accelerate drug approval review.
- 2026-05-15 [[figure-ai-03-robot-30-hours]] — Figure AI 03 humanoid robot operates continuously for 30+ hours straight on a real-world task.
- 2026-05-15 [[gen-ai-web-traffic-may-2026]] — Gen AI web traffic update: ChatGPT nears 50% share, Gemini and Claude both rising in May 2026.
- 2026-05-15 [[github-copilot-pricing-exodus]] — GitHub Copilot's shift to usage-based pricing triggers a user exodus to open-source alternatives.
- 2026-05-15 [[openai-100-dollar-tier]] — OpenAI launched a $100/month ChatGPT Pro tier in April 2026, slotting between Plus ($20) and Pro ($200).
- 2026-05-15 [[roo-code-shutdown-roomote]] — Roo Code shuts down after 3 million installs and pivots to Roomote, a remote coding agent product.
- 2026-05-14 [[github-copilot-app]] — GitHub released a standalone desktop application for agent-driven parallel development with GitHub Copilot.
- 2026-05-13 [[figure-ai-team-robots-livestream]] — Figure AI 03 team of humanoid robots shown working together on a livestream.
- 2026-05-11 [[enterprise-gpu-underutilization]] — Enterprises averaging 5% GPU utilization despite millions in investment; inference cost + TCO rose to 41% of AI spend.
- 2026-05-07 [[pinecone-nexus]] — Pinecone announced Nexus, a "compiled knowledge engine" for agents that pre-compiles retrieval at index time.

---

## 💡 Tips (21)
- [[agentic-ai-coding-patterns-tornhill]] — Adam Tornhill's battle-tested patterns for agentic AI coding: speed with quality, context management, and verification loops.
- [[agentic-ai-development-copilot-lessons]] — Practitioner lessons from real-world agentic AI-assisted development using GitHub Copilot CLI on an open-source project.
- [[chorus-multi-model-setup]] — CHORUS: a multi-model coding setup that routes tasks to the best model for each job.
- [[claude-code-deferral-behavior]] — Opus 4.7 task-skipping pattern: when and why Claude Code defers work, and how to prevent it.
- [[claude-code-handoff-prototype-skills]] — Three high-value Claude Code skills: /handoff (session compaction), /prototype (rapid scaffolding), and improve-codebase-architecture.
- [[claude-code-plugins-guide]] — A curated ranking of the most useful Claude Code plugins across official marketplace, community, and partner categories.
- [[claude-code-prompting-era]] — The new prompting era: Claude 4.7 literal execution vs GPT-5.5 autonomous behavior, and what it means for prompt engineering.
- [[claude-code-workflows-best-practices]] — Official best practices for Claude Code: context management, planning, verification, and multi-agent workflows.
- [[cline-roo-alternatives]] — Community recommendations for Cline and Roo Code alternatives in 2026, following their decline.
- [[copilot-cli-telegram-bridge]] — Using Telegram as a mobile front-end for GitHub Copilot CLI via the examon/copilot-cli-telegram-bridge extension.
- [[github-copilot-cli-best-practices]] — GitHub Copilot CLI is a terminal-native agentic coding assistant; best practices for workflow integration.
- [[karpathy-claude-code-guidelines]] — A single CLAUDE.md distilling Karpathy-inspired coding guidelines for Claude Code projects.
- [[llm-assumption-propagation]] — Karpathy's insight: LLMs make wrong assumptions and run with them without checking. How to diagnose, interrupt, and prevent assumption propagation in agentic coding.
- [[llm-assisted-coding-systems-perspective]] — Dragan Stepanović applies systems thinking to LLM-assisted coding: feedback loops, constraints, and emergent behavior.
- [[llm-wiki-scientific-research]] — The LLM Wiki pattern applied to scientific research and academic writing workflows.
- [[llm-wiki-setup-guide]] — Step-by-step guide to building Karpathy's LLM Wiki from scratch: tools, folder structure, and first entries.
- [[mathwiki-improvement-plan]] — Plan for automating and improving the Yaro2709/MathWiki hand-crafted Obsidian math knowledge base with AI.
- [[spec-driven-development-bmad]] — Fabrice Monnier's journey from vibe coding to spec-driven development with BMAD and custom skills.
- [[test-driven-agentic-behaviours]] — Antony Marcano demonstrates applying TDD principles to define and verify agentic AI behaviors.
- [[dynamic-compute-budget-local-llm]] — Test-time compute technique: let a local Qwen-35B model assign priorities to hard problems, then spawn parallel agents — reaching 39.9% on HLE (vs GPT-5.4-xHigh at 41.6%).
- [[xp-practices-ai-assisted-development]] — Paul Hammond argues that Extreme Programming practices (TDD, pairing, small releases) are the missing piece for AI-assisted development.

---

## 👤 People (2)
- [[andrej-karpathy]] — Andrej Karpathy: AI researcher, educator, founding member of OpenAI, former Director of AI at Tesla. Coined Software 2.0, vibe coding, and the LLM Wiki pattern. Founder of Eureka Labs.
- [[matt-pocock-aihero]] — Matt Pocock (aihero.dev): TypeScript educator turned AI practitioner; creator of the viral /grill-me skill (46k+ stars), tracer bullets technique, and codebase-design-for-AI philosophy.

---

## 📅 Digests
_No digests generated yet._

