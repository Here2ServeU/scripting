"""
Pattern 01 — Counter
count_by_status.py

Count how many items fall into each status category.
T2S: Python for AI & ML Engineers
"""

from collections import Counter


def count_by_status(items, key):
    """
    Count how many items have each value for the given key.

    Args:
        items: list of dicts
        key:   the field to count by

    Returns:
        dict mapping each value to its count

    Examples:
        >>> count_by_status([{'status': 'Running'}, {'status': 'Crashed'}, {'status': 'Running'}], 'status')
        {'Running': 2, 'Crashed': 1}
        >>> count_by_status([], 'status')
        {}
    """
    if not items:
        return {}
    return dict(Counter(item[key] for item in items))


# ── DEMO ─────────────────────────────────────────────────────────────────────

pods = [
    {'name': 'api-1',      'status': 'Running'},
    {'name': 'api-2',      'status': 'Crashed'},
    {'name': 'worker-1',   'status': 'Running'},
    {'name': 'worker-2',   'status': 'Running'},
    {'name': 'database-1', 'status': 'Pending'},
    {'name': 'cache-1',    'status': 'Running'},
    {'name': 'cache-2',    'status': 'Crashed'},
]

result = count_by_status(pods, 'status')
print("Pod status counts:")
for status, count in sorted(result.items(), key=lambda x: -x[1]):
    print(f"  {status:<12} {count}")
# Running      4
# Crashed      2
# Pending      1

# Edge cases
print(count_by_status([], 'status'))        # {}
print(count_by_status([{'status': 'Running'}], 'status'))  # {'Running': 1}
