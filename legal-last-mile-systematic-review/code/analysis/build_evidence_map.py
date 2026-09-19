#!/usr/bin/env python3
"""Derive as much of evidence_map.csv as can be safely derived, per study.

05_analysis/descriptive/evidence_map.csv (CODEBOOK.md, PRISMA_WORKFLOW.md
S"Evidence classification matrix") summarizes each study for synthesis
planning. Some of its fields are mechanical restatements of data already
recorded in extraction_database.csv during extraction; others require a
judgment call this script must never make silently. This script fills
only the former, appends one row per study_id not yet present (idempotent,
never overwrites an existing row -- same discipline as
init_screening_db.py/init_full_text_db.py), and prints a clear warning for
every field it deliberately left blank so a human follows up rather than
assuming the row is complete.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

WHAT GETS DERIVED, AND WHY EACH ONE IS SAFE
--------------------------------------------
- study_design_class: from `risk_of_bias_tool`, inverting the
  design<->tool mapping RISK_OF_BIAS.md S1 already commits to (RoB 2 ->
  experimental, ROBINS-I -> quasi_experimental, either JBI checklist ->
  observational, CASP -> qualitative, MMAT -> mixed_methods, AMSTAR 2 ->
  systematic_review_secondary per RISK_OF_BIAS.md S1's own instruction).
  Left BLANK (with a warning) for the project's own Legal Institutional
  Evidence Appraisal Framework, since RISK_OF_BIAS.md S2 covers both
  doctrinal and jurimetric studies without a mechanical way to tell them
  apart from the tool name alone -- a real judgment call.
- mechanism_family: from the four top-level mechanism booleans
  (`eligibility`/`burden`/`discretion_accommodation`/`enforcement`,
  CODEBOOK.md S4) -- exactly one true maps directly to that family;
  more than one true maps to MULTIPLE (an enum value this schema already
  defines for exactly this case); none true is left BLANK with a warning
  rather than guessed.
- legal_context / institutional_context: copied straight from
  extraction_database.csv's own `legal_system` / `regulatory_model`
  fields (CODEBOOK.md S2) -- not a judgment call, just avoiding
  re-typing a value already recorded once.

WHAT IS DELIBERATELY NEVER DERIVED
-----------------------------------
- evidence_level: DATA_DICTIONARY.md is explicit this is a narrative
  tier, not a numeric score -- there is no mechanical formula for prose.
- outcome_family: PROJECT_SPEC.md S7's own hierarchy lists
  "approval/refusal" under BOTH the primary outcome (formal connection)
  and under secondary "administrative outcomes" -- a study coded with
  `application_success`/`refusal`/`delay_outcome` could genuinely belong
  to either family depending on what was actually being approved or
  refused, and PROJECT_SPEC.md itself doesn't resolve that ambiguity
  mechanically. Guessing here risks silently mis-classifying a study for
  quantitative-synthesis-family purposes -- exactly the kind of
  manufactured comparability PROJECT_SPEC.md S3 exists to prevent. Left
  BLANK with a warning in every case; a human reads the study and
  decides which family the specific approval/refusal/delay actually
  concerned.
- quantitative_synthesis_eligible / qualitative_synthesis_eligible:
  these apply ANALYSIS_PLAN.md S2's decision tree, evaluated per
  candidate synthesis family across the whole evidence base, not a
  per-study mechanical fact -- Phase 11's job, not this script's.

USAGE
-----
    python3 build_evidence_map.py \\
        --extraction-db ../../03_extraction/extracted_data/extraction_database.csv \\
        --evidence-map ../../05_analysis/descriptive/evidence_map.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

SCHEMA = [
    "study_id", "study_design_class", "evidence_level", "mechanism_family",
    "outcome_family", "quantitative_synthesis_eligible",
    "qualitative_synthesis_eligible", "legal_context", "institutional_context",
]

MECHANISM_FIELDS = ["eligibility", "burden", "discretion_accommodation", "enforcement"]

TOOL_TO_DESIGN_CLASS = [
    (("rob 2", "rob2", "rob-2"), "experimental"),
    (("robins-i", "robins i", "robinsi"), "quasi_experimental"),
    (("jbi",), "observational"),
    (("casp",), "qualitative"),
    (("mmat",), "mixed_methods"),
    (("amstar",), "systematic_review_secondary"),
    # Legal Institutional Evidence Appraisal Framework intentionally
    # excluded -- RISK_OF_BIAS.md S2 covers both doctrinal and jurimetric
    # studies, and the tool name alone can't tell them apart.
]


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def truthy(value: str) -> bool:
    return (value or "").strip().lower() in {"true", "1", "yes"}


def derive_study_design_class(risk_of_bias_tool: str) -> str | None:
    tool_lower = (risk_of_bias_tool or "").strip().lower()
    if not tool_lower:
        return None
    for patterns, design_class in TOOL_TO_DESIGN_CLASS:
        if any(p in tool_lower for p in patterns):
            return design_class
    return None


def derive_mechanism_family(rec: dict) -> str | None:
    active = [field.upper() for field in MECHANISM_FIELDS if truthy(rec.get(field, ""))]
    if len(active) == 1:
        return active[0]
    if len(active) > 1:
        return "MULTIPLE"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--extraction-db", type=Path, required=True)
    parser.add_argument("--evidence-map", type=Path, required=True)
    args = parser.parse_args()

    if not args.extraction_db.exists():
        print(f"No extraction database at {args.extraction_db} -- nothing to derive from.")
        return 0

    extracted = read_csv(args.extraction_db)
    existing = read_csv(args.evidence_map)
    existing_ids = {r["study_id"] for r in existing}

    appended = 0
    blanks = {"study_design_class": [], "mechanism_family": [], "outcome_family": []}

    for rec in extracted:
        study_id = rec.get("study_id", "").strip()
        if not study_id or study_id in existing_ids:
            continue

        design_class = derive_study_design_class(rec.get("risk_of_bias_tool", ""))
        if design_class is None:
            blanks["study_design_class"].append(study_id)

        mechanism_family = derive_mechanism_family(rec)
        if mechanism_family is None:
            blanks["mechanism_family"].append(study_id)

        # outcome_family is never derived -- see module docstring.
        blanks["outcome_family"].append(study_id)

        existing.append({
            "study_id": study_id,
            "study_design_class": design_class or "",
            "evidence_level": "",
            "mechanism_family": mechanism_family or "",
            "outcome_family": "",
            "quantitative_synthesis_eligible": "",
            "qualitative_synthesis_eligible": "",
            "legal_context": rec.get("legal_system", ""),
            "institutional_context": rec.get("regulatory_model", ""),
        })
        existing_ids.add(study_id)
        appended += 1

    args.evidence_map.parent.mkdir(parents=True, exist_ok=True)
    with args.evidence_map.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(existing)

    print(f"Appended {appended} new study row(s) to {args.evidence_map}")
    print(f"evidence_map.csv now has {len(existing)} total row(s).")
    for field, ids in blanks.items():
        if ids:
            print(f"WARNING: {field} left blank for {len(ids)} study/studies -- "
                  f"needs manual judgment, see this script's docstring for why: {ids}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
