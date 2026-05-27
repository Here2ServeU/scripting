"""
Python for AI & ML Engineers
Practice Test 2: Lists and Dictionaries
github.com/Here2ServeU/scripting

Timer: 70 minutes  ·  4 questions
"""

from collections import Counter, defaultdict


# ── Q1: Filter and Sort Scores ────────────────────────────────────────────────
# Pattern 3: sorted / filter
# EASY

def passing_scores(scores, threshold=0.85):
    """
    Return a sorted list (biggest first) of scores >= threshold.

    Examples:
        >>> passing_scores([0.94, 0.61, 0.88, 0.45, 0.92], 0.85)
        [0.94, 0.92, 0.88]
        >>> passing_scores([], 0.85)
        []
    """
    if not scores:
        return []
    return sorted([s for s in scores if s >= threshold], reverse=True)


# ── Q2: Key with Highest Value ────────────────────────────────────────────────
# Pattern 3: max with key
# EASY

def best_agent(scores_dict):
    """
    Return the agent name with the highest score.
    Return '' if the dict is empty.

    Examples:
        >>> best_agent({'voice-v1': 0.94, 'voice-v2': 0.61, 'voice-v3': 0.88})
        'voice-v1'
        >>> best_agent({})
        ''
    """
    if not scores_dict:
        return ''
    return max(scores_dict, key=scores_dict.get)


# ── Q3: Count by Field ────────────────────────────────────────────────────────
# Pattern 1: Counter
# MEDIUM

def count_by_field(items, field):
    """
    Count how many items have each value for the given field.

    Examples:
        >>> items = [{'env':'prod'},{'env':'dev'},{'env':'prod'},{'env':'staging'}]
        >>> count_by_field(items, 'env')
        {'prod': 2, 'dev': 1, 'staging': 1}
        >>> count_by_field([], 'env')
        {}
    """
    if not items:
        return {}
    return dict(Counter(item[field] for item in items))


# ── Q4: Group and Average ─────────────────────────────────────────────────────
# Pattern 2: defaultdict -> average
# MEDIUM

def average_by_group(runs, group_key, score_key='score'):
    """
    Compute the average score for each group.
    Return {} if runs is empty.

    Examples:
        >>> runs = [{'env':'prod','score':0.94},{'env':'dev','score':0.61},{'env':'prod','score':0.88}]
        >>> average_by_group(runs, 'env')
        {'prod': 0.91, 'dev': 0.61}
    """
    if not runs:
        return {}
    groups = defaultdict(list)
    for run in runs:
        groups[run[group_key]].append(run[score_key])
    return {
        group: round(sum(s) / len(s), 4)
        for group, s in groups.items()
    }


# ── TEST RUNNER ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 50)
    print("Practice Test 2: Lists and Dictionaries")
    print("=" * 50)

    print("\nQ1: passing_scores")
    assert passing_scores([0.94, 0.61, 0.88, 0.45, 0.92], 0.85) == [0.94, 0.92, 0.88]
    assert passing_scores([], 0.85) == []
    assert passing_scores([0.50, 0.60], 0.85) == []
    assert passing_scores([0.85], 0.85) == [0.85]
    print("  All Q1 tests passed ✓")

    print("\nQ2: best_agent")
    assert best_agent({'v1': 0.94, 'v2': 0.61, 'v3': 0.88}) == 'v1'
    assert best_agent({}) == ''
    assert best_agent({'only': 0.75}) == 'only'
    print("  All Q2 tests passed ✓")

    print("\nQ3: count_by_field")
    items = [{'env':'prod'},{'env':'dev'},{'env':'prod'},{'env':'staging'}]
    result = count_by_field(items, 'env')
    assert result['prod'] == 2
    assert result['dev']  == 1
    assert count_by_field([], 'env') == {}
    print("  All Q3 tests passed ✓")

    print("\nQ4: average_by_group")
    runs = [
        {'env': 'prod', 'score': 0.94},
        {'env': 'dev',  'score': 0.61},
        {'env': 'prod', 'score': 0.88},
    ]
    avgs = average_by_group(runs, 'env')
    assert avgs['prod'] == 0.91
    assert avgs['dev']  == 0.61
    assert average_by_group([], 'env') == {}
    print("  All Q4 tests passed ✓")

    print("\n✅  All Practice Test 2 tests passed!")
