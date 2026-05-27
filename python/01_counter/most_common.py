"""
Pattern 01 — Counter
most_common.py

Find the most frequent item. Handle alphabetical tiebreak.
T2S: Python for AI & ML Engineers
"""

from collections import Counter


def most_common_word(words):
    """
    Return the word that appears the most times.
    If the input is empty, return ''.

    Examples:
        >>> most_common_word(['cat', 'dog', 'cat', 'bird', 'dog', 'cat'])
        'cat'
        >>> most_common_word([])
        ''
    """
    if not words:
        return ''
    counts = Counter(words)
    return counts.most_common(1)[0][0]


def most_frequent_char(s):
    """
    Return the character that appears the most times.
    On a tie, return the character that comes first alphabetically.
    Return '' if the string is empty.

    Examples:
        >>> most_frequent_char('mississippi')
        'i'
        >>> most_frequent_char('aabb')
        'a'
    """
    if not s:
        return ''
    counts = Counter(s)
    # sorted(counts) puts keys in alphabetical order first.
    # max then picks the one with the highest count.
    # If two have the same count, alphabetical order wins.
    return max(sorted(counts), key=counts.get)


def most_common_log_level(logs):
    """
    Given a list of log lines, return the most frequent log level.
    Each line starts with a level word (ERROR, WARN, INFO, DEBUG).

    Examples:
        >>> most_common_log_level(['ERROR pod crashed', 'WARN slow', 'ERROR oom'])
        'ERROR'
        >>> most_common_log_level([])
        ''
    """
    if not logs:
        return ''
    levels = [line.split()[0] for line in logs if line.strip()]
    if not levels:
        return ''
    counts = Counter(levels)
    return counts.most_common(1)[0][0]


# ── DEMO ─────────────────────────────────────────────────────────────────────

words = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
print(most_common_word(words))   # cat
print(most_common_word([]))      # ''

print(most_frequent_char('mississippi'))  # i  (appears 4 times)
print(most_frequent_char('aabb'))         # a  (tied at 2, 'a' < 'b')
print(most_frequent_char(''))             # ''

logs = [
    'ERROR pod-api crashed',
    'INFO  service started',
    'ERROR oom killed',
    'WARN  disk usage high',
    'ERROR timeout',
]
print(most_common_log_level(logs))   # ERROR
print(most_common_log_level([]))     # ''
