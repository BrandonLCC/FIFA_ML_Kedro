"""
Este pipeline llamado "Unsupervised_learning" sera el pipeline orquestador para los 
submodulos de pipeline

- 01_dimensionality_reduction (obligatorio)
- 02_clustering (obligatorio)
- 03_anomaly_detection (opcional)
- 04_association_rules (opcional)

-- Tomar en cuenta para configurar el pipeline -- 

1. Crear y configurar los submodulos (pipelines) manualmente (_init_.py, nodes.py y pipeline.py) - ok
2. Realizar las configuraciónes en catalog y los parametros etc
3. modificar y Conectar los pipelines en pipeline_registry.py - ok
4. El consejo que dio el profesor en clases. 
   
   Re-entrenar los modelos supervisados usando datos transformados por los pipelines no supervisados.

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

Ejemplo: Nos dimos cuenta que existen 5 o 4 grupos. eso lo podemos agrupar,  
y con esto hacer nuevamente un analis exploratorio de los datos
podemos decir, grupo 1,2,3 o 4. pueden ser categorias, esas categorias, insertarlo en los dos mejores modelos
de regresion y clasificicacion y incluir esas variables ver si mejora o empeora en esos modelos.

seria reentrenar pero a partir de todo esto. 

Con esto: 

- Entrenar y tomar en cuenta esta nueva variable creada (clustering)
- aplicar el PCA (Reduccion de dimensionalidad) aplicarlo a los datos 
que nosotros tenemos para entrenar los modelos que ya existian para entrenar mas rapido (con los features del los modelos o el dataset completo?)

Esto es normal cuando:

- quieres limpiar outliers (anomalías),
- quieres simplificar los datos (reducción de dimensionalidad),
- quieres agrupar datos similares (clustering),
- usar esos datos procesados para mejorar un modelo supervisado.

¿Por qué el no supervisado puede mejorar los modelos supervisados?

1. Detección de anomalías
- Quitas valores extremados o incorrectos.
- Esto mejora precisión y estabilidad.

2. Clustering

- Añade información estructural a los datos (Cluster IDs).
- permite separar conjuntos de entrenamiento por grupos.

3. Reducción de dimensionalidad (PCA / t-SNE / UMAP)

- Hace los datos más livianos.
- Reduce ruido.
- Acelera el entrenamiento.


Flujo casi exacto del los pipelines 

RAW → INTERMEDIATE → PRIMARY → FEATURE
    → UNSUPERVISED → CLEAN_DATASET → MODEL_INPUT
    → TRAIN_SUPERVISED → MODEL_OUTPUT

Tambien nos pide un pipeline que orqueste todo (eso no se si es verdad)

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
