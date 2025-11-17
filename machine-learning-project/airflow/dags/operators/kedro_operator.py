from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from airflow.models import BaseOperator
from kedro.framework.project import configure_project
from kedro.framework.session import KedroSession

logger = logging.getLogger(__name__)


class KedroOperator(BaseOperator):

# Operador de Airflow para ejecutar pipelines y nodos de Kedro.

# Este operador crea una sesión de Kedro y ejecuta los nodos especificados

# de un pipeline de Kedro, integrando los flujos de trabajo de aprendizaje automático de Kedro con las capacidades de orquestación de Airflow.

#Argumentos:

# package_name: Nombre del paquete de Kedro (p. ej., 'spaceflights')

# pipeline_name: Nombre del pipeline que se va a ejecutar (p. ej., 'data_processing')

# node_name: Nombre(s) del/de los nodo(s) que se van a ejecutar
 
# project_path: Ruta a la raíz del proyecto de Kedro

# env: Entorno de Kedro que se va a usar (p. ej., 'local', 'production')

# conf_source: Ruta a los archivos de configuración

# Ejemplo:

# >>> task = KedroOperator(

# ... task_id="preprocess_data",

# ... package_name="spaceflights",

# ...pipeline_name="data_processing",

# ... node_name="preprocess_companies_node",

# ... ruta_proyecto="/app",

# ... entorno="local",

    ui_color = "#ffc900"
    ui_fgcolor = "#000000"

    def __init__(
        self,
        task_id: str,
        package_name: str,
        pipeline_name: str,
        node_name: str | list[str],
        project_path: str | Path,
        env: str = "local",
        conf_source: str = "",
        **kwargs,
    ):
        super().__init__(task_id=task_id, **kwargs)
        self.package_name = package_name
        self.pipeline_name = pipeline_name
        self.node_name = node_name if isinstance(node_name, list) else [node_name]
        self.project_path = Path(project_path)
        self.env = env
        self.conf_source = conf_source or str(self.project_path / "conf")

    def execute(self, context: Any):
        logger.info(f"Running Kedro pipeline={self.pipeline_name} nodes={self.node_name}")

        configure_project(self.package_name)

        with KedroSession.create(
            project_path=self.project_path,
            env=self.env,
            conf_source=self.conf_source,
        ) as session:
            session.run(
                pipeline_name=self.pipeline_name,
                node_names=self.node_name,
            )

        logger.info("Kedro Ejecución completada")
