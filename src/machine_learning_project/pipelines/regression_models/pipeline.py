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
            func=division_datos_test_train,                               # Como entrada de dataaset, ver si usamo model_input_table o clustered_data o clean_dataset o otros.
            inputs=["model_input_table", "params:model_options_regression"], #<-- Cambiando antes model_option (ver si )
                                                                          #< --- Ahora: model_options_regression
                                                                          # Buscando solucionar Error: Metricas malas en modelos de clasificacion

            #=["model_input_table", "params:model_options_regression"], Dataset cuando no estaba unsupervised_processed_dataset.

            #=["model_input_table", "params:model_options"], # NO 
            outputs=["X_train_regression", "X_test_regression", "y_train_regression", "y_test_regression"],
            name="division_datos_test_train_node_regression"
        ),              

        # Entrenamiento GridSearch
        Node(
            func=entrenar_modelo_linear_cv,
            inputs=["X_train_regression", "y_train_regression", "params:_linear_param_grid"],
            outputs="grid_linear_model",
            name="grid_linear_model_node"
        ),
        Node(
            func=entrenar_linear_multiple_cv,
            inputs=["X_train_regression", "y_train_regression", "params:_linear_param_grid"],
            outputs="grid_linear_multiple_model",
            name="grid_linear_multiple_model_node"
        ),
        Node(
            func=entrenar_svr_cv,
            inputs=["X_train_regression", "y_train_regression", "params:_svr_param_grid"],
            outputs="grid_svr_model",
            name="entrenar_svr_cv_node"
        ),
        Node(
            func=entrenar_dt_grid,
            inputs=["X_train_regression", "y_train_regression", "params:_dt_param_grid"],
            outputs="grid_decision_tree_model",
            name="grid_decision_tree_model_node"
        ),

        Node(
            func=entrenar_random_forest_cv,
            inputs=["X_train_regression", "y_train_regression", "params:_rf_param_grid"],
            outputs="grid_randomforest_model",
            name="grid_randomforest_model_node"
        ),

        # Evaluación de modelos
        Node(
            func=evaluacion_modelo,
            inputs=["grid_linear_model", "X_test_regression", "y_test_regression"],
            outputs=None,
            name="evaluacion_linearRegression_node",
        ),
        Node(
            func=evaluacion_modelo,
            inputs=["grid_linear_multiple_model", "X_test_regression", "y_test_regression"],
            outputs=None,
            name="evaluacion_linearRegression_multiple_node",
        ),
        Node(
            func=evaluacion_modelo,
            inputs=["grid_svr_model", "X_test_regression", "y_test_regression"],
            outputs=None,
            name="evaluacion_SVR_node",
        ),
        Node(
            func=evaluacion_modelo,
            inputs=["grid_decision_tree_model", "X_test_regression", "y_test_regression"],
            outputs=None,
            name="evaluacion_DecisionTreeRegressor_node",
        ), 
        Node(
            func=evaluacion_modelo,
            inputs=["grid_randomforest_model", "X_test_regression", "y_test_regression"],
            outputs=None,
            name="evaluacion_RandomForestRegressor_node",
        )

    ])
