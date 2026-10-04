#!/usr/bin/env bash
# Regenerate every derived file in dependency order, then run the verifier. Run from legal-last-mile-systematic-review/.
# (build_evidence_map.py is not part of this: the evidence map is edited in place by dated scripts.)
set -euo pipefail
cd "$(dirname "$0")/../.."
for s in current_figures:--write audit_data_quality build_fulltext_request_list audit_sparse_records sensitivity_analysis propose_family_vocabulary build_second_extractor_sample build_figures \
         build_preliminary_report build_report_html build_manuscript_pieces build_manuscript_draft; do
  name="${s%%:*}"; arg=""; [[ "$s" == *:* ]] && arg="${s#*:}"
  python3 "code/analysis/${name}.py" $arg | tail -1
done
python3 code/analysis/verify_repository.py | tail -3
