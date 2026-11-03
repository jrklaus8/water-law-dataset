"""2026-10-14 (open item A6, tier 1): the PI's rulings under reviewer CK on (a) S391 and S395, the two rows flagged in batch 1, and (b) the 20 includes of batch 2 (A6_TIER1_BATCHES_2_TO_4_CK_SHEET_2026-10-14.csv).
All 22 are confirmed as includes, so no decision, code, count or family changes (the frozen 0.2.0-interim corpus of 1,080 reports / 1,078 distinct studies, Family B and the RoB 2 trial count are untouched; S366 is kept alongside
its companion trial report S294). Ten of them are recorded as BORDERLINE INCLUDES, with the reason, because their connection to the narrow, rule-type reading of criterion 2 is thin (S391, S395, S374, S366, S357, S354, S369, S368)
or because they are borderline on another criterion (S359 on criterion 3, S378 on the criterion 2 exposure). The note token 'BORDERLINE INCLUDE' is counted in current_figures.py.
Writes a dated note on each row of full_text_screening_database.csv (as for the A16 confirmations: `reviewer_2` and every decision field are unchanged) and fills the ck_* columns of both sheets. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
FT = '02_screening/full_text/full_text_screening_database.csv'
S1 = '02_screening/full_text/A6_TIER1_SECOND_MODEL_CK_SHEET_2026-10-14.csv'
S2 = '02_screening/full_text/A6_TIER1_BATCHES_2_TO_4_CK_SHEET_2026-10-14.csv'
MARK, DATE = 'A6 tier-1 ruling', '2026-10-14'
B = 'BORDERLINE INCLUDE'
R = {  # record_id: (study, borderline?, comment)
    'R0EED09DB6147': ('S391', True, 'Rule-type connection thin. It scores the legality of management and compliance with government institutional criteria (Permendagri, BPPSPAM) across four community-run units; the only rule-type flag is discretion_accommodation and the rule is a regulatory benchmark, not an access rule that varies.'),
    'RC4C6E385D8B9': ('S395', True, 'Rule-type connection thin. It examines local tariff-setting and management discretion under Government Regulation 122/2015 in one community-run system (SPAMDes); the only rule-type flag is discretion_accommodation.'),
    'R03C00C7DDAD7': ('S374', True, 'Rule-type connection thin: Seattle municipal water-utility governance and resilience policy framework; the only rule-type flag is discretion_accommodation.'),
    'R16023D0A5829': ('S361', False, 'Delegated community water-management model in two Togolese towns (eligibility, burden and fee rules).'),
    'R17B1B3A7B266': ('S358', False, 'Arizona groundwater management areas and Tribal versus state primacy; regression over 1,881 service areas.'),
    'R2FB71740FDFD': ('S363', False, 'Sanitation governance and monitoring framework shaping community participation in Jakarta (enforcement).'),
    'R3BFAF175DBF1': ('S366', True, 'Retained alongside its companion trial report S294 (same cluster-randomised trial) under Family B assistance and participation mechanisms; national community-driven WASH programme, the only rule-type flag is discretion_accommodation, so the programme-delivery side of the narrow reading. The Family B effect row of S294 and the RoB 2 trial count are unchanged.'),
    'R3D6B3724D341': ('S359', True, 'Borderline on criterion 3: a practitioner Communication by tribal water-authority co-directors with no stated method or primary data, kept because the federal-Tribal jurisdictional, funding and legal rules are its subject.'),
    'R4699865C8B65': ('S357', True, 'Participatory action research with multisectoral stakeholders on lack of safe water in rural Mpumalanga; examines municipal service-delivery governance under the participatory water-governance framework; the only rule-type flag is discretion_accommodation; partial companion of S369.'),
    'R4FE13503AC55': ('S362', False, 'Constitutional cooperative-government obligations and intergovernmental relations in a South African district (enforcement).'),
    'R581406026ADC': ('S364', False, 'Post-1989 English and Welsh water regulation, legal protections for vulnerable households, disconnection and affordability.'),
    'R5F18E0BC6D04': ('S375', False, 'State tariff and billing regime applied to an informal settlement in Cairo.'),
    'R6667931A0DBB': ('S377', False, 'Service-area regime of the formal utility delegation that excludes legally unrecognised (non loti) neighbourhoods in Burkina Faso.'),
    'R6756A903FAFA': ('S376', False, "Brazil's Law 14.026/2020 audited with the ACERTAR regulatory indicators (eligibility, enforcement, service area)."),
    'R749B86F34484': ('S354', True, 'Rule-type connection thin: post-2002 utility reform and access in Kibera; the only rule-type flag is discretion_accommodation.'),
    'R798F6D592650': ('S378', True, 'Borderline on the criterion 2 exposure: the tested variable is the NFHS-4 wealth index; the Swachh Bharat and open-defecation bill framework is the policy context, not the exposure.'),
    'R7AC977C0F191': ('S379', False, 'Mexican national water law (Ley de Aguas Nacionales) does not recognise community-managed independent systems (eligibility).'),
    'R812E3C486FA8': ('S369', True, 'Photovoice participatory action research in three Mpumalanga villages on the participatory water-governance framework and its municipal devolution; the only rule-type flag is discretion_accommodation; companion of S357.'),
    'R835B5C80B84D': ('S368', True, 'Rule-type connection thin: COVID-19 and municipal service delivery under the developmental local-government framework (household survey, n=449); the only rule-type flag is discretion_accommodation.'),
    'R897B0E5CB3C7': ('S388', False, 'Water-point management arrangement and national governance framework in Liberia (n=11,065 water points); holds a reasoned non-fit effect row.'),
    'R918B0EF111DE': ('S360', False, 'Federal and First Nations drinking-water advisory regime in Ontario (eligibility, enforcement, service area).'),
    'R928138B31379': ('S353', False, 'Safe Drinking Water Act compliance regime and service areas, 662 community water systems; holds a reasoned non-fit effect row.'),
}


def rd(p):
    raw = open(p, newline='', encoding='utf-8').read()
    eol = '\r\n' if '\r\n' in raw[:20000] else '\n'
    with open(p, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r), eol


def wr(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)


ff, ft, feol = rd(FT)
by = {r['record_id']: r for r in ft}
n = 0
for rid, (sid, border, com) in R.items():
    r = by[rid]
    assert r['final_decision'] == 'include', rid
    if MARK in r['notes']:
        continue
    text = f"{B} ({com})" if border else com
    r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"{MARK} {DATE} by CK: confirms include; {text}"
    n += 1
wr(FT, ff, ft, feol)
print(n, 'notes added')

for path, ids in ((S1, {'R0EED09DB6147', 'RC4C6E385D8B9'}), (S2, set(R) - {'R0EED09DB6147', 'RC4C6E385D8B9'})):
    fs, sh, eol = rd(path)
    k = 0
    for x in sh:
        if x['record_id'] in ids:
            sid, border, com = R[x['record_id']]
            x['ck_decision (include/exclude)'], x['ck_exclusion_code (E01-E12)'] = 'include', ''
            x['ck_comment'] = (B + ': ' if border else '') + com
            k += 1
    assert k == len(ids), (path, k, len(ids))
    wr(path, fs, sh, eol)
print('sheets filled: S391/S395 in the batch-1 sheet, 20 rows in the batch sheet; borderline =', sum(1 for v in R.values() if v[1]))
