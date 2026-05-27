# Pattern 04: Sliding Window

**Use this pattern when the question says:**

`k items in a row` · `window of k` · `highest average over k` · `count windows above a limit`

## One-Line Reminder

```python
window = sum(nums[:k])  ->  window += nums[i] - nums[i-k]  ->  best = max(best, window)
```

## Scripts in This Folder

| File | What It Teaches |
|------|----------------|
| `max_window_sum.py` | Highest sum of any K consecutive items |
| `max_window_average.py` | Highest average of any K consecutive items |
| `count_windows_above.py` | How many windows have sum/avg above a threshold |

## Study Order

1. Read `max_window_sum.py` — understand the slide step
2. Read `max_window_average.py` — divide by k at the end
3. Read `count_windows_above.py` — count instead of track best
4. Write each from memory without looking
