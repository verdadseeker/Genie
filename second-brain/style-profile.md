# Style Profile — Manish

> Derived from seed notes: *AI Agentic Development (Jan course)* + *Great Ideas / Days 12–15*.
> Source playlist: https://www.youtube.com/watch?v=Hl7v0jMwglE&list=PLzyW-XtBCYd5B88C73jDuyz7IY5RyLlNd
> Purpose: a reusable lens so Claude can (a) generate new notes that read like Manish wrote them, and (b) write tweets in his voice.

---

## 1. The mental lens (how he listens)

He holds **two lenses at once**, and the combination is what makes him distinctive:

**Lens A — the builder shipping to production.** Every concept gets filtered through three silent questions:

1. **"How do I actually do this?"** — actionable steps over theory.
2. **"How do I test / deploy / pay for this?"** — ops, cost, and latency are never an afterthought.
3. **"When would I pick this over the alternative?"** — decision criteria, not feature lists.

**Lens B — the universal-concept seeker.** Beneath the practical, he wants the *transferable principle* — the idea stripped of its tooling. He's drawn to:

- **The universal abstraction** behind a specific tool (e.g. MCP isn't "a Python thing", it's *the m×n → m+n problem solved by a shared protocol* — a pattern that recurs everywhere from USB to APIs to language itself).
- **Philosophy** — connecting a technical idea to a deeper principle about systems, trust, communication, or how humans organize complexity.
- **Day-to-day analogies** that make the concept *interesting and sticky*, not just understood (USB-C port, robots.txt, universal translator, a boss delegating to workers).

The two lenses pull in opposite directions on purpose: A keeps him concrete and shippable; B keeps him from drowning in tool-specific trivia. A concept earns a place in his notes when it satisfies **either** — actionable *or* universal. The best content satisfies both.

---

## 2. SIGNAL — what he always captures

| Type | Evidence from notes |
|---|---|
| **Actionable steps / how-to** | "Ask it to create pass/fail criteria", "Do development in a phased manner" |
| **Decision rules & thresholds (quantified)** | ">10 files = red flag", "~7–8 python files", "min cacheable tokens 1024 (OpenAI) / 4096 (Claude)", "retrieval should be <0.5 sec" |
| **Red flags / gotchas** | "it will generate a block of code and u have no idea about it", "90% of code won't work, model trained ~6 months ago" |
| **Analogies that compress a concept** | WSGI = "universal translator", MCP Client = "USB driver", MCP = "USB-C port", agent cards = "robots.txt for agents" |
| **Architecture comparisons (X vs Y)** | "MCP = depth, A2A = breadth", "CrewAI = role-based / LangGraph = workflow-based", "manager agent = Opus, workers = gpt-mini" |
| **Economics & performance** | prompt-caching math, rate limits (tpm), cost/latency tradeoffs |
| **Concrete code/structure when it's reusable** | glob snippet, CrewAI assembly block, exec-sandbox `scope={}` pattern |
| **Definition → Analogy → TL;DR pattern** | He likes a term explained, then an analogy, then a one-line "TL;DR" |
| **Universal principle behind the tool** | "MCP solves the m×n problem → m+n problem" — he reaches for the pattern, not just the API |
| **Philosophy / everyday hook** | wants concepts tied to a deeper principle or a simple life example that makes them *interesting* |

---

## 3. NOISE — what he cuts

