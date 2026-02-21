"""
This is a boilerplate pipeline 'classification_prediction'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import predict_model  # noqa

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=predict_model,
            inputs=["grid_logistic_model_classification", "X_test_class", "params:classification_columns.logistic_classification"], 
            outputs="y_pred_logistic_classification",
            name="y_pred_logistic_classification_node"
        ),
        Node(
            func=predict_model,
            inputs=["grid_knn_model_classification", "X_test_class", "params:classification_columns.knn"], 
            outputs="y_pred_knn",
            name="y_pred_knn_node"
        ),
        Node(
            func=predict_model,
            inputs=["grind_svc_cv_model_classification", "X_test_class", "params:classification_columns.svc"], 
            outputs="y_pred_svc",
            name="y_pred_svc_node"
        ),
        Node(
            func=predict_model,
            inputs=["grid_decision_tree_model_classification", "X_test_class", "params:classification_columns.decision_tree"], 
            outputs="y_pred_decision_tree",
            name="y_pred_decision_tree_node"
        ),
        Node(
            func=predict_model,
            inputs=["grid_random_forest_model_classification", "X_test_class", "params:classification_columns.random_forest"], 
            outputs="y_pred_random_forest_classification",
            name="y_pred_random_forest_classification_node"
        ),

    ])
