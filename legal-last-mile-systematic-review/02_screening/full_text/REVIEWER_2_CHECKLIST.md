# Reviewer 2 checklist — one page

For each record, in `full_text_reviewer_2_priority_queue_2026-09-28.csv` order. **Decide before you read the AI's reasoning.**

**1. Get the paper.** DOI/URL columns; if you cannot get the full text, record `cannot_tell` and the reason — never guess from the abstract.

**2. Apply the inclusion criteria** (`INCLUSION_EXCLUSION.md`) — all of them, in this order:
- [ ] Examines water or sanitation **service access**?
- [ ] Examines a **legal, administrative, institutional, regulatory or governance** factor?
- [ ] Contains **empirical evidence or a systematic empirical synthesis**? (A policy overview, essay or commentary with no method and no primary data is **not** enough → E05.)
- [ ] Reports an **outcome** relevant to access, connection, availability, reliability, quantity, affordability or exclusion?
- [ ] Enough information to identify **population, exposure and outcome**? Study **design identifiable**?
- [ ] Language English, Portuguese or Dutch (others only if translation is feasible and logged)?
- [ ] Not a **duplicate** of another included paper (same paper under another title/language, or a companion report of the same study — see `linked_reports_2026-09-28.csv`)?

Qualitative socio-legal studies are **never** excluded merely because they cannot be pooled.

**3. Pick the decision.** `include`, `exclude` + one code, or `cannot_tell`.

| Code | Use when |
|---|---|
| E01 wrong topic | not about water/sanitation service access + a legal/administrative factor |
| E02 wrong population | population out of scope | 
| E03 wrong exposure | no legal/administrative/governance exposure |
| E04 wrong outcome | no access-relevant outcome |
| E05 no empirical evidence | commentary, essay, non-systematic overview, purely normative |
| E06 engineering only | infrastructure engineering with no governance angle |
| E07 wrong service | not water/sanitation household service |
| E08 duplicate | same paper as another record |
| E09 insufficient information | cannot identify exposure/outcome/design |
| E12 wrong study design | design cannot support the question |

**4. Then compare** with `ai_decision` and `ai_reasoning_READ_AFTER_YOUR_OWN_JUDGMENT`. Fill `reviewer_2_agrees_with_AI` (Y/N) and, if N, say why in one line.

**5. Extra checks for includes (tiers 1 and 3):** does the extraction row (`study_id` column → `03_extraction/extracted_data/extraction_database.csv`) match the paper on country, design, sample size, exposure and outcome, and the effect direction if one is recorded? Note any mismatch in `reviewer_2_comment`.

**6. Tier 1 only:** the row has no reviewer label; if you confirm it, your confirmation is the first recorded review of that decision.

**Do not:** infer from the title or abstract alone; force a decision when you cannot read the paper; edit the AI's columns; extrapolate from a small sample — report per-tier agreement and flag disagreement patterns.
