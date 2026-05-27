# T2S: Python for AI & Machine Learning Engineers

> **T2S: Transformed 2 Succeed** — Python Skills for Real Tech Jobs  
> *DevOps · Cloud · SRE · AI/ML Platform Engineering*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![T2S](https://img.shields.io/badge/T2S-Transformed%202%20Succeed-orange)](https://www.emmanuelnaweji.com/ai-course)

---

## About This Repository

This is the official study repo for the **T2S Python for AI & ML Engineers** course taught by  
**Rev. Dr. Emmanuel Naweji** — AI/ML/Robotics practitioner, founder of T2S: Transformed 2 Succeed.

Every script in this repo is referenced directly from the course workbook and video series.  
Clone it once, then open each folder as you work through each lesson.

---

## Course Links

| Resource | Link |
|----------|------|
| 🎥 YouTube Course | [Python for AI & ML Engineers — Free 3-Hour Course](https://www.emmanuelnaweji.com/ai-course) |
| 📚 Course Website | [www.emmanuelnaweji.com/ai-course](https://www.emmanuelnaweji.com/ai-course) |
| 🐦 Follow Dr. Naweji | [@Here2ServeU](https://github.com/Here2ServeU) |

---

## Repository Structure

```
scripting/
└── python/
    ├── 01_counter/             # Pattern 1 — Counting with Counter
    ├── 02_defaultdict/         # Pattern 2 — Grouping with defaultdict
    ├── 03_sorted_lambda/       # Pattern 3 — Sorting with lambda
    ├── 04_sliding_window/      # Pattern 4 — Sliding window algorithms
    ├── 05_set_operations/      # Pattern 5 — Set math
    ├── tests/                  # All 4 practice test solutions (mock1–mock4)
    ├── projects/
    │   ├── log_parser/         # Real-world log parsing project
    │   ├── ml_pipeline/        # End-to-end ML pipeline project
    │   └── deployment/         # FastAPI model deployment project
    ├── utils/                  # Shared helper utilities
    └── lessons/                # Lesson scripts (lesson1–lesson7)
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Here2ServeU/scripting.git
cd scripting/python

# 2. Create a virtual environment (the professional way)
python -m venv venv

# Mac / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run your first script
python 01_counter/count_by_status.py
```

---

## The 5 Patterns

Every Python interview question is one of these patterns in a different outfit.

| # | Pattern | Use When You See |
|---|---------|-----------------|
| 1 | `Counter` | count · how many · most frequent · top K · duplicates |
| 2 | `defaultdict` | group by · for each X collect all Y · average per group |
| 3 | `sorted + lambda` | top K · rank by score · sort by a field · tiebreak |
| 4 | sliding window | K items in a row · highest average over K · windows |
| 5 | set operations | missing · extra · in both · appeared · went away |

---

## Learning Path

| Day | What to Study | Scripts |
|-----|---------------|---------|
| Day 1 | Lessons 1–4 (Variables, Strings, Lists, Dicts) | `lessons/lesson1–4.py` |
| Day 2 | Lessons 5–7 + Patterns 1–5 | `lessons/lesson5–7.py` + all pattern folders |
| Day 3 | Practice Tests 1 & 2 with answers visible | `tests/mock1.py`, `tests/mock2.py` |
| Day 4 | Practice Tests 3 & 4 without looking at answers | `tests/mock3.py`, `tests/mock4.py` |
| Day 5 | Projects — real-world applications | `projects/` |

---

## The Guard Clause — Write This First in Every Function

```python
def my_function(items):
    if not items:  return 0   # or []  or {}  or ''
    # ... rest of your logic
```

This single habit will save you from crashes and earn you easy points on every test.

---

## Author

**Rev. Dr. Emmanuel Naweji**  
AI/ML/Robotics Applied to Highly Regulated Environments  
Years of Experience Working with Top Tech Leading Companies  
Founder and Mentor · T2S: Transformed 2 Succeed · 2026

> *"When you can write all 5 patterns from memory, you are ready."*

---

## License

MIT License — see [LICENSE](LICENSE) for details.
