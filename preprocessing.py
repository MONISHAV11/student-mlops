import pandas as pd
import os
from sklearn.model_selection import train_test_split

def preprocess(df):
    df = df.dropna()

    # Target is final grade G3
    X = df.drop("G3", axis=1)
    y = df["G3"]

    return train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == "__main__":
    df = pd.read_csv("data/raw/student.csv")

    X_train, X_test, y_train, y_test = preprocess(df)

    os.makedirs("data/processed", exist_ok=True)

    X_train.to_csv("data/processed/X_train.csv", index=False)
    X_test.to_csv("data/processed/X_test.csv", index=False)
    y_train.to_csv("data/processed/y_train.csv", index=False)
    y_test.to_csv("data/processed/y_test.csv", index=False)

    print("✅ Preprocessing completed successfully")
