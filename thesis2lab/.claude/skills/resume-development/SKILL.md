---
name: resume-development
description: Read project state and continue the next approved engineering milestone.
---
1. Read `CLAUDE.md`, run `git status`, read `docs/SESSION_STATE.md`.
2. Run `npm run status`. If anything is stale, revalidate first.
3. Take the first item under "Next steps" in SESSION_STATE that does not need researcher input. If every item needs input, ask for exactly that input.
4. After meaningful progress, update SESSION_STATE.md and commit.
