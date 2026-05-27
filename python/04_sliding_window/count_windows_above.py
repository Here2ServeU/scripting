"""
Pattern 04 — Sliding Window
count_windows_above.py

Count how many K-windows have a sum or average above a threshold.
T2S: Python for AI & ML Engineers
"""


def count_windows_above_threshold(scores, k, threshold):
    """
    Count how many k-windows have an average >= threshold.

    Examples:
        >>> count_windows_above_threshold([0.9, 0.4, 0.8, 0.7, 0.95], 3, 0.80)
        2
        >>> count_windows_above_threshold([], 3, 0.80)
        0
    """
    if not scores or len(scores) < k:
        return 0

    window = sum(scores[:k])
    count  = 1 if (window / k) >= threshold else 0

    for i in range(k, len(scores)):
        window += scores[i]
        window -= scores[i - k]
        if (window / k) >= threshold:
            count += 1

    return count


def windows_above_threshold(scores, k, threshold):
    """
    Return all k-windows whose average >= threshold.
    Each result is the list of scores in that window.
    """
    if not scores or len(scores) < k:
        return []

    result = []
    window = sum(scores[:k])
    if (window / k) >= threshold:
        result.append(scores[:k])

    for i in range(k, len(scores)):
        window += scores[i]
        window -= scores[i - k]
        if (window / k) >= threshold:
            result.append(scores[i - k + 1: i + 1])

    return result


# ── DEMO ─────────────────────────────────────────────────────────────────────

scores    = [0.9, 0.4, 0.8, 0.7, 0.95]
k         = 3
threshold = 0.80

print(f"scores = {scores},  k = {k},  threshold = {threshold}")
print(f"Windows above threshold: {count_windows_above_threshold(scores, k, threshold)}")

print("\nAll winning windows:")
for w in windows_above_threshold(scores, k, threshold):
    avg = sum(w) / len(w)
    print(f"  {w}  avg={avg:.2f}")

print()
print("Edge cases:")
print(count_windows_above_threshold([], 3, 0.80))            # 0
print(count_windows_above_threshold([0.5, 0.6], 3, 0.80))   # 0
print(count_windows_above_threshold([1.0, 1.0, 1.0], 3, 0.80))  # 1
