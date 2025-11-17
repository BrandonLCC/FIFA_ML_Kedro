from airflow import DAG
from datetime import datetime

from operators.kedro_operator import KedroOperator
from config import *

with DAG(
    dag_id="FIFA_on_demand",
    schedule_interval=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args=DEFAULT_DAG_ARGS,
    tags=TAGS["ML"],
) as dag:

    run_all = KedroOperator(
        task_id="run_full_pipeline",
        package_name=KEDRO_PACKAGE_NAME,
        pipeline_name="__default__",
        node_name=[],
        project_path=KEDRO_PROJECT_PATH,
        env=KEDRO_ENV,
    )

    run_all
