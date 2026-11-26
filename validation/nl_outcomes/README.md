# Netherlands outcome coding (FUTURE_WORK.md, Priority 1): first pass

Status: **machine-coded, not yet human-validated.** Do not cite the rates below as findings until the blind check sheet is completed.

## What was done (2026-11-26)

- Source: `water_law_global_coded.csv` from Harvard Dataverse (doi:10.7910/DVN/C9PEFS), 68,654 Dutch rows, `win_loss` = `not_coded` for all of them.
- Full XML retrieved from `data.rechtspraak.nl` for **3,682 decisions**: every Dutch row in a specific governance category (2,182 rows; everything except `other_water` and `not_water_related`) plus a **random sample of 1,500 `other_water` rows** (seed 42).
- The dispositive part was extracted and classified by `utils/nl_outcome_coding.py` (rule based, standard library only, 13 offline tests in `tests/test_nl_outcome_coding.py`). Each row stores the rule that fired and the dispositive text, so every label can be audited.
- **Added later the same day:** a keyword screen of the dataset's own `summary` field (water, drinkwater, riool, waterschap, dijk, grondwater, lozing and similar) found only **1,337 of 50,883 `other_water` rows (2.6%)** with any water term; 9,974 (19.6%) have an empty summary. All 1,337 were retrieved and coded (total now 4,980 distinct decisions; 39 of the random-sample rows are also keyword matches and are labelled `other_water_keyword_match`, with `in_random_sample` = 1). The keyword list is crude (it matches "Watertorengebied", a zoning plan name) and the screen misses rows whose summary is empty, so it bounds relevance, it does not measure it.
- Not done: the other ~49,500 `other_water` rows, the 15,589 `not_water_related` rows, and any LLM fallback.

## Files

| File | Content |
|---|---|
| `nl_outcomes_coded.csv` | One row per ECLI: outcome label, rule, `multi_step` flag, dispositive text |
| `nl_outcome_summary.csv` | Counts, share of challenges upheld among decided cases, Wilson 95% interval, per category |
| `manual_check_sample_BLIND.csv` | 150 rows (120 labelled, 30 unresolved) with the machine label hidden. Fill `human_label`, then compare |
| `build_outcome_table.py` | Rebuilds the coded table from the fetch checkpoint |

## First-pass results (share of decided challenges upheld = WIN / (WIN + PARTIAL + LOSS))

| Group | n | Decided | Upheld |
|---|---|---|---|
| All specific categories | 2,182 | 1,849 | 24.7% (95% CI 22.8 to 26.7) |
| `other_water` rows with a water term in the summary | 1,337 | 1,189 | 23.5% (21.1 to 26.0) |
| Specific categories + keyword matches | 3,519 | 3,038 | 24.2% (22.7 to 25.7) |
| Random `other_water` sample | 1,500 | 1,025 | 24.4% (21.9 to 27.1) |
| `connection_refusal` | 12 | 12 | 16.7% (4.7 to 44.8) |
| `sanitation_sewage` | 44 | 38 | 28.9% (17.0 to 44.8) |
| `flood_protection` | 1,266 | 1,093 | 23.0% (20.6 to 25.5) |

The upheld rate is almost identical (about 24%) across every sample, which suggests it reflects the court system more than the topic. Per-category rows with very small n (connection_refusal, water_quality, irrigation_agricultural) carry intervals too wide to support any of the three Priority 1 hypotheses.

## Things a reader must know

1. **The three hypotheses are still untested.** "Upheld" is the success rate of whoever challenged the decision at that instance. Appellant identity (individual, municipality, utility, firm) is not coded, and the hypotheses depend on it. Many decisions in this corpus (flood protection, nature permits) are brought by organisations, not households.
2. **Error found in the FUTURE_WORK.md recipe.** Its regex reads "verklaart het hoger beroep gegrond; vernietigt de uitspraak; verklaart het beroep ongegrond" as WIN. That sequence means the original challenge failed. The coder follows the final merits clause and sets `multi_step = 1` (131 rows). Its XML example also looks for `<section role="beslissing">`, which these documents do not contain; the dispositive is a run of `<para>` elements after a "Beslissing" paragraph.
3. **No machine-readable body for 306 of the 1,500 random `other_water` rows (20%).** These are district-court records where Rechtspraak.nl publishes metadata only. They cannot be outcome coded from this source, and the 1,500-row sample suggests the gap is concentrated in `rechtbank` decisions.
4. **144 rows in the specific categories and 84 in the random sample are UNCLASSIFIED** (costs-only orders, preliminary questions to the CJEU, complex multi-party dispositions) and 103 are INTERIM (tussenuitspraak). They are left unlabelled on purpose, not guessed.
5. **Dataset quality flag for the PI:** 50,883 of 68,654 Dutch rows (74%) sit in the catch-all category `other_water`, and the first row inspected (ECLI:NL:RVS:2016:159) concerns childcare benefit advances, not water. Only 2.6% of those rows mention a water term in their summary (point 3 of the added note above). The headline "68,654 Dutch water-law decisions" therefore probably overstates the water-specific corpus by an order of magnitude; the defensible core is the roughly 3,500 rows coded here. A human read of a random sample of the keyword-negative rows is needed to confirm.
6. Rule precision is **unmeasured**. The earlier "87% regex, 96% with LLM" figure in FUTURE_WORK.md does not apply to this implementation.

## Next steps for the researcher

1. Fill `human_label` in `manual_check_sample_BLIND.csv` (WIN, LOSS, PARTIAL, INADMISSIBLE, REMAND, INTERIM, NO_MERITS_RULING, or UNCLEAR, from the appellant's perspective) and compute agreement against the key rebuilt from `nl_outcomes_coded.csv`.
2. Decide whether to extend retrieval to the other 48,000 `other_water` rows (about 2 hours at 8 requests per second) or first test water relevance on the random sample.
3. Decide how to code appellant identity (FUTURE_WORK.md optional extension), since it is what the hypotheses need.
