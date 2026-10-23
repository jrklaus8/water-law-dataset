import csv, tempfile, os

DB = '/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv'
LOG = '/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv'

includes = {'R9FFEBB4E1EFA': ('Silva-Novoa Sanchez, Bossenbroek, Schilling & Berger 2022, "Governance and Sustainability '
            'Challenges in the Water Policy of Morocco 1995-2020," Water. INCLUDE -- extracted as S540 (CASP). Content '
            'analysis of 10 policy documents + 37 semi-structured interviews. Genuine legal-administrative mechanisms: '
            'well-digging permits (illegal digging, bribery for permits), drip-irrigation subsidy eligibility circularity '
            '(tribal land-use certificate required before permit, permit required before certificate), institutional '
            'fragmentation between Agriculture/Water/Interior ministries, unequal water-rights allocation (Kharouba/1/8/'
            '1/4 shares), unconnected households.')}

excludes = {
    'R397656949E83': {
        'title': "Construing the transformed property paradigm of South Africa's water law: new opportunities presented by legal pluralism?",
        'authors': 'Viljoen, Germarie',
        'year': '2022',
        'code': 'E05',
        'detail': ('Purely doctrinal/theoretical property-law analysis of South Africa\'s National Water Act public-'
                   'trusteeship model, comparing public/common-property/African-customary-law paradigms for classifying '
                   'water as a legal object. No empirical study of household-level water access, connection, or '
                   'administrative service-delivery outcomes; the two case-law examples discussed (Mostert -- illegal '
                   'water abstraction/theft prosecution; Gongqose -- customary fishing rights) do not concern household '
                   'water/sanitation service access. Pure doctrinal commentary without empirical access evidence.'),
    },
    'R98A0DCEA5699': {
        'title': 'The contemporary challenges municipalities face in effectively implementing municipal service partnerships',
        'authors': 'Mamokhere, John; Mabeba, Selaelo John; Kgobe, France Khutso Lavhelani',
        'year': '2022',
        'code': 'E07',
        'detail': ('Self-described "conceptual paper" (no primary empirical data collection; Critical Discourse '
                   'Analysis of secondary literature/legislation only) about general Municipal Service Partnerships '
                   '(MSPs/PPPs) across all South African municipal services (housing, electricity, roads, water, PPE '
                   'procurement during COVID-19) -- water is mentioned only incidentally as one example service among '
                   'several, not the specific focus of empirical access-mechanism analysis this review requires.'),
    },
    'R1BF978DC83F1': {
        'title': 'Predictors of access to safe drinking water: policy implications',
        'authors': 'Shadabi, Leila; Ward, Frank A',
        'year': '2022',
        'code': 'E01',
        'detail': ('Macro cross-national panel-regression study (74 countries, 2012-2017) explaining aggregate national '
                   'safe-drinking-water-access percentage using GDP per capita, Gini coefficient, education, a '
                   'Transparency International corruption-avoidance index, government-size (% of GDP), a World Bank '
                   'government-effectiveness index, and a Freedom House civil-liberties index. Same genre as the '
                   'earlier-excluded Nkiaka (2022): macro cross-national governance-quality indices, not a specific '
                   'household/applicant-level legal-administrative access mechanism. Wrong unit of analysis (country) '
                   'and wrong topic for this review\'s scope.'),
    },
}

with open(DB) as f:
    reader = csv.DictReader(f)
    db_fieldnames = reader.fieldnames
    db_rows = list(reader)

changed = 0
for r in db_rows:
    if r['record_id'] in includes:
        info = includes[r['record_id']]
        assert r['full_text_decision'] == '' and r['final_decision'] == '', f"{r['record_id']} not open!"
        r['full_text_decision'] = 'include'
        r['final_decision'] = 'include'
        r['reviewer_1'] = 'Claude-AI-fulltext-2026-09-21'
        r['notes'] = (r['notes'] + ' ' if r['notes'] else '') + info
        changed += 1
    elif r['record_id'] in excludes:
        info = excludes[r['record_id']]
        assert r['full_text_decision'] == '' and r['final_decision'] == '', f"{r['record_id']} not open!"
        r['full_text_decision'] = 'exclude'
        r['final_decision'] = 'exclude'
        r['exclusion_reason'] = info['code']
        r['exclusion_reason_detail'] = info['detail']
        r['reviewer_1'] = 'Claude-AI-fulltext-2026-09-21'
        changed += 1

assert changed == 4, f"expected 4, got {changed}"

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
