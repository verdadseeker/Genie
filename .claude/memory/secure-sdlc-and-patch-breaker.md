---
name: secure-sdlc-and-patch-breaker
description: "Manish's two software products and the shared-engine thesis connecting them"
metadata: 
  node_type: memory
  type: project
  originSessionId: 51435e96-c790-4246-90f6-f32a46cf0d95
---

Part of the [[second-brain-project]]. Manish wants to build two products:

1. **Secure SDLC tool** (PRIMARY focus) — based on Microsoft Zero Trust SDLC approach. Evaluates a software development lifecycle/pipeline against Zero Trust controls (verify explicitly, least privilege, assume breach).
2. **Patch-Breaker** (SECONDARY, built after) — tests Windows patches to predict which servers/applications/services they'll break from an ops perspective.

**Shared-engine thesis (he flagged finding similarities as important):** both products are the SAME engine — *predict the blast radius of a change before it ships, over a dependency graph, scored against a rule set.* Core: **Change → Dependency Graph → Rule/Policy Engine → Impact Score → Remediation.** They differ only in the Change type, the asset graph, and the rulepack. Plan: build the shared core once for SDLC; Patch-Breaker becomes a second rulepack + Windows asset adapter on top. Folders: `second-brain/products/{shared-core,secure-sdlc,patch-breaker}/`.

Sequencing agreed: finish knowledge track (notes/tweets) first, then SDLC design doc, then Patch-Breaker.

**Thesis evolution (2026-06-18) → ARGUS.** The two products are now reframed under one unifying vision: **Zero Trust for any risk a third party introduces** (code, deps, vendor updates incl. Patch Tuesday, contractors/people). Core moat = *you can't detect intent, so detect **unjustified capability**: intent = the delta between what an artifact is authorized to do and what it's actually capable of doing.* Engine = Blast Radius × Capability Delta → gate. Beachhead = capability-diffing on npm/OSS dependencies (sidesteps cold-start). Driven by Manish's lived pain: his advanced team had no preventive answer during the npm attacks, and existing tools are reactive CVE-matchers (blind to zero-signature supply-chain attacks). Vision doc: `second-brain/products/argus-universal-intent-detection.md`. Two caveats: people-risk needs different (UEBA) data than code so it's vision-not-v1; cold-start baseline is the real R&D risk.
