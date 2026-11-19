# AI Context — Telecom Customer Churn Prediction with Bagging & Ensembling

## Project identity
- **Project:** Bagging & Ensembling — Predicting Telecom Customer Churn
- **Type:** Practical machine-learning case study
- **Learning focus:** Ensemble learning for binary classification and customer-risk ranking
- **GitHub:** https://github.com/atanuduttagupta/ai-daily-practice/tree/main/ML/ensembling-customer-churn
- **Interactive Streamlit app:** https://ai-daily-practice-ensembling-customer-churn.streamlit.app/

## Business problem
A telecom company loses customers through churn and can contact only a limited number of customers with retention offers. The goal is to rank customers by their likelihood of churning so the retention team can contact the highest-risk group first, and to test whether combining models identifies churners more effectively than individual models.

## Dataset
- IBM Telco Customer Churn dataset.
- 7,043 customer records.
- Public CSV downloaded from the IBM GitHub-hosted dataset and cached locally as `telco-churn.csv`.
- Internet access is required for the first download.
- `TotalCharges` is converted to numeric; blank or invalid values become missing values.
- `Churn` is converted to a binary target (`Yes` = 1, otherwise 0).
- `customerID` is removed from model features.

## Technology stack
- Python
- scikit-learn
- pandas
- NumPy
- Streamlit

## Data preparation and evaluation design
- Stratified train/test split: 80% training and 20% test data.
- Random seed: 42.
- Numeric features: median imputation followed by standardization.
- Categorical features: most-frequent imputation followed by one-hot encoding.
- Preprocessing is inside scikit-learn Pipelines, so preprocessing is learned from each training fold rather than from validation/test observations.
- Cross-validation uses `StratifiedKFold` with 5 folds and shuffling, applied to the training set only.
- The held-out test set is evaluated once after fitting on the complete training split.

## Models compared
The case study compares seven model approaches:

1. **Single Decision Tree:** one tree-based classifier. It can fit complex patterns but may overfit and have high variance.
2. **Logistic Regression:** a simple classification baseline.
3. **Bagged Trees (100):** an ensemble of decision trees trained on bootstrap samples; predictions are combined.
4. **Random Forest:** bagged decision trees with random feature subsets at each split.
5. **Gradient Boosting:** sequential boosting using scikit-learn's `HistGradientBoostingClassifier`.
6. **Voting (LR + RF + GB):** soft-voting ensemble that combines predicted probabilities from logistic regression, random forest, and gradient boosting.
7. **Stacking (LR + RF + GB):** combines base-model predictions using a final logistic regression estimator.

## Ensemble-learning concepts
### Bagging
Bagging means Bootstrap Aggregating. Multiple copies of a model are trained on bootstrap samples drawn with replacement, then their predictions are averaged or voted. It mainly reduces variance. Averaging unstable trees makes the overall model less sensitive to changes in the training sample.

### Random Forest
Random Forest is a bagging-based tree ensemble. In addition to bootstrap sampling, it considers a random subset of features at each split so trees become less alike.

### Boosting
Boosting builds models sequentially. Later models focus on patterns or errors that earlier models did not model well. Gradient boosting often performs strongly on tabular data and mainly targets bias reduction.

### Voting
Soft voting averages predicted class probabilities from multiple models.

### Stacking
Stacking trains a final estimator to learn how to combine predictions from different base models.

### Out-of-bag (OOB) score
A bootstrap sample leaves out some training rows. Each tree can be evaluated against rows it did not see during its own training. Aggregating these predictions gives an OOB estimate without requiring a separate validation set.

## Evaluation metrics
- **ROC-AUC:** probability that a randomly selected churner receives a higher risk score than a randomly selected non-churner. A value of 0.5 represents random ranking; 1.0 represents perfect ranking.
- **Top-20% capture:** share of all actual churners found among the 20% of customers ranked as highest risk. A random ranking would find about 20% of churners when contacting 20% of customers.
- **OOB accuracy:** out-of-bag accuracy reported for the bagging model.

The top-fraction capture metric reflects the operational constraint that the retention team can call only a limited group of customers.

## Reference results from the README
One documented run reports:

