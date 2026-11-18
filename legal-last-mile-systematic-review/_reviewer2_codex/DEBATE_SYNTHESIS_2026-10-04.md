# AI-vs-AI debate on three open methodological items (2026-10-04)

Two independent models (Codex `gpt-5.6-sol`, Gemini `gemini-3.1-flash-lite`) each gave a cold first-round position
on three open items from `00_admin/DECISIONS_AND_OPEN_ITEMS.md`, then each was shown the other's position and asked
whether it changed its mind. Full prompts, raw responses and both rounds for every question are in
`debate/<question>_r{1,2}_{codex,gemini}.json`. This is **advisory**, not a decision: it is two AI opinions, one of
them (Codex) from a different model family than the one that screened the review, informing — not replacing — the
researcher's own judgment call. Nothing in the repository's data was changed by this debate.

## 1. Do the 13 narrative/non-systematic reviews (tool `NONE`) satisfy inclusion criterion 3? (open item, 00_admin/DECISIONS_AND_OPEN_ITEMS.md)

**Converged: exclude under E05**, consistent with how S356 was already excluded. Codex held this position in both
rounds; Gemini started at the opposite position (keep as secondary evidence, option c) and explicitly changed its
mind in round 2 after engaging with Codex's argument that "systematic empirical synthesis" requires documented,
reproducible selection and synthesis procedures — which narrative reviews by definition lack, however much
empirical material they discuss. Both models agree S329 and S418 should **not** be automatically grouped with the
13 merely for having a multi-database search; they qualify for inclusion (not E05) only if they also document a
reproducible eligibility/selection/synthesis procedure, which a database search alone does not establish.

**If the researcher accepts this:** 13 studies (S079, S320, S321, S322, S326, S429, S430, S436, S440, S466, S479,
S480, S482) move from `include` to `exclude` under `E05`, and S329/S418 need an individual check against the same
reproducibility standard — not a blanket decision either way.

## 2. Should linked (companion) reports be collapsed, kept-and-linked, or left separate? (A3)

**Converged: collapse confirmed same-data pairs for counting and synthesis; keep possible/partial pairs separate but linked, with dependence managed if they co-occur in a synthesis.** Both models reached materially the same position independently in round 1 (Codex from a PRISMA report-vs-study framing, Gemini from a unit-of-analysis-error framing) and reinforced each other in round 2 rather than changing position. Both single out **LR01 (S294/S366)** by name: it should be treated as **one cluster-randomised trial with two companion outcome reports** — retain both rows and their distinct eligible outcomes, but do not count or weight them as two independent studies in Family B.

**If the researcher accepts this:** collapse LR01 (S294/S366) and LR02 (S097/S098) — the two `same_underlying_data=yes` pairs — for any count or synthesis (distinct-study total moves from 1,159 toward 1,157, as `00_admin/DECISIONS_AND_OPEN_ITEMS.md` A3 already flags); the 2 "partial" pairs and the 8 "possible"/lower-confidence pairs stay as separate counted studies, flagged for dependence-aware handling if they ever enter the same synthesis cell.

## 3. Should the draft `mechanism_family`/`outcome_family` controlled vocabulary be adopted? (A5)

**Converged: adopt as a provisional multi-label taxonomy, not as-is for headline single-label tabulation; add a separately, manually coded primary-family variable; validate the 45 needs-review studies before relying on any of it.** Codex's round-1 position already included this; Gemini started by proposing to refine the keyword rules to shrink the 45% "multiple" bucket, but changed its view (marked "partially") after Codex argued the high multiple-rate may reflect genuine multi-mechanism complexity in the studies themselves, not just rule overbreadth — so forcing single labels via tighter keywords would hide real complexity rather than fix a coding error. Both explicitly reject using the mechanical draft, unmodified, as the field a headline table pools by.

**If the researcher accepts this:** treat the 9 mechanism families as a multi-label coding scheme (co-occurrence analysis, not mutually-exclusive tabulation), keep every original free-text label, treat blank booleans as unknown rather than false, and have a human manually assign one primary mechanism per study (from its stated main causal/analytic focus) for any table or figure that needs one value per study — do not derive that primary value mechanically from the extraction booleans.

## What this debate does and does not establish

- It is **not** a third independent screening pass — Codex and Gemini are the same two models already used for the
  tier 1-3 full-text re-screen; this is a separate, higher-level methodological question, not a re-read of any
  paper.
- Agreement between two different model families on a scope question is more informative than one model agreeing
  with itself, but it is still an AI opinion. A human reading the protocol and a sample of the actual papers could
  reasonably reach a different conclusion, particularly on item 1 (the "systematic" threshold is a genuinely
  contestable reading of criterion 3).
- Round 2 "changed_mind" responses were not forced — both models were explicitly permitted to disagree, and did
  (Codex, both times) or agreed only partially, which is some evidence the convergence is not just two models
  being agreeable by default.
