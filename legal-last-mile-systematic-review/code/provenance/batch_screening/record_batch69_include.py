import csv, tempfile, os

DB = '/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv'

with open(DB) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

target = 'RA0FB2C52085F'
note = ('Zhang, Gonzalez Rivas, Grant & Warner 2022, "Water pricing and affordability in the US: public vs. '
        'private ownership," Water Policy. INCLUDE -- extracted as S539 (JBI Analytical Cross Sectional). '
        'OLS regression across the 500 largest US community water systems: private ownership associated with '
        '$144 higher annual bill and 1.55pp higher share of low-income household income spent on water '
        '(both p<0.01); state regulation favorable to private providers (NJ/PA fair-value legislation, DSIC '
        'surcharges) associated with $89 higher annual bill. Real legal-administrative mechanisms (PUC '
        'regulation, fair-value legislation) with clean effect estimates -- added to effect_sizes.csv.')

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
