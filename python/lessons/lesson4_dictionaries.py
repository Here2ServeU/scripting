"""
Python for AI & ML Engineers
Lesson 4: Dictionaries
github.com/Here2ServeU/scripting

A dictionary connects a key to a value.
In Python: {'name': 'voice-v2', 'score': 0.94}
Curly braces { } hold everything. Each item is 'key': value.
"""

# ── CREATING AND READING A DICTIONARY ────────────────────────────────────────

result = {'agent': 'voice-v2', 'score': 0.94, 'passed': True}

# Read a value by its key
print(result['score'])           # 0.94

# .get() is the SAFE way to read
# If the key does not exist, it returns a default instead of crashing
print(result.get('cost', 0.0))   # 0.0  — 'cost' not in dict, returns 0.0
print(result.get('score', 0.0))  # 0.94 — 'score' exists, returns its value

# Add a new key or update an existing one
result['status'] = 'done'
result['score']  = 0.96          # update existing key
print(result)

# Check if a key exists
if 'score' in result:
    print('score is there')      # score is there

if 'cost' not in result:
    print('cost is missing')     # cost is missing

# ── LOOPING THROUGH A DICTIONARY ─────────────────────────────────────────────

scores = {'voice-v1': 0.94, 'voice-v2': 0.61, 'voice-v3': 0.88}

# Loop through keys and values together
for agent, score in scores.items():
    print(f'{agent}: {score}')
# voice-v1: 0.94
# voice-v2: 0.61
# voice-v3: 0.88

# Loop through keys only
for agent in scores:
    print(agent)

# Loop through values only
for score in scores.values():
    print(score)

# ── DICTIONARY COMPREHENSION ──────────────────────────────────────────────────

runs   = [{'id': 'r1', 'score': 0.94}, {'id': 'r2', 'score': 0.61}]

# Build a lookup dict from a list
lookup = {run['id']: run['score'] for run in runs}
print(lookup)        # {'r1': 0.94, 'r2': 0.61}
print(lookup['r1'])  # 0.94

# Filter while building
passed = {run['id']: run['score'] for run in runs if run['score'] >= 0.85}
print(passed)        # {'r1': 0.94}

# ── USEFUL PATTERNS ───────────────────────────────────────────────────────────

d = {'a': 10, 'b': 30, 'c': 20}

# Key with the highest value
best = max(d, key=d.get)
print(best)   # b

# Keys sorted by their value (biggest first)
ranked = sorted(d, key=d.get, reverse=True)
print(ranked)   # ['b', 'c', 'a']

# ── NESTED DICTIONARIES ───────────────────────────────────────────────────────

config = {
    'model': {
        'name': 'classifier-v3',
        'layers': 4,
        'dropout': 0.2,
    },
    'training': {
        'epochs': 100,
        'batch_size': 32,
        'learning_rate': 0.001,
    }
}

print(config['model']['name'])             # classifier-v3
print(config['training']['learning_rate']) # 0.001

# Safe read on nested dict
lr = config.get('training', {}).get('learning_rate', 0.01)
print(lr)   # 0.001

# ── PRACTICE ─────────────────────────────────────────────────────────────────
# Try It: d = {'a': 10, 'b': 30, 'c': 20}
# Print the key that has the highest value.

d = {'a': 10, 'b': 30, 'c': 20}
winner = max(d, key=d.get)
print(winner)   # b
