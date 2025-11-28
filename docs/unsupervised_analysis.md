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

# Notebooks

```
notebooks/
├── 01-04_notebooks_EP1_EP2/      # ya existen
├── 05_unsupervised/  # <-- NUEVA CARPETA
│   ├── 01_clustering_kmeans.ipynb
│   ├── 02_clustering_dbscan.ipynb
│   ├── 03_clustering_hierarchical.ipynb
│   ├── 04_pca_analysis.ipynb
│   ├── 05_tsne_umap_analysis.ipynb
│   ├── 06_anomaly_detection.ipynb         (opcional)
│   ├── 07_association_rules.ipynb         (opcional)
│   └── resumen_unsupervised.ipynb  # <- para defensa
├── 06_final_analysis.ipynb
```
### Contenido esperado

# 01_clustering_kmeans.ipynb
- Estandarización
- Elbow Method
- Silhouette Score
- Calinski-Harabasz
- Visualizaciones
- Insights por cluster

# 02_clustering_dbscan.ipynb
- Búsqueda de eps y min_samples
- Visualización
- Comparación con KMeans

# 03_clustering_hierarchical.ipynb
- Dendrograma
- Distancias
- Interpretación

# 04_PCA.ipynb
- Varianza explicada
- Scree plot
- Loading matrix
- Biplot
- Cómo afecta supervisados

# 05_tsne_umap.ipynb
- Parámetros (perplexity, n_neighbors, min_dist)
- Mapas 2D
- Mapas 3D
- Comparación entre técnicas

# 06_anomalias.ipynb (opcional)
- Isolation Forest
- LOF
- Comparación
- Visualización

# 07_association_rules.ipynb (opcional)
- Apriori
- Support / confidence / lift
- Reglas importantes

# 08_resumen_unsupervised.ipynb
- Resultados finales
- Visualizaciones limpias
- Comparación entre técnicas
- Conclusiones
- Decisiones justificadas

# Link a las etapas en Kedro
- Formato README.md
