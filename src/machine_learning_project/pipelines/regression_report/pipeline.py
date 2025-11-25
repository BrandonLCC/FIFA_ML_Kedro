from kedro.pipeline import Pipeline, Node
from .nodes import evaluacion_modelo_individual

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        #Utiliando la funcion evaluacion 
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_linear_model", "X_test_regression", "y_test_regression","params:_modelo_linear_regression"],
            outputs="regression_report_linear_simple", #Las salidas que se visualizan las metricas en kedro viz
            name="evaluacion_linear_model_regression_node"
        ), 
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_linear_multiple_model", "X_test_regression", "y_test_regression","params:_modelo_linear_multiple_regression"],
            outputs="regression_report_linear_multiple",
            name="evaluacion_linear_multiple_regression_node"
        ), 
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_svr_model", "X_test_regression", "y_test_regression","params:_modelo_svr_regression"],
            outputs="regression_report_svr",
            name="evaluacion_svr_regression_node"
        ), 
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_decision_tree_model", "X_test_regression", "y_test_regression","params:_modelo_decision_tree_regression"],
            outputs="regression_report_decision_tree",  
            name="evaluacion_decision_tree_regression_node"
        ),
    
        Node(
            func=evaluacion_modelo_individual,
            inputs=["grid_randomforest_model", "X_test_regression", "y_test_regression","params:_modelo_grid_randomforest_regression"],
            outputs="regression_report_randomforest",
            name="evaluacion_linear_randomforest_regression_node"
        ), 
        
            
    ])
