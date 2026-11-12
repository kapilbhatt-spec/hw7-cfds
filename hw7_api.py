from pathlib import Path
from typing import Annotated

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"

model = joblib.load(MODEL_PATH)

Binary = Annotated[int, Field(ge=0, le=1)]


class Patient(BaseModel):
    model_config = ConfigDict(extra="forbid")

    age: float = Field(gt=0)
    height: float = Field(gt=0)
    weight: float = Field(gt=0)
    aids: Binary
    cirrhosis: Binary
    hepatic_failure: Binary
    immunosuppression: Binary
    leukemia: Binary
    lymphoma: Binary
    solid_tumor_with_metastasis: Binary


app = FastAPI()


@app.post("/predict")
def predict(patient: Patient):
    features = pd.DataFrame([patient.model_dump()])
    features = features[model.feature_names_in_]
    try:
        prediction = model.predict(features)
    except ValueError as exc:
        raise HTTPException(
            status_code=500, detail=f"Model prediction failed: {exc}"
        ) from exc
    return {"prediction": prediction.tolist()}
