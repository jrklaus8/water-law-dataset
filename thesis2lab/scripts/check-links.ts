/** Checks relative links in Markdown files and internal route links in source. External URLs are not fetched (no network in CI by design). */
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs'
import { dirname, join, relative } from 'node:path'
import { ROOT, p } from './lib/project'

const md: string[] = []
const walk = (d: string) => readdirSync(d).forEach((n) => {
  if (['node_modules', 'dist', '.git', 'test-results'].includes(n)) return
  const f = join(d, n)
  if (statSync(f).isDirectory()) walk(f)
  else if (f.endsWith('.md')) md.push(f)
})
walk(ROOT)
const bad: string[] = []
for (const f of md) {
  for (const m of readFileSync(f, 'utf8').matchAll(/\]\((?!https?:|mailto:|#)([^)\s]+)\)/g)) {
    const target = join(dirname(f), m[1].split('#')[0])
    if (!existsSync(target)) bad.push(`${relative(ROOT, f)} -> ${m[1]}`)
  }
}
const routes = new Set(['', 'cover', 'thesis', 'lab', 'evidence', 'compare', 'methods', 'versions', 'about'])
const app = readFileSync(p('app/src/App.tsx'), 'utf8')
for (const m of app.matchAll(/path: '([^']*)'/g)) if (!routes.has(m[1])) bad.push(`App.tsx navigation names unknown route ${m[1]}`)
if (bad.length) { console.error('Broken links:\n  ' + bad.join('\n  ')); process.exit(1) }
console.log(`Link check passed: ${md.length} Markdown files, navigation routes valid.`)
