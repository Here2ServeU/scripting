"""
T2S: Python for AI & ML Engineers
Module 4: Data Visualisation
github.com/Here2ServeU/scripting

Rule: Never train a model on data you have not visualised.
Patterns invisible in a table are obvious in a chart.
"""

import matplotlib.pyplot as plt
import numpy             as np

np.random.seed(42)

ages    = np.random.randint(22, 65, 200)
incomes = ages * 900 + np.random.normal(0, 8000, 200)
labels  = (incomes > np.median(incomes)).astype(int)
colors  = ['#e74c3c' if l == 0 else '#27ae60' for l in labels]

# ── PLOT 1: HISTOGRAM — FEATURE DISTRIBUTION ─────────────────────────────────

plt.figure(figsize=(7, 4))
plt.hist(ages, bins=20, color='steelblue', edgecolor='white')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('plot1_histogram.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved plot1_histogram.png")

# ── PLOT 2: SCATTER — CLASS SEPARATION ───────────────────────────────────────
# If the two colours are completely mixed — your features can't separate the classes.

plt.figure(figsize=(7, 4))
plt.scatter(ages, incomes, c=colors, alpha=0.5, s=18)
plt.title('Age vs Income — coloured by class')
plt.xlabel('Age')
plt.ylabel('Income')
plt.tight_layout()
plt.savefig('plot2_scatter.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved plot2_scatter.png")

# ── PLOT 3: TRAINING CURVE ────────────────────────────────────────────────────
# Screenshot this. You will see this exact pattern in your own models.
#
# Both lines fall together    → learning and generalising  ✅
# Training falls, val rises   → overfitting                ⚠️
# Large gap from the start    → underfitting               ❌

epochs     = range(1, 51)
train_loss = [1.0 * 0.92 ** e + np.random.uniform(0, 0.02) for e in epochs]
val_loss   = [1.0 * 0.94 ** e + np.random.uniform(0, 0.05) for e in epochs]

plt.figure(figsize=(8, 4))
plt.plot(epochs, train_loss, label='Train Loss',      color='#2980b9', lw=2)
plt.plot(epochs, val_loss,   label='Validation Loss', color='#e67e22', lw=2)
plt.axvline(x=30, color='red', linestyle='--', alpha=0.4, label='Early stop')
plt.legend()
plt.title('Training Curves')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.tight_layout()
plt.savefig('plot3_training_curve.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved plot3_training_curve.png")

# ── PLOT 4: DASHBOARD — ALL IN ONE ───────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(16, 4))

axes[0].hist(ages, bins=20, color='steelblue', edgecolor='white')
axes[0].set_title('Age Distribution')
axes[0].set_xlabel('Age')

axes[1].scatter(ages, incomes, c=colors, alpha=0.5, s=18)
axes[1].set_title('Age vs Income by Class')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Income')

axes[2].plot(epochs, train_loss, label='Train', color='#2980b9', lw=2)
axes[2].plot(epochs, val_loss,   label='Val',   color='#e67e22', lw=2)
axes[2].legend()
axes[2].set_title('Training Curves')
axes[2].set_xlabel('Epoch')
axes[2].set_ylabel('Loss')

plt.tight_layout()
plt.savefig('ml_dashboard.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved ml_dashboard.png")

# ── PLOT 5: BOX PLOT — OUTLIER DETECTION ──────────────────────────────────────

plt.figure(figsize=(6, 4))
plt.boxplot(incomes, vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue'))
plt.title('Income Distribution — Box Plot')
plt.ylabel('Income')
plt.tight_layout()
plt.savefig('plot5_boxplot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved plot5_boxplot.png")

print("\nAll 5 plots saved. The ML dashboard is ml_dashboard.png.")
