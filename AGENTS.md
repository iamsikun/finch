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

## Releasing

Development happens on `main`. Users install from the `stable` branch, and their
installs update automatically: `install.sh` runs a daily fast-forward, and Claude Code
checks the plugin version. Only move `stable` deliberately:

1. Run the validators above and at least one smoke reading from `evals/evals.json`.
2. Bump the version in `skills/finch/SKILL.md` (`metadata.version`) and in
   `.claude-plugin/plugin.json`. Use semantic versioning: a major bump means a visible
   change to the output structure or the workflow. Claude Code only updates a plugin when
   this version changes.
3. Add an entry to `CHANGELOG.md`.
4. Commit, tag, and publish:
   ```bash
   git tag vX.Y.Z
   git push origin main vX.Y.Z
   git push origin main:stable      # this is the release; it fast-forwards stable
   ```

Never force-push `stable`. Installs update with `--ff-only`, so rewriting the branch's
history would leave them stuck on the old version.