- Verbatim transcription / lecture filler.
- Polished grammar and prose (he never self-edits — typos stay).
- Theory with no application hook.
- Basics he already knows — he only writes the *delta* (what's new or non-obvious to him).
- Motivational / marketing content.

---

## 4. Format & structure conventions

- **Numbered and bulleted lists dominate.** Prose paragraphs are rare and only used for definitions/analogies.
- **Organized by Day / Section / topic** ("Day 12", "Section 8", "Day 15 Observability").
- **Timestamps as bookmarks** to revisit ("2:18:00 lab to build mcp server", "44:20", "2:48:00 onwards").
- **Tables/columns** appear when comparing concepts.
- Sub-points nest freely (1 → a → i), often inconsistently — structure serves speed, not tidiness.

---

## 5. Voice & mechanics (for when generating *as* him)

- Heavy shorthand: **"u", "ur", "tok ns", "chekc"** — fast typing, no spellcheck.
- Lowercase-first, sentence fragments, dropped articles.
- Direct and declarative — states the rule, skips the hedging.
- Occasional emphatic markers: "**… important ….**", "**Key is to have**", "TL;DR".
- Em-dashes and "—>" arrows to show cause/flow ("User query → llm → decides which tool → returns result").

> NOTE: shorthand/typos reflect his *raw capture* mode. For **published tweets**, keep the voice (direct, builder, decisive) but fix spelling — authority content must be clean.

---

## 6. Metacognitive markers (a defining habit)

He explicitly tags his own knowledge state inline — this is one of his strongest tells:

- **Gaps to revisit:** "need to understand more", "find out more what it means?", "need to investigate from transcript?"
- **Open questions** collected under a "Questions?" heading.
- **Importance flags:** "… important …", "Key is".

When generating notes in his style, **preserve this**: flag what's uncertain, list open questions, mark the high-value items. Don't pretend to full understanding he didn't claim.

---

## 7. Reusable rubric — generating NEW notes in his style

When given a new lecture/transcript, produce notes that:

1. **Lead with actionable steps**, numbered, in the order you'd actually do them.
2. **Extract every quantified threshold / red flag / decision rule** as its own bullet.
3. **For each new term:** one-line definition → analogy → TL;DR.
4. **Add X-vs-Y comparison tables** wherever the lecture contrasts approaches.
5. **Always surface the ops/cost/latency/testing angle**, even if the lecture under-emphasizes it.
5b. **Name the universal principle.** For the key concept, state the transferable pattern beneath the tool ("this is really just X problem"), and add a philosophy or day-to-day analogy that makes it interesting — not just understood.
6. **Keep timestamp bookmarks** for anything worth re-watching.
7. **End with an "Open questions / to investigate" list** — be honest about gaps.
8. **Cut** filler, basics, and theory-without-application.
9. Structure by topic/section; lists over prose; concise.

---

## 8. Implications for TWEETS (authority voice)

His natural material *is* authority content — quantified rules, contrarian gotchas, and sharp analogies are exactly what reads as expertise on X. Tweet angles that fit him:

- **Quantified rule of thumb** ("If your AI scaffolds >10 files for one feature, that's a red flag, not productivity.")
- **Myth-bust / hard truth** ("90% of AI-generated code won't run — the model's libraries are 6 months stale.")
- **Crisp analogy** ("MCP is the USB-C port for AI tools. A2A is how the devices talk to each other.")
- **X-vs-Y decision** ("CrewAI = role-based. LangGraph = workflow-based. Pick by how you think about the problem.")
- **Cost/ops insight** ("Prompt caching won't save you a cent if your static prompt is under 1024 tokens. Most people's are.")
- **Universal principle / philosophy** ("Every protocol is the same bet humans made with language: agree on a shared format once, and you stop needing a translator for every pair. MCP just did it for AI tools — m×n becomes m+n.")
- **Everyday analogy that reframes** ("Your AI agent without observability is a new hire who never tells you what they did all day. You don't need more talent — you need a timesheet.")

Voice: declarative, specific, no fluff, one idea per tweet, ends with a takeaway not a question (unless deliberately baiting engagement).

---

## 9. The empirical filter — learned by diffing 4 full lectures against his notes

> Method: pulled the full ~3-hour transcripts of Days 12, 14, 15, 16 and compared what each lecture *actually contained* against what he *wrote down*. The keep/drop behavior was strikingly consistent across all four. This is the operational filter for generating future notes.

### KEEP / DROP table

| KEEP | DROP |
|---|---|
| **Repeatable procedures & prompt recipes** (phased dev, scaffold prompt, "files one by one + test each") | **Motivational/philosophical framing the *instructor* wraps around them** (career pep talks, "you'll feel empowered") |
| **Hard numbers, thresholds, heuristics** (>10 files = red flag, 1024/4096 cache tokens, retrieval <0.5s, ~7-8 py files) | **Session-specific demo numbers** (28.2s vs 16s, token counts) — they won't reproduce |
| **Crisp definitions + ONE canonical analogy/TL;DR per concept** (WSGI one-liner, m×n→m+n) | **The long narrative buildup, origin stories, vendor backstory** that leads to the definition |
| **Named tools/vendors to actually use** (Langfuse, Tavily MCP, FastMCP, Voyage AI, cursor) | **Feature-by-feature UI tours & per-vendor mechanics** (dashboard clicks, callback-vs-env-var) |
| **API verbs & keyword swaps** (`kickoff` vs `invoke`, `Process.sequential/.hierarchical`, mcp.tool/resource/prompt) | **Live-coding plumbing** (base64 flow, file saving, dataframe building) |
| **Non-obvious implementation mechanics / gotchas** (the `exec(scope={})` sandbox, `async def` for true parallelism) | **Architecture diagrams & design patterns he already knows** (reflect loop, fan-out/fan-in, map-reduce) |
| **The X-vs-Y contrast that resolves confusion** (CrewAI role-based vs LangGraph workflow-based) | **Standalone description of either tool** once the contrast is captured |
| **One striking standalone fact per tangent** ("Claude uses Voyage AI") | **The 10-minute vendor discussion** that fact lived inside |
| **A timestamp bookmark** when content is worth revisiting but too dense to capture live | **Anecdotes, war stories, pricing/billing personal stories** (AWS $120 bill, BPCL breach) |
| | **Anything the speaker labels out-of-scope or defers to another session** (kept to a one-line pointer at most) |

### His active processing (what he ADDS, not transcribes)

- **Authors his own analogy/TL;DR** to lock in a concept (USB-driver/printer triad, "universal translator"). *This is where Lens B lives* — the philosophy/universal principle is **his synthesis layered on top**, NOT extracted from the lecturer's filler. When generating notes, the universal hook is something *the note-taker adds*, not something mined from motivational lecture content.
- **Reconstructs copy-pasteable API signatures** the instructor never wrote that compactly (`scope={}; exec(import_str, code_str, scope)`).
- **Compresses derivations into a maxim + an action** ("know the constraints of the solution"; "check your rate limit = TPM").
- **Reorders by topic, not transcript order** — groups related ideas even when minutes apart.
- **Flags gaps honestly, never fakes coverage** — logs "need to understand more", "find out more?", "Q: what is X?" rather than dropping or fabricating. (One useful caveat: he sometimes *misattributes* in these flags — e.g. tagged SageMaker as an "observability setup" when it was the instructor's load-testing aside. A generator should flag gaps but get the attribution right.)

### The mastery-sparseness rule (important)

**The amount he writes is inversely proportional to how well he already knows the topic.** On Day 12 (LangGraph, which he knows cold) a 3-hour lecture yielded ~3 lines: one gotcha (`exec` sandbox), one mechanic (`async` for parallelism), one fact-to-not-forget (rate limit = TPM). He dropped *every* concept a tutorial would teach and kept only the **residue: the delta between the lecture and what he already knew.**

→ When generating notes for a *new* topic, be fuller. When the topic overlaps what he knows, **shrink to the residue**: gotchas, copy-pasteable signatures, facts he might misremember, and TODOs-to-self.

### His knowledge baseline (for novelty triage — derived from the diffs)

Use this to gauge how full vs. sparse a new note should be. *This is a living map — update it as new lectures reveal more.*

**Already solid → write sparse, residue-only** (he drops all of this when it appears):
- LangGraph core: state schemas, reducers (`add_messages`, `operator.add`), nodes/edges, conditional routing, fan-out/fan-in, map-reduce, `Send`
- Pydantic structured outputs / data contracts (he noted "4th week we're doing pydantic")
- RAG basics, reflect/agent design patterns, the agent framework landscape
- `async`/`await` as a concept; deterministic vs non-deterministic software
- HTTP/REST, auth (OAuth/JWT), basic web/infra plumbing

**Newer / actively learning → write fuller treatment:**
- MCP internals (server/client/host roles, FastMCP, primitives, stdio/SSE transports, m×n→m+n)
- A2A protocol (agent cards, AgentExecutor, combined MCP+A2A architecture)
- CrewAI specifics (`kickoff`, `Process.hierarchical` + manager LLM, role-vs-workflow)
- Observability/traceability tooling (LangSmith / Langfuse / Phoenix) and the 3-level taxonomies
- Prompt-caching economics; managed vector DBs (Pinecone, Voyage AI embeddings); `glob`

**Explicitly flagged as gaps he wants to close** (always surface these in "Open questions"):
- MCP+LLM binding details ("need to understand more", ~2:48:00)
- OpenAI SDK vs Claude SDK
- Deployment as automated functions (Lambda / Azure Function)
- OpenAI image-generation API (how the image is actually created)
- Programmatic trace retrieval / SageMaker (note: he misattributed SageMaker as an observability setup — it was a load-testing aside)

> Caveat carried from the diffs: when he flags a gap, he occasionally **misattributes** the source. The generator should preserve his honest gap-flagging habit but verify attribution against the transcript before recording it.

---

## 10. Note-generation playbook (use this for every new lecture)

Given a transcript, produce notes that:

1. **Triage by novelty first.** Estimate how much of this he already knows. Familiar topic → sparse residue-only notes. New topic → fuller treatment. Never transcribe.
2. **Lead with actionable procedures/recipes**, numbered in do-this-order.
3. **Extract every hard number, threshold, red flag, heuristic** as its own bullet.
4. **One crisp definition + one analogy/TL;DR per key concept.** Author the analogy if the lecture's is weak.
5. **For the single most important concept, add the universal principle + a philosophy or everyday hook** (Lens B) — *your* synthesis, not lecturer filler.
6. **Capture API verbs, keyword swaps, and copy-pasteable signatures** for anything new.
7. **Capture non-obvious mechanics/gotchas** — the things that silently break.
8. **Build an X-vs-Y comparison** wherever the lecture contrasts approaches.
9. **Surface the ops/cost/latency/testing angle** even if under-emphasized.
10. **Timestamp-bookmark** dense sections worth revisiting instead of transcribing them.
11. **End with "Open questions / to investigate"** — honest gaps, correctly attributed.
12. **DROP** everything in the right column of the table above.
13. **Match his voice** in raw notes (shorthand fine); clean spelling only for anything published.

---

## 11. Small refinements he's open to (iterative — not a rewrite)

> His style is intentional and stays as-is. These are tiny, *opt-in* micro-habits that
> extend what he already does — never "what you missed", never more transcription.
> Adopt one, see if it sticks, then maybe the next. New ones get added here one at a
> time as more lectures are reviewed — no backlog dumps.

1. **Tag a captured trick with its pattern name (one word).** When he notes a mechanic,
   add the pattern name beside it so future-him can find it. e.g. next to the `exec`/scope
   note → `(reflective pattern)`; next to parallel nodes → `(fan-out/fan-in)` or
   `(map-reduce / Send)`. One word, big findability payoff. (Complements the
   "residue-only" sparseness rule in §9 — the tag is the index, not extra content.)

2. **Pair each bare timestamp with a 3-word "why".** He already drops timestamp
   bookmarks (§4); adding a tiny reason turns "go back here" into "go back here *for X*".
   e.g. `44:20 — routing + MAX_ATTEMPTS const` instead of just `44:20`. Also prevents the
   misattribution noted in §9 (44:20 was routing/PEP-8, not the bottleneck point at ~1:09:56).
