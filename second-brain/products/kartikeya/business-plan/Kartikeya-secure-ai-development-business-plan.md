# Kartikeya — Business Plan

> **Product:** Kartikeya — Universal Intent Detection for third-party-introduced risk.
> **Wedge:** Secure AI Development (capability-delta for the AI supply chain), with **agent intent detection** as the differentiated runtime core.
> **Thesis (unchanged):** *Does this third-party artifact's actual capability exceed what its declared purpose justifies — and was that delta authorized?*
> Full vision: [[Kartikeya-universal-intent-detection]]. This doc is the commercial plan. Drafted 2026-06-24 · updated 2026-06-26.

---

## 🗺️ Visual map

**Document at a glance**

```
KARTIKEYA — BUSINESS PLAN
│
├─ 1. THESIS ........... Intent = unjustified capability delta (one primitive)
│
├─ 2. ENGINE .......... Gate = Blast Radius × Capability Delta
│
├─ 3. UNIVERSAL FRAME . Same primitive across:  code → updates → people
│        └─ wedge = the AI-development instance of "code"
│
├─ 4. WEDGE ........... Secure AI Development
│        ├─ build-time:  capability-diff models · tools · MCP servers
│        └─ runtime:     AGENT INTENT DETECTION  ← differentiator
│
├─ 5. WHY NOW ......... AI TRiSM: "runtime enforcement is no longer optional"
│
├─ 6. MARKET .......... AI TRiSM $3.1B → $13.8B (35% CAGR)
│
├─ 7. COMPETITION ..... scanners check the file · firewalls check the message
│        └─ whitespace: nobody checks the CAPABILITY
│
├─ 8. GTM ............. land via CI scanner → expand to runtime gate → fleet
│
└─ 9. EXPANSION ....... AI dev → npm/OSS → vendor updates → people
```

**The engine, visually**

```
   Third-party artifact (model · tool · MCP server · agent · dependency)
                 │
                 ▼
      ┌──────────────────────┐        ┌──────────────────────┐
      │  DECLARED capability  │        │   OBSERVED actual     │
      │  (what it claims/     │        │   capability          │
      │   is authorized to do)│        │  (what it CAN do)     │
      └──────────┬───────────┘         └──────────┬───────────┘
                 └───────────── diff ─────────────┘
                                 │
                                 ▼
                     ⚠️  CAPABILITY DELTA   ( = "intent" )
                                 │
                                 ×
                          BLAST RADIUS  (impact over the asset/tool graph)
                                 │
                                 ▼
                    🚦  GATE  →  allow · flag · quarantine
```

**Wedge → expansion ladder** (start narrow, narrate the frame)

```
  people / contractors      ░░░░  Expansion 3 (vision — different telemetry)
  vendor updates / patches   ░░   Expansion 2
  npm / OSS dependencies      ░    Expansion 1  (the original Kartikeya wedge)
  SECURE AI DEVELOPMENT     ████   ◀── WEDGE: build here first
```

---

## 1. Executive summary

Kartikeya brings Zero Trust to anything a third party introduces into your environment. The full vision spans **code → vendor updates → people**, unified by one primitive. **We enter through Secure AI Development**: the lifecycle of building AI applications and agents, which now pulls in a sprawl of third-party artifacts — models, tools/MCP servers, plugins, datasets, and the agents themselves — each with a *declared* purpose and a much larger *actual* capability.

Every team shipping AI agents in 2026 has the same unanswered question: **"My agent can do more than I authorized it to. What is it actually capable of, and will it act beyond that?"** Existing AI-security tools either scan model files for malware (Protect AI, HiddenLayer) or filter prompts at runtime (Lakera, Prompt Security). **None govern the capability delta across the agent's whole tool/model graph, and none turn it into a least-privilege gate.** That is Kartikeya's wedge and moat.

The timing is set by the analyst category itself: **Gartner's AI TRiSM** says *"runtime enforcement is no longer optional"* — exactly the gate Kartikeya is. AI TRiSM is **$3.1B (2025) → $13.8B (2030), 35% CAGR**, three times faster than the traditional supply-chain market where we'd otherwise fight Socket and Endor.

