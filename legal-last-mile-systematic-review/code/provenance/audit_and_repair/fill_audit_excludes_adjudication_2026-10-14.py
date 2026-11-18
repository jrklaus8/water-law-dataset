"""2026-10-14: write the PI's rulings (reviewer CK) on the four open substantive excludes of EXCLUSION_BASIS_AUDIT_2026-10-04.md as a filled adjudication sheet,
02_screening/full_text/AUDIT_EXCLUDES_ADJUDICATION_FILLED_2026-10-14.csv, in the layout apply_a16_adjudications.py reads. All four exclusions are confirmed; R0B0F3925F533 and RC9378CBDB2EE are re-coded E01 to E04
(no household access outcome), R977ECB01FA02 and RFC362FE42028 keep E01. Run from legal-last-mile-systematic-review/."""
import csv, sys
csv.field_size_limit(sys.maxsize)
FT = '02_screening/full_text/full_text_screening_database.csv'
OUT = '02_screening/full_text/AUDIT_EXCLUDES_ADJUDICATION_FILLED_2026-10-14.csv'
ROWS = [
 ('R0B0F3925F533', 'E04', 'A19 wider-set ruling 2026-10-14: exclusion confirmed and re-coded E01 to E04. Rahayu et al. 2019 studies inter-local cooperation over a utility\'s water supply; there is no household water or sanitation access outcome. Full text read 2026-10-04.'),
 ('R977ECB01FA02', 'E01', 'A19 wider-set ruling 2026-10-14: exclusion confirmed, E01 kept. Milgroom et al. 2014 study access to bundled natural resources after resettlement; household water-service findings are not separable. Full text read 2026-10-04.'),
 ('RC9378CBDB2EE', 'E04', 'A19 wider-set ruling 2026-10-14: exclusion confirmed and re-coded E01 to E04. Steflova et al. 2022 assess governance capacity for desalination; the measured outcomes are institutional barriers, perceptions and environmental impact, not household service access. Full text read 2026-10-04.'),
 ('RFC362FE42028', 'E01', 'A19 wider-set ruling 2026-10-14: exclusion confirmed, E01 kept. Espluga et al. 2011 study public participation in river-basin planning under the EU Water Framework Directive, not household service access. Full text read 2026-10-04.'),
]
ft = {r['record_id']: r for r in csv.DictReader(open(FT, newline='', encoding='utf-8'))}
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['record_id', 'citation', 'ai_decision', 'researcher_decision (include/exclude)', 'researcher_exclusion_code (E01-E12)', 'researcher_comment'])
    for rid, code, com in ROWS:
        r = ft[rid]
        assert r['final_decision'] == 'exclude' and r['exclusion_reason'] == 'E01', (rid, r['exclusion_reason'])
        w.writerow([rid, f"{r['authors'][:60]} ({r['year']}). {r['title'][:120]}", 'exclude E01', 'exclude', code, com])
print('wrote', OUT)
