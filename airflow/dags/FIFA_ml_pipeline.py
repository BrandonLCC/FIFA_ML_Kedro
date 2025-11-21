from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project


class KedroOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        package_name: str,
        pipeline_name: str,
        node_name: str | list[str],
        project_path: str | Path,
        env: str,
        conf_source: str,
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.package_name = package_name
        self.pipeline_name = pipeline_name
        self.node_name = node_name
        self.project_path = project_path
        self.env = env
        self.conf_source = conf_source

    def execute(self, context):
        configure_project(self.package_name)
        with KedroSession.create(self.project_path, env=self.env, conf_source=self.conf_source) as session:
            if isinstance(self.node_name, str):
                self.node_name = [self.node_name]
            session.run(self.pipeline_name, node_names=self.node_name)

# Kedro settings required to run your pipeline
env = "local"
pipeline_name = "__default__"
project_path = Path.cwd()
package_name = "machine_learning_project"
conf_source = "" or Path.cwd() / "conf"


# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG(
    dag_id="machine-learning-project",
    start_date=datetime(2023,1,1),
    max_active_runs=3,
    # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
    schedule_interval="@once",
    catchup=False,
    # Default settings applied to all tasks
    default_args=dict(
        owner="airflow",
        depends_on_past=False,
        email_on_failure=False,
        email_on_retry=False,
        retries=1,
        retry_delay=timedelta(minutes=5)
    )
) as dag:
    tasks = {
        "preprocess-fifa-20-node": KedroOperator(
            task_id="preprocess-fifa-20-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="preprocess_fifa_20_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "preprocess-fifa-21-node": KedroOperator(
            task_id="preprocess-fifa-21-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="preprocess_fifa_21_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "preprocess-fifa-22-node": KedroOperator(
            task_id="preprocess-fifa-22-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="preprocess_fifa_22_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "transformacion2-columns-fifa20-node": KedroOperator(
            task_id="transformacion2-columns-fifa20-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="transformacion2_columns_fifa20.node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "transformacion2-columns-fifa21-node": KedroOperator(
            task_id="transformacion2-columns-fifa21-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="transformacion2_columns_fifa21.node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "transformacion2-columns-fifa22-node": KedroOperator(
            task_id="transformacion2-columns-fifa22-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="transformacion2_columns_fifa22.node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "create-model-input-table-node": KedroOperator(
            task_id="create-model-input-table-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="create_model_input_table_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "division-datos-test-train-node-classification": KedroOperator(
            task_id="division-datos-test-train-node-classification",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="division_datos_test_train_node_classification",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "division-datos-test-train-node-regression": KedroOperator(
            task_id="division-datos-test-train-node-regression",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="division_datos_test_train_node_regression",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "entrenar-svr-cv-node": KedroOperator(
            task_id="entrenar-svr-cv-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="entrenar_svr_cv_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-decision-tree-model-clasificacion-node": KedroOperator(
            task_id="grid-decision-tree-model-clasificacion-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_decision_tree_model_clasificacion_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-decision-tree-model-node": KedroOperator(
            task_id="grid-decision-tree-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_decision_tree_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-knn-model-clasificacion-node": KedroOperator(
            task_id="grid-knn-model-clasificacion-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_knn_model_clasificacion_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-linear-model-node": KedroOperator(
            task_id="grid-linear-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_linear_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-linear-multiple-model-node": KedroOperator(
            task_id="grid-linear-multiple-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_linear_multiple_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-logistic-model-clasificacion-node": KedroOperator(
            task_id="grid-logistic-model-clasificacion-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_logistic_model_clasificacion_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-random-forest-model-clasificacion-node": KedroOperator(
            task_id="grid-random-forest-model-clasificacion-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_random_forest_model_clasificacion_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grid-randomforest-model-node": KedroOperator(
            task_id="grid-randomforest-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grid_randomforest_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "grind-svc-cv-model-clasificacion-node": KedroOperator(
            task_id="grind-svc-cv-model-clasificacion-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="grind_svc_cv_model_clasificacion_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-decisiontreeregressor-node": KedroOperator(
            task_id="evaluacion-decisiontreeregressor-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_DecisionTreeRegressor_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-randomforestregressor-node": KedroOperator(
            task_id="evaluacion-randomforestregressor-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_RandomForestRegressor_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-svr-node": KedroOperator(
            task_id="evaluacion-svr-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_SVR_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-decision-tree-node": KedroOperator(
            task_id="evaluacion-decision-tree-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_decision_tree_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-decision-tree-regression-node": KedroOperator(
            task_id="evaluacion-decision-tree-regression-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_decision_tree_regression_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-knn-node": KedroOperator(
            task_id="evaluacion-knn-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_knn_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-linearregression-multiple-node": KedroOperator(
            task_id="evaluacion-linearregression-multiple-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_linearRegression_multiple_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-linearregression-node": KedroOperator(
            task_id="evaluacion-linearregression-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_linearRegression_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-linear-model-regression-node": KedroOperator(
            task_id="evaluacion-linear-model-regression-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_linear_model_regression_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-linear-multiple-regression-node": KedroOperator(
            task_id="evaluacion-linear-multiple-regression-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_linear_multiple_regression_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-linear-randomforest-regression-node": KedroOperator(
            task_id="evaluacion-linear-randomforest-regression-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_linear_randomforest_regression_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-logisticregression-node": KedroOperator(
            task_id="evaluacion-logisticregression-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_logisticRegression_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-random-forest-node": KedroOperator(
            task_id="evaluacion-random-forest-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_random_forest_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-svc-node": KedroOperator(
            task_id="evaluacion-svc-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_svc_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "evaluacion-svr-regression-node": KedroOperator(
            task_id="evaluacion-svr-regression-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="evaluacion_svr_regression_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "report-decision-tree-model-classification-node": KedroOperator(
            task_id="report-decision-tree-model-classification-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="report_decision_tree_model_classification_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "report-grind-svc-cv-model-classification-node": KedroOperator(
            task_id="report-grind-svc-cv-model-classification-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="report_grind_svc_cv_model_classification_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "report-knn-model-classification-node": KedroOperator(
            task_id="report-knn-model-classification-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="report_knn_model_classification_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "report-logistic-model-classification-node": KedroOperator(
            task_id="report-logistic-model-classification-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="report_logistic_model_classification_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "report-random-forest-model-classification-node": KedroOperator(
            task_id="report-random-forest-model-classification-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="report_random_forest_model_classification_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        )
    }
    tasks["preprocess-fifa-20-node"] >> tasks["transformacion2-columns-fifa20-node"]
    tasks["preprocess-fifa-21-node"] >> tasks["transformacion2-columns-fifa21-node"]
    tasks["preprocess-fifa-22-node"] >> tasks["transformacion2-columns-fifa22-node"]
    tasks["transformacion2-columns-fifa20-node"] >> tasks["create-model-input-table-node"]
    tasks["transformacion2-columns-fifa21-node"] >> tasks["create-model-input-table-node"]
    tasks["transformacion2-columns-fifa22-node"] >> tasks["create-model-input-table-node"]
    tasks["create-model-input-table-node"] >> tasks["division-datos-test-train-node-classification"]
    tasks["create-model-input-table-node"] >> tasks["division-datos-test-train-node-regression"]
    tasks["division-datos-test-train-node-regression"] >> tasks["entrenar-svr-cv-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["grid-decision-tree-model-clasificacion-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["grid-decision-tree-model-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["grid-knn-model-clasificacion-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["grid-linear-model-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["grid-linear-multiple-model-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["grid-logistic-model-clasificacion-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["grid-random-forest-model-clasificacion-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["grid-randomforest-model-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["grind-svc-cv-model-clasificacion-node"]
    tasks["grid-decision-tree-model-node"] >> tasks["evaluacion-decisiontreeregressor-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-decisiontreeregressor-node"]
    tasks["grid-randomforest-model-node"] >> tasks["evaluacion-randomforestregressor-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-randomforestregressor-node"]
    tasks["entrenar-svr-cv-node"] >> tasks["evaluacion-svr-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-svr-node"]
    tasks["grid-decision-tree-model-clasificacion-node"] >> tasks["evaluacion-decision-tree-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["evaluacion-decision-tree-node"]
    tasks["grid-decision-tree-model-node"] >> tasks["evaluacion-decision-tree-regression-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-decision-tree-regression-node"]
    tasks["grid-knn-model-clasificacion-node"] >> tasks["evaluacion-knn-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["evaluacion-knn-node"]
    tasks["grid-linear-multiple-model-node"] >> tasks["evaluacion-linearregression-multiple-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-linearregression-multiple-node"]
    tasks["grid-linear-model-node"] >> tasks["evaluacion-linearregression-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-linearregression-node"]
    tasks["grid-linear-model-node"] >> tasks["evaluacion-linear-model-regression-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-linear-model-regression-node"]
    tasks["grid-linear-multiple-model-node"] >> tasks["evaluacion-linear-multiple-regression-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-linear-multiple-regression-node"]
    tasks["grid-randomforest-model-node"] >> tasks["evaluacion-linear-randomforest-regression-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-linear-randomforest-regression-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["evaluacion-logisticregression-node"]
    tasks["grid-logistic-model-clasificacion-node"] >> tasks["evaluacion-logisticregression-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["evaluacion-random-forest-node"]
    tasks["grid-random-forest-model-clasificacion-node"] >> tasks["evaluacion-random-forest-node"]
    tasks["grind-svc-cv-model-clasificacion-node"] >> tasks["evaluacion-svc-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["evaluacion-svc-node"]
    tasks["entrenar-svr-cv-node"] >> tasks["evaluacion-svr-regression-node"]
    tasks["division-datos-test-train-node-regression"] >> tasks["evaluacion-svr-regression-node"]
    tasks["grid-decision-tree-model-clasificacion-node"] >> tasks["report-decision-tree-model-classification-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["report-decision-tree-model-classification-node"]
    tasks["grind-svc-cv-model-clasificacion-node"] >> tasks["report-grind-svc-cv-model-classification-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["report-grind-svc-cv-model-classification-node"]
    tasks["grid-knn-model-clasificacion-node"] >> tasks["report-knn-model-classification-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["report-knn-model-classification-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["report-logistic-model-classification-node"]
    tasks["grid-logistic-model-clasificacion-node"] >> tasks["report-logistic-model-classification-node"]
    tasks["division-datos-test-train-node-classification"] >> tasks["report-random-forest-model-classification-node"]
    tasks["grid-random-forest-model-clasificacion-node"] >> tasks["report-random-forest-model-classification-node"]