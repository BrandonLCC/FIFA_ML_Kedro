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