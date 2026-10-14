"""2026-10-14: keep evidence_map.csv `study_design_class` consistent with the appraisal tool after the PI's A11 tool moves (apply_a11_tool_moves_2026-10-14.py).
verify_repository.py requires each design-matched tool to sit with its design class (CASP-qualitative, MMAT-mixed_methods, JBI-observational), as resync_study_design_class.py did on 2026-09-28.
S345 and S231 (CASP) -> qualitative; S333 and S334 (MMAT) -> mixed_methods; S310 (JBI) -> observational. S480 moved from NONE to the Legal Institutional Evidence Appraisal Framework; its old class
'systematic_review_secondary' was only the label that sent it to NONE (the extraction record calls it a documentary/regulatory-compliance review, 'closer to a doctrinal/regulatory-history analysis'), so it becomes `doctrinal`.
The S480 class is an AI classification the PI can veto. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
EM = '05_analysis/descriptive/evidence_map.csv'
NEW = {'S345': 'qualitative', 'S231': 'qualitative', 'S333': 'mixed_methods', 'S334': 'mixed_methods', 'S310': 'observational', 'S480': 'doctrinal'}
raw = open(EM, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(EM, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
done = []
for r in rows:
    if r['study_id'] in NEW and r['study_design_class'] != NEW[r['study_id']]:
        done.append((r['study_id'], r['study_design_class'], NEW[r['study_id']])); r['study_design_class'] = NEW[r['study_id']]
if done:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, EM)
    md = '04_quality/appraisal_forms/A11_TOOL_MOVES_2026-10-14.md'
    with open(md, 'a', encoding='utf-8') as f:
        f.write('\n**Design class kept in step (evidence_map.csv `study_design_class`):** ' + '; '.join(f'{s} {a} -> {b}' for s, a, b in done) +
                ". The verifier requires a design-matched tool to sit with its design class. S480's old class was only the label that had sent it to NONE; `doctrinal` is an AI classification the PI can veto "
                "(script `code/provenance/audit_and_repair/sync_design_class_after_a11_moves_2026-10-14.py`).\n")
for d in done:
    print(*d)
print(len(done), 'design classes updated')
