"""
This is a boilerplate pipeline 'regresssion_prediction'
generated using Kedro 1.0.0
"""

from kedro.pipeline import node, Pipeline  # noqa
from .nodes import predict_model

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            # El tercer argumento es simplemente un  nombre de la columna que se va dar.
            func=predict_model,
            inputs=["grid_linear_model", "X_test_regression","params:prediction_columns.linear_simple"], 
            outputs="y_pred_linear_regression",
            name="y_pred_linear_regression_node"
        ),
        node(
            func=predict_model,
            inputs=["grid_linear_multiple_model", "X_test_regression", "params:prediction_columns.linear_multiple"], 
            outputs="y_pred_linear_multiple_regression",
            name="y_pred_linear_multiple_regression_node"
        ),
        node(
            func=predict_model,
            inputs=["grid_svr_model", "X_test_regression", "params:prediction_columns.svr"], 
            outputs="y_pred_svr",
            name="y_pred_svr_node"
        ),
        node(
            func=predict_model,
            inputs=["grid_decision_tree_model", "X_test_regression", "params:prediction_columns.decision_tree"], 
            outputs="y_pred_decision_tree_regression",
            name="y_pred_decision_tree_regression_node"
        ),
        node(
            func=predict_model,
            inputs=["grid_randomforest_model", "X_test_regression", "params:prediction_columns.random_forest"], 
            outputs="y_pred_random_forest_regression",
            name="y_pred_random_forest_regression_node"
        ),
    ])
