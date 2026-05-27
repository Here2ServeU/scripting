"""
Pattern 02 — defaultdict
average_per_group.py

Compute the average score per group.
T2S: Python for AI & ML Engineers
"""

from collections import defaultdict


def average_per_group(runs, group_key='agent', score_key='score'):
    """
    Compute the average score for each group.

    Returns a dict mapping group name -> average score (rounded to 4 dp).

    Examples:
        >>> runs = [{'agent':'v1','score':0.94},{'agent':'v1','score':0.80},{'agent':'v2','score':0.60}]
        >>> average_per_group(runs)
        {'v1': 0.87, 'v2': 0.6}
        >>> average_per_group([])
        {}
    """
    if not runs:
        return {}

    groups = defaultdict(list)
    for run in runs:
        groups[run[group_key]].append(run[score_key])

    return {
        group: round(sum(scores) / len(scores), 4)
        for group, scores in groups.items()
    }


def best_and_worst_group(runs, group_key='agent', score_key='score'):
    """
    Return the group with the highest average and the group with the lowest average.

    Returns (best_name, best_avg, worst_name, worst_avg)
    Returns (None, 0, None, 0) if runs is empty.
    """
    if not runs:
        return None, 0.0, None, 0.0

    avgs  = average_per_group(runs, group_key, score_key)
    best  = max(avgs, key=avgs.get)
    worst = min(avgs, key=avgs.get)
    return best, avgs[best], worst, avgs[worst]


# ── DEMO ─────────────────────────────────────────────────────────────────────

runs = [
    {'agent': 'voice-v1', 'score': 0.94},
    {'agent': 'voice-v2', 'score': 0.61},
    {'agent': 'voice-v1', 'score': 0.88},
    {'agent': 'voice-v3', 'score': 0.72},
    {'agent': 'voice-v1', 'score': 0.90},
    {'agent': 'voice-v2', 'score': 0.55},
    {'agent': 'voice-v3', 'score': 0.87},
    {'agent': 'voice-v2', 'score': 0.91},
]

avgs = average_per_group(runs)
print("Average score per agent:")
for agent, avg in sorted(avgs.items(), key=lambda x: -x[1]):
    bar = '█' * int(avg * 20)
    print(f"  {agent:<12} {avg:.4f}  {bar}")

print()
best, b_avg, worst, w_avg = best_and_worst_group(runs)
print(f"Best:  {best}  ({b_avg:.4f})")
print(f"Worst: {worst} ({w_avg:.4f})")
