from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def run_kedro_pipeline(pipeline_name: str, node_name: str = None):
    """Ejecuta un pipeline o un nodo específico de Kedro."""
    command = ["kedro", "run", "--pipeline", pipeline_name]
    if node_name:
        command += ["--node", node_name]
    subprocess.run(command, check=True)

with DAG(
    'kedro_master_dag',
    default_args=default_args,
    description='DAG maestro para pipelines Kedro',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['kedro', 'ml_project']
) as dag:

    # -----------------------------
    # PIPELINE: data_engineering
    # -----------------------------
    de_cleaning = PythonOperator(
        task_id='data_cleaning',
        python_callable=run_kedro_pipeline,
        op_args=['data_engineering', 'data_cleaning_node']
    )

    de_feature_engineering = PythonOperator(
        task_id='feature_engineering',
        python_callable=run_kedro_pipeline,
        op_args=['data_engineering', 'feature_engineering_node']
    )

    # -----------------------------
    # PIPELINE: supervised
    # -----------------------------
    supervised_linear_reg = PythonOperator(
        task_id='linear_regression_model',
        python_callable=run_kedro_pipeline,
        op_args=['supervised_models', 'linear_regression_node']
    )

    supervised_random_forest = PythonOperator(
        task_id='random_forest_model',
        python_callable=run_kedro_pipeline,
        op_args=['supervised_models', 'random_forest_node']
    )

    # -----------------------------
    # PIPELINE: unsupervised
    # -----------------------------
    unsupervised_pca = PythonOperator(
        task_id='pca_reduction',
        python_callable=run_kedro_pipeline,
        op_args=['unsupervised_learning', 'pca_node']
    )

    unsupervised_clustering = PythonOperator(
        task_id='clustering',
        python_callable=run_kedro_pipeline,
        op_args=['unsupervised_learning', 'clustering_node']
    )

    # -----------------------------
    # DEPENDENCIAS
    # -----------------------------
    de_cleaning >> de_feature_engineering
    de_feature_engineering >> [supervised_linear_reg, supervised_random_forest]
    [supervised_linear_reg, supervised_random_forest] >> unsupervised_pca
    unsupervised_pca >> unsupervised_clustering
