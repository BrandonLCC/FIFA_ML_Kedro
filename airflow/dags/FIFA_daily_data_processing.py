from airflow import DAG
from datetime import datetime

from operators.kedro_operator import KedroOperator
from config import *

with DAG(
    dag_id="FIFA_daily_data_processing",
    schedule_interval="0 */4 * * *",   # cada 4 horas
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args=DEFAULT_DAG_ARGS,
    tags=TAGS["Data"],
) as dag:

    preprocess = KedroOperator(
        task_id="preprocess_data",
        package_name=KEDRO_PACKAGE_NAME,
        pipeline_name="data_processing",
        node_name=[],  # todos los nodos del pipeline
        project_path=KEDRO_PROJECT_PATH,
        env=KEDRO_ENV,
    )

    preprocess
