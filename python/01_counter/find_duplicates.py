"""
Pattern 01 — Counter
find_duplicates.py

Find items that appear more than once.
T2S: Python for AI & ML Engineers
"""

from collections import Counter


def find_duplicates(items):
    """
    Return a sorted list of values that appear more than once.

    Examples:
        >>> find_duplicates([1, 2, 3, 2, 4, 3, 5])
        [2, 3]
        >>> find_duplicates([])
        []
    """
    if not items:
        return []
    counts = Counter(items)
    return sorted(k for k, v in counts.items() if v > 1)


def find_duplicate_ids(records, key='id'):
    """
    Return IDs that appear more than once across records.

    Examples:
        >>> records = [{'id':'a'},{'id':'b'},{'id':'a'},{'id':'c'},{'id':'b'}]
        >>> find_duplicate_ids(records)
        ['a', 'b']
    """
    if not records:
        return []
    ids    = [r[key] for r in records if key in r]
    counts = Counter(ids)
    return sorted(k for k, v in counts.items() if v > 1)


def has_duplicate(items):
    """
    Return True if any value appears more than once.

    Examples:
        >>> has_duplicate([1, 2, 3, 2])
        True
        >>> has_duplicate([1, 2, 3])
        False
    """
    if not items:
        return False
    return len(items) != len(set(items))


# ── DEMO ─────────────────────────────────────────────────────────────────────

nums = [1, 2, 3, 2, 4, 3, 5, 1, 1]
print(find_duplicates(nums))   # [1, 2, 3]
print(find_duplicates([]))     # []

records = [
    {'id': 'run-001', 'agent': 'v1'},
    {'id': 'run-002', 'agent': 'v2'},
    {'id': 'run-001', 'agent': 'v1'},
    {'id': 'run-003', 'agent': 'v3'},
    {'id': 'run-002', 'agent': 'v2'},
]
print(find_duplicate_ids(records))         # ['run-001', 'run-002']
print(find_duplicate_ids(records, 'agent')) # ['v1', 'v2']

print(has_duplicate([1, 2, 3, 2]))   # True
print(has_duplicate([1, 2, 3]))      # False
