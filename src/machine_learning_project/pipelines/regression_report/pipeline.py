from kedro.pipeline import Pipeline, Node
from machine_learning_project.pipelines.regression_report.nodes import combinar_metricas, def_report_regresion, report_comparacion_modelos, seleccionar_mejor_modelo

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=def_report_regresion,
            inputs=["params:name_report_regression.linear_simple", "y_test_class", "y_pred_linear_regression"],
            outputs=["report_linear_simple_pred_vs_real",
                     "report_linear_simple_residual_plot",
                     "report_linear_simple_qq_plot"],
            name="report_linear_regresion_node"
        ),
        Node(
            func=def_report_regresion,
            inputs=["params:name_report_regression.linear_multiple", "y_test_class", "y_pred_linear_multiple_regression"],
            outputs=["report_linear_multiple_pred_vs_real",
                     "report_linear_multiple_residual_plot",
                     "report_linear_multiple_qq_plot"],
            name="report_linear_multiple_regresion_node"
        ),
        Node(
            func=def_report_regresion,
            inputs=["params:name_report_regression.svr", "y_test_class", "y_pred_svr"],
            outputs=["report_svr_pred_vs_real",
                     "report_svr_residual_plot",
                     "report_svr_qq_plot"],
            name="report_svr_regresion_node"
        ),
        Node(
            func=def_report_regresion,
            inputs=["params:name_report_regression.decision_tree", "y_test_class", "y_pred_decision_tree_regression"],
            outputs=["report_decision_tree_pred_vs_real",
                     "report_decision_tree_residual_plot",
                     "report_decision_tree_qq_plot"],
            name="report_decision_tree_regresion_node"
        ),
        Node(
            func=def_report_regresion,
            inputs=["params:name_report_regression.random_forest", "y_test_class", "y_pred_random_forest_regression"],
            outputs=["report_random_forest_pred_vs_real",
                     "report_random_forest_residual_plot",
                     "report_random_forest_qq_plot"],
            name="report_grid_randomforest_model_regresion_node"
        ),
        # Report busca comunicar, es por eso que al generar una comparación de 
        # Evaluacion de modelos comunicamos cuales de los modelos es mejor...
        Node(
            func=combinar_metricas,
            inputs=[
                "metrics_linear_simple_regression",
                "metrics_linear_multiple_regression",
                "metrics_svr",
                "metrics_decision_tree_regression",
                "metrics_random_forest_regression"

            ],
            outputs="metrics_all_models_regresion",
            name="combine_metrics_regresion_node"
        ),
        Node(
            func=seleccionar_mejor_modelo,
            inputs=["metrics_all_models_regresion"],
            outputs="Reporte_mejor_metrica_modelo_regresion",
            name="Reporte_mejor_metrica_modelo_regresion_node"
        )

        # Vizualización de la comparación de modelos.
        #Node(
        #    func=report_comparacion_modelos,
        #    inputs=["model_comparison_report"],
        #    outputs=None,
        #    name="comparacion_modelos_report_node"
        #)

       
    ])
