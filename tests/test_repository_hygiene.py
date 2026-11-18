"""Repository hygiene checks: secrets, configuration, links, required files, Python-version syntax.

SAFETY: read-only, offline, no credentials. When a check finds something it reports FILE:LINE and the rule that matched, never the matched text,
so a failing run cannot copy a secret into a CI log. Data files (.csv, .json, .xlsx) are not scanned here: they hold licensed database exports and
decision text, and the data-protection / licence review of those is a human task recorded in docs/audit-report.md.

Tests marked @unittest.expectedFailure document a known defect (docs/audit-report.md) in executable form. They state the behaviour the repository
SHOULD have, fail today, and will start to pass - which makes unittest report an "unexpected success" - when the defect is fixed, at which point
the marker must be removed. Fixing a scraper changes how data would be collected, so those fixes need the researcher's approval first.

Run from the repository root:  python -m unittest discover -s tests -v
"""
import ast
import os
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.py', '.md', '.yml', '.yaml', '.toml', '.txt', '.cff', '.cfg', '.ini', '.sh', '.html', '.js', '.tex', '.bib', '.example'}
SKIP_DIRS = {'.git', '__pycache__', 'node_modules'}


def tracked_files():
    """Tracked files when run inside a git checkout, otherwise every file under ROOT."""
    try:
        out = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, check=True).stdout.decode('utf-8', 'replace')
        return [ROOT / p for p in out.split('\0') if p and (ROOT / p).is_file()]
    except (OSError, subprocess.CalledProcessError):
        return [p for p in ROOT.rglob('*') if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)]


def text_files():
    return [p for p in tracked_files() if (p.suffix in TEXT_SUFFIXES or p.name.startswith('.env')) and p.stat().st_size < 3_000_000]


def lines(p):
    return p.read_text(encoding='utf-8', errors='replace').splitlines()


def scraper_sources():
    return [p for p in tracked_files() if p.suffix == '.py' and p.relative_to(ROOT).parts[0] in ('scrapers', 'utils', 'validation')]


# --- secrets -----------------------------------------------------------------------------------------------------------------------------------
SECRET_RULES = {
    'anthropic-style key': re.compile(r'\bsk-ant-[A-Za-z0-9_\-]{20,}'),
    'openai-style key': re.compile(r'\bsk-[A-Za-z0-9]{32,}'),
    'github token': re.compile(r'\b(ghp|gho|ghs|ghu|ghr)_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}'),
    'aws access key id': re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
    'google api key': re.compile(r'\bAIza[0-9A-Za-z_\-]{35}\b'),
    'slack token': re.compile(r'\bxox[abprs]-[A-Za-z0-9\-]{10,}'),
    'private key block': re.compile(r'-----BEGIN (RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----'),
}
ASSIGNED_SECRET = re.compile(r'''(?i)\b(api[_-]?key|secret|token|passwd|password)\b\s*[:=]\s*['"]([^'"\s]{16,})['"]''')
PLACEHOLDER = re.compile(r'(?i)your|example|placeholder|changeme|xxxx|<.*>|\{.*\}|os\.environ|getenv')


class TestNoSecretsInCodeConfigDocs(unittest.TestCase):
    def test_no_known_credential_patterns(self):
        hits = []
        for p in text_files():
            for n, ln in enumerate(lines(p), 1):
                for name, rx in SECRET_RULES.items():
                    if rx.search(ln):
                        hits.append(f'{p.relative_to(ROOT)}:{n} ({name})')
        self.assertEqual(hits, [], 'possible credential(s) - rotate first, then remove; values deliberately not printed')

    def test_no_literal_credentials_assigned_to_secret_looking_names(self):
        hits = []
        for p in text_files():
            for n, ln in enumerate(lines(p), 1):
                m = ASSIGNED_SECRET.search(ln)
                if m and not PLACEHOLDER.search(m.group(2)) and not PLACEHOLDER.search(ln):
                    hits.append(f'{p.relative_to(ROOT)}:{n}')
        self.assertEqual(hits, [], 'literal value assigned to an api_key / secret / token / password name; values deliberately not printed')

    def test_only_the_example_env_file_is_tracked(self):
        env_files = [str(p.relative_to(ROOT)) for p in tracked_files() if p.name == '.env' or (p.name.startswith('.env.') and p.name != '.env.example')]
        self.assertEqual(env_files, [])

    def test_example_env_file_holds_placeholders_only(self):
        for p in ROOT.glob('**/.env.example'):
            for n, ln in enumerate(lines(p), 1):
                if '=' in ln and not ln.lstrip().startswith('#'):
                    value = ln.split('=', 1)[1].strip()
                    if re.search(r'(?i)key|token|secret', ln.split('=', 1)[0]):
                        self.assertRegex(value, r'(?i)your|example|placeholder|^$', f'{p.relative_to(ROOT)}:{n} does not look like a placeholder')


