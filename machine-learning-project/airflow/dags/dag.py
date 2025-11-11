from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 11, 10),
    'retries': 1
}

# Define tu DAG
with DAG(
    dag_id='kedro_pipeline_dag',
    default_args=default_args,
    schedule_interval=None,  # Se ejecuta manualmente
    catchup=False,
    tags=['kedro']
) as dag:

    # Comando para ejecutar un pipeline de Kedro
    ejecutar_pipeline = BashOperator(
        task_id='ejecutar_pipeline',
        bash_command='cd /opt/airflow/machine-learning-project && kedro run'
    )
