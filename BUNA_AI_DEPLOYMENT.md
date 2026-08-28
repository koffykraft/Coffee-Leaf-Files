# Buna AI deployment

## Architecture

- `/api/companion` — existing sensory Companion.
- `/api/guide` — site-wide Buna Guide.
- `buna-index.json` — small source-of-truth navigation/retrieval index.
- `ask-buna.html` — Guide interface.
- `assets/ask-buna.js` — optional floating entry button for pages.

## Scope

Both assistants are intentionally restricted to coffee leaves / Coffea leaves, Buna library resources, Engere, Chemo, Kuti, Kawa Daun, Citane, coffee-leaf processing, chemistry, sensory work, food use, safety, human biology and related research.

The Guide ranks local Buna pages first. If the visitor explicitly enables external research, it queries OpenAlex for records from 2023 onward and passes a small set of result metadata to the language model. External search records are not treated as verified full-text evidence.

## Cloudflare Pages setup

1. Create or open the Pages project for `koffykraft/Coffee-Leaf-Files`.
2. Production branch: `main` after this work is reviewed and merged.
3. Build command: none.
4. Output directory: `.`.
5. Custom domain: `buna.koffykraft.coffee`.
6. Add secret `ANTHROPIC_API_KEY` to Production and Preview if required.
7. Optional variable `BUNA_AI_MODEL`; default in code is `claude-sonnet-4-6`.
8. Deploy and verify `POST /api/companion` and `POST /api/guide`.

## Future upgrade

The local JSON retrieval layer is deliberately simple so launch does not depend on Vectorize. It can later be replaced with Cloudflare AI Search or Vectorize/RAG while keeping the same `/api/guide` contract and UI.

## Security / cost controls still recommended before public launch

- Add Cloudflare rate limiting for `/api/*`.
- Add per-request and per-session length limits to `/api/guide`, matching the existing Companion limits.
- Consider Turnstile only if abuse appears; do not obstruct normal reading by default.
- Keep API keys only in Cloudflare secrets, never in repository files.