| Model | CV AUC (±std) | Train AUC | Test AUC | Top-20% capture |
|---|---:|---:|---:|---:|
| Stacking (LR+RF+GB) | 0.848 ± 0.010 | 0.917 | 0.844 | 50% |
| Voting (LR+RF+GB) | 0.848 ± 0.009 | 0.936 | 0.843 | 50% |
| Logistic regression | 0.846 ± 0.013 | 0.849 | 0.842 | 50% |
| Random forest | 0.841 ± 0.009 | 0.962 | 0.837 | 49% |
| Gradient boosting | 0.838 ± 0.007 | 0.951 | 0.835 | 49% |
| Bagged trees (100) | 0.821 ± 0.008 | 1.000 | 0.812 | 46% |
| Single decision tree | 0.658 ± 0.012 | 1.000 | 0.657 | 35% |

Additional documented observations:
- Bagging improved the single-tree test AUC from 0.657 to 0.812, illustrating variance reduction.
- Logistic regression (test AUC 0.842) was close to stacking (0.844); the top four models' differences were smaller than the approximate CV spread, so the results do not establish a clear winner among them.
- Contacting the 20% highest-risk customers found about 50% of churners for the top models, around 2.5 times the 20% expected from random selection.
- Bagging out-of-bag accuracy was 0.784.

These metrics describe one dataset and one train/test split. They can change with different random seeds, splits, and library versions. ROC-AUC and capture rates alone do not establish whether a retention campaign is profitable.

## Main implementation workflow
1. Load the IBM Telco CSV; cache it locally as `telco-churn.csv`.
2. Convert `TotalCharges` to numeric and convert `Churn` to a binary target.
3. Remove `customerID` from model inputs.
4. Create a stratified train/test split.
5. Build numeric and categorical preprocessing transformations.
6. Wrap preprocessing and each classifier in a scikit-learn Pipeline.
7. Run stratified 5-fold cross-validation on the training split using ROC-AUC.
8. Fit each pipeline on the full training split and evaluate on train and test sets.
9. Calculate top-20% capture using predicted churn probabilities.
10. Fit a separate bagged-tree pipeline with `oob_score=True` and report its OOB accuracy.

## Interactive Streamlit app
The interactive app provides:
- Dataset overview, churn rate, class distribution, and sample records.
- Controls for random seed, test-set fraction, number of stratified CV folds, retention-team contact capacity, bagging tree count, and random-forest tree count.
- Training and comparison of the seven model approaches.
- CV AUC, CV standard deviation, train AUC, test AUC, and top-fraction capture scorecard.
- Out-of-bag accuracy for bagged trees.
- Test AUC comparison chart.
- Customer risk ranking with predicted churn probabilities and contact priority.
- CSV download of the test-set customer risk ranking.
- ROC curve and confusion matrix for a selected model.
- Learning tabs for Bagging, Boosting, Voting & Stacking, metrics, and further experiments.

## Suggested experiments
1. Change bagging `n_estimators` to 10, 50, 100, 300 and observe where improvements flatten.
2. Add `max_features="sqrt"` to bagged trees and compare with Random Forest.
3. Try `class_weight="balanced"` and observe how top-fraction capture changes.
4. Remove `StandardScaler` and compare model performance.
5. Add LightGBM or XGBoost as extra models.
6. Add campaign economics: call cost, retention-offer cost, customer value, and likelihood that an offer actually prevents churn.

## Limitations and interpretation
- Results are from one public dataset and one stratified split; results may shift with other seeds and library versions.
- The top-20% capture metric is a ranking measure, not a complete business-profit calculation.
- The analysis does not model the causal effect of a retention offer; high churn probability does not guarantee that a customer can be persuaded to stay.
- Ensemble models can cost more to train and run and can be harder to explain.
- Ensembles may add little if models make similar mistakes or a simple model is already stable and well suited.

## Run locally
Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the original script:

```bash
python main.py
```

Run the interactive app:

```bash
python -m streamlit run app.py
```

The first run needs internet access to download the public dataset. The app and script cache the data locally.

## Project links
- GitHub source: https://github.com/atanuduttagupta/ai-daily-practice/tree/main/ML/ensembling-customer-churn
- Streamlit demo: https://ai-daily-practice-ensembling-customer-churn.streamlit.app/
