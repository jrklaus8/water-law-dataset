---
name: publish-lab
description: Build the public site and prepare a versioned release. Never deploys by itself.
---
1. `npm run check:all`, then `npm run test:e2e`.
2. `npm run status`. Stop and report if any experiment is downgraded or any report is stale.
3. `npm run release:prepare -- X.Y.Z` (draft). Tell the user a researcher must approve it and that deployment is a manual workflow (see `docs/DEPLOYMENT.md`, including the warning about the existing GitHub Pages site).
4. Do not push, tag, deploy or enable Pages without explicit instruction.
