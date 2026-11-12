# hw7-cfds: Diabetes prediction API

A FastAPI service that serves a Random Forest model (trained in hw4) to predict
`diabetes_mellitus` from 10 patient features.

## Files

| File | Description |
|---|---|
| `hw7_api.py` | API with a `POST /predict` endpoint |
| `hw7_request.py` | Client that sends `input_example.json` to the API and prints the result |
| `model.joblib` | Trained `RandomForestClassifier` (serialized with `joblib.dump()`) |
| `input_example.json` | Example input with the 10 features the model needs |

## How to run

```bash
uv sync                                   # install dependencies
uv run uvicorn hw7_api:app --reload       # terminal 1: start the API on localhost:8000
uv run python hw7_request.py              # terminal 2: send the example request
```

Expected output:

```
Prediction: 1
Probability of diabetes: 0.52
```

Interactive docs are available at http://localhost:8000/docs.

## Input

`age`, `height` and `weight` must be positive numbers. `aids`, `cirrhosis`,
`hepatic_failure`, `immunosuppression`, `leukemia`, `lymphoma` and
`solid_tumor_with_metastasis` must be 0 or 1. Invalid input returns `422`.
