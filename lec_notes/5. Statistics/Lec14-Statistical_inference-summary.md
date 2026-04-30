# Lec14 Summary: Statistical Inference

## What this lecture is about
- Statistical inference helps distinguish real signal from random chance.
- Polling is used as the motivating example: estimate population opinion from a sample.
- Main topics: standard deviation vs standard error, confidence intervals, power, and p-values.

## Polling as a sampling model
- Let `p` be the proportion supporting one side (e.g., blue beads/candidate A).
- Opposing proportion is `1 - p`.
- Spread is `p - (1 - p) = 2p - 1`.
- Different polls give different estimates because of sampling variability.
- Larger sample sizes produce tighter estimate distributions (less uncertainty).

## Standard deviation vs standard error
- **Standard deviation (SD):** spread of observations within one dataset.
- **Standard error (SE):** spread of a statistic (usually the sample mean/proportion) across repeated samples.
- For a sample mean: `SE = s / sqrt(N)`.
- For a proportion: `SE = sqrt(p(1-p)/N)`.
- As `N` increases, SE decreases roughly at rate `1/sqrt(N)`.

## Confidence intervals (CI) and margin of error (MoE)
- A confidence interval gives a range of plausible values for the true parameter under repeated sampling.
- Under normal approximation:
  - About 68% CI: estimate ± 1 SE
  - About 95% CI: estimate ± 1.96 SE (often approximated as ± 2 SE)
  - About 99.7% CI: estimate ± 3 SE
- In polling, margin of error is typically tied to a 95% CI and often approximated by `~2 x SE`.
- Narrower CI means more precise estimates.

## Power
- **Power** is the probability of detecting a real non-zero effect (e.g., spread not equal to 0).
- Low sample size can produce CIs that include 0 even when a real difference exists.
- This can create "toss-up" conclusions due to insufficient data, not necessarily because reality is close.
- Increasing sample size increases power by reducing SE.

## p-values and hypothesis testing
- Set a null hypothesis (e.g., `p = 0.5`, no difference).
- Compute a test statistic (z-score) measuring distance from null in SE units.
- **p-value:** probability of observing a result at least as extreme as the data, assuming the null is true.
- Typical conventions:
  - `p <= 0.05`: statistically unlikely under null
  - `p <= 0.01`: very unlikely under null

## Chi-square example (categorical comparison)
- For two-way categorical outcomes (e.g., success/failure by gender), use a chi-square test.
- It compares observed counts to expected counts under "no association".
- Output is a p-value for whether differences are likely due to chance.

## Important cautions
- Small p-values do not imply large practical effects.
- With very large samples, tiny effects can become statistically significant.
- Always interpret p-values together with effect size and domain relevance.
- Large datasets can still mislead when systematic bias/confounding exists.

## Bottom line
- Inference quantifies uncertainty, not certainty.
- SE and CI quantify precision; power quantifies detectability; p-values quantify compatibility with null assumptions.
- Good data science practice combines statistical significance, effect size, study design quality, and bias checks.
