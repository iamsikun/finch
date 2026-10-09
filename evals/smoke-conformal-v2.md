# Manual smoke reading, October 9, 2026

Case 2 in `evals.json`, using Finch's revised core and formal guide. The key was
prepared first in `keys/conformal-v2.md`. This is a same-agent source check, not a blind
evaluation or a measured improvement over version 0.1.0.

## Source and access

Read [arXiv:1904.06019v2](https://arxiv.org/pdf/1904.06019v2), April 25, 2019.
This PDF lists Barber, Candès, Ramdas, and Tibshirani in that order. The source hash is
in the key. The helper extracted 17 pages, matching `pdfinfo`; PDF and printed page
numbers coincide here. Rendered pages 4, 12, and 13 were inspected for the equations
and proof. Text extraction alone scrambled math and included chart glyphs as text,
despite no page being flagged sparse: the warning heuristic does not certify quality.
The arXiv record was consulted; a separate journal-notice search was not performed.

## Reading produced

Theorem 2 (p. 13) replaces ordinary exchangeability with **weighted exchangeability**
and gives finite-sample marginal coverage of at least $1-\alpha$. Corollary 1 (p. 4)
specializes this to covariate shift. Training observations are IID; the test observation
is independent; $Y\mid X$ is unchanged; and the test covariate distribution is absolutely
continuous with respect to the training distribution (model (6), p. 3).

Write $w=d\widetilde P_X/dP_X$. Equation (7) assigns each training score weight
$p_i=w(X_i)/(\sum_j w(X_j)+w(x))$ and the candidate test point weight
$p_{n+1}=w(x)/(\sum_j w(X_j)+w(x))$. Equation (8) compares the candidate score with
the $1-\alpha$ quantile of $\sum_i p_i\delta_{V_i}+p_{n+1}\delta_\infty$.
Here $V_i$ is the symmetric nonconformity score computed for candidate $(x,y)$,
$\delta_a$ puts unit mass at $a$, and large scores mean poorer conformity.

Why the weighting works: conditional on the unordered observations, the test point's
identity is no longer uniform. The joint density's symmetric factor cancels across
permutations, yielding the assignment probabilities in equation (15) (Lemma 3,
pp. 12–13). In the covariate-shift case, there are $n!$ permutations per candidate;
cancelling that factor yields normalized likelihood ratios (§3.5, p. 14). Thus the
weighted quantile uses the correct conditional distribution of the test score.
Replacing its unknown score by infinity gives the conservative comparison used for
prediction; marginalizing establishes the bound.

The result averages over calibration/training data and the test point. It does not
guarantee coverage at every fixed $X=x$, exact equality to the target, or narrow sets.
A common positive scale factor in $w$ cancels (Remark 3). Arbitrary estimated weights
do not inherit the oracle guarantee: the illustration in §2.3 and discussion on p. 14
provide empirical support for particular estimates, not that theorem.

I checked the symmetric-factor cancellation, covariate-shift normalization, and
Theorem 2's reduction to Lemma 3. I took the authors' extension from distinct scores
to ties and the formal conditioning details on trust; this is not a complete proof
audit. A useful transfer boundary is support: when test covariates enter a region
absent from training, absolute continuity fails and Corollary 1 no longer applies.

## Verification observations

- The answer retains the theorem/corollary distinction, the distributional assumptions,
  marginal coverage, and the infinity atom. No literature neighborhood was added to
  this focused technical question.
- Visual inspection confirmed an apparent typo in Remark 5 (p. 13): it prints
  normalized probabilities as 1 in the unweighted case. Equation (15) instead gives
  $1/(n+1)$. The reading uses the defining equation; it does not silently propagate
  the remark's value or treat this typo as invalidating the theorem.
- No experiment or cited repository was executed. The empirical figure results were
  not independently reproduced. This run covers one formal-methodology example;
  synthetic regressions and other contribution types still need model evaluation.
