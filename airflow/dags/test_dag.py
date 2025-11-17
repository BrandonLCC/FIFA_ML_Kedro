from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dag_de_prueba",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    tarea = BashOperator(
        task_id="tarea_test",
        bash_command="echo 'Airflow funciona!'"
    )
