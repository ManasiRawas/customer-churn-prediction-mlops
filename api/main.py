from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

try:
    model = pickle.load(open("models/churn_model.pkl", "rb"))
except:
    model = None

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def predict(data: dict):
    if model is None:
        return {"error": "Model not trained yet"}

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    return {"prediction": int(prediction)}