---

## 2. The intent reframe & the engine *(from the core thesis)*

**You cannot detect intent — so don't try. Detect *unjustified capability* instead.**

> **Intent = the delta between what an artifact is *authorized/expected* to do and what it is *actually capable of* doing.**

We don't ask "is this malicious?" (unanswerable — mind-reading). We ask "does this artifact's actual capability exceed what its declared function justifies — and was that delta authorized?" That question is **answerable, and identical across every domain.**

```
Gate decision = f( Blast Radius  ×  Capability Delta )
```

- **Capability Delta** = the trust violation ("intent") — actual capability minus justified capability.
- **Blast Radius** = impact over the asset / tool / dependency graph — what's exposed if it acts.

**Shared pipeline:** Third-party artifact → declared/expected capability → observed actual capability → unjustified-delta detection → blast-radius scoring → gate / quarantine / remediation.

This is literally **"verify explicitly + least privilege + assume breach"** turned into a product.

---

## 3. The universal frame *(why this generalizes — the moat)*

The same primitive applies, unchanged, across all third-party-introduced risk. The AI-development wedge is just the first instance of the "code" row:

| Domain | Declared purpose | Unjustified capability delta = "intent" |
|---|---|---|
| **AI artifact (wedge)** | "calendar-reading MCP server" / "support agent" | …also sends email, reads secrets, calls admin APIs |
| **Code / dependency** | "a library that formats dates" | …also has network + filesystem + credential access (the npm worm) |
| **Vendor update / Patch Tuesday** | "fix for print spooler" | …also touches the auth/registry subsystem |
| **Contractor / people** | mandate is "DB migration" | …starts enumerating Active Directory |

**The moat, in three parts (the investor framing):**

- **"Intent detection"** = *what* we sell. Not defensible — anyone in security can claim it.
- **"Intent = unjustified capability delta"** = the *method*. Defensible — it's **preventive** (catches zero-signature attacks with nothing to match against) where everyone else is reactive.
- **"…applied uniformly across AI → code → updates → people"** = the *unification*. The real moat — a competitor can clone one detector, but not the single primitive that generalizes across all third-party risk.

---

## 4. The product (the wedge)

**One sentence:** Kartikeya is the security layer for building and running AI agents — it diffs what every model, tool, and MCP server an agent depends on *declares* against what it can *actually do*, blocks unjustified capability in development, and detects when an agent acts beyond its authorized capability at runtime.

Two surfaces, one engine:

- **Build-time (the entry):** a capability scanner in the AI development pipeline (CI/CD). When a developer wires a model, an MCP server, or a tool into an agent, Kartikeya computes its declared-vs-actual capability and flags unjustified deltas before they ship. *"This calendar-reading MCP server can also send email and read environment secrets — not in its declared scope. Blocked."*
- **Runtime (the differentiator — agent intent detection):** Kartikeya watches the deployed agent and gates actions exceeding its justified capability. *"This support agent's mandate is answering tickets; it just tried to call an internal admin API. Quarantined."*

---

## 5. Why now — anchored to Gartner AI TRiSM

Kartikeya is not inventing a category; it slots into one Gartner just minted. **AI TRiSM (AI Trust, Risk & Security Management)** defines four layers of technical capability to enforce AI governance — and the headline 2025 message is that **runtime enforcement is no longer optional**: without real-time monitoring and automated guardrails, policies have no effect in production. That is precisely the Kartikeya gate.

| Gartner AI TRiSM layer | What it means | Where Kartikeya plays |
|---|---|---|
| **AI Governance** | visibility, traceability, accountability across AI assets (catalogs, assurances) | ✅ build-time capability inventory / AI-BOM |
| **AI Runtime Inspection & Enforcement** | real-time monitoring of models, apps, **agent interactions**; detect & mitigate policy violations | ✅✅ **core — agent intent detection IS this layer** |
| **Information Governance** | AI accesses only permissioned, classified data | ◐ adjacent (capability includes data-egress) |
| **Infrastructure & Stack** | endpoint/network/cloud controls on AI workloads | ✗ not us (partner/integrate) |

