"""
T2S: Python for AI & ML Engineers
Lesson 7: Counter, defaultdict, and Sorting
github.com/Here2ServeU/scripting

These three tools appear in Python tests for tech jobs again and again.
Study them until you can write each one from memory.
"""

# ── COUNTER ───────────────────────────────────────────────────────────────────
# Counter counts how many times each value appears.
# IMPORTANT: This import line must be at the very top of your file.

from collections import Counter, defaultdict

# Basic counting
words  = ['ERROR', 'WARN', 'ERROR', 'INFO', 'ERROR', 'WARN']
counts = Counter(words)

print(counts)                # Counter({'ERROR': 3, 'WARN': 2, 'INFO': 1})
print(counts['ERROR'])       # 3
print(counts['DEBUG'])       # 0  — Counter NEVER crashes on a missing key
print(counts.most_common(2)) # [('ERROR', 3), ('WARN', 2)]  — top 2
print(dict(counts))          # {'ERROR': 3, 'WARN': 2, 'INFO': 1}

# Count characters in a string
letter_counts = Counter('mississippi')
print(letter_counts)            # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(letter_counts.most_common(1))  # [('i', 4)]

# Most common word — full function
def most_common_word(words):
    if not words:
        return ''
    counts = Counter(words)
    return counts.most_common(1)[0][0]

print(most_common_word(['cat', 'dog', 'cat', 'bird', 'dog', 'cat']))   # cat
print(most_common_word([]))                                             # ''

# Count by field from list of dicts
def count_by_status(items, key):
    if not items:
        return {}
    return dict(Counter(item[key] for item in items))

pods = [
    {'name': 'api-1',    'status': 'Running'},
    {'name': 'api-2',    'status': 'Crashed'},
    {'name': 'worker-1', 'status': 'Running'},
    {'name': 'worker-2', 'status': 'Running'},
]
print(count_by_status(pods, 'status'))
# {'Running': 3, 'Crashed': 1}

# ── DEFAULTDICT ───────────────────────────────────────────────────────────────
# defaultdict is like a regular dict, but if you access a key that does not
# exist yet, it creates it automatically instead of crashing.

# defaultdict(int) — new keys start at 0
errors = defaultdict(int)
errors['pod-a'] += 1
errors['pod-a'] += 1
errors['pod-b'] += 1
print(dict(errors))   # {'pod-a': 2, 'pod-b': 1}

# defaultdict(list) — new keys start with an empty list
groups = defaultdict(list)
groups['prod'].append('api-1')
groups['prod'].append('worker-1')
groups['dev'].append('api-2')
print(dict(groups))   # {'prod': ['api-1', 'worker-1'], 'dev': ['api-2']}

# Group items by a field
def group_by(items, key):
    if not items:
        return {}
    groups = defaultdict(list)
    for item in items:
        groups[item[key]].append(item)
    return dict(groups)

runs = [
    {'agent': 'v1', 'score': 0.94},
    {'agent': 'v2', 'score': 0.61},
    {'agent': 'v1', 'score': 0.80},
    {'agent': 'v2', 'score': 0.73},
]
grouped = group_by(runs, 'agent')
for agent, agent_runs in grouped.items():
    scores = [r['score'] for r in agent_runs]
    avg    = sum(scores) / len(scores)
    print(f"{agent}: avg = {avg:.2f}")
# v1: avg = 0.87
# v2: avg = 0.67

# ── SORTED() WITH KEY= ────────────────────────────────────────────────────────
# sorted() can sort by any field using key=lambda.
# A lambda is a tiny function you write in one line.

runs = [
    {'id': 'r1', 'score': 0.94},
    {'id': 'r2', 'score': 0.61},
    {'id': 'r3', 'score': 0.88},
]

# Sort by score, biggest first
by_score = sorted(runs, key=lambda r: r['score'], reverse=True)
print(by_score[0]['id'])   # r1 — r1 has the highest score

# Get top K
k    = 2
top2 = sorted(runs, key=lambda r: r['score'], reverse=True)[:k]
print([r['id'] for r in top2])   # ['r1', 'r3']

# Tiebreak: score descending, then name ascending
agents = [
    {'name': 'beta',  'score': 0.88},
    {'name': 'alpha', 'score': 0.88},
    {'name': 'gamma', 'score': 0.94},
]
ranked = sorted(agents, key=lambda a: (-a['score'], a['name']))
for a in ranked:
    print(f"{a['name']}: {a['score']}")
# gamma: 0.94
# alpha: 0.88  (tiebreak: alpha < beta alphabetically)
# beta:  0.88

# max() with key=
best     = max(runs, key=lambda r: r['score'])
print(best['id'])   # r1

scores_d = {'voice-v1': 0.94, 'voice-v2': 0.61, 'voice-v3': 0.88}
best_key = max(scores_d, key=scores_d.get)
print(best_key)     # voice-v1

# Sort version strings correctly: v1, v2, v10 — NOT v1, v10, v2
versions = ['v10', 'v2', 'v1', 'v20']
natural  = sorted(versions, key=lambda v: int(v[1:]))
print(natural)   # ['v1', 'v2', 'v10', 'v20']

# ── PRACTICE ─────────────────────────────────────────────────────────────────
# Try It: words = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
# Write a function that returns the word appearing the most times.

def most_common(words):
    if not words:
        return ''
    counts = Counter(words)
    return counts.most_common(1)[0][0]

print(most_common(['cat', 'dog', 'cat', 'bird', 'dog', 'cat']))   # cat
