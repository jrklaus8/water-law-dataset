# EXP-001 Bibliometric explorer (synthetic demonstration)

Status: EXPLORATORY. Data: **synthetic** (`DS-SYN-BIBLIO`, 600 invented records, seeded generator).
Shows how filters, counts, shares, a yearly trend slope and exports work. Describes no real literature.

Verification: TypeScript (`app/src/research/descriptive.ts`) versus an independent Python implementation (`tests/reference_impl.py`) on 7 frozen scenarios, plus repeatability and dataset checks.
Refreeze references after deliberately changing the data or the reference code: `python3 experiments/EXP-001/tests/reference_impl.py --freeze`, then review the diff.
To use real records: register the source, add a dataset record, and a new manifest. Never relabel this one as authentic.
