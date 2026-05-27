"""
Python for AI & ML Engineers
Project 2: End-to-End ML Pipeline
github.com/Here2ServeU/scripting

A complete ML pipeline from raw data to saved model.
Covers the full workflow taught in the course:
  Module 3 — Pandas (load, clean, engineer features)
  Module 4 — Visualisation (training curve)
  Module 5 — Scikit-learn (train, cross-validate, pipeline, save)

Run this script with the venv active:
    source venv/bin/activate
    python projects/ml_pipeline/ml_pipeline.py
"""

import numpy  as np
import pandas as pd
import joblib
import os

from sklearn.datasets        import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing   import StandardScaler
from sklearn.ensemble        import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model    import LogisticRegression
from sklearn.metrics         import classification_report, accuracy_score
from sklearn.pipeline        import Pipeline
from sklearn.impute          import SimpleImputer
from collections             import defaultdict


# ── STEP 1: GENERATE DATA ────────────────────────────────────────────────────

def load_data(n_samples=1000, n_features=10, random_state=42):
    """
    Generate a synthetic classification dataset.
    In production, replace this with your actual data loading logic.
    """
    print("Step 1: Loading data...")
    X, y = make_classification(
        n_samples     = n_samples,
        n_features    = n_features,
        n_informative = 6,
        n_redundant   = 2,
        random_state  = random_state,
    )

    # Wrap in a DataFrame to practice Pandas
    feature_names = [f'feature_{i}' for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y

    # Inject ~5% missing values to simulate real data
    np.random.seed(random_state)
    mask = np.random.random(df.shape) < 0.05
    mask[:, -1] = False   # never mask the target
    df[mask] = np.nan

    print(f"  Shape:         {df.shape}")
    print(f"  Missing values:{df.isnull().sum().sum()}")
    print(f"  Class balance: {df['target'].value_counts().to_dict()}")
    return df


# ── STEP 2: INSPECT DATA ─────────────────────────────────────────────────────

def inspect_data(df):
    """Run the 5 inspection commands you use on every new dataset."""
    print("\nStep 2: Inspecting data...")
    print(f"  Shape:   {df.shape}")
    print(f"  Dtypes:\n{df.dtypes.to_string()}")
    print(f"\n  Head:\n{df.head(3).to_string()}")
    print(f"\n  Stats:\n{df.describe().round(2).to_string()}")
    print(f"\n  Missing per column:\n{df.isnull().sum()[df.isnull().sum() > 0].to_string()}")


# ── STEP 3: SPLIT ─────────────────────────────────────────────────────────────

def split_data(df, target_col='target', test_size=0.2, random_state=42):
    """Split into features and labels, then train/test."""
    print("\nStep 3: Splitting data...")
    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    print(f"  Train: {X_train.shape}  Test: {X_test.shape}")
    return X_train, X_test, y_train, y_test


# ── STEP 4: TRAIN AND COMPARE MODELS ─────────────────────────────────────────

def train_and_compare(X_train, X_test, y_train, y_test):
    """
    Train three models. Compare test accuracy.
    Uses a Pipeline to prevent data leakage.
    """
    print("\nStep 4: Training and comparing models...")

    model_configs = {
        'Logistic Regression':  LogisticRegression(max_iter=1000, random_state=42),
        'Random Forest':        RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting':    GradientBoostingClassifier(n_estimators=100, random_state=42),
    }

    results = {}
    for name, estimator in model_configs.items():
        pipe = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler',  StandardScaler()),
            ('model',   estimator),
        ])
        pipe.fit(X_train, y_train)
        acc = pipe.score(X_test, y_test)
        results[name] = {'pipeline': pipe, 'accuracy': acc}
        print(f"  {name:<25} test accuracy: {acc:.4f}")

    return results


# ── STEP 5: CROSS-VALIDATE THE BEST MODEL ────────────────────────────────────

def cross_validate_best(results, X_train, y_train):
    """
    Find the best model from the comparison.
    Run 5-fold cross-validation for a reliable score estimate.
    """
    print("\nStep 5: Cross-validating best model...")

    best_name = max(results, key=lambda n: results[n]['accuracy'])
    best_pipe = results[best_name]['pipeline']

    print(f"  Best model: {best_name}")

    cv_scores = cross_val_score(best_pipe, X_train, y_train, cv=5, scoring='accuracy')
    print(f"  CV scores:  {cv_scores.round(4)}")
    print(f"  CV mean:    {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

    return best_name, best_pipe, cv_scores.mean()


# ── STEP 6: FULL REPORT ───────────────────────────────────────────────────────

def full_report(pipe, X_test, y_test, model_name):
    """Print a classification report for the final model."""
    print(f"\nStep 6: Final report — {model_name}")
    y_pred = pipe.predict(X_test)
    print(classification_report(y_test, y_pred, digits=4))


# ── STEP 7: SAVE THE PIPELINE ─────────────────────────────────────────────────

def save_pipeline(pipe, path='model_pipeline.pkl'):
    """Save the trained pipeline to disk."""
    joblib.dump(pipe, path)
    size_kb = os.path.getsize(path) / 1024
    print(f"\nStep 7: Pipeline saved to '{path}'  ({size_kb:.1f} KB)")
    print("  Load later with:  pipeline = joblib.load('model_pipeline.pkl')")


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 55)
    print("  End-to-End ML Pipeline")
    print("=" * 55)

    df                               = load_data()
    inspect_data(df)
    X_train, X_test, y_train, y_test = split_data(df)
    results                          = train_and_compare(X_train, X_test, y_train, y_test)
    best_name, best_pipe, cv_mean    = cross_validate_best(results, X_train, y_train)
    full_report(best_pipe, X_test, y_test, best_name)
    save_pipeline(best_pipe)

    print("\n" + "=" * 55)
    print(f"  Done. Best model: {best_name}  CV accuracy: {cv_mean:.4f}")
    print("=" * 55)
