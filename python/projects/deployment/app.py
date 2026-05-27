"""
Python for AI & ML Engineers
Project 3: FastAPI Model Deployment
github.com/Here2ServeU/scripting

Wrap the trained ML pipeline from Project 2 in a live REST API.

SETUP:
    pip install fastapi uvicorn
    python projects/ml_pipeline/ml_pipeline.py   # train and save the model first
    uvicorn projects.deployment.app:app --reload

ENDPOINTS:
    GET  /          — health check
    GET  /model     — model metadata
    POST /predict   — single prediction
    POST /batch     — batch predictions

DEMO (once the server is running):
    curl http://localhost:8000/
    curl http://localhost:8000/model
    curl -X POST http://localhost:8000/predict \
         -H "Content-Type: application/json" \
         -d '{"features": [0.1, -0.5, 1.2, 0.8, -1.1, 0.3, 0.7, -0.2, 1.5, 0.4]}'

Or open the interactive docs at: http://localhost:8000/docs
"""

import os
import joblib
import numpy  as np
from typing     import List
from datetime   import datetime

try:
    from fastapi            import FastAPI, HTTPException
    from fastapi.responses  import JSONResponse
    from pydantic           import BaseModel, Field
except ImportError:
    raise ImportError("Install FastAPI: pip install fastapi uvicorn")


# ── MODEL LOADING ────────────────────────────────────────────────────────────

MODEL_PATH = "model_pipeline.pkl"

def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model not found at '{path}'. "
            "Run ml_pipeline.py first to train and save the model."
        )
    return joblib.load(path)

try:
    model = load_model()
    MODEL_LOADED = True
    print(f"✅ Model loaded from '{MODEL_PATH}'")
except FileNotFoundError as e:
    model = None
    MODEL_LOADED = False
    print(f"⚠️  {e}")


# ── PYDANTIC SCHEMAS ──────────────────────────────────────────────────────────

class PredictRequest(BaseModel):
    features: List[float] = Field(
        ...,
        description="Feature vector for a single sample",
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
        description="List of feature vectors",
        example=[[0.1, -0.5, 1.2, 0.8, -1.1, 0.3, 0.7, -0.2, 1.5, 0.4]]
    )

class BatchResponse(BaseModel):
    predictions: List[int]
    confidences: List[float]
    count:       int
    timestamp:   str


# ── APP ───────────────────────────────────────────────────────────────────────

app = FastAPI(
    title       = "AI Model API",
    description = "Serve predictions from a trained Scikit-learn pipeline.",
    version     = "1.0.0",
)


# ── ROUTES ────────────────────────────────────────────────────────────────────

@app.get("/", tags=["Health"])
def health():
    """Health check endpoint."""
    return {
        "status":       "running",
        "model_loaded": MODEL_LOADED,
        "timestamp":    datetime.utcnow().isoformat(),
    }


@app.get("/model", tags=["Model"])
def model_info():
    """Return metadata about the loaded model."""
    if not MODEL_LOADED:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {
        "model_path":  MODEL_PATH,
        "model_type":  type(model.named_steps.get('model', model)).__name__,
        "status":      "ready",
    }


@app.post("/predict", response_model=PredictResponse, tags=["Prediction"])
def predict(request: PredictRequest):
    """
    Make a single prediction.

    Send a flat list of feature values. Returns:
    - prediction (0 or 1)
    - confidence (probability of the predicted class)
    - label (human-readable)
    """
    if not MODEL_LOADED:
        raise HTTPException(status_code=503, detail="Model not loaded")

    try:
        X    = np.array(request.features).reshape(1, -1)
        pred = int(model.predict(X)[0])
        prob = float(model.predict_proba(X)[0][pred])
        return PredictResponse(
            prediction = pred,
            confidence = round(prob, 4),
            label      = "positive" if pred == 1 else "negative",
            timestamp  = datetime.utcnow().isoformat(),
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Prediction error: {e}")


@app.post("/batch", response_model=BatchResponse, tags=["Prediction"])
def batch_predict(request: BatchRequest):
    """
    Make predictions for multiple samples at once.
    """
    if not MODEL_LOADED:
        raise HTTPException(status_code=503, detail="Model not loaded")
    if not request.samples:
        raise HTTPException(status_code=422, detail="samples list is empty")

    try:
        X       = np.array(request.samples)
        preds   = model.predict(X).tolist()
        proba   = model.predict_proba(X)
        confs   = [round(float(proba[i][p]), 4) for i, p in enumerate(preds)]
        return BatchResponse(
            predictions = preds,
            confidences = confs,
            count       = len(preds),
            timestamp   = datetime.utcnow().isoformat(),
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Batch prediction error: {e}")


# ── ENTRY POINT ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    print("\nStarting AI Model API...")
    print("Docs available at: http://localhost:8000/docs\n")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
