import numpy as np
import joblib
import pandas as pd
from datetime import datetime
from pathlib import Path
import os

# Defining the base directory
BASE_DIR = Path(__file__).parent

# Load encoder and scaler 
encoder = joblib.load(BASE_DIR /"encoder.joblib")
scaler = joblib.load(BASE_DIR /"scaler.joblib")

# List of columns in the order the model expects
MODEL_FEATURES = [
    'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest',
    'day_number', 'hour_of_day', 'day_of_week', 'is_night', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']


def preprocess_input(transaction: dict):
    if isinstance(transaction['timestamp'], str):
        ts = pd.to_datetime(transaction['timestamp'])
    else:
        ts = transaction['timestamp']

    day_number = ts.day
    hour_of_day = ts.hour
    day_of_week = ts.weekday()
    is_night = 1 if hour_of_day < 6 else 0

    df = pd.DataFrame([{
        'amount': transaction['amount'],
        'oldbalanceOrg': transaction['oldbalanceOrg'],
        'newbalanceOrig': transaction['newbalanceOrig'],
        'oldbalanceDest': transaction['oldbalanceDest'],
        'newbalanceDest': transaction['newbalanceDest'],
        'day_number': day_number,
        'hour_of_day': hour_of_day,
        'day_of_week': day_of_week,
        'is_night': is_night,
        'type': transaction['type']
    }])

    type_encoded = encoder.transform(df[['type']]).toarray()
    feature_names = encoder.get_feature_names_out(['type'])
    feature_names = [name.split('_', 1)[1] for name in feature_names]
    for i, name in enumerate(feature_names):
        df[name] = type_encoded[0, i]
    df.drop(columns='type', inplace=True)

    cols_to_scale = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest',
                     'day_number', 'hour_of_day', 'day_of_week']
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    df = df.reindex(columns=MODEL_FEATURES, fill_value=0)

    return df.values