# --- configuration -----------------------------------------------------------------------------------------------------------------------------
class TestEnvironmentVariablesAreDocumented(unittest.TestCase):
    READ = re.compile(r'''os\.(?:getenv|environ\.get|environ)\s*[\(\[]\s*['"]([A-Z][A-Z0-9_]+)['"]''')

    def read_by_root_code(self):
        found = {}
        for p in scraper_sources():
            for n, ln in enumerate(lines(p), 1):
                for name in self.READ.findall(ln):
                    found.setdefault(name, f'{p.relative_to(ROOT)}:{n}')
        return found

    def documented(self):
        keys = set()
        for ln in lines(ROOT / '.env.example'):
            if '=' in ln and not ln.lstrip().startswith('#'):
                keys.add(ln.split('=', 1)[0].strip())
        return keys

    def test_every_variable_the_code_reads_is_in_env_example(self):
        missing = {k: where for k, where in self.read_by_root_code().items() if k not in self.documented()}
        self.assertEqual(missing, {}, 'read by code but not documented in .env.example')

    def test_every_variable_in_env_example_is_read_somewhere(self):
        unused = sorted(self.documented() - set(self.read_by_root_code()))
        self.assertEqual(unused, [], 'documented in .env.example but no script reads it')


class TestVersionsAgree(unittest.TestCase):
    def test_citation_version_matches_pyproject(self):
        cff = (ROOT / 'CITATION.cff').read_text(encoding='utf-8')
        toml = (ROOT / 'pyproject.toml').read_text(encoding='utf-8')
        v_cff = re.search(r'^version:\s*"?([^"\s]+)"?', cff, re.M).group(1)
        v_toml = re.search(r'^version\s*=\s*"([^"]+)"', toml, re.M).group(1)
        self.assertEqual(v_cff, v_toml)

    def test_every_script_parses_with_the_declared_minimum_python(self):
        toml = (ROOT / 'pyproject.toml').read_text(encoding='utf-8')
        major, minor = re.search(r'requires-python\s*=\s*">=(\d+)\.(\d+)"', toml).groups()
        bad = []
        for p in scraper_sources():
            try:
                ast.parse(p.read_text(encoding='utf-8', errors='replace'), feature_version=(int(major), int(minor)))
            except SyntaxError as e:
                bad.append(f'{p.relative_to(ROOT)}:{e.lineno}')
        self.assertEqual(bad, [], f'syntax not valid for Python {major}.{minor}')


# --- documentation -----------------------------------------------------------------------------------------------------------------------------
LINK = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')


class TestDocumentationLinks(unittest.TestCase):
    def test_relative_links_in_root_documents_resolve(self):
        docs = [ROOT / n for n in ('README.md', 'RESEARCH_CONTEXT.md', 'FUTURE_WORK.md', 'CONTRIBUTING.md', 'SECURITY.md', 'CHANGELOG.md') if (ROOT / n).exists()]
        docs += sorted((ROOT / 'docs').glob('*.md'))
        broken = []
        for d in docs:
            in_code = False
            for n, ln in enumerate(lines(d), 1):
                if ln.lstrip().startswith('```'):
                    in_code = not in_code
                if in_code:
                    continue
                for target in LINK.findall(ln):
                    if re.match(r'(?i)^(https?:|mailto:|#|tel:)', target):
                        continue
                    path = target.split('#', 1)[0]
                    if path and not (d.parent / path).resolve().exists():
                        broken.append(f'{d.relative_to(ROOT)}:{n} -> {path}')
        self.assertEqual(broken, [])


class TestRequiredFiles(unittest.TestCase):
    REQUIRED = ['README.md', 'LICENSE', 'CITATION.cff', '.env.example', 'requirements.txt', 'pyproject.toml', 'CONTRIBUTING.md', 'SECURITY.md', 'CHANGELOG.md',
                'docs/research-protocol.md', 'docs/data-management.md', 'docs/ai-use-and-disclosure.md', 'docs/source-register.md', 'docs/reproducibility.md',
                'docs/limitations.md', 'docs/audit-report.md', 'docs/standards-matrix.md', 'docs/release-checklist.md']

    def test_required_files_exist_and_are_not_empty(self):
        missing = [f for f in self.REQUIRED if not (ROOT / f).is_file() or (ROOT / f).stat().st_size < 200]
        self.assertEqual(missing, [])

    def test_audit_documents_do_not_claim_compliance_or_certification(self):
        # The audit is a self-assessment by an AI assistant. It must never read as an official review, certification, ethics approval or legal opinion.
        rx = re.compile(r'(?i)\b(is|are|was|were|fully|hereby)\s+(certified|compliant|approved|endorsed)\b|official (university )?(review|certification)')
        bad = []
        for f in ('docs/audit-report.md', 'docs/standards-matrix.md', 'docs/release-checklist.md'):
            p = ROOT / f
            if p.exists():
                for n, ln in enumerate(lines(p), 1):
                    if rx.search(ln) and not re.search(r'(?i)\bnot\b|\bno\b|never|nor\b|does not|cannot|unless', ln):
                        bad.append(f'{f}:{n}')
        self.assertEqual(bad, [])


