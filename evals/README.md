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
or URL. Add `assertions` as answer keys mature.

## 5. Iterate

After each round, record the missing intellectual content: an unexplained mechanism,
a dropped condition, a poor choice of predecessor, or the wrong level of detail. Change
the skill only where a pattern recurs, and remove instructions that make no measurable
difference.
