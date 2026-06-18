# Draft Tweets — Agentic AI / Security Engineering
Generated 2026-06-17 from seed notes (MCP, A2A, CrewAI, observability, prompt caching, AI-code reality). Each labeled with the proven structure used.

---

**1. [Contrarian Hook — myth-bust]**
Everyone's shipping AI-generated code like it's free.

90% of it won't run.

The model's libraries are ~6 months stale — it's confidently writing against APIs that don't exist anymore.

"Generated" isn't "working." One working feature ≈ 20 hrs of review from someone who knows the stack.

---

**2. [Analogy Reframe]**
MCP is just USB-C for AI tools.

Before: every model needs a custom cable for every tool. m×n integrations.
After: one port, plug anything in. m+n.

That's the entire breakthrough. Standardize the connection, stop rebuilding the cable.

---

**3. [Numbered Heuristic / Rule]**
A red flag I use when AI scaffolds a project:

If it generates >10 files for one feature, stop.

A clean build is ~20–25 files total, ~7–8 of them Python. More than that and it's inventing structure to look busy — you've lost the plot.

---

**4. [X vs Y Decision]**
CrewAI vs LangGraph isn't about features. It's about how you think:

• LangGraph = workflow-based. You design the graph.
• CrewAI = role-based. You design the team.

Pick by the question you're answering: "what's the flow?" or "who does what?"

---

**5. [Number/Cost Reveal]**
Prompt caching won't save you a cent — and almost nobody checks why.

Minimum cacheable prompt: 1024 tokens (OpenAI/Gemini), 4096 (Claude).
Your system prompt is probably 300–400.

Caching only pays off with real context to cache. Most people are optimizing nothing.

---

**6. [Aphorism / Universal principle]**
Every protocol is the same bet humans made with language:

agree on a shared format once, and you stop needing a translator for every pair.

Roads. USB. HTTP. Now MCP for AI.

Civilization is just standardized interfaces all the way down.

---

**7. [Everyday Analogy Reframe — observability]**
An AI agent with no observability is a new hire who never tells you what they did all day.

You don't need more talent.
You need a timesheet.

Trace every step — cost, latency, which tool it called — or you're managing a black box.

---

**8. [Hard-won Lesson — how experts learn]**
How I take notes on a 3-hour technical lecture:

If I already know the topic, I write 3 lines.

Not a summary — the residue. The one gotcha, the one API call I'll forget, the one number I'll misremember.

Notes should capture the delta, not the lecture.

---

**9. [Mini-Framework]**
Manager–worker is the cheat code for multi-agent cost:

• Manager = a big model (Opus). Delegates, reviews, does QC.
• Workers = small models (mini). Do the narrow task.

You don't need your smartest model doing grunt work. Match the model to the job.

---

**10. [The Quiet Fact]**
Quiet fact most people miss:

Claude has no embedding model of its own. It uses Voyage AI.

The lesson isn't about Claude — it's that even frontier labs don't own the whole stack.

Specialize or integrate. Nobody wins doing everything in-house.

---

## Notes for refinement
- Strongest hooks (line 1): #1, #6, #7, #10. Weakest: #9 (could open punchier).
- #6 and #8 lean Lens-B (philosophy/universal) — most "authority" flavor, least tutorial.
- If threading: open with #1 or #6, close with #8. #2–#5 are the technical payoff middle.
