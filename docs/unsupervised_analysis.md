# todo lo que tenga que ver con modelo no supervizado

## creacion y orgnaizcion para el aprendizaje no supervizados

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
    │   └── __init__.pyc
    ├── dimensionality_reduction/
    ├── anomaly_detection/
    └── association_rules/
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


¿Debe existir un flujo definido para el dataset en un pipeline no supervisado, por ejemplo aplicando primero detección de anomalías sobre la tabla de entrada, generando un clean_dataset, luego usando ese dataset limpio para clustering (clustered_data), y finalmente aplicar reducción de dimensionalidad, o es correcto que algunas técnicas sigan usando directamente la tabla imputada original?

Respuesta; 

Sí, debe existir un flujo lógico para el dataset no supervisado, y ese flujo normalmente tiene como base un clean_dataset.
Tiene sentido aplicar detección de anomalías primero sobre la tabla imputada para limpiar o marcar outliers y generar un dataset estable (clean_dataset). A partir de ese dataset limpio, clustering y reducción de dimensionalidad deberían usar el mismo clean_dataset como input, **no encadenarse obligatoriamente entre sí.** La reducción de dimensionalidad no necesita recibir el output del clustering, salvo que se use únicamente con fines de visualización. Por lo tanto, si actualmente el pipeline de reducción de dimensionalidad usa la tabla imputada original, no está mal, pero lo más coherente y consistente es que use el clean_dataset, ya que representa el estado validado y confiable de los datos para las técnicas no supervisadas.