# machine_learning_project/pipelines/unsupervised_learning/clustering/nodes.py

import pandas as pd
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score

def kmeans_clustering(dataset: pd.DataFrame, params: dict) -> pd.DataFrame:
    """
    Aplica KMeans clustering al dataset.
    
    Args:
        dataset: DataFrame con datos de entrada.
        params: Diccionario con los parámetros de KMeans (n_clusters, random_state).

    Returns:
        DataFrame con columna 'cluster_kmeans'.
    """
    model = KMeans(
        n_clusters=params.get("n_clusters", 4),
        random_state=params.get("random_state", 42)
    )
    labels = model.fit_predict(dataset)
    df = dataset.copy()
    df["cluster_kmeans"] = labels
    return df

def dbscan_clustering(dataset: pd.DataFrame, params: dict) -> pd.DataFrame:
    """
    Aplica DBSCAN clustering al dataset.
    
    Args:
        dataset: DataFrame con datos de entrada.
        params: Diccionario con los parámetros de DBSCAN (eps, min_samples).

    Returns:
        DataFrame con columna 'cluster_dbscan'.
    """
    model = DBSCAN(
        eps=params.get("eps", 0.5),
        min_samples=params.get("min_samples", 5)
    )
    labels = model.fit_predict(dataset)
    df = dataset.copy()
    df["cluster_dbscan"] = labels
    return df

def hierarchical_clustering(clean_data, params):
    from sklearn.cluster import AgglomerativeClustering

    max_samples = params.get("max_samples", 2000)

    # Muestra para evitar OOM
    if len(clean_data) > max_samples:
        data = clean_data.sample(max_samples, random_state=42).copy()
    else:
        data = clean_data.copy()

    model = AgglomerativeClustering(
        n_clusters=params["n_clusters"],
        linkage=params["linkage"]
    )

    labels = model.fit_predict(data)

    # NOMBRE OBLIGATORIO PARA SELECT_BEST_CLUSTER
    data["cluster_hierarchical"] = labels

    return data



def select_best_cluster(kmeans_df: pd.DataFrame, dbscan_df: pd.DataFrame, hierarchical_df: pd.DataFrame) -> pd.DataFrame:
    """
    Selecciona el mejor clustering basado en silhouette score.
    Por simplicidad, devuelve el dataset con la mejor columna de clusters.
    
    Args:
        kmeans_df, dbscan_df, hierarchical_df: DataFrames con columnas de cluster.

    Returns:
        DataFrame final con columna 'clustered_data'.
    """
    scores = {}

    for name, df, col in [
        ("kmeans", kmeans_df, "cluster_kmeans"),
        ("dbscan", dbscan_df, "cluster_dbscan"),
        ("hierarchical", hierarchical_df, "cluster_hierarchical")
    ]:
        labels = df[col]
        # DBSCAN puede generar -1 como ruido, ignorar en silhouette
        if len(set(labels)) > 1 and min(labels) >= 0:
            score = silhouette_score(df.drop(columns=[col]), labels)
            scores[name] = score
        else:
            scores[name] = -1  # mal score si no hay clusters válidos

    # Seleccionamos el mejor algoritmo
    best_algo = max(scores, key=scores.get)

    print(f"Mejor clustering según silhouette: {best_algo} (score={scores[best_algo]:.3f})")

    best_df = {
        "kmeans": kmeans_df,
        "dbscan": dbscan_df,
        "hierarchical": hierarchical_df
    }[best_algo]

    # Renombramos la columna de clusters a 'clustered_data'
    df_final = best_df.copy()
    cluster_col = [col for col in df_final.columns if "cluster" in col][0]
    df_final = df_final.drop(columns=[c for c in df_final.columns if "cluster" in c and c != cluster_col])
    df_final.rename(columns={cluster_col: "clustered_data"}, inplace=True)

    return df_final
