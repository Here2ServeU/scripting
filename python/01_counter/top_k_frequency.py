"""
Pattern 01 — Counter
top_k_frequency.py

Return the top K most frequent items.
T2S: Python for AI & ML Engineers
"""

from collections import Counter


def top_k_words(words, k):
    """
    Return a list of the k most frequent words, sorted by frequency descending.
    On a frequency tie, sort alphabetically.

    Examples:
        >>> top_k_words(['a','b','a','c','b','a'], 2)
        ['a', 'b']
        >>> top_k_words([], 3)
        []
    """
    if not words or k <= 0:
        return []
    counts = Counter(words)
    # Sort by (-count, word) so ties go alphabetically
    return [word for word, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]]


def top_k_agents(runs, k):
    """
    Return the k agents that appear most frequently in the runs list.

    Args:
        runs: list of dicts, each with an 'agent' key
        k:    number of top agents to return

    Examples:
        >>> runs = [{'agent':'v1'},{'agent':'v2'},{'agent':'v1'},{'agent':'v1'},{'agent':'v2'}]
        >>> top_k_agents(runs, 2)
        ['v1', 'v2']
    """
    if not runs or k <= 0:
        return []
    counts = Counter(r['agent'] for r in runs)
    return [agent for agent, _ in counts.most_common(k)]


def top_k_log_errors(logs, k):
    """
    Count ERROR lines that contain each service name.
    Return the k services with the most errors.

    Examples:
        >>> logs = ['ERROR api-1 crash','ERROR api-1 oom','ERROR api-2 crash','WARN api-1 slow']
        >>> top_k_log_errors(logs, 1)
        ['api-1']
    """
    if not logs or k <= 0:
        return []
    error_lines   = [line for line in logs if line.startswith('ERROR')]
    service_names = []
    for line in error_lines:
        parts = line.split()
        if len(parts) >= 2:
            service_names.append(parts[1])
    if not service_names:
        return []
    counts = Counter(service_names)
    return [svc for svc, _ in counts.most_common(k)]


# ── DEMO ─────────────────────────────────────────────────────────────────────

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'cherry', 'banana']
print(top_k_words(words, 2))    # ['apple', 'banana']
print(top_k_words(words, 1))    # ['apple']
print(top_k_words([], 2))       # []

runs = [
    {'agent': 'v1', 'score': 0.94},
    {'agent': 'v2', 'score': 0.61},
    {'agent': 'v1', 'score': 0.88},
    {'agent': 'v3', 'score': 0.72},
    {'agent': 'v1', 'score': 0.90},
    {'agent': 'v2', 'score': 0.65},
]
print(top_k_agents(runs, 2))    # ['v1', 'v2']

logs = [
    'ERROR api-1 pod crashed',
    'ERROR api-1 oom killed',
    'ERROR api-2 pod crashed',
    'ERROR api-1 timeout',
    'WARN  api-2 slow response',
    'INFO  api-3 started',
]
print(top_k_log_errors(logs, 2))    # ['api-1', 'api-2']
print(top_k_log_errors(logs, 1))    # ['api-1']
