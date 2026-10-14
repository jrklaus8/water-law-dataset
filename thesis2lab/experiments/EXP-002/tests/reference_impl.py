"""Independent Python implementation for EXP-002 (Cohen's kappa audit).

Standard library only. When the original calculator (validation/kappa_calculator.py in
the water-law-dataset repository) is present next to this project, its own
`cohen_kappa` function is extracted with `ast` and run on the same labels, so the
formula is compared with the original author's code and not only with our own.

  python3 reference_impl.py --params '{"specification": "mananciais_rule"}'
"""
import argparse
import ast
import csv
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = ROOT / "data/public/wld-intercoder-sample.csv"
ORIGINAL = ROOT.parent / "validation/kappa_calculator.py"


def kappa(y1, y2):
    n = len(y1)
    po = sum(a == b for a, b in zip(y1, y2)) / n
    c1, c2 = Counter(y1), Counter(y2)
    pe = sum(c1[k] * c2[k] for k in set(c1) | set(c2)) / (n * n)
    return po, (1.0 if pe == 1 else (po - pe) / (1 - pe))


def original_cohen_kappa():
    if not ORIGINAL.exists():
        return None
    tree = ast.parse(ORIGINAL.read_text(encoding="utf-8"))
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "cohen_kappa")
    ns = {"Counter": Counter}
    exec(compile(ast.Module([fn], []), str(ORIGINAL), "exec"), ns)  # noqa: S102 - our own sibling repo file
    return ns["cohen_kappa"]


def compute(rows, spec):
    pairs = [(r["coder1_label"], r["coder2_label"], r["country"]) for r in rows]
    if spec == "mananciais_rule":
        pairs = [("WATER" if c == "Brazil" and a == "UNCERTAIN" else a, b, c) for a, b, c in pairs]
    elif spec == "binary_exclude_uncertain":
        pairs = [p for p in pairs if "UNCERTAIN" not in p[:2]]
    elif spec == "coder1_confident":
        pairs = [p for p in pairs if p[0] != "UNCERTAIN"]
    elif spec != "three_label_baseline":
        raise SystemExit(f"unknown specification {spec}")
    y1, y2 = [p[0] for p in pairs], [p[1] for p in pairs]
    po, k = kappa(y1, y2)
    m = {"n": len(y1), "observed_agreement": po, "cohen_kappa": k}
    for cat in sorted(set(y1) | set(y2)):
        m[f"tp_{cat}"] = sum(a == cat and b == cat for a, b in zip(y1, y2))
        m[f"fp_{cat}"] = sum(a != cat and b == cat for a, b in zip(y1, y2))
        m[f"fn_{cat}"] = sum(a == cat and b != cat for a, b in zip(y1, y2))
    orig = original_cohen_kappa()
    return m, (orig(y1, y2) if orig else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=str(DATA))
    ap.add_argument("--params", default="{}")
    a = ap.parse_args()
    with open(a.dataset, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    spec = json.loads(a.params).get("specification", "three_label_baseline")
    metrics, orig = compute(rows, spec)
    json.dump({"metrics": metrics, "original_function_kappa": orig}, sys.stdout)


if __name__ == "__main__":
    main()
