"""
Python for AI & ML Engineers
Practice Test 1: Strings and Counting
github.com/Here2ServeU/scripting

Timer: 70 minutes  ·  4 questions
Try each question yourself first. Write your code before looking at the answer.
For each question, ask: which of the 5 patterns does this match?
"""

from collections import Counter


# ── Q1: Count ERROR Lines ─────────────────────────────────────────────────────
# Pattern: parse text (startswith)
# EASY

def count_errors(logs):
    """
    Return how many log lines start with 'ERROR'.

    Examples:
        >>> count_errors(['ERROR pod crashed', 'INFO started', 'ERROR oom', 'WARN slow'])
        2
        >>> count_errors([])
        0
    """
    if not logs:
        return 0
    return sum(1 for line in logs if line.startswith('ERROR'))


# ── Q2: First Word ────────────────────────────────────────────────────────────
# Pattern: parse text (strip + split)
# EASY

def first_word(sentence):
    """
    Return the first word of the sentence.
    If the string is empty or all spaces, return ''.

    Examples:
        >>> first_word('hello world today')
        'hello'
        >>> first_word('   spaces before')
        'spaces'
        >>> first_word('')
        ''
    """
    clean = sentence.strip()
    if not clean:
        return ''
    return clean.split()[0]


# ── Q3: Most Frequent Character ───────────────────────────────────────────────
# Pattern 1: Counter + sorted tiebreak
# MEDIUM

def most_frequent_char(s):
    """
    Return the character that appears most often.
    On a tie, return the one that comes first alphabetically.
    Return '' if the input is empty.

    Examples:
        >>> most_frequent_char('mississippi')
        'i'
        >>> most_frequent_char('aabb')
        'a'
        >>> most_frequent_char('')
        ''
    """
    if not s:
        return ''
    counts = Counter(s)
    # sorted(counts) puts keys alphabetically first.
    # max then picks the highest count.
    # Alphabetical order wins on a tie.
    return max(sorted(counts), key=counts.get)


# ── Q4: Reverse the Words ─────────────────────────────────────────────────────
# Pattern: parse text (split + reverse + join)
# MEDIUM

def reverse_words(sentence):
    """
    Return the sentence with words in reverse order.
    Extra spaces between words must be removed.

    Examples:
        >>> reverse_words('hello world')
        'world hello'
        >>> reverse_words('  the sky   is blue  ')
        'blue is sky the'
        >>> reverse_words('')
        ''
    """
    words = sentence.split()   # split() handles all extra spaces automatically
    if not words:
        return ''
    return ' '.join(words[::-1])


# ── TEST RUNNER ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 50)
    print("Practice Test 1: Strings and Counting")
    print("=" * 50)

    print("\nQ1: count_errors")
    assert count_errors(['ERROR pod crashed', 'INFO started', 'ERROR oom', 'WARN slow']) == 2
    assert count_errors([]) == 0
    assert count_errors(['INFO only', 'WARN only']) == 0
    assert count_errors(['ERROR alone']) == 1
    print("  All Q1 tests passed ✓")

    print("\nQ2: first_word")
    assert first_word('hello world today') == 'hello'
    assert first_word('   spaces before')  == 'spaces'
    assert first_word('') == ''
    assert first_word('   ') == ''
    assert first_word('single') == 'single'
    print("  All Q2 tests passed ✓")

    print("\nQ3: most_frequent_char")
    assert most_frequent_char('mississippi') == 'i'
    assert most_frequent_char('aabb')        == 'a'
    assert most_frequent_char('')            == ''
    assert most_frequent_char('z')           == 'z'
    print("  All Q3 tests passed ✓")

    print("\nQ4: reverse_words")
    assert reverse_words('hello world')           == 'world hello'
    assert reverse_words('  the sky   is blue  ') == 'blue is sky the'
    assert reverse_words('')                       == ''
    assert reverse_words('   ')                    == ''
    assert reverse_words('single')                 == 'single'
    print("  All Q4 tests passed ✓")

    print("\n✅  All Practice Test 1 tests passed!")
