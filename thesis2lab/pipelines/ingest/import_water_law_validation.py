"""Read-only import of the inter-coder validation sample from the
water-law-dataset repository (validation/ folder).

Nothing in the source repository is modified. Output:
  data/public/wld-intercoder-sample.csv     (pseudonymised case references)
  data/metadata/DS-WLD-INTERCODER.json      (dataset record with checksums)

Privacy decision: public court-case identifiers (ECLI numbers, Brazilian
process numbers) are NOT republished. Each is replaced by a stable record id
and a truncated SHA-256 so the researcher can match rows privately against the
original files. See docs/DECISIONS.md (D-008).

Usage: python3 pipelines/ingest/import_water_law_validation.py [--source ../validation]
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import ROOT, sha256_file, sha256_text, write_json  # noqa: E402

CATS = ["WATER", "NOT_WATER", "UNCERTAIN"]


def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=str(ROOT.parent / "validation"))
    a = ap.parse_args()
    src = Path(a.source)
    files = {n: src / n for n in ("coder1_kappa.csv", "coder2_labels.csv", "kappa_agreement_detail.csv", "kappa_results.json")}
    for n, p in files.items():
        if not p.exists():
            sys.exit(f"missing source file: {p}")

    c1 = {r["case_id"]: r["label"] for r in read(files["coder1_kappa.csv"])}
    c2 = {r["case_id"]: r["label"] for r in read(files["coder2_labels.csv"])}
    detail = read(files["kappa_agreement_detail.csv"])
    if set(c1) != set(c2) or len(c1) != len(detail):
        sys.exit("source files do not describe the same case set; refusing to import")
    for r in detail:  # cross-check the three sources agree before publishing anything
        if c1[r["case_id"]] != r["coder1_label"] or c2[r["case_id"]] != r["coder2_label"]:
            sys.exit(f"label mismatch between source files for {r['case_id']}")
        if r["coder1_label"] not in CATS or r["coder2_label"] not in CATS:
            sys.exit(f"unexpected label for {r['case_id']}")

    rows = []
    for i, r in enumerate(sorted(detail, key=lambda r: int(r["sample_id"])), start=1):
        rows.append({
            "record_id": f"WLD-IC-{i:03d}",
            "case_ref_sha256_16": sha256_text(r["case_id"])[:16],
            "country": r["country"],
            "stratum": r["stratum"],
            "coder1_label": r["coder1_label"],
            "coder2_label": r["coder2_label"],
        })
    out = ROOT / "data/public/wld-intercoder-sample.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    record = {
        "schema_version": "1.0",
        "id": "DS-WLD-INTERCODER",
        "title": "Water-law dataset: 91-decision relabelling sample (coder 1 vs LLM-assisted coder 2)",
        "version": "1.0.0",
        "kind": "authentic",
        "description": "Labels (WATER / NOT_WATER / UNCERTAIN) given to the same 91 court decisions by coder 1 (the author) and by an LLM-assisted second coder, as committed in the water-law-dataset repository. Case identifiers are pseudonymised.",
        "source_ids": ["SRC-WLD-VALIDATION"],
        "licence": "MIT (repository licence); case identifiers withheld",
        "checksum_sha256": sha256_file(out),
        "path": "data/public/wld-intercoder-sample.csv",
        "row_count": len(rows),
        "privacy_status": "public_no_personal_data",
        "privacy_notes": "Court case identifiers replaced by record ids and truncated hashes. No decision text, party names or summaries are included. Researcher should confirm redistribution before a public release.",
        "permitted_uses": ["view", "filter", "export", "derive"],
        "variables": [
            {"name": "record_id", "type": "string", "description": "Thesis2Lab stable record id"},
            {"name": "case_ref_sha256_16", "type": "string", "description": "First 16 hex chars of SHA-256 of the original case id"},
            {"name": "country", "type": "category", "categories": sorted({r['country'] for r in rows})},
            {"name": "stratum", "type": "category", "categories": sorted({r['stratum'] for r in rows})},
            {"name": "coder1_label", "type": "category", "categories": CATS},
            {"name": "coder2_label", "type": "category", "categories": CATS},
        ],
        "provenance": {
            "imported_from": "water-law-dataset/validation (read-only)",
            "source_file_sha256": {n: sha256_file(p) for n, p in files.items()},
            "import_script": "pipelines/ingest/import_water_law_validation.py",
        },
    }
    write_json(ROOT / "data/metadata/DS-WLD-INTERCODER.json", record)
    print(f"wrote {out.relative_to(ROOT)} ({len(rows)} rows)", dict(Counter(r['country'] for r in rows)))


if __name__ == "__main__":
    main()
