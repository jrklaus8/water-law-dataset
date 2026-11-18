import csv, tempfile, os

DB = '/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv'

with open(DB) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

targets = {
    'R0206140E81E4': 'Abrams et al 2021, South Africa WASH vulnerability qualitative case study. INCLUDE -- extracted as S536 (CASP). Genuine legal-administrative content: leiwater title-deed-based water allocation, failed municipal system replaced by community Water Committees.',
    'REA101C40B5BB': 'Alam et al 2025, sewer connectivity behaviour-change scoping review. INCLUDE -- extracted as S537 (systematic_review_secondary, AMSTAR 2). Legal-administrative content: mandatory-connection provisions, subsidies, fees, penalties across 11 country case studies.',
}

changed = 0
for r in rows:
    if r['record_id'] in targets:
        assert r['full_text_decision'] == '' and r['final_decision'] == '', f"{r['record_id']} not open!"
        r['full_text_decision'] = 'include'
        r['final_decision'] = 'include'
        r['reviewer_1'] = 'Claude-AI-fulltext-2026-09-21'
        r['notes'] = (r['notes'] + ' ' if r['notes'] else '') + targets[r['record_id']]
        changed += 1

assert changed == 2, f"expected 2, got {changed}"

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, DB)
print('done, changed', changed)
