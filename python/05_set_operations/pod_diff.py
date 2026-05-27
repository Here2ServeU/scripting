"""
Pattern 05 — Set Operations
pod_diff.py

Full real-world example: detect what changed between two pod snapshots.
Python for AI & ML Engineers
"""


def pod_diff(before, after):
    """
    Given two lists of pod names, return what changed.

    Returns a dict with:
        'added':     pods in after but not in before
        'removed':   pods in before but not in after
        'unchanged': pods in both (no change)

    Examples:
        >>> before = ['api-1','api-2','worker-1']
        >>> after  = ['api-1','worker-1','worker-2']
        >>> pod_diff(before, after)
        {'added': ['worker-2'], 'removed': ['api-2'], 'unchanged': ['api-1', 'worker-1']}
    """
    before_set = set(before)
    after_set  = set(after)

    return {
        'added':     sorted(after_set  - before_set),
        'removed':   sorted(before_set - after_set),
        'unchanged': sorted(before_set & after_set),
    }


def summarise_diff(before, after):
    """Print a human-readable deployment diff."""
    diff = pod_diff(before, after)
    print(f"  ✅ Added     ({len(diff['added'])}):     {diff['added']}")
    print(f"  ❌ Removed   ({len(diff['removed'])}):   {diff['removed']}")
    print(f"  ⏸  Unchanged ({len(diff['unchanged'])}): {diff['unchanged']}")
    total_change = len(diff['added']) + len(diff['removed'])
    print(f"  Total changes: {total_change}")


def agents_only_in_one_test(test_a, test_b):
    """
    Return agents that ran in exactly one test but not both.
    (Symmetric difference)
    """
    return sorted(set(test_a) ^ set(test_b))


# ── DEMO ─────────────────────────────────────────────────────────────────────

before = ['api-1', 'api-2', 'worker-1', 'worker-2', 'cache-1']
after  = ['api-1', 'worker-1', 'worker-2', 'cache-1', 'cache-2', 'api-3']

print("=== Deployment diff ===")
summarise_diff(before, after)

print()
print("=== Raw diff dict ===")
import json
print(json.dumps(pod_diff(before, after), indent=2))

print()
test_a = ['voice-v1', 'voice-v2', 'voice-v3']
test_b = ['voice-v2', 'voice-v3', 'voice-v4']
print(f"Only in one test: {agents_only_in_one_test(test_a, test_b)}")
# ['voice-v1', 'voice-v4']

print()
print("Edge cases:")
print(pod_diff([], []))
print(pod_diff(['api-1'], ['api-1']))
print(pod_diff([], ['new-1', 'new-2']))
