import joblib
from fastapi import FastAPI, HTTPException
import numpy as np
from src.base_model import TransactionInput
from src.inference import preprocess_input
import os

model = joblib.load('model/fraud_detection_model.joblib')
app = FastAPI() 

@app.post("/fraud-detection-model")
async def check_transaction_input(data: TransactionInput):
    try:
        # Convert pydantic model to dictionary
        transaction_dict = data.dict()

        # Preprocess input
        features = preprocess_input(transaction_dict)

        # Predict
        result = model.predict(features)
        status = "Not Fraudulent" if result[0] == 0 else "Fraudulent"

        return {
            "Prediction": int(result[0]),
            "Result": status
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating prediction: {str(e)}")
