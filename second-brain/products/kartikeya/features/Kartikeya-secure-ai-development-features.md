# Kartikeya — Secure AI Development: Feature Specification

> **Product surface:** the Secure AI Development wedge — build-time + runtime security for AI apps and agents, built on one primitive: **capability delta** (actual capability − justified capability).
> **Design principle:** every feature either (a) reaches table-stakes parity with incumbents so we're a credible platform, or (b) is **net-new** because it derives from the capability-delta primitive nobody else has — and **every net-new feature emits compliance evidence as a by-product**. Secure *and* compliant from the same engine.
> Companion to [[Kartikeya-secure-ai-development-business-plan]]. Drafted 2026-06-26.

---

## Legend

| Mark | Meaning |
|---|---|
| 🟦 **NET-NEW** | Not offered by competitors today — derives from the capability-delta primitive. The moat. |
| ◐ **PARITY** | Table-stakes; competitors have it. We build or match so we're a real platform, not a point tool. |
| 🤝 **INTEGRATE** | Better bought/partnered than built; we orchestrate rather than reinvent. |

---

## The line we draw (read this first)

Lasso, Lakera, Prompt Security and others already do **behavioral intent monitoring** and **runtime guardrails**. That sounds like us — it isn't. The distinction is the whole moat:

| | Competitors' "intent monitoring" | Kartikeya capability-delta |
|---|---|---|
| Basis | **Statistical / behavioral** — "this looks anomalous vs. a learned norm" | **Deterministic / least-privilege** — "this exceeds the *authorized* capability set" |
| Output | A risk score / probability | A **justified yes/no + the exact unjustified capability** |
| Explainable to an auditor? | Hard (it's a model) | **Yes — traces to a named capability and its authorization record** |
| Works before runtime? | Mostly runtime-only | **Yes — build-time, before the agent ships** |
| Cold-start | Needs a behavioral baseline to learn | **Per-tenant declared scope — known on day one** |

We don't guess intent. We **measure the gap between declared and actual capability** and gate on it. That is both more defensible *and* more auditable — which is why it doubles as compliance evidence (§3).

---

## 1. Table-stakes features (◐ parity — we match or integrate)

To be bought as a platform we must not be obviously missing what incumbents ship. These are deliberately *parity*, not differentiators:

| Feature | Who has it today | Our stance |
|---|---|---|
| Prompt-injection / jailbreak detection | Lakera, Prompt Security, Lasso | 🤝 integrate at runtime; feed our gate |
| PII / sensitive-data leakage redaction | Lakera, Lasso | 🤝 integrate |
| Malicious **model-file scanning** (pickle/serialization exploits) | Protect AI Guardian, HiddenLayer | ◐ build/partner — it's an input to capability extraction anyway |
| **Shadow-AI discovery** (what agents/models/tools exist) | Prompt Security, HiddenLayer, Lasso | ◐ build — it's the inventory our capability graph rides on |
| AI-BOM / supply-chain inventory | HiddenLayer, Protect AI | ◐ build — but we annotate it with capability (see §2) |
| Red-teaming / attack simulation | HiddenLayer Recon, Lakera Red, Protect AI | 🤝 integrate; use results to validate our gate |
| Runtime content-moderation guardrails | Lakera, Prompt Security | 🤝 integrate |
| MCP gateway basics (server reputation, PII redaction) | Lasso (open-source MCP gateway) | ◐ match — then extend with capability diffing (§2) |

**Position:** we don't win on this list — we win by *not losing* on it, then layering §2 on top.

---

## 2. Net-new features (🟦 the moat — capability-delta derived)

These do not exist in competitor products today. Each follows directly from the primitive.

### 2.1 🟦 Capability extraction for AI artifacts
Static + behavioral analysis that produces a **structured capability manifest** for any model, tool, plugin, or MCP server: `{network, filesystem, process-spawn, credential-access, data-egress, external-API, code-execution, memory/retrieval}`. Competitors scan for *known-bad*; we describe *what it can do* regardless of whether it's known-bad.

### 2.2 🟦 Declared-vs-actual capability diffing
The core. Take the artifact's **declared scope** (MCP server manifest, tool spec, agent system-prompt mandate, model card) and diff it against **extracted actual capability**. Surface the **unjustified delta**. *"This calendar MCP server declares read-only calendar; it can also send email and read env vars — 2 unjustified capabilities."* **Nobody does this.**

### 2.3 🟦 Version-over-version capability diff
When a model/tool/MCP server updates, diff capability **gained** between versions — the npm-worm insight ported to AI. *"v1.4 of this tool added child-process spawn + outbound network. Was that justified by the changelog?"* Sidesteps cold-start (needs only the prior version, not a global baseline).

### 2.4 🟦 The Justified-Capability Ledger (least-privilege baseline per agent)
Each agent gets an explicit, versioned **manifest of authorized capabilities**. Every build-time addition and every runtime action is checked against it. This is the deterministic alternative to behavioral anomaly scoring — and the artifact auditors actually want.

### 2.5 🟦 Build-time Unjustified-Capability Gate (shift-left, in CI)
Block an agent/tool from shipping when it acquires capability beyond its declared mandate — **before production**, in the AI CI/CD pipeline. Incumbents are overwhelmingly runtime-only or scan-only; **we gate at build time on capability.**

### 2.6 🟦 Runtime Agent Intent Detection = the enforcement gate
At runtime, gate any agent action that exceeds its justified capability — `allow / flag / quarantine`. This is OWASP **LLM06 "Excessive Agency"** turned into an enforced control, and it sits exactly in Gartner AI TRiSM's **"Runtime Inspection & Enforcement"** layer (the one Gartner calls non-negotiable for 2025+).

### 2.7 🟦 Capability Blast-Radius scoring
Score each delta by **impact over the agent's tool/data/permission graph** — what's exposed if it acts. `Gate = Blast Radius × Capability Delta`. Turns a flat list of findings into a *prioritized, risk-weighted* gate. Competitors emit unranked alerts.

### 2.8 🟦 Capability-annotated AI-BOM (fleet capability inventory)
Not just "you have 40 agents and 120 tools" (inventory = parity) but **"…and here is the aggregate capability surface, the 9 unjustified deltas, and the 3 over-privileged MCP servers across the fleet."** Inventory + capability = decisions.

### 2.9 🟦 Capability provenance / explainable gate decisions
Every block traces to: the specific unjustified capability, the artifact and version that introduced it, and the authorization record it violated. Audit-grade "why" — not a model score. This is what makes §3 (compliance) possible.

---

## 3. Compliance-by-design (🟦 compliance as a by-product of the primitive)

The unlock: **the same capability ledger that secures the agent is the evidence an auditor needs.** Competitors bolt governance on as a separate module; for us it falls out of the engine. We don't sell "governance" as GRC paperwork — we **auto-emit control evidence** from capability data.

| Framework | The relevant control | How Kartikeya satisfies it (🟦 auto-emitted evidence) |
|---|---|---|
| **OWASP LLM Top 10** | **LLM06 Excessive Agency** (direct hit) | The capability gate *is* the mitigation; the ledger is the proof. Also touches LLM01 (prompt injection — via integration), LLM07 (system-prompt leakage), LLM08 (vector/embedding misuse via data-egress capability). |
| **NIST AI RMF** | GOVERN · MAP · MEASURE · MANAGE | **MAP** = capability inventory/AI-BOM; **MEASURE** = the delta; **MANAGE** = the gate + quarantine. We populate three of four functions from one engine. |
| **ISO/IEC 42001** | AI management-system controls (operational controls, monitoring) | Versioned capability ledger + gate logs = continuous-control evidence for certification. |
| **EU AI Act** | High-risk system logging, traceability, human oversight | Per-action capability provenance + approval gates = the traceability/oversight record. |
| **MITRE ATLAS** | Adversary technique coverage | Map blocked deltas to ATLAS techniques (e.g., tool/agent abuse) for kill-chain reporting. |
| **Google SAIF / SOC 2** | Secure-by-design + control attestation | Build-time gate evidence supports secure-SDLC attestations. |

### 🟦 3.1 Compliance Evidence Pack (auto-generated)
One click → an export mapping the tenant's capability ledger, deltas, and gate decisions to the framework(s) above, dated and signed. **This is net-new: nobody derives audit evidence from a capability-delta engine because nobody else has one.** It collapses "secure the agent" and "prove it's compliant" into a single workflow.

### 🟦 3.2 Policy-as-capability
Express compliance policy directly as capability rules (*"no production agent may hold data-egress + credential-access without sign-off"*) — enforced by the same gate. Policy and enforcement share one model, so drift between "what the policy says" and "what's enforced" is impossible.

---

## 4. Master matrix — at a glance

| Capability | Kartikeya | Protect AI / HiddenLayer | Lakera / Prompt Sec. | Lasso | Socket / Endor |
|---|:--:|:--:|:--:|:--:|:--:|
| Model-file malware scanning | ◐ | ✅ | – | – | – |
| Prompt-injection / runtime guardrails | 🤝 | partial | ✅ | ✅ | – |
| Shadow-AI discovery / AI-BOM | ◐ | ✅ | partial | ✅ | – |
| Behavioral anomaly "intent" | (we go further) | – | – | ✅ | – |
| **Declared-vs-actual capability diff** | 🟦 | – | – | – | – |
| **Version-over-version capability diff** | 🟦 | – | – | – | (npm only) |
| **Build-time capability gate (CI)** | 🟦 | – | – | – | (deps only) |
| **Runtime capability gate (Excessive Agency)** | 🟦 | – | partial* | partial* | – |
| **Capability blast-radius prioritization** | 🟦 | – | – | – | – |
| **Capability-annotated fleet inventory** | 🟦 | – | – | – | – |
| **Auto-emitted compliance evidence pack** | 🟦 | – | – | – | – |

\* runtime *filtering* exists; runtime *least-privilege capability enforcement* does not.

---

## 5. The one line

> Everyone else scans the **file**, filters the **message**, or scores the **behavior**. Kartikeya is the only tool that measures the **capability** — what your AI is actually allowed to do versus what it can do — blocks the gap before it ships, enforces it at runtime, and hands you the compliance evidence on the way out.

---

*Related: [[Kartikeya-secure-ai-development-business-plan]] · [[Kartikeya-universal-intent-detection]].*
*Competitor/framework grounding: Lakera Guard, Lasso MCP gateway & behavioral monitoring, Protect AI Guardian, HiddenLayer; OWASP LLM Top 10 (LLM06 Excessive Agency), NIST AI RMF, ISO/IEC 42001, EU AI Act, MITRE ATLAS, Gartner AI TRiSM.*
