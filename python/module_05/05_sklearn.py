"""
T2S: Python for AI & ML Engineers
Module 5: Scikit-learn — Classical ML
github.com/Here2ServeU/scripting

Every Scikit-learn model follows the same 4 steps:
  1. Create   — instantiate the model
  2. Fit      — train on training data
  3. Predict  — run on new data
  4. Evaluate — measure accuracy

The Pipeline object chains preprocessing + model into one object.
This prevents data leakage and makes deployment clean.
"""

import numpy  as np
import joblib

from sklearn.datasets        import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing   import StandardScaler
from sklearn.linear_model    import LogisticRegression
from sklearn.ensemble        import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics         import classification_report, confusion_matrix
from sklearn.pipeline        import Pipeline
from sklearn.impute          import SimpleImputer

np.random.seed(42)

# ── 1. DATA ────────────────────────────────────────────────────────────────────

X, y = make_classification(
    n_samples     = 1000,
    n_features    = 10,
    n_informative = 6,
    n_redundant   = 2,
    random_state  = 42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {X_train.shape}  Test: {X_test.shape}")

# ── 2. DATA LEAKAGE — THE MOST IMPORTANT RULE ─────────────────────────────────
# Fit the scaler ONLY on training data.
# If you fit on test data, you leak future information into training.
# Your model will look better than it actually is. In production, it fails.

scaler     = StandardScaler()
X_train_s  = scaler.fit_transform(X_train)   # fit AND transform training data
X_test_s   = scaler.transform(X_test)        # ONLY transform test data — never fit

# ── 3. TRAIN AND COMPARE ──────────────────────────────────────────────────────

print("\n--- Model Comparison ---")

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest':       RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting':   GradientBoostingClassifier(n_estimators=100, random_state=42),
}

for name, model in models.items():
    model.fit(X_train_s, y_train)
    acc = model.score(X_test_s, y_test)
    print(f"  {name:<25} {acc:.4f}")

# ── 4. CROSS-VALIDATION — THE HONEST EVALUATION ───────────────────────────────
# One train-test split is a guess.
# Cross-validation splits your data 5 different ways and averages the scores.
# The mean ± std is the REAL score.

print("\n--- Cross-Validation (5-fold) ---")
rf     = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(rf, X_train_s, y_train, cv=5, scoring='accuracy')
print(f"  Scores: {scores.round(4)}")
print(f"  Mean:   {scores.mean():.4f} ± {scores.std():.4f}")

# ── 5. PIPELINE — THE PRODUCTION WAY ─────────────────────────────────────────
# A Pipeline chains preprocessing + model in one object.
# Benefits:
#   - No data leakage (everything fits on train only, automatically)
#   - One file to save and deploy
#   - Clean code

print("\n--- Production Pipeline ---")

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),   # handle missing values
    ('scaler',  StandardScaler()),                    # scale features
    ('model',   RandomForestClassifier(n_estimators=100, random_state=42)),
])

pipeline.fit(X_train, y_train)

cv_mean = cross_val_score(pipeline, X_train, y_train, cv=5).mean()
acc     = pipeline.score(X_test, y_test)
y_pred  = pipeline.predict(X_test)

print(f"  CV mean:    {cv_mean:.4f}")
print(f"  Test acc:   {acc:.4f}")

print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred, digits=4))

print("--- Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
print(f"  TN={cm[0,0]}  FP={cm[0,1]}")
print(f"  FN={cm[1,0]}  TP={cm[1,1]}")

# ── 6. SAVE ────────────────────────────────────────────────────────────────────

joblib.dump(pipeline, 'model_pipeline.pkl')
print("\nPipeline saved to model_pipeline.pkl")
print("Load with: pipeline = joblib.load('model_pipeline.pkl')")

# ── 7. FEATURE IMPORTANCE ─────────────────────────────────────────────────────

rf_model     = pipeline.named_steps['model']
importances  = rf_model.feature_importances_
feature_names = [f'feature_{i}' for i in range(X.shape[1])]

print("\n--- Feature Importances ---")
for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1])[:5]:
    bar = '█' * int(imp * 100)
    print(f"  {name:<12} {imp:.4f}  {bar}")
