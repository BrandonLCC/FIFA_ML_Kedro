from kedro.pipeline import Pipeline, node, pipeline
from .nodes import aplicar_pca, aplicar_tsne_umap

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=aplicar_pca,
            inputs=dict(
                datos="model_input_data",
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
            outputs="tsne_umap_output",
            name="tsne_umap_node"
        )
    ])
