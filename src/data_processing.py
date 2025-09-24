# src/data_processing.py

import pandas as pd
import os

def load_data():
    """
    Load the SmartCrop dataset.
    Returns:
        df: pandas DataFrame
    """
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'SmartCrop-Dataset.csv')
    df = pd.read_csv(data_path)
    return df

def check_missing_values(df):
    """
    Check for missing values in the dataset.
    Returns:
        missing_counts: Series with count of missing values per column
    """
    missing_counts = df.isnull().sum()
    return missing_counts

def preprocess_features(df):
    """
    Preprocess dataset features and target.
    Returns:
        X: features DataFrame
        y: target Series
    """
    # Assuming your CSV has columns: N, P, K, temperature, humidity, ph, rainfall, label
    feature_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    target_col = 'label'

    X = df[feature_cols]
    y = df[target_col]

    return X, y

if __name__ == "__main__":
    # Quick test
    df = load_data()
    print("Dataset shape:", df.shape)
    print("Missing values:\n", check_missing_values(df))
    X, y = preprocess_features(df)
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)
