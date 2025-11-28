"""
This is a boilerplate pipeline 'unsupervised_learning'
generated using Kedro 1.0.0

"""

def combine_unsupervised_outputs(pca_data, clustered_data, datos_limpios_sin_anomalias):
    """
    Combina los resultados de PCA, clustering y anomaly detection
    para formar un dataset final.
    """
    # clustered_data ya incluye las columnas originales + cluster
    df = clustered_data.copy()

    # Agregar componentes PCA
    for col in pca_data.columns:
        df[col] = pca_data[col]

    # Filtrar anomalías (clean_data viene filtrado desde el submódulo)
    df = df[df.index.isin(datos_limpios_sin_anomalias.index)]

    return df
