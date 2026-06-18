---
name: tweet-forge
description: Draft authority-building tweets, X posts, or threads from notes, an article, a transcript, or a raw topic. Fuses the writer's own voice with proven viral tweet structures used by top technical creators. Use whenever someone wants to turn knowledge into tweets that position them as an expert.
---

# Tweet Forge

Turn knowledge into tweets that build authority. The output should sound like **the writer**, but be shaped by **structures that are proven to perform** on X.

Two layers, always kept separate:
1. **VOICE** — *how* it sounds (the writer's words, rhythm, opinions). Personal, swappable.
2. **STRUCTURE** — *how* it's built (the skeleton that makes people stop scrolling). Universal, reusable.

A good tweet = the writer's voice poured into a proven structure. Never let the structure flatten the voice into generic LinkedIn-speak.

---

## Step 1 — Load the VOICE

In priority order:
1. If a `style-profile.md` exists in the project (e.g. `second-brain/style-profile.md`), **read it** — it defines the writer's lens, signal/noise, and voice. Use it.
2. Else, if the user pasted sample writing or notes, infer voice from those.
3. Else, ask the user for 2–3 samples of their writing, or a one-line description of their voice (e.g. "blunt, technical, contrarian, hates fluff").

**Default voice profile (Manish — edit/replace when shared):**
- Declarative, specific, no fluff. Builder shipping to production.
- Loves: quantified rules, contrarian-but-defensible takes, sharp analogies, the *universal principle* beneath a tool, everyday reframes.
- One idea per tweet. Ends on a takeaway, not a weak question.
- Clean spelling for anything published (raw notes can be shorthand; tweets cannot).

> When this skill is shared, the new user should replace this default block with their own voice, or point the skill at their own `style-profile.md`.

---

## Step 2 — Pick a STRUCTURE

These are the patterns that consistently perform for technical creators (Naval, Levelsio, Sahil Bloom, swyx, Shaan Puri, etc.). Each entry: when it works + the skeleton.

1. **Contrarian Hook (myth-bust)** — pattern-interrupt. Best for a strong opinion.
   `Everyone believes X. / They're wrong. / Here's what's actually true: …`

2. **Analogy Reframe** — make the complex instantly graspable + memorable.
   `[Hard concept] is just [familiar thing]. / before: … / after: … / That's the whole idea.`

3. **Numbered Heuristic / Rule** — a quantified rule reads as hard-won expertise.
   `My rule: if [signal], [action]. / [the number]. / [why it matters].`

4. **X vs Y Decision** — two-column clarity, ends with how to choose.
   `[A] vs [B] isn't about features. It's about [the real axis]. / • A = … / • B = … / Pick by [the question].`

5. **List / Thread Opener** — promise + curiosity gap; each line earns the next.
   `[N] things about [topic] that took me [time] to learn: / 1) … (then thread).`

6. **Hard-won Lesson** — earned authority via a story compressed to its lesson.
   `I spent [time/cost] on [thing]. / Nobody tells you: [non-obvious lesson].`

7. **Aphorism / One-liner** — short, quotable, zoom-out. Philosophy of the craft.
   `[Punchy universal truth in ≤2 lines].`

8. **Number/Cost Reveal** — a surprising stat + its implication.
   `[Surprising number]. / [what it means for you].`

9. **Mini-Framework** — labeled components people screenshot and save.
   `[Name] is the cheat code for [goal]: / • [part] = … / • [part] = … / [the principle].`

10. **The Quiet Fact** — non-obvious truth + a bigger lesson it points to.
    `Quiet fact most people miss: / [fact]. / The real lesson isn't about [surface] — it's [zoom-out].`

---

## Step 3 — Formatting rules (non-negotiable)

These separate authority tweets from amateur ones:

- **Line 1 is the whole game.** It must stop the scroll and work alone. Write it last if needed.
- **One idea per tweet.** If there are two, it's two tweets.
- **Short lines, generous whitespace.** Break between beats. Walls of text die.
- **Specific beats general.** Real numbers, real names, concrete examples. "1024 tokens" not "a lot of tokens."
- **End on a takeaway, reframe, or earned CTA** — not a limp question (unless deliberately baiting replies).
- **No hashtags. No emoji-spam.** 0 hashtags reads as native; 3+ reads as 2015.
- **Cut every word that isn't load-bearing.** Read it aloud; if you stumble, trim.
- **Keep the writer's opinions sharp.** Defensible-contrarian > safe-correct.

---

## Step 4 — Generate

1. Confirm the **source material** (notes / transcript / article / topic) and **how many** tweets, and whether they want **standalone tweets or a thread**.
2. For each tweet, **vary the structure** (don't ship 10 myth-busts). Aim for a spread across the 10 patterns.
3. Draft in the writer's voice. **Label each tweet with the structure used** so the writer learns the patterns.
4. Keep each under 280 chars unless the writer wants long-form/threads. Flag char count if close.
5. Save to a file (default: `second-brain/tweets/<topic>-<date>.md`) and show them inline.

---

## Step 5 — Offer a refinement pass

After drafting, offer to:
- Tighten the hooks (line 1 of each).
- Re-roll any tweet in a different structure.
- Sequence the best 5–7 into a thread.
- A/B two versions of the top tweet.

---

## Quality bar (self-check before delivering)

- [ ] Does line 1 of each tweet stop the scroll on its own?
- [ ] Is there a spread of structures, not one repeated?
- [ ] Does it sound like the writer — not generic AI-thought-leader voice?
- [ ] Is every claim specific and defensible (numbers, names)?
- [ ] Zero fluff, zero hashtags, clean spelling?
- [ ] Does each end on a takeaway, not a shrug?

---

## Sharing this skill

This whole folder is portable. To give it to someone:
`Copy the `tweet-forge/` folder into their `.claude/skills/` directory.`
Tell them to either replace the **Default voice profile** block in Step 1 with their own, or point it at their own `style-profile.md`. The STRUCTURE library and formatting rules work for anyone.
