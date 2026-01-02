# *Proyecto de análisis de Jugadores FIFA 20-22*

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Kedro](https://img.shields.io/badge/kedro-1.0.0-orange.svg)](https://kedro.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![EA](https://img.shields.io/badge/EA-%23000000.svg?logo=ea&logoColor=white)](#)

![image.png](https://assets.goal.com/images/v3/bltf84864c2d1921a81/Kylian%20Mbappe%20Real%20Madrid%20HIC.jpg?auto=webp&format=pjpg&width=3840&quality=60)

**Autores:** Benjamin Andres Oviedo y Brandon Casas. 

**Docente:** Giocrisrai Godoy Bonillo.

## Introducción  

### Contexto del caso

*EA Sports FIFA*, conocido simplemente como FIFA, es una saga de videojuegos de fútbol publicada anualmente por *Electronic Arts* bajo el sello de EA Sports, en colaboración con la FIFA.

### Problema / Necesidad del negocio

La empresa busca **replicar la experiencia del fútbol real**, tanto en la gestión de equipos como en la competencia dentro del campo, ofreciendo realismo gracias a sus licencias oficiales de equipos, jugadores y ligas de todo el mundo. Con la reciente transición a EA Sports FC, el objetivo principal sigue siendo simular el deporte del fútbol y permitir a los jugadores disputar partidos o gestionar un club en diversos modos de juego.

### Herramientas  y Framework (mejora o elimina)

Este proyecto utiliza la herramienta [Kedro](https://kedro.org/#get-started) para el procesamiento de datos de FIFA y aplicar técnicas de aprendizaje no supervisado y supervisado para predecir métricas y categorías de jugadores.

Se incluyen pipelines de limpieza, reducción de dimensionalidad, clustering y entrenamiento de modelos de regresión y clasificación.

## Datos

### Datos obtenidos

El dataset (conjunto de datos) obtenidos para el proyecto es probeniente de [kaggle](https://www.kaggle.com/) en la que se obtuvieron los datasets de FIFA20 hasta FIFA22. En este proyecto se descartaron el uso de los datos de años anteriores al fifa20

### Acerca de los datos

Contiene más de 17.000 registros con atributos demográficos, características físicas, estadísticas de juego, detalles contractuales y afiliaciones a clubes.

**Enlace al dataset:** [Link](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1)	


Características claves 

Caracteristicas de modelos 

Clasificacion 

Regresion: 

### Objetivos

**Objetivos del proyecto**

El objetivo principal del proyecto es desarrollar e integrar en un sistema funcionalidades basadas en modelos de predicción con machine learning, con el fin de generar análisis y predicciones automáticas sobre el desempeño de los jugadores de FIFA en función de determinadas características.


### **Objetivos de Machine Learning**

- Analizar y evaluar la calidad y veracidad de los datos utilizados, asi como realizar una correcta limpieza e imputación de datos faltantes para el desarrollo de los modelos de predicción.

- Creación de variables relevantes mediante feature engineering para enriquecer el conjunto de datos.

- Evaluar el desempeño de los modelos mediante métricas de rendimiento.

- Seleccionar las características más relevantes para los modelos de aprendizaje automático, aplicando **criterios** de importancia que optimicen su rendimiento.

- Construir e implementar un modelo de regresión que prediga el valor de mercado de un jugador en función de sus características (edad, habilidades técnicas, estadísticas de juego, potencial), entre otros factores relevantes.

- Construir un modelo de clasificación que categorice el rendimiento de los jugadores (por ejemplo: alto, medio o bajo) utilizando atributos clave que influyen en su desempeño.


## Metodologias  

### Metodologia CRISP-DM


Notebooks: 

[Business Understanding](notebooks\01_Business_Understanding.ipynb)

[Data Understanding](notebooks\02_Data_Understanding.ipynb)

[Data Preparation](notebooks\03_Data_Preparation.ipynb)

[Modeling](notebooks\04_Modeling.ipynb)

[Final analysis](notebooks\06_final_analysis.ipynb)

### Repositorios 

[DockerHub](https://hub.docker.com/repository/docker/brandonlcc/fifa_ml_kedro/general)

[DVC con Dagshub](https://dagshub.com/br.casas/ML-Kedro-FIFA-DVC)

[Deployment FIFA](#)

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

- Resultados com implementación de modelos no supervizados

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

