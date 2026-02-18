from kedro.pipeline import Pipeline, Node
from .nodes import evaluacion_modelo_individual

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        # Utiliando la funcion evaluacion 
        Node( 
            func=evaluacion_modelo_individual,
            inputs=["grid_linear_model", "X_test_regression", "y_test_regression","params:_modelo_linear_regression"],
            outputs="metrics_linear_simple_regression", 
            name="metrics_linear_simple_regression_node"
        ), 
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_linear_multiple_model", "X_test_regression", "y_test_regression","params:_modelo_linear_multiple_regression"],
            outputs="metrics_linear_multiple_regression",
            name="metrics_linear_multiple_regression_node"
        ),
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_svr_model", "X_test_regression", "y_test_regression","params:_modelo_svr_regression"],
            outputs="metrics_svr",
            name="metrics_svr_node"
        ), 
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_decision_tree_model", "X_test_regression", "y_test_regression","params:_modelo_decision_tree_regression"],
            outputs="metrics_decision_tree_regression",  
            name="metrics_decision_tree_regression_node"
        ),
    
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_randomforest_model", "X_test_regression", "y_test_regression","params:_modelo_grid_randomforest_regression"],
            outputs="metrics_random_forest_regression",
            name="metrics_random_forest_regression_node"
        ),

    ])
