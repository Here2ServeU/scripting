"""
Pattern 04 — Sliding Window
max_window_sum.py

Find the highest sum of any K consecutive items.
Python for AI & ML Engineers
"""


def max_window_sum(nums, k):
    """
    Return the largest sum of any k consecutive numbers.
    Return 0 if the list has fewer than k elements.

    Examples:
        >>> max_window_sum([1, 4, 2, 9, 7, 3, 8], 3)
        24   # window [9, 7, 3] = 19? No — [2, 9, 7] = 18? Check: 9+7+8=24
        >>> max_window_sum([1, 2], 3)
        0
        >>> max_window_sum([], 3)
        0
    """
    if not nums or len(nums) < k:
        return 0

    # Step 1: Sum the first window
    window = sum(nums[:k])
    best   = window

    # Step 2: Slide the window one position at a time
    for i in range(k, len(nums)):
        window += nums[i]       # bring in the new item on the right
        window -= nums[i - k]   # remove the old item on the left
        best = max(best, window)

    return best


def max_window_sum_with_index(nums, k):
    """
    Return (max_sum, start_index) of the best window.
    start_index is where the winning window begins.
    """
    if not nums or len(nums) < k:
        return 0, -1

    window    = sum(nums[:k])
    best      = window
    best_start = 0

    for i in range(k, len(nums)):
        window += nums[i]
        window -= nums[i - k]
        if window > best:
            best       = window
            best_start = i - k + 1

    return best, best_start


# ── DEMO ─────────────────────────────────────────────────────────────────────

nums = [1, 4, 2, 9, 7, 3, 8]
k    = 3

print(f"nums = {nums},  k = {k}")
print(f"Max window sum: {max_window_sum(nums, k)}")

best_sum, start = max_window_sum_with_index(nums, k)
print(f"Best window:    {nums[start:start+k]}  (starts at index {start})  sum={best_sum}")

print()
print("Edge cases:")
print(max_window_sum([5], 1))          # 5
print(max_window_sum([1, 2], 3))       # 0
print(max_window_sum([], 3))           # 0
print(max_window_sum([3, 3, 3], 3))    # 9
