"""
Python for AI & ML Engineers
Lesson 2: Working With Text (Strings)
github.com/Here2ServeU/scripting

A string is any text you put inside quotes.
Log messages, names, job statuses, and IDs are all strings.
"""

# ── STRING METHODS ───────────────────────────────────────────────────────────

text = "  ERROR pod-api crashed  "

# .strip()  removes extra spaces from both ends
clean = text.strip()
print(clean)              # 'ERROR pod-api crashed'

# .split()  breaks the text into a list of words
words = clean.split()
print(words)              # ['ERROR', 'pod-api', 'crashed']
print(words[0])           # 'ERROR'

# .split(char)  breaks at a specific character
pod   = "everse-api-7d9f-abc"
parts = pod.split('-')
print(parts)              # ['everse', 'api', '7d9f', 'abc']

# .startswith() and .endswith()
print(clean.startswith('ERROR'))    # True
print(clean.startswith('INFO'))     # False
print(clean.endswith('crashed'))    # True

# .upper() and .lower()
print('hello'.upper())    # HELLO
print('HELLO'.lower())    # hello

# len()  — number of characters
print(len('hello'))       # 5

# in  — check if a word exists inside the text
print('ERROR' in clean)   # True
print('WARN'  in clean)   # False

# .replace()  — swap one word for another
print('hello world'.replace('world', 'Python'))   # hello Python

# .join()  — glue a list back into one string
print('-'.join(['a', 'b', 'c']))    # a-b-c
print(' '.join(['hello', 'world'])) # hello world

# ── SLICING ──────────────────────────────────────────────────────────────────
# Every character has a position number starting at 0.

text = "ABCDEF"
#        012345

print(text[0])     # A   — first character
print(text[-1])    # F   — last character
print(text[0:3])   # ABC — positions 0, 1, 2  (3 is excluded)
print(text[2:])    # CDEF — from position 2 to the end
print(text[::-1])  # FEDCBA — reversed

# ── REAL-WORLD PATTERN: PARSE A LOG LINE ─────────────────────────────────────
# strip() then split() — you will use this in every log-parsing question.

log = "  2024-01-15 ERROR everse-api request timeout  "

parts     = log.strip().split()
timestamp = parts[0]    # '2024-01-15'
level     = parts[1]    # 'ERROR'
service   = parts[2]    # 'everse-api'
message   = ' '.join(parts[3:])  # 'request timeout'

print(f"Level: {level} | Service: {service} | Message: {message}")

# ── PRACTICE ─────────────────────────────────────────────────────────────────
# Try It: You have log = '  WARN disk-usage high  '
# Print just the first word, in ALL CAPITAL LETTERS.

log   = '  WARN disk-usage high  '
clean = log.strip()
words = clean.split()
first = words[0]
print(first.upper())   # WARN
