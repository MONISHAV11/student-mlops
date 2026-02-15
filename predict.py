import joblib
import pandas as pd

def predict(input_dict):
    model = joblib.load("models/model.pkl")
    df = pd.DataFrame([input_dict])
    pred = model.predict(df)
    return float(pred[0])
