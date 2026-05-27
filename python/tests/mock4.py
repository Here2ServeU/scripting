"""
T2S: Python for AI & ML Engineers
Practice Test 4: Full DevOps Test — The Hardest One
github.com/Here2ServeU/scripting

Timer: 70 minutes  ·  4 questions
If you can finish this without looking at answers, you are ready.
"""

from collections import defaultdict


# ── Q1: Read the Log Level ────────────────────────────────────────────────────
# Pattern: parse text (split + index)
# EASY

def parse_log_level(line):
    """
    You get a log line in the format: TIMESTAMP LEVEL SERVICE MESSAGE
    Return the second word, which is the log level.
    If the line has fewer than 2 words, return 'UNKNOWN'.

    Examples:
        >>> parse_log_level('2024-01-15 ERROR everse-api request failed')
        'ERROR'
        >>> parse_log_level('2024-01-15')
        'UNKNOWN'
        >>> parse_log_level('')
        'UNKNOWN'
    """
    words = line.strip().split()
    if len(words) < 2:
        return 'UNKNOWN'
    return words[1]


# ── Q2: Unique Agent Names ────────────────────────────────────────────────────
# Pattern: set comprehension + sorted()
# EASY

def unique_agents(runs):
    """
    Return a sorted list of unique agent names with no duplicates.

    Examples:
        >>> runs = [{'agent':'v1','score':0.9},{'agent':'v2','score':0.6},{'agent':'v1','score':0.8}]
        >>> unique_agents(runs)
        ['v1', 'v2']
        >>> unique_agents([])
        []
    """
    if not runs:
        return []
    return sorted({run['agent'] for run in runs})


# ── Q3: Find the Failing Agents ───────────────────────────────────────────────
# Pattern 2: group (defaultdict -> average -> filter)
# MEDIUM

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


# ── Q4: Highest Average Window ────────────────────────────────────────────────
# Pattern 4: sliding window
# HARD

def max_window_average(scores, k):
    """
    Return the highest average of any k consecutive scores.
    Round to 2 decimal places.
    Return 0.0 if there are fewer than k scores.

    Examples:
        >>> max_window_average([0.9, 0.4, 0.8, 0.7, 0.95], 3)
        0.82
        >>> max_window_average([0.5, 0.6], 3)
        0.0
        >>> max_window_average([], 3)
        0.0
    """
    if not scores or len(scores) < k:
        return 0.0

    window = sum(scores[:k])
    best   = window

    for i in range(k, len(scores)):
        window += scores[i]
        window -= scores[i - k]
        best = max(best, window)

    return round(best / k, 2)


# ── TEST RUNNER ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 50)
    print("Practice Test 4: Full DevOps Test")
    print("=" * 50)

    print("\nQ1: parse_log_level")
    assert parse_log_level('2024-01-15 ERROR everse-api request failed') == 'ERROR'
    assert parse_log_level('2024-01-15')                                  == 'UNKNOWN'
    assert parse_log_level('')                                            == 'UNKNOWN'
    assert parse_log_level('  ')                                          == 'UNKNOWN'
    assert parse_log_level('2024-01-15 INFO service started')             == 'INFO'
    assert parse_log_level('2024-01-15 WARN slow response detected')      == 'WARN'
    print("  All Q1 tests passed ✓")

    print("\nQ2: unique_agents")
    runs = [{'agent':'v1','score':0.9},{'agent':'v2','score':0.6},{'agent':'v1','score':0.8}]
    assert unique_agents(runs) == ['v1', 'v2']
    assert unique_agents([]) == []
    assert unique_agents([{'agent':'only','score':0.5}]) == ['only']
    print("  All Q2 tests passed ✓")

    print("\nQ3: failing_agents")
    runs = [
        {'agent': 'v1', 'score': 0.94},
        {'agent': 'v1', 'score': 0.80},
        {'agent': 'v2', 'score': 0.60},
    ]
    assert failing_agents(runs, 0.85) == ['v2']
    assert failing_agents([], 0.85) == []
    runs2 = [{'agent':'a','score':0.50},{'agent':'b','score':0.50}]
    assert failing_agents(runs2, 0.85) == ['a', 'b']
    runs3 = [{'agent':'a','score':0.90},{'agent':'b','score':0.90}]
    assert failing_agents(runs3, 0.85) == []
    print("  All Q3 tests passed ✓")

    print("\nQ4: max_window_average")
    assert max_window_average([0.9, 0.4, 0.8, 0.7, 0.95], 3) == 0.82
    assert max_window_average([0.5, 0.6], 3)                   == 0.0
    assert max_window_average([], 3)                            == 0.0
    assert max_window_average([1.0, 1.0, 1.0], 3)              == 1.0
    assert max_window_average([0.8, 0.8, 0.8], 3)              == 0.8
    assert max_window_average([0.5], 1)                         == 0.5
    print("  All Q4 tests passed ✓")

    print("\n✅  All Practice Test 4 tests passed!")
    print("\n🎯  If you reached this line without looking at answers, you are ready.")
