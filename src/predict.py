# src/predict.py

import os
import pickle
import numpy as np

# Load trained model and label encoder
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'crop_model.pkl')

with open(model_path, 'rb') as f:
    saved = pickle.load(f)

model = saved['model']
label_encoder = saved['label_encoder']

def predict_crop(features):
    """
    Predict the best crop based on input features.

    Args:
        features (list or array): [N, P, K, temperature, humidity, ph, rainfall]

    Returns:
        str: Predicted crop name
    """
    features = np.array(features).reshape(1, -1)  # reshape for single sample
    pred_encoded = model.predict(features)[0]     # get encoded label
    crop_name = label_encoder.inverse_transform([pred_encoded])[0]  # decode label
    return crop_name

# Quick test
if __name__ == "__main__":
    test_features = [90, 42, 43, 20, 80, 6.5, 200]
    print("Predicted Crop:", predict_crop(test_features))
