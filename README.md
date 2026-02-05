# *Proyecto de análisis de Jugadores FIFA 20-22*

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Kedro](https://img.shields.io/badge/kedro-1.0.0-orange.svg)](https://kedro.org/)
[![EA](https://img.shields.io/badge/EA-%23000000.svg?logo=ea&logoColor=white)](#)

![image.png](https://assets.goal.com/images/v3/bltf84864c2d1921a81/Kylian%20Mbappe%20Real%20Madrid%20HIC.jpg?auto=webp&format=pjpg&width=3840&quality=60)

**Colaboradores:** Benjamin Andres Oviedo y Brandon Casas. 

**Docente:** Giocrisrai Godoy Bonillo.

## Introducción  

### Descripción del caso del proyecto

*[EA Sports FIFA](https://www.ea.com/es-es/games)*, es una saga de videojuegos de fútbol publicada anualmente por *Electronic Arts* bajo el sello de **EA Sports**, en colaboración con la **FIFA**.

### Problema / Necesidad del negocio

La empresa busca **replicar la experiencia del fútbol real**, tanto en la gestión de equipos como en la competencia dentro del campo, ofreciendo realismo gracias a sus licencias oficiales de equipos, jugadores y ligas de todo el mundo. Con la reciente transición a EA Sports FC, el objetivo principal sigue siendo simular el deporte del fútbol y permitir a los jugadores disputar partidos o gestionar un club en diversos modos de juego.

### Herramientas  y Framework 

#### Framework: 

**Kedro**

[Kedro](https://kedro.org/#get-started) es el framework principal de código abierto utilizado en este proyecto con el propósito de realizar el procesamiento y la limpieza de datos, el entrenamiento de modelos, la implementación de pipelines, entre otras tareas.

#### Herramientas 


[Jupyer notebooks](notebooks): 

[DVC con Dagshub](https://dagshub.com/): 

[Airflow-apache](https://airflow.apache.org/docs/apache-airflow/stable/start.html): 

[DockerHub](https://hub.docker.com/) y [DockerDesktop](https://docs.docker.com/desktop/): Entorno de pruebas 

**Librerias** 

Algunas de las librerías utilizadas durante las etapas de [Data Understanding](notebooks/02_Data_Understanding.ipynb), [Data Preparation](notebooks/03_Data_Preparation.ipynb) y [Modeling](notebooks/04_Modeling.ipynb) en Jupyter Notebook. De la misma forma, estas librerías son aplicadas dentro de los pipelines del proyecto.

- **numpy:** 
- **pandas:**
- **seaborn:**
- **matplotlib:**
- **sklearn:** 

## Datos de FIFA

### Datos obtenidos

El dataset (conjunto de datos) obtenidos para el proyecto es probeniente de [kaggle](https://www.kaggle.com/) en la que se obtuvieron los datasets de FIFA20 hasta FIFA22. En este proyecto se descartaron el uso de los datos de años anteriores al fifa20

### Acerca de los datos

Contiene más de 17.000 registros con atributos demográficos, características físicas, estadísticas de juego, detalles contractuales y afiliaciones a clubes.

**Enlace al dataset:** [Link](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1)	

## Objetivos

### Objetivos del proyecto

El objetivo principal del proyecto es desarrollar e integrar en un sistema funcionalidades basadas en modelos de predicción con machine learning, con el fin de generar análisis y predicciones automáticas sobre el desempeño de los jugadores de FIFA en función de determinadas características.

### Objetivos de Machine Learning

- Analizar y evaluar la calidad y veracidad de los datos utilizados, asi como realizar una correcta limpieza e imputación de datos faltantes para el desarrollo de los modelos de predicción.

- Creación de variables relevantes mediante feature engineering para enriquecer el conjunto de datos.

- Evaluar el desempeño de los modelos mediante métricas de rendimiento.

- Seleccionar las características más relevantes para los modelos de aprendizaje automático, aplicando **criterios** de importancia que optimicen su rendimiento.

- Construir e implementar un modelo de regresión que prediga el valor de mercado de un jugador en función de sus características (edad, habilidades técnicas, estadísticas de juego, potencial), entre otros factores relevantes.

- Construir un modelo de clasificación que categorice el rendimiento de los jugadores (por ejemplo: alto, medio o bajo) utilizando atributos clave que influyen en su desempeño.


La premisa central del machine learning (ML) es que si se optimiza el rendimiento de un modelo en un conjunto de datos de tareas que se asemejan adecuadamente a los problemas del mundo real para los que se usará, a través de un proceso llamado entrenamiento de modelos, el modelo puede hacer predicciones precisas sobre los nuevos datos que ve en su caso de uso final.

## Metodologia

### Metodologia CRISP-DM


Para mas información: [¿Qué es CRISP DM?](https://www.datascience-pm.com/crisp-dm-2/?utm_source=chatgpt.com)	

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


### Conclusiones 

