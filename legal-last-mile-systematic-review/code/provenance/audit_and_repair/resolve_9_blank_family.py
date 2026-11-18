import csv, os, tempfile

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

assert len(rows) == 61

updates = {
    "S434": {
        "family": "",
        "reason": (
            "ANALYSIS_PLAN.md §2 decision tree -- re-examined 2026-09-28 against "
            "PROJECT_SPEC.md §8's Family A/B/C definitions (the same pass that "
            "resolved this row's 8 siblings, S435/S445/S448/S470/S471/S483/S489/S491, "
            "left blank without a documented family-fit judgment in the batches that "
            "added them). This study's exposure is proximity to an active mining site -- "
            "an economic/geographic exposure, not a legal or administrative mechanism at "
            "all. It does not match Family A (legal recognition/tenure/eligibility), "
            "Family B (bureaucratic assistance/procedural simplification), or Family C "
            "(legal or administrative barriers, documentation, eligibility restrictions, "
            "formalization barriers). The source discusses local institutional strength as "
            "a moderator of this effect, but only narratively -- no separate numeric "
            "interaction coefficient was retrievable (see provenance_note), so there is no "
            "institutional/legal estimate here to classify in the first place. "
            "synthesis_family is left blank as a reasoned non-fit, not an omission -- "
            "single study for this exposure-comparator in any case, so pooling would not "
            "yet be possible even if a family did apply."
        ),
    },
    "S435": {
        "family": "",
        "reason": (
            "ANALYSIS_PLAN.md §2 -- re-examined 2026-09-28 (see S434's note for the "
            "batch context). This study's outcome is a special water district's board-level "
            "decision to adopt a low-income bill-assistance program -- a jurisdiction/"
            "institution-level policy-adoption outcome, not a household-level access "
            "outcome, exactly the same distinction already documented for S312 (state/city "
            "adoption of a disconnection moratorium, excluded on identical grounds: "
            "'outcome is jurisdiction-level policy adoption... not household-level water "
            "access itself'). The exposure (electoral competitiveness/accountability) is "
            "also not itself a legal recognition, bureaucratic-assistance, or "
            "administrative-barrier mechanism as PROJECT_SPEC.md §8 defines those terms -- "
            "it is a governance-accountability variable one causal step upstream of any of "
            "them. synthesis_family is left blank as a reasoned non-fit, consistent with "
            "the S312 precedent; single study for this exposure-comparator regardless."
        ),
    },
    "S445": {
        "family": "",
        "reason": (
            "ANALYSIS_PLAN.md §2 -- re-examined 2026-09-28 (see S434's note for the "
            "batch context). This study's exposure is a Brazilian rural school's regional "
            "location, used as a proxy for weaker municipal fiscal/institutional capacity "
            "under the PDDE's enrolment-based (not needs-based) school funding formula -- "
            "the same kind of fiscal/administrative-transfer mechanism already excluded for "
            "S636 (Indonesia's Water Hibah performance-grant program: 'does not cleanly "
            "match... Family A... Family B... or Family C') and S649 (Mexico's federal "
            "intergovernmental transfers: 'does not map onto the Family A/B/C "
            "legal-recognition, administrative-assistance, or administrative-barrier "
            "definitions'). S445 is if anything a weaker fit than either: it uses region as "
            "a proxy for funding-formula disadvantage rather than a directly measured grant/"
            "transfer variable, and its unit of analysis is the school, not the household, "
            "further distinguishing it from Family A-C's household-facing access framing. "
            "synthesis_family is left blank as a reasoned non-fit, consistent with the "
            "S636/S649 precedent; single study for this exposure-comparator regardless."
        ),
    },
    "S448": {
        "family": "",
        "reason": (
            "ANALYSIS_PLAN.md §2 -- re-examined 2026-09-28 (see S434's note for the "
            "batch context). This study's exposure -- a Brazilian municipality's "
            "participation in a formal intermunicipal cooperation (IMC) arrangement for "
            "water/wastewater services -- is the same exposure category already excluded "
            "for S869 (Brazilian intermunicipal sanitation-consortium cooperation, also "
            "under Brazil's constitutional decentralisation framework: 'this "
            "institutional-cooperation-arrangement exposure does not cleanly map to Family "
            "A/B/C'). S448 is if anything a cleaner non-fit than S869: its primary recorded "
            "effect (the financial-performance index, FIN) is not itself a water/sanitation "
            "access or coverage outcome at all, whereas S869's outcome was at least a "
            "directly measured service-coverage figure. synthesis_family is left blank as a "
            "reasoned non-fit, consistent with the S869 precedent; single study for this "
            "exposure-comparator regardless."
        ),
    },
    "S470": {
        "family": "C",
        "reason": (
            "ANALYSIS_PLAN.md §2 decision tree -- re-examined 2026-09-28 as part of the "
            "same corpus-wide family-fit pass that resolved this row's 8 siblings (see "
            "S434's note for context). This study's exposure -- a state regulator's new "
            "enforcement norm and compliance inspections targeting municipal "
            "implementation of an income-eligibility-based water/sewage social tariff -- is "
            "squarely a legal/administrative eligibility-restriction mechanism per "
            "PROJECT_SPEC.md §8's Family C definition ('legal or administrative barriers, "
            "documentation, eligibility restrictions, formalization barriers'), and its "
            "outcome (the share of eligible households actually enrolled) is an affordability-"
            "program access outcome of the same kind already accepted for Family C via "
            "S1038 (state-vs-local economic regulation of municipal water utilities against "
            "a water-affordability outcome). Corrected from blank to Family C here. Still "
            "not pooled: single study for this specific before/after regulatory-enforcement-"
            "of-social-tariff operationalization; no other included study shares it, so "
            "pooling is not yet possible or meaningful -- see "
            "06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md and the "
            "Family C SWiM synthesis for how this is presented instead."
        ),
    },
    "S471": {
        "family": "C",
        "reason": (
            "ANALYSIS_PLAN.md §2 decision tree -- re-examined 2026-09-28 (see S434's note "
            "for the batch context). This study's exposure -- a US municipality's mayor-led "
            "vs. manager/council-led form of local government, among municipalities that own "
            "their own water utility -- is a governance/regulatory-structure mechanism, and "
            "its outcome (monthly cost of a fixed quantity of municipal drinking water) is a "
            "price/affordability outcome. This is the same kind of comparison already "
            "accepted for Family C via S1038 (state-vs-local economic regulation of "
            "municipal water utilities against a water-affordability outcome) -- both are "
            "governance/regulatory-structure exposures tested against a price outcome for "
            "municipally-owned US water utilities. Corrected from blank to Family C here. "
            "Still not pooled: single study for this specific form-of-government "
            "operationalization (and its own estimate loses significance once further "
            "covariates are added, per this row's provenance_note); no other included study "
            "shares this exact exposure, though it should be presented alongside S1038 in "
            "the Family C SWiM synthesis as the same broader 'institutional/regulatory "
            "structure and affordability' theme Phase 11 §5.1 already identified for S1038."
        ),
    },
    "S483": {
        "family": "",
        "reason": (
            "ANALYSIS_PLAN.md §2 -- re-examined 2026-09-28 (see S434's note for the batch "
            "context). This study's exposure is residence in a high- vs. low-income "
            "residential area of Nairobi -- an income-based geographic classification, not "
            "itself a legal recognition, bureaucratic-assistance, or administrative-barrier "
            "mechanism as PROJECT_SPEC.md §8 defines those terms. The paper's discussion "
            "ties the disparity to differential connection type and a documented "
            "tenure-security gap (a Family-A-adjacent concept), but the regression itself is "
            "not adjusted for tenure and does not test tenure status as the exposure -- only "
            "income-based residential classification is directly estimated here. "
            "synthesis_family is left blank as a reasoned non-fit, the same kind of "
            "institutional-variable-adjacent-but-not-quite call already made for S353 "
            "(ownership type: 'a real institutional/regulatory-model variable, but does not "
            "cleanly match Family A... B... or C'); single study for this exposure-"
            "comparator regardless."
        ),
    },
    "S489": {
        "family": "",
        "reason": (
            "ANALYSIS_PLAN.md §2 -- re-examined 2026-09-28 (see S434's note for the batch "
            "context). This study's exposure is a household's own perception that its "
            "existing water supply is costly, predicting intent to contract a paid "
            "maintenance service -- a household-level attitude/perception variable, not a "
            "legal recognition, administrative-assistance, or administrative-barrier "
            "exposure as PROJECT_SPEC.md §8 defines Family A/B/C. synthesis_family is left "
            "blank as a reasoned non-fit; single study for this exposure-comparator "
            "regardless."
        ),
    },
    "S491": {
        "family": "",
        "reason": (
            "ANALYSIS_PLAN.md §2 -- re-examined 2026-09-28 (see S434's note for the batch "
            "context). The study setting is a genuine legal/administrative mechanism (a "
            "presidential directive suspending water disconnections for non-payment during "
            "COVID-19), but the exposure actually tested is a household-level payment-"
            "history characteristic (normally pays vs. does not normally pay for water) -- "
            "the moratorium itself applies equally to both groups and is not the "
            "exposure-comparator being estimated. As operationalized, this is a household "
            "behavioral/payment-relationship variable, not a legal-recognition, "
            "bureaucratic-assistance, or administrative-barrier exposure difference across "
            "the sample. synthesis_family is left blank as a reasoned non-fit; single study "
            "for this exposure-comparator regardless. A future researcher re-mining this "
            "source for a directly moratorium-vs-no-moratorium comparison (e.g. against a "
            "pre-2020 baseline) might find a genuine Family-C-eligible estimate here that "
            "this extraction did not capture."
        ),
    },
}

assert set(updates.keys()) == {"S434","S435","S445","S448","S470","S471","S483","S489","S491"}

touched = 0
for row in rows:
    sid = row["study_id"]
    if sid in updates:
        assert row["synthesis_family"].strip() == "", f"{sid} already has a family: {row['synthesis_family']!r}"
        row["synthesis_family"] = updates[sid]["family"]
        row["exclusion_from_pooling_reason"] = updates[sid]["reason"]
        touched += 1

assert touched == 9, touched
assert len(rows) == 61

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(PATH), suffix=".tmp")
with os.fdopen(fd, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp_path, PATH)

print("OK, touched", touched, "rows")
