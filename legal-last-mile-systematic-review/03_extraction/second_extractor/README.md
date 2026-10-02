# Second-extractor sample (independent check of the AI's extraction)

The AI extracted every study and no human has re-extracted any of them, so **the error rate of the extraction is unknown**. This folder holds the cheapest
way to estimate it: a seeded, stratified sample of 60 studies (seed 20260929) and a blank comparison sheet.

**What to do (about 15–20 minutes per study for someone who knows the field):**
1. Copy `second_extractor_sheet_BLANK_2026-09-29.csv` to a new name (for example `..._FILLED_<initials>.csv`). Never edit the BLANK file (it is regenerated).
2. For each row, read the paper *before* looking at `ai_value` if you can (the AI's value can anchor you). Write what you find in `second_extractor_value`.
3. Set `agrees (Y/N/cannot_tell)`: **Y** = same substance (wording and rounding can differ), **N** = a real difference, **cannot_tell** = the paper does not let you decide.
4. Score it: `python3 code/analysis/score_second_extractor_sheet.py path/to/filled.csv` (disagreement rate per field and overall, Wilson 95% intervals).

**What the sample can and cannot tell you.** 60 studies × 9 fields (540 rows). Any single field's interval is about ±10 points, so read the overall rate.
Studies still extracted from abstract or metadata only are excluded (no full text to check against). The strata are: effect-size rows 15, RoB 2 / ROBINS-I 8,
JBI 8, MMAT 8, CASP 8, Legal Framework 8, AMSTAR 2 / NONE 5 — drawn in that order without overlap. `where_the_AI_looked` shows the page or table the AI recorded, when it recorded one.

**If the overall disagreement is high** (a threshold is the researcher's call), the appropriate response is a wider second extraction, not adjusting this sample.
