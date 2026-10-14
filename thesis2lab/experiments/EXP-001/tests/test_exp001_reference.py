"""Sanity checks on the independent EXP-001 reference implementation."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
import importlib.util

_spec = importlib.util.spec_from_file_location("reference_impl_exp001", HERE / "reference_impl.py")
ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ref)


def test_hand_computed_trend_and_median():
    rows = [{"year": 2000, "citations": 1, "country": "a", "theme": "t", "method": "m", "institution": "i"},
            {"year": 2000, "citations": 3, "country": "a", "theme": "t", "method": "m", "institution": "i"},
            {"year": 2002, "citations": 5, "country": "b", "theme": "t", "method": "m", "institution": "i"}]
    m = ref.compute(rows, {})
    assert m["n_selected"] == 3 and m["citations_median"] == 3
    assert abs(m["yearly_trend_slope"] - (-0.5)) < 1e-12  # counts 2,0,1 over 2000..2002
    assert m["top_country"] == "a"


def test_empty_selection_is_null_not_zero():
    m = ref.compute(ref.load(ref.DATASET), {"year_min": 1900, "year_max": 1901})
    assert m["n_selected"] == 0 and m["yearly_trend_slope"] is None and m["top_country"] is None
