"""Independent Python re-implementation of the EXP-001 calculations.

Written separately from app/src/research/descriptive.ts (standard library only)
and used as the reference for the TypeScript implementation.

  python3 reference_impl.py --dataset DATA.csv --params '{"year_min": 2010}'
  python3 reference_impl.py --freeze      # (re)write ../references/reference_outputs.json
"""
import argparse
import csv
import json
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATASET = ROOT / "data/synthetic/synthetic-bibliometrics.csv"
CATS = ["country", "theme", "method", "institution"]

SCENARIOS = [
    ("default", "All records, no filters", {"year_min": 2000, "year_max": 2025}),
    ("years-2010-2020", "Years 2010 to 2020", {"year_min": 2010, "year_max": 2020}),
    ("brazil", "Country = Brazil", {"year_min": 2000, "year_max": 2025, "country": ["Brazil"]}),
    ("two-countries-theme", "Brazil or Canada, water quality only", {"year_min": 2000, "year_max": 2025, "country": ["Brazil", "Canada"], "theme": ["water_quality"]}),
    ("qualitative-recent", "Qualitative or mixed methods, 2015 onward", {"year_min": 2015, "year_max": 2025, "method": ["qualitative", "mixed_methods"]}),
    ("single-year", "A single year (trend undefined)", {"year_min": 2024, "year_max": 2024}),
    ("empty-selection", "Filters that match nothing", {"year_min": 2000, "year_max": 2000, "country": ["Netherlands"], "theme": ["wastewater_treatment"], "method": ["systematic_review"], "institution": ["Synthetic Centre E"]}),
]


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["year"] = int(r["year"])
        r["citations"] = int(r["citations"])
    return rows


def compute(rows, p):
    lo, hi = p.get("year_min", -10**9), p.get("year_max", 10**9)
    sel = [r for r in rows
           if lo <= r["year"] <= hi
           and all(not p.get(c) or r[c] in p[c] for c in CATS)]
    out = {"n_total": len(rows), "n_selected": len(sel), "share_selected": len(sel) / len(rows)}
    if sel:
        ys = [r["year"] for r in sel]
        y0, y1 = min(ys), max(ys)
        out["year_min"], out["year_max"] = y0, y1
        xs = list(range(y0, y1 + 1))
        cs = [ys.count(x) for x in xs]
        if len(xs) >= 2:
            out["yearly_trend_slope"] = statistics.linear_regression(xs, cs).slope
        else:
            out["yearly_trend_slope"] = None
        cit = [r["citations"] for r in sel]
        out["citations_mean"] = sum(cit) / len(cit)
        out["citations_median"] = statistics.median(cit)
    else:
        out.update(year_min=None, year_max=None, yearly_trend_slope=None, citations_mean=None, citations_median=None)
    for c in CATS:
        tally = {}
        for r in sel:
            tally[r[c]] = tally.get(r[c], 0) + 1
        out[f"n_distinct_{c}"] = len(tally)
        out[f"top_{c}"] = sorted(tally.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] if tally else None
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=str(DATASET))
    ap.add_argument("--params", default="{}")
    ap.add_argument("--freeze", action="store_true")
    a = ap.parse_args()
    rows = load(Path(a.dataset))
    if a.freeze:
        cases = [{
            "id": sid, "description": desc, "parameters": params,
            "expected": compute(rows, params),
            "tolerance": {"default": 1e-9},
            "required": True,
            "provenance": {"kind": "independent_reimplementation", "source": "experiments/EXP-001/tests/reference_impl.py",
                           "note": "Frozen output of the independent Python implementation. Not a published thesis result."},
        } for sid, desc, params in SCENARIOS]
        dest = HERE.parent / "references/reference_outputs.json"
        dest.write_text(json.dumps({"experiment_id": "EXP-001", "cases": cases}, indent=2) + "\n", encoding="utf-8")
        print("froze", len(cases), "cases")
        return
    json.dump({"metrics": compute(rows, json.loads(a.params))}, sys.stdout)


if __name__ == "__main__":
    main()
