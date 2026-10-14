"""Pytest suite for the Python pipelines and the independent reference implementations."""
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipelines/ingest"))
import register_source  # noqa: E402


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def test_dataset_records_match_files():
    for rec in (ROOT / "data/metadata").glob("*.json"):
        d = json.loads(rec.read_text())
        assert sha(ROOT / d["path"]) == d["checksum_sha256"], rec.name
        with open(ROOT / d["path"], newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == d["row_count"]
        assert list(rows[0]) == [v["name"] for v in d["variables"]]


def test_all_records_validate_against_schemas():
    pairs = {"research/sources": "source", "research/claims": "claim", "research/methods": "method",
             "research/governance": "governance-evidence", "data/metadata": "dataset", "validation/reports": "validation-report"}
    for folder, schema in pairs.items():
        s = json.loads((ROOT / f"data/schemas/{schema}.schema.json").read_text())
        for f in (ROOT / folder).glob("*.json"):
            jsonschema.validate(json.loads(f.read_text()), s)
    s = json.loads((ROOT / "data/schemas/experiment.schema.json").read_text())
    for f in (ROOT / "experiments").glob("*/manifest.json"):
        jsonschema.validate(json.loads(f.read_text()), s)


def test_schema_rejects_bad_records():
    s = json.loads((ROOT / "data/schemas/experiment.schema.json").read_text())
    good = json.loads((ROOT / "experiments/EXP-001/manifest.json").read_text())
    for mutate in (lambda d: d.pop("requires_ai"), lambda d: d.update(reproducibility_status="PROVEN"), lambda d: d.update(id="exp1"), lambda d: d.update(surprise=1)):
        bad = json.loads(json.dumps(good))
        mutate(bad)
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(bad, s)


def test_synthetic_generator_is_deterministic(tmp_path):
    before = sha(ROOT / "data/synthetic/synthetic-bibliometrics.csv")
    subprocess.run([sys.executable, "-I", str(ROOT / "pipelines/build/make_synthetic_bibliometrics.py")], check=True, capture_output=True)
    assert sha(ROOT / "data/synthetic/synthetic-bibliometrics.csv") == before


def test_public_dataset_has_no_case_identifiers():
    text = (ROOT / "data/public/wld-intercoder-sample.csv").read_text(encoding="utf-8")
    assert "ECLI" not in text and "TJSP" not in text
    assert all(len(r["case_ref_sha256_16"]) == 16 for r in csv.DictReader(text.splitlines()))


def test_register_source_records_checksum_and_refuses_overwrite(tmp_path, monkeypatch):
    monkeypatch.setattr(register_source, "ROOT", tmp_path)
    (tmp_path / "research/sources").mkdir(parents=True)
    f = tmp_path / "chapter.md"
    f.write_text("# Chapter\n\ntext\n", encoding="utf-8")
    sid = register_source.main([str(f), "--title", "Ch", "--kind", "chapter", "--id", "SRC-CH-001"])
    rec = json.loads((tmp_path / f"research/sources/{sid}.json").read_text())
    assert rec["checksum_sha256"] == sha(f) and rec["extraction_status"] == "text_extracted"
    with pytest.raises(SystemExit):
        register_source.main([str(f), "--title", "Ch", "--kind", "chapter", "--id", "SRC-CH-001"])
    jsonschema.validate(rec, json.loads((ROOT / "data/schemas/source.schema.json").read_text()))


def test_register_source_flags_undecodable_text(tmp_path, monkeypatch):
    monkeypatch.setattr(register_source, "ROOT", tmp_path)
    (tmp_path / "research/sources").mkdir(parents=True)
    f = tmp_path / "bad.md"
    f.write_bytes(b"\xff\xfe\x00bad")
    sid = register_source.main([str(f), "--title", "Bad", "--kind", "other", "--id", "SRC-BAD-001"])
    assert json.loads((tmp_path / f"research/sources/{sid}.json").read_text())["extraction_status"] == "failed"
