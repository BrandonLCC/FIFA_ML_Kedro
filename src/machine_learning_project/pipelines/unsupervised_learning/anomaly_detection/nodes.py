import pandas as pd
from sklearn.ensemble import IsolationForest

def detectar_anomalias(dataset: pd.DataFrame, params: dict):
    """
    Detecta anomalías usando parámetros de parameters.yml
    """
    contamination = params["contamination"]

    modelo = IsolationForest(contamination=contamination, random_state=42)
    etiquetas = modelo.fit_predict(dataset)

    # 1 = normal, -1 = anomalía
    dataset_filtrado = dataset[etiquetas == 1]

    return dataset_filtrado
