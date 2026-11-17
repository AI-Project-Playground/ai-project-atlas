# AI Context — K-Means & Gaussian Mixture Models

## Project identity
- **Project:** P0 — Track G: Unsupervised Learning
- **Topic:** K-Means & Gaussian Mixture Models (GMM)
- **Type:** Hands-on unsupervised-learning comparison lab
- **Status:** Implemented and deployed; learning experiments can be extended.
- **Language:** Python
- **Recommended environment:** Python 3.11
- **Modes:** Local CLI, local Streamlit, hosted Streamlit Community Cloud
- **Goal:** Cluster the same synthetic 2-D dataset with K-Means and GMM, compare hard versus soft assignments, and study how to select the number of clusters.

## Project links
- **Run experience:** https://ai-daily-practice-k-means-gmm.streamlit.app/
- **GitHub source:** https://github.com/atanuduttagupta/ai-daily-practice/tree/main/ML/k-means-gmm
- **Repository:** https://github.com/atanuduttagupta/ai-daily-practice
- **Project directory:** `ML/k-means-gmm/`

## Learning objectives
1. Understand clustering as an unsupervised-learning task.
2. Learn the K-Means assignment/update loop and its inertia objective.
3. Understand K-Means assumptions, strengths and limitations.
4. Understand GMM components, means, covariance matrices and mixture weights.
5. Explain the Expectation-Maximization (E-step and M-step) algorithm.
6. Compare hard assignments from K-Means with soft membership probabilities from GMM.
7. Explore GMM covariance types: `full`, `tied`, `diag`, and `spherical`.
8. Compare inertia, silhouette score, Adjusted Rand Index (ARI), and GMM BIC when evaluating clustering.
9. Understand why cluster-count selection criteria can disagree.
10. Connect K-Means to vector quantization and IVF-style vector-search indexes.

## Implemented experiment
- Synthetic data generated with `sklearn.datasets.make_blobs`.
- 600 samples, 3 centres, `cluster_std=[1.6, 3.2, 1.0]`, `random_state=42`.
- A 2×2 linear transform stretches/rotates the data into elliptical-looking groups.
- K-Means: `KMeans(n_clusters=3, n_init=10, random_state=42)`.
- GMM: `GaussianMixture(n_components=3, covariance_type="full", n_init=5, random_state=42)`.
- GMM `predict_proba()` exposes soft component membership probabilities.
- Candidate k values 2 through 6 are compared using K-Means inertia, K-Means silhouette, and GMM BIC.
- `clusters.png` displays true generated groups, K-Means assignments, and GMM assignments.

## Technical stack
- Python
- scikit-learn: `KMeans`, `GaussianMixture`, `make_blobs`, `adjusted_rand_score`, `silhouette_score`
- NumPy
- Matplotlib
- Streamlit (interactive UI)
- pandas (tables)

## Dataset and metrics
The project uses synthetic data with known generated labels. Those labels are used only to calculate ARI after clustering; they are not supplied to either clustering algorithm.

- **Inertia:** within-cluster sum of squared distances for K-Means; lower always results as k increases, so look for an elbow rather than simply minimizing it.
- **Silhouette:** internal measure of cohesion/separation, range -1 to 1; does not require true labels and tends to favour compact, well-separated clusters.
- **ARI:** external measure comparing predicted clusters with generated true labels, adjusted for chance.
- **BIC:** GMM model-selection criterion balancing likelihood and complexity; lower is preferred among comparable candidate models.

### Documented example results
| Model | Adjusted Rand Index | Silhouette |
|---|---:|---:|
| K-Means | 0.718 | 0.614 |
| GMM | 0.942 | 0.612 |

Other documented observations:
- 14 of 600 points had maximum GMM membership probability below 0.9.
- GMM BIC was lowest at k=3, matching the number of generated groups.
- Silhouette scored k=2 highest (0.659 vs 0.614 at k=3).
- These are observations from one deliberately designed synthetic experiment, not universal benchmarks.

## Streamlit experience
The Streamlit application provides:
1. Controls for seed, sample count, generated groups, fitted cluster count, GMM covariance type, group spreads and elliptical stretching.
2. K-Means and GMM metric comparison.
3. Side-by-side true groups, K-Means and GMM plots.
4. Inspection of observations with the least certain GMM membership probabilities.
5. Candidate-k table with inertia, silhouette and GMM BIC.
6. Expandable theory and interview reminders.

## Run instructions
Run from `ML/k-means-gmm/`.

### Windows PowerShell
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### CLI
```powershell
python main.py
```

### Streamlit
```powershell
python -m streamlit run app.py
```

## Dependencies
```text
scikit-learn>=1.3.0
matplotlib>=3.7.0
numpy>=1.26.0
streamlit>=1.40
pandas>=2.0
```

## Design boundaries and cautions
- The dataset is synthetic and deliberately configured with overlap, different spreads and stretching to illustrate a case where GMM can outperform K-Means.
- Results from this one seed and synthetic dataset should not be generalized to real data.
- ARI requires reference labels, which may not be available in true unsupervised-learning use cases.
- Silhouette and ARI measure different properties and can disagree.
- Inertia always decreases or stays the same as k grows.
- AIC/BIC are used for GMM candidate comparison; lower is better among comparable models.
- The project uses scikit-learn APIs rather than implementing K-Means or EM from scratch.

## Potential next learning steps
These are extensions, not claims about implemented features:
1. Change cluster spreads and transformation to test when K-Means catches up.
2. Compare GMM covariance types (`full`, `tied`, `diag`, `spherical`).
3. Apply `StandardScaler` and examine the effect of feature scaling.
4. Cluster the scikit-learn digits dataset with k=10 and compare ARI.
5. Try `MiniBatchKMeans` for larger datasets.
6. Explore clustering embeddings for near-duplicate detection or vector-search indexing.

## Guidance for future AI assistants
- Continue from the existing project; do not replace it with an unrelated architecture.
- Keep the topic focused on K-Means, GMM, clustering evaluation and cluster-count selection.
- Distinguish documented experiment results from universal claims.
- Prefer scikit-learn APIs; this project is not a from-scratch algorithm implementation.
- Give Windows PowerShell commands for local setup.
- Treat the supplied Streamlit URL as the public run experience and the GitHub directory as source documentation.
