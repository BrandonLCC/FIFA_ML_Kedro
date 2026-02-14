from kedro.pipeline import Pipeline, node, pipeline
from .nodes import aplicar_pca, aplicar_tsne_umap

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node( 
            func=aplicar_pca,
            inputs=dict(
                datos="clustered_dataset", # cambio: Se cambia el dataset imput_table a clean_dataset debido a que se sigue el flujo 
                                       # Flujo esperado: (anomaly_detection output: clea_dataset) > dimensionality_reduction 
                                       # Ojo: La salida de este dataset no debe aplicarse a clustering, se puede usar el mismo clean_dataset. 
                                       # me refiero a que no es necesario que haya un flujo de datasets anomaly>clustering>dimensionality  
                                       # Todo depende de un  proposito claro.
                                                                    
                n_componentes="params:dimensionality_reduction.pca_n_components"
            ),
            outputs="pca_output",
            name="pca_node"
        ),
        node(
            func=aplicar_tsne_umap,
            inputs=dict(
                datos="pca_output",
                metodo="params:dimensionality_reduction.tsne_umap_method",
                n_componentes="params:dimensionality_reduction.tsne_umap_n_components",
                random_state="params:dimensionality_reduction.tsne_umap_random_state"
            ),
            outputs="unsupervised_processed_dataset",
            name="dimensionality_reduction_dataset_node"
        )
    ])
