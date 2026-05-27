# Projects

Three real-world projects that tie all course patterns and modules together.

## Project 1 — Log Parser

**File:** `log_parser/log_parser.py`  
**Patterns used:** Counter · defaultdict · sorted/lambda · set operations

Parses a stream of structured log lines and produces a full analysis report:
error counts per service, lines grouped by level, top error services, and new error types vs a baseline.

```bash
python projects/log_parser/log_parser.py
```

---

## Project 2 — End-to-End ML Pipeline

**File:** `ml_pipeline/ml_pipeline.py`  
**Modules used:** Pandas · Scikit-learn (Pipeline · cross-validation · joblib)

Covers the full workflow:
load → inspect → clean → split → train → cross-validate → evaluate → save.

```bash
python projects/ml_pipeline/ml_pipeline.py
# Outputs: model_pipeline.pkl
```

---

## Project 3 — FastAPI Deployment

**File:** `deployment/app.py`  
**Modules used:** FastAPI · joblib · NumPy

Wraps the saved model in a live REST API with health check, single prediction, and batch prediction endpoints.

```bash
# Train the model first (Project 2)
python projects/ml_pipeline/ml_pipeline.py

# Start the API
uvicorn projects.deployment.app:app --reload

# Open docs
# http://localhost:8000/docs
```

---

## Suggested Order

1. Run Project 1 — practice all 5 patterns together
2. Run Project 2 — build the full ML pipeline
3. Run Project 3 — deploy the model as a live API

These three projects are portfolio pieces. Push them to your GitHub and link them in your resume.
