# Second-extractor sample (independent check of the AI's extraction)

The AI extracted every study and no human has re-extracted any of them, so **the error rate of the extraction is unknown**. This folder holds the cheapest
way to estimate it: a seeded, stratified sample of 60 studies (seed 20260929) drawn **only from S001–S200** — the 200 includes whose full-text screening decisions you have already reviewed — and a blank comparison sheet. *(Redrawn 2026-10-04; the 2026-09-29 sheet drew from all studies and has been deleted. If you started filling the old one, finish it separately — the two samples overlap only by chance.)*

**What to do (about 15–20 minutes per study for someone who knows the field):**
1. Easiest: copy `second_extractor_sheet_BLANK_2026-10-04.xlsx` (same rows; the verdict column is a Y / N / cannot_tell drop-down) and fill that copy; the scorer reads it directly. Or copy `second_extractor_sheet_BLANK_2026-10-04.csv` to a new name (for example `..._FILLED_<initials>.csv`). Never edit the BLANK file (it is regenerated).
2. For each row, read the paper *before* looking at `ai_value` if you can (the AI's value can anchor you). Write what you find in `second_extractor_value`.
3. Set `agrees (Y/N/cannot_tell)`: **Y** = same substance (wording and rounding can differ), **N** = a real difference, **cannot_tell** = the paper does not let you decide.
4. Score it: `python3 code/analysis/score_second_extractor_sheet.py path/to/filled.csv` (or `.xlsx`) (disagreement rate per field and overall, Wilson 95% intervals).

**What the sample can and cannot tell you.** 60 studies × 9 fields (540 rows). Any single field's interval is about ±10 points, so read the overall rate. The pool is S001–S200 minus five rows whose own notes say only the abstract or citation was read (S015, S019, S027, S079, S116), so the sample says nothing about how well the later extractions (S201 onward) were done — **it cannot be generalised to the whole corpus**, which is the price of using papers you already know. You confirmed those studies' *include decisions*, not their extractions, so you still have to read the paper against each field. Strata, drawn in this order without overlap and capped at what S001–S200 holds: RoB 2 / ROBINS-I 8 (all available), effect-size rows 5 more (9 of the 60 have an effect-size row; that is all S001–S200 has), AMSTAR 2 / NONE 1 (the rest are among the excluded thin rows), JBI 8, MMAT 8, CASP 8, Legal Framework 8, then a random top-up of 14. `where_the_AI_looked` shows the page or table the AI recorded, when it recorded one.

**If the overall disagreement is high** (a threshold is the researcher's call), the appropriate response is a wider second extraction, not adjusting this sample.

## What the result can speak for

The 60 studies are drawn from S001-S200 only (the includes the researcher already knows), so the measured disagreement rate describes the AI's extraction of those 200 studies. That subset skews recent (about three quarters published 2020 or later, against about 43% of all extracted studies), and the later batches (S201-S1164) were extracted by the same process but are not sampled. `score_second_extractor_sheet.py` prints this caveat with every score; carry it into the limitations when reporting the rate.
