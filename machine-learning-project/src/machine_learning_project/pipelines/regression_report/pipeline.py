from kedro.pipeline import Node, Pipeline 
from .nodes import generate_regression_report, evaluacion_modelo_individual

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=evaluacion_modelo_individual,
            inputs="regression_report_input",
            outputs="regression_report_output",
        )
    ])
