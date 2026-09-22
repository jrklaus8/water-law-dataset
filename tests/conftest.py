"""Shared fixtures for the regression suite.

`utils/jurimetric_coding.py` is a script: it loads a CSV at import time. To test
its classifiers we exec only the pattern-table and function region, skipping the
data load. That region is delimited by the banner comments in the file, so this
stays in step with the source as long as the banners do.
"""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _harvest(start_marker, end_marker):
    src = (ROOT / 'utils' / 'jurimetric_coding.py').read_text(encoding='utf-8')
    try:
        body = src[src.index(start_marker):src.index(end_marker)]
    except ValueError:  # pragma: no cover
        pytest.skip(f'markers {start_marker!r}/{end_marker!r} not found; '
                    'jurimetric_coding.py banners changed')
    ns = {}
    exec(compile('import re\n' + body, 'jurimetric_coding.py', 'exec'), ns)
    return ns


@pytest.fixture(scope='session')
def coding():
    """Namespace holding the classifiers and their pattern tables."""
    return _harvest('# 1. HUMAN RIGHTS', '# 4. WIN/LOSS')


@pytest.fixture(scope='session')
def outcome():
    """Namespace holding code_win_loss and its tiers."""
    return _harvest('# 4. WIN/LOSS', '# 5.')
