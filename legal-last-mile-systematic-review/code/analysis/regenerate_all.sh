#!/usr/bin/env bash
# Regenerate every derived file in dependency order, then run the verifier. Run from legal-last-mile-systematic-review/.
# (build_evidence_map.py is not part of this: the evidence map is edited in place by dated scripts.)
set -euo pipefail
cd "$(dirname "$0")/../.."
for s in current_figures:--write audit_data_quality build_fulltext_request_list audit_sparse_records build_reclassification_proposal build_a16_adjudication_sheet audit_exclusion_basis sensitivity_analysis propose_family_vocabulary propose_design_vocabulary audit_effect_size_families audit_includes_criterion3 build_second_extractor_sample build_figures \
         build_preliminary_report build_report_html build_manuscript_pieces build_manuscript_draft build_supporting_texts; do
  name="${s%%:*}"; arg=""; [[ "$s" == *:* ]] && arg="${s#*:}"
  python3 "code/analysis/${name}.py" $arg | tail -1
done
for t in test_a16_pipeline test_second_extractor_scoring test_analysis_helpers test_r_templates test_current_figures_independent test_search_reconciliation test_database_integrity test_sensitivity_invariants test_fix_documented_counts; do
  python3 "code/tests/$t.py" > /tmp/test_$t.log 2>&1 || { cat "/tmp/test_$t.log"; echo "TEST FAILED: $t"; exit 1; }
  tail -1 "/tmp/test_$t.log"
done
python3 code/analysis/verify_repository.py | tail -3
