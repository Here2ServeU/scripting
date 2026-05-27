"""
Python for AI & ML Engineers
Lesson 3: Lists
github.com/Here2ServeU/scripting

A list holds many values inside one variable.
Lists use square brackets [ ] with commas between each item.
The first item is number 0, not number 1.
"""

# ── CREATING AND USING A LIST ────────────────────────────────────────────────

scores = [0.94, 0.61, 0.88, 0.45]
#          [0]   [1]   [2]   [3]

print(scores[0])    # 0.94  — first item
print(scores[-1])   # 0.45  — last item
print(len(scores))  # 4     — number of items

# Modifying a list
scores.append(0.92)          # add 0.92 to the end
print(scores)                # [0.94, 0.61, 0.88, 0.45, 0.92]

scores.remove(0.61)          # remove the value 0.61
print(scores)                # [0.94, 0.88, 0.45, 0.92]

# Sorting
scores.sort()                # changes the original, smallest first
print(scores)                # [0.45, 0.88, 0.92, 0.94]

scores.sort(reverse=True)    # changes the original, biggest first
print(scores)                # [0.94, 0.92, 0.88, 0.45]

# sorted() makes a COPY — the original is not changed
original = [0.94, 0.61, 0.88]
copy     = sorted(original)
print(original)   # [0.94, 0.61, 0.88]  — unchanged
print(copy)       # [0.61, 0.88, 0.94]  — sorted copy

# ── FOR LOOP ─────────────────────────────────────────────────────────────────
# A for loop reads every item in the list one by one.
# The 4 spaces before print are required.

names = ['api', 'worker', 'database']
for name in names:
    print(name)
# Output:
# api
# worker
# database

# Loop with index
for i, name in enumerate(names):
    print(f"{i}: {name}")
# 0: api
# 1: worker
# 2: database

# ── LIST COMPREHENSION ───────────────────────────────────────────────────────
# A shorter way to filter or transform a list in one line.

scores = [0.94, 0.61, 0.88, 0.45, 0.92]

# Keep only scores above 0.80
high = [s for s in scores if s > 0.80]
print(high)    # [0.94, 0.88, 0.92]

# Transform: multiply every score by 100
pct = [round(s * 100, 1) for s in scores]
print(pct)     # [94.0, 61.0, 88.0, 45.0, 92.0]

# Count how many scores are above 0.80
count = sum(1 for s in scores if s > 0.80)
print(count)   # 3

# Find the FIRST score below 0.70  (or None if no match)
first_low = next((s for s in scores if s < 0.70), None)
print(first_low)   # 0.61

# ── BUILT-IN FUNCTIONS ───────────────────────────────────────────────────────

nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(sum(nums))           # 31  — add all numbers
print(max(nums))           # 9   — biggest
print(min(nums))           # 1   — smallest
print(sorted(nums))        # [1, 1, 2, 3, 4, 5, 6, 9]  — sorted copy
print(list(set(nums)))     # unique values only, no duplicates

# ── PRACTICE ─────────────────────────────────────────────────────────────────
# Try It: scores = [0.94, 0.61, 0.88, 0.45, 0.92]
# Return a sorted list of only the scores above 0.80. Put the biggest first.

scores = [0.94, 0.61, 0.88, 0.45, 0.92]
high   = [s for s in scores if s > 0.80]
result = sorted(high, reverse=True)
print(result)   # [0.94, 0.92, 0.88]
