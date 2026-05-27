"""
Python for AI & ML Engineers
Module 2: NumPy — The Engine of AI
github.com/Here2ServeU/scripting

A digital image is a NumPy array.
A training dataset is a NumPy array.
A neural network layer is one line: output = X @ W + b
"""

import numpy as np
import time

# ── SPEED COMPARISON ─────────────────────────────────────────────────────────

size    = 1_000_000
py_list = list(range(size))
np_arr  = np.arange(size)

start  = time.time()
_      = [x * 2 for x in py_list]
list_t = time.time() - start

start  = time.time()
_      = np_arr * 2
numpy_t = time.time() - start

print(f"List:  {list_t:.4f}s")
print(f"NumPy: {numpy_t:.4f}s")
print(f"NumPy is ~{list_t / numpy_t:.0f}x faster\n")

# ── CREATING ARRAYS ───────────────────────────────────────────────────────────

weights = np.zeros((3, 4))            # 3 inputs, 4 neurons — all zeros
biases  = np.ones(4)                  # 4 bias values — all ones
rand_w  = np.random.randn(3, 4)       # random initialisation (normal distribution)
seq_arr = np.arange(0, 1.0, 0.1)     # [0.0, 0.1, 0.2, ..., 0.9]
lin_arr = np.linspace(0, 1, 11)      # 11 equally spaced values from 0 to 1

print(f"weights shape: {weights.shape}")   # (3, 4)
print(f"biases shape:  {biases.shape}")    # (4,)
print(f"rand_w:\n{rand_w.round(3)}\n")

# ── BROADCASTING ─────────────────────────────────────────────────────────────
# NumPy can do math between arrays of different shapes — no loops required.

data      = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]], dtype=float)

# Zero-centre by subtracting column means (a common preprocessing step)
col_means = data.mean(axis=0)          # mean of each column — shape (3,)
centred   = data - col_means           # broadcasting: (3,3) - (3,) = (3,3)

print("Column means:", col_means)
print("Centred:\n",   centred.round(2), "\n")

# Scale a row vector across all rows (also broadcasting)
weights_row = np.array([0.5, 1.0, 2.0])
scaled      = data * weights_row
print("Scaled:\n", scaled, "\n")

# ── THE MOST IMPORTANT LINE IN DEEP LEARNING ─────────────────────────────────

print("=" * 45)
print("  output = X @ W + b")
print("  That is a neural network layer.")
print("=" * 45, "\n")

X      = np.random.randn(5, 3)    # 5 samples, 3 features
W      = np.random.randn(3, 4)    # 3 inputs → 4 neurons
b      = np.zeros(4)              # 4 bias values
output = X @ W + b

print(f"X shape:      {X.shape}")       # (5, 3)
print(f"W shape:      {W.shape}")       # (3, 4)
print(f"b shape:      {b.shape}")       # (4,)
print(f"output shape: {output.shape}")  # (5, 4)
print()

# ── INDEXING AND SLICING ──────────────────────────────────────────────────────

arr = np.arange(20).reshape(4, 5)
print("Array:\n", arr)
print("Row 0:        ", arr[0])
print("Column 2:     ", arr[:, 2])
print("Top-left 2x2:\n", arr[:2, :2])
print("Every other row:\n", arr[::2])
print()

# ── RESHAPING FOR DEEP LEARNING ───────────────────────────────────────────────

flat  = np.random.randint(0, 255, 784)    # 28×28 = 784 pixels (flattened)
img   = flat.reshape(28, 28)              # grayscale image
batch = flat.reshape(1, 28, 28, 1)        # single image batch for a CNN

print(f"Flat:  {flat.shape}")    # (784,)
print(f"Image: {img.shape}")     # (28, 28)
print(f"Batch: {batch.shape}")   # (1, 28, 28, 1)

# Normalise pixel values from 0-255 to 0.0-1.0
normalised = img.astype(np.float32) / 255.0
print(f"\nPixel range (raw):        {img.min()}-{img.max()}")
print(f"Pixel range (normalised): {normalised.min():.2f}-{normalised.max():.2f}")

# ── USEFUL AGGREGATIONS ───────────────────────────────────────────────────────

scores = np.array([0.94, 0.61, 0.88, 0.45, 0.92])
print(f"\nScores:  {scores}")
print(f"Mean:    {scores.mean():.4f}")
print(f"Std:     {scores.std():.4f}")
print(f"Max:     {scores.max():.4f}  at index {scores.argmax()}")
print(f"Above 0.85: {scores[scores > 0.85]}")
