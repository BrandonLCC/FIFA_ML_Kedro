from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import (
    division_datos_test_train,
    entrenar_modelo_logistic_cv,
    entrenar_knn_cv,
    entrenar_svc_cv,
    entrenar_decision_tree_cv,
    entrenar_random_forest_cv,
    evaluacion_modelo
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
             # Nodo que divide los datos y guarda en el catalog
      #  Node(
      #      func=division_datos_test_train,
      #      inputs=["clustered_data", "params:model_options"],
      #      #inputs=["model_input_table", "params:model_options"],
      #      outputs=["X_train_class", "X_test_class", "y_train_class", "y_test_class"],
      #      name="division_datos_test_train_node_classification"
      #  ),
        
        # Entrenamiento de modelos usando datasets de clasificación

        # Node(
        #     func=entrenar_modelo_logistic_cv, 
        #     inputs=["X_train_class", "y_train_class", "params:_logistic_param_grid"],
        #     outputs="grid_logistic_model_classification",
        #     name="grid_logistic_model_clasificacion_node"
        # ),

        # Node(
        #     func=entrenar_knn_cv,
        #     inputs=["X_train_class", "y_train_class", "params:_knn_param_grid"],
        #     outputs="grid_knn_model_classification",
        #     name="grid_knn_model_clasificacion_node"
        # ),

        # --- ÚNICO MODELO ACTIVADO (el elegido) ---
        #Node(
        #    func=entrenar_svc_cv,
        #    inputs=["X_train_class", "y_train_class", "params:_svc_param_grid"],
        #    outputs="grind_svc_cv_model_classification",
        #    name="grind_svc_cv_model_clasificacion_node"
        #),
        # -------------------------------------------

        #Node(
        #     func=entrenar_decision_tree_cv,
        #     inputs=["X_train_class", "y_train_class", "params:_decision_tree_param_grid"],
        #     outputs="grid_decision_tree_model_classification",
        #     name="grid_decision_tree_model_clasificacion_node"
        # ),

         Node(
             func=entrenar_random_forest_cv,
             inputs=["X_train_class", "y_train_class", "params:_random_forest_param_grid"],
             outputs="grid_random_forest_model_classification",
             name="grid_random_forest_model_clasificacion_node"
         ),

        # Evaluación de modelos usando X_test_class y y_test_class

        # Node(
        #     func=evaluacion_modelo,
        #     inputs=["grid_logistic_model_classification", "X_test_class", "y_test_class"],
        #     outputs=None,
        #     name="evaluacion_logisticRegression_node"
        # ), 

        # Node(
        #     func=evaluacion_modelo,
        #     inputs=["grid_knn_model_classification", "X_test_class", "y_test_class"],
        #     outputs=None,
        #     name="evaluacion_knn_node"
        # ),

        # --- ÚNICA EVALUACIÓN  ---
        #Node(
        #    func=evaluacion_modelo,
        #    inputs=["grind_svc_cv_model_classification", "X_test_class", "y_test_class"],
        #    outputs=None,
        #    name="evaluacion_svc_node"
        #),
        # ----------------------------------

        # Node(
        #     func=evaluacion_modelo,
        #     inputs=["grid_decision_tree_model_classification", "X_test_class", "y_test_class"],
        #     outputs=None,
        #     name="evaluacion_decision_tree_node"
        # ),

         Node(
             func=evaluacion_modelo,
             inputs=["grid_random_forest_model_classification", "X_test_class", "y_test_class"],
             outputs=None,
             name="evaluacion_random_forest_node"
         ),
  
    ])
