"""2026-10-04 (late): fourth Drive-inbox batch (9 files). Records the comparison of the last three unchecked effect-size rows with their papers (S470 Amorim 2025,
S489 Koehler 2021, S526 Switzer & Teodoro 2025; all verified) in FULLTEXT_VERIFICATION_2026-10-04.csv. The other six files were renamed re-drops of papers already
processed (S057 Kozole, S084 Lubeck-Schricker, S085 Gaikwad, S483 Mutono, S491 Sempewo; S489 arrived twice). Nothing is copied into the repository.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
VER = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'
SRC = 'Drive inbox full text (2026-10-04 late)'
VERIFIED = {
    'S470': ('7', '7', '', 'verified', 'Table 5 REGU coefficient 19.2078 (SE 0.8174, p < 0.01) in Model 1, 19.155 and 18.819 in Models 2-3; N = 1,144 municipality-years (572 x 2); Table 6 robustness panel 570 municipalities x 4 years = 2,280 observations with REGU 0.1345, 0.1348 and 0.1313 (0-1 index, about 13 points)'),
    'S489': ('6', '6', '', 'verified', 'Table 2 Model 1 (intent to contract the maintenance provider, 1,215 households at 190 waterpoints, SE clustered by waterpoint): concern that water supply is costly OR 0.532 (SE 0.138, p = 0.015); in favour of free water for the vulnerable OR 0.537 (SE 0.120, p = 0.005)'),
    'S526': ('5', '5', '', 'verified', 'Table 4 Model A (unit price ratio at 30,000 gallons, N = 1,183): private ownership -0.167 (p < 0.001), inequality 0.310 (p = 0.005); Model B interaction -0.209 (p = 0.387); 134 investor-owned and 1,055 local-government utilities of 1,189'),
}
with open(VER, encoding='utf-8', newline='') as f:
    raw = f.read()
nl = '\r\n' if '\r\n' in raw else '\n'
rows = list(csv.DictReader(raw.splitlines()))
fields = list(rows[0].keys())
n = 0
for r in rows:
    if r['study_id'] in VERIFIED and r['verdict'] == 'not_checked':
        a, b, c, v, note = VERIFIED[r['study_id']]
        r.update(numbers_in_row=a, numbers_found_in_text=b, numbers_not_found=c, source_text=SRC, verdict=v, note=note)
        n += 1
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(VER))
with os.fdopen(fd, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator=nl); w.writeheader(); w.writerows(rows)
os.replace(tmp, VER)
print('verification rows updated:', n)
