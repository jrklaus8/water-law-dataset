#!/usr/bin/env python3
"""Regression tests for the two A16 adjudication scripts (code/screening/apply_a16_adjudications.py and resolve_a16_pending_reversals.py).

Self-contained: builds a tiny project tree in a temp directory whose CSV headers are read from the real files (so a schema change that breaks the
scripts is caught here), runs the scripts through their main() with --root, and checks the invariants the verifier relies on. Touches no real data.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_a16_pipeline.py
"""
from __future__ import annotations

import csv
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/screening'))
csv.field_size_limit(sys.maxsize)
import apply_a16_adjudications as apply_mod  # noqa: E402
import resolve_a16_pending_reversals as resolve_mod  # noqa: E402

REL = resolve_mod.REL
SHEET_COLS = ['record_id', apply_mod.DEC_COL, apply_mod.CODE_COL, apply_mod.COMMENT_COL]


def headers(rel):
    with open(ROOT / rel, encoding='utf-8', newline='') as f:
        return next(csv.reader(f))


def write(path, fields, rows, eol='\n'):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in fields})


def read(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def run(mod, argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = mod.main(argv)
    return rc, buf.getvalue()


class A16Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        ft = lambda rid, dec, **kw: dict(record_id=rid, title='T ' + rid, authors='A', year='2020', doi='', full_text_status='retrieved',
                                         full_text_decision=dec, final_decision=dec, exclusion_reason=kw.get('code', ''), exclusion_reason_detail=kw.get('detail', ''),
                                         notes=kw.get('notes', ''))
        # R1, R2: excludes (E01, E06); R3: an include (S002); R4: an include with an effect-size row (S003); R5: an include (S004)
        write(self.root / REL['FT'], headers(REL['FT']), [ft('R1', 'exclude', code='E01', detail='d1'), ft('R2', 'exclude', code='E06', detail='d2'),
                                                           ft('R3', 'include'), ft('R4', 'include'), ft('R5', 'include')], '\r\n')
        el = lambda rid, code: dict(record_id=rid, title='T ' + rid, authors='A', year='2020', stage='full_text', exclusion_code=code, exclusion_reason_detail='d', reviewer='x', date='2026-01-01')
        write(self.root / REL['EL'], headers(REL['EL']), [el('R1', 'E01'), el('R2', 'E06')])
        ed_rows = [dict(study_id=s, record_id=r, citation='c ' + s, doi='10.1/' + s) for s, r in (('S002', 'R3'), ('S003', 'R4'), ('S004', 'R5'))]
        write(self.root / REL['ED'], headers(REL['ED']), ed_rows)
        write(self.root / REL['EM'], headers(REL['EM']), [dict(study_id=r['study_id'], study_design_class='x') for r in ed_rows])
        mp = [dict(study_id=s, record_id=r, link_method='doi', status='active', note='') for s, r in (('S002', 'R3'), ('S003', 'R4'), ('S004', 'R5'))]
        mp.append(dict(study_id='S001', record_id='R0', link_method='x', status='retired_duplicate', note='retired earlier'))
        write(self.root / REL['MAP'], headers(REL['MAP']), mp)
        write(self.root / REL['ES'], headers(REL['ES']), [dict(study_id='S003')])
        write(self.root / REL['LINKS'], headers(REL['LINKS']), [])
        write(self.root / REL['AB'], ['study_id', 'risk_of_bias_tool'], [dict(study_id='S004', risk_of_bias_tool='x'), dict(study_id='S002', risk_of_bias_tool='x')])  # abstract-only sensitivity list

    def sheet(self, rows):
        p = self.root / 'filled.csv'
        write(p, SHEET_COLS, rows)
        return p

    def adjudicate(self, rows, apply=True):
        argv = [str(self.sheet(rows)), '--reviewer', 'T', '--root', str(self.root)] + (['--apply'] if apply else [])
        return run(apply_mod, argv)

    def resolve(self, apply=True):
        return run(resolve_mod, ['--reviewer', 'T', '--root', str(self.root)] + (['--apply'] if apply else []))

    def ft(self):
        return {r['record_id']: r for r in read(self.root / REL['FT'])}

    def include_json(self, rid):
        ed_cols = [c for c in headers(REL['ED']) if c not in ('study_id', 'record_id')]
        em_cols = [c for c in headers(REL['EM']) if c != 'study_id']
        d = self.root / REL['INC']; d.mkdir(parents=True, exist_ok=True)
        (d / f'{rid}.json').write_text(json.dumps({'extraction': {c: 'v' for c in ed_cols}, 'evidence_map': {c: 'v' for c in em_cols}}), encoding='utf-8')


D, C, M = apply_mod.DEC_COL, apply_mod.CODE_COL, apply_mod.COMMENT_COL


class TestApply(A16Base):
    def test_dry_run_writes_nothing(self):
        before = (self.root / REL['FT']).read_bytes()
        rc, out = self.adjudicate([{'record_id': 'R1', D: 'include'}], apply=False)
        self.assertEqual(rc, 0); self.assertIn('DRY RUN', out)
        self.assertEqual((self.root / REL['FT']).read_bytes(), before)
        self.assertFalse((self.root / REL['PEND']).exists())

    def test_confirm_recode_and_reverse(self):
        rc, _ = self.adjudicate([{'record_id': 'R1', D: 'exclude', C: 'E01', M: 'agree'},
                                 {'record_id': 'R2', D: 'exclude', C: 'E07'},
                                 {'record_id': 'R3', D: 'exclude', C: 'E01', M: 'too broad'},
                                 {'record_id': 'R5', D: 'include'}])
        self.assertEqual(rc, 0)
        ft = self.ft()
        self.assertIn('confirms exclude', ft['R1']['notes']); self.assertEqual(ft['R1']['exclusion_reason'], 'E01')
        self.assertEqual(ft['R2']['exclusion_reason'], 'E07')
        el = {r['record_id']: r for r in read(self.root / REL['EL'])}
        self.assertEqual(el['R2']['exclusion_code'], 'E07')
        self.assertEqual(ft['R3']['final_decision'], 'include')  # reversal is queued, not applied
        pend = read(self.root / REL['PEND'])
        self.assertEqual([p['record_id'] for p in pend], ['R3']); self.assertEqual(pend[0]['researcher_exclusion_code'], 'E01')
        self.assertIn(b'\r\n', (self.root / REL['FT']).read_bytes()[:5000])  # CRLF preserved

    def test_idempotent(self):
        rows = [{'record_id': 'R3', D: 'exclude', C: 'E01'}]
        self.adjudicate(rows)
        _, out = self.adjudicate(rows)
        self.assertIn('already adjudicated', out)
        self.assertEqual(len(read(self.root / REL['PEND'])), 1)

    def test_invalid_rows_stop_everything(self):
        before = (self.root / REL['FT']).read_bytes()
        for bad in ({'record_id': 'R1', D: 'maybe'}, {'record_id': 'R1', D: 'exclude'}, {'record_id': 'R1', D: 'exclude', C: 'E99'}, {'record_id': 'NOPE', D: 'include'}):
            rc, _ = self.adjudicate([{'record_id': 'R2', D: 'include'}, bad])
            self.assertEqual(rc, 2)
            self.assertEqual((self.root / REL['FT']).read_bytes(), before)


class TestResolve(A16Base):
    def queue(self, rows):
        self.adjudicate(rows)

    def test_new_include_and_new_exclude(self):
        self.queue([{'record_id': 'R1', D: 'include'}, {'record_id': 'R5', D: 'exclude', C: 'E01', M: 'out of scope'}])
        self.include_json('R1')
        rc, _ = self.resolve()
        self.assertEqual(rc, 0)
        ft = self.ft()
        self.assertEqual((ft['R1']['final_decision'], ft['R1']['exclusion_reason']), ('include', ''))
        self.assertEqual((ft['R5']['final_decision'], ft['R5']['exclusion_reason']), ('exclude', 'E01'))
        mp = {r['study_id']: r for r in read(self.root / REL['MAP'])}
        self.assertEqual(mp['S005']['record_id'], 'R1'); self.assertEqual(mp['S005']['status'], 'active')  # next ID after S004; retired S001 never reused
        self.assertEqual(mp['S004']['status'], 'retired_excluded')
        self.assertEqual([r['study_id'] for r in read(self.root / REL['AB'])], ['S002'])  # the retired study leaves the abstract-only list
        ed_ids = {r['study_id'] for r in read(self.root / REL['ED'])}
        self.assertEqual(ed_ids, {'S002', 'S003', 'S005'})
        self.assertEqual({r['study_id'] for r in read(self.root / REL['EM'])}, ed_ids)
        el = {r['record_id'] for r in read(self.root / REL['EL'])}
        self.assertEqual(el, {'R2', 'R5'})
        # the invariants verify_repository.py checks
        inc = {r['record_id'] for r in read(self.root / REL['FT']) if r['final_decision'] == 'include'}
        self.assertEqual({r['record_id'] for r in read(self.root / REL['MAP']) if r['status'] == 'active'}, inc)
        exc = {r['record_id'] for r in read(self.root / REL['FT']) if r['final_decision'] == 'exclude'}
        self.assertEqual(el, exc)
        self.assertEqual(read(self.root / REL['PEND']), [])
        done = read(self.root / REL['DONE'])
        self.assertEqual({d['record_id']: d['study_id'] for d in done}, {'R1': 'S005', 'R5': 'S004'})
        rc, out = self.resolve(); self.assertIn('No pending', out)  # re-running is safe

    def test_refusals_write_nothing(self):
        self.queue([{'record_id': 'R4', D: 'exclude', C: 'E01'}])  # S003 has an effect-size row
        before = {k: (self.root / REL[k]).read_bytes() for k in ('FT', 'EL', 'ED', 'EM', 'MAP')}
        rc, out = self.resolve(apply=True)
        self.assertEqual(rc, 2); self.assertIn('effect_sizes', out)
        self.assertEqual(before, {k: (self.root / REL[k]).read_bytes() for k in before})

    def test_missing_or_malformed_extraction_json(self):
        self.queue([{'record_id': 'R2', D: 'include'}])
        rc, out = self.resolve(); self.assertEqual(rc, 2); self.assertIn('no prepared extraction', out)
        d = self.root / REL['INC']; d.mkdir(parents=True, exist_ok=True)
        (d / 'R2.json').write_text(json.dumps({'extraction': {'citation': 'x'}, 'evidence_map': {}}), encoding='utf-8')
        rc, out = self.resolve(); self.assertEqual(rc, 2); self.assertIn('columns differ', out)

    def test_dry_run_writes_nothing(self):
        self.queue([{'record_id': 'R1', D: 'include'}]); self.include_json('R1')
        before = (self.root / REL['MAP']).read_bytes()
        rc, out = self.resolve(apply=False)
        self.assertEqual(rc, 0); self.assertIn('DRY RUN', out)
        self.assertEqual((self.root / REL['MAP']).read_bytes(), before)
        self.assertEqual(len(read(self.root / REL['PEND'])), 1)


class TestSheetReading(A16Base):
    def raw_sheet(self, data: bytes):
        p = self.root / 'raw.csv'; p.write_bytes(data)
        return run(apply_mod, [str(p), '--reviewer', 'T', '--root', str(self.root), '--apply'])

    def test_bom_cp1252_and_semicolon_sheets(self):
        head = f'priority,record_id,{D},{C},{M}\n'
        rc, _ = self.raw_sheet(('\ufeff' + head + '1, r5 ,Include,,caf\u00e9\n').encode('utf-8'))   # BOM, padded and lower-case record id, capitalised decision
        self.assertEqual(rc, 0); self.assertIn('confirms include', self.ft()['R5']['notes'])
        rc, _ = self.raw_sheet((head + '1,R1,exclude,E01,caf\u00e9\n').encode('cp1252'))          # Windows-1252 with an accented character
        self.assertEqual(rc, 0); self.assertIn('café', self.ft()['R1']['notes'])
        rc, _ = self.raw_sheet(head.replace(',', ';').encode('utf-8') + b'1;R2;exclude;E06;x\n;;;;\n')  # semicolon delimiter, blank trailing row
        self.assertEqual(rc, 0); self.assertIn('confirms exclude', self.ft()['R2']['notes'])

    def test_missing_columns_and_duplicate_rows_write_nothing(self):
        before = (self.root / REL['FT']).read_bytes()
        rc, out = self.raw_sheet(b'a,b\n1,2\n')
        self.assertEqual(rc, 2); self.assertIn('lacks the column', out)
        rc, out = self.adjudicate([{'record_id': 'R1', D: 'include'}, {'record_id': 'R1', D: 'exclude', C: 'E01'}])
        self.assertEqual(rc, 2); self.assertIn('more than one row', out)
        self.assertEqual((self.root / REL['FT']).read_bytes(), before)


class TestRoundTrip(unittest.TestCase):
    def test_real_files_rewrite_byte_identical(self):
        """Reading and re-writing each CSV the scripts touch must reproduce it exactly (line endings, quoting), so an adjudication changes only the intended rows."""
        for key in ('FT', 'EL', 'ED', 'EM', 'MAP'):
            for mod in (apply_mod, resolve_mod):
                reader, writer = (mod._read, mod._write) if mod is apply_mod else (mod.read, mod.write)
                src = ROOT / REL[key]
                fields, rows, eol = reader(src)
                with tempfile.TemporaryDirectory() as d:
                    out = Path(d) / 'x.csv'
                    writer(out, fields, rows, eol)
                    self.assertEqual(out.read_bytes(), src.read_bytes(), f'{mod.__name__} does not round-trip {REL[key]}')


if __name__ == '__main__':
    unittest.main(verbosity=1)
