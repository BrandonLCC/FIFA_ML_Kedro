"""
This is a boilerplate pipeline 'classification_prediction'
generated using Kedro 1.0.0
"""

import pandas as pd

def predict_model(model, X_test, column_name: str):
    predictions = model.predict(X_test)
    return pd.DataFrame({column_name: predictions})
