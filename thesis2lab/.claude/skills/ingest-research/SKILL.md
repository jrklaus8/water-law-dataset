---
name: ingest-research
description: Add new research material (chapter, article, dataset, method) without rebuilding everything.
---
Follow `docs/ADDING_RESEARCH.md` sections 1 to 3.
1. Ask the user for the file path and, if unknown, its copyright and confidentiality status. Stop if they are restricted and the user has not authorised use.
2. `python3 pipelines/ingest/register_source.py PATH --title ... --kind ... --copyright ...`.
3. Extract only the sections relevant to the request. For PDFs without a parser, say extraction is not possible yet; do not guess text.
4. Use the research-mapper agent only if scripts cannot do it. Pass the source id and sections, not the whole file.
5. `npm run validate:schemas`, then `npm run changes` to list affected experiments. Report what changed.
