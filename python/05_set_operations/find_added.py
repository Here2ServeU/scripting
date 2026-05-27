"""
Pattern 05 — Set Operations
find_added.py

Find items that are in B but NOT in A.
"What appeared?" / "What was added?"
T2S: Python for AI & ML Engineers
"""


def find_added(before, after):
    """
    Return a sorted list of items in 'after' that were not in 'before'.

    Examples:
        >>> find_added(['api-1','api-2','worker-1'], ['api-1','worker-1','worker-2'])
        ['worker-2']
        >>> find_added(['a','b'], ['a','b'])
        []
    """
    if not after:
        return []
    return sorted(set(after) - set(before))


def new_features(old_features, new_features_list):
    """
    Return features that are new in the latest version.
    """
    return sorted(set(new_features_list) - set(old_features))


# ── DEMO ─────────────────────────────────────────────────────────────────────

before = ['api-1', 'api-2', 'worker-1']
after  = ['api-1', 'worker-1', 'worker-2', 'cache-1']

print(f"Added:   {find_added(before, after)}")     # ['cache-1', 'worker-2']

old_v = ['login', 'logout', 'profile']
new_v = ['login', 'logout', 'profile', 'dashboard', 'analytics']
print(f"New features: {new_features(old_v, new_v)}")   # ['analytics', 'dashboard']

print()
print("Edge cases:")
print(find_added([], ['api-1']))              # ['api-1']
print(find_added(['api-1'], []))              # []
print(find_added(['a', 'b'], ['a', 'b']))     # []
