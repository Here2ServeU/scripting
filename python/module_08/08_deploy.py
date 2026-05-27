"""
Python for AI & ML Engineers
Module 8: Deployment — Make the Model Real
github.com/Here2ServeU/scripting

A model that is not deployed does not exist.
Three steps: save → wrap → serve.

SETUP:
    pip install fastapi uvicorn scikit-learn joblib numpy

USAGE:
    # Step 1: Train the model (from module_05 or ml_pipeline project)
    python module_05/05_sklearn.py          # saves model_pipeline.pkl

    # Step 2: Run the API
    uvicorn module_08.08_deploy:app --reload

    # Step 3: Open the docs
    # http://localhost:8000/docs

    # Step 4: Make a prediction (curl example)
    curl -X POST http://localhost:8000/predict \\
         -H "Content-Type: application/json" \\
         -d '{"features": [0.1,-0.5,1.2,0.8,-1.1,0.3,0.7,-0.2,1.5,0.4]}'
"""

import os
import joblib
import numpy as np
from datetime import datetime
from typing   import List

# ── STEP 1: SAVE THE PIPELINE ─────────────────────────────────────────────────
# (Already done by module_05/05_sklearn.py — shown here for reference)

def save_example():
    """
    Train a minimal model and save it.
    Run this if model_pipeline.pkl does not exist yet.
    """
    from sklearn.datasets     import make_classification
    from sklearn.pipeline     import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.impute        import SimpleImputer
    from sklearn.ensemble      import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    X, y     = make_classification(n_samples=500, n_features=10, random_state=42)
    X_tr, _, y_tr, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler',  StandardScaler()),
        ('model',   RandomForestClassifier(n_estimators=50, random_state=42)),
    ])
    pipeline.fit(X_tr, y_tr)
    joblib.dump(pipeline, 'model_pipeline.pkl')
    print("model_pipeline.pkl saved.")
    return pipeline


# ── STEP 2: LOAD THE MODEL ────────────────────────────────────────────────────

MODEL_PATH = 'model_pipeline.pkl'

if not os.path.exists(MODEL_PATH):
    print(f"'{MODEL_PATH}' not found — training a quick demo model...")
    pipeline = save_example()
else:
    pipeline = joblib.load(MODEL_PATH)
    print(f"Loaded model from '{MODEL_PATH}'")


# ── STEP 3: BUILD THE API ─────────────────────────────────────────────────────

try:
    from fastapi  import FastAPI, HTTPException
    from pydantic import BaseModel, Field

    class PredictRequest(BaseModel):
        features: List[float] = Field(
            ...,
            description="One feature vector for a single sample",
            example=[0.1, -0.5, 1.2, 0.8, -1.1, 0.3, 0.7, -0.2, 1.5, 0.4]
        )

    class PredictResponse(BaseModel):
        prediction:  int
        confidence:  float
        label:       str
        timestamp:   str

    class BatchRequest(BaseModel):
        samples: List[List[float]] = Field(
            ...,
            description="Multiple feature vectors",
        )

    app = FastAPI(
        title       = "Python for AI & ML Engineers",
        description = "Module 8 — FastAPI deployment of a trained ML pipeline.",
        version     = "1.0.0",
    )

    # ── ROUTES ───────────────────────────────────────────────────────────────

    @app.get("/", tags=["Health"])
    def health():
        """Health check — is the API running?"""
        return {
            "status":    "running",
            "model":     type(pipeline.named_steps.get('model', pipeline)).__name__,
            "timestamp": datetime.utcnow().isoformat(),
        }

    @app.post("/predict", response_model=PredictResponse, tags=["Prediction"])
    def predict(req: PredictRequest):
        """
        Predict the class for a single sample.
        Returns prediction (0/1), confidence, and human-readable label.
        """
        try:
            X    = np.array(req.features).reshape(1, -1)
            pred = int(pipeline.predict(X)[0])
            prob = float(pipeline.predict_proba(X)[0][pred])
            return PredictResponse(
                prediction = pred,
                confidence = round(prob, 4),
                label      = "positive" if pred == 1 else "negative",
                timestamp  = datetime.utcnow().isoformat(),
            )
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))

    @app.post("/batch", tags=["Prediction"])
    def batch_predict(req: BatchRequest):
        """
        Predict classes for multiple samples at once.
        """
        if not req.samples:
            raise HTTPException(status_code=422, detail="samples list is empty")
        try:
            X      = np.array(req.samples)
            preds  = pipeline.predict(X).tolist()
            probas = pipeline.predict_proba(X)
            confs  = [round(float(probas[i][p]), 4) for i, p in enumerate(preds)]
            return {
                "predictions": preds,
                "confidences": confs,
                "count":       len(preds),
                "timestamp":   datetime.utcnow().isoformat(),
            }
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))

    print("\nFastAPI app built successfully.")
    print("Run with: uvicorn module_08.08_deploy:app --reload")
    print("Docs at:  http://localhost:8000/docs\n")

    # ── ENTRY POINT ──────────────────────────────────────────────────────────

    if __name__ == "__main__":
        import uvicorn
        uvicorn.run("08_deploy:app", host="0.0.0.0", port=8000, reload=True)

except ImportError:
    print("\nFastAPI not installed. Run: pip install fastapi uvicorn")
    print("Then re-run this script.")


# ── STEP 4: TEST WITHOUT THE SERVER (DIRECT CALL) ─────────────────────────────
# You can always test the pipeline directly in Python,
# before wrapping it in an API.

def predict_local(features):
    """Make a prediction directly — no server needed."""
    X    = np.array(features).reshape(1, -1)
    pred = int(pipeline.predict(X)[0])
    prob = float(pipeline.predict_proba(X)[0][pred])
    return {'prediction': pred, 'confidence': round(prob, 4)}


sample = [0.1, -0.5, 1.2, 0.8, -1.1, 0.3, 0.7, -0.2, 1.5, 0.4]
result = predict_local(sample)
print(f"Local prediction test: {result}")
