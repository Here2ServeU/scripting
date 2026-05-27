"""
Pattern 01 — Counter
count_per_agent.py

Count test runs, passes, and failures per agent.
T2S: Python for AI & ML Engineers
"""

from collections import Counter


def count_runs_per_agent(runs):
    """
    Count how many test runs each agent has.

    Examples:
        >>> runs = [{'agent':'v1'},{'agent':'v2'},{'agent':'v1'}]
        >>> count_runs_per_agent(runs)
        {'v1': 2, 'v2': 1}
    """
    if not runs:
        return {}
    return dict(Counter(r['agent'] for r in runs))


def count_passes_per_agent(runs, threshold=0.85):
    """
    Count how many PASSING runs each agent has.
    A run passes if its score >= threshold.

    Examples:
        >>> runs = [{'agent':'v1','score':0.94},{'agent':'v1','score':0.61},{'agent':'v2','score':0.90}]
        >>> count_passes_per_agent(runs, 0.85)
        {'v1': 1, 'v2': 1}
    """
    if not runs:
        return {}
    passing = [r['agent'] for r in runs if r.get('score', 0) >= threshold]
    return dict(Counter(passing))


def pass_rate_per_agent(runs, threshold=0.85):
    """
    Return the pass rate (0.0 to 1.0) for each agent.

    Examples:
        >>> runs = [{'agent':'v1','score':0.94},{'agent':'v1','score':0.61},{'agent':'v2','score':0.90}]
        >>> pass_rate_per_agent(runs, 0.85)
        {'v1': 0.5, 'v2': 1.0}
    """
    if not runs:
        return {}

    total  = Counter(r['agent'] for r in runs)
    passed = Counter(r['agent'] for r in runs if r.get('score', 0) >= threshold)

    return {
        agent: round(passed.get(agent, 0) / total[agent], 4)
        for agent in total
    }


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

print("Runs per agent:")
for agent, n in sorted(count_runs_per_agent(runs).items()):
    print(f"  {agent}: {n}")

print("\nPasses per agent (threshold=0.85):")
for agent, n in sorted(count_passes_per_agent(runs, 0.85).items()):
    print(f"  {agent}: {n}")

print("\nPass rate per agent:")
for agent, rate in sorted(pass_rate_per_agent(runs, 0.85).items()):
    print(f"  {agent}: {rate:.0%}")
