from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load model (will work after we train it)
try:
    model = pickle.load(open("models/churn_model.pkl", "rb"))
except:
    model = None

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    if model is None:
        return {"error": "Model not trained yet"}

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    return {"prediction": int(prediction)}
