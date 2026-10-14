import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('..', import.meta.url))

// Relative base keeps the static build working under any GitHub Pages path.
export default defineConfig({
  root: fileURLToPath(new URL('.', import.meta.url)),
  base: './',
  plugins: [react()],
  server: { fs: { allow: [root] } },
  build: { outDir: 'dist', emptyOutDir: true, target: 'es2022' },
})
