# A6 tier-3 check: comparison plan, fixed before any second-AI result exists

*Written 2026-11-18 by Claude at the PI's request. The git commit that adds this file is its timestamp. **No second-AI result and no human verdict on the 50 tier-3 records existed in the repository when this was written.** Any later change to this plan is made in a new dated section below, never by editing the text above it, and is logged in `DEVIATIONS_REGISTER.csv`.*

## What is being checked

The 50 records in the reviewer-2 queue with `priority_tier = 3`: AI full-text **includes** that no second reviewer has read. The question for each record is whether the include decision survives an independent read of the paper (screening criteria in `INCLUSION_EXCLUSION.md`, including the 2026-10-13 narrow reading of criterion 2), and, for the human only, whether the extraction row matches the paper.

Three views are compared per record: the original AI decision (Claude, from the queue), a second AI (Gemini, blind, brief in `GEMINI_HANDOFF_BRIEF_2026-11-17.md`) and the human (CK, on the evidence cards). The human decides first and without any second-AI output.

## Inputs (frozen when results arrive)

- Human: the filled `A6_TIER3_FILL_IN_SHEET_2026-11-15.csv`.
- Second AI: `gemini_review/screening/GEMINI_SCREENING_*.csv` plus per-record JSON and the raw API responses.
- Original AI: `full_text_reviewer_2_priority_queue_2026-09-28.csv`, column `ai_decision`.
- Second AI's input file: `A6_TIER3_BLIND_INPUT_FOR_SECOND_AI_2026-11-18.csv` (shuffled with seed 20261118, no tier, no AI decision, no extraction, no study ID).

## Analysis (deterministic; `code/screening/compare_a6_reviews.py`)

1. **Per-record status**: all three agree; DISAGREEMENT; cannot_tell involved; human not yet decided; second AI missing.
2. **Pairwise raw agreement**: original AI vs human, second AI vs human, original AI vs second AI, among records where both decided include or exclude. `cannot_tell` is reported, not forced into a side.
3. **No kappa for tier 3.** Every original-AI decision here is "include", so chance-corrected agreement is undefined. Raw counts and the list of disagreements are the output.
4. **Disagreement list**: every record where at least one of the three says exclude while another says include. The PI looks at these first. There is no pass/fail threshold; none was pre-set and none will be invented after seeing the numbers.
5. **Human audit columns**: counts of records with `paper_read` other than `full`, and records where the human reports seeing AI output before deciding. These are reported next to every agreement figure so a reader can discount accordingly.
6. **Extraction check (human only)**: the number of records where the human marked `extraction_matches_paper = N`, with the human's comments. This is a count of flagged mismatches, not an error rate for the corpus.

## Controls on the second AI (`code/screening/verify_second_ai_quotes.py`)

- **Quote verification**: every quotation cited by the second AI is checked against the paper text. The verified share is reported for the batch. A share below 100% is reported as is; unverified quotes are not corrected or removed.
- **Self-consistency**: 10 records, chosen by seed 20261118 from the shuffled input file (orders 1 to 10), are run a second time with identical settings. The flip rate (decision changed between runs) is reported. A second AI that disagrees with itself cannot be read as a signal about Claude.
- **Raw outputs preserved**: the raw API request and response for every call are archived, not just the parsed result.

## What this check can and cannot show

- It checks the include decision on a **non-random** set: the 50 tier-3 records were chosen as a random check of AI includes within the queue's design, and the queue does not cover the 1,072 includes. A result here does not generalise to all includes.
- No control records with a known human answer are mixed in. If the PI wants calibration against the 197 earlier human second-review decisions, control records should be added and this plan amended in a dated section before the run.
- The second AI is a different model family but is still an AI. Agreement between two AIs is not human verification and is not counted as such.
- The original AI decision and the second AI's training overlap in unknown ways. Independence is a design aim, not something this check proves.

## Who does what

The PI records all human verdicts and every field with `ck_` in its name. Claude runs the comparison script and writes the report, and the script is the only step that produces numbers. Anyone can rerun it from the three input files.

## Dated amendments

*(none)*
