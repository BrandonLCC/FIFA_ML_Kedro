# src/machine_learning_project/pipelines/classification_report/pipeline.py
from kedro.pipeline import Pipeline, Node
from machine_learning_project.pipelines.classification_report.nodes import combinar_metricas, seleccionar_mejor_modelo

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node (
            func=combinar_metricas,
            inputs=["metrics_logistic", 
                    "metrics_knn_classification", 
                    "metrics_svc",
                    "metrics_decision_tree_classification",
                    "metrics_random_forest_classification"],
            outputs="metris_all_models_clasificacion",
            name="combine_metrics_clasificacion_node"
        ),
        Node (
            func=seleccionar_mejor_modelo,
            inputs=["metris_all_models_clasificacion"],
            outputs="Reporte_mejor_metrica_modelo_clasificacion",
            name="Reporte_mejor_metrica_modelo_clasificacion_node"
        )
    ])
