# Lec16 Summary: Regression

## Core idea
Lecture 16 introduces **regression** as a way to model relationships between variables and make predictions, using the classic father-son height example from Francis Galton.

## Key concepts
- **Correlation (`rho`)** measures how two variables move together using standardized values.
- `rho` ranges from `-1` to `1`:
  - positive: variables tend to increase together
  - negative: one tends to decrease when the other increases
  - near zero: weak/no linear relationship
- Correlation is useful but incomplete; different-shaped datasets can share similar correlation values.
- Always inspect relationships visually (e.g., scatter plots), and consider alternatives like **Spearman rank correlation** when appropriate.

## Regression line
- Linear regression predicts `Y` from `X` with:
  - `y = b + mx`
  - slope `m = rho * (sigma_y / sigma_x)`
  - intercept `b = mu_y - m * mu_x`
- In standardized units, the regression slope equals `rho`.
- Regression to the mean: predictions are pulled toward the average unless correlation is perfect.
- Regression is directional:
  - predicting son from father is not the same as predicting father from son.

## Prediction and variance
- Compared with stratified averaging, the regression line gives more stable predictions in small samples.
- A fuller model includes residual error:
  - `y = b + mx + epsilon`
- The explained proportion of variance is `rho^2`:
  - with `rho ≈ 0.5`, father height explains about `25%` of son-height variation.

## Causation warnings
Lecture emphasis: **association is not causation**.

Main pitfalls:
- **Spurious correlation / data dredging**: high correlations can appear by chance when searching many variable pairs.
- **Outliers**: one extreme point can create a misleadingly strong correlation.
- **Reverse causality**: cause/effect direction can be incorrectly flipped.
- **Confounding**: a third variable affects both `X` and `Y`, creating misleading associations.

## Confounders and Simpson's paradox
- UC Berkeley admissions example: aggregate data suggested gender bias, but stratifying by major changed conclusions.
- This illustrates **Simpson's paradox**: overall trend can reverse within subgroups.
- Proper stratification/conditioning is essential before interpretation.

## Toward causal conclusions
- **Randomized Controlled Trials (RCTs)** are the gold standard for causal claims because randomization balances confounders.
- Observational studies can mislead (example: hormone replacement therapy and cardiovascular risk), while later RCTs revealed opposite effects.
- Other causal strategies mentioned: twins studies, difference-in-differences, propensity score matching, and graphical models.

## Takeaways
- Use correlation and regression for **association and prediction**, not automatic causal claims.
- Check plots, outliers, subgroup structure, and possible confounders before interpreting results.
- Prefer randomized or robust causal-inference designs when the goal is causation.
