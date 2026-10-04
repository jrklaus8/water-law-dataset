# Session handoff — state of the project at the end of the 2026-10-04 autonomous session

*For the next AI session or reviewer picking this up. The researcher-facing list is `RESEARCHER_DECISION_BRIEF_2026-10-04.md`; this file says how to resume and what not to redo. Dated entries: `CHANGELOG.md`.*

## State in one paragraph

Branch `claude/legal-last-mile-review-spec-8ri0zs` is pushed and clean; `python3 code/analysis/verify_repository.py` passes (135 checks), and a fresh clone of the pushed branch also passes. Everything the AI can do without the researcher's decisions or PDFs it cannot reach is done: full-text re-extraction of 79 studies, 47 of the 62 effect-size rows compared with their sources, AMSTAR 2 for 12 of 23 reviews, a tool-reclassification proposal, supporting texts, a manuscript draft, an adjudication sheet for the blind-reviewer disagreements. What remains needs the researcher (decisions 1-14 in the brief, the human second extraction, PDFs) or PDFs that are not in Drive.

## How to resume

1. `git pull`, then `bash code/analysis/regenerate_all.sh` (rebuilds every derived file in dependency order, runs the A16 script tests in `code/tests/`, then the verifier). Run from `legal-last-mile-systematic-review/`.
2. Change data only with a small dated script under `code/provenance/audit_and_repair/` that asserts row counts and writes atomically (pattern: `enrich_s1163_ci_2026-10-04.py`), add a dated `CHANGELOG.md` entry, regenerate, verify, commit. Word versions are made with `pandoc … --reference-doc=<a reference .docx>` (not in the repository).
3. Re-extraction from a Drive full text: write `code/provenance/audit_and_repair/reextract_2026-10-04/<study>.json` (`nonprefix: true` for rows without the abstract-only note), run `run_reextract_2026-10-04.py` (idempotent), then `reextract_2026-10-04/build_campaign_notes.py`. **`.gitignore` ignores `*.json`; the folder has an exception line, so `git add` picks the JSONs up. Check `git ls-files` after adding any new JSON.**
4. When the researcher returns a filled A16 sheet: `python3 code/screening/apply_a16_adjudications.py <filled.csv> --reviewer <initials>` (dry run), then `--apply`. Confirmations are written; reversals go to `02_screening/full_text/A16_PENDING_REVERSALS.csv` and are then processed by `python3 code/screening/resolve_a16_pending_reversals.py --reviewer <initials>` (dry run, then `--apply`; scratch-tested). Each new include needs a prepared full-text extraction at `02_screening/full_text/a16_new_includes/<record_id>.json` (format in the script's docstring); the script assigns the study ID and updates the map, extraction, evidence map, full-text database and exclusion log together so the one-to-one checks keep passing. Afterwards the verifier will flag the hand-written study counts (README, root README, evidence-limitations note, RISK_OF_BIAS) — update them from its output.
5. Never apply an open decision (items 1-14) without the researcher's answer; the brief says what each answer triggers.

## What was completed this session (details in `CHANGELOG.md`)

- **Re-extraction campaign:** 79 studies from Drive full texts (25 abstract-only, 54 sparse-audit rows); 9 of the 54 had a materially wrong or incomplete first extraction. Records: `code/provenance/audit_and_repair/reextract_2026-10-04/` (`CAMPAIGN_NOTES.md`).
- **Effect-size check:** `05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv` (all 62 rows): 40 verified, 4 in part, 3 corrected or enriched (S312 and S649 mislabelled but not pooled; S348 and S1163 filled), 15 not checkable (no full text in Drive; list in `DECISIONS_AND_OPEN_ITEMS.md` A17). AI-on-AI, not independent.
- **A16 (independent-model disagreement on AI excludes):** `02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.{csv,md}` (56 records, most likely mis-excludes first, blank decision columns), now stated in the generated limitations, the report and the supporting texts. The disagreement may be a scope question (protocol criterion 2 is literally broad; the original E01 excludes look narrower). Nothing was changed in the screening data.
- **A16 scale and triage (later the same day):** the sheet now projects the blind-reviewer rate per exclusion code (about 468 implied further includes at the models' rate; about 37 under a narrow reading and 366 under the literal reading, from Claude's N/B/X triage with abstract checks of the 15 narrow candidates), and the includes side (3 of 18 sampled unconfirmed includes look excludable; about 160 of 959, range 56-376). All computed by `build_a16_adjudication_sheet.py` and carried into the generated limitations, report and manuscript draft. Two lessons logged: blind reviewers cannot see duplicates (R21CAA5C1809C = S102), and two excludes rest partly on non-significant results (decision 14 / A18).
- **Reproducibility fix:** the campaign JSONs had never been committed (`*.json` ignored); now tracked, so a fresh clone reproduces the counts.
- **Other:** AMSTAR 2 for S328; tool-reclassification proposal (A11); supporting texts; the `AI_USE_STATEMENT.md` PDF wording requested by the researcher (plus one count update).

## Decisions and judgments made this session (reversible)

- Treated the blind Codex/Gemini reviews as AI opinions only; did not auto-correct any screening decision.
- Counted rows with a blank sample size or a generic estimate as *incomplete* in the "materially wrong or incomplete" tally.
- Left S911, S1014, S1097, S1098 and S1105 unchanged although their texts were found: their extractions already rest on the full text and blank sample/effect fields are legitimate for policy or doctrinal papers.
- Mapped S434 as "verified in part": its Table 2 prints a coefficient whose sign contradicts the abstract, but the converted text has no minus signs anywhere, so the table sign cannot be relied on.

## What remains, and the best next steps

1. **Researcher (highest payoff):** decide the scope reading of criterion 2 and work through `A16_ADJUDICATION_SHEET_2026-10-04.csv`, priority 1 first (the 3 rows triaged N are the likeliest mis-excludes; R21CAA5C1809C is a duplicate and can be skipped); decide 14 (results-based exclusions); then answer decisions 1-12 and 14 in the brief; fill `03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv` (the only independent extraction check; the S001-S100 PDFs are not in Drive, so the AI cannot stand in for it); supply PDFs for the 15 unchecked effect-size rows and the 14 strong sparse rows.
2. **AI, after any answer:** apply it with a dated script, regenerate, verify. If decision 11 is "apply", re-answer each moved study's appraisal item by item. If A16 resolves towards the broad reading, run the screening pipeline on the reversed excludes (new includes need extraction, appraisal, effect-size consideration).
3. **AI, no answer needed but blocked on files:** the 15 effect-size rows and 11 unrated AMSTAR 2 reviews need PDFs; none is in the researcher's Drive.
4. **AI, small (A19):** nine substantive full-text-stage excludes were decided on a landing-page abstract (`05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.md`); if the researcher supplies those full texts, re-screen them with the same A16 machinery.
5. **Known limits to keep stating:** AI-on-AI checks are not independent verification; the source PDFs are not in the repository (publisher copyright and licensing); the 1,383 never-assessed records bound the corpus.
