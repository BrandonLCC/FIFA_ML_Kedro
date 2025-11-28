"""
This is a boilerplate pipeline 'unsupervised_learning'
generated using Kedro 1.0.0
"""
import pandas as pd
from sklearn.decomposition import PCA

def aplicar_pca(dataset: pd.DataFrame, params: dict):
    """
    Aplica PCA con parámetros configurados en parameters.yml
    """
    n_componentes = params["n_componentes"]

    pca = PCA(n_components=n_componentes)
    componentes = pca.fit_transform(dataset)

    columnas = [f"PCA_{i+1}" for i in range(n_componentes)]
    df_pca = pd.DataFrame(componentes, columns=columnas, index=dataset.index)

    return df_pca
