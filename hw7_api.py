import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

model = joblib.load("joblib_pickle")

app = FastAPI()

@app.post("/predict")
def predict(data: dict[str, float]):
    try:
        features = pd.DataFrame([data])
        prediction = model.predict(features)
        return {"prediction": prediction.tolist()}
    except Exception as exc:
        raise HTTPException(status_code=422, detail=str(exc))


