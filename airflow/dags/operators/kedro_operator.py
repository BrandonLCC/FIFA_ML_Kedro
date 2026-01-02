from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Union

from airflow.models import BaseOperator
from kedro.framework.project import configure_project
from kedro.framework.session import KedroSession

logger = logging.getLogger(__name__)

class KedroOperator(BaseOperator):
    ui_color = "#ffc900"
    ui_fgcolor = "#000000"

    def __init__(
        self,
        task_id: str,
        package_name: str,
        pipeline_name: str,
        node_name: Union[str, list[str]],
        project_path: str | Path,
        env: str = "local",
        conf_source: str = "",
        **kwargs,
    ):
        super().__init__(task_id=task_id, **kwargs)
        self.package_name = package_name
        self.pipeline_name = pipeline_name
        self.node_name = [node_name] if isinstance(node_name, str) else node_name
        self.project_path = Path(project_path)
        self.env = env
        self.conf_source = str(conf_source) if conf_source else str(self.project_path / "conf")

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
