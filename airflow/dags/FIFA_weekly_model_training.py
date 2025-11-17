from airflow import DAG
from datetime import datetime

from operators.kedro_operator import KedroOperator
from config import *

with DAG(
    dag_id="FIFA_weekly_model_training",
    schedule_interval="0 3 * * 0",  # domingo a las 3am
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args=DEFAULT_DAG_ARGS,
    tags=TAGS["ML"],
) as dag:

    train = KedroOperator(
        task_id="train_model",
        package_name=KEDRO_PACKAGE_NAME,
        pipeline_name="model_training",
        node_name=[],
        project_path=KEDRO_PROJECT_PATH,
        env=KEDRO_ENV,
    )

    train
