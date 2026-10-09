# Finch

**Finch** is a paper-reading skill for LLM agents. It helps you understand an academic paper
well enough to use its ideas:

- **Reconstruct the argument:** what the paper states, assumes, estimates, or proves,
  with locations in the version actually read.
- **Explain the central idea:** what obstacle it overcomes, which ingredient does the
  work, and why that ingredient works.
- **Situate it in the literature:** a small verified neighborhood of foundations,
  predecessors, alternatives, and later work, compared on concrete dimensions.

It covers economics, finance, business, statistics, econometrics, machine learning, and
experimental science. Contribution-type guides load only when relevant.

Finch follows the open [Agent Skills](https://agentskills.io/specification) format, so the
same `skills/finch/` folder works in Claude Code, Codex, Gemini CLI, Cursor, GitHub
Copilot, OpenCode, and other compatible agents.

## Install

The installable skill is `skills/finch/`. Everything else in this repo is design notes and
evaluation material.

**Any agent, via the `skills` CLI** (detects installed agents):

```bash
npx skills add iamsikun/finch            # project scope
npx skills add iamsikun/finch -g         # user scope (all projects)
```

**Claude Code: plugin marketplace**

```bash
claude plugin marketplace add iamsikun/finch
claude plugin install finch@finch
```

**Manual install (symlink or copy the folder):**

| Agent | User-level path | Project-level path |
|---|---|---|
| Claude Code | `~/.claude/skills/finch` | `.claude/skills/finch` |
| Codex | `~/.agents/skills/finch` | `.agents/skills/finch` |
| Gemini CLI | `~/.gemini/skills/finch` or `~/.agents/skills/finch` | `.gemini/skills/finch` or `.agents/skills/finch` |
| Cursor | `~/.cursor/skills/finch` or `~/.agents/skills/finch` | `.cursor/skills/finch` or `.agents/skills/finch` |

```bash
git clone https://github.com/iamsikun/finch.git
ln -s "$PWD/finch/skills/finch" ~/.claude/skills/finch      # Claude Code
ln -s "$PWD/finch/skills/finch" ~/.agents/skills/finch      # Codex / Gemini / Cursor
```

Gemini CLI can also install directly with
`gemini skills install https://github.com/iamsikun/finch --path skills/finch`.

## Use

Agents should pick up Finch automatically when you ask them to read or explain a paper. You
can also invoke it explicitly: `/finch` in Claude Code, or `$finch` in Codex.

```text
Use finch to read this paper: <PDF path, arXiv link, or DOI>.
```

```text
Use finch to read this paper. Assume I am comfortable with economics, statistics,
and machine learning, but unfamiliar with this specific literature. Explain the
essential idea, why it works, what the evidence establishes, and how it differs from
the closest related papers. Put intuition before technical detail.
```

```text
Use finch for a deep reading of the main theorem. Explain the result precisely,
the role of its assumptions, and the important proof steps. Distinguish what you
checked from what remains unverified.
```

```text
Use finch to quickly triage these five papers. Is each worth a full read for my
project on <topic>?
```

Reading modes: **quick orientation**, **standard** (default), **deep technical**, and
**guided co-reading**. Finch infers the mode from your request.

## Repository layout

```
skills/finch/            the installable skill
  SKILL.md               core workflow (modes, routing, evidence, explanation, checks)
  references/            contribution-type guides, loaded on demand
    empirical.md         causal, structural, experimental, descriptive, qualitative
    formal.md            theory, mathematical statistics, optimization, proofs
    computational.md     empirical ML and algorithms
    literature.md        building and verifying a literature neighborhood
docs/design.md           objectives and the research behind each design choice
docs/sources.md          annotated sources and attribution for adapted ideas
evals/                   evaluation protocol, seed prompts, answer-key template
.claude-plugin/          Claude Code plugin + marketplace manifests
```

## Status

This is version 0.1.0, an untested first draft. The design rests on the sources in
`docs/sources.md`, but whether it beats a good ordinary prompt is an empirical question.
See `evals/README.md` for how to test it on papers you know well.

## License

MIT. See [LICENSE](LICENSE). Ideas adapted from other skills are credited in
[docs/sources.md](docs/sources.md).
