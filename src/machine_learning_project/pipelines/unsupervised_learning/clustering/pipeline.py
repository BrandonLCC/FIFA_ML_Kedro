from kedro.pipeline import Pipeline, node, pipeline
from .nodes import aplicar_clustering

def create_pipeline(**kwargs):
    return pipeline([
        node(
            func=aplicar_clustering,
            inputs=["datos_limpios_sin_anomalias", "params:clustering"],   # input desde anomaly detection
            outputs="clustered_data", # primero el procesamiento, en mi caso, luego los outputs van a 04_feature, luego van los modelos
            name="aplicar_clustering_node"
        )
    ])



            