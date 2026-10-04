# AI-use statement

**This is an AI-assisted systematic review.** A large language model (Claude, from Anthropic) carried out most of the
screening, data extraction, risk-of-bias appraisal, classification and synthesis drafting in this repository, working under
the researcher's direction and within a written protocol. The researcher (Claudio Klaus) set the question, the protocol and
eligibility criteria, ran the database searches, supplied the full texts, made the closing and scoping decisions, and
independently reviewed a part of the screening. The AI's outputs have **not** been independently verified in full. The
title carries the words "AI-Assisted" so that no reader has to discover this from the methods.

## What the AI did, and what a human checked

| Stage | AI role | Human role | Independently checked by a human |
|---|---|---|---|
| Search strategy, exports, deduplication | Wrote and ran scripts for deduplication and audits | Designed searches, ran them in the databases, exported records | Duplicate audits were also run by the AI; not independently re-checked |
| Title/abstract screening | First-pass decision and written rationale for each record | Second reviewer on the 3,665 include-plus-unsure records, not on the AI's 22,557 exclusions (99.8% agreement — flagged in the README as unusually high) | Yes, for those records |
| Full-text screening | Read each supplied full text and decided include/exclude with a coded reason | Obtained and supplied the full texts; confirmed 200 includes (S001–S100 on 2026-09-27, S101–S200 on 2026-10-02) | **Only those 200 includes**; no excludes |
| Data extraction (92 fields) | Extracted every study, largely from full text; 37 studies from abstract or metadata only (down from 62 after 25 were re-extracted from Drive full texts on 2026-10-04; see `code/provenance/audit_and_repair/reextract_2026-10-04/CAMPAIGN_NOTES.md`) (a floor: a 2026-10-04 audit found 80 more rows (after a further 47 were re-extracted from Drive full texts the same day) with signs of shallow extraction — 12 whose own notes say so and 21 whose recorded location cites only the abstract; see `05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`) | Supplied documents | **None**; no second extractor |
| Risk-of-bias appraisal | Rule-based batch ratings from extracted fields, using the published instruments' structure | Supplied the official instrument documents | **None**; not a signalling-question read of each paper. One instrument is the project's own and is not validated |
| Classification, effect-size table | Coded and classified | — | None |
| Structured (SWiM) syntheses, feasibility judgment | Drafted, with disclosed judgment calls | Approves and decides | None |
| This repository's audits and corrections | Found and corrected its own errors in the open | Approved merges and exclusions | — |

## Why you should still read it critically

- The same system produced and audited much of the work, so its checks find inconsistencies and arithmetic errors but cannot
  confirm that an extracted value matches its source paper. The source PDFs are not included in this public repository
  because many are subject to publisher copyright and licensing terms that do not permit their redistribution. Their
  absence reflects those legal and licensing restrictions, not a decision by the author to withhold the underlying sources.
- The audit found, and this repository corrected in the open, errors of the AI's own making: stale figures, two papers
  counted twice, a sign-versus-valence error in a synthesis, provenance gaps. See `AUDITING_GUIDE.md` §4 and
  `00_admin/audits/2026-09-28_repository_audit.md`. Assume more exist.
- Reviewer labels in the databases (`Claude-AI-fulltext-YYYY-MM-DD`, `Claude-AI-audit-…`, and older variants such as `Claude`)
  identify AI-made decisions; **73 decided full-text rows carry no reviewer label** and their provenance is unknown.
- No pooled estimate exists and none is claimed; the syntheses report direction of association, not effect size or GRADE certainty.

## A second AI tool appears in one file

`06_outputs/slides/Water_Access_Evidence_Diagnostic_slides_2026-09-29.pdf` is a slide summary of the preliminary report that the researcher produced
with a different AI tool (its footers read "A Gemini Notebook", i.e. Google NotebookLM). It is kept unaltered for reference; where it differs from the
current report the report is right — see `06_outputs/slides/README.md`. Nothing else in the repository was produced with that tool.

## Third and fourth AI tools: two independent second reviewers on part of the full-text decisions (2026-10-03)

To begin closing the provenance gap on full-text decisions with no independent check, 99 of the 226 reviewer-2 queue rows (tiers
1-3; those whose PDF was available) were re-screened **blind** by two different model families — the Codex CLI (OpenAI,
`gpt-5.6-sol`) and the Gemini CLI (Google, `gemini-3.1-flash-lite` / `gemini-2.5-flash`) — each of which saw only the protocol
criteria and the paper, never Claude's decision or reasoning. Decisions are recorded in `full_text_screening_database.csv` under
`reviewer_2` labels `Codex-gpt-5.6-sol-reviewer2-fulltext-2026-10-03` / `Gemini-...`, with `conflict = true` where a model disagreed
and `final_decision` left to the researcher. **This is an AI-versus-AI check, not a human check**: it detects decisions that a
second model reads differently, it does not certify either side as correct.

**The main finding is a substantial disagreement rate on tier 2** (the stratified sample of the AI's own full-text excludes): of
62 excludes independently re-read, 32 (52%) were judged `include` by the independent model, concentrated in exclusion codes E01
"wrong topic" and E06 "engineering only." This has not been human-adjudicated and nothing was auto-corrected — every disagreement
is a `conflict = true` row awaiting the researcher. Full technical disclosure (exact tools, versions, prompts, blinding protocol,
known limitations, and how to reproduce or extend this work) is in `_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md`; the row-by-row
report is `_reviewer2_codex/REVIEWER_2_AGREEMENT_2026-10-03.md` (`CHANGELOG.md` 2026-10-03).

## Where to check

`AUDITING_GUIDE.md` (how to verify and challenge), `00_admin/DECISIONS_AND_OPEN_ITEMS.md` (what is undecided and what was a
judgment call), `00_admin/CURRENT_FIGURES.md` and `python3 code/analysis/verify_repository.py` (numbers re-derived from the data),
`code/provenance/` (the scripts that wrote the data), `CHANGELOG.md` (every change, dated).

## For manuscripts and citations

Any manuscript based on this work should state the AI use in its title or subtitle and methods, name the tool as "Claude
(Anthropic)", state which stages were AI-conducted using the table above, and report the verification status honestly.
Journals' and funders' AI-disclosure policies vary; check the target venue's before submission.

*Version-specific model identifiers are deliberately not recorded in this repository's files; the per-decision reviewer labels and
`CHANGELOG.md` dates identify when each AI decision was made.*
