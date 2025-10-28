from kedro.pipeline import Node, Pipeline  
from .nodes import (
    division_datos_test_train,
    evaluacion_modelo,
    entrenar_modelo_linear_cv,
    entrenar_linear_multiple_cv,
    entrenar_svr_cv,
    entrenar_random_forest_cv, 
    entrenar_dt_grid
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            # División de datos
            Node(
                func=division_datos_test_train,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="division_datos_test_train_node"
            ),              

            # Entrenamiento GridSearch
            Node(
                func=entrenar_modelo_linear_cv,
                inputs=["X_train", "y_train", "params:_linear_param_grid"],
                outputs="grid_linear_model",
                name="grid_linear_model_node"
            ),
            Node(
                func=entrenar_linear_multiple_cv,
                inputs=["X_train", "y_train", "params:_linear_param_grid"],
                outputs="grid_linear_multiple_model",
                name="grid_linear_multiple_model_node"
            ),
            Node(
                func=entrenar_svr_cv,
                inputs=["X_train", "y_train", "params:_svr_param_grid"],
                outputs="grid_svr_model",
                name="entrenar_svr_cv_node"
            ),
            Node(
                func=entrenar_dt_grid,
                inputs=["X_train", "y_train", "params:_dt_param_grid"],
                outputs="grid_decision_tree_model",
                name="grid_decision_tree_model_node"
            ),
            Node(
                func=entrenar_random_forest_cv,
                inputs=["X_train", "y_train", "params:_rf_param_grid"],  # Corregido params:
                outputs="grid_randomforest_model",
                name="grid_randomforest_model_node"
            ),

            # Evaluación de modelos
            Node(
                func=evaluacion_modelo,
                inputs=["grid_linear_model", "X_test", "y_test"],
                outputs=None,
                name="evaluacion_linearRegression_node",
            ),
            Node(
                func=evaluacion_modelo,
                inputs=["grid_linear_multiple_model", "X_test", "y_test"],
                outputs=None,
                name="evaluacion_linearRegression_multiple_node",
            ),
            Node(
                func=evaluacion_modelo,
                inputs=["grid_svr_model", "X_test", "y_test"],
                outputs=None,
                name="evaluacion_SVR_node",
            ),
            Node(
                func=evaluacion_modelo,
                inputs=["grid_decision_tree_model", "X_test", "y_test"],
                outputs=None,
                name="evaluacion_DecisionTreeRegressor_node",
            ), 
            Node(
                func=evaluacion_modelo,
                inputs=["grid_randomforest_model", "X_test", "y_test"],
                outputs=None,
                name="evaluacion_RandomForestRegressor_node",
            )
    ])
