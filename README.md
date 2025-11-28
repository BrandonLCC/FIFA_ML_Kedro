# *FIFA Player Analysis Project*

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Kedro](https://img.shields.io/badge/kedro-1.0.0-orange.svg)](https://kedro.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Este proyecto utiliza Kedro para procesar datos de FIFA y aplicar técnicas de aprendizaje no supervisado y supervisado para predecir métricas y categorías de jugadores.

Se incluyen pipelines de limpieza, reducción de dimensionalidad, clustering y entrenamiento de modelos de regresión y clasificación.

# Contenido

- Instalación
- Estructura del proyecto
- Ejecución de pipelines
- Descripción de pipelines
- Modelos entrenados
- Métricas de evaluación
- Visualización
- Notas

# Instalación

```bash
git clone <url_del_proyecto>
cd machine_learning_project
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
pip install --upgrade pip
pip install -r requirements.txt
```
## Estructura del proyecto

```
machine_learning_project/
│
├── data/
│   ├── 01_raw/                  # Datos originales CSV
│   ├── 02_intermediate/         # Datos preprocesados
│   ├── 04_feature/              # Features generadas con unsupervised
│   ├── 05_model_input/          # Datasets para entrenamiento y test
│   ├── 06_models/               # Modelos entrenados (Pickle)
│   └── 08_reporting/            # Reportes de métricas
│
├── src/
│   ├── pipelines/
│   │   ├── unsupervised_learning/
│   │   └── supervised_models/
│   ├── nodes.py
│   └── catalog.yml
│
├── conf/
│   ├── base/
│   │   ├── parameters.yml       # Configuración de parámetros
│   │   └── catalog.yml          # Catalog de datasets
│   └── local/
│
├── README.md
└── requirements.txt
```

## Estructura de los pipelines 
```
├── classification_models
│   
├── classification_report
│ 
├── data_processing
│ 
├── final_report_comparativo
│ 
├── regression_models
│ 
├── regression_report
│ 
├── unsupervised_learning
│   │
│   ├── anomaly_detection
│   │   
│   ├── association_rules
│   │
│   ├── clustering
│   │   
│   ├── dimensionality_reduction
│   
├───unsupervised_to_supervised   

```

### Descripción de pipelines

| Pipeline                   | Función                                                               |
| -------------------------- | --------------------------------------------------------------------- |
| unsupervised_learning      | Limpieza de datos, reducción de dimensionalidad, clustering y reglas. |
| supervised_models          | Entrena modelos de regresión y clasificación usando dataset limpio.   |
| unsupervised_to_supervised | Genera datasets de train/test a partir del dataset limpio.            |


### Modelos implementados

| Modelo              | Tipo          | Archivo (.pkl)                              |
| ------------------- | ------------- | ------------------------------------------- |
| Linear Regression   | Regresión     | grid_linear_model.pkl                       |
| SVR                 | Regresión     | grid_svr_model.pkl                          |
| Decision Tree       | Regresión     | grid_decision_tree_model.pkl                |
| Random Forest       | Regresión     | grid_randomforest_model.pkl                 |
| Logistic Regression | Clasificación | grid_logistic_model_classification.pkl      |
| KNN                 | Clasificación | grid_knn_model_classification.pkl           |
| Decision Tree       | Clasificación | grid_decision_tree_model_classification.pkl |
| Random Forest       | Clasificación | grid_random_forest_model_classification.pkl |

### Metricas de evaluación 

#### Regresión

| Modelo            | MSE             | RMSE       | R²     |
| ----------------- | --------------- | ---------- | ------ |
| Random Forest     | 952,778,836,132 | 976,103.91 | 0.9353 |
| Decision Tree     | ...             | ...        | ...    |
| Linear Regression | ...             | ...        | ...    |

#### Clasificación

| Modelo              | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Decision Tree       | 0.0975   | 0.0996    | 0.0975 | 0.0915   |
| Random Forest       | 0.1075   | 0.1129    | 0.1075 | 0.0974   |
| Logistic Regression | ...      | ...       | ...    | ...      |


### Visualización

Usa Kedro-Viz para explorar tus pipelines:

kedro viz

### DVC 
Link del repositorio de versionamiento 

https://dagshub.com/br.casas/ML-Kedro-FIFA-DVC