# --- the audit's own records must agree with each other ------------------------------------------------------------------------------------------
class TestFindingsRegister(unittest.TestCase):
    """docs/findings-register.csv is the source; docs/audit-report.md quotes a summary table of it; every F-nn cited anywhere must exist."""

    @classmethod
    def setUpClass(cls):
        import csv
        with open(ROOT / 'docs' / 'findings-register.csv', newline='', encoding='utf-8') as f:
            cls.rows = list(csv.DictReader(f))

    def test_ids_are_unique_and_fields_are_filled(self):
        ids = [r['id'] for r in self.rows]
        self.assertEqual(len(ids), len(set(ids)))
        for r in self.rows:
            self.assertIn(r['severity'], {'High', 'Medium', 'Low', 'Info'}, r['id'])
            for col in ('title', 'severity_rationale', 'primary_location', 'evidence', 'why_it_matters', 'recommended_correction', 'fixed_in_this_audit',
                        'verification', 'uncertainty', 'researcher_decision_needed'):
                self.assertTrue(r[col].strip(), f"{r['id']} has an empty {col}")

    def test_report_table_matches_the_register(self):
        text = (ROOT / 'docs' / 'audit-report.md').read_text(encoding='utf-8')
        block = text.split('<!-- findings-table:start -->')[1].split('<!-- findings-table:end -->')[0]
        in_table = {}
        for ln in block.splitlines():
            m = re.match(r'\|\s*(F-\d+)\s*\|\s*([A-Za-z]+)\s*\|\s*(.+?)\s*\|', ln)
            if m:
                in_table[m.group(1)] = (m.group(2), m.group(3))
        from_csv = {r['id']: (r['severity'], r['title']) for r in self.rows}
        self.assertEqual(in_table, from_csv)

    def test_every_cited_finding_id_exists(self):
        known = {r['id'] for r in self.rows}
        docs = [p for p in (ROOT / 'docs').glob('*.md')] + [ROOT / n for n in ('CONTRIBUTING.md', 'SECURITY.md', 'CHANGELOG.md')]
        missing = []
        for d in docs:
            for n, ln in enumerate(lines(d), 1):
                for fid in re.findall(r'\bF-\d{2}\b', ln):
                    if fid not in known:
                        missing.append(f'{d.relative_to(ROOT)}:{n} {fid}')
        self.assertEqual(missing, [])

    def test_primary_locations_point_to_real_files_and_lines(self):
        bad = []
        for r in self.rows:
            for m in re.finditer(r'([A-Za-z0-9_./-]+\.(?:py|md|csv|yml|cff|toml|txt))(?::(\d+)(?:-(\d+))?(?:,\s*(\d+))?)?', r['primary_location']):
                path = ROOT / m.group(1)
                if not path.is_file():
                    bad.append(f"{r['id']}: {m.group(1)} not found")
                    continue
                n_lines = len(lines(path))
                for g in (m.group(2), m.group(3), m.group(4)):
                    if g and int(g) > n_lines:
                        bad.append(f"{r['id']}: {m.group(1)}:{g} beyond the {n_lines} lines of the file")
        self.assertEqual(bad, [])


# --- known defects, written as the behaviour the repository should have ---------------------------------------------------------------------
class TestKnownScraperDefects(unittest.TestCase):
    """Each failing test is an audit finding (docs/audit-report.md). Remove the marker when the finding is fixed AND the researcher has approved the change."""

    def offenders(self, rx, only=None):
        out = []
        for p in scraper_sources():
            if only and p.relative_to(ROOT).parts[0] not in only:
                continue
            for n, ln in enumerate(lines(p), 1):
                if rx.search(ln):
                    out.append(f'{p.relative_to(ROOT)}:{n}')
        return out

    @unittest.expectedFailure
    def test_f_tls_verification_is_not_disabled(self):
        self.assertEqual(self.offenders(re.compile(r'verify_mode\s*=\s*ssl\.CERT_NONE|check_hostname\s*=\s*False|_create_unverified_context')), [])

    @unittest.expectedFailure
    def test_f_no_hardcoded_personal_windows_paths(self):
        self.assertEqual(self.offenders(re.compile(r'[A-Za-z]:\\+Users\\+')), [])

    @unittest.expectedFailure
    def test_f_user_agent_does_not_imitate_a_browser(self):
        self.assertEqual(self.offenders(re.compile(r'''['"]User-Agent['"]\s*:\s*['"]Mozilla/'''), only=('scrapers',)), [])

    @unittest.expectedFailure
    def test_f_user_agent_has_no_placeholder_contact(self):
        self.assertEqual(self.offenders(re.compile(r'your-email@example\.com')), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
