---
name: second-brain-project
description: "Manish's \"AI second brain\" project — objectives, structure, and current state"
metadata: 
  node_type: memory
  type: project
  originSessionId: 51435e96-c790-4246-90f6-f32a46cf0d95
---

Building an "AI second brain" in Claude Code that replicates Manish's thinking style. Lives at `Genie-Official/second-brain/`.

**Objectives:**
1. Learn his note-taking style from seed notes → generate notes in his style from new YouTube/lecture content (AI / Security / DevOps / Data Engineering).
2. Generate 10 draft tweets on those topics to build authority on X.
3. Help build two software products (see [[secure-sdlc-and-patch-breaker]]).

**Structure:** `style-profile.md` (the core asset — his lens + empirical keep/drop filter + note-generation playbook), `seed-notes/`, `notes/` (generated), `tweets/`, `sources/` (transcripts + `clean_vtt.py` cleaner), `products/`.

**His style (verified by diffing 4 full lecture transcripts vs his notes):** Two lenses — (A) builder shipping to production, (B) universal-concept/philosophy seeker. KEEPs procedures, hard numbers/thresholds, crisp definitions + one analogy, tool names, API verbs, gotchas, X-vs-Y contrasts. DROPs demo noise, lecturer pep talks, anecdotes, out-of-scope tangents, and things he already knows. **Mastery-sparseness rule:** the better he knows a topic, the less he writes (residue only). The philosophy/universal hook is HIS synthesis added on top, not mined from lecture filler. Flags gaps honestly.

**Tooling note:** transcripts pulled via `python -m yt_dlp` (installed --user; no ffmpeg/yt-dlp on PATH). `clean_vtt.py` dedupes rolling auto-captions + adds timestamp bookmarks.

**State (2026-06-17):** style-profile.md complete. 7 of 8 playlist transcripts on disk (Day 13 has no captions). Next: generate a test note to validate the filter, then the 10 tweets.
