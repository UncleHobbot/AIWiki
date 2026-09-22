# Typesafe.ai & Jev — Research Notes (2026-09-21)

> Research agent notes for a future wiki entry. All official claims are marked as such; third-party and community statements are marked separately. Inline citations link to the source fetched on 2026-09-21. Raw caches of key pages are in this directory (`typesafe-ai-home.html`, `typesafe-ai-blog-introducing.html`, `typesafe-ai-manifesto.html`, `typesafe-ai-team.html`, `docs-typesafe-*.md`, `hn-49717558-jev-thread.json`, `ddg-jev.html`, `datacamp-jev.html`).

**Disambiguation up front:** This is **TypeSafe AI** (typesafe.ai, San Francisco AI lab, GitHub org `TypeSafeAI`), founded 2024, launched Sept 2026. It has **no connection** to the old "Typesafe" company (the Scala/Typesafe stewardship that became Lightbend in 2016) or to `typesafe.com`, the Typesafe config library, or Lightbend. The name collision is real and will confuse searches; GitHub org is `TypeSafeAI`, website footer says "©2026" and "Version 0.01" ([homepage](https://typesafe.ai)).

---

## 1. Company

- **Name:** TypeSafe AI; site header "TypeSafe AI", tagline "machine-native intelligence infrastructure for automation" ([homepage](https://typesafe.ai)).
- **Founded:** 2024 (not 2026 — it spent ~2 years in stealth before launch). [Wikipedia: Jev (AI model)](https://en.wikipedia.org/wiki/Jev_(AI_model)); TechCrunch says founder "left OpenAI two years ago" ([TechCrunch, Tim Fernholz, 2026-09-18](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)). Emerged from stealth **September 15, 2026** [Forkast](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/).
- **Location:** San Francisco ("Made in SF. With Love." — [homepage](https://typesafe.ai)); office near Embarcadero station, in-person 5 days/week ([team page](https://typesafe.ai/team)).
- **Founders** ([team page](https://typesafe.ai/team), corroborated by [Forkast](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/) and [Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))):
  - **Diogo Almeida — CEO.** Team page: "co-invented RLHF and InstructGPT, the methods that lead to ChatGPT and GPT4"; also credits Google Brain. TechCrunch: spent ~4 years at OpenAI on RLHF, InstructGPT, ChatGPT, GPT-4.
  - **Erik Gafni — CTO.** Repeat founder (Ravel, multi-modal AI for DNA sequencing); early employee at Invitae and Freenome.
  - **Sasha Sheng — COO.** Former research engineer, Meta/FAIR; NeurIPS/ECCV publications.
- **Funding:** **$40M seed led by DCVC**, at a reported **~$200M valuation** (Forbes-reported) ([Forkast](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/); [Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model)) citing Forbes 2026-09-15; The Register also says "a startup with $40 million in funding" ([The Register, Claburn, 2026-09-16](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711))). No investors named on the team page ("top-tier investors", unnamed).
- **Not Y Combinator:** ycombinator.com/companies/typesafe returns 404 (checked 2026-09-21).
- **Team claims:** drawn from OpenAI, Google Brain, Meta/FAIR, Stripe, Airbnb, Plaid, Docker; "Build Prod, Not God" motto ([team page](https://typesafe.ai/team)). TechCrunch: "half of our company" is a synthetic-data lab.
- **Contacts/channels:** hello@typesafe.ai; X [@typesafeai](https://x.com/typesafeai); [LinkedIn](https://www.linkedin.com/company/typesafe-ai/); hiring on [Ashby](https://jobs.ashbyhq.com/typesafe-ai) ([homepage](https://typesafe.ai)).

## 2. What Jev is (plain terms)

Jev is a hosted API model that answers narrow questions about a chunk of text/data you send it — but instead of writing prose, it returns **typed answers with probability distributions and a confidence score**, designed to be branched on in code. You send one `state` (a string, JSON object, or array of strings) plus any number of named questions; all questions are answered in a single parallel pass. There are three question types ("primitives"):

- **Choice** — pick one of up to 255 options; returns `choice`, per-option `probabilities`, `confidence`.
- **Score** — rate the state against 2–10 ordered levels ("legend"); returns score, probabilities, confidence.
- **Noul** — a yes/no question; returns a 0–1 probability of "yes" (no separate confidence field).

([docs introduction](https://docs.typesafe.ai/introduction), [primitives](https://docs.typesafe.ai/primitives), [The Register](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711), [flaviocopes deep dive](https://flaviocopes.com/jev/))

It **cannot generate text at all** — no chat, no code, no free-form output. TypeSafe brands it the first of a class of "**System One Models**" (Kahneman's fast/intuitive System 1 vs. deliberative System 2), positioned as the thing you call inside the "inner loop" of software instead of paying an LLM to classify/route/score with generated text. One commenter's shorthand that matched the docs' own framing: "a smart if statement" ([flaviocopes](https://flaviocopes.com/jev/), [manifesto](https://typesafe.ai/manifesto)).

**Naming:** Jev is named for economist **William Stanley Jevons** and the **Jevons paradox** — cheaper intelligence should drive *more* total consumption ([blog launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)).

## 3. How it works (as far as public info goes)

- **API:** single endpoint `POST https://api.typesafe.ai/v1/systemone`, Bearer auth; `model` field selects variant ([API reference](https://docs.typesafe.ai/api), cached at `docs-typesafe-api.md`). Example request/response shapes in [flaviocopes](https://flaviocopes.com/jev/).
- **Models/versions:** current release `jev-1.13.0` (stable); aliases `jev-latest`, `jev-preview` ([docs Models](https://docs.typesafe.ai/models), cached at `docs-typesafe-models.md`). The homepage footer says "Version 0.01" for the product overall.
- **Limits:** text-only input (no image/audio/video — pre-process to text); 64k-token total context, of which `state` + longest question ≤32k; rate limits 250,000 tokens/sec and 1,200 requests/min, "adjusting dynamically… serving a very large volume of demand" ([docs Models](https://docs.typesafe.ai/models)). Error codes 401/422/429/529 ([flaviocopes](https://flaviocopes.com/jev/)).
- **Parallelism model:** state is ingested once and every question is evaluated "in parallel and in isolation" — adding questions doesn't slow responses or cause context-rot between questions ([docs introduction](https://docs.typesafe.ai/introduction)). Outputs have cardinality ≤255; higher-cardinality uses a two-stage score-then-choose ([launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)).
- **Confidence:** every Choice/Score answer carries a 0–1 confidence derived from the shape of the probability distribution (demo formula for 3 options: `(3 × max_prob − 1) / 2`). Docs are explicit that there are **no stated calibration guarantees** and you may substitute your own definition. Prescribed pattern: high confidence → act; medium → confirm/review; low → route to human. Example thresholds in docs: `< 0.5 → human review`, `> 0.9 required for destructive actions` ([docs Confidence](https://docs.typesafe.ai/confidence)).
- **Training:** transformer-based ([TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/), [Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))), trained **exclusively on synthetic data**, with a proprietary method called **RLCD — Reinforcement Learning for Calibrated Decisions** (optimize probabilities against outcomes rather than human preference). A parallel sampler produces all outputs in one pass instead of autoregressive token generation ([launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)).
- **Architecture is secret.** No paper, no weights, no parameter count. TechCrunch: "outsiders suspect it's built on an open-weight LLM." HN commenters noted docs imagery shows a pre-trained base model + RLCD post-training, which contradicts the "not an LLM" marketing ([HN thread](https://news.ycombinator.com/item?id=49717558), comment by `mortsnort`; `paraschopra` estimated ~3B params from the pricing).
- **Documented weaknesses** (docs own "jaggedness" page + [flaviocopes](https://flaviocopes.com/jev/) summary): literal instruction reading (negations), no math/counting/date arithmetic, scores aren't measurements, context rot on large states, adversarial text in state can steer answers, typed output ≠ correct answer.
- **SDKs:** Python (`typesafe-sdk`, sync+async), JavaScript/TypeScript (`@typesafe-ai/sdk`, Node 20+), Vercel AI SDK provider (`@ai-sdk/typesafe-ai`, gateway id `typesafe-ai/jev`), plus an "agent skill" for Claude Code/Codex ([docs llms.txt index](https://docs.typesafe.ai/llms.txt), [flaviocopes](https://flaviocopes.com/jev/)). Console at [console.typesafe.ai](https://console.typesafe.ai).

## 4. Claims & benchmarks

All numbers in this section are **official TypeSafe claims** unless marked independent:

- **Headline:** "193.6x Faster, 444.6x Cheaper" than LLMs on their workflow benchmarks; demo comparison on homepage: TypeSafe **$0.000081 / 0.114s** vs. LLM **$0.013880 / 8.566s** (baseline named as OpenAI's GPT-5.6 Terra in [The Register](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711)). Blog frames these as upper-end estimates; general ranges claimed 40–200x faster / 40–400x cheaper ([launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))).
- **Latency:** 70–500ms end-to-end vs. 3–329s for frontier LLMs (the LLM side includes long reasoning runs — see critique below).
- **Accuracy:** ~67.8% on their internal four-workflow benchmark, claimed comparable to GPT-5.6 Terra ([Forkast](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/)); blog claims Jev "owns the Pareto frontier for almost 2 orders of magnitude."
- **Methodology (from the launch blog):** models run identical compute graphs ("workflows"); reference answers = **average of GPT-6 Astra and Claude Fable 5.1 outputs** (not ground truth). Admitted caveats in the blog itself: workflows were written by TypeSafe's own capabilities team (possible bias); benchmarks run from West Coast laptops; LLM baseline numbers pulled via OpenRouter (possible routing bias); the "0% type-error rate" is guaranteed by schema constraints, not measured; and they "cannot prove the price is unsubsidized."
- **Demos:** Jev playing Doom from structured game-state text (~10 queries/sec, ~$7/hour); Wikiracing ([launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [The Register](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711)).
- **"Zero hallucinations":** the claim means outputs are schema-constrained (a wrong-but-valid answer is still possible). The Register called the framing "unfair"; MarkTechPost and HN made the same point.

**Independent checks:**

- **Every (every.to)** reportedly found Jev **~25x faster and ~580x cheaper than Claude Fable 5.1** on one extraction task (0.35s vs. 8.83s per passage) — cited by [Forkast](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/); the original every.to article could not be located directly (search engines returned nothing; see §9), so treat as second-hand.
- **Vercel** engineer Pranit Sharma: replacing a "ChatGPT Luna 5.6" classifier with Jev gave **5–18x faster** results with greater accuracy; Vercel CEO Guillermo Rauch reported **18x faster p95** than GPT Luna and more accurate ([TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/), [MarkTechPost](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/)).
- **Bryo AI** CTO Nikhil Mudholkar: vs. Gemini for email classification, Gemini slightly more accurate but **10–20x more expensive** ([TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)).
- **Bartosz Mikulski's pre-registered experiment** ([mikulskibartosz.name](https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew)): 400 Quick-Draw! sketches serialized as SVG text — Jev ~35% correct vs. Sonnet 5 on the real image ~91% (Sonnet on the same SVG: ~57%; Jev on base64: ~9%, chance-level; 209/400 answers were "airplane"). Conclusion: Jev extracts real signal from text but is far from vision models — consistent with its text-only design.

## 5. Pricing

- **$42 per billion input tokens** ($0.042 per million) — homepage badge "Jev.Cost: $42/Btok"; **output tokens free** ("too cheap to meter") ([homepage](https://typesafe.ai), [docs Models](https://docs.typesafe.ai/models), [launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)).
- Claimed "**238x cheaper than Claude Fable 5.1**" on input price ([homepage](https://typesafe.ai), [The Register](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711)). Claimed LLM input range for comparison: $0.20–$10/MTok.
- Worked example: a ~300-token ticket ≈ $0.0000126, i.e. **$1.26 per 100,000 classifications** ([flaviocopes](https://flaviocopes.com/jev/)). Forkast cites "~$0.0004 per decision" in one framing.
- The company's own FAQ concedes prices **may be subsidized** during early access and "cannot prove the price is unsubsidized" ([homepage FAQ](https://typesafe.ai), [launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)).

## 6. Applications / intended use cases

From docs use-case map + cookbooks ([docs index](https://docs.typesafe.ai/llms.txt)) and press:

- **Agent infrastructure:** tool-call gating, intent routing (deterministic code vs. LLM vs. human), guardrails/jailbreak screening, monitoring LLM agents, model routing (Armin Ronacher's use cases, [TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)).
- **Document/data pipelines:** RAG passage filtering & injection detection, citation checking, BM25 re-ranking (top-1 5%→18% in their legal-query cookbook), entity alignment, extraction cascades ("SDE cascade"), date extraction, hierarchical classification (75 SEC industry groups).
- **Ops:** support-ticket routing (canonical example in [The Register](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711): billing 0.08 / technical 0.85 / sales 0.07, confidence 0.82), email triage, content moderation, "Luna classifier" replacement at Vercel.
- **Fun/edge:** the Doom bot, smart-home assistant demo, Home Assistant integration, StarCraft play, live community playground ([docs demos](https://docs.typesafe.ai/demos), [MarkTechPost](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/), [GitHub TypeSafeAI/typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground)).
- Docs repeatedly frame it as *composable infrastructure*: "keep code in control, delegate narrow decisions" ([how-to-build](https://docs.typesafe.ai/concepts/how-to-build-with-system-one)).

## 7. Reviews & community reception

Independent coverage exists in volume — this is not a zero-coverage launch.

**Hacker News** — ["Introducing System One Models and Jev"](https://news.ycombinator.com/item?id=49717558): **1,941 points, 507 comments** (2026-09-15; full JSON cached at `hn-49717558-jev-thread.json`). Representative comments:

- `jacobgold` (11 replies): "genuinely interesting and new," but "the speed comparison seems misleading?… Jev can only generate structured output… And 'can't hallucinate' seems wrong? Sure, it can't emit an invalid type, but it can still emit a completely wrong valid value."
- `zmmmmm`: "The eval is baffling… they don't compare to [the correct graph], they compare to the average of the smartest models… even on this hand constructed eval, the first plot is showing Jev at less than Sonnet 5 accuracy."
- `ramon156`: "all claims just sound like marketing terms… '70-500ms vs 3-329 seconds' are apples-to-oranges… Nonetheless i want this to be true." (Later edited to praise the manifesto.)
- `mortsnort`: "I am confused why they say it is not an LLM and then in the documentation it is shown as being an LLM derivative."
- `paraschopra`: "likely… a tiny transformer… targeted on distillation of logprobs… Astra estimates the model to be 3bn parameters. One could replicate this by post training Qwen… I expect people to do so soon!"
- `abeppu`: the "vs Claude" framing is misleading; you'd use Claude to *write* your Jev configs.

Other HN submissions: [TechCrunch repost](https://news.ycombinator.com/item?id=49763045) (5 points, 0 comments), ["TypeSafe's Jev Can't See" experiment](https://news.ycombinator.com/item?id=49768633) (3 points), [forkast repost](https://news.ycombinator.com/item?id=49761730), and a same-day clone ["Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev" (von)](https://github.com/wfzyx/von) (2026-09-21).

**Clone/derivative ecosystem within one week** (both flattery and moat-skepticism):

- [wfzyx/von](https://github.com/wfzyx/von) — "Sub-15ms, non-autoregressive, local drop-in alternative."
- [r-ms/mini-jev](https://github.com/r-ms/mini-jev) — "Jev implemented on top of an LLM locally."
- [TitovDigital/kbai-skill](https://github.com/TitovDigital/kbai-skill) — "Open-Source Alternative to TypeSafe.ai" (Show HN).
- [HF space: parallel-constrained-decoding](https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding) — "Jev Open Source Alternative Qwen-2.5-1B-RLCD."
- [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) (2,965 stars) — "Semantic ifs from open models… Independent; not affiliated with Jev or TypeSafe."
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) (901 stars), [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) (754), [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) (615), [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) (424).
- [Cua's Show HN: CUA-S1](https://github.com/trycua/cua) — a 706k-param specialist model "built from ideas and code in jevlike"; on their form task it scored 99.7% vs. hosted Jev's 83.6%, at 7–9ms local vs. 260–280ms hosted per call. (Specialist-vs-general comparison, but notable.)
- Official org [github.com/TypeSafeAI](https://github.com/TypeSafeAI): 6 repos (playground with 110 use cases, typesafe-router, typesafe-ui, clarity-judge, community-blog) — docs-first, no model code.

**Press:**

- [TechCrunch — Tim Fernholz, 2026-09-18](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/): profile of Almeida; "demand was so high the company briefly couldn't serve its API"; customer quotes above; Ronacher (Earendil, creator of Flask): Jev "delegates the hallucination problem a little bit to the user" (you pick the confidence thresholds).
- [The Register — Thomas Claburn, 2026-09-16](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711): wry/skeptical — "hallucination-free" is unfair since structured outputs can still be wrong; the Jevons-paradox bet assumes a token market as broad as energy, "unproven given surveys showing many people avoid or don't use AI tools"; closing drone-targeting jab.
- [Forkast — Lena Park, 2026-09-17](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/): funding details, Every.to check, notes no named customers or revenue at launch.
- [MarkTechPost — Asif Razzaq, 2026-09-19](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/): standard tech-press recap; flags vendor-run benchmarks and subsidized-price admission; lists community projects (jev-guard, Postgres filtering, Home Assistant, StarCraft).
- Also reported (per [Wikipedia's references](https://en.wikipedia.org/wiki/Jev_(AI_model)), not fetched directly): Forbes (funding/valuation, 2026-09-15), SiliconANGLE (2026-09-16), The Rundown AI (2026-09-16), TechStock² (2026-09-17 — notes the 445x cost claim is self-tested).
- [flaviocopes.com deep dive](https://flaviocopes.com/jev/) (updated 2026-09-21): most thorough practitioner explainer; cautiously optimistic, plans shadow-mode adoption "one branch at a time"; "most demos won't survive real traffic."
- [DataCamp explainer](https://www.datacamp.com/blog/system-one-models-jev) exists but was blocked by Cloudflare (HTTP 403 on fetch).

**Reddit:** search blocked on both www.reddit.com and old.reddit.com (non-JSON/empty responses) — no data; unresolved.
**Product Hunt / X:** not checked (time-boxed). X account exists at [@typesafeai](https://x.com/typesafeai).
**SEO squatter sites to ignore:** jevtypesafeai.com, jevtypesafe.org, jevai.org, jevai.net are third-party "community"/SEO sites, not official (found via DuckDuckGo results).

## 8. Critical assessment

**Verdict: a real, funded, shipping product — not satire.** Evidence: (1) $40M seed led by DCVC reported by multiple outlets with a Forbes-cited ~$200M valuation; (2) named founders with checkable records (Almeida's RLHF/InstructGPT role is reported by TechCrunch's Tim Fernholz, a longstanding AI reporter); (3) a live public API with real docs, three SDKs, rate limits, changelogs, a Vercel AI SDK provider, and a GitHub org; (4) named customers quoted by TechCrunch (Vercel, Bryo AI); (5) a huge organic HN thread (1,941 points) and a within-a-week clone ecosystem — the opposite of a parody pattern. The bold claims ("zero hallucinations," "Claude Fable 5.1") are real marketing claims the company makes, but its own blog/FAQ attach explicit caveats to them, which satire does not do.

**Claims vs. evidence:**

- **Verifiable/credible:** price, latency, API behavior (docs are concrete and testable); the cost-per-classification math is arithmetically sound; independent spot-checks (Every.to via Forkast, Vercel, Bryo) confirm large speed/cost gains on narrow structured tasks — roughly 18–25x in the field vs. claimed peaks of ~194x.
- **Contested marketing:** "193.6x faster / 444.6x cheaper" are self-run peaks; the benchmark's reference answers are *other LLMs' averaged outputs*, not ground truth; workflows authored by TypeSafe's own team; company admits results are the high end and pricing may be subsidized. "Zero hallucinations" = schema conformance only (wrong-but-typed answers possible) — The Register, HN, and MarkTechPost all flagged this. "Not an LLM" is contested: transformer-based, suspected open-weight base + RLCD post-training (TechCrunch sourcing; HN commenters citing docs imagery).
- **Open questions:** architecture/paper undisclosed; no weights or self-hosting; no published independent broad benchmark; moat unclear given the clone wave (SemIf, von, mini-jev, CUA-S1); the Jevons-paradox growth bet is speculative (The Register).

**Name collision:** significant for any wiki entry — "Typesafe" is still strongly associated with the Scala company (Lightbend) and the `typesafe.com`/Config library. Use "TypeSafe AI" + typesafe.ai consistently and disambiguate explicitly.

## 9. Source list

**Fetched successfully (primary):**
- https://typesafe.ai — homepage: thesis, headline metrics, pricing badge, FAQ topics, links (cached: `typesafe-ai-home.html`)
- https://typesafe.ai/blog/introducing-system-one-models-and-jev — launch post by Diogo Almeida: architecture, RLCD, benchmark methodology + self-admitted caveats, naming, demos (cached: `typesafe-ai-blog-introducing.html`)
- https://typesafe.ai/blog/bitterest-lesson — "task > data > compute > algorithms"; InstructGPT argument (no cache; summarized via WebFetch)
- https://typesafe.ai/manifesto — "Composable AI: Build Prod, Not God"; three-step plan; 3% TFP goal (cached: `typesafe-ai-manifesto.html`)
- https://typesafe.ai/team — founder bios, culture, office (cached: `typesafe-ai-team.html`)
- https://docs.typesafe.ai/ + /llms.txt — full docs index: primitives, patterns, 19 cookbooks, SDKs, agent skill
- https://docs.typesafe.ai/confidence — confidence mechanics, thresholds, example code
- https://docs.typesafe.ai/models, /api, /concepts/system-one, /concepts/use-case-map — cached as `docs-typesafe-*.md`
- https://console.typesafe.ai — linked from homepage (pricing details mirrored in docs; not separately fetched)

**Fetched successfully (third party):**
- https://en.wikipedia.org/wiki/Jev_(AI_model) — founding 2024, funding, criticism, reference list
- https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/ — Fernholz profile, customers, quotes
- https://www.theregister.com/ai-and-ml/2026/09/16/typesafe_ai_debuts_model_for_machines_that_plays_doom/5296711 — Claburn skeptical writeup
- https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/ — $40M DCVC seed, ~$200M valuation, Every.to check
- https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/ — recap + community projects
- https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew — independent pre-registered experiment
- https://flaviocopes.com/jev/ — practitioner deep dive (code, limits, pricing math)
- https://hn.algolia.com/api/v1/search?query=… and /items/49717558 — HN discovery + full thread (cached: `hn-49717558-jev-thread.json`)
- https://api.github.com/users/TypeSafeAI (+ /repos), https://api.github.com/search/repositories?q=jev+typesafe — org + ecosystem repos
- https://html.duckduckgo.com/html/?q=… — discovery of Register/DataCamp/Wikipedia/squatter sites (cached: `ddg-jev.html`)
- https://www.bing.com/search?q=every.to+jev+typesafe — no useful results

**Failed / blocked:**
- https://www.reddit.com/search.json and https://old.reddit.com/search.json — blocked (non-JSON/empty); **no Reddit data**
- https://www.datacamp.com/blog/system-one-models-jev — HTTP 403 Cloudflare (article exists; cached challenge page only: `datacamp-jev.html`)
- https://www.ycombinator.com/companies/typesafe — 404 (not a YC company)
- Every.to original test article — referenced by Forkast but not locatable via DDG/Bing; treat the 25x/580x figure as second-hand
- https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai — body is JS-rendered; only metadata extracted (title + date Jun 19, 2026; cached shell: `typesafe-ai-blog-too-good.html`)
- Product Hunt, X, LinkedIn, Crunchbase — not attempted/expected to block
