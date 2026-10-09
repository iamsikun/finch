# Evaluating Finch

A skill is a hypothesis that the agent will behave better with it. Test that hypothesis
against good alternatives, on papers you know well.

## 1. Build a reference set

Start with **12–18 development papers** and a **separate held-out set of 4–6 papers**.
Choose papers you understand deeply, covering the contribution types:

- causal empirical
- structural
- formal theory and mathematical statistics
- empirical ML
- experimental
- descriptive or qualitative

Include hard cases:

- qualifications buried in appendices
- tables that extract badly
- papers with substantively different revised versions
- papers whose introduction claims more than their results support

For each paper, write an answer key with `answer-key-template.md` **before** looking at
any model output. Keep keys under `evals/keys/`. Paper PDFs go under `evals/papers/`,
which is gitignored.

## 2. Compare against meaningful baselines

Use the same model, paper version, tools, output budget, and approximate effort for:

1. **Plain request:** "Read this paper and explain it to me."
2. **Good generic prompt:** a concise, well-written reading prompt without the skill
   (see `baseline-prompt.md`).
3. **Finch.**

Run **paper-only** conditions (no web access) separately from **retrieval** conditions.
Otherwise extra retrieval can pass for better reading.

## 3. Score separate dimensions

Score each dimension from 0 to 2 (absent, partial, good) against the answer key:

| Dimension | Question |
|---|---|
| Essential-idea coverage | Does the output convey the ideas that determine the contribution? |
| Factual fidelity | Are results, quantities, signs, and comparisons correct? |
| Scope fidelity | Are assumptions, populations, quantifiers, and regimes preserved? |
| Mechanistic explanation | Could you explain why the method or argument works? |
| Attribution | Are inherited ideas, new findings, and interpretations distinguished? |
| Citation support | Do the references exist, and do they support the statements? |
| Literature value | Are the comparisons close, verified, and informative? |
| Calibration | Are missing evidence and open issues handled honestly? |
| Efficiency | How much reading and verification time does the output need? |

**Count severe errors separately; never average them away:**

- fabricated findings
- invented citations
- reversed conclusions
- a missing assumption the result depends on

A polished output with one severe error is worse than a plain output with none.

**Transfer test.** Finish with the key's transfer question, something like "what changes
if assumption X fails?" or "would this method work for problem Y?". Check whether
reading the output lets you answer it.

## 4. Running evals

`evals.json` follows the Anthropic skill-creator schema, so its eval loop can run these
prompts with and without the skill. Each prompt's `files` should point to the paper PDF
when a local fixture is available; otherwise put the versioned URL in the prompt. Add
`assertions` as answer keys mature. Synthetic excerpts in cases 4–8 are self-contained
behavioral regressions, not real papers or substitutes for domain evaluation.

Run packaging and utility checks separately from reading evals:

```bash
uv run --no-project python scripts/validate.py
uvx --from skills-ref agentskills validate skills/finch
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
uv run --no-project python -m unittest discover -s scripts -p 'test_*.py'
```

The utility tests exercise failure handling, page boundaries, non-overwrite behavior,
and updater preservation of local edits. They cannot measure reading quality.

## Recorded smoke reading

`keys/conformal-v2.md` pins the source and expectations for case 2.
`smoke-conformal-v2.md` records the October 9, 2026 manual reading and its verification
limits. The same agent authored and checked it: this is a source-checked smoke run,
not an independent evaluation, benchmark score, or comparison against a baseline.
The new cases 4–8 are regression prompts awaiting model runs.

## 5. Iterate

After each round, record the missing intellectual content: an unexplained mechanism,
a dropped condition, a poor choice of predecessor, or the wrong level of detail. Change
the skill only where a pattern recurs, and remove instructions that make no measurable
difference.
