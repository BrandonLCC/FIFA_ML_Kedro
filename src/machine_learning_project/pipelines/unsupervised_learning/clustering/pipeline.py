from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    kmeans_clustering,
    dbscan_clustering,
    hierarchical_clustering,
    select_best_cluster
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        # En clustering buscamos crear nuevas características basadas en la estructura de los datos, por lo que el input es el dataset limpio
        #  y el output es un dataset con una nueva columna que representa el cluster asignado a cada muestra.
        # Agregaremos estas características al dataset limpio para que 
        # puedan ser utilizadas en el módulo de detección de anomalías.

        # Clustering con KMeans, DBSCAN y Clustering Jerárquico
        # El pipeline de reduccion de dimensionalizad sera el encargado de reducir la dimensionalidad 
        # del dataset limpio, por lo que el input de los nodos de clustering sera el dataset limpio 
        # con las nuevas características de reduccion de dimensionalidad.

        node(
            func=kmeans_clustering,
            inputs=["clean_dataset", "params:clustering.kmeans"],
            outputs="kmeans_clusters",
            name="kmeans_clustering_node"
        ),
        node(
            func=dbscan_clustering,
            inputs=["clean_dataset", "params:clustering.dbscan"],
            outputs="dbscan_clusters",
            name="dbscan_clustering_node"
        ),
        node(
            func=hierarchical_clustering,
            inputs=["clean_dataset", "params:clustering.hierarchical"],
            outputs="hierarchical_clusters",
            name="hierarchical_clustering_node"
        ),
        #Funcion: selecciona el mejor clustering 
        node(
            func=select_best_cluster,
            inputs=[
                "kmeans_clusters",
                "dbscan_clusters",
                "hierarchical_clusters"
            ],
            outputs="clustered_unsupervised_processed_dataset",
            name="select_best_cluster_node"
        )

        # Agregar al dataset limpio la nueva columna de cluster asignado para que pueda 
        # ser utilizada en el módulo de detección de anomalías.

      # usar deteccion antes o despues dek clustering?  
    ])
