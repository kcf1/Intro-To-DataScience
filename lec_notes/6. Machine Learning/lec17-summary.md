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
