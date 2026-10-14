"""2026-10-14 (open item A6, tier 1, batches 3 and 4): the PI's rulings under reviewer CK on the last 34 unruled rows of tier 1 of the reviewer-2 queue, which completes all 73 tier-1 rows.
All 34 are confirmations: the 18 AI excludes keep their Pass-1 codes, the 16 AI includes stay includes; so no decision, code, count or family changes. Three includes are recorded as BORDERLINE INCLUDE (S370, S372, S352), which brings the
count from 10 to 13; S380 and S365 are confirmed with a note that their extractions are abstract_only. Writes a dated note on each row of full_text_screening_database.csv (as for the other A6 rulings: reviewer_2 and every decision
field unchanged) and fills the ck_* columns of A6_TIER1_BATCHES_2_TO_4_CK_SHEET_2026-10-14.csv. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
FT = '02_screening/full_text/full_text_screening_database.csv'
SH = '02_screening/full_text/A6_TIER1_BATCHES_2_TO_4_CK_SHEET_2026-10-14.csv'
MARK, DATE, B = 'A6 tier-1 ruling', '2026-10-14', 'BORDERLINE INCLUDE'
X = {  # excludes: record_id: (code, comment)
    'R05BF44B8A339': ('E07', 'Kariba Dam displacement and restitution; the resources at issue are fishery, tourism and hydropower, not household water or sanitation service.'),
    'R19A9F20BC53A': ('E01', 'Total-factor-productivity study of Portuguese utilities; no legal or administrative factor affecting household access.'),
    'R1C0CF917B85E': ('E01', 'Historiography of the WASH sector; not an empirical access study.'),
    'R47B995771A17': ('E01', "Women's problems after the 2023 Kahramanmaras earthquake; toilet access is a minor issue in a broader disaster study."),
    'R47F7BDFF23F7': ('E06', 'Water-security risk-index (SWARA) for five Palestinian cities; an engineering index method.'),
    'R553D7F2BD960': ('E04', "Role-play simulation workshop for peri-urban water institutions; the outcomes are participants' learning, not access."),
    'R6414B5FB0A19': ('E06', 'GIS siting and performance of 741 rural sewage facilities; governance only descriptive.'),
    'R6F38D218A764': ('E01', 'Climate-resilient sanitation planning in four Indonesian cities; planning process, not household access barriers.'),
    'R788D093EA440': ('E07', 'Economics of reclaimed-water markets; wrong service.'),
    'R7B8C7CDFCC7A': ('E05', 'Narrative review of WASH and COVID-19; no empirical data on a legal or administrative access mechanism.'),
    'R8FB559FE24DC': ('E03', 'Ukraine water-management SWOT and composite index; access percentage is only an index input, no legal exposure.'),
    'RB76A3B41BBBF': ('E05', 'Protocol for the ARISE scales; no results.'),
    'RB83291F58980': ('E04', 'Global mapping of WASH-related antimicrobial-resistance policy; strong legal mapping, but the outcome is AMR risk, not access.'),
    'RC3AD9364CFB5': ('E07', "Chile's water-rights market and Atacameno identity; resource-rights markets, not household drinking-water or sanitation service."),
    'RC9C18FC0333A': ('E06', 'Ingredients-based cost estimate for WASH upgrades in Indian health facilities; an engineering cost exercise.'),
    'RCB78D4EF3652': ('E04', 'Rainwater harvesting near Paris as a service model in transition; the empirical outcome is utility revenue and tariff sustainability, not access. This confirms the E04 settled earlier in the ledger (A19) and records it on the row.'),
    'RD4B9888B8A1E': ('E01', '2009 Kurnool flood response and recovery; disaster coping, not an access-barrier study.'),
    'RFF1E12E56199': ('E05', "Conceptual 'capitalist Black Hole' research note; no identifiable study data."),
}
I = {  # includes: record_id: (study, borderline?, comment)
    'R99B6CE47433C': ('S380', False, 'Comparative institutionalist analysis of the rules governing drinking-water access in francophone West Africa. ABSTRACT_ONLY extraction (no full text): this reading rests on the abstract.'),
    'RB5DB265B1A09': ('S365', False, 'Dual formal (municipal) and customary (dorbar shnong) water governance in Shillong, mixed-methods indicators. ABSTRACT_ONLY extraction (no full text): this reading rests on the abstract.'),
    'RBB6D12489912': ('S355', False, 'Institutional and regulatory framework for fecal-sludge services; eight business models in Kampala (burden, fees).'),
    'RBFF9D3F5FAD2': ('S370', True, 'Systematic map of gender-equality and social-inclusion outcomes in WASH interventions: no review-level rule exposure; AMSTAR 2 Critically Low.'),
    'RC0FF0932D727': ('S371', False, 'Indigenous customary governance versus formal coastal-zone regulation in an Indonesian settlement (eligibility, service area).'),
    'RC520790212D3': ('S381', False, 'Post-1989 England and Wales tariff-regulation regime and water poverty (burden, fees).'),
    'RC869B89B74B1': ('S382', False, 'South African constitutional water right and municipal service-provision framework; rural household survey n=448.'),
    'RD03D0D823CB8': ('S372', True, 'Realist review of community-participation mechanisms: mechanisms and contexts rather than a rule; AMSTAR 2 Critically Low.'),
    'RD874B0BA92F5': ('S383', False, 'Mexican national water-concession regime and allocation priority in tourist destinations; 847 concessions plus a resident survey.'),
    'RDBEE0C32E0CA': ('S373', False, 'Increasing block tariff and service-level reform for continuous supply; matched-cohort quasi-experiment.'),
    'RDE592D874BF6': ('S367', False, 'Decree-based central water regulation with no comprehensive national legislation and weak local implementation (Cameroon).'),
    'RE0CF385853FE': ('S384', False, "Nigeria's ODF roadmap and CLTS sanitation-law enforcement framework; cross-sectional survey n=500."),
    'RE6A43701E1CD': ('S400', False, 'LEMA disconnection ban and social-tariff framework in two French sites.'),
    'REDAACBE44344': ('S385', False, 'Colombian fiscal, political and administrative decentralisation regime and municipal water coverage (panel 2008-2019).'),
    'REF1C494CE2D1': ('S352', True, 'One community-built water and sewerage initiative and citizenship claims in Dar es Salaam; the only rule-type flag is discretion_accommodation.'),
    'RF6F82FE94F8C': ('S386', False, 'Weak local regulatory oversight and payment-conditioned access in a Mexican community water system.'),
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


fs, sh, seol = rd(SH)
todo = {x['record_id'] for x in sh if x['batch'] in ('3', '4')}
assert todo == set(X) | set(I) and len(todo) == 34, (len(todo), sorted(todo ^ (set(X) | set(I))))
ff, ft, feol = rd(FT)
by = {r['record_id']: r for r in ft}
n = 0
for rid, (code, com) in X.items():
    r = by[rid]
    assert r['final_decision'] == 'exclude' and r['exclusion_reason'] == code, (rid, r['final_decision'], r['exclusion_reason'])
    if MARK not in r['notes']:
        r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"{MARK} {DATE} by CK: confirms exclude ({code}); {com}"
        n += 1
for rid, (sid, border, com) in I.items():
    r = by[rid]
    assert r['final_decision'] == 'include', rid
    if MARK not in r['notes']:
        r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"{MARK} {DATE} by CK: confirms include; " + (f"{B} ({com})" if border else com)
        n += 1
wr(FT, ff, ft, feol)
print(n, 'notes added')
for x in sh:
    rid = x['record_id']
    if rid in X:
        x['ck_decision (include/exclude)'], x['ck_exclusion_code (E01-E12)'], x['ck_comment'] = 'exclude', X[rid][0], X[rid][1]
    elif rid in I:
        x['ck_decision (include/exclude)'], x['ck_exclusion_code (E01-E12)'], x['ck_comment'] = 'include', '', (B + ': ' if I[rid][1] else '') + I[rid][2]
wr(SH, fs, sh, seol)
print('sheet: rulings in', sum(1 for x in sh if x['ck_decision (include/exclude)']), 'rows')
