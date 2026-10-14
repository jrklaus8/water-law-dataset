import { useEffect, useRef } from 'react'
import { config } from './lib/registry'
import { href, useRoute } from './lib/router'
import { AboutPage } from './pages/About'
import { CoverPage } from './pages/Cover'
import { ComparePage } from './pages/Compare'
import { EvidencePage } from './pages/Evidence'
import { ExperimentPage } from './pages/Experiment'
import { HomePage } from './pages/Home'
import { LabPage } from './pages/Lab'
import { MethodsPage } from './pages/Methods'
import { ThesisPage } from './pages/Thesis'
import { VersionsPage } from './pages/Versions'

const NAV: { path: string; label: string }[] = [
  { path: '', label: 'Home' }, { path: 'cover', label: 'Read first' }, { path: 'thesis', label: 'Thesis' }, { path: 'lab', label: 'Laboratory' }, { path: 'evidence', label: 'Evidence' },
  { path: 'compare', label: 'Compare' }, { path: 'methods', label: 'Methods' }, { path: 'versions', label: 'Versions' }, { path: 'about', label: 'About' },
]

function Page({ route }: { route: string[] }) {
  const [top, id] = route
  switch (top) {
    case undefined: return <HomePage />
    case 'thesis': return <ThesisPage focus={id} />
    case 'lab': return id ? <ExperimentPage id={id} /> : <LabPage />
    case 'evidence': return <EvidencePage focus={id} />
    case 'compare': return <ComparePage />
    case 'methods': return <MethodsPage />
    case 'versions': return <VersionsPage />
    case 'cover': return <CoverPage />
    case 'about': return <AboutPage />
    default: return <section><h1 tabIndex={-1}>Page not found</h1><p><a href={href()}>Return home</a></p></section>
  }
}

export function App() {
  const route = useRoute()
  const main = useRef<HTMLElement>(null)
  const first = useRef(true)
  useEffect(() => {
    // Move focus to the new page and update the title, so keyboard and screen reader users notice navigation.
    const h1 = main.current?.querySelector('h1')
    document.title = `${h1?.textContent ?? 'Page'} | ${config.project.title}`
    if (first.current) { first.current = false; return }
    ;(h1 as HTMLElement | null)?.focus()
    window.scrollTo(0, 0)
  }, [route.join('/')])
  const current = route[0] ?? ''
  return (
    <>
      <a className="skip" href="#main" onClick={(e) => { e.preventDefault(); main.current?.focus() }}>Skip to content</a>
      <header className="site-header">
        <div className="wrap bar">
          <a className="brand" href={href()}><span className="logo" aria-hidden="true">T2L</span> <span>{config.project.title}<small>Thesis2Lab</small></span></a>
          <nav aria-label="Main">
            <ul>{NAV.map((n) => <li key={n.path}><a href={n.path ? href(n.path) : href()} aria-current={current === n.path ? 'page' : undefined}>{n.label}</a></li>)}</ul>
          </nav>
        </div>
        <div className="wip" role="note"><div className="wrap">Research in progress. The thesis is not written yet. Read each result together with its status label.</div></div>
      </header>
      <main id="main" tabIndex={-1} ref={main} className="wrap"><Page route={route} /></main>
      <footer className="site-footer"><div className="wrap">
        <p>{config.project.disclaimer}</p>
        <p>Calculations run in your browser. No data leave your device and no AI service is contacted.</p>
      </div></footer>
    </>
  )
}
