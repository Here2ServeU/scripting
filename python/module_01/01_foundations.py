"""
T2S: Python for AI & ML Engineers
Module 1: Python Foundations for AI
github.com/Here2ServeU/scripting

In AI, everything is eventually a number.
This module covers the 5 data types, functions, classes,
and list comprehensions used in real ML code.
"""

# ── THE 5 DATA TYPES ─────────────────────────────────────────────────────────

learning_rate = 0.001          # float  — loss values, accuracy, weights
batch_size    = 32             # int    — epochs, layers, units
losses        = [0.98, 0.87, 0.73, 0.61, 0.54]   # list — loss history
labels        = [0, 1, 0, 1, 1, 0]               # list — training targets
is_training   = True           # bool  — mode flags

model_config = {
    'layers':    4,
    'units':     128,
    'dropout':   0.2,
    'optimizer': 'adam',
}

print(f"Learning rate: {learning_rate}")
print(f"Batch size:    {batch_size}")
print(f"Losses:        {losses}")
print(f"Config:        {model_config}")

# Always check types
print(type(learning_rate))   # <class 'float'>
print(type(batch_size))      # <class 'int'>
print(type(losses))          # <class 'list'>

# Convert explicitly — never assume
as_float = float("3.14")
as_int   = int(3.99)         # truncates, does NOT round
print(as_float, as_int)      # 3.14  3

# ── FUNCTIONS ─────────────────────────────────────────────────────────────────

def normalize(data, method='minmax'):
    """
    Normalize a list of numbers.
    method='minmax' scales to [0, 1]
    method='zscore' centers at 0 with std=1
    """
    if not data:
        return []

    if method == 'minmax':
        lo, hi = min(data), max(data)
        if lo == hi:
            return [0.0] * len(data)
        return [(x - lo) / (hi - lo) for x in data]

    elif method == 'zscore':
        mean = sum(data) / len(data)
        std  = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        if std == 0:
            return [0.0] * len(data)
        return [(x - mean) / std for x in data]

    else:
        raise ValueError(f"Unknown method: {method}")


raw = [10, 25, 3, 89, 42, 67]
print('\nMin-Max:', [round(v, 3) for v in normalize(raw)])
print('Z-Score:', [round(v, 3) for v in normalize(raw, 'zscore')])
print('Empty:  ', normalize([]))

# ── CLASSES ───────────────────────────────────────────────────────────────────

class DataPipeline:
    """
    A reusable preprocessing pipeline.
    Demonstrates method chaining with return self.
    """

    def __init__(self, name, normalize_data=True):
        self.name      = name
        self.do_norm   = normalize_data
        self.data      = []
        self._original = []

    def load(self, data):
        self._original = list(data)
        self.data      = list(data)
        print(f"[{self.name}] Loaded {len(data)} samples")
        return self   # enables chaining: .load(...).process()

    def process(self):
        if not self.data:
            print(f"[{self.name}] Nothing to process")
            return self
        if self.do_norm:
            lo, hi = min(self.data), max(self.data)
            if lo != hi:
                self.data = [(x - lo) / (hi - lo) for x in self.data]
            print(f"[{self.name}] Normalised")
        return self

    def summary(self):
        if not self.data:
            print(f"[{self.name}] Empty")
            return self
        print(f"[{self.name}] Range: [{min(self.data):.3f}, {max(self.data):.3f}]  "
              f"Mean: {sum(self.data)/len(self.data):.3f}")
        return self


pipe = DataPipeline('Sales Data')
pipe.load([5, 15, 25, 35, 45]).process().summary()

pipe2 = DataPipeline('Scores', normalize_data=False)
pipe2.load([0.9, 0.7, 0.8]).summary()

# ── LIST COMPREHENSIONS ───────────────────────────────────────────────────────

data       = [10, -5, 23, -8, 17, -2, 31]

positive   = [x for x in data if x > 0]
squared    = [x ** 2 for x in data]
normalised = [(x + 100) / 200 for x in data]

print('\nPositive: ',  positive)
print('Squared:  ',  squared)
print('Normalised:', [round(v, 3) for v in normalised])

# Nested comprehension: flatten a 2D list
matrix  = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat    = [x for row in matrix for x in row]
print('Flat:     ', flat)
