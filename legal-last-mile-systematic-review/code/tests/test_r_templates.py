#!/usr/bin/env python3
"""End-to-end test of the R meta-analysis templates (08_code/R) against the REAL column layout of effect_sizes.csv, with SYNTHETIC numbers.

No row is flagged for pooling in the real data (Phase 11 verdict), so the templates are otherwise never exercised. This copies the two input CSVs into a temp
project, flags ten Family A rows as pooled with made-up numeric effects, runs the three scripts with Rscript and checks that each exits cleanly and writes its
outputs; it also checks that with no flagged rows the scripts refuse with their documented message, and that a flagged row with no numeric SE is rejected clearly.
Skipped if Rscript or its packages are missing. Run from legal-last-mile-systematic-review/:  python3 code/tests/test_r_templates.py
Found by this test's first run (2026-10-04): the free text in non-pooled rows made R read effect_estimate as character, so rma() failed on the first real use."""
import csv
import random
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
csv.field_size_limit(sys.maxsize)
ES, ED = '05_analysis/effect_sizes/effect_sizes.csv', '03_extraction/extracted_data/extraction_database.csv'
HAVE_R = shutil.which('Rscript') is not None and subprocess.run(['Rscript', '-e', 'library(metafor);library(dplyr);library(ggplot2)'], capture_output=True).returncode == 0


def rscript(cwd, name):
    return subprocess.run(['Rscript', str(ROOT / f'08_code/R/{name}.R')], cwd=cwd, capture_output=True, text=True, timeout=300)


@unittest.skipUnless(HAVE_R, 'Rscript with metafor, dplyr and ggplot2 not available')
class TestRTemplates(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory(); self.addCleanup(self._t.cleanup)
        self.d = Path(self._t.name)
        for rel in (ES, ED):
            (self.d / rel).parent.mkdir(parents=True, exist_ok=True); shutil.copy(ROOT / rel, self.d / rel)

    def flag(self, n=10, numeric=True):
        p = self.d / ES
        with open(p, newline='', encoding='utf-8') as f:
            rd = csv.DictReader(f); fields, rows = rd.fieldnames, list(rd)
        rng, k = random.Random(1), 0
        for r in rows:
            if r['synthesis_family'] == 'A' and k < n:
                r['included_in_pooled_estimate'] = 'TRUE'
                r['effect_estimate'] = str(round(rng.gauss(0.4, 0.3), 3)) if numeric else 'positive'
                r['standard_error'] = str(round(rng.uniform(0.1, 0.3), 3)) if numeric else ''
                k += 1
        with open(p, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n'); w.writeheader(); w.writerows(rows)

    def test_refuses_when_nothing_is_pooled(self):
        for name in ('01_meta_analysis', '02_sensitivity_analysis', '03_publication_bias'):
            r = rscript(self.d, name)
            self.assertNotEqual(r.returncode, 0, name); self.assertIn('nothing to', r.stderr, name)

    def test_runs_end_to_end_with_synthetic_pooled_rows(self):
        self.flag()
        for name in ('01_meta_analysis', '02_sensitivity_analysis', '03_publication_bias'):
            r = rscript(self.d, name)
            self.assertEqual(r.returncode, 0, f'{name}: {r.stderr[-500:]}')
        for rel in ('05_analysis/meta_analysis/A_model.rds', '05_analysis/meta_analysis/A_forest.png', '05_analysis/heterogeneity/A_heterogeneity.csv',
                    '05_analysis/sensitivity/A_sensitivity.csv', '05_analysis/publication_bias/A_funnel.png', '05_analysis/publication_bias/A_tests.csv'):
            self.assertTrue((self.d / rel).exists() and (self.d / rel).stat().st_size > 0, rel)

    def test_non_numeric_pooled_row_is_rejected_clearly(self):
        self.flag(n=3, numeric=False)
        r = rscript(self.d, '01_meta_analysis')
        self.assertNotEqual(r.returncode, 0); self.assertIn('numeric effect_estimate and standard_error', r.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=1)
