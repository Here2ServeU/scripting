# Pattern 01: Counter

**Use this pattern when the question says:**

`count` · `how many` · `most frequent` · `top K by frequency` · `duplicates`

## One-Line Reminder

```python
Counter(items) -> .most_common(k) -> filter count > 1
```

## Scripts in This Folder

| File | What It Teaches |
|------|----------------|
| `count_by_status.py` | Count items by a field key |
| `most_common.py` | Find the most frequent item |
| `top_k_frequency.py` | Return the top K most frequent items |
| `count_per_agent.py` | Count occurrences per agent across runs |
| `find_duplicates.py` | Find items that appear more than once |

## Study Order

1. Read `count_by_status.py` — the simplest form
2. Read `most_common.py` — adding the tiebreak
3. Read `top_k_frequency.py` — slicing the top K
4. Read `count_per_agent.py` — applying to dicts
5. Read `find_duplicates.py` — filtering count > 1
6. Write each one from memory without looking
