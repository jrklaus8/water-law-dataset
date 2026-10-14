import { useEffect, useState } from 'react'

export const parseHash = (h: string): string[] => h.replace(/^#\/?/, '').split('/').filter(Boolean).map(decodeURIComponent)

export function useRoute(): string[] {
  const [route, setRoute] = useState(() => parseHash(window.location.hash))
  useEffect(() => {
    const on = () => setRoute(parseHash(window.location.hash))
    window.addEventListener('hashchange', on)
    return () => window.removeEventListener('hashchange', on)
  }, [])
  return route
}

export const href = (...parts: string[]) => '#/' + parts.map(encodeURIComponent).join('/')
