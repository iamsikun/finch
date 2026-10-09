# Sources and attribution

## Reading protocols

- S. Keshav, "How to Read a Paper" (2007, revised 2016).
  https://svr-sk818-web.cl.cam.ac.uk/keshav/papers/07/paper-reading.pdf
  - Three passes: (1) the five Cs, namely category, context, correctness,
    contributions, clarity; (2) careful reading of content and evidence;
    (3) virtual re-implementation.
  - Also gives a procedure for surveying a literature from a few seed papers.
  - Basis for Finch's reading modes. This is experienced advice, not experimental
    evidence.
- Carey, Steiner & Petri, "Ten Simple Rules for Reading a Scientific Paper,"
  *PLOS Computational Biology* (2020).
  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008032
  - Read with a purpose, distinguish article types, examine figures and methods, and
    separate results from interpretation.
- Brendan Price, "Reading Papers: Some Tips" (2019).
  https://sangmino.github.io/Documents/r30.pdf
- Sangmin Oh, "Reading Papers Critically" (updated 2024).
  https://sangmino.github.io/Documents/reading_papers.pdf
  - These two are economics and finance guidance: the question, the conceptual basis,
    the empirical strategy, assumptions, quantitative importance, and position relative
    to prior work.

## Comprehension and learning

- W. Kintsch, "The Role of Knowledge in Discourse Comprehension: A
  Construction–Integration Model," *Psychological Review* 95 (1988).
  https://doi.org/10.1037/0033-295X.95.2.163
  - Distinguishes a textbase from a situation model. Finch applies this as faithful
    vs. explanatory reconstruction, which is an engineering analogy.
- Chi, de Leeuw, Chiu & LaVancher, "Eliciting Self-Explanations Improves
  Understanding," *Cognitive Science* 18 (1994).
  https://doi.org/10.1207/s15516709cog1803_3

## Scientific argument and attribution

- Teufel & Moens, "Summarizing Scientific Articles: Experiments with Relevance and
  Rhetorical Status," *Computational Linguistics* 28(4) (2002).
  https://aclanthology.org/J02-4002/
  - Rhetorical status (own work, background, other work, basis, contrast) is the
    basis for Finch's intellectual-status labels.

## Grounded scientific QA and generation

- Dasigi et al., QASPER, NAACL 2021. https://aclanthology.org/2021.naacl-main.365/
- Wadden et al., SciFact, EMNLP 2020. https://aclanthology.org/2020.emnlp-main.609/
- Gao et al., ALCE, EMNLP 2023. https://aclanthology.org/2023.emnlp-main.398/
- Slobodkin et al., "Attribute First, then Generate," ACL 2024.
  https://aclanthology.org/2024.acl-long.182/
- Liu et al., "Lost in the Middle," TACL 2024. https://aclanthology.org/2024.tacl-1.9/

## Literature synthesis

- Asai et al., "Synthesizing Scientific Literature with Retrieval-Augmented Language
  Models" (OpenScholar), *Nature* (2026).
  https://www.nature.com/articles/s41586-025-10072-4
  - Its benchmark has no social-science instances.

## Skill engineering

- Li et al., "SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks,"
  arXiv:2602.12670 (2026). https://arxiv.org/abs/2602.12670
  - Curated skills improved the average pass rate, but the effect varied by task and
    was sometimes negative.
  - Focused skills with at most three modules beat exhaustive bundles in their setting.
- Agent Skills specification. https://agentskills.io/specification
- Anthropic `skill-creator` (Apache-2.0).
  https://github.com/anthropics/skills/tree/main/skills/skill-creator
  - Process for writing skills, and the `evals/evals.json` layout.

## Adapted ideas from existing skills

Finch's text is original. The ideas below were adapted, with credit:

| Skill | License (as checked, Oct 2026) | Idea adapted |
|---|---|---|
| [drbzw/theory-paper-reader-skill](https://github.com/drbzw/theory-paper-reader-skill) | MIT (LICENSE file) | Provenance distinctions (paper-explicit / model-inferred / background / not specified); location pointers; flagging failed text extraction; the "empirical translation" of theory |
| [ZhimingMei/finance-paper-reader-skill](https://github.com/ZhimingMei/finance-paper-reader-skill) | README says MIT, but there is no LICENSE file; only ideas were used | Routing by empirical, theory, or mixed contribution; skipping sections that don't apply; concerns phrased as questions; a single key takeaway |
| [RayChen200318/stats-econometrics-paper-reader](https://github.com/RayChen200318/stats-econometrics-paper-reader) | No license found; only ideas were used | Estimand vs. estimator; inference choices (SE, clustering, fixed effects) treated as substantive; co-reading with pauses |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (`literature-review`, `scientific-critical-thinking`) | MIT | Keeping "not reported" apart from "not done"; concerns given as location → observation → consequence; no checklist scores; citation counts used for reading order, not inclusion; a DOI resolving does not show that the source supports the claim |

## Possible future backends

- FutureHouse PaperQA (Apache-2.0). https://github.com/Future-House/paper-qa
- OpenScholar (Apache-2.0). https://github.com/AkariAsai/OpenScholar
