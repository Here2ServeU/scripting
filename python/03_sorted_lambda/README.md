# Pattern 03: sorted + lambda

**Use this pattern when the question says:**

`top K` · `best K` · `rank by score` · `sort by a field` · `alphabetical tiebreak`

## One-Line Reminder

```python
sorted(items, key=lambda x: (-x['score'], x['name']))[:k]
```

## Scripts in This Folder

| File | What It Teaches |
|------|----------------|
| `top_k_by_score.py` | Return the top K items by a score field |
| `rank_with_tiebreak.py` | Sort with secondary (alphabetical) tiebreak |
| `sort_versions.py` | Sort version strings in natural order |

## Study Order

1. Read `top_k_by_score.py` — basic sorted() with key
2. Read `rank_with_tiebreak.py` — tuple key for tiebreak
3. Read `sort_versions.py` — lambda with type conversion
4. Write each from memory without looking
