# src/machine_learning_project/pipelines/classification_report/pipeline.py
from kedro.pipeline import Pipeline, Node
from .nodes import evaluacion_completa_modelo_clasificacion

def create_pipeline(**kwargs) -> Pipeline:
    from .nodes import evaluacion_completa_modelo_clasificacion
    
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
            outputs="regression_report_logistic_model_classification",
            name="grid_logistic_model_classification_report_node"
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
            outputs="regression_report_knn_model_classification",
            name="grid_knn_model_classification_report_node"
        ),
        Node(
            func=evaluacion_completa_modelo_clasificacion,
            inputs=[
                "grid_xgboost_model_classification",
                "X_test_class",
                "y_test_class",
                "params:_modelo_xgboost_classification",
                "params:report_path_xgboost"
            ],
            outputs="regression_report_xgboost_model_classification",
            name="grid_xgboost_model_classification_report_node"
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
            outputs="regression_report_decision_tree_model_classification",
            name="grid_decision_tree_model_classification_report_node"
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
            outputs="regression_report_random_forest_model_classification",
            name="grid_random_forest_model_classification_report_node"
        )
    ])
