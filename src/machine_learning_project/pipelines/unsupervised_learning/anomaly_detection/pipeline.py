from kedro.pipeline import Pipeline, node, pipeline
from .nodes import detectar_anomalias

def create_pipeline(**kwargs):
    return pipeline([
        node(
            func=detectar_anomalias,
             inputs=["primary_dataset", "params:anomaly"],  # Ajusta si corresponde
            outputs="datos_limpios_sin_anomalias", # primero el procesamiento, en mi caso, luego los outputs van a 04_feature, luego van los modelos
            name="detectar_anomalias_node"
        )
    ])
