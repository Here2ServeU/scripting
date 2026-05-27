"""
T2S: Python for AI & ML Engineers
Practice Test 3: Sliding Window and Set Operations
github.com/Here2ServeU/scripting

Timer: 70 minutes  ·  4 questions
"""


# ── Q1: Pods Added and Removed ────────────────────────────────────────────────
# Pattern 5: set operations
# EASY

def deployment_changes(before, after):
    """
    Given lists of pod names before and after a deployment,
    return a dict with 'added' and 'removed' lists (both sorted).

    Examples:
        >>> deployment_changes(['api-1','api-2','worker-1'], ['api-1','worker-1','worker-2'])
        {'added': ['worker-2'], 'removed': ['api-2']}
        >>> deployment_changes([], [])
        {'added': [], 'removed': []}
    """
    before_set = set(before)
    after_set  = set(after)
    return {
        'added':   sorted(after_set  - before_set),
        'removed': sorted(before_set - after_set),
    }


# ── Q2: Remove Duplicates ─────────────────────────────────────────────────────
# Pattern 5: set
# EASY

def unique_sorted(items):
    """
    Return a sorted list of unique items with duplicates removed.

    Examples:
        >>> unique_sorted([3, 1, 4, 1, 5, 9, 2, 6, 5])
        [1, 2, 3, 4, 5, 6, 9]
        >>> unique_sorted([])
        []
    """
    if not items:
        return []
    return sorted(set(items))


# ── Q3: Highest Sum Window ────────────────────────────────────────────────────
# Pattern 4: sliding window
# MEDIUM

def max_window_sum(nums, k):
    """
    Return the largest sum of any k consecutive numbers.
    Return 0 if there are fewer than k numbers.

    Examples:
        >>> max_window_sum([2, 1, 5, 1, 3, 2], 3)
        9
        >>> max_window_sum([1, 2], 3)
        0
        >>> max_window_sum([], 3)
        0
    """
    if not nums or len(nums) < k:
        return 0
    window = sum(nums[:k])
    best   = window
    for i in range(k, len(nums)):
        window += nums[i]
        window -= nums[i - k]
        best = max(best, window)
    return best


# ── Q4: Agents in Both Test Suites ───────────────────────────────────────────
# Pattern 5: intersection
# MEDIUM

def agents_in_both(suite_a, suite_b):
    """
    Given two lists of agent names, return a sorted list of agents
    that appear in both suites.

    Examples:
        >>> agents_in_both(['v1','v2','v3'], ['v2','v3','v4'])
        ['v2', 'v3']
        >>> agents_in_both([], ['v1'])
        []
    """
    if not suite_a or not suite_b:
        return []
    return sorted(set(suite_a) & set(suite_b))


# ── TEST RUNNER ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 50)
    print("Practice Test 3: Sliding Window & Set Operations")
    print("=" * 50)

    print("\nQ1: deployment_changes")
    r = deployment_changes(['api-1','api-2','worker-1'], ['api-1','worker-1','worker-2'])
    assert r == {'added': ['worker-2'], 'removed': ['api-2']}, f"Got: {r}"
    assert deployment_changes([],[]) == {'added':[],'removed':[]}
    assert deployment_changes(['a'],['a']) == {'added':[],'removed':[]}
    print("  All Q1 tests passed ✓")

    print("\nQ2: unique_sorted")
    assert unique_sorted([3,1,4,1,5,9,2,6,5]) == [1,2,3,4,5,6,9]
    assert unique_sorted([]) == []
    assert unique_sorted([1]) == [1]
    assert unique_sorted([2,2,2]) == [2]
    print("  All Q2 tests passed ✓")

    print("\nQ3: max_window_sum")
    assert max_window_sum([2,1,5,1,3,2], 3) == 9
    assert max_window_sum([1,2], 3) == 0
    assert max_window_sum([], 3) == 0
    assert max_window_sum([5], 1) == 5
    assert max_window_sum([3,3,3], 3) == 9
    print("  All Q3 tests passed ✓")

    print("\nQ4: agents_in_both")
    assert agents_in_both(['v1','v2','v3'], ['v2','v3','v4']) == ['v2','v3']
    assert agents_in_both([], ['v1']) == []
    assert agents_in_both(['v1'], ['v2']) == []
    assert agents_in_both(['v1','v2'], ['v1','v2']) == ['v1','v2']
    print("  All Q4 tests passed ✓")

    print("\n✅  All Practice Test 3 tests passed!")