We own the layer Gartner calls non-negotiable, and ride the layer above it. Reinforcing tailwinds: MCP exploded across 2024–2025 as how agents get tools (each an undated third-party capability), and "verified ≠ trusted" is now a board-level truth after high-profile "one trusted update, global outage" events.

---

## 6. Why this wedge (Secure AI Development)

| Reason | Detail |
|---|---|
| **Faster market** | AI TRiSM 35% CAGR vs. ~13% for traditional supply-chain security — early S-curve, not a maturing one. |
| **Sidesteps cold-start** | Capability baseline is *per-tenant & per-artifact* (this customer's agent, this MCP server's declared scope) — knowable on day one. No npm-registry-scale corpus needed before we're useful. |
| **Lighter incumbent density** | AI-security is consolidating via acquisition (validation, not saturation); the capability-delta-across-the-agent-graph niche is genuinely open. |
| **No domain-experience handicap** | AI agent security is new enough that thesis quality beats incumbent tenure — unlike Socket/Endor's deep npm/build-system turf. |
| **Preserves the universal frame** | "Secure AI Development" is the AI-stack instance of the Secure-SDLC story; the npm engine survives as a credible Expansion 1. |

---

## 7. Market & TAM (concentric rings)

Analyst-blended; treat the *shape* as the signal. Firm figures in §13.

| Ring | Market | ~2025 | ~2030 | CAGR |
|---|---|---|---|---|
| **SOM** (beachhead) | AI agent / MCP capability assurance | obtainable slice of TRiSM | — | — |
| **SAM** | **AI TRiSM** (Gartner) | **$3.1B** | **$13.8B** | **35%** |
| Adjacent | Responsible AI (platforms/services) | ~$1.6B | ~$10.3B | ~45% |
| Adjacent | AI Governance / compliance | ~$0.75–1.6B | ~$5.6–10B | 40–45% |
| Expansion | Software Supply Chain Security (npm wedge) | $5.5B | $10.1B | 13% |
| Frame ceiling | Zero Trust + Third-Party Risk Mgmt | ~$15–25B | ~$50B+ | — |

**Say out loud:** SAM (AI TRiSM) = **$3.1B → $13.8B by 2030**; the frame ("Zero Trust for third-party-introduced risk, starting with AI") ≈ **$15–25B → $50B+.**

---

## 8. Competitive landscape & whitespace

| Player | What they do | The gap |
|---|---|---|
| **Protect AI** (acq. Palo Alto), **HiddenLayer** | Model scanning, AI-BOM, model risk | Artifact scanning, not capability-delta across the agent's tool graph; little runtime intent gating |
| **Lakera** (acq. Check Point), **Prompt Security**, **Lasso** | Runtime prompt-injection / LLM firewall (I/O filtering) | Filter inputs/outputs; don't model *authorized capability* or diff tool scopes |
| **Robust Intelligence** (acq. Cisco), **Mindgard** | Red-teaming / model validation | Test-time stress, not continuous least-privilege enforcement |
| **Socket.dev, Endor Labs** | OSS dependency behavior (npm/code) | Bounded to package supply chain; not the AI/agent/MCP surface |

**Whitespace Kartikeya owns:** *least-privilege capability-delta unified across model + tool/MCP server + agent action, gated by blast radius.* **MCP capability governance specifically is open and 2026-urgent.**

**One-liner positioning:** *"Model scanners check the file. Prompt firewalls check the message. Neither checks whether your agent has more power than its job allows — or notices when it uses it. We do."* Stay technical/preventive; don't get lumped with questionnaire-based GRC.

---

## 9. Go-to-market: beachhead → expansion

**Land:** the AI platform / ML-engineering team shipping agents to production (not GRC). Entry = the build-time capability scanner + MCP/tool diffing, low-friction in CI, with a falsifiable demo (*"a real MCP server whose actual capability exceeds its declared scope — blocked"*).

