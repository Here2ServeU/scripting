# Pattern 02: defaultdict

**Use this pattern when the question says:**

`group by` · `for each X collect all Y` · `average per group` · `agents below a limit` · `put into buckets`

## One-Line Reminder

```python
defaultdict(list) -> groups[item['field']].append(item) -> return dict(groups)
```

## Scripts in This Folder

| File | What It Teaches |
|------|----------------|
| `group_by.py` | Group items into buckets by a field |
| `average_per_group.py` | Compute average score for each group |
| `agents_below_threshold.py` | Find agents whose average falls below a cutoff |

## Study Order

1. Read `group_by.py` — the foundational pattern
2. Read `average_per_group.py` — adding a calculation step
3. Read `agents_below_threshold.py` — filter after grouping
4. Write each from memory without looking
