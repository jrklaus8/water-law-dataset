"""Integrity tests over the committed validation material.

These guard the evidence base itself: that the reported reliability figures are
reproducible from committed files, that the coding protocol has no colliding
codes, and that the engine's taxonomy matches the one the second coder was given.
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
VAL = ROOT / 'validation'


def read(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def test_protocol_short_codes_are_unique():
    """A coder cannot apply two categories that share a code."""
    text = (VAL / 'second_coder_protocol.md').read_text(encoding='utf-8')
    codes = re.findall(r'^\| `(\w+)` \| (\w+) \|', text, re.M)
    seen = {}
    for code, name in codes:
        assert code not in seen or seen[code] == name, \
            f'code {code!r} used for both {seen[code]!r} and {name!r}'
        seen[code] = name


def test_protocol_covers_every_engine_category(coding):
    """The second coder must be told about every category the engine can emit."""
    text = (VAL / 'second_coder_protocol.md').read_text(encoding='utf-8')
    documented = {n for _, n in re.findall(r'^\| `(\w+)` \| (\w+) \|', text, re.M)}
    engine = {c for c, _ in coding['GOV_CATS']}
    missing = engine - documented
    assert not missing, f'categories absent from the coding protocol: {sorted(missing)}'


def test_kappa_results_match_the_committed_labels():
    """The stored baseline must be what the stored labels actually produce."""
    stored = json.loads((VAL / 'kappa_results.json').read_text(encoding='utf-8'))
    detail = read(VAL / 'kappa_agreement_detail.csv')
    y1 = [r['coder1_label'] for r in detail]
    y2 = [r['coder2_label'] for r in detail]
    n = len(y1)
    po = sum(a == b for a, b in zip(y1, y2)) / n
    labels = sorted(set(y1) | set(y2))
    pe = sum((y1.count(l) / n) * (y2.count(l) / n) for l in labels)
    kappa = (po - pe) / (1 - pe)
    assert n == stored['n_cases']
    assert kappa == pytest.approx(stored['cohen_kappa'], abs=1e-3)
    assert po == pytest.approx(stored['observed_agreement'], abs=1e-3)


def test_decision_rule_script_runs_and_reports_every_variant(tmp_path):
    """The headline kappa must be reproducible, not prose."""
    out = tmp_path / 'ruled.json'
    subprocess.run([sys.executable, str(VAL / 'apply_decision_rules.py'),
                    '--boot', '50', '--output', str(out)],
                   check=True, capture_output=True)
    data = json.loads(out.read_text(encoding='utf-8'))
    variants = {s['label'].split(':')[-1] for s in data['rule_variants']}
    assert variants == {'narrow', 'standard', 'broad'}
    assert data['baseline_three_label']['cohen_kappa'] == pytest.approx(0.5684, abs=1e-3)
    assert data['binary_exclude_uncertain']['cohen_kappa'] == pytest.approx(0.9321, abs=1e-3)
    for s in data['rule_variants']:
        assert s['cohen_kappa'] > data['baseline_three_label']['cohen_kappa'], \
            'resolving a protocol ambiguity should not lower agreement'
    assert data['rule_definition']['id'] == 'RULE-BR-MANANCIAIS'


def test_coder_label_vocabularies_agree():
    c1 = {r['coder1_label'] for r in read(VAL / 'kappa_agreement_detail.csv')}
    c2 = {r['coder2_label'] for r in read(VAL / 'kappa_agreement_detail.csv')}
    allowed = {'WATER', 'NOT_WATER', 'UNCERTAIN'}
    assert c1 <= allowed and c2 <= allowed, f'unexpected labels: {(c1 | c2) - allowed}'


def test_precision_recall_strata_sum_to_the_coded_total():
    d = json.loads((VAL / 'precision_recall_results.json').read_text(encoding='utf-8'))
    total = sum(s['TP'] + s['FP'] for s in d['per_stratum'].values())
    assert total == d['coded_size'], \
        f'stratum counts sum to {total}, header says {d["coded_size"]}'


def test_reported_stratum_precision_is_recomputable():
    d = json.loads((VAL / 'precision_recall_results.json').read_text(encoding='utf-8'))
    for name, s in d['per_stratum'].items():
        expected = s['TP'] / (s['TP'] + s['FP'])
        assert expected == pytest.approx(s['precision'], abs=1e-3), name


def test_datapackage_matches_the_engine_taxonomy(coding):
    """The published schema must list exactly the categories the engine emits."""
    pkg = json.loads((ROOT / 'datapackage.json').read_text(encoding='utf-8'))
    coded = next(r for r in pkg['resources'] if r['name'] == 'water-law-global-coded')
    field = next(f for f in coded['schema']['fields'] if f['name'] == 'governance_cat')
    declared = set(field['constraints']['enum'])
    engine = {c for c, _ in coding['GOV_CATS']} | {'other_water', 'not_water_related'}
    assert declared == engine, f'schema/engine mismatch: {declared ^ engine}'


def test_datapackage_schema_matches_merge_output():
    """The declared source columns must be the ones merge_national.py writes."""
    src = (ROOT / 'utils' / 'merge_national.py').read_text(encoding='utf-8')
    block = re.search(r'FIELDS\s*=\s*\[(.*?)\]', src, re.S).group(1)
    produced = re.findall(r"'([a-z_]+)'", block)
    pkg = json.loads((ROOT / 'datapackage.json').read_text(encoding='utf-8'))
    base = next(r for r in pkg['resources'] if r['name'] == 'water-law-global')
    declared = [f['name'] for f in base['schema']['fields']]
    assert declared == produced, f'declared {declared} != produced {produced}'


def test_codebook_documents_every_category(coding):
    """A category the engine can emit but the codebook omits is undocumented data."""
    text = (ROOT / 'CODEBOOK.md').read_text(encoding='utf-8')
    for cat, _ in coding['GOV_CATS']:
        assert f'`{cat}`' in text, f'{cat} is not documented in CODEBOOK.md'
