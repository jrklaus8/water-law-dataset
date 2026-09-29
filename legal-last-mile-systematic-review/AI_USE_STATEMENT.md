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
| Full-text screening | Read each supplied full text and decided include/exclude with a coded reason | Obtained and supplied the full texts; confirmed 100 includes (S001–S100) | **Only those 100 includes**; no excludes |
| Data extraction (92 fields) | Extracted every study, largely from full text; 66 studies from abstract or metadata only | Supplied documents | **None**; no second extractor |
| Risk-of-bias appraisal | Rule-based batch ratings from extracted fields, using the published instruments' structure | Supplied the official instrument documents | **None**; not a signalling-question read of each paper. One instrument is the project's own and is not validated |
| Classification, effect-size table | Coded and classified | — | None |
| Structured (SWiM) syntheses, feasibility judgment | Drafted, with disclosed judgment calls | Approves and decides | None |
| This repository's audits and corrections | Found and corrected its own errors in the open | Approved merges and exclusions | — |

## Why you should still read it critically

- The same system produced and audited much of the work, so its checks find inconsistencies and arithmetic errors but cannot
  confirm that an extracted value matches its source paper. The source PDFs are not in the repository.
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
