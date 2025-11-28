"""
This is a boilerplate pipeline 'unsupervised_learning'
generated using Kedro 1.0.0
"""
import pandas as pd
from sklearn.cluster import KMeans

def aplicar_clustering(dataset: pd.DataFrame, params: dict):
    """
    Aplica K-Means con parámetros configurados en parameters.yml
    """
    n_clusters = params["n_clusters"]
    modelo = KMeans(n_clusters=n_clusters, random_state=42)

    dataset = dataset.copy()
    dataset["cluster"] = modelo.fit_predict(dataset)

    return dataset
