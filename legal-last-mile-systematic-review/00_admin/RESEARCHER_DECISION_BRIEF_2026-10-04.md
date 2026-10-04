# Researcher decision brief — what only you can do to finish the review (2026-10-04)

*A short route to the end. Everything the AI could do on its own has been done and pushed; what is left needs your judgment, your access or your reading.
Detail for each item: `DECISIONS_AND_OPEN_ITEMS.md`. Figures: `CURRENT_FIGURES.md`. A reply of just the item numbers and letters (for example "1b, 2a, 3: yes") is enough — the AI will apply each answer, regenerate every dependent file and re-run the verifier.*

## Part 1 — Decisions (about 30 minutes in total)

| # | Decision | Options | AI recommendation | What happens next |
|---|---|---|---|---|
| 1 | **Scope of three AMSTAR 2 groups** (S327 handwashing behaviour; narrative or hybrid reviews S329, S418 and the 13 `NONE` studies; weak single-author reviews S325, S344) — do they meet inclusion criterion 3 (empirical evidence or a *systematic* empirical synthesis)? | (a) keep all, state caveat; (b) exclude S327 only; (c) exclude all non-systematic reviews | **(b)** S327 has almost no legal content; keep the rest, as secondary evidence that is never pooled | Re-run counts, report, manuscript draft; log an E-code exclusion with rationale |
| 2 | **S589** (the only effect-size row for a study not flagged eligible) | (a) keep and flip the flag; (b) remove the row | **(a)** it is a real descriptive comparison; the sensitivity analysis shows no conclusion depends on it | Family A stays 20 (or becomes 19) and every dependent file regenerates |
| 3 | **Linked reports** (S294/S366 one trial; S097/S098 one interview sample) | (a) keep both rows and link; (b) collapse | **(a)** already linked; collapse only in the counts that need independent studies | None needed if (a) |
| 4 | **S366 effect-size row** (full-text results now extracted: improved source +33 pp, CI 22–45) | (a) add a row to Family B; (b) leave it out because S294 already represents the trial | **(b)** adding it would count one trial twice | None needed if (b) |
| 5 | **Sparse-record audit**: should the headline abstract-only count use the broader definition (117 rows, of which 37 are on the current list)? | (a) keep 37 and state it is a floor; (b) adopt the broader set | **(a)** until the remaining strong rows are re-extracted; the report already says it is a floor | Re-extract from full text when PDFs arrive |
| 6 | **Taxonomy** (`mechanism_family`/`outcome_family`: 236 and 127 distinct labels; draft vocabulary exists) | (a) adopt the draft; (b) edit it first; (c) leave and say so | **(b)** spot-check the `needs_review = TRUE` rows, then adopt | Add controlled columns to the evidence map by a dated script |
| 7 | **Mechanism-certainty re-coding** (35 studies coded 3–4; only 10 are quasi-experimental/experimental) | (a) re-code to match design; (b) keep and footnote | **(a)** after reading the 25 outside-design papers or accepting a rule from design | Regenerate figures; no effect-size row changes |
| 8 | **AMSTAR 2 for realist/scoping/qualitative reviews** (11 of 12 rated are Critically Low; the tool separates little) | (a) keep; (b) add a second, narrative-review instrument | **(a)** for this paper; note the limitation | None needed if (a) |
| 9 | **Registration**: submit the OSF draft as an explicitly **retrospective** registration | (a) submit now; (b) skip registration and state so | **(a)** — the draft already carries the disclosure; it takes ~20 minutes | Record the identifier in `PROTOCOL.md`; update draft §2.1 and PRISMA item 24a |
| 10 | **Release**: tag a version and update `CITATION.cff` (still `0.1.0-interim`) | (a) tag now; (b) after the human verification below | **(b)** the data may still change | AI updates version and date |

## Part 2 — Things only you can do, ranked by payoff per hour

1. **Human second-extraction sample** (`03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv`; 60 studies from S001–S200, 9 fields each; about 15–20 minutes per study if you know the field). This is the single biggest credibility gain: it gives the first estimate of the extraction error rate. Even 20 studies helps — send the filled sheet and the AI scores it (`score_second_extractor_sheet.py`, Wilson intervals).
2. **Human screening check of the 73 no-reviewer rows** (`02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv`, tier 1; about 5 minutes each) — closes the provenance gap (A2/A6).
3. **PDFs the AI could not read or reach** (the egress proxy blocks the open web, so retrieval is yours): `R0908697F9FE5` (156 MB scan) and `RBEDB6556B711` (a scanned JSTOR PDF with no text layer — needs a text-searchable copy or the pages as images); the 14 *strong* sparse-audit rows (`SPARSE_RECORD_AUDIT_2026-10-04.csv`, `strength = strong`); and the unrated AMSTAR 2 reviews S015, S019, S027, S116, S323, S328, S329, S350, S427, S475, S521, S537.
4. **Fill PRISMA items 25 and 26** (funding, competing interests) in `00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md` — five minutes, and it unblocks the manuscript declarations.
5. **Read and edit the manuscript draft** (`07_manuscript/draft/MANUSCRIPT_DRAFT_2026-10-04.md`): add the `[ref]` citations and the literature context for the Introduction and Discussion; nothing in it has been human-reviewed.
6. **Check checklist wording against the official sources** (PRISMA 2020, AMSTAR 2, RoB 2, ROBINS-I, JBI, CASP, MMAT) — the AI could only verify at search-snippet level (A9).
7. **Decide the next retrieval step** for the 1,383 never-assessed records (older on average): targeted retrieval of an older-records sample, or state the limitation as is.

## Part 3 — What the AI will do the moment you answer

- Apply decisions 1–10, regenerate the report, HTML and Word versions, manuscript draft, sensitivity file and figures, and run the verifier (127 checks) before every push.
- Score the filled second-extractor sheet and update the AI-use statement and limitations with the measured error rate.
- Re-extract and appraise any PDF you supply (about 20 minutes of AI time each) and update the AMSTAR 2 count (12 of 23 rated now).
- Draft the cover letter, a journal-specific AI-disclosure paragraph and a plain-language summary once decisions 1–4 and the second-extraction sheet are in.

## Where the project stands in one paragraph

Screening, extraction, appraisal and three structured syntheses are complete as far as the AI can take them, and every figure is reproducible (`verify_repository.py`). The headline result is cautious: 1,159 studies, 6% with designs able to support a causal claim, 62 effect-size rows and no pooled estimate; direction of association mostly favourable for legal recognition and for administrative assistance, mixed for barriers and ownership; confidence low to very low. What stands between this and a submittable paper is human verification (second extraction, the no-reviewer rows, the AMSTAR 2 and overlap questions), the missing disclosures and citations, and a decision about registration and the unassessed records.