**Expand within AI:** build-time diffing → runtime intent detection (the gate) → AI-BOM / fleet capability inventory → least-privilege policy management.

**Expand the frame:** **Exp. 1** npm/OSS dependency diffing (original wedge) → **Exp. 2** vendor updates / Patch Tuesday → **Exp. 3** contractor/people risk (vision; different telemetry — pitch, don't build first).

> **Caveat (carried from the vision):** the *principle* spans AI→code→people; the *implementation* does not. Code/AI capability is tractable (static + behavioral analysis). People-risk needs identity/behavioral telemetry (UEBA territory). **Pitch people-risk as vision; build the AI/code engine first.**

---

## 10. Business model

- **Pricing:** SaaS, per protected *agent / workload* + capability-scan volume. Free build-time scanner tier; monetize runtime gating and fleet inventory.
- **Why it works:** runtime intent gating is the painkiller (board-visible risk) and carries ACV; the free scanner drives bottoms-up adoption and the per-tenant capability data that improves detection.
- **Motion:** product-led entry (CI scanner) → security/platform-leader expansion (runtime + fleet).

---

## 11. Roadmap & milestones

| Phase | Window | Goal |
|---|---|---|
| **0 — Proof** | now → ~2026-09 | Capability taxonomy v1 (model/tool/MCP scopes: network, filesystem, process, credential, data-egress). Falsifiable MCP capability-diff demo. |
| **1 — Design partners** | ~2026-09 → 2027-03 | 5 partners running agents in prod; scanner in their CI; first runtime intent-detection pilot. |
| **2 — v1 GA** | 2027-03 → 2027-09 | GA of scanner + runtime gate; AI-BOM/capability inventory; published "attacks we'd have stopped." |
| **3 — Expand** | 2027-09+ | Fleet policy management; begin Expansion 1 (npm/OSS) to prove the universal frame. |

---

## 12. Team, funding & risks

**Team:** founder (thesis + product). **Critical first hire:** an applied-security/ML engineer to build capability-extraction (static + behavioral) for AI artifacts — the technical core and the cold-start mitigation. Recruit advisors from the agent/MCP ecosystem and Zero Trust practice.

**Funding:** pre-seed to fund Phase 0–1 (taxonomy, scanner MVP, 5 design partners; ~12–18 months runway for 2–3 people — size once the hire's comp + infra are scoped). **Seed proof points:** working scanner, design-partner logos, ≥1 documented real capability-delta catch, runtime-pilot data.

| Risk | Mitigation |
|---|---|
| Capability extraction is hard | Start with **MCP servers / tools — explicit, inspectable scopes** — before opaque model behavior. |
| Softer cold-start persists (sensible default policies) | Per-tenant baseline → useful day one; ship conservative defaults, learn from partners. |
| Fast-moving target (agent/MCP standards shift) | Anchor to the *primitive* (capability delta), standard-agnostic; connectors are swappable. |
| Incumbent acquires into the gap | Move now while the niche is open; defensibility is the unifying primitive, not any one detector. |
| Buyer confusion (vs. scanners / firewalls) | Sharp positioning (§8): *capability*, not file-scanning or I/O-filtering. |

---

## 13. Open items before the deck

- Sourced, citable TAM figures (AI TRiSM, Responsible AI) — blended estimates in §7.
- Whitespace map confirming MCP/tool capability governance is genuinely unowned (scan Lasso, Operant, Prompt Security, Protect AI roadmaps).
- Capability taxonomy v1 + diff/alert thresholds for AI artifacts.
- Confirm 5 nameable companies running agents in production — the real gating question, not TAM.

---

*Related: [[Kartikeya-universal-intent-detection]] (full vision) · [[secure-sdlc-and-patch-breaker]] · [[second-brain-project]].*
*Sources for market/framework figures: Gartner AI TRiSM Market Guide 2025 (via Mindgard, F5, Palo Alto), Precedence Research, nextMSC, Mordor Intelligence.*
