"""
Pattern 04 — Sliding Window
max_window_average.py

Find the highest average of any K consecutive items.
Python for AI & ML Engineers
"""


def max_window_average(scores, k):
    """
    Return the highest average of any k consecutive scores.
    Round to 2 decimal places.
    Return 0.0 if fewer than k scores.

    Examples:
        >>> max_window_average([0.9, 0.4, 0.8, 0.7, 0.95], 3)
        0.82
        >>> max_window_average([0.5, 0.6], 3)
        0.0
    """
    if not scores or len(scores) < k:
        return 0.0

    window = sum(scores[:k])
    best   = window

    for i in range(k, len(scores)):
        window += scores[i]
        window -= scores[i - k]
        best = max(best, window)

    return round(best / k, 2)


def best_k_window(scores, k):
    """
    Return (average, window_list) for the best K-window.
    """
    if not scores or len(scores) < k:
        return 0.0, []

    window    = sum(scores[:k])
    best      = window
    best_start = 0

    for i in range(k, len(scores)):
        window += scores[i]
        window -= scores[i - k]
        if window > best:
            best       = window
            best_start = i - k + 1

    best_window = scores[best_start:best_start + k]
    return round(best / k, 2), best_window


# ── DEMO ─────────────────────────────────────────────────────────────────────

scores = [0.9, 0.4, 0.8, 0.7, 0.95]
k      = 3

print(f"scores = {scores},  k = {k}")
print(f"Max window average: {max_window_average(scores, k)}")

avg, window = best_k_window(scores, k)
print(f"Best window: {window}  avg={avg}")

print()
print("Edge cases:")
print(max_window_average([0.5, 0.6], 3))         # 0.0
print(max_window_average([], 3))                  # 0.0
print(max_window_average([0.8, 0.8, 0.8], 3))    # 0.8
print(max_window_average([1.0], 1))               # 1.0
