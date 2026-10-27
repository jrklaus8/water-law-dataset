#!/usr/bin/env python3
"""The reader's guides (START_HERE.md, GLOSSARY.md and the README.md in every numbered folder) are how a supervisor or a future researcher finds their way, so they must not rot.

Checks: START_HERE.md's key-figures block equals what build_start_here.py writes from the databases; every numbered folder has a README.md; and every relative link in these guides
points at a file or folder that exists. Run from legal-last-mile-systematic-review/."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import build_start_here as bsh  # noqa: E402

FOLDERS = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and re.match(r'\d\d_', p.name))
GUIDES = ['START_HERE.md', 'GLOSSARY.md'] + [f'{d}/README.md' for d in FOLDERS]
LINK = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)\s]+)\)')


class TestReaderGuides(unittest.TestCase):
    def test_key_figures_block_is_current(self):
        text = (ROOT / 'START_HERE.md').read_text(encoding='utf-8')
        self.assertEqual(bsh.render(text), text, 'run code/analysis/build_start_here.py')

    def test_every_numbered_folder_has_a_readme(self):
        self.assertEqual(len(FOLDERS), 12)
        for d in FOLDERS:
            self.assertTrue((ROOT / d / 'README.md').exists(), d)

    def test_relative_links_resolve(self):
        bad = []
        for g in GUIDES:
            base = (ROOT / g).parent
            for target in LINK.findall((ROOT / g).read_text(encoding='utf-8')):
                if target.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue
                if not (base / target.split('#')[0]).exists():
                    bad.append((g, target))
        self.assertEqual(bad, [])

    def test_start_here_names_the_limits(self):
        low = (ROOT / 'START_HERE.md').read_text(encoding='utf-8').lower()
        for needle in ('preliminary', 'ai-assisted', 'partly human-verified', 'no second extractor', 'not registered before the work was done', 'current_figures.md'):
            self.assertIn(needle, low, needle)


if __name__ == '__main__':
    unittest.main(verbosity=1)
