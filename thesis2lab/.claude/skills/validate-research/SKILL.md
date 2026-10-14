---
name: validate-research
description: Run relevant tests and generate evidence reports.
---
Run in order and stop at the first failure, diagnosing before retrying (max three attempts):
`npm run validate:schemas`, `npm run validate:experiments`, `npm test`, `npm run test:py`. For interface changes also build and `npm run test:e2e`.
Report real pass or fail counts and any downgrade reasons. Never loosen tolerances or skip tests to get green. Do not sign reviews.
