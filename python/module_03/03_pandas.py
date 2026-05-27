"""
T2S: Python for AI & ML Engineers
Module 3: Pandas — Data Wrangling
github.com/Here2ServeU/scripting

70-80% of ML work is data work — not building models.
Pandas is your primary tool for loading, cleaning, and transforming data.
"""

import pandas as pd
import numpy  as np

np.random.seed(42)

# ── CREATE A REALISTIC DATASET ────────────────────────────────────────────────

df = pd.DataFrame({
    'age':       np.random.randint(18, 65, 200),
    'income':    np.random.normal(50000, 20000, 200).round(2),
    'education': np.random.choice(['high_school', 'bachelors', 'masters', 'phd'], 200),
    'score':     np.random.uniform(0.3, 1.0, 200).round(3),
    'purchased': np.random.randint(0, 2, 200),
})

# Inject missing values — like a real dataset
df.loc[df.sample(frac=0.05).index, 'income'] = np.nan

# ── THE 5 INSPECTION COMMANDS ─────────────────────────────────────────────────
# Run these on EVERY new dataset, every time, without exception.

print("1. Shape (rows, columns):")
print(df.shape)

print("\n2. Data types per column:")
print(df.dtypes)

print("\n3. First 3 rows:")
print(df.head(3).to_string())

print("\n4. Descriptive statistics:")
print(df.describe().round(2).to_string())

print("\n5. Missing values per column:")
print(df.isnull().sum())

# ── HANDLE MISSING VALUES ─────────────────────────────────────────────────────
# Rule: use median for numerical columns, not mean.
# One billionaire in your dataset destroys the mean. The median stays stable.

print(f"\nMissing before: {df.isnull().sum().sum()}")
df['income'] = df['income'].fillna(df['income'].median())
print(f"Missing after:  {df.isnull().sum().sum()}")

# ── REMOVE OUTLIERS (IQR METHOD) ──────────────────────────────────────────────
# Remove values that fall outside 1.5 × the interquartile range.
# This is the standard approach in data science.

Q1  = df['income'].quantile(0.25)
Q3  = df['income'].quantile(0.75)
IQR = Q3 - Q1

before_rows = len(df)
df = df[(df['income'] >= Q1 - 1.5 * IQR) & (df['income'] <= Q3 + 1.5 * IQR)]
print(f"\nRows before outlier removal: {before_rows}")
print(f"Rows after:                  {len(df)}")

# ── FEATURE ENGINEERING ───────────────────────────────────────────────────────
# Create new columns that give your model better information.
# This step often matters more than which algorithm you choose.

df['income_per_age'] = (df['income'] / df['age']).round(2)

df['high_earner'] = (df['income'] > df['income'].median()).astype(int)

edu_map = {'high_school': 0, 'bachelors': 1, 'masters': 2, 'phd': 3}
df['edu_level'] = df['education'].map(edu_map)

print(f"\nEngineered features:")
print(df[['income_per_age', 'high_earner', 'edu_level']].head())
print(f"\nFinal shape: {df.shape}")

# ── USEFUL PANDAS OPERATIONS ──────────────────────────────────────────────────

# Filter rows
high_scorers = df[df['score'] >= 0.85]
print(f"\nHigh scorers (>= 0.85): {len(high_scorers)}")

# Group and aggregate
avg_by_edu = df.groupby('education')['score'].mean().sort_values(ascending=False)
print("\nAverage score by education:")
print(avg_by_edu.round(3).to_string())

# Value counts
print("\nEducation distribution:")
print(df['education'].value_counts().to_string())

# Correlation (useful before training)
print("\nCorrelation with 'purchased':")
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.corr()['purchased'].sort_values(ascending=False).to_string())
