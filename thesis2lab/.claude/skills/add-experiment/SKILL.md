---
name: add-experiment
description: Create an experiment from a documented method and registered source material.
---
Follow `docs/ADDING_RESEARCH.md` section 4.
1. Confirm the method is documented in a registered source and the data are registered with a dataset record. If not, create a BLOCKED manifest instead and list what is missing.
2. Copy the nearest experiment, set the next EXP number, edit the manifest. Start `reproducibility_status` at UNVERIFIED unless it is a labelled demonstration (EXPLORATORY).
3. Implementation by the reproducibility-engineer; independent reference by the scientific-validator (never the same author on the same logic).
4. `npm run validate:schemas && npm run validate:experiments`. Raise the declared status only as far as the report supports.
