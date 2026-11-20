#!/usr/bin/env python3
"""PROPOSED HELPER FOR CLAUDE / PI ONLY (DO NOT RUN AS GEMINI — PRESERVES SET-COMPOSITION BLINDING).

Builds `02_screening/full_text/A6_TIER2_MIXED_BLIND_INPUT_FOR_SECOND_AI.csv` per
`00_admin/GEMINI_HANDOFF_BRIEF_2026-11-17.md` §3 Task B:
- Selects all 102 `priority_tier == 2` records from `full_text_reviewer_2_priority_queue_2026-09-28.csv`
- Mixes in a fixed-seed decoy sample of `priority_tier == 1` or `3` includes so set composition does not hint at Claude's original decision
- Outputs ONLY `order,record_id,title,authors,year,doi,paper_link` (stripping tier, original decision, exclusion code, rationale, and study_id)
- Saves the secret key (`order -> priority_tier, original_decision`) locally outside the repo or in a Claude-only key file that Gemini is forbidden to open.
"""
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / "02_screening" / "full_text" / "full_text_reviewer_2_priority_queue_2026-09-28.csv"
FT_DB = ROOT / "02_screening" / "full_text" / "full_text_screening_database.csv"
OUT_BLIND = ROOT / "02_screening" / "full_text" / "A6_TIER2_MIXED_BLIND_INPUT_FOR_SECOND_AI.csv"


def main() -> None:
    ft_by_rid = {r["record_id"].strip(): r for r in csv.DictReader(FT_DB.open(encoding="utf-8"))}
    q_rows = list(csv.DictReader(QUEUE.open(encoding="utf-8")))
    tier2 = [r for r in q_rows if str(r.get("priority_tier", "")).strip() == "2"]
    decoys = [r for r in q_rows if str(r.get("priority_tier", "")).strip() == "1" and (r.get("original_decision") or r.get("full_text_decision") or "").strip() == "include"]

    rng = random.Random(20261120)
    rng.shuffle(decoys)
    mixed = tier2 + decoys[:28]  # 102 Tier-2 + 28 Tier-1 decoys = 130 mixed blind records
    rng.shuffle(mixed)

    out_rows = []
    for idx, r in enumerate(mixed, 1):
        rid = r["record_id"].strip()
        ft = ft_by_rid.get(rid, {})
        out_rows.append({
            "order": idx,
            "record_id": rid,
            "title": (ft.get("title") or r.get("title") or "").strip(),
            "authors": (ft.get("authors") or r.get("authors") or "").strip(),
            "year": (ft.get("year") or r.get("year") or "").strip(),
            "doi": (ft.get("doi") or r.get("doi") or "").strip(),
            "paper_link": (ft.get("full_text_location") or ft.get("url") or "").strip(),
        })

    with OUT_BLIND.open("w", encoding="utf-8", newline="\n") as fh:
        w = csv.DictWriter(fh, fieldnames=["order", "record_id", "title", "authors", "year", "doi", "paper_link"], lineterminator="\n")
        w.writeheader()
        w.writerows(out_rows)
    print(f"Wrote {len(out_rows)} mixed blind rows ({len(tier2)} Tier-2 + {len(mixed)-len(tier2)} decoys) to {OUT_BLIND}")


if __name__ == "__main__":
    main()
