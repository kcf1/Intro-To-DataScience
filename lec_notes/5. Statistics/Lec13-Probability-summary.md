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
