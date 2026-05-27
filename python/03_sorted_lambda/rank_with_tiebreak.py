"""
Pattern 03 — sorted + lambda
rank_with_tiebreak.py

Sort with a secondary (alphabetical) tiebreak.
Python for AI & ML Engineers
"""


def rank_agents(agents):
    """
    Rank agents by score descending. On a tie, sort by name ascending.

    Args:
        agents: list of {'name': str, 'score': float}

    Returns:
        sorted list

    Examples:
        >>> agents = [{'name':'beta','score':0.88},{'name':'alpha','score':0.88},{'name':'gamma','score':0.94}]
        >>> [a['name'] for a in rank_agents(agents)]
        ['gamma', 'alpha', 'beta']
    """
    if not agents:
        return []
    # (-score, name) means: biggest score first, then alphabetically on tie
    return sorted(agents, key=lambda a: (-a['score'], a['name']))


def top_k_with_tiebreak(runs, k):
    """
    Return the top K runs by score. On score ties, prefer the one with the
    lower run ID (alphabetically).

    Examples:
        >>> runs = [{'id':'r2','score':0.90},{'id':'r1','score':0.90},{'id':'r3','score':0.80}]
        >>> [r['id'] for r in top_k_with_tiebreak(runs, 2)]
        ['r1', 'r2']
    """
    if not runs or k <= 0:
        return []
    return sorted(runs, key=lambda r: (-r['score'], r['id']))[:k]


# ── DEMO ─────────────────────────────────────────────────────────────────────

agents = [
    {'name': 'beta',    'score': 0.88},
    {'name': 'alpha',   'score': 0.88},
    {'name': 'gamma',   'score': 0.94},
    {'name': 'delta',   'score': 0.88},
    {'name': 'epsilon', 'score': 0.72},
]

print("Ranking (score desc, name asc on tie):")
for i, a in enumerate(rank_agents(agents), 1):
    print(f"  #{i}  {a['name']:<10} {a['score']}")
# #1  gamma       0.94
# #2  alpha       0.88   (tie broken alphabetically)
# #3  beta        0.88
# #4  delta       0.88
# #5  epsilon     0.72

print()
runs = [
    {'id': 'r3', 'score': 0.90},
    {'id': 'r1', 'score': 0.90},
    {'id': 'r2', 'score': 0.90},
    {'id': 'r4', 'score': 0.80},
]
top2 = top_k_with_tiebreak(runs, 2)
print(f"Top 2 with tiebreak: {[r['id'] for r in top2]}")
# ['r1', 'r2']
