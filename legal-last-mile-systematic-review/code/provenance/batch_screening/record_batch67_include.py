import csv, tempfile, os

DB = '/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv'

with open(DB) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

target = 'R0482B6E724C6'
note = ('Dallasheh 2022, "Would the United States Come to Nazareth\'s Aid?" Journal of Palestine '
        'Studies. INCLUDE -- extracted as S538 (Legal Institutional Evidence Appraisal Framework). '
        'Archival historical case study of Nazareth water infrastructure as legal-administrative '
        'contest: Municipal Corporations Ordinance 1934, military-government authorization over '
        'municipal water decisions, national water utility (Mekorot) control, 1966 debt-based '
        'water-supply cutoff.')

changed = 0
for r in rows:
    if r['record_id'] == target:
        assert r['full_text_decision'] == '' and r['final_decision'] == '', f"{target} not open!"
        r['full_text_decision'] = 'include'
        r['final_decision'] = 'include'
        r['reviewer_1'] = 'Claude-AI-fulltext-2026-09-21'
        r['notes'] = (r['notes'] + ' ' if r['notes'] else '') + note
        changed += 1

assert changed == 1, f"expected 1, got {changed}"

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, DB)
print('done, changed', changed)
