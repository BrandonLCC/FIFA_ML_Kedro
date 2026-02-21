from __future__ import annotations

'''
"""Project pipelines original."""

from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
'''
"""Project pipelines modificado con los submodulos en orden de ejecucion"""

"""
from __future__ import annotations
from kedro.pipeline import Pipeline

# Pipelines principales
from machine_learning_project.pipelines.data_processing import pipeline as de_pipeline

# Submódulos de unsupervised
from machine_learning_project.pipelines.unsupervised_learning.dimensionality_reduction import pipeline as dimred_pipeline
from machine_learning_project.pipelines.unsupervised_learning.clustering import pipeline as clust_pipeline
from machine_learning_project.pipelines.unsupervised_learning.anomaly_detection import pipeline as anom_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    pipelines = {
        "data_processing": de_pipeline.create_pipeline(),
        "dimensionality_reduction": dimred_pipeline.create_pipeline(),
        "clustering": clust_pipeline.create_pipeline(),
        "anomaly_detection": anom_pipeline.create_pipeline(),
    }

    # Pipeline master end-to-end
    pipelines["__default__"] = (
        pipelines["data_processing"]
        + pipelines["dimensionality_reduction"]
        + pipelines["clustering"]
        + pipelines["anomaly_detection"]
    )

    return pipelines
"""

"""Project pipelines final con todos los submódulos y flujo completo."""

from kedro.pipeline import Pipeline

from machine_learning_project.pipelines.data_processing import pipeline as de_pipeline

from machine_learning_project.pipelines.unsupervised_learning.dimensionality_reduction import pipeline as dimred_pipeline
from machine_learning_project.pipelines.unsupervised_learning.clustering import pipeline as clust_pipeline
from machine_learning_project.pipelines.unsupervised_learning.anomaly_detection import pipeline as anom_pipeline

from machine_learning_project.pipelines.regression_models import pipeline as reg_pipeline
from machine_learning_project.pipelines.classification_models import pipeline as class_pipeline

from machine_learning_project.pipelines.regresssion_prediction import pipeline as reg_pred_pipeline
from machine_learning_project.pipelines.classification_prediction import pipeline as class_pred_pipeline

from machine_learning_project.pipelines.regression_evaluation import pipeline as reg_eval_pipeline
from machine_learning_project.pipelines.classification_evaluation import pipeline as class_eval_pipeline

from machine_learning_project.pipelines.regression_report import pipeline as reg_report_pipeline
from machine_learning_project.pipelines.classification_report import pipeline as class_report_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    pipelines = {
        "data_processing": de_pipeline.create_pipeline(),
        "dimensionality_reduction": dimred_pipeline.create_pipeline(),
        "clustering": clust_pipeline.create_pipeline(),
        "anomaly_detection": anom_pipeline.create_pipeline(),
        "regression_models": reg_pipeline.create_pipeline(),
        "classification_models": class_pipeline.create_pipeline(),
        "regression_prediction": reg_pred_pipeline.create_pipeline(),
        "classification_prediction": class_pred_pipeline.create_pipeline(),
        "regression_evaluation": reg_eval_pipeline.create_pipeline(),
        "classification_evaluation": class_eval_pipeline.create_pipeline(),
        "regression_report": reg_report_pipeline.create_pipeline(),
        "classification_report": class_report_pipeline.create_pipeline(),
    }

    # Pipeline maestro no supervisado
    pipelines["unsupervised_learning"] = (
        pipelines["dimensionality_reduction"]
        + pipelines["clustering"]
        + pipelines["anomaly_detection"]
    )

    # Pipeline master end-to-end
    pipelines["__default__"] = (
        pipelines["data_processing"]
        + pipelines["unsupervised_learning"]
        + pipelines["regression_models"]
        + pipelines["regression_prediction"]
        + pipelines["regression_evaluation"]
        + pipelines["classification_models"]
        + pipelines["classification_prediction"]       
        + pipelines["classification_evaluation"] 
        + pipelines["regression_report"]
        + pipelines["classification_report"]
    )

    return pipelines
