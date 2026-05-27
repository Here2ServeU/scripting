"""
T2S: Python for AI & ML Engineers
Module 6: Deep Learning Foundations
github.com/Here2ServeU/scripting

A neural network is matrix multiplication, repeated,
with non-linear functions placed in between.

We build one from scratch with NumPy first.
Then Keras does the same thing in 4 lines.
"""

import numpy as np

# ── PART A: NEURAL NETWORK FROM SCRATCH ──────────────────────────────────────
# No libraries. Pure NumPy. So you understand what Keras is doing.

class NeuralNetwork:
    """
    A fully-connected feed-forward neural network.
    Supports ReLU hidden layers and sigmoid output.
    Trained with gradient descent (backpropagation).
    """

    def __init__(self, layer_sizes, lr=0.01):
        """
        Args:
            layer_sizes: list of ints, e.g. [2, 8, 1]
                         input size → hidden units → output size
            lr: learning rate
        """
        self.lr = lr
        # Initialize weights with small random values (Xavier-ish)
        self.W  = [np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * 0.1
                   for i in range(len(layer_sizes) - 1)]
        self.b  = [np.zeros((1, layer_sizes[i + 1]))
                   for i in range(len(layer_sizes) - 1)]

    # ── ACTIVATIONS ──────────────────────────────────────────────────────────

    def _relu(self, x):
        return np.maximum(0, x)

    def _relu_grad(self, x):
        return (x > 0).astype(float)

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    # ── FORWARD PASS ─────────────────────────────────────────────────────────

    def forward(self, X):
        """Compute output for every sample in X."""
        self.activations = [X]    # store activations for backprop
        self.z_values    = []     # store pre-activation values

        for i, (W, b) in enumerate(zip(self.W, self.b)):
            z = self.activations[-1] @ W + b
            self.z_values.append(z)

            # Last layer → sigmoid (binary output)
            # Hidden layers → ReLU
            a = self._sigmoid(z) if i == len(self.W) - 1 else self._relu(z)
            self.activations.append(a)

        return self.activations[-1]

    # ── BACKWARD PASS (BACKPROPAGATION) ──────────────────────────────────────

    def backward(self, y):
        """Compute gradients and update weights."""
        m      = y.shape[0]
        # Gradient of binary cross-entropy loss w.r.t. sigmoid output
        delta  = self.activations[-1] - y.reshape(-1, 1)

        for i in reversed(range(len(self.W))):
            dW = self.activations[i].T @ delta / m
            db = delta.mean(axis=0, keepdims=True)

            if i > 0:
                # Propagate gradient through ReLU
                delta = (delta @ self.W[i].T) * self._relu_grad(self.z_values[i - 1])

            # Gradient descent update
            self.W[i] -= self.lr * dW
            self.b[i] -= self.lr * db

    # ── LOSS ─────────────────────────────────────────────────────────────────

    def _loss(self, y_true, y_pred):
        """Binary cross-entropy loss."""
        eps = 1e-8
        return -np.mean(
            y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps)
        )

    # ── TRAIN ─────────────────────────────────────────────────────────────────

    def train(self, X, y, epochs=300, verbose=True):
        history = []
        for epoch in range(epochs):
            y_pred = self.forward(X)
            loss   = self._loss(y, y_pred.flatten())
            self.backward(y)
            history.append(loss)

            if verbose and epoch % 50 == 0:
                acc = ((y_pred.flatten() > 0.5) == y).mean()
                print(f"  Epoch {epoch:3d} | Loss {loss:.4f} | Acc {acc:.4f}")
        return history

    def predict(self, X):
        return (self.forward(X).flatten() > 0.5).astype(int)


# ── DEMO: LEARN XOR ──────────────────────────────────────────────────────────
# XOR cannot be solved by a single line (linear model).
# It requires a hidden layer — this is the classic proof that depth matters.

print("=" * 45)
print("  Neural Network from Scratch — XOR")
print("=" * 45)

X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y_xor = np.array([0, 1, 1, 0])

nn = NeuralNetwork([2, 8, 1], lr=0.5)
nn.train(X_xor, y_xor, epochs=301)

preds = nn.predict(X_xor)
print(f"\nFinal predictions: {preds}")
print(f"Expected:          {y_xor}")
print(f"Correct:           {(preds == y_xor).all()}\n")


# ── PART B: KERAS — SAME THING, 4 LINES ──────────────────────────────────────

print("=" * 45)
print("  Keras does all of that. In 4 lines.")
print("=" * 45)

try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers
    from sklearn.datasets        import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing   import StandardScaler

    X_k, y_k = make_classification(
        n_samples=2000, n_features=15, n_informative=10, random_state=42
    )
    X_tr, X_te, y_tr, y_te = train_test_split(X_k, y_k, test_size=0.2, random_state=42)
    sc   = StandardScaler()
    X_tr = sc.fit_transform(X_tr)
    X_te = sc.transform(X_te)

    # ── THE 4 LINES ──────────────────────────────────────────────────────────
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(15,)),
        layers.Dropout(0.3),   # randomly disable 30% of neurons — prevents overfitting
        layers.Dense(32, activation='relu'),
        layers.Dense(1,  activation='sigmoid'),
    ])

    model.compile(
        optimizer = 'adam',
        loss      = 'binary_crossentropy',
        metrics   = ['accuracy'],
    )

    # EarlyStopping: stop training when val_loss stops improving
    cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)

    history = model.fit(
        X_tr, y_tr,
        validation_split = 0.2,
        epochs           = 100,
        batch_size       = 32,
        callbacks        = [cb],
        verbose          = 1,
    )

    loss, acc = model.evaluate(X_te, y_te, verbose=0)
    print(f"\nKeras Test accuracy: {acc:.4f}")
    print(f"Epochs trained:      {len(history.history['loss'])}")

except ImportError:
    print("\nTensorFlow not installed.")
    print("Install with: pip install tensorflow")
    print("Then re-run this script.")
