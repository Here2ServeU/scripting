"""
Pattern 03 — sorted + lambda
sort_versions.py

Sort version strings in natural order: v1, v2, v10, v20
NOT the default string order: v1, v10, v2, v20
Python for AI & ML Engineers
"""


def sort_versions(versions):
    """
    Sort version strings (e.g. 'v1', 'v2', 'v10') in natural numeric order.

    Examples:
        >>> sort_versions(['v10', 'v2', 'v1', 'v20'])
        ['v1', 'v2', 'v10', 'v20']
        >>> sort_versions([])
        []
    """
    if not versions:
        return []
    # Strip the 'v' prefix, convert to int, sort numerically
    return sorted(versions, key=lambda v: int(v[1:]))


def sort_semantic_versions(versions):
    """
    Sort semantic version strings: '1.2.10' before '1.10.2'.

    Examples:
        >>> sort_semantic_versions(['1.10.0', '1.2.3', '2.0.0', '1.2.10'])
        ['1.2.3', '1.2.10', '1.10.0', '2.0.0']
    """
    if not versions:
        return []
    return sorted(versions, key=lambda v: tuple(int(x) for x in v.split('.')))


def latest_version(versions):
    """
    Return the most recent version string.

    Examples:
        >>> latest_version(['v10', 'v2', 'v1', 'v20'])
        'v20'
    """
    if not versions:
        return ''
    return sort_versions(versions)[-1]


# ── DEMO ─────────────────────────────────────────────────────────────────────

versions = ['v10', 'v2', 'v1', 'v20', 'v3', 'v11']

print("Default (broken) sort:")
print(sorted(versions))
# ['v1', 'v10', 'v11', 'v2', 'v20', 'v3']  <- WRONG

print("Natural sort:")
print(sort_versions(versions))
# ['v1', 'v2', 'v3', 'v10', 'v11', 'v20']  <- CORRECT

print(f"Latest: {latest_version(versions)}")
# v20

print()
semver = ['1.10.0', '1.2.3', '2.0.0', '1.2.10', '1.0.9']
print("Semantic version sort:")
print(sort_semantic_versions(semver))
# ['1.0.9', '1.2.3', '1.2.10', '1.10.0', '2.0.0']
