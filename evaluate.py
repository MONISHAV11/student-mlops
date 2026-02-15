import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, r2_score

if __name__ == "__main__":
    X_test = pd.read_csv("data/processed/X_test.csv")
    y_test = pd.read_csv("data/processed/y_test.csv")

    model = joblib.load("models/model.pkl")
    preds = model.predict(X_test)

    print("MAE:", mean_absolute_error(y_test, preds))
    print("R2:", r2_score(y_test, preds))
