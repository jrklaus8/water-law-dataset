# Second-Coder Validation Protocol (Route B)
## Inter-Coder Reliability for the `other_water` Residual

**Purpose:** Establish independent validation of the coding engine's residual
by having a second coder classify a stratified sample of `other_water` decisions,
then computing Cohen's kappa to measure inter-coder agreement.

**Why this matters:** The conflict-of-interest concern is that the engine was
designed by the same researcher who authored the thesis the engine is meant to
support. A second coder — blind to the thesis — breaks that epistemic loop.
Even a partial validation (100–500 decisions) materially strengthens the
methodology for peer review at JELS, Law and Society Review, or Jurimetrics.

---

## Who Should Do This

**Ideal second coder:** A lawyer with reading ability in Portuguese AND Dutch,
familiar with administrative law in at least one of the three jurisdictions.

**Minimum requirement:** A lawyer with Portuguese reading ability who can code
the Brazil residual (818 genuine cases). A separate Dutch-language coder for
the Netherlands residual (338 genuine cases) would be ideal but optional given
the low count.

**Compensation:** Budget approximately 30–50 hours for a 200-case sample.
At typical RA rates (CAD 25–35/hr), total cost CAD 750–1,750.

---

## Sampling Strategy

A stratified random sample, not a simple random sample. Strata:

| Stratum | N to code | Rationale |
|---|---|---|
| Brazil genuine residual (has water vocab) | 150 | Primary concern for thesis |
| Netherlands genuine residual (has water vocab) | 30 | Spot check only |
| Canada genuine residual (has water vocab) | 20 | Spot check only |
| **Total** | **200** | Minimum viable for kappa calculation |

Generate the sample with:
```bash
python validation/generate_second_coder_sample.py --n 200 --seed 42
```
This produces `validation/second_coder_sample.csv` with pre-populated columns
for the coder to fill in.

---

## Coding Categories

The second coder assigns ONE of the following labels to each decision:

| Code | Label | Description |
|---|---|---|
| `TAR` | tariff_dispute | Billing, meter readings, charges, debts to water utility |
| `CON` | connection_refusal | Denial, suspension, or reconnection of water supply |
| `QUA` | water_quality | Contamination, potability, boil-water advisory |
| `INF` | informal_settlement | Water access in irregular, informal, or unregistered areas |
| `GRD` | groundwater | Aquifer, well, groundwater abstraction |
| `SAN` | sanitation_sewage | Sewage, wastewater, ETE, drainage |
| `FLD` | flooding | Flood damage claims, waterlogging |
| `RIP` | riparian_waterway | Watercourse, riverbank, navigation rights |
| `ENV` | environmental_protection | Manancial, mata ciliar, APA, wetland protection |
| `PLN` | spatial_planning_water | Planning permits with drainage/flood-risk dimension |
| `WBD` | waterboard_governance | Water board levies, keur, peil decisions |
| `PIP` | pipe_leak_damage | Burst main, leak, infrastructure damage liability |
| `THF` | water_theft_fraud | Illegal connection, meter tampering |
| `REG` | regulatory_permit | Water licence, permit, abstraction right |
| `HYD` | hydroelectric_dam | Dam, reservoir, hydroelectric |
| `IRR` | irrigation_agricultural | Irrigation, agricultural water use |
| `FSH` | fisheries_water | Fisheries, aquaculture |
| `INF` | water_infrastructure_contract | Procurement, concession, PPP |
| `FP`  | not_water_related | False positive — not a water law case |
| `OTH` | other_water | Genuine water case, does not fit any category |
| `UNK` | unclear | Cannot determine from available text |

**Decision rule:** When in doubt between two substantive categories, apply the
one that best describes the PRIMARY legal dispute (the claim or ground of appeal),
not incidental mentions of water.

---

## Coding Guide for Brazilian Cases

See `validation/coding_guide_brazil.md` for detailed decision rules with
worked examples in Portuguese.

Key distinctions:

**`TAR` vs `CON`:**
- TAR = dispute is about *how much* is owed or *whether* a charge is valid
- CON = dispute is about *whether* the utility must provide the service at all

**`CON` vs `INF`:**
- CON = the right to be connected regardless of area type
- INF = the connection issue is *specifically* because the address is irregular/
  informal/unregistered

**`FP` vs `OTH`:**
- FP = the word "água" appears but the case is about something else entirely
  (e.g., a property sale near water, a flood insurance claim, a criminal case)
- OTH = the case is substantively about water governance but doesn't fit a named category

---

## Cohen's Kappa Calculation

After both coders have coded the same sample, run:

```bash
python validation/kappa_calculator.py \
    --coder1 validation/coder1_labels.csv \
    --coder2 validation/coder2_labels.csv
```

**Interpreting kappa:**

| κ range | Interpretation | Implication for the thesis |
|---|---|---|
| ≥ 0.80 | Near-perfect agreement | Engine validation is strong |
| 0.75–0.80 | Substantial agreement | Acceptable for peer review |
| 0.60–0.75 | Moderate agreement | Worth discussing in methods section |
| < 0.60 | Fair/poor agreement | Revise categories or coding guide |

For a jurimetric coding study, κ ≥ 0.75 is the standard threshold used by
the Caselaw Access Project, the Stanford Codebook on Constitutional Decisions,
and the Brazilian jurimetrics literature (Epstein & Martin 2014; Hartmann 2022).

---

## Reporting in the Methods Section

After completing this protocol, add the following (adapt to your results):

> **Inter-coder reliability.** A stratified random sample of 200 decisions
> classified as `other_water` by the automated engine was independently coded
> by a second coder (a Brazilian-trained lawyer with administrative law expertise)
> blind to the thesis. Cohen's kappa for the 21-category governance scheme was
> κ = [X.XX] (95% CI: [X.XX, X.XX]), indicating [substantial / near-perfect]
> agreement. Of the 150 Brazilian residual cases in the sample, [N] were
> reclassified to substantive categories: [n] to `connection_refusal`, [n] to
> `informal_settlement`, [n] to `tariff_dispute`, and [n] to `pipe_leak_damage`.
> These reclassifications changed the Brazil connection-refusal count by [X]%
> and the informal-settlement count by [Y]%, leaving the core Administrative
> Ghost finding [unchanged / within the margin of / materially affected by]
> the residual classification.

---

## Files Produced by This Protocol

| File | Description |
|---|---|
| `validation/second_coder_sample.csv` | 200-case stratified sample with text |
| `validation/coder1_labels.csv` | Author's labels (generated by `generate_second_coder_sample.py`) |
| `validation/coder2_labels.csv` | Second coder's labels (filled in manually) |
| `validation/kappa_results.json` | κ statistic, CI, category-level agreement |

All files should be committed to the repository alongside the published article
to satisfy open-data requirements at JELS, L&SR, and Jurimetrics.
