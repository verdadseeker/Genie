# Genie — Project Context (auto-loaded by Claude Code)

This repo is **Genie**: Manish's AI "second brain" plus the security products it is incubating. It is synced across machines via this GitHub repo (`github.com/verdadseeker/Genie`). Claude memory lives in `.claude/memory/` and travels with the repo.

## Sync workflow (read this first)
- **At the start of a session:** `git pull` before doing any work.
- **At the end of a session:** commit and push so the other machine stays current.
- Do **not** work on two machines simultaneously without pulling first.
- Durable project facts go in `.claude/memory/` (indexed by `MEMORY.md`). This is the same memory system as before — now version-controlled.

## What's here
- `second-brain/style-profile.md` — the core asset: Manish's note-taking lens + note-generation playbook.
- `second-brain/seed-notes/`, `notes/`, `tweets/`, `sources/` — knowledge track (learn his style → generate notes/tweets).
- `second-brain/products/` — the product work.
- `.claude/memory/` — persistent memory (project, user, feedback, reference facts).

## The flagship product: ARGUS
See `second-brain/products/argus-universal-intent-detection.md` for the full vision.

- **What it is:** Zero Trust for anything a third party introduces — code, dependencies, vendor updates (incl. Patch Tuesday), contractors/people.
- **The moat (one line):** reframing intent as an *unjustified capability delta*, applied uniformly across code → updates → people. ("Intent detection" is what we sell; the capability-delta primitive + its universal reach is why we win.)
- **Engine:** `Gate = Blast Radius × Capability Delta`.
- **Beachhead:** capability-diffing on npm/OSS dependencies (sidesteps the cold-start problem); SDLC is the starting product.
- **Nearest competitor to learn from:** Socket.dev (behavior-first, 70+ signals) and Endor Labs (150+ signals, multi-ecosystem). The gap to exploit: they use flat signal lists bounded to packages; ARGUS uses a *capability delta* unified across code/updates/people.

## Working norms
- Analyze Manish's notes as **style improvements**, never as "what you missed" / gap framing.
- Convert relative dates to absolute when recording facts.
