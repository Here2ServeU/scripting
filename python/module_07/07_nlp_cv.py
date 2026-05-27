"""
Python for AI & ML Engineers
Module 7: NLP & Computer Vision
github.com/Here2ServeU/scripting

NLP:  Text → numbers → model → prediction
CV:   Image → NumPy array → model → prediction

Both fields use the same fundamental insight:
everything is eventually a number.
"""

import re
import numpy as np

# ══════════════════════════════════════════════════════════════
# PART A — NATURAL LANGUAGE PROCESSING
# ══════════════════════════════════════════════════════════════

# ── STEP 1: TOKENISATION ────────────────────────────────────────────────────

def tokenize(text):
    """
    Clean and split text into tokens.
    Lowercases, removes punctuation, splits on whitespace.
    """
    return re.sub(r'[^a-z0-9 ]', '', text.lower()).split()


corpus = [
    'Machine learning is a subset of artificial intelligence',
    'Deep learning uses neural networks for AI',
    'Python is the top language for machine learning',
]

print("=== NLP: Tokenisation ===")
for doc in corpus:
    print(f"  {tokenize(doc)}")

# ── STEP 2: TF-IDF + LOGISTIC REGRESSION ───────────────────────────────────
# TF-IDF weights words by how specific they are to a document.
# Common words like 'the' get low scores.
# Rare, specific words like 'transformer' get high scores.

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model            import LogisticRegression
    from sklearn.model_selection         import train_test_split
    from sklearn.metrics                 import accuracy_score

    reviews = [
        'great product love it',
        'terrible quality waste of money',
        'amazing value highly recommend',
        'worst purchase ever made',
        'fantastic item works perfectly',
        'absolutely horrible broke immediately',
        'excellent quality fast delivery',
        'disappointing does not work at all',
    ]
    sentiments = [1, 0, 1, 0, 1, 0, 1, 0]   # 1 = positive, 0 = negative

    vec = TfidfVectorizer()
    X   = vec.fit_transform(reviews)

    clf  = LogisticRegression(random_state=42).fit(X, sentiments)

    test_phrases = ['fantastic item', 'terrible product', 'great quality']
    X_test       = vec.transform(test_phrases)
    predictions  = clf.predict(X_test)
    probas       = clf.predict_proba(X_test)

    print("\n=== NLP: TF-IDF + Logistic Regression ===")
    for phrase, pred, prob in zip(test_phrases, predictions, probas):
        label = 'POSITIVE' if pred == 1 else 'NEGATIVE'
        conf  = prob[pred]
        print(f"  '{phrase}'  →  {label}  ({conf:.2f})")

except ImportError:
    print("scikit-learn not installed: pip install scikit-learn")

# ── STEP 3: WORD EMBEDDINGS CONCEPT ────────────────────────────────────────
# In a trained embedding space:
#   king - man + woman ≈ queen
#
# This works because words with similar meanings sit close together
# geometrically in the high-dimensional vector space.
# This is the mathematical core of every LLM, including GPT and Claude.

print("\n=== NLP: Word Embeddings (conceptual demo) ===")

# Simulate a tiny embedding space (in reality these are 768+ dimensions)
embeddings = {
    'king':   np.array([0.9, 0.1, 0.8, 0.2]),
    'queen':  np.array([0.9, 0.9, 0.8, 0.2]),
    'man':    np.array([0.1, 0.1, 0.8, 0.2]),
    'woman':  np.array([0.1, 0.9, 0.8, 0.2]),
    'prince': np.array([0.8, 0.1, 0.6, 0.3]),
}

result = embeddings['king'] - embeddings['man'] + embeddings['woman']

# Find the closest word to our result
best_word = min(
    (w for w in embeddings if w != 'king'),
    key=lambda w: np.linalg.norm(embeddings[w] - result)
)
print(f"  king - man + woman ≈ {best_word}")   # queen

# ── STEP 4: HUGGINGFACE PIPELINE ───────────────────────────────────────────

print("\n=== NLP: HuggingFace Sentiment Analysis ===")
try:
    from transformers import pipeline as hf_pipeline

    sentiment = hf_pipeline('sentiment-analysis')
    sentences = [
        'Python is an amazing language for building AI!',
        'This dataset is full of missing values and problems.',
        'The model accuracy is deeply disappointing.',
    ]
    results = sentiment(sentences)
    for sentence, r in zip(sentences, results):
        print(f"  {r['label']:<10} {r['score']:.3f}  |  {sentence[:50]}")

except ImportError:
    print("  transformers not installed: pip install transformers")
    print("  (Showing expected output instead)")
    print("  POSITIVE   0.999  |  Python is an amazing language for building AI!")
    print("  NEGATIVE   0.872  |  This dataset is full of missing values...")
    print("  NEGATIVE   0.995  |  The model accuracy is deeply disappointing.")


# ══════════════════════════════════════════════════════════════
# PART B — COMPUTER VISION
# ══════════════════════════════════════════════════════════════

print("\n=== CV: An Image is a NumPy Array ===")

# A colour image is a 3D array: (height, width, channels)
# Channels: [Red, Green, Blue]  — each value 0-255

image = np.random.randint(0, 256, (28, 28, 3), dtype=np.uint8)
print(f"  Image shape:   {image.shape}")          # (28, 28, 3)
print(f"  Pixel [0,0]:   {image[0, 0]}")           # [R, G, B] values
print(f"  Red channel:\n  {image[:3, :3, 0]}")     # top-left 3x3 of red

# Normalise: scale pixel values from [0, 255] to [0.0, 1.0]
# Neural networks learn much better with small numbers close to 0.
normalised = image.astype(np.float32) / 255.0
print(f"\n  Raw range:        {image.min()} to {image.max()}")
print(f"  Normalised range: {normalised.min():.2f} to {normalised.max():.2f}")

# Reshape for a CNN: add batch dimension → (batch, height, width, channels)
batch = normalised[np.newaxis, ...]    # same as reshape(1, 28, 28, 3)
print(f"\n  Single image:   {normalised.shape}")   # (28, 28, 3)
print(f"  Batched:        {batch.shape}")           # (1, 28, 28, 3)

# Batch of 32 images (as a model would receive during training)
batch_32 = np.random.rand(32, 28, 28, 3).astype(np.float32)
print(f"  Batch of 32:    {batch_32.shape}")        # (32, 28, 28, 3)

print("\n=== CV: What a CNN Learns ===")
print("  Layer 1 → Edges (horizontal, vertical, diagonal)")
print("  Layer 2 → Shapes (corners, curves, circles)")
print("  Layer 3 → Parts  (eyes, wheels, letters)")
print("  Layer 4 → Objects (faces, cars, words)")
print()
print("  Starting from: an image is a NumPy array.")
print("  Everything else is: output = X @ W + b, stacked and repeated.")
