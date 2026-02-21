"""
This is a boilerplate pipeline 'regresssion_prediction'
generated using Kedro 1.0.0
"""

import pandas as pd
from kedro.pipeline import node, Pipeline

# Función para hacer predicciones con el modelo entrenado
# Solo una funcion de predicción, ya que se pueden comparar los resultados de los diferentes modelos entrenados en la etapa anterior.
def predict_model(model, X_test, column_name: str):
    predictions = model.predict(X_test)
    return pd.DataFrame({column_name: predictions})

"""

¿Cuándo NO conviene usar una sola función?

No conviene cuando:

Un modelo necesita .predict_proba()

Otro necesita postprocesamiento diferente

Uno devuelve probabilidades y otro valores continuos

Necesitas transformar la salida

Ejemplo:

Regresión -> devuelve valores numéricos

Clasificación -> puede devolver probabilidades

Clustering -> devuelve labels

"""