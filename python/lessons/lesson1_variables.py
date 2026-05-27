"""
T2S: Python for AI & ML Engineers
Lesson 1: Variables
github.com/Here2ServeU/scripting

A variable is like a labeled box.
You pick a name for the box. Then you put a value inside it.
The = sign means: put this value into this box.
"""

# ── DATA TYPES ──────────────────────────────────────────────────────────────

# Text  — always goes inside quotes
name    = "Emmanuel"

# Whole number — no quotes needed
age     = 35

# Decimal number — no quotes needed
score   = 0.94

# True or False — capital T or F, no quotes
running = True

print(name)     # Emmanuel
print(age)      # 35
print(score)    # 0.94
print(running)  # True

# ── MATH WITH VARIABLES ─────────────────────────────────────────────────────

total   = 10
failed  = 3
healthy = total - failed    # 10 - 3 = 7
double  = total * 2         # 10 * 2 = 20
half    = total / 2         # 10 / 2 = 5.0
percent = (healthy / total) * 100  # 70.0

print(healthy)   # 7
print(double)    # 20
print(half)      # 5.0
print(percent)   # 70.0

# ── F-STRINGS: PUT A VARIABLE INSIDE A SENTENCE ─────────────────────────────
# Put the letter f right before your quote.
# Then put the variable name inside { }.

agent_name = "voice-v2"
agent_score = 0.94

print(f"Agent {agent_name} scored {agent_score}")
# Output: Agent voice-v2 scored 0.94

pods = 10
print(f"We have {pods} pods running.")
# Output: We have 10 pods running.

# Round a decimal inside an f-string
print(f"Score: {agent_score:.2f}")   # Score: 0.94
print(f"Score: {agent_score:.0%}")   # Score: 94%

# ── PRACTICE ────────────────────────────────────────────────────────────────
# Try It: Create three variables — name='Alex', score=0.88, pods=50
# Print: Alex: 50 pods, score 0.88

name  = 'Alex'
score = 0.88
pods  = 50
print(f"{name}: {pods} pods, score {score}")
# Output: Alex: 50 pods, score 0.88
