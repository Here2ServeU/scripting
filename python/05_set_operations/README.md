# Pattern 05: Set Operations

**Use this pattern when the question says:**

`missing` · `extra` · `added` · `in both lists` · `appeared` · `went away` · `remove duplicates`

## One-Line Reminder

```python
set(a) - set(b)  ->  missing   |   set(a) & set(b)  ->  in both
```

## Scripts in This Folder

| File | What It Teaches |
|------|----------------|
| `find_missing.py` | Items in A but not in B |
| `find_added.py` | Items in B but not in A |
| `find_common.py` | Items in both A and B |
| `pod_diff.py` | Real-world pod change detection |

## Set Operation Reference

```python
set(a) - set(b)    # items in a but NOT in b   (missing / removed)
set(a) & set(b)    # items in BOTH a and b      (intersection)
set(a) | set(b)    # items in EITHER a or b     (union)
set(a) ^ set(b)    # items in one but NOT both  (symmetric difference)
```

## Study Order

1. Read `find_missing.py` and `find_added.py` — the two most common variants
2. Read `find_common.py` — intersection
3. Read `pod_diff.py` — full real-world application
4. Write each from memory without looking
