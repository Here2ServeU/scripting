"""
Pattern 05 — Set Operations
find_common.py

Find items that appear in BOTH lists.
Python for AI & ML Engineers
"""


def find_common(list_a, list_b):
    """
    Return a sorted list of items that appear in both lists.

    Examples:
        >>> find_common(['api-1','api-2','worker-1'], ['api-1','worker-1','worker-2'])
        ['api-1', 'worker-1']
        >>> find_common([], ['api-1'])
        []
    """
    if not list_a or not list_b:
        return []
    return sorted(set(list_a) & set(list_b))


def agents_in_both_tests(test_a_agents, test_b_agents):
    """
    Return agents that participated in both test suites.
    """
    return find_common(test_a_agents, test_b_agents)


def shared_error_types(errors_a, errors_b):
    """
    Return error types that appear in both sets of logs.
    """
    return find_common(errors_a, errors_b)


# ── DEMO ─────────────────────────────────────────────────────────────────────

set_a = ['api-1', 'api-2', 'worker-1', 'cache-1']
set_b = ['api-1', 'worker-1', 'worker-2', 'cache-2']

print(f"In both: {find_common(set_a, set_b)}")     # ['api-1', 'worker-1']

test_a = ['voice-v1', 'voice-v2', 'voice-v3']
test_b = ['voice-v2', 'voice-v3', 'voice-v4']
print(f"In both test suites: {agents_in_both_tests(test_a, test_b)}")
# ['voice-v2', 'voice-v3']

errors_prod   = ['OOMKilled', 'CrashLoopBackOff', 'Timeout']
errors_staging = ['Timeout', 'ConnectionRefused', 'OOMKilled']
print(f"Common error types: {shared_error_types(errors_prod, errors_staging)}")
# ['OOMKilled', 'Timeout']

print()
print("Edge cases:")
print(find_common([], ['api-1']))                   # []
print(find_common(['a', 'b'], ['c', 'd']))           # []
print(find_common(['a', 'b'], ['a', 'b', 'c']))     # ['a', 'b']
