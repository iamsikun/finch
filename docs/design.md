# Finch design notes

This file records what Finch is trying to do and why each part of the skill exists, so
changes can be judged against intent. Sources are listed in [sources.md](sources.md).

## Objective

Finch serves three connected goals:

1. **Reconstruct** the paper's argument.
2. **Explain** its central idea.
3. **Situate** it in the literature.

The test of success is whether the reader can answer seven questions:

1. What problem does the paper solve, and why is it hard?
2. What is the new idea?
3. Why does it work?
4. What is established, and under which conditions?
5. What was already known?
6. Where does the argument stop applying?
7. What tool is worth retaining?

These questions condense into a target sentence:

> Earlier approaches could do A under B. This paper introduces C, which makes D possible
> because E. Its evidence establishes F under G, while H remains unresolved.

The default reader is a quantitatively trained researcher (economics, statistics, ML,
business) who is new to the specific literature.

## Design principles and their grounds

| Skill element | Rationale | Grounding |
|---|---|---|
| Reading modes (quick / standard / deep / co-reading) | Give each stage of attention its own objective | Keshav's three-pass method; Carey et al. "read with a purpose" |
| Route by contribution type | A proof and a field experiment need different reconstruction | Economics reading guides (Price; Oh); finance-paper-reader's empirical/theory/mixed split |
| Faithful vs. explanatory reconstruction | Restating propositions is different from understanding the situation they describe | Kintsch's construction–integration model (applied here by analogy) |
| Small checkable explanations (special case, failed assumption) | Self-explanation helps human learning, and small explanations are easy to inspect | Chi et al. (1994). This supports the reader's learning; it does not show that LLM explanations are accurate. |
| Intellectual status labels (inherited / modified / new / interpreted / inferred) | Contributions hide in how familiar parts are recombined; attribution is part of summarization | Teufel & Moens' rhetorical status; theory-paper-reader's provenance labels |
| Evidence ledger before drafting | Attribution is more precise when sources are selected before generation | Slobodkin et al., "Attribute First, then Generate" (2024); QASPER evidence anchoring |
| Four separate checks (existence, passage support, scope, warrant) | Answer quality and citation quality come apart; a real citation can still drop the condition that makes it true | ALCE (Gao et al. 2023); SciFact (Wadden et al. 2020) |
| Targeted rereading of supporting sections | Models use long contexts unevenly | Liu et al., "Lost in the Middle" (2024). Current models may differ, so the skill recommends rereading rather than assuming an error rate. |
| Verified literature neighborhood with a stated relationship per paper | Synthesis needs retrieval that can return to sources | OpenScholar (Asai et al. 2026) |
| Concerns as questions tied to locations | Proportionate, checkable critique | finance-paper-reader (idea); K-Dense scientific-critical-thinking |
| "Not reported" ≠ "not done" | Avoids false accusations of omission | K-Dense scientific-critical-thinking |
| Compact core plus a few on-demand guides | Focused skills outperformed exhaustive bundles in one benchmark | SkillsBench (Li et al. 2026). This is a pattern from one setting, not a universal law. |

## What is deliberately left out (for now)

- **No retrieval backend.** Finch uses whatever search tools the host agent has. If
  searching a personal corpus becomes a bottleneck, PaperQA or OpenScholar could serve as a
  backend.
- **No archival multi-file outputs.** The default output is a reading brief in the
  conversation. Notes and collections belong outside the skill.
- **No fixed scoring rubric inside the skill.** Scoring belongs in `evals/`.
- **No biomedical appraisal frameworks** (GRADE, RoB 2). They can be added as a guide if
  clinical papers become a use case.

## Open questions to settle with evaluation

- Does the evidence ledger improve fidelity enough to justify its cost in effort?
- Is the 3–6 paper neighborhood the right default, or should standard reading be
  paper-only unless asked?
- Do the contribution guides help, or does the core alone match their performance?
- Which output sections do readers actually use?

## Audit findings, October 9, 2026

The installed 0.1.0 skill matched the repository at `d29befe` byte for byte. Codex's
session catalog exposed Finch through the shared `~/.agents/skills/finch` link to the
stable clone; Claude and Copilot links and a daily launchd configuration also existed.
This confirms discovery and file integrity in this environment, not automatic selection
or compliance by every supported agent. A separate `~/.codex/skills/finch` copy was not
needed. The installable folder's reference routes were complete.

The content audit found a strong argument/evidence workflow, with narrower gaps:

- A focused question was advertised in discovery but not exempted from the standard
  report and literature-search defaults. Make its scope explicit.
- The contribution router omitted reviews and meta-analyses. Absorb that guidance into
  the existing literature guide rather than adding another module.
- Equations and visual evidence needed more explicit writing instructions, especially
  symbol roles, transformations, axes, denominators, and local qualifications.
- Source existence/version checks did not cover publication-status notices or distinguish
  primary-source inspection clearly enough from secondary summaries.
- Extraction fallbacks lacked a reusable way to retain PDF page locations. Add one
  optional, local-only helper; do not build a retrieval service or require a renderer.
- Copying only the skill folder omitted the license. Bundle the repository license.
- `git merge --ff-only` can succeed with unrelated local changes, contradicting the
  installer's promise to skip edited clones. Check the working tree before fetching.

Version 0.2.0 fills these gaps while retaining the six-step reading workflow, four modes,
and standard output structure. It is an additive minor release under this repository's
versioning rules. Development edits do not update the stable installation until release.

The largest remaining gap is evidence of effectiveness: the original three seed prompts
did not constitute a benchmark, and there were no committed paper-specific keys or
recorded outputs. The added regression prompts and one source-checked smoke reading
improve coverage, but do not establish superiority over a generic prompt or validate
every contribution type. A held-out, controlled comparison remains the next substantial
evaluation task. See `evals/README.md` and the audit sources in `docs/sources.md`.
