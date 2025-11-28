"""
Este pipeline llamado "Unsupervised_learning" sera el pipeline orquestador para los 
submodulos de pipeline

- 01_dimensionality_reduction
- 02_clustering
- 03_anomaly_detection
- 04_association_rules

-- Tomar en cuenta -- 

1. Realizar las configuraciónes de los parametros en catalog
2. Flujo correspondiente en airflow: data_engineering → supervised → unsupervised → reporting - 
3. Crear y configurar los submodulos (pipelines) manualmente (_init_.py, nodes.py y pipeline.py) - ok
4. modificar y Conectar los pipelines en pipeline_registry.py - ok

5. El consejo que dio el profesor en clases. 
   - Re-entrenar los modelos supervisados usando datos transformados por los pipelines no supervisados.

    raw_data
    ↓
    data_processing
    ↓
    unsupervised (dimred → clustering → anomaly_clean)
    ↓
    clean_and_clustered_dataset
    ↓
    supervised_training (reg o clasif)
    ↓
    metrics + report

"""

"""
Logica 

1. La idea es que hagamos los clustering o todo esto no supervizado y entender

¿En que nos va a mejorar los datos?

Ejemplo: Nos dimos cuenta que existen 2 o 4 grupos. y con esto hacer nuevamente un analis exploratorio de los datos


"""

from kedro.pipeline import Node, Pipeline  # noqa

from .clustering.pipeline import create_pipeline as clustering_pipeline
from .dimensionality_reduction.pipeline import create_pipeline as dimred_pipeline
from .anomaly_detection.pipeline import create_pipeline as anomaly_pipeline

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        dimred_pipeline(),
        clustering_pipeline(),
        anomaly_pipeline(),

    ])
