import os
import pandas as pd

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    print("Loaded data shape:", df.shape)
    return df

def save_raw_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print("Saved raw data to:", output_path)

if __name__ == "__main__":
    input_csv = "data/student.csv"   # put your CSV here
    output_csv = "data/raw/student.csv"

    df = load_data(input_csv)
    save_raw_data(df, output_csv)

