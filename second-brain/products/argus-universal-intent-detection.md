# Kartikeya  — Universal Intent Detection for Third-Party-Introduced Risk

> *Working name. Argus Panoptes: the all-seeing guardian who watches every gate, and looks two ways at once — at what a thing **claims** to be, and what it is **actually capable of**.*

---

## The one-line vision

**Zero Trust applied to anything a third party introduces into your environment** — code, dependencies, vendor updates, contractor access, people. One engine that answers a single question, everywhere: *does this third-party artifact's actual capability exceed what its declared purpose justifies — and was that delta authorized?*

---

## The problem (lived, not theoretical)

When the npm supply-chain attacks hit, even a technically advanced team had **no preventive answer**. The reason isn't that tools don't exist — it's that the existing tools solve a *different* problem:

- **What Snyk / Dependabot / GitHub / most SCA do:** match dependencies against *known* CVEs in a database. **Reactive and lagging** — only works *after* a vulnerability is published.
- **What the npm worm actually was:** freshly-compromised packages, malicious `postinstall` scripts, credential theft, self-propagation. **Zero CVE. Nothing to match against.** Every CVE-matching tool was blind by design.

The gap is not "another scanner." The gap is **preventive assurance** for risk that has no signature yet.

---

## The intent-detection angle (the part you actually want to crack)

Here's the unlock, and I think it's genuinely novel as a *unifying* primitive: **you cannot detect intent — so don't try. Detect *unjustified capability* instead.** Zero Trust gives you the reframe for free via *least privilege*:

> **Intent = the delta between what an artifact is *authorized/expected* to do and what it is *actually capable of* doing.**

You're not asking "is this malicious?" (unanswerable, mind-reading). You're asking "does this third-party artifact's actual capability exceed what its declared function justifies — and was that delta authorized?" That question is **answerable, and identical across all three of your domains:**

- **Code / dependency:** A package that formats dates doesn't need network + filesystem + credential access. The npm worm's payload was *capability the package's stated function never justified*. → flag the capability delta.
- **Vendor update / Patch Tuesday:** A patch described as "fix for print spooler" that touches the auth/registry subsystem is exercising capability its change description doesn't justify. → same primitive.
- **Contractor / people:** A contractor whose mandate is "DB migration" who starts enumerating Active Directory is exercising capability beyond declared role. → same primitive.

So your engine becomes two complementary scores feeding one Zero Trust gate:
- **Blast radius** (impact, over the dependency/asset graph) — your original engine.
- **Capability delta** (trust violation = "intent") — the new piece.

Gate = `Impact × Trust-violation`. *That* is "verify explicitly + least privilege + assume breach" turned into a product. It's a cleaner, more defensible thesis than anything I've seen Socket.dev or Endor articulate publicly, because they're mostly still anchored to known-vuln + behavioral heuristics, not a unified least-privilege/capability-delta model spanning code→updates→people.

---

## The moat (in one line)

> **Our moat is reframing intent as an *unjustified capability delta* — and applying that one primitive uniformly across code, vendor updates, and people.**

The distinction matters for an investor:

- **"Intent detection"** = the goal. *Not* defensible — it's a claim anyone in security can make.
- **"Intent = unjustified capability delta"** = the *method*. Defensible, because it's preventive (catches zero-signature attacks with nothing to match against) where everyone else is reactive.
- **"…applied uniformly across code → updates → people"** = the *unification*. The real moat — a competitor can clone one detector, but not the single primitive that generalizes across all third-party risk.

So: intent detection is **what** we sell; the capability-delta primitive + its universal reach is **why we win**.

---

## The engine

Two complementary scores feeding one Zero Trust gate:

