import { defineConfig } from 'vitest/config'
import { fileURLToPath } from 'node:url'

export default defineConfig({
  root: fileURLToPath(new URL('..', import.meta.url)),
  test: { include: ['app/src/**/*.test.ts', 'tests/unit/**/*.test.ts'], environment: 'node' },
})
