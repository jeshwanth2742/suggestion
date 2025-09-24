# src/model_training.py

import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from data_processing import load_data, preprocess_features

def train_and_save_model():
    # Load and preprocess dataset
    df = load_data()
    X, y = preprocess_features(df)

    # Encode target labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    # Train Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model and label encoder together
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'crop_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump({'model': model, 'label_encoder': le}, f)

    # Print accuracy on test set
    accuracy = model.score(X_test, y_test)
    print(f"✅ Model trained and saved at {model_path}")
    print(f"Test Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    train_and_save_model()


