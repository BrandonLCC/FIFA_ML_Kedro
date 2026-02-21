# src/machine_learning_project/pipelines/classification_report/pipeline.py
from kedro.pipeline import Pipeline, Node
from .nodes import evaluacion_modelo_individual

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
           func=evaluacion_modelo_individual,
           inputs=[
               "y_pred_logistic_classification",
               "y_test_class",
               "params:modelo_logistic_classification",
           ],
           outputs="metrics_logistic",
           name="metrics_logistic_node"
        ),
        Node(
           func=evaluacion_modelo_individual,
           inputs=[
               "y_pred_knn_classification",
               "y_test_class",
               "params:modelo_knn_classification",
           ],
           outputs="metrics_knn_classification",
           name="metrics_knn_node"
        ),

        Node(
           func=evaluacion_modelo_individual,
           inputs=[
               "y_pred_svc",
               "y_test_class",
               "params:svc_classification",
           ],
           outputs="metrics_svc",
            name="metrics_svc_node"
        ),

        Node(
           func=evaluacion_modelo_individual,
           inputs=[
               "y_pred_decision_tree_classification",
               "y_test_class",
               "params:modelo_decision_tree_classification",
           ],
           outputs="metrics_decision_tree_classification",
           name="metrics_decision_tree_node"
        ),

        Node(
           func=evaluacion_modelo_individual,
           inputs=[
               "y_pred_random_forest_classification",
               "y_test_class",
               "params:modelo_random_forest_classification",
           ],
           outputs="metrics_random_forest_classification",
           name="metrics_random_forest_classification_node"
        )

    ])
