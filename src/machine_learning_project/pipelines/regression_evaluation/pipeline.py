from kedro.pipeline import Pipeline, node
from .nodes import evaluacion_modelo_individual

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        # Antes de haber creado el pipeline evaluacion, se generaba las evaluaciónes en el pipeline de creación de modelos 
        # la cual habia una funcion llamada evaluacion_modelo_individual, la cual se encargaba de evaluar cada modelo individualmente y generar reportes.
        # Ahora se ha decidido mover esa función al pipeline de evaluación, para que sea más coherente y se pueda generar los reportes de evaluación en un solo lugar.

        # Utiliando la funcion evaluacion 
        node( 
            func=evaluacion_modelo_individual,
            inputs=["y_pred_linear_regression", "y_test_regression","params:modelo_linear_regression"],
            outputs="metrics_linear_simple_regression", 
            name="metrics_linear_simple_regression_node"
        ), 
        node(
            func=evaluacion_modelo_individual,
            inputs=["y_pred_linear_multiple_regression", "y_test_regression","params:modelo_linear_multiple_regression"],
            outputs="metrics_linear_multiple_regression",
            name="metrics_linear_multiple_regression_node"
        ), 
        node(
            func=evaluacion_modelo_individual,
            inputs=["y_pred_svr", "y_test_regression","params:modelo_svr_regression"],
            outputs="metrics_svr",
            name="metrics_svr_node"
        ), 
        node(
            func=evaluacion_modelo_individual,
            inputs=["y_pred_decision_tree_regression", "y_test_regression","params:modelo_decision_tree_regression"],
            outputs="metrics_decision_tree_regression",  
            name="metrics_decision_tree_regression_node"
        ),
    
        node(
            func=evaluacion_modelo_individual,
            inputs=["y_pred_random_forest_regression", "y_test_regression","params:modelo_grid_randomforest_regression"],
            outputs="metrics_random_forest_regression",
            name="metrics_random_forest_regression_node"
        ),


        # Version del nodo anterior:
        # Pasaba directamente los output modelo, x_Test  y_test
        # Y se hacia directamente la prediccion en la funcion evaluacion_modelo_individual
        

        #   node(
        #    func=evaluacion_modelo_individual,
        #    inputs=["grid_randomforest_model", "X_test_regression", "y_test_regression","params:_modelo_grid_randomforest_regression"],
        #    outputs="metrics_random_forest_regression",
        #    name="metrics_random_forest_regression_node"
        #),

        
    ])
    
