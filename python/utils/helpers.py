"""
T2S: Python for AI & ML Engineers
utils/helpers.py — Shared utilities used across all modules and patterns
github.com/Here2ServeU/scripting
"""

from collections import Counter, defaultdict
from typing      import Any, Dict, List, Optional, Tuple


# ── GUARD CLAUSE WRAPPERS ────────────────────────────────────────────────────
# These mirror the guard clause pattern taught in the course.
# Use them to keep your function bodies clean.

def safe_avg(values: List[float], default: float = 0.0) -> float:
    """Return the average of a list, or default if the list is empty."""
    if not values:
        return default
    return sum(values) / len(values)


def safe_max(values: List[Any], default: Any = None) -> Any:
    """Return the max of a list, or default if the list is empty."""
    if not values:
        return default
    return max(values)


def safe_min(values: List[Any], default: Any = None) -> Any:
    """Return the min of a list, or default if the list is empty."""
    if not values:
        return default
    return min(values)


# ── PATTERN HELPERS ──────────────────────────────────────────────────────────

def count_by(items: List[Dict], key: str) -> Dict[str, int]:
    """Pattern 1 — Count items by a field key."""
    if not items:
        return {}
    return dict(Counter(item[key] for item in items if key in item))


def group_by(items: List[Dict], key: str) -> Dict[str, List]:
    """Pattern 2 — Group items into lists by a field key."""
    if not items:
        return {}
    groups = defaultdict(list)
    for item in items:
        if key in item:
            groups[item[key]].append(item)
    return dict(groups)


def top_k(items: List[Dict], score_key: str, k: int, reverse: bool = True) -> List[Dict]:
    """Pattern 3 — Return the top k items sorted by a score field."""
    if not items or k <= 0:
        return []
    return sorted(items, key=lambda x: x.get(score_key, 0), reverse=reverse)[:k]


def max_window(nums: List[float], k: int) -> float:
    """Pattern 4 — Return the maximum sum of any k consecutive numbers."""
    if not nums or len(nums) < k:
        return 0.0
    window = sum(nums[:k])
    best   = window
    for i in range(k, len(nums)):
        window += nums[i]
        window -= nums[i - k]
        best = max(best, window)
    return best


def missing_items(before: List, after: List) -> List:
    """Pattern 5 — Items in before but not in after."""
    if not before:
        return []
    return sorted(set(before) - set(after))


def added_items(before: List, after: List) -> List:
    """Pattern 5 — Items in after but not in before."""
    if not after:
        return []
    return sorted(set(after) - set(before))


def common_items(list_a: List, list_b: List) -> List:
    """Pattern 5 — Items in both lists."""
    if not list_a or not list_b:
        return []
    return sorted(set(list_a) & set(list_b))


# ── LOG UTILITIES ────────────────────────────────────────────────────────────

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parse a structured log line: TIMESTAMP LEVEL SERVICE MESSAGE
    Returns {} if the line is malformed (fewer than 3 words).
    """
    if not line:
        return {}
    parts = line.strip().split()
    if len(parts) < 3:
        return {}
    return {
        'timestamp': parts[0],
        'level':     parts[1].upper(),
        'service':   parts[2],
        'message':   ' '.join(parts[3:]) if len(parts) > 3 else '',
        'raw':       line.strip(),
    }


def parse_logs(lines: List[str]) -> List[Dict]:
    """Parse a list of raw log lines. Silently skip malformed lines."""
    return [p for line in lines if (p := parse_log_line(line))]


def error_lines(parsed: List[Dict]) -> List[Dict]:
    """Return only lines where level == 'ERROR'."""
    return [log for log in parsed if log.get('level') == 'ERROR']


# ── SCORE UTILITIES ───────────────────────────────────────────────────────────

def score_label(score: float, threshold: float = 0.85) -> str:
    """Return 'PASS' if score >= threshold, else 'FAIL'."""
    return 'PASS' if score >= threshold else 'FAIL'


def grade(score: float) -> str:
    """Return A/B/C/D based on score."""
    if score >= 0.90:
        return 'A'
    if score >= 0.80:
        return 'B'
    if score >= 0.70:
        return 'C'
    return 'D'


def normalise_scores(scores: List[float]) -> List[float]:
    """Min-max normalise a list of scores to [0.0, 1.0]."""
    if not scores:
        return []
    lo, hi = min(scores), max(scores)
    if lo == hi:
        return [0.0] * len(scores)
    return [round((s - lo) / (hi - lo), 4) for s in scores]


# ── SELF-TEST ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Running utils self-tests...")

    assert safe_avg([1, 2, 3]) == 2.0
    assert safe_avg([])        == 0.0
    assert safe_max([3, 1, 4]) == 4
    assert safe_max([])        is None

    assert count_by([{'s':'A'},{'s':'B'},{'s':'A'}], 's') == {'A':2,'B':1}
    assert count_by([], 's') == {}

    assert missing_items(['a','b','c'], ['a','c']) == ['b']
    assert added_items(['a','c'], ['a','b','c'])   == ['b']
    assert common_items(['a','b'], ['b','c'])       == ['b']

    assert max_window([1,4,2,9,7,3,8], 3) == 19.0
    assert max_window([], 3)              == 0.0

    assert score_label(0.94) == 'PASS'
    assert score_label(0.61) == 'FAIL'
    assert grade(0.91) == 'A'
    assert grade(0.82) == 'B'

    log = parse_log_line("2024-01-15 ERROR api-1 connection refused")
    assert log['level']   == 'ERROR'
    assert log['service'] == 'api-1'
    assert parse_log_line("") == {}

    print("All utils tests passed ✅")
