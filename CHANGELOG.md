# Changelog

Finch uses semantic versioning:
- **Major** releases change the output structure or the reading workflow noticeably.
- **Minor** releases add guidance or capabilities.
- **Patch** releases make wording fixes.

## 0.1.0 — 2026-10-09

First release.
- Core workflow: reading modes, routing by contribution type, an evidence ledger with
  intellectual-status labels, the four checks, mechanism reconstruction with the
  removal test, a verified literature neighborhood, and layered output.
- Reference guides: `empirical.md`, `formal.md`, `computational.md`, `literature.md`.
- Fixes from the first smoke test:
  - a routing row for methodology papers
  - length guidance for standard readings
  - PDF extraction fallbacks
  - the four checks merged into the final checklist
- Distribution:
  - `install.sh` with automatic daily updates from the `stable` branch
  - Claude Code plugin manifests
