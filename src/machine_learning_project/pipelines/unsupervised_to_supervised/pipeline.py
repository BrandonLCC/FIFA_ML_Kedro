from kedro.pipeline import Pipeline, node, pipeline
from .nodes import create_supervised_datasets

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=create_supervised_datasets,
            inputs=dict(
                clean_dataset="clean_dataset", # Entrada dataset anomalias + clustering o anomalias + ..?
                features_regression="params:model_options_regression.features",##
                target_regression="params:model_options_regression.target",##
                features_classification="params:model_options_classification.features", ####
                target_classification="params:model_options_classification.target",###
                test_size_reg="params:model_options.test_size",
                test_size_class="params:model_options_classification.test_size",
                random_state="params:model_options.random_state",
                stratify_class="params:model_options_classification.stratify"
            ),
            outputs=[
                # unsup = no supervizado
                # Cambios realizados el 10/02/2026
                # Cambiamos el orden de las salidas retornadas 
                # en la funcion de nodes.py de unsupervised_to_supervised era 
                # los retornos de los train y test de regresion y luego de clasificacion

                # en este outputs de este archivo pipeline.py la salida estaban al revez.

                # ¿Que error estoy solucionando?
                # Se espera que las metricas concidan correctamente 
                # ya que las metricas de los modelos de clasificación son bastante bajas, mientras que las de regresion son altas. 

                # Estado del Error: [Por soluciónar]

                "X_train_regression_unsup", "X_test_regression_unsup",
                "y_train_regression_unsup", "y_test_regression_unsup",
                "X_train_class_unsup", "X_test_class_unsup", 
                "y_train_class_unsup", "y_test_class_unsup"
               
                ],
            name="create_supervised_datasets_node"
        )
    ])


