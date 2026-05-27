# Project 3: FastAPI Deployment

Deploy your trained ML pipeline as a live REST API.

## Quick Start

```bash
# 1. Train the model first (from the repo root)
cd python/projects/ml_pipeline
python ml_pipeline.py

# 2. Start the API (from the repo root)
cd python/projects/deployment
uvicorn app:app --reload

# 3. Open the interactive docs
# http://localhost:8000/docs
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/model` | Model metadata |
| `POST` | `/predict` | Single prediction |
| `POST` | `/batch` | Batch predictions |

## Example: Single Prediction

```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [0.1, -0.5, 1.2, 0.8, -1.1, 0.3, 0.7, -0.2, 1.5, 0.4]}'
```

Response:
```json
{
  "prediction": 1,
  "confidence": 0.8734,
  "label": "positive",
  "timestamp": "2026-01-15T10:32:00.000000"
}
```

## Next Steps

- Add Docker containerisation
- Deploy to AWS/GCP/Azure
- Add authentication
- Add request logging and monitoring
