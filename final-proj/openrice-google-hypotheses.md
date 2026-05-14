# Hypotheses and quantifiable evidence: OpenRice vs. Google

**Context:** Social media sometimes claims OpenRice reviews are biased (e.g., overly positive, filtered negatives, or promotion-driven). Comparing the **same venues** on **OpenRice** and **Google Maps / Google Reviews** turns that narrative into testable claims.

---

## 1. Research questions (from the idea)

1. For matched restaurants, are **average ratings** and **review sentiment** higher on OpenRice than on Google?
2. Are differences **stable across segments** (cuisine, price band, chain vs. independent, district) or concentrated in subsets that align with ad/promotion exposure?
3. Do **behavioral signals** (timing, text duplication, reviewer history) differ between platforms in ways consistent with manipulation or moderation, beyond what brand demographics explain?

---

## 2. Hypotheses

Use matched venues \(i = 1,\ldots,n\) with OpenRice rating \(R^{OR}_i\) and Google rating \(R^{G}_i\) (map both to a common scale if needed, e.g. 0–5).

| ID | Hypothesis | Plain language |
|----|------------|----------------|
| **H1** | \(E[R^{OR}_i - R^{G}_i] > 0\) | OpenRice is systematically more favorable than Google for the same restaurants. |
| **H2** | After controlling for observable venue traits (cuisine, price, chain, location), the OpenRice–Google gap remains positive. | The gap is not fully explained by “different kinds of restaurants” on each platform. |
| **H3** | Venues with stronger OpenRice commercial exposure (e.g., featured listings, coupons, “award” badges—operationalize from page metadata) show a **larger** OpenRice–Google gap than similar venues without those signals. | Bias (or selection) correlates with monetization-related visibility on OpenRice. |
| **H4** | OpenRice shows more **burstiness** (clusters of reviews in short windows) or **text reuse** than Google for the same venue, holding review volume roughly constant. | Platform-specific patterns resemble coordinated or templated reviews more on one side. |
| **H5 (null-oriented)** | Any rating gap is explained by **sampling** (different time windows, different review counts, survivorship of closed venues) and **scale interpretation** (users calibrate stars differently). | There is no systematic favorability on OpenRice once measurement is tightened. |

**H1–H4** support the social-media “biased / rosier OpenRice” story if the data agree; **H5** is the skeptical benchmark your methods should try to falsify.

---

## 3. Quantifiable evidence (what to measure)

### 3.1 Matching and outcomes

| Evidence | Definition / operationalization | Why it matters |
|----------|----------------------------------|----------------|
| **Matched sample** | Same legal entity or same address + name similarity threshold; manual spot-check on a random subset | Avoids comparing different restaurants |
| **Primary outcome** | \(\Delta_i = R^{OR}_i - R^{G}_i\) (or logit of positive rate if using binary sentiment) | Direct “same place, two platforms” contrast |
| **Robustness** | \(\Delta_i\) using only reviews in overlapping date ranges on both platforms | Reduces “Google only got bad reviews last year” confounding |
| **Distribution** | Histogram / QQ of \(\Delta_i\); fraction with \(\Delta_i \geq +0.3\) stars | Shows whether the effect is tail-driven |

### 3.2 Statistical tests (examples)

- **Paired test:** one-sample \(t\)-test or Wilcoxon signed-rank on \(\Delta_i\) vs. 0 (report effect size: mean \(\Delta\), Cohen’s \(d\), or Cliff’s delta).
- **Regression:** \(\Delta_i = \beta_0 + \beta_1 X_i + \epsilon_i\) where \(X_i\) includes cuisine, price, chain, district FE; cluster SEs by district or brand if needed.
- **H3:** interaction of OpenRice commercial flags with platform fixed effects in a stacked model, or stratified comparison of mean \(\Delta\) in flag vs. no-flag groups.

### 3.3 Text and temporal signals (for H4)

| Signal | Quantifiable metric |
|--------|---------------------|
| **Sentiment** | Mean sentiment score per venue per platform (dictionary or embedding model); difference in means |
| **Burstiness** | Reviews per day; max rolling 7-day count; Gini of inter-review times; compare OR vs. G for same venue |
| **Duplication** | Share of reviews with high n-gram overlap to other reviews on same platform; duplicate near-posts across accounts |
| **Genericness** | Length, unique token rate, template phrases (“環境不錯”, “值得一試”) frequency vs. platform baseline |

### 3.4 “Social media claim” as auxiliary evidence (optional)

| Evidence | How to quantify |
|----------|-----------------|
| **Volume of concern** | Count posts / comments mentioning “OpenRice” + bias keywords over a window (API or manual sample); time series vs. news events |
| **Triangulation** | Correlation (ecological) between districts or cuisines with high \(\Delta\) and higher social-media complaint rate—weak but descriptive |

---

## 4. Success criteria (what would convince you)

1. **Direction + magnitude:** Mean \(\Delta\) positive with CI excluding zero on a large matched sample.
2. **Robustness:** Survives overlapping time windows, alternative matching rules, and controls for venue type.
3. **Plausibility for mechanism:** Either H3-style monetization correlation or H4-style behavioral anomalies—or a clear measurement story (H5) that explains the gap without “bias.”

---

## 5. Main threats to validity (brief)

- **Different user bases** and star calibration (not bias).
- **Moderation / removal** on either platform (unobserved truncation).
- **Selection:** restaurants with strong OpenRice presence differ from those that are “Google-first.”
- **Scraping bias:** incomplete history on one platform shrinks \(n\) toward easy-to-scrape venues.

Document these in the final write-up and, where possible, bound them with sensitivity analyses (e.g., restrict to venues with \(\geq 20\) reviews on **both** platforms).
