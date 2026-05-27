"""
T2S: Python for AI & ML Engineers
Lesson 5: Making Decisions With If Statements
github.com/Here2ServeU/scripting

An if statement lets your code ask a question and do different
things based on the answer.
"""

# ── IF / ELIF / ELSE ──────────────────────────────────────────────────────────
# IMPORTANT:
# ==  means 'is this equal to?' (two equals signs)
#  =  means 'put this value in the box' (one equals sign)

score = 0.61

if score >= 0.85:
    print('PASS')        # runs if score is 0.85 or higher
elif score >= 0.70:
    print('BORDERLINE')  # runs if score is 0.70 to 0.84
else:
    print('FAIL')        # runs if nothing above was true
# Output: FAIL

# ── COMBINING CONDITIONS ─────────────────────────────────────────────────────

# and — BOTH conditions must be true
if score > 0.50 and score < 0.85:
    print('In the middle range')

# or — EITHER condition can be true
if score < 0.50 or score > 0.95:
    print('Unusual result')

# not — flip True to False or False to True
is_running = True
if not is_running:
    print('Pod is down!')
else:
    print('Pod is running')

# ── ONE-LINE IF (TERNARY) ────────────────────────────────────────────────────

result = 'PASS' if score >= 0.85 else 'FAIL'
print(result)   # FAIL

grade = 'A' if score >= 0.90 else 'B' if score >= 0.80 else 'C' if score >= 0.70 else 'D'
print(grade)    # D  (score is 0.61)

# ── COMPARISON OPERATORS ─────────────────────────────────────────────────────
# ==   is equal to
# !=   is NOT equal to
# >    is greater than
# <    is less than
# >=   is greater than or equal to
# <=   is less than or equal to

print(0.94 == 0.94)   # True
print(0.94 != 0.61)   # True
print(0.94 >  0.85)   # True
print(0.61 <  0.85)   # True
print(0.85 >= 0.85)   # True
print(0.61 <= 0.61)   # True

# ── CHECKING TYPES AND EXISTENCE ─────────────────────────────────────────────

value = None

# Check for None
if value is None:
    print('value is empty')

# Check type
x = 42
if isinstance(x, int):
    print('x is an integer')

# Check membership
allowed = {'PASS', 'BORDERLINE', 'FAIL'}
status  = 'PASS'
if status in allowed:
    print(f'{status} is a valid status')

# ── REAL-WORLD PATTERN: CLASSIFY LOG LEVEL ───────────────────────────────────

def classify_log(line):
    if not line:
        return 'UNKNOWN'

    line = line.strip()

    if line.startswith('ERROR') or line.startswith('CRITICAL'):
        return 'HIGH'
    elif line.startswith('WARN'):
        return 'MEDIUM'
    elif line.startswith('INFO') or line.startswith('DEBUG'):
        return 'LOW'
    else:
        return 'UNKNOWN'

print(classify_log('ERROR pod-api crashed'))     # HIGH
print(classify_log('WARN disk usage at 90%'))    # MEDIUM
print(classify_log('INFO service started'))      # LOW
print(classify_log(''))                          # UNKNOWN

# ── PRACTICE ─────────────────────────────────────────────────────────────────
# Try It: score = 0.82
# Print A if score >= 0.90
# Print B if score >= 0.80
# Print C if score >= 0.70
# Print D for anything else

score = 0.82
if score >= 0.90:
    print('A')
elif score >= 0.80:
    print('B')   # 0.82 matches here
elif score >= 0.70:
    print('C')
else:
    print('D')
