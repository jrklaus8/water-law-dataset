# Codebook

Canonical definition of every variable in the Global Water Law Judicial
Decisions Dataset. If you are interpreting, extending or replicating this
dataset, this file is authoritative. Where prose elsewhere in the repository
disagrees with this file, this file is correct and the prose is a bug.

- **Dataset version:** v0.3.0
- **Coverage:** 2016–2026 (plus a hand-coded TJSP slice, 1997–2015)
- **Unit of observation:** one judicial decision
- **n:** 83,596 (Brazil 11,724 · Canada 3,218 · Netherlands 68,654)
- **Producing code:** `utils/merge_national.py` then `utils/jurimetric_coding.py`

Related: `DATA_ACCESS.md` (where the data is), `VERIFICATION.md` (how to check
it), `validation/` (inter-coder reliability).

---

## 1. Source variables

Emitted by `utils/merge_national.py`. Every value originates from the court's
own published record; none is derived.

| Variable | Type | Definition | Missingness |
|---|---|---|---|
| `country` | categorical | `Brazil`, `Canada`, `Netherlands` | never |
| `tribunal` | string | Court abbreviation (`TJSP`, `RvS`, `CBb`, `FC`) | never |
| `court_name` | string | Full court name where the source supplies one | frequent |
| `case_id` | string | Court's own identifier. Netherlands: ECLI. Brazil: CNJ process number, or an ESAJ internal key for pre-2008 TJSP records. Canada: neutral citation or style of cause | never |
| `title` | string | Case title or style of cause. Netherlands: often the ECLI repeated | rare |
| `date` | ISO date | Date of judgment as published | occasional |
| `year` | integer | Year extracted from `date`, or from the ECLI where `date` is absent | rare |
| `case_type` | string | Procedural class (`Apelação Cível`, `Hoger beroep`) | frequent |
| `chamber` | string | Chamber, panel or division | frequent |
| `judge` | string | Reporting judge (*relator*) where published | frequent, Brazil-dominant |
| `legal_area` | string | Court's own subject classification (`rechtsgebied`, TJSP *assunto*) | frequent |
| `summary` | text | **The court's own headnote.** Brazil: *ementa*. Netherlands: *inhoudsindicatie*. Canada: case digest | occasional |
| `url` | URL | Address captured at scrape time. May rot; prefer `permalink` | frequent for historical TJSP |

> **`summary` is not the judgment.** It is an editorial artefact written by the
> court or its registry, and its length varies from a full paragraph to a single
> clause. Full decision text is not in the dataset; see `DATA_ACCESS.md` §3–4.
> Every coded variable below is derived from `summary` plus metadata, never from
> the judgment, which caps what any of them can measure.

---

## 2. Coded variables

Emitted by `utils/jurimetric_coding.py`. All are **regex-derived, not
hand-coded**, except where a validation subset was hand-checked (§5).

The engine builds two searchable fields and uses them for different variables:

- `_text` — all metadata plus the headnote. Used for `governance_cat` only,
  because court name and subject classification help identify dispute type.
