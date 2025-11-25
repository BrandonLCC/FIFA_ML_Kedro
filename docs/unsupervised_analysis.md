# todo lo que tenga que ver con modelo no supervizado

## creacion y orgnaizcion para los modelos no supervizados

1. primero creamos el pipeline

```Bash
    kedro pipeline create unsupervised_learning
```
2. creamos las carpetas o submodulos de pipeline manualmente para tener la esctructura pedida
```
src/proyecto_ml/pipelines/unsupervised_learning/
    ├── clustering/
    │   ├── nodes.py
    │   ├── pipeline.py
    │   └── __init__.py
    ├── dimensionality_reduction/
    ├── anomaly_detection/
    └── association_rules/
```
3. combinas todo en el __init__.py del pipeline principal

proposito: 

| Función                      | Explicación                                            |
| ---------------------------- | ------------------------------------------------------ |
| Convierte carpeta en paquete | Python puede importarla                                |
| Ayuda a Kedro                | Kedro encuentra pipelines automáticamente              |
| Exporta el pipeline          | Defines `create_pipeline()` para combinar subpipelines |
| Organiza el módulo           | Es el punto de entrada del pipeline                    |



```BASH
Crear un __init__

from kedro.pipeline import pipeline
from .clustering.pipeline import create_pipeline as clustering_pipeline
from .dimensionality_reduction.pipeline import create_pipeline as dr_pipeline

def create_pipeline(**kwargs):
    return pipeline([
        clustering_pipeline(),
        dr_pipeline(),
    ])
```


## ESTRUTURAS 

ESTRUCTURA DEL PIPELINE

```
├── unsupervised_learning/  
    ├── clustering/ 
    ├── dimensionality_reduction/ 
    ├── anomaly_detection/ 
    └── association_rules/ 
```

ESTRUCTURA FINAL
```
unsupervised_learning/
    __init__.py
    pipeline.py
    
    clustering/
        __init__.py
        kmeans.py
        dbscan.py
        hierarchical.py
        gmm.py
        metrics.py
        elbow.py
        dendrogram.py

    dimensionality_reduction/
        __init__.py
        pca.py
        tsne.py
        umap.py

    anomaly_detection/
        __init__.py
        isolation_forest.py
        lof.py

    association_rules/
        __init__.py
        apriori.py
        fpgrowth.py

    utils/
        __init__.py
        plotting.py
        helpers.py
```