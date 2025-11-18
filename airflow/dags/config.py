from datetime import timedelta
from pathlib import Path

# Nombre del paquete Kedro (tu proyecto)
KEDRO_PACKAGE_NAME = "PROYECTO_ML_KEDRO"   
KEDRO_PACKAGE_NAME = "machine-learning-project"   

# Ruta del proyecto dentro del contenedor Airflow ok?
#KEDRO_PROJECT_PATH = Path("machine-learning-project\airflow")

# opcion 2 con docker

KEDRO_PROJECT_PATH = Path("/app")
#KEDRO_CONF_SOURCE = str(KEDRO_PROJECT_PATH / "conf")

# Carpeta de configuración
#KEDRO_CONF_SOURCE = KEDRO_PROJECT_PATH / "conf" # (anterior)
KEDRO_CONF_SOURCE = "/app/conf" # (con docker)


# Entorno usado por Kedro
KEDRO_ENV = "local"

# Etiquetas comunes para clasificar DAGs
TAGS = {
    "ML": ["machine-learning", "kedro", "pipeline"],
    "ETL": ["etl", "processing"],
    "DAILY": ["daily"],
    "WEEKLY": ["weekly"],
}

# Configuración por defecto para todos los DAGs
DEFAULT_DAG_ARGS = {
    "owner": "brandon",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
    "email_on_retry": False,
}

