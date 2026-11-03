"""2026-10-14: give the 12 'Group 1' studies kept by the PI's A24 ruling (S200, S207, S649, S650, S651, S652, S655, S662, S679, S848, S909, S970) a rule-type mechanism flag in extraction_database.csv.

The A24 recheck sheet listed them as carrying governance-type flags only (participation, institutional fragmentation, political coordination, bureaucratic assistance, formal connection); the PI ruled that a legal or
administrative rule is the direct subject of each and asked that the flags say so. The flags below are an AI classification from the text ALREADY in each extraction row (regulatory_model, effect_estimate and the evidence-map
mechanism family); no paper was re-read for this, and the PI can veto any of them. Each change is recorded in the row's extraction_note. evidence_map.csv needed no change: all 12 rows already carry a rule-related
mechanism_family. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '03_extraction/extracted_data/extraction_database.csv'
MARK = 'A24 keep ruling 2026-10-14'
FLAGS = {
    'S200': (['discretion_accommodation'], 'no federal rule says who manages the decentralised sewage systems in use and only some states assign that responsibility (evidence-map family DISCRETION_ACCOMMODATION)'),
    'S207': (['service_area'], "Brazil's 2020 reform sets national reference standards, regionalisation and mandatory tenders for service provision"),
    'S649': (['service_area'], 'Article 115 of the Constitution assigns water-service management to municipalities and federal per-capita transfers fund up to 45% of municipal water investment'),
    'S650': (['service_area'], 'the 2008 Constitution (Article 318) creates a single water authority (SENAGUA) with overlapping jurisdiction among MIDUVI, MAE, MSP and INAR'),
    'S651': (['enforcement'], 'the PURC Act 538 (1997) set up the regulator and an affermage-style management contract governs urban supply'),
    'S652': (['eligibility', 'tenure'], "the settlement's illegal tenure status bars a direct DWASA connection, until a 2007 mandate to supply 'slum' committees regardless of tenure"),
    'S655': (['tenure', 'property'], 'tenure insecurity and a landowner-consent requirement block formal service extension in informal settlements'),
    'S662': (['service_area'], 'the Urban Councils Act and Water Policy 2012 designate local authorities as service authorities for urban water (operation and maintenance duties)'),
    'S679': (['property'], 'the National Water Act 1998 and the 1996 abolition of riparian rights and private land-based water ownership'),
    'S848': (['eligibility'], "the Indian Act's reserve system fixes who carries responsibility for, and funding of, First Nations water systems (evidence-map family eligibility)"),
    'S909': (['property'], 'the National Water Act 1998 reclassified groundwater from private property to a public significant resource'),
    'S970': (['property'], 'constitutional recognition of the human right to water and public ownership of water in Uruguay, Bolivia and Ecuador'),
}
raw = open(P, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(P, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
by = {r['study_id']: r for r in rows}
n = 0
for sid, (flags, basis) in FLAGS.items():
    r = by[sid]
    if MARK in r['extraction_note']:
        continue
    assert all(f in fields for f in flags), flags
    for f in flags:
        r[f] = 'TRUE'
    r['extraction_note'] = (r['extraction_note'].rstrip() + ' ' if r['extraction_note'] else '') + (
        f"[{MARK}: kept by the PI's narrow-scope recheck (a legal or administrative rule is the direct subject); rule-type flag(s) {', '.join(flags)} set because {basis}. "
        'AI classification from the existing extraction text, not a new reading of the paper.]')
    n += 1
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
os.replace(tmp, P)
print(f'{n} rows updated')
