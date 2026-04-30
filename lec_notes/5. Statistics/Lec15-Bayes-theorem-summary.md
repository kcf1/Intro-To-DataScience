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

- `P(Disease | Positive) ≈ 0.024` (about 2.4%)

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
