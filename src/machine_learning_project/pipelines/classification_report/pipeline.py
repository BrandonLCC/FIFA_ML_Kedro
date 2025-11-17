# src/machine_learning_project/pipelines/classification_report/pipeline.py
from kedro.pipeline import Pipeline, Node
from .nodes import evaluacion_completa_modelo_clasificacion

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=evaluacion_completa_modelo_clasificacion,
            inputs=[
                "grid_logistic_model_classification",
                "X_test_class",
                "y_test_class",
                "params:_modelo_logistic_classification",
                "params:report_path_logistic"
            ],
            outputs="report_logistic_model_classification",
            name="report_logistic_model_classification_node"
        ),
        Node(
            func=evaluacion_completa_modelo_clasificacion,
            inputs=[
                "grid_knn_model_classification",
                "X_test_class",
                "y_test_class",
                "params:_modelo_knn_classification",
                "params:report_path_knn"
            ],
            outputs="report_knn_model_classification",
            name="report_knn_model_classification_node"
        ),
        Node(
            func=evaluacion_completa_modelo_clasificacion,
            inputs=[
                "grind_svc_cv_model_classification",
                "X_test_class",
                "y_test_class",
                "params:_svc_param_grid",
                "params:report_path_svc"
            ],
            outputs="report_grind_svc_cv_model_classification",
            name="report_grind_svc_cv_model_classification_node"
        ),
        Node(
            func=evaluacion_completa_modelo_clasificacion,
            inputs=[
                "grid_decision_tree_model_classification",
                "X_test_class",
                "y_test_class",
                "params:_modelo_decision_tree_classification",
                "params:report_path_decision_tree"
            ],
            outputs="report_decision_tree_model_classification",
            name="report_decision_tree_model_classification_node"
        ),
        Node(
            func=evaluacion_completa_modelo_clasificacion,
            inputs=[
                "grid_random_forest_model_classification",
                "X_test_class",
                "y_test_class",
                "params:_modelo_random_forest_classification",
                "params:report_path_random_forest"
            ],
            outputs="report_random_forest_model_classification",
            name="report_random_forest_model_classification_node"
        )
    ])
