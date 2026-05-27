"""
Pattern 02 — defaultdict
group_by.py

Group items into buckets by any field.
T2S: Python for AI & ML Engineers
"""

from collections import defaultdict


def group_by(items, key):
    """
    Group a list of dicts by the value of a given key.

    Returns a dict mapping each unique value to a list of matching items.

    Examples:
        >>> runs = [{'agent':'v1','score':0.9},{'agent':'v2','score':0.6},{'agent':'v1','score':0.8}]
        >>> group_by(runs, 'agent')
        {'v1': [{'agent': 'v1', 'score': 0.9}, {'agent': 'v1', 'score': 0.8}], 'v2': [...]}
        >>> group_by([], 'agent')
        {}
    """
    if not items:
        return {}
    groups = defaultdict(list)
    for item in items:
        groups[item[key]].append(item)
    return dict(groups)


def group_logs_by_level(logs):
    """
    Group log lines by their level (first word).

    Examples:
        >>> group_logs_by_level(['ERROR pod crashed', 'WARN slow', 'ERROR oom'])
        {'ERROR': ['ERROR pod crashed', 'ERROR oom'], 'WARN': ['WARN slow']}
    """
    if not logs:
        return {}
    groups = defaultdict(list)
    for line in logs:
        level = line.strip().split()[0] if line.strip() else 'UNKNOWN'
        groups[level].append(line)
    return dict(groups)


# ── DEMO ─────────────────────────────────────────────────────────────────────

runs = [
    {'agent': 'voice-v1', 'score': 0.94, 'region': 'us-east'},
    {'agent': 'voice-v2', 'score': 0.61, 'region': 'us-west'},
    {'agent': 'voice-v1', 'score': 0.88, 'region': 'us-east'},
    {'agent': 'voice-v3', 'score': 0.72, 'region': 'eu-west'},
    {'agent': 'voice-v2', 'score': 0.55, 'region': 'us-west'},
    {'agent': 'voice-v1', 'score': 0.91, 'region': 'eu-west'},
]

grouped = group_by(runs, 'agent')
print("Grouped by agent:")
for agent, agent_runs in grouped.items():
    scores = [r['score'] for r in agent_runs]
    print(f"  {agent}: {len(agent_runs)} runs — scores: {scores}")

print()

by_region = group_by(runs, 'region')
print("Grouped by region:")
for region, region_runs in by_region.items():
    print(f"  {region}: {len(region_runs)} runs")

print()

logs = [
    'ERROR pod-api crashed',
    'INFO  service started',
    'ERROR oom killed',
    'WARN  disk high',
    'INFO  checkpoint saved',
    'ERROR timeout',
]
log_groups = group_logs_by_level(logs)
print("Logs grouped by level:")
for level, lines in log_groups.items():
    print(f"  {level}: {len(lines)}")
