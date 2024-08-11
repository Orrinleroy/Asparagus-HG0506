import joblib
import numpy as np
import pandas as pd
from config import Config

# Load the trained model from the file
model = joblib.load(Config.FRAUD_MODEL_PATH)

def preprocess_input(data):
    df = pd.DataFrame([data])
    return df  # Return the processed data

def predict_fraud(data):
    processed_data = preprocess_input(data)
    prediction = model.predict(processed_data)
    probability = model.predict_proba(processed_data)
    return prediction[0], probability[0][1]  # Return the prediction and probability of fraud
