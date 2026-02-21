from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import (
    division_datos_test_train,
    entrenar_modelo_logistic_cv,
    entrenar_knn_cv,
    entrenar_svc_cv,
    entrenar_decision_tree_cv,
    entrenar_random_forest_cv,
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        # Nodo que divide los datos y guarda en el catalog

        # !!REVICION DE ESTE NODO: SOLUCIONANDO BAJO DESEMPEÑO DE MODELOS DE CLASIFICACIÓN
        # ESTADO DEL ERROR: solucionando..

        Node(
            func=division_datos_test_train, # Como entrada de dataaset, ver si usamo model_input_table o clustered_data o clean_dataset o otros.
            inputs=["model_input_table", "params:model_options_classification"], # <-- En parameter Models_option es de regresion
                                                                
                                                                # <-- Deberia ser de model_options_classification de parameters de clasificacion
                                                                # Ojo, no usar todavia las entradas no supervizados, entender el porque             
            #inputs=["model_input_table", "params:model_options_classification"],
            outputs=["X_train_class", "X_test_class", "y_train_class", "y_test_class"],
            name="division_datos_test_train_node_classification"
       ),
         
        Node(
            func=entrenar_modelo_logistic_cv, 
            inputs=["X_train_class", "y_train_class", "params:_logistic_param_grid"],
            outputs="grid_logistic_model_classification",
            name="grid_logistic_model_clasificacion_node"
        ),

        Node(
            func=entrenar_knn_cv,
            inputs=["X_train_class", "y_train_class", "params:_knn_param_grid"],
            outputs="grid_knn_model_classification",
            name="grid_knn_model_clasificacion_node"
        ),

        # --- ÚNICO MODELO ACTIVADO (el elegido) ---
        Node(
            func=entrenar_svc_cv,
            inputs=["X_train_class", "y_train_class", "params:_svc_param_grid"],
            outputs="grind_svc_cv_model_classification",
            name="grind_svc_cv_model_clasificacion_node"
        ),
 
        Node(
            func=entrenar_decision_tree_cv,
            inputs=["X_train_class", "y_train_class", "params:_decision_tree_param_grid"],
            outputs="grid_decision_tree_model_classification",
            name="grid_decision_tree_model_clasificacion_node"
        ),

        Node(
            func=entrenar_random_forest_cv,
            inputs=["X_train_class", "y_train_class", "params:_random_forest_param_grid"],
            outputs="grid_random_forest_model_classification",
            name="grid_random_forest_model_clasificacion_node"
        ),
    ])
