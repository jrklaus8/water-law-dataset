# Slide copy of the preliminary results report

`Water_Access_Evidence_Diagnostic_slides_2026-09-29.pdf` — 13 slides, "Mapping the Water-Access Evidence Base", supplied by the researcher on
2026-09-29 as a visual companion to `../PRELIMINARY_RESULTS_REPORT_2026-09-29.md`. Kept unaltered for future reference.

## Provenance (read before citing it)

- **Not made by the repository's scripts and not made by Claude.** The slide footers read "A Gemini Notebook" (Google NotebookLM); the researcher
  produced the deck from an early 2026-09-29 version of the report. It is a second AI summary of an AI-generated report, so it inherits every caveat in
  `../../AI_USE_STATEMENT.md` and adds its own risk of paraphrase drift.
- **It predates later changes.** It was built before S366, S326 and S277 were re-extracted from full text, before the data-quality audits, and before the AMSTAR 2
  wording was corrected. Where it differs from the current report, **the report and `../../00_admin/CURRENT_FIGURES.md` are right**.
- The PDF file itself passed a basic safety scan (no JavaScript, launch actions, embedded files or links). Only its **text** was checked here; the charts and
  images on slides 4, 5, 7, 8, 9, 10, 11 and 13 were not visually reviewed.

## Where the deck differs from the current report

| Slide | Deck says | Current position |
|---|---|---|
| 2 | "92% concentrated in just 10 countries" | Wrong: the ten commonest single countries hold **599 studies, 52%** (the deck's own slide 4 says 52%) |
| 2 | "94% of the corpus is qualitative, observational, or doctrinal" | Report: **6%** (68 studies) use causal-capable designs; the other 94% also include secondary reviews and free-text case-study labels, so "qualitative, observational, or doctrinal" is a loose paraphrase |
| 5, 13 | Netherlands and Canada "a data desert"; the evidence base "utterly fails"; primary data collection or targeted searching "is mandatory" | Stronger than the report, which says only that the comparative frame "cannot be tested from this base as it stands". What to do about it is a researcher decision, not a finding |
| 7 | "Qualitative research heavily focuses on institutional fragmentation and official discretion" | The mechanism counts (663, 597, 541 …) are over **all 1,159 studies**, not qualitative studies only |
| 8 | "Only 35 of these [68] studies carry a numeric mechanism-certainty of 3 or 4" | Wrong: 35 is the **corpus-wide** count of studies coded certainty 3 or 4, and **only 10 of them are among the 68 ROBINS-I/RoB 2 studies**; the other 25 are qualitative, mixed-methods, cross-sectional or documentary designs — a coding inconsistency found while checking this slide (`../../05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md` §5). The report's earlier wording was also misleading and has been corrected |
| 11 | contains a placeholder "(XX records)" | The figures are 3,665 include/unsure records and 22,557 AI exclusions (report §1, §3.2) |
| 12 | "AMSTAR 2 Misalignments (24 studies)"; "only 12 carry a confirmed systematic method label; 12 rely on bare AI classification"; "22 of 24 Not ratable" | Superseded: S326 moved to `NONE` on 2026-09-29, so **23** studies carry AMSTAR 2; as of 2026-10-03 **11 of 23** have a formal rating (10 Critically Low, S327 Low) and **12** are "Not ratable". The "12 vs 12 label" finding was an artefact of checking one field; across all recorded fields 9 name a registration/PRISMA/JBI method and 9 state a count of included studies (`../../05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md` §3) |
| 12 | "All 5 [RoB 2] rate 'Some concerns' heavily driven by 'No information' answers" | S366 was re-appraised on its full text on 2026-09-29 (Domains 1 and 3 Low); S057, S085, S294 and S879 remain "No information"-heavy, and S879's cluster unit is still inferred |

Everything else on the slides (1,159 studies; 985 or 85% published since 2010; 34,594 raw and 27,481 unique records; 2,276 of 3,659 assessed, 62.2%; 1,383 unassessed; the
ten-country counts; Canada 15 / Netherlands 1; the mechanism and outcome counts; the 15/20, 6, and 7/9/4 family splits) matches the report as generated at the time.

**If you present or cite the slides, use the current report's numbers and treat the "mandatory" recommendations as the deck author's opinion.**
