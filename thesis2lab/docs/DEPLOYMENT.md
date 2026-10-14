# Local use and deployment

## Run locally
```
cd thesis2lab
npm install
npm run dev            # http://localhost:5173
```
Build and preview the static site: `npm run build && npm run preview` (http://localhost:4173). The output is `app/dist/`; any static host works.

## Checks before publishing
`npm run check:all` runs typecheck, unit tests, Python tests and the build (which validates schemas and experiments). `npm run test:e2e` runs browser and accessibility tests against the built site.

## CI
`.github/workflows/thesis2lab-ci.yml` (repository root) runs on pull requests and pushes that touch `thesis2lab/`: schemas, validation reports (fails if committed reports are stale), unit, Python and browser tests, build, link check of the static output, and uploads the build and a validation summary.

## GitHub Pages (manual, not yet enabled)
`.github/workflows/thesis2lab-pages.yml` runs only on manual dispatch. **Read first:** this repository already publishes the old dashboard from `docs/`. Setting the Pages source to "GitHub Actions" would replace that site. Recommended: move Thesis2Lab into its own repository (`git subtree split --prefix=thesis2lab -b thesis2lab-only`), move the two workflow files to its `.github/workflows/` and remove the `thesis2lab/` path prefixes, then enable Pages there. The static build works under any sub-path.

Publishing needs a human decision: review `npm run status`, confirm the draft release, and run the workflow yourself.

## Optional later
Zenodo archiving of approved releases (connect the repository in Zenodo, tag a release). No custom domain needed.
