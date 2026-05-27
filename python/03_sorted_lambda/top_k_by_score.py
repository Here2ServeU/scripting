"""
Pattern 03 — sorted + lambda
top_k_by_score.py

Return the top K items by score.
T2S: Python for AI & ML Engineers
"""


def top_k_runs(runs, k):
    """
    Return the k runs with the highest scores.

    Examples:
        >>> runs = [{'id':'r1','score':0.94},{'id':'r2','score':0.61},{'id':'r3','score':0.88}]
        >>> top_k_runs(runs, 2)
        [{'id': 'r1', 'score': 0.94}, {'id': 'r3', 'score': 0.88}]
        >>> top_k_runs([], 2)
        []
    """
    if not runs or k <= 0:
        return []
    return sorted(runs, key=lambda r: r['score'], reverse=True)[:k]


def top_k_agent_names(scores_dict, k):
    """
    Given a dict of agent -> score, return the names of the top k agents.

    Examples:
        >>> top_k_agent_names({'v1': 0.94, 'v2': 0.61, 'v3': 0.88}, 2)
        ['v1', 'v3']
    """
    if not scores_dict or k <= 0:
        return []
    return sorted(scores_dict, key=scores_dict.get, reverse=True)[:k]


def best_run(runs):
    """
    Return the single run with the highest score.
    Returns None if runs is empty.
    """
    if not runs:
        return None
    return max(runs, key=lambda r: r['score'])


# ── DEMO ─────────────────────────────────────────────────────────────────────

runs = [
    {'id': 'r1', 'score': 0.94, 'agent': 'voice-v1'},
    {'id': 'r2', 'score': 0.61, 'agent': 'voice-v2'},
    {'id': 'r3', 'score': 0.88, 'agent': 'voice-v3'},
    {'id': 'r4', 'score': 0.45, 'agent': 'voice-v1'},
    {'id': 'r5', 'score': 0.92, 'agent': 'voice-v2'},
]

print("Top 3 runs:")
for r in top_k_runs(runs, 3):
    print(f"  {r['id']}: {r['score']}")

print()
scores = {'voice-v1': 0.94, 'voice-v2': 0.61, 'voice-v3': 0.88}
print(f"Top 2 agents: {top_k_agent_names(scores, 2)}")

print()
b = best_run(runs)
print(f"Best run: {b['id']} ({b['score']})")
