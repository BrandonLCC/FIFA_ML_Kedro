from kedro.pipeline import Pipeline, Node, pipeline
from .nodes import aplicar_pca, aplicar_umap

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        Node( 
            func=aplicar_pca,
            inputs=dict(
                datos="model_input_table", 
                n_componentes="params:dimensionality_reduction.pca_n_components"
            ),
            outputs="pca_output",
            name="pca_node"
        ),
        Node(
            func=aplicar_umap,
            inputs=dict(
                datos="model_input_table",
                metodo="params:dimensionality_reduction.umap_method",
                n_componentes="params:dimensionality_reduction.umap_n_components",
                random_state="params:dimensionality_reduction.umap_random_state"
            ),
            outputs="umap_dataset",
            name="umap_node"
        )
    ])
