# Notes for agents working on this repo

Finch is a portable Agent Skill. The installable unit is `skills/finch/`; keep it
self-contained, since that folder alone gets copied into users' agents.

- `skills/finch/SKILL.md` frontmatter may only use the six standard fields: `name`,
  `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
  `name` must stay `finch` (it must match the directory name), and `description`
  must stay at or under 1024 characters.
- Keep `SKILL.md` under ~500 lines. Put domain detail in `references/`, one level deep,
  and point to each file from SKILL.md with a statement of when to read it.
- Prefer a few focused guides over many modules. Before adding a file, ask whether an
  existing guide can absorb it.
- Write instructions in the imperative and explain *why*. Avoid all-caps rule lists.
- Keep design rationale in `docs/` and evaluation material in `evals/`, not in the skill folder.
- When adapting ideas from other skills, credit them in `docs/sources.md`. Do not copy text
  from repositories without a license.
- Bump `metadata.version` in SKILL.md and `version` in `.claude-plugin/plugin.json` together.
- Validate after editing: `uv run --no-project python scripts/validate.py` and
  `uvx --from skills-ref agentskills validate skills/finch`; for manifests, `claude plugin validate .`.
