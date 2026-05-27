"""
Pattern 02 — defaultdict
agents_below_threshold.py

Find agents whose average score falls below a threshold.
Python for AI & ML Engineers
"""

from collections import defaultdict


def failing_agents(runs, threshold):
    """
    Return a sorted list of agent names whose average score < threshold.

    Examples:
        >>> runs = [{'agent':'v1','score':0.94},{'agent':'v1','score':0.80},{'agent':'v2','score':0.60}]
        >>> failing_agents(runs, 0.85)
        ['v2']
        >>> failing_agents([], 0.85)
        []
    """
    if not runs:
        return []

    scores = defaultdict(list)
    for run in runs:
        scores[run['agent']].append(run['score'])

    failing = []
    for agent, agent_scores in scores.items():
        avg = sum(agent_scores) / len(agent_scores)
        if avg < threshold:
            failing.append(agent)

    return sorted(failing)


def agents_by_status(runs, threshold):
    """
    Classify every agent as PASS or FAIL based on their average score.

    Returns {'PASS': [...sorted names...], 'FAIL': [...sorted names...]}
    """
    if not runs:
        return {'PASS': [], 'FAIL': []}

    scores = defaultdict(list)
    for run in runs:
        scores[run['agent']].append(run['score'])

    passing, failing = [], []
    for agent, agent_scores in scores.items():
        avg = sum(agent_scores) / len(agent_scores)
        (passing if avg >= threshold else failing).append(agent)

    return {'PASS': sorted(passing), 'FAIL': sorted(failing)}


# ── DEMO ─────────────────────────────────────────────────────────────────────

runs = [
    {'agent': 'voice-v1', 'score': 0.94},
    {'agent': 'voice-v2', 'score': 0.61},
    {'agent': 'voice-v1', 'score': 0.80},
    {'agent': 'voice-v3', 'score': 0.72},
    {'agent': 'voice-v2', 'score': 0.55},
    {'agent': 'voice-v3', 'score': 0.87},
    {'agent': 'voice-v2', 'score': 0.91},
]

threshold = 0.85
print(f"Agents failing (avg < {threshold}):")
print(failing_agents(runs, threshold))
# ['voice-v2', 'voice-v3']  — depends on averages

print()
status = agents_by_status(runs, threshold)
print(f"PASS: {status['PASS']}")
print(f"FAIL: {status['FAIL']}")

print()
print("Edge cases:")
print(failing_agents([], 0.85))             # []
print(agents_by_status([], 0.85))           # {'PASS': [], 'FAIL': []}
