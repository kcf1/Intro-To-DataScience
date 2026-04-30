# Lec13-17 Summaries

---

# Lec13 Summary: Probability

## What this lecture covers
- Probability and random numbers
- Discrete probability
- Independence and conditional probability
- Continuous probability, expected value, and variance
- Law of Large Numbers (LLN) and Central Limit Theorem (CLT)
- Bank loan risk case study
- Markov vs Nekrasov debate

## 1) Probability and randomness
- Probability quantifies uncertainty and can be interpreted as long-run frequency or degree of belief.
- Monte Carlo simulation estimates unknown quantities via repeated random sampling (example: estimating pi).
- In practice, computers use pseudo-random number generators (PRNGs): same seed gives reproducible sequences.
- True randomness usually comes from physical processes (thermal noise, quantum effects), but is throughput-limited.

## 2) Discrete probability basics
- Sample space `Omega`: all possible outcomes; event `A`: subset of outcomes.
- Core properties include:
  - `P(Omega) = 1`
  - `P(A) >= 0`
  - `P(not A) = 1 - P(A)`
  - `P(A union B) <= P(A) + P(B)`
  - `P(A and B) <= min(P(A), P(B))`
- Card and bead examples are used to build intuition on counting outcomes.

## 3) Independence and conditional probability
- Two events are independent if one does not change the probability of the other.
- Conditional probability:
  - `P(A|B) = P(A and B) / P(B)`
- Independence equivalences:
  - `P(A and B) = P(A)P(B)`
  - `P(A|B) = P(A)`
- The lecture highlights common mistakes (e.g., gambler's fallacy, assuming big samples are always unbiased).

## 4) Combinations, permutations, and simulation
- Use permutations when order matters; combinations when order does not.
- Poker/blackjack examples show exact probability computation and conditional reasoning.
- Monte Carlo is useful when exact counting is difficult, but experiment size and assumptions still matter.

## 5) Continuous probability
- For continuous random variables, exact-point probability is zero (`P(X = x) = 0`).
- Probability is assigned to intervals (e.g., `P(a <= X <= b)`).
- eCDF/CDF represent cumulative probability behavior; PDF describes density.
- Normal distribution is introduced with R tooling (`pnorm`, `rnorm`), plus note that many other distributions exist.

## 6) Expected value and variance
- Expected value `E(X)` is the long-run average outcome.
- Variance and standard deviation measure spread/risk.
- For i.i.d. samples:
  - Mean of sample mean equals population mean.
  - Variance of sample mean decreases with `n` (standard error scales like `1/sqrt(n)`).
- LLN: sample averages converge to expected value as sample size grows.

## 7) Central Limit Theorem (CLT)
- For many distributions with finite mean/variance, sample mean is approximately normal for large `n`.
- CLT explains why averages often look "normal" even if raw data is not.
- Requires assumptions (especially i.i.d.) in the standard form taught here.

## 8) Case study: bank loans
- Each loan return is modeled as a random variable under default/no-default outcomes.
- Monte Carlo shows distribution of average return across many loans.
- Key insights:
  - Raising interest rate can shift expected return positive.
  - To reduce loss probability, either increase margin or portfolio size (`n`) to reduce standard error.
  - Results are very sensitive to assumptions (default rate, independence, macro conditions).
- Important realism checks: correlated defaults, recessions, feedback loops (higher rates can raise default risk), and hidden systemic risk.

## 9) Markov vs Nekrasov debate
- Nekrasov argued independence is necessary for LLN/CLT behavior.
- Markov gave counterexamples with dependent observations and developed ideas leading to Markov chains.
- Big takeaway: dependence structures matter; useful probabilistic behavior can still emerge without full independence.
- Modern relevance: Markov chains, Monte Carlo, PageRank, HMMs, MDPs, and language modeling.

## Final takeaway
The lecture connects probability theory to data science practice: model uncertainty, simulate when exact math is hard, check assumptions behind LLN/CLT, and stress-test real-world decisions (like lending) against dependence and changing environments.

---

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
  - About 68% CI: estimate +/- 1 SE
  - About 95% CI: estimate +/- 1.96 SE (often approximated as +/- 2 SE)
  - About 99.7% CI: estimate +/- 3 SE
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

---

# Lec15 Summary: Bayes' Theorem

## Core idea

Bayes' theorem updates the probability of a hypothesis after seeing evidence:

\[
P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}
\]

- `P(A)` is the prior probability (belief before seeing data).
- `P(B|A)` is the likelihood (how likely evidence is if the hypothesis is true).
- `P(B)` is the evidence (overall chance of observing the data).
- `P(A|B)` is the posterior probability (updated belief after seeing data).

## Intuition from Lego example

The lecture uses colored Lego pegs to explain conditional probability:

- Total pegs: 192
- White pegs: 64, so `P(white) = 64/192 = 0.33`
- Blue pegs: 128, so `P(blue) = 128/192 = 0.67`
- Black pegs: 8 total, but these are distributed across white/blue regions

Key point: probabilities must be conditioned on context.

- `P(black|blue) = 2/128 = 0.015625`
- `P(black|white) = 6/64 = 0.09375`
- `P(blue|black) = 2/8 = 0.25`

Using Bayes:

- `P(black|white) = P(white|black) * P(black) / P(white)`
- `P(white|black) = P(black|white) * P(white) / P(black)`

