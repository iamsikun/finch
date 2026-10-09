# Smoke key: Conformal Prediction Under Covariate Shift

Prepared from the source before writing the recorded smoke answer.

- Source: https://arxiv.org/pdf/1904.06019v2 (April 25, 2019), 17 pages.
- Authors in this PDF's order: Rina Foygel Barber, Emmanuel J. Candès, Aaditya Ramdas,
  Ryan J. Tibshirani. Use this version's numbering, not another version's metadata.
- SHA-256: `c471ff1dd7370a5c1e1f2e16d2bd720898bc772c835c2f984a019ded4375068f`.
- Route: formal/statistical methodology, focused deep technical reading (case 2).

## Required content and anchors

| Claim | Source | Conditions to retain |
|---|---|---|
| General finite-sample marginal coverage at least 1−α | Theorem 2, p. 13 | Weighted exchangeability with the specified weight functions; symmetric score construction |
| Covariate-shift specialization | Model (6), p. 3; Corollary 1, p. 4 | IID training, independent test, identical Y given X, test covariates absolutely continuous with respect to training covariates |
| Normalized weights and infinity atom | Equations (7)–(8), p. 4; Remark 3 | True test/train density ratio, up to a positive common scale |
| Proof mechanism | Definition 1, Lemma 3, pp. 12–13; §3.5, p. 14 | Conditional assignment probabilities from permutations; symmetric factor cancels |
| Estimated weights | §2.3, p. 8; discussion, p. 14 | Empirical illustration does not supply a distribution-free oracle guarantee for arbitrary estimates |

## Severe misreadings

- Claiming coverage at each fixed test covariate, or exact equality to the target.
- Allowing arbitrary concept shift or unseen support while retaining the same guarantee.
- Omitting the candidate test point's mass, or treating any estimated ratio as exact.
- Claiming a complete proof audit when ties or measure-theoretic details were trusted.

## Transfer check

If test covariates place positive mass outside training support, Corollary 1's absolute
continuity assumption fails. Explain why importance weighting cannot supply information
about outcomes in a region absent from the training distribution; do not promise that
the corollary still applies.
