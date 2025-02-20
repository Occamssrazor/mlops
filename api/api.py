import subprocess

import joblib
import uvicorn
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

def load_model():
    subprocess.run(["dvc", "pull", "mlflow/boosting_model.pkl.dvc"], check=True)

    with open("mlflow/boosting_model.pkl", 'rb') as file:
        model = joblib.load(file)
        return model

model = load_model()
class ModelRequestData(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

class Result(BaseModel):
    result: float

@app.get("/")
def root():
    return {"message": "Wine quality model. Let's get started"}

@app.get("/health")
def health():
    return JSONResponse(content={"message": "It's alive!"}, status_code=200)

@app.get("/model-info")
def model_info():
    return f"model_type: {str(type(model))}, model_params: {model.get_params()}"

@app.post("/predict", response_model=Result)
def predict(data: ModelRequestData):
    input_data = data.model_dump()

    input_data = {
        "fixed acidity": input_data["fixed_acidity"],
        "volatile acidity": input_data["volatile_acidity"],
        "citric acid": input_data["citric_acid"],
        "residual sugar": input_data["residual_sugar"],
        "chlorides": input_data["chlorides"],
        "free sulfur dioxide": input_data["free_sulfur_dioxide"],
        "total sulfur dioxide": input_data["total_sulfur_dioxide"],
        "density": input_data["density"],
        "pH": input_data["pH"],
        "sulphates": input_data["sulphates"],
        "alcohol": input_data["alcohol"]
    }

    input_df = pd.DataFrame([input_data])
    result = model.predict(input_df)
    return Result(result=result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

