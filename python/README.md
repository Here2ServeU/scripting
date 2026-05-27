# Python Scripts — T2S: Python for AI & ML Engineers

All scripts referenced in the T2S course workbook and YouTube series.

## Setup (do once)

```bash
git clone https://github.com/Here2ServeU/scripting.git
cd scripting

python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

---

## Folder Map

| Folder | Content | Course Reference |
|--------|---------|-----------------|
| `lessons/` | `lesson1_variables.py` … `lesson7_counter.py` | Part 1: Lessons 1–7 |
| `01_counter/` | Counter pattern — 5 scripts | Pattern 1 |
| `02_defaultdict/` | defaultdict pattern — 3 scripts | Pattern 2 |
| `03_sorted_lambda/` | sorted + lambda — 3 scripts | Pattern 3 |
| `04_sliding_window/` | sliding window — 3 scripts | Pattern 4 |
| `05_set_operations/` | set operations — 4 scripts | Pattern 5 |
| `tests/` | `mock1.py` … `mock4.py` — all 4 practice tests | Part 3: Practice Tests |
| `module_01/` | Python foundations | Module 1 |
| `module_02/` | NumPy | Module 2 |
| `module_03/` | Pandas | Module 3 |
| `module_04/` | Visualisation | Module 4 |
| `module_05/` | Scikit-learn | Module 5 |
| `module_06/` | Deep learning | Module 6 |
| `module_07/` | NLP & Computer Vision | Module 7 |
| `module_08/` | FastAPI deployment | Module 8 |
| `projects/log_parser/` | Real-world log analysis project | Projects |
| `projects/ml_pipeline/` | End-to-end ML pipeline project | Projects |
| `projects/deployment/` | FastAPI model serving | Projects |
| `utils/` | Shared helper functions | All modules |

---

## Run a Script

```bash
# Always activate the venv first
source venv/bin/activate

# Run any script by path
python lessons/lesson1_variables.py
python 01_counter/count_by_status.py
python tests/mock4.py
python projects/log_parser/log_parser.py

# Run the full ML pipeline
python projects/ml_pipeline/ml_pipeline.py

# Start the deployment API (after running the pipeline to save the model)
uvicorn projects.deployment.app:app --reload
# Open: http://localhost:8000/docs
```

---

## Run All Practice Tests

```bash
python tests/mock1.py
python tests/mock2.py
python tests/mock3.py
python tests/mock4.py
```

If all four complete without errors, you are ready.

---

## The Guard Clause — Write This First in Every Function

```python
def my_function(items):
    if not items:  return 0   # or []  or {}  or ''
```

---

*Rev. Dr. Emmanuel Naweji · T2S: Transformed 2 Succeed · www.emmanuelnaweji.com/ai-course*
