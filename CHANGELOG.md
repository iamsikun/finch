# Changelog

Finch uses semantic versioning:
- **Major** releases change the output structure or the reading workflow noticeably.
- **Minor** releases add guidance or capabilities.
- **Patch** releases make wording fixes.

## 0.2.0 — 2026-10-09

- Fill gaps in the existing reading workflow: honor focused questions and reader
  preferences; explain equations and figures with their conditions beside the claims;
  support interruptions and optional comprehension checks during co-reading.
- Add survey/meta-analysis/perspective guidance to the existing literature guide,
  source-status checks, and clearer sample, benchmark, and reproducibility checks.
- Bundle an optional PDF extraction helper with page anchors, source hashes, and sparse
  page warnings, plus the license needed when copying only the skill folder.
- Make the updater skip tracked and untracked local edits before fetching.
- Add a `finch` command (linked into `~/.local/bin`): `finch status`, `finch update`,
  `finch uninstall`.
- Extend portable-resource validation, utility regression tests, and behavioral evals.

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
