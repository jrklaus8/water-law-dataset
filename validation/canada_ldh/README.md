# Can Legal Data Hunter supply full text for the Canadian rows? (tested 2026-11-27)

**Short answer: for about 10% of them (British Columbia), not for the rest.**

Method: 143 citations drawn at random, up to 6 per court, from the 25 largest courts in the Canadian part of the deposited dataset (3,218 rows), resolved through LDH's `resolve_reference` tool (`ldh_coverage_test.py`). No decision text was stored; the CSV holds only the citation, whether it resolved, the reason if not, the source and the text size. The sample is stratified by court, so the raw 13 of 143 is not a population rate.

| Result | Courts |
|---|---|
| Resolved with full text (every time) | BCSC 6 of 6, BCCA 6 of 6 |
| Resolved occasionally | Federal Court 1 of 6 |
| Never resolved | the other 22 courts tested (all Quebec, Ontario, Alberta, Nova Scotia, New Brunswick and Newfoundland courts and tribunals, the Federal Court of Appeal, and the BC tribunals) |

Reasons for failure: `no_matching_source` 106 (LDH has no source for that court), `no_document` 23 (court recognised, decision absent, including 5 of 6 Federal Court and 6 of 6 Federal Court of Appeal citations), `unreadable_citation` 1. No call errored, so nothing was dropped from the rate.

All 13 hits come from one LDH source, `CA/A2AJ`, with full texts between 11 KB and 211 KB. The two BC courts make up 334 of the 3,218 Canadian rows (10.4%), so the expected coverage of the deposited Canadian set through LDH is about **10 to 11%**. Quebec Superior Court alone is 1,345 rows (42%) and is not available.

Implications for FUTURE_WORK.md Priority 3A: LDH is a front end to the A2AJ dataset, so using the A2AJ project directly should give the same courts and not more. Filling in the Quebec, Ontario and Alberta rows will need another source (the courts' own portals, or SOQUIJ/CanLII under their terms of use), which this test did not examine.

Not tested: whether the coverage gaps close for other citation formats, whether `search` by title finds decisions that `resolve_reference` misses, and whether the BC decisions that resolve are about water (the earlier yacht-lien case suggests many are not).

Repeat with: `LDH_API_KEY=... python validation/canada_ldh/ldh_coverage_test.py CODED_CSV OUT.csv 6 25` (about 15 minutes; the script stops if the account's usage limit is reached).
