# app/streamlit_app.py

import streamlit as st
import os
import sys

# Add src folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Auto-train model if missing
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'crop_model.pkl')
if not os.path.exists(model_path):
    from model_training import train_and_save_model
    st.info("Training model for the first time, please wait...")
    train_and_save_model()
    st.success("Model training complete!")

# Import predict function after model exists
from predict import predict_crop

st.set_page_config(page_title="Smart Crop Recommendation", page_icon="🌾")

st.title("🌾 Smart Crop Recommendation System")
st.write("Enter your soil and weather parameters to get the best crop recommendation.")

# Input sliders / number inputs
nitrogen = st.slider("Nitrogen (N)", 0, 140, 50)
phosphorus = st.slider("Phosphorus (P)", 0, 140, 50)
potassium = st.slider("Potassium (K)", 0, 140, 50)
temperature = st.slider("Temperature (°C)", 0, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 50)
ph = st.slider("Soil pH", 0.0, 14.0, 6.5, 0.1)
rainfall = st.slider("Rainfall (mm)", 0.0, 300.0, 100.0, 0.1)

# Predict button
if st.button("Recommend Crop"):
    features = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
    
    try:
        recommended_crop = predict_crop(features)
        st.success(f"✅ Recommended Crop: **{recommended_crop}**")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
