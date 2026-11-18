"""2026-10-14 (open item A14, PI ruling under reviewer CK): honest full-text status for the ten included studies that rest on a landing page or on no file.

Eight (S256, S280, S284, S290, S300, S301, S314, S317) carry full_text_status 'retrieved' and a Drive file named <record_id>_<author>_<year>.pdf that is an HTML page saved under a .pdf name (checked 2026-10-14: a publisher
or repository landing page with the abstract and metadata only; S280 is Springer's 'preview of subscription content', S284 Griffith's 'Metadata only'). Their status becomes 'landing_page_only'. Two (S365, S380) have a blank
status and no Drive file; their status becomes 'abstract_only'. The two values are added to the full_text_status enum (DATA_DICTIONARY.md, verify_repository.py). Inclusion decisions, reviewer labels, extraction rows and the
abstract-only sensitivity analysis are untouched. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '02_screening/full_text/full_text_screening_database.csv'
LANDING = {'R1C49FC594C30': 'S256', 'R44F453EBBB3E': 'S280', 'R5D32F286D8C0': 'S284', 'R63F2C609535B': 'S290', 'REEAB5AAA9C0A': 'S300', 'R9047CC17268A': 'S301', 'RFA4E99C75D4F': 'S314', 'RED5FE8ECD48C': 'S317'}
ABSTRACT = {'RB5DB265B1A09': 'S365', 'R99B6CE47433C': 'S380'}
MARK = 'status set 2026-10-14'
raw = open(P, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(P, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n = 0
for r in rows:
    rid = r['record_id']
    if rid not in LANDING and rid not in ABSTRACT:
        continue
    if MARK in r['notes']:
        continue
    assert r['final_decision'] == 'include' and r['full_text_decision'] == 'include', rid
    if rid in LANDING:
        assert r['full_text_status'] == 'retrieved', (rid, r['full_text_status'])
        new = 'landing_page_only'
        why = (f"the Drive file {rid}_*.pdf for {LANDING[rid]} is a publisher or repository landing page saved under a .pdf name (abstract and metadata only), not the full text; the inclusion decision is unchanged")
    else:
        assert r['full_text_status'] == '', (rid, r['full_text_status'])
        new = 'abstract_only'
        why = (f"there is no full text for {ABSTRACT[rid]} in Drive (only the abstract and introduction were read); the inclusion decision is unchanged")
    r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"[{MARK} by CK (open item A14): full_text_status {r['full_text_status'] or '(blank)'} -> {new}, because {why}; the extraction is an abstract-only extraction and stays in the abstract-only sensitivity analysis]"
    r['full_text_status'] = new
    n += 1
assert n in (0, 10), n
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
os.replace(tmp, P); print(n, 'rows updated')
