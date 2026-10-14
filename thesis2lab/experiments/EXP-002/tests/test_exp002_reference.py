"""Hand-checked reference values for EXP-002 (independent of the TypeScript code)."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
import importlib.util

_spec = importlib.util.spec_from_file_location("reference_impl_exp002", HERE / "reference_impl.py")
ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ref)

ROWS = [{"coder1_label": a, "coder2_label": b, "country": "NL"} for a, b in [("A", "A"), ("A", "B"), ("B", "B"), ("B", "B")]]


def test_kappa_hand_computed():
    # po = 3/4, pe = .5*.25 + .5*.75 = .5, kappa = .5
    po, k = ref.kappa(["A", "A", "B", "B"], ["A", "B", "B", "B"])
    assert po == 0.75 and abs(k - 0.5) < 1e-12


def test_published_values_recomputed():
    rows = ref.csv.DictReader(open(ref.DATA, encoding="utf-8"))
    rows = list(rows)
    expect = {"three_label_baseline": (91, 0.5684), "mananciais_rule": (91, 0.832), "binary_exclude_uncertain": (59, 0.932), "coder1_confident": (63, 0.821)}
    for spec, (n, kappa) in expect.items():
        m, _ = ref.compute(rows, spec)
        assert m["n"] == n and abs(m["cohen_kappa"] - kappa) < 5e-4, spec


def test_original_function_matches_when_present():
    if not ref.ORIGINAL.exists():
        return
    rows = list(ref.csv.DictReader(open(ref.DATA, encoding="utf-8")))
    m, orig = ref.compute(rows, "three_label_baseline")
    assert orig is not None and abs(orig - m["cohen_kappa"]) < 1e-12


def test_cli_emits_json():
    out = subprocess.run([sys.executable, "-I", str(HERE / "reference_impl.py"), "--params", '{"specification":"binary_exclude_uncertain"}'], capture_output=True, text=True, check=True)
    assert json.loads(out.stdout)["metrics"]["n"] == 59
