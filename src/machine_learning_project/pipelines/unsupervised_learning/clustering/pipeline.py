from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    kmeans_clustering,
    dbscan_clustering,
    hierarchical_clustering,
    select_best_cluster
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
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
            outputs="clustered_dataset",
            name="select_best_cluster_node"
        )
    ])