- **Blast radius** — impact of the change, computed over the dependency / asset graph. *(What breaks / what's exposed if this acts.)*
- **Capability delta** — the trust violation, i.e. "intent." *(What can this actually do vs. what it's justified to do.)*

```
Gate decision = f( Blast Radius  ×  Capability Delta )
```

This is literally **"verify explicitly + least privilege + assume breach"** turned into a product.

Pipeline (shared core): **Third-party artifact → Declared/expected capability → Observed actual capability → Unjustified-delta detection → Blast-radius scoring → Gate / quarantine / remediation.**

---

## Beachhead → expansion

**Start narrow, narrate the frame.**

- **Wedge (build first):** capability-diffing on software dependencies (npm / OSS). *"This package gained credential + network access in a patch release — we blocked it; here's the npm worm we'd have stopped."* Killer, falsifiable demo.
  - Why this wedge: **version-over-version diffing sidesteps the cold-start problem** — it needs no absolute "expected behavior" baseline, just a delta between versions.
- **Expansion 1:** Secure SDLC / pipeline (the dependency + build graph).
- **Expansion 2:** vendor updates including Microsoft Patch Tuesday (reframed as untrusted third-party change).
- **Expansion 3:** third-party contractors / people risk.

The principle spans all of these. **The implementation does not** — see caveats.

---

## Why now

- Supply-chain attacks (npm worm class) have no signature and defeat every CVE-based tool — a felt, unsolved, painkiller-grade pain.
- High-profile "one trusted update, global outage" events made *"verified ≠ trusted"* an accepted truth at the board level.
- Zero Trust and Third-Party Risk Management are funded categories with existing budget lines — the frame is legible, not a category we have to invent.

---

## Market (TAM — concentric rings)

Analyst-blended estimates; treat the *shape* as the signal, firm numbers to be sourced for the deck.

| Ring | Market | ~Today | ~2030 |
|---|---|---|---|
| **SOM** (beachhead) | OSS / 3rd-party dependency preventive assurance | ~$0.3–1B obtainable slice | — |
| **Layer 1** | Software Supply Chain Security | ~$2.5B | ~$9–12B |
| **Layer 2** | AppSec + ASPM + DevSecOps | ~$10B | ~$30B+ |
| **Layer 3 (the frame)** | Third-Party Risk Management (TPRM) | ~$6–8B | ~$18–20B |
| **Layer 4 (ceiling)** | Zero Trust Security (overall) | ~$30B+ | ~$90–120B |
| *(ref)* | Patch management alone | ~$1B | ~$2–3B — deliberately small; proves patching is a *feature*, not the market |
| *(ref)* | Privileged / 3rd-party access (PAM) | ~$3–4B | ~$10B+ |

**The number to say out loud:** the frame ("Zero Trust for third-party-introduced risk") ≈ **$15–25B today → $50B+ by 2030.** SAM (technical preventive core) ≈ **$5–12B.** SOM (npm/OSS dependency wedge) = a nameable slice of Layer 1.

---

## The two caveats (the things that will bite)

1. **The principle spans code→people; the implementation does not.** Capability-delta for code is tractable (static + behavioral analysis of the artifact). For people/contractors it needs identity + behavioral telemetry — different data sources (UEBA territory). Pitch people-risk as *vision*; build the code/dependency engine first.

2. **Cold-start / baseline is the real R&D risk.** "Unjustified capability" needs a baseline of *expected* capability, which most packages never declare. Mitigation: **start with version-over-version capability diffing** (needs no absolute baseline) before attempting absolute "expected behavior" modeling.

---

## Positioning guardrail

Open against the incumbents explicitly, or get pattern-matched into the "supply-chain security" pile: *"Every existing tool is a reactive CVE scanner. The npm attacks had no CVE. Here is what they all structurally cannot see."* And stay on the **technical / preventive** side of the line — not lumped with questionnaire-based GRC TPRM (OneTrust et al.).

---

## Open questions to resolve next

- Sourced, citable TAM figures for the deck.
- Competitive whitespace map: where do Socket.dev / Endor / Phylum / Chainguard already touch capability analysis, and where is the capability-delta gap genuinely open?
- Define the v1 capability taxonomy for the dependency wedge (network / filesystem / process-spawn / credential / env-access …) and the diff/alerting threshold.

---

*Related: [[secure-sdlc-and-patch-breaker]] · [[second-brain-project]]. This document supersedes the two-separate-products framing with a single unifying engine.*