This shows how to move between "probability of reality given observation" and
"probability of observation given reality."

## Why Bayes matters

Bayes' theorem is powerful when intuition fails in complex settings. Applications mentioned:

- Email spam detection
- Disease risk assessment from test results
- Driverless car decision making
- Voice recognition
- Text autocompletion
- Finance and machine learning more broadly

## COVID test example (base-rate effect)

Even with a 99% accurate test, if disease prevalence is very low (1 in 4,000),
the probability of truly having disease after a positive test can still be low.

In the lecture's calculation:

- `P(Disease | Positive) ~= 0.024` (about 2.4%)

Takeaway: high test accuracy does not automatically imply a high posterior
probability when the condition is rare. Prevalence (base rate) strongly affects
the posterior.

## Monte Carlo simulation insight

A simulation with 100,000 people illustrates why:

- There are far more healthy individuals than diseased individuals.
- Even a small false positive rate can create many false positives.
- Among all positive tests, many are false positives when prevalence is low.

Repeated simulation converges to the analytical Bayes result (~0.024).

## Practical interpretation reminders

- Bayesian thinking combines prior reality with new observations.
- Different people can reach different posteriors if priors differ.
- Good data interpretation requires distinguishing:
  - `P(reality | observation)` from
  - `P(observation | reality)`

## Suggested further reading from lecture

- *Introduction to Data Science* materials (Bayes chapters/background)
- *Everything is Predictable* (Bayesian statistics introduction)
- Additional online Bayes intuition resources linked in class slides

---

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
  - with `rho ~= 0.5`, father height explains about `25%` of son-height variation.

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

---

# Lec17 Summary - Introduction to Machine Learning

## Main topics
- Machine learning notation and problem setup
- Evaluation metrics and why accuracy alone can mislead
- Decision boundaries and model flexibility
- Practical workflows using `caret` in R
- Common model families and tool choices in practice

## 1) Core notation and learning goals
- `X` = observed input features (e.g., image pixels, text, lab values).
- `Y` = target outcome (class label or continuous value).
- `P(Y|X)` is **discriminative modeling** (predict label from features), used in classification/regression tasks.
- `P(X|Y)` is **generative modeling** (model data distribution conditioned on class).
- `P(X)` is unconditional modeling (e.g., language modeling, anomaly detection).
- If `Y` is categorical: classification (binary if 2 classes).  
  If `Y` is continuous: regression.

## 2) Evaluation: what "good model" means
- Data must be split into **training set** and **test set**.
- Test data must not be used for model selection/tuning.
- Accuracy is intuitive but can be deceptive under class imbalance.

### Confusion-matrix-based metrics
- **Sensitivity / Recall / TPR** = `TP / (TP + FN)`  
  (How many actual positives are found?)
- **Specificity / TNR** = `TN / (TN + FP)`  
  (How many actual negatives are correctly rejected?)
- **Precision / PPV** = `TP / (TP + FP)`  
  (How many predicted positives are truly positive?)
- **Accuracy** = `(TP + TN) / (P + N)`
- **F1-score** = harmonic mean of precision and recall; useful for balancing both.

### Thresholding and ROC
- Different classification cutoffs change sensitivity/specificity trade-offs.
- ROC curve plots `TPR` vs `FPR = 1 - specificity`.
- **AUC** summarizes ranking/classification quality across all thresholds.

### Loss functions
- For continuous outcomes, use loss functions such as **MSE**.
- For binary classification with hard 0/1 predictions, MSE relates closely to `1 - accuracy`.
- For multi-class classification, softmax + classification losses are commonly used.

## 3) Decision boundary intuition (MNIST 2 vs 7 case study)
- Even simple engineered features can separate classes somewhat.
- Linear regression creates a **linear/planar boundary**, which may underfit nonlinear patterns.
- When true class structure is nonlinear, need more flexible models (e.g., kNN, trees, kernels, neural nets).

## 4) Practical modeling workflow (R `caret`)
- `train()` gives a common interface for many algorithms.
- `predict()` applies trained models consistently.
- Built-in cross-validation supports hyperparameter tuning (e.g., choosing `k` in kNN).
- Compare models on held-out test data, not only training/CV performance.

## 5) Preprocessing and compute-aware practice
- Remove near-zero-variance features and standardize/transform as needed.
- Feature filtering can shrink dimensionality significantly (example: many MNIST pixels are uninformative).
- Run small pilot experiments first to estimate runtime before full-scale training.

## 6) What to use in practice
- Supervised model families mentioned:
  - Linear/logistic models (+ regularization: lasso, ridge, elastic net)
  - Tree-based models (random forest, gradient boosting/XGBoost)
  - SVM
  - kNN
  - Neural networks
- Broader paradigms: unsupervised, semi-supervised, self-supervised, weakly supervised, meta-learning, reinforcement learning.
- Common ecosystems:
  - Python: `scikit-learn`, `xgboost`, `pytorch`/`tensorflow`/`keras`, `transformers`
  - R: `caret`, `torch` (and Python interop when needed)

## Takeaway
The lecture emphasizes that ML is not just fitting models: it is defining the right objective, using unbiased evaluation (beyond raw accuracy), understanding boundary/representation limits, and selecting practical tools and workflows that balance performance with compute constraints.
