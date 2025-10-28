from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import (
    division_datos_test_train,
    entrenar_modelo_logistic_cv,
    entrenar_knn_cv,
    entrenar_xgboost_cv,
    entrenar_decision_tree_cv,
    entrenar_random_forest_cv,
    evaluacion_modelo
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=division_datos_test_train,
            inputs=["model_input_table", "params:model_options"],
            outputs=["X_train", "X_test", "y_train", "y_test"], #Como no tiene salida en catalog pra output definimos el train y train para los otro nodos 
            name="division_datos_test_train_node"
        ),
        Node(
            func=entrenar_modelo_logistic_cv, 
            inputs=["X_train", "y_train", "params:_logistic_param_grid"],
            outputs="grid_logistic_model_classification",
            name="grid_logistic_model_clasificacion_node"
        ),
        Node(
            func=entrenar_knn_cv,
            inputs=["X_train", "y_train", "params:_knn_param_grid"],
            outputs="grid_knn_model_classification",
            name="grid_knn_model_clasificacion_node"
        ),
        Node(
            func=entrenar_xgboost_cv,
            inputs=["X_train", "y_train", "params:_xgboost_param_grid"],
            outputs="grid_xgboost_model_classification",
            name="grid_xgboost_model_clasificacion_node"
        ),
        Node(
            func=entrenar_decision_tree_cv,
            inputs=["X_train", "y_train", "params:_decision_tree_param_grid"],
            outputs="grid_decision_tree_model_classification",
            name="grid_decision_tree_model_clasificacion_node"
        ),
        Node(
            func=entrenar_random_forest_cv,
            inputs=["X_train", "y_train", "params:_random_forest_param_grid"],
            outputs="grid_random_forest_model_classification",
            name="grid_random_forest_model_clasificacion_node"
        ),
        Node(
            func=evaluacion_modelo,
            inputs=["grid_logistic_model_classification", "X_test", "y_test"],
            outputs=None,
            name="evaluacion_logisticRegression_node"
        ), 
        Node(
            func=evaluacion_modelo,
            inputs=["grid_knn_model_classification", "X_test", "y_test"],
            outputs=None,
            name="evaluacion_knn_node"
        ),
        Node(
            func=evaluacion_modelo,
            inputs=["grid_xgboost_model_classification", "X_test", "y_test"],
            outputs=None,
            name="evaluacion_xgboost_node"
        ),
        Node(
            func=evaluacion_modelo,
            inputs=["grid_decision_tree_model_classification", "X_test", "y_test"],
            outputs=None,
            name="evaluacion_decision_tree_node"
        ),
        Node(
            func=evaluacion_modelo,
            inputs=["grid_random_forest_model_classification", "X_test", "y_test"],
            outputs=None,
            name="evaluacion_random_forest_node"
        ),  

    ])
