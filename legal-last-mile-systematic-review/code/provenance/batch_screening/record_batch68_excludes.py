import csv, tempfile, os, datetime

DB = '/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv'
LOG = '/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv'

excludes = {
    'RD864629E91F7': {
        'title': 'Exploring the socioeconomic determinants of water security in developing regions',
        'authors': 'Nkiaka, Elias',
        'year': '2022',
        'code': 'E01',
        'detail': ('Macro cross-national econometric study (117 countries, 3 developing regions) of a '
                   'composite Water Security Index using GDP per capita, Government Effectiveness Index, '
                   'ODA-WSS, female education, urban population as national-level statistical determinants. '
                   'No examination of any specific household/applicant-level legal-administrative access '
                   'mechanism (eligibility, documentation, fees, connection procedure, enforcement); '
                   '"governance" here is a macro cross-national governance-quality index, not an '
                   'administrative-law mechanism. Wrong unit of analysis and wrong topic for this review.'),
    },
    'R2C5270DE77D8': {
        'title': 'Governance and Practices for Achieving Sustainable and Resilient Urban Water Services',
        'authors': 'Laitinen, Jyrki; Katko, Tapio S; Hukka, Jarmo J; Juuti, Petri; Juuti, Riikka',
        'year': '2022',
        'code': 'E01',
        'detail': ('Sequential PESTEL/SWOT strategic-planning analysis of Finnish urban water utility '
                   'governance, synthesizing prior literature and expert workshops on infrastructure '
                   'investment, institutional framework, and sustainability/resilience. Finland has '
                   'near-universal water access; the paper does not examine any specific household- or '
                   'applicant-level legal-administrative access-exclusion mechanism (eligibility, '
                   'documentation, fees, connection procedure, enforcement) -- it is a generic utility '
                   'governance/sustainability-planning discussion, not empirical access-mechanism evidence.'),
    },
}

with open(DB) as f:
    reader = csv.DictReader(f)
    db_fieldnames = reader.fieldnames
    db_rows = list(reader)

changed = 0
for r in db_rows:
    if r['record_id'] in excludes:
        assert r['full_text_decision'] == '' and r['final_decision'] == '', f"{r['record_id']} not open!"
        info = excludes[r['record_id']]
        r['full_text_decision'] = 'exclude'
        r['final_decision'] = 'exclude'
        r['exclusion_reason'] = info['code']
        r['exclusion_reason_detail'] = info['detail']
        r['reviewer_1'] = 'Claude-AI-fulltext-2026-09-21'
        changed += 1
assert changed == 2, f"expected 2, got {changed}"

with open(DB) as f:
    pass
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=db_fieldnames)
    writer.writeheader()
    writer.writerows(db_rows)
os.replace(tmp, DB)

with open(LOG) as f:
    reader = csv.DictReader(f)
    log_fieldnames = reader.fieldnames
    log_rows = list(reader)

today = '2026-09-21'
for rid, info in excludes.items():
    row = {k: '' for k in log_fieldnames}
    row.update({
        'record_id': rid,
        'title': info['title'],
        'authors': info['authors'],
        'year': info['year'],
        'stage': 'full_text',
        'exclusion_code': info['code'],
        'exclusion_reason_detail': info['detail'],
        'reviewer': 'Claude-AI-fulltext-2026-09-21',
        'date': today,
    })
    log_rows.append(row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(LOG))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=log_fieldnames)
    writer.writeheader()
    writer.writerows(log_rows)
os.replace(tmp, LOG)

print('done, db changed', changed, 'log rows now', len(log_rows))
