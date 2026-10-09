import csv, tempfile, os

EM = '/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv'

with open(EM) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

row = {k: '' for k in fieldnames}
row.update({
    'study_id': 'S538',
    'study_design_class': 'doctrinal',
    'evidence_level': 'Archival historical case study drawing on primary-source government, municipal, and press archives (Israeli State Archives, Nazareth Municipal Archives, US National Archives, Knesset records). Legal Institutional Evidence Appraisal Framework rating deferred pending the official instrument; provisional confidence: high for the documented sequence of administrative control (extensively archivally sourced with named files/dates), moderate for causal interpretation of settler-colonial intent (author\'s own analytical framing).',
    'mechanism_family': 'MULTIPLE',
    'outcome_family': 'effective_access',
    'quantitative_synthesis_eligible': 'FALSE',
    'qualitative_synthesis_eligible': 'TRUE',
    'legal_context': 'common law (Mandate-era ordinance retained under Israeli military administration)',
    'institutional_context': 'Nazareth\'s water-infrastructure decisions were formally vested in its elected municipal council under the 1934 Municipal Corporations Ordinance but required Israeli military-government authorization at every step (funding, equipment import, foreign currency) during 1948-1966 martial law; Mekorot, the national water utility, ultimately secured control of the municipal well as a condition of network connection (1955) and later weaponized a water debt to force a 1966 supply cutoff against an elected mayor.',
})
rows.append(row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, EM)
print('done, total rows now', len(rows))
