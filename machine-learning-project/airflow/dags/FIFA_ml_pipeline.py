# Dag maestro
#Este es el corazón que permite llamar pipelines y nodos de Kedro desde Airflow.

from airflow import DAG
from airflow.utils.task_group import TaskGroup
from datetime import datetime

from operators.kedro_operator import KedroOperator
from config import *

with DAG(
    dag_id="FIFA_ml_pipeline",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args=DEFAULT_DAG_ARGS,
    tags=TAGS["ML"],
) as dag:

    start = KedroOperator(
        task_id="start",
        package_name=KEDRO_PACKAGE_NAME,
        pipeline_name="__default__",  # pipeline completo
        node_name=[],
        project_path=KEDRO_PROJECT_PATH,
        env=KEDRO_ENV,
    )

    start
