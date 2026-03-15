"""
Este pipeline llamado "Unsupervised_learning" sera el pipeline orquestador para los 
submodulos de pipeline

- 01_dimensionality_reduction (obligatorio)
- 02_clustering (obligatorio)
- 03_anomaly_detection (opcional)
- 04_association_rules (opcional)

-- Tomar en cuenta para configurar el pipeline -- 

1. Crear y configurar los submodulos (pipelines) manualmente (_init_.py, nodes.py y pipeline.py) - ok
2. Realizar las configuraciónes en catalog y los parametros etc - ok
3. modificar y Conectar los pipelines en pipeline_registry.py - ok
4. El consejo que dio el profesor en clases. 
   
   Re-entrenar los modelos supervisados usando datos transformados por los pipelines no supervisados. (Confirmado y bien hecho: 09/03/2026)

    Flujo: correcto 

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

Objetivo del pipeline padre

El pipeline padre debe:

- Leer el dataset desde 03_primary
- Aplicar en orden:
    PCA
    Clustering
    Anomaly Detection

- Retornar un clean_dataset final que será guardado en 04_feature

Ese dataset será usado luego por data_processing para hacer el train/test split. ojo aqui, no se si en data_prcoesing pero si verificar si crear nuesvo train test _nosupervisado o algo asi para no mezclarlo con el train test original.

Flujo casi exacto del los pipelines 

RAW → INTERMEDIATE → PRIMARY → FEATURE
    → UNSUPERVISED → CLEAN_DATASET → MODEL_INPUT
    → TRAIN_SUPERVISED → MODEL_OUTPUT
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import merge_dimensionality_with_dataset
from .dimensionality_reduction.pipeline import create_pipeline as pca_pipeline
from .clustering.pipeline import create_pipeline as clustering_pipeline

def create_pipeline(**kwargs) -> Pipeline:
    pca = pca_pipeline()

    prepare_nodes = [
        node(
            func=merge_dimensionality_with_dataset,
            inputs=["model_input_table", "pca_output"],
            outputs="model_input_table_with_pca",
            name="merge_dimensionality_node"
        ),
        #node(
        #    # cuidado con esta funsion, verificar para no confidirte 
        #    func=func_dataset_for_clustering, # funcion no hace mucho y se puede modificar para que no sea solo PCA
        #    inputs="model_input_table_with_pca",
        #    outputs="dataset_for_clustering",
        #    name="prepare_clustering_dataset_node"
        #),

        # No se usara esta funcion ya que el submodulo de clustering 
        # Ya realiza la integracion de los clusteres con el dataset limpio, por lo que no es necesario hacer una funcion adicional para esto.

        #node(
        #    func=merge_clusters_with_dataset,
        #    inputs=[
        #        "model_input_table_with_pca", # pca y modelo imput
        #        "dataset_with_best_clusters" # clusteres 
        #    ],
        #    outputs="reduccion_clustering_dataset_final", # componentes + clusteres + model imput
        #
        #    name="merge_clusters_dataset_node"
        #),
    ]

    clustering = clustering_pipeline()

    return pipeline([
        pca,
        prepare_nodes[0],   # merge_dimensionality_node
        clustering,
])
 
 # (Faltan modificar cosas para desactivar el pipeline de deteccion de anomalias.)