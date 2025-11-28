"""

"""
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import aplicar_pca

def create_pipeline(**kwargs):
    return pipeline([
        node(
            func=aplicar_pca,
            inputs=["primary_dataset", "params:pca"], # Ajusta si tu dataset se llama distinto y confugura en tu archivo parameters
            outputs="pca_output", # primero el procesamiento, en mi caso, luego los outputs van a 04_feature, luego van los modelos
            name="aplicar_pca_node"
        )
    ])

