"""
T2S: Python for AI & ML Engineers
Lesson 6: Functions
github.com/Here2ServeU/scripting

A function is a recipe you write once and use as many times as you want.
def    — I am about to define a new function
()     — holds the inputs the function needs
return — sends the answer back to whoever called the function
"""

# ── BASIC FUNCTION ────────────────────────────────────────────────────────────

def check_score(score):
    if score >= 0.85:
        return 'PASS'
    else:
        return 'FAIL'

print(check_score(0.94))   # PASS
print(check_score(0.61))   # FAIL
print(check_score(0.85))   # PASS

# ── MULTIPLE INPUTS ───────────────────────────────────────────────────────────

def grade_agent(name, score):
    status = 'PASS' if score >= 0.85 else 'FAIL'
    return f'{name}: {status}'

print(grade_agent('voice-v2', 0.94))   # voice-v2: PASS
print(grade_agent('voice-v3', 0.61))   # voice-v3: FAIL

# ── DEFAULT VALUES ────────────────────────────────────────────────────────────
# Give an input a default value.
# If the caller does not provide one, Python uses the default.

def check(score, threshold=0.85):
    return score >= threshold

print(check(0.94))           # True  — uses default 0.85
print(check(0.94, 0.95))     # False — uses custom 0.95
print(check(0.80, 0.75))     # True  — uses custom 0.75

# ── THE GUARD CLAUSE — WRITE THIS FIRST IN EVERY FUNCTION ────────────────────
# Every function must check for an empty input at the top.
# Python tests ALWAYS include an empty case.
# Handle it and you get those points for free.

def sum_scores(scores):
    if not scores:       # if the list is empty, handle it right away
        return 0
    return sum(scores)

print(sum_scores([]))          # 0
print(sum_scores([1, 2, 3]))   # 6

def most_common_level(logs):
    if not logs:
        return ''
    from collections import Counter
    counts = Counter(logs)
    return counts.most_common(1)[0][0]

print(most_common_level([]))                               # ''
print(most_common_level(['ERROR','WARN','ERROR','INFO']))   # ERROR

# ── RETURN MULTIPLE VALUES ────────────────────────────────────────────────────

def score_summary(scores):
    if not scores:
        return 0, 0, 0.0
    return len(scores), max(scores), sum(scores) / len(scores)

count, best, avg = score_summary([0.94, 0.61, 0.88])
print(f"Count: {count}, Best: {best}, Avg: {avg:.2f}")
# Count: 3, Best: 0.94, Avg: 0.81

# ── FUNCTIONS AS ARGUMENTS (HIGHER-ORDER) ─────────────────────────────────────

def apply_threshold(scores, threshold, action):
    """Apply a function to every score that passes the threshold."""
    return [action(s) for s in scores if s >= threshold]

def to_percent(score):
    return round(score * 100, 1)

scores  = [0.94, 0.61, 0.88, 0.45, 0.92]
results = apply_threshold(scores, 0.85, to_percent)
print(results)   # [94.0, 88.0, 92.0]

# ── REAL-WORLD PATTERN: PIPELINE STEP ────────────────────────────────────────

def parse_log_line(line):
    """Parse a structured log line into its components."""
    if not line:
        return {}

    parts = line.strip().split()
    if len(parts) < 3:
        return {}

    return {
        'timestamp': parts[0],
        'level':     parts[1],
        'service':   parts[2],
        'message':   ' '.join(parts[3:]) if len(parts) > 3 else '',
    }

line   = "2024-01-15 ERROR everse-api request timeout after 30s"
parsed = parse_log_line(line)
print(parsed)
# {'timestamp': '2024-01-15', 'level': 'ERROR', 'service': 'everse-api', 'message': 'request timeout after 30s'}

print(parse_log_line(""))   # {}

# ── PRACTICE ─────────────────────────────────────────────────────────────────
# Try It: Write a function called highest that takes a list of numbers
# and returns the biggest one. If the list is empty, return 0.

def highest(numbers):
    if not numbers:
        return 0
    return max(numbers)

print(highest([3, 7, 2, 9, 1]))   # 9
print(highest([]))                 # 0