- `_text_sub` — headnote fields only (`ementa`, `summary`, `text`, `snippet`).
  Used for every other variable, to stop a court's own subject label
  (for example TJSP's `legal_area = "Direito à Água / Saneamento"`) from being
  read as substantive framing by the judge.

### 2.1 `governance_cat` — type of dispute

Categorical, exactly one value per decision, exhaustive. 21 possible values:
19 substantive categories plus `not_water_related` and `other_water`.

**Assignment order matters.** The engine applies, in sequence:

1. **Water-vocabulary gate.** No water-core term in `_text` → `not_water_related`,
   and no category is ever considered. See the limitation in §4.1.
2. **Brazil rescue patterns** for three categories the main table was shown to
   miss during the residual audit (`tariff_dispute`, `connection_refusal`,
   `pipe_leak_damage`).
3. **Main category table**, first match wins, in the order below.
4. **Fallback.** Water vocabulary present but no category matched →
   `other_water`.

Because first match wins, a decision matching two categories receives the one
earlier in the table. Categories are therefore **priority-ordered, not
mutually exclusive in substance**.

| # | Value | Definition |
|---:|---|---|
| 1 | `tariff_dispute` | Billing, meter readings, charges, debts owed to a water utility |
| 2 | `connection_refusal` | Denial, suspension, disconnection or reconnection of supply |
| 3 | `water_quality` | Contamination, potability, boil-water advisories |
| 4 | `informal_settlement` | Water access in irregular, informal or unregistered areas |
| 5 | `groundwater` | Aquifers, wells, abstraction |
| 6 | `flooding` | Flood damage claims, waterlogging, *wateroverlast* |
| 7 | `riparian_waterway` | Watercourses, riverbanks, navigation |
| 8 | `irrigation_agricultural` | Irrigation and agricultural water use |
| 9 | `sanitation_sewage` | Sewage, wastewater, treatment plants, drainage |
| 10 | `environmental_protection` | *Mananciais*, *mata ciliar*, APAs, wetlands |
| 11 | `flood_protection` | Dikes, *waterkering*, flood defence works |
| 12 | `spatial_planning_water` | Planning permits with a drainage or flood-risk dimension |
| 13 | `waterboard_governance` | Water board levies, *keur*, *peilbesluiten* |
| 14 | `pipe_leak_damage` | Burst mains, leaks, infrastructure damage liability |
| 15 | `water_theft_fraud` | Illegal connections, meter tampering |
| 16 | `water_infrastructure_contract` | Procurement, concessions, PPPs |
| 17 | `fisheries_water` | Fisheries and aquaculture |
| 18 | `hydroelectric_dam` | Dams, reservoirs, hydroelectric works |
| 19 | `regulatory_permit` | Water licences, permits, abstraction rights |
| 20 | `other_water` | Water vocabulary present, no category matched |
| 21 | `not_water_related` | No water vocabulary; a false positive of the keyword scrape |

**Priority-order caveat.** `environmental_protection` (10) sits above
`flood_protection` (11) and `spatial_planning_water` (12), so a *mananciais*
case that also concerns planning is coded environmental. Any cross-category
claim should be checked against `gov_matched_rule` (§3) rather than assumed.

### 2.2 `win_loss` — who prevailed

Categorical. **Brazil only.** Canada and the Netherlands are `not_coded`; this
is the outcome gap recorded in `README.md` and `FUTURE_WORK.md`, not an error.

| Value | Meaning |
|---|---|
| `user_wins` | The access-seeker, consumer or plaintiff prevailed |
| `utility_wins` | The utility, municipality or defendant prevailed |
| `mixed` | Partial success, or both directions matched |
| `unclear` | Brazilian case whose headnote does not disclose the outcome |
| `not_coded` | Non-Brazilian case; outcome coding was never attempted |

Assigned by three tiers of decreasing pattern strength; where both a
user-favourable and a utility-favourable pattern match at the same tier the
result is `mixed`. **Treat `unclear` as missing, not as a category**, and report
what share of the Brazilian subset it covers alongside any outcome result.

### 2.3 Binary flags

All are 0/1, derived from `_text_sub`. Each records **the presence of language**,
not a finding of fact by the court. `hr_language = 1` means the headnote used
rights vocabulary, not that a right was recognised.

| Variable | 1 means | Scope |
|---|---|---|
| `hr_language` | Human rights or right-to-water framing | all |
| `sust_language` | Sustainability or environmental framing | all |
| `mp_involvement` | *Ministério Público* appears as a party or intervener | Brazil only; always 0 elsewhere |
| `indigenous_water` | Indigenous or First Nations water rights | all; Canada-dominant |
| `public_interest` | Public interest or collective action framing (*ação civil pública*, class proceedings) | all |

Because these run on headnotes, they are **lower bounds**. A decision that
engages a right without the registry saying so scores 0.

---

## 3. Audit variables

Emitted alongside the coded variables so that any classification can be checked
without re-running the pipeline. See `VERIFICATION.md` Level 2.

| Variable | Definition |
|---|---|
| `gov_matched_rule` | The rule that assigned `governance_cat`. `FILTER:no_water_vocabulary` (the gate), `RESCUE:<name>` (a Brazil rescue pattern), `GOV_CATS:<category>#<n>` (pattern *n* of that category), `FALLBACK:water_vocab_no_category` |
| `gov_matched_span` | The substring the rule matched, trimmed to 300 characters. Empty for the gate and fallback rules, which fire on absence |

`explain_governance()` in `utils/jurimetric_coding.py` is the single source of
truth; `code_governance()` delegates to it, so these columns cannot drift from
the labels.

### Resolver variables

Added by `utils/resolve_case.py`, not present in the deposited CSV.

| Variable | Definition |
|---|---|
| `permalink` | Most durable public address for the decision |
| `permalink_kind` | Durability class; see `DATA_ACCESS.md` §4.1 |
| `identifier` | Normalised identifier (ECLI, or CNJ number in canonical form) |
| `fulltext_url` | Machine-retrievable full text, Netherlands only |

---

## 4. Known defects

Recorded here because a codebook that hides them is worthless.

### 4.1 The Dutch water gate cannot see compound nouns

`_WATER_CORE_RE` gates the entire classifier and is written with `\b` word
boundaries. This is correct for Portuguese and English and **wrong for Dutch**,
which compounds nouns without spaces: `\bwater\b` does not match `waterwet` or
`watervergunning`, and `\bgrondwater\b` does not match `grondwateronttrekking`.
Affected decisions are returned `not_water_related` before any category is
considered.

Measured: in `validation/second_coder_sample_raw.csv`, 65 of the 100 decisions
in the `NL_broad_water` stratum carry such a compound, and the human coder
labelled 61 of them WATER. This is the mechanism behind the 0.3579 precision
recorded for that stratum in `validation/precision_recall_results.json`.

`utils/audit_trail.py` quantifies it across the dataset and changes no label.
**Any analysis of the Netherlands subset should treat `not_water_related` as
over-inclusive.**

### 4.2 Two protocol codes collided

`validation/second_coder_protocol.md` assigned the short code `INF` to both
`informal_settlement` and `water_infrastructure_contract`, and omitted
`flood_protection` entirely. A second coder working from the protocol could not
distinguish the two `INF` categories and was never told the nineteenth existed.
`informal_settlement` is thesis-critical, so any hand-coding that used those
short codes should be re-checked. Fixed in the protocol as of this version:
`informal_settlement` = `INF`, `water_infrastructure_contract` = `ICT`,
`flood_protection` = `FPR`.

### 4.3 Headnote ceiling

Every coded variable is derived from the court's summary. Where an *ementa* or
`inhoudsindicatie` is a single clause, neither the engine nor a human coder can
classify reliably. The `UNCERTAIN` labels in `validation/coder1_labels.csv` mark
exactly these cases.

### 4.4 Brazil is a convenience sample

Eight of twenty-seven *Tribunais de Justiça* are present. The other nineteen
were inaccessible (status table in `README.md`), and the accessible eight are
those with modern search infrastructure, which correlates with state wealth.
**The Brazilian subset is not a national census** and should not be used for
claims about Brazil as a whole without that caveat.

### 4.5 Priority ordering is not substantive exclusivity

See §2.1. First match wins.

---

## 5. Validation status by variable

| Variable | Validation | Evidence |
|---|---|---|
| `governance_cat`, water/not-water gate | Hand-coded stratified sample (n=207) plus an independent second-coder pass (n=91) | `validation/precision_recall_results.json`, `kappa_results.json`, `kappa_results_ruled.json` |
| `governance_cat`, the 21 categories | **Not validated.** Only the upstream gate has been checked | `validation/README.md` |
| `win_loss` | Not independently validated | — |
| Binary flags | Not independently validated | — |

**Reliability figures, all reproducible via
`python validation/apply_decision_rules.py`:**

| Measure | κ | n | Note |
|---|---:|---:|---|
| Three-label, no decision rule | 0.5684 | 91 | Baseline; what `kappa_results.json` holds |
| Three-label, RULE-BR-MANANCIAIS `narrow` | 0.7975 | 91 | |
| Three-label, RULE-BR-MANANCIAIS `standard` | 0.8145 | 91 | |
| Three-label, RULE-BR-MANANCIAIS `broad` | 0.8506 | 91 | |
| Binary WATER/NOT_WATER, `UNCERTAIN` dropped | 0.9321 | 59 | |

`validation/README.md` reports a headline of 0.832. That figure lies inside the
rule-variant spread above but is **not reproducible from any committed
artefact**, because the rule's exact scope was never written down. Cite a
variant by name and the kappa it produces, or cite the 0.5684 baseline. Do not
cite 0.832 without saying which rule produced it.

Population-weighted filter precision on `not_water_related` is 99.79%, but the
mass sits in the `NL_plain` stratum where precision is 1.0. Where water
vocabulary is present, precision is 0.3579. **Cite both numbers or neither.**

---

## 6. Changing the coding

The category patterns are research instruments. If you change one you change
the findings, so:

1. Run the regression tests first: `python -m pytest tests/ -q`. They pin the
   current behaviour on known decisions.
2. Make your change, then run them again. Failures tell you exactly which
   classifications moved.
3. Update the expected values **only** with a note in the commit message saying
   why the new behaviour is correct.
4. Regenerate the audit bundle and diff `audit_rule_coverage.csv`. A change that
   moves thousands of decisions between categories needs saying out loud.
5. Bump the version in `CITATION.cff` and deposit a new DOI version. The
   deposited CSV and the code that produced it must stay in step.

See `CONTRIBUTING.md` for adding a court or a jurisdiction.
