"""
This is a boilerplate pipeline 'unsupervised_learning'
generated using Kedro 1.0.0

"""
import pandas as pd

# Función para combinar los resultados de PCA con el dataset original
# Para que el clustering y la detección de anomalías puedan usar tanto las características originales como las componentes PCA.
# Se puede usar solo los componentes, pero en mi caso usaremos tanto componentes, como caracteristicas.
def merge_dimensionality_with_dataset(imput_table: pd.DataFrame, pca_output: pd.DataFrame) -> pd.DataFrame:
    
    # Asegurar mismo índice
    pca_output = pca_output.set_index(imput_table.index)

    dataset_with_components = pd.concat(
        [imput_table, pca_output],
        axis=1
    )

    return dataset_with_components


def dataset_for_clustering(pca_output: pd.DataFrame) -> pd.DataFrame:
    
    clustering_dataset = pca_output.copy()

    return clustering_dataset


def merge_clusters_with_dataset(
    dataset_with_pca: pd.DataFrame,clustered_dataset: pd.DataFrame ) -> pd.DataFrame:

    result = dataset_with_pca.copy()

    result["cluster_id"] = clustered_dataset["cluster_id"]

    return result