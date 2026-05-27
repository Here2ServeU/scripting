"""
Pattern 05 — Set Operations
find_missing.py

Find items that are in A but NOT in B.
"What disappeared?" / "What is missing?"
Python for AI & ML Engineers
"""


def find_missing(before, after):
    """
    Return a sorted list of items that were in 'before' but are not in 'after'.

    Examples:
        >>> find_missing(['api-1', 'api-2', 'worker-1'], ['api-1', 'worker-1', 'worker-2'])
        ['api-2']
        >>> find_missing([], ['api-1'])
        []
    """
    if not before:
        return []
    return sorted(set(before) - set(after))


def find_removed_pods(before, after):
    """
    Return pods that existed before but are gone after the deployment.

    Examples:
        >>> find_removed_pods({'api-1','api-2','worker-1'}, {'api-1','worker-1','worker-2'})
        ['api-2']
    """
    return sorted(set(before) - set(after))


def missing_keys(expected_keys, actual_dict):
    """
    Return keys that are expected but missing from the actual dict.

    Examples:
        >>> missing_keys(['name','score','status'], {'name':'v1','score':0.94})
        ['status']
    """
    if not expected_keys:
        return []
    return sorted(set(expected_keys) - set(actual_dict.keys()))


# ── DEMO ─────────────────────────────────────────────────────────────────────

before = ['api-1', 'api-2', 'worker-1', 'worker-2', 'cache-1']
after  = ['api-1', 'worker-1', 'worker-2', 'cache-1', 'cache-2']

missing = find_missing(before, after)
print(f"Removed: {missing}")    # ['api-2']

before_set = {'api-1', 'api-2', 'worker-1'}
after_set  = {'api-1', 'worker-1', 'worker-2'}
print(f"Gone:    {find_removed_pods(before_set, after_set)}")   # ['api-2']

record = {'name': 'voice-v1', 'score': 0.94}
print(f"Missing keys: {missing_keys(['name','score','status','region'], record)}")
# ['region', 'status']

print()
print("Edge cases:")
print(find_missing([], ['api-1']))              # []
print(find_missing(['api-1'], []))              # ['api-1']
print(find_missing(['a', 'b'], ['a', 'b']))     # []
