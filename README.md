# *Proyecto de análisis de Jugadores FIFA 20-22*

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Kedro](https://img.shields.io/badge/kedro-1.0.0-orange.svg)](https://kedro.org/)
[![EA](https://img.shields.io/badge/EA-%23000000.svg?logo=ea&logoColor=white)](#)

![image.png](https://assets.goal.com/images/v3/bltf84864c2d1921a81/Kylian%20Mbappe%20Real%20Madrid%20HIC.jpg?auto=webp&format=pjpg&width=3840&quality=60)

**Colaboradores:** Benjamin Andres Oviedo y Brandon Casas. 

**Docente:** Giocrisrai Godoy Bonillo.

## Contenido 

### Descripción del caso del proyecto *

*[EA Sports FIFA](https://www.ea.com/es-es/games)*, es una saga de videojuegos de fútbol publicada anualmente por *Electronic Arts* bajo el sello de **EA Sports**, en colaboración con la **FIFA**.

### Necesidad del negocio / Problema *

La empresa busca **replicar la experiencia del fútbol real**, tanto en la gestión de equipos como en la competencia dentro del campo, ofreciendo realismo gracias a sus licencias oficiales de equipos, jugadores y ligas de todo el mundo. Con la reciente transición a EA Sports FC, el objetivo principal sigue siendo simular el deporte del fútbol y permitir a los jugadores disputar partidos o gestionar un club en diversos modos de juego.

Es por eso..

## Datos de FIFA

### Datos obtenidos

El dataset (conjunto de datos) obtenidos para el proyecto es probeniente de [kaggle](https://www.kaggle.com/) en la que se obtuvieron los datasets de FIFA20 hasta FIFA22. En este proyecto se descartaron el uso de los datos de años anteriores al fifa20

### Acerca de los datos

Contiene más de 17.000 registros con atributos demográficos, características físicas, estadísticas de juego, detalles contractuales y afiliaciones a clubes.

**Enlace al dataset:** [Link](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1)	

## Objetivos

### Objetivo del proyecto

El objetivo principal del proyecto es desarrollar e integrar en un sistema funcionalidades basadas en modelos de predicción, aplicando técnicas de machine learning, con el fin de generar análisis y predicciones automáticas sobre el desempeño de los jugadores de FIFA en función de sus características, **contribuyendo a la simulación del fútbol real y al modelado del rendimiento de los jugadores en distintos escenarios de juego**, alineándose con la necesidad de la empresa de ofrecer una experiencia realista y basada en datos.

### Objetivos de Machine Learning *

La premisa central del machine learning (ML) es que si se optimiza el rendimiento de un modelo en un conjunto de datos de tareas que se asemejan adecuadamente a los problemas del mundo real para los que se usará, a través de un proceso llamado entrenamiento de modelos, el modelo puede hacer predicciones precisas sobre los nuevos datos que ve en su caso de uso final. [ML](https://www.ibm.com/mx-es/think/topics/machine-learning)	

---
<!-- TEXTO README hecho por el colaborador
     
     El texto visualizado en el repositorio fue simplicado por CHATGPT 

"""

## Metodologia CRISP-DM **

La metodología CRISP-DM es un modelo de proceso estandarizado para llevar a cabo proyectos de minería de datos y, por extensión, de machine learning. Fue desarrollada a finales de la década de 1990 por un consorcio de empresas como SPSS, Daimler AG y NCR. Su objetivo principal es proporcionar una guía **flexible** y no propietaria que sea aplicable a una amplia variedad de industrias y problemas.

> CRISP-DM es ideal para Proyectos de Data Science e IA: Modelado de predicción, detección de anomalías y sistemas de recomendación.


### Fases de CRISP-DM

Se aplican las 6 fases de La metodologia CRISP-DM. A continuación, se presenta un breve resumen de cada fases del proyecto y las tareas realizadas en cada una:

- **la comprension del negocio:** 
Se orienta a indetificar y entender las necesidades del cliente. En esta fase definimos los objetivos del proyecto y se evalua la situación desde distintos puntos de vista, tanto del contexto empresarial como de  los recursos monetarios asignados. Asi mismo se analizan los riesgos, alcances y costos asociados.

- **Comprension de datos:** 
En esta fase, estudiamos en detalle los datos obtenidos. La comprensión de datos implicando acceder a ellos y explorarlos mediante tablas y gráficos. En esta etapa se realizan tareas como la recopilación de datos, la descripción de los resultados, la identificación de anomalías, la exploración inicial y la verificación de la calidad de los datos.

- **Modelado:** 
Luego de la comprención de los datos, se utilizó **kedro** para realizar una limpieza de datos automatizada. Posteriormente, se seleccionaron las técnicas de modelos mas adecuados. En este proyecto se realizaron:

-  Modelos supervizados de regresión.

- Modelos supervizados de clasificación.

- Modelos no supervizados. 

---

- **Evaluación:**
Esta etapa se centra en la **evaluacion tecnica de los modelos**, considerando diferentes tipos de aspectos de desempeño y alineado con los objetivos del negocio 

- **Evaluación de resultados:** Modelos que cumplan con los criterios de exito empresarial utilizando métricas de desempeño aceptables como R², F1-Score, entre otras.

- **Proceso de revisión:** Se revisan los parámetros aplicados, los pasos ejecutados durante el modelado y los hallazgos obtenidos, así como posibles errores o anomalías identificadas.

- **Despliegue:** 
Etapa final en la que se ponen a prueba los resultados obtenidos. En esta fase se realiza un entregable funcional, en el cual se ponen en uso los modelos desarrollados o las funciones basadas en dichos modelos, permitiendo su aplicación en un entorno real o de prueba Y da por finalizado las etapas de CRISP-DM 

> Dependiendo de las necesidades de la organización es posible una o mas fases.

En general, la fase de despliegue de CRISP-DM incluye dos tipos de actividades:

- Planificación y control del despliegue de los resultados

- Finalización de tareas de presentación como la producción de un informe final y la revisión de un proyecto

-->

# Metodología CRISP-DM

La metodología **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*) es un modelo estandarizado para proyectos de **minería de datos** y **machine learning**.  
Fue desarrollada a finales de los años 90 por empresas como **SPSS, Daimler AG y NCR**, y proporciona una guía **flexible y no propietaria**, aplicable a diferentes industrias y tipos de problemas.

> **CRISP-DM es ideal para proyectos de Data Science e Inteligencia Artificial**  
> - Modelado de predicción  
> - Detección de anomalías  
> - Sistemas de recomendación

---

### Fases de CRISP-DM

Se aplican las seis fases de CRISP-DM. A continuación se detallan cada fase y las tareas realizadas:

---

### 1. Comprensión del negocio
- **Objetivo:** Identificar y entender las necesidades del cliente.  
- **Tareas principales:**  
  - Definir los objetivos del proyecto  
  - Evaluar el contexto empresarial y los recursos asignados  
  - Analizar riesgos, alcances y costos

---

### 2. Comprensión de los datos
- **Objetivo:** Estudiar los datos en detalle y explorarlos mediante tablas y gráficos.  
- **Tareas principales:**  
  - Recopilación de datos  
  - Descripción de resultados  
  - Identificación de anomalías  
  - Exploración inicial  
  - Verificación de la calidad de los datos

---

### 3. Modelado
- **Objetivo:** Construir modelos que respondan a los objetivos del proyecto.  
- **Herramienta utilizada:** **Kedro** (para limpieza automatizada de datos)  
- **Modelos desarrollados:**  
  - Supervisados de **regresión**  
  - Supervisados de **clasificación**  
  - **No supervisados**

---

### 4. Evaluación
- **Objetivo:** Evaluar el desempeño técnico de los modelos y su alineación con los objetivos de negocio.  
- **Evaluación de resultados:**  
  - Modelos que cumplan con criterios de éxito empresarial  
  - Métricas utilizadas: **R²**, **F1-Score**, entre otras  
- **Proceso de revisión:**  
  - Revisión de parámetros aplicados  
  - Pasos ejecutados durante el modelado  
  - Hallazgos, errores o anomalías detectadas

---

### 5. Despliegue

- **Objetivo:** Poner a prueba y entregar los modelos de manera funcional.  
- **Actividades principales:**  
  - Planificación y control del despliegue de resultados  
  - Elaboración de informe final y revisión del proyecto  
- **Notas:**  
  - Permite la aplicación de modelos o funciones en entornos reales o de prueba  
  - Esta fase finaliza el ciclo de CRISP-DM, aunque según las necesidades, puede ser necesario repetir alguna fase

---

**Para mas información:**

- [La metodología CRISP-DM: desarrollo de modelos de machine learning](https://www.mytaskpanel.com/la-metodologia-crisp-dm-desarrollo-de-modelos-de-machine-learning/#:~:text=programas%20de%20retenci%C3%B3n.-,2.,de%20descuento%20ser%C3%ADan%20m%C3%A1s%20efectivas.)	

- [¿Qué es CRISP DM?](https://www.datascience-pm.com/crisp-dm-2/)	

**Notebooks:**

- [Business Understanding](notebooks/01_Business_Understanding.ipynb)
- [Data Understanding](notebooks/02_Data_Understanding.ipynb)
- [Data Preparation](notebooks/03_Data_Preparation.ipynb)
- [Modeling](notebooks/04_Modeling.ipynb)
- [Final analysis](notebooks/06_final_analysis.ipynb)

## Repositorios 

- [DockerHub](https://hub.docker.com/repository/docker/brandonlcc/fifa_ml_kedro/general)

- [DVC con Dagshub](https://dagshub.com/br.casas/ML-Kedro-FIFA-DVC)

- [Deployment FIFA](https://github.com/BrandonLCC/FIFA-web)

---

## Estructura del proyecto

```
Proyecto_ML_Kedro/
│
├── .dvc/
│
├── airflow/
│   ├── dags/
│   ├── logs/
│   └── plugins/
│
├── conf/
│   ├── base/
│   │   ├── parameters.yml    # Configuración de parámetros
│   │   └── catalog.yml       # Catalog de datasets
│   └── local/
│
├── data/
│   ├── 01_raw/
│   ├── 02_intermediate/      # Datos preprocesados
│   ├── 03_primary/      
│   ├── 04_feature/           # Features generadas con unsupervised
│   ├── 05_model_input/       # Datasets para entrenamiento y test
│   ├── 06_models/            # Modelos entrenados (Pickle)
│   ├── 07_model_output/
│   └── 08_reporting/         # Reportes de métricas
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
|
├── docs/
|
├── img-viz/
| 
├── logs/
|
├── notebooks/
│
├── src/
│   └── proyecto_ml_kedro/
│       ├── __init__.py
│       ├── pipeline_registry.py
│       │
│       ├── pipelines/
│       │   ├── data_processing/
|       |   |
│       │   ├── regression_models/
|       |   |
│       │   ├── classification_models/
|       |   |
│       │   ├── regression_report/
|       |   |
│       │   ├── classification_report/
|       |   |
│       │   ├── classification_report/
│       │   │
│       │   │
│       │   └── unsupervised_learning/
│       │
│       └── settings.py
│
├── .dockerignore
├── .dvcignore
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── start.sh
└── README.md
```

--- 

## Documentación

Algunos documentos no menciónados seran modificados o borrados.

| Documentos                     | Descripción          
| -------------------------- | ------------- 
| [Integración de airflow.md](docs/airflow.md)	   | Pasos de como se realizo la integración y configuración de Airflow.    
| [Uso de DVC](docs/dvc.md)| Pasos y configuración de DVC     
| [dockerfile-kedro](docs/Aprendizaje/dockerfile-kedro.md)                       | Pasos realizados para la implementación de Docker con kedro.    

## Pipelines del proyecto FIFA

### Descripción de pipelines

**Recomendaciónes:** Como aprendizaje para futuras iteraciones del proyecto o nuevo proyectos, se identificó que el pipeline `data_processing` concentra demasiadas funciones, lo que dificulta su mantenimiento, modificación y escalabilidad.

Se recomienda dividir este pipeline en varios pipelines más pequeños y especializados, con el objetivo de mejorar la modularidad, facilitar futuras modificaciones y reducir la complejidad dentro de un único flujo.

| Pipeline | Función |
|-----------|----------|
| **data_processing** | Limpieza de datos, imputación de valores faltantes, conversión de tipos, eliminación de inconsistencias y *feature engineering* inicial para generar el dataset base del proyecto. |
| **unsupervised_learning** (Módulo raíz) | Pipeline orquestador que integra procesos de detección de anomalías, clustering y reducción de dimensionalidad para enriquecer el dataset antes del modelado de regresión y clasificación. |
|  **anomaly_detection** (submódulo) | Identificación y tratamiento de valores atípicos para mejorar la calidad y estabilidad del dataset. |
| **clustering** (submódulo) | Segmentación de los datos en grupos homogéneos para generar nuevas características (por ejemplo, etiquetas de cluster). |
| **dimensionality_reduction** (submódulo) | Reducción de la dimensionalidad del dataset mediante técnicas como PCA, generando un dataset optimizado para el modelado. |
| **regression_models** | Entrenamiento y evaluación de modelos de regresión utilizando métricas apropiadas (por ejemplo, MAE, RMSE y R²). |
| **classification_models** | Entrenamiento y evaluación de modelos de clasificación utilizando métricas como accuracy, precision, recall y F1-score. |
| **regression_report** | Generación de visualizaciones y análisis de desempeño de los modelos de regresión. |
| **classification_report** | Generación de visualizaciones y análisis de desempeño de los modelos de clasificación. |
| **final_report_comparativo** (No realizado) | Comparación de resultados entre modelos de regresión y clasificación para facilitar el análisis global del rendimiento del sistema. |

### Arquitectura pipelines  ** (actualizar la arquitec)

El pipeline `unsupervised_learning` aplica tres transformaciones sobre el dataset base para generar un conjunto de datos enriquecido, el cual posteriormente es utilizado por modelos de aprendizaje supervisado para tareas de predicción.

```
  data_processing 
    ↓
  unsupervised_learning
    |
    |--> anomaly_detection
    |
    |--> clustering
    |
    |--> dimensionality_reduction 
    ↓
  regression_models
    ↓
  classification_models
    ↓
  reporting_pipeline
```

### Arquitectura de Pipelines (Kedro Viz)

> Haz clic en la imagen para explorar el flujo automatizado del proyecto.

![Kedro Pipeline Viz](https://raw.githubusercontent.com/BrandonLCC/FIFA_ML_Kedro/main/img/kedro-pipeline-viz.svg)

### Airflow img

## Conjunto de datos generados

## Modelos 

## Variables


| Target   | Descripción      
| --------------|-------------
| `Value_num`   |  d 

| Features            | Descripción      
| ---------------------------|-------------
| `Best Overall Rating`      |
| `Special`                  |
| `International Reputation` |
| `Reactions`                |
| `Potential`                |

### Modelos implementados

| Modelo                     | Tipo          
| -------------------------- | ------------- 
| **Simple Linear Regression**   | Regresión     
| **Multiple Linear Regression** | Regresión     
| **SVR**                        | Regresión     
| **Decision Tree**              | Regresión     
| **Random Forest**              | Regresión     
| **Logistic Regression**        | Clasificación 
| **KNN**                        | Clasificación 
| **XGBClassifier**              | Clasificación 
| **Decision Tree**              | Clasificación 
| **Random Forest**              | Clasificación 

## Metricas de evaluación 

### Regresión

| Modelo                     | MSE             | RMSE       | R²     |
| -----------------          | --------------- | ---------- | ------ |
| **Simple_Linear_Regression**   | ...             | ...        | ...    |
| **Multiple_Linear_Regression** | ...             | ...        | ...    |
| **SVR_Model**                  | ...             | ...        |        |
| **Decision_Tree_Regression**   | ...             | ...        | ...    |
| **Random_Forest_Regression**   | ...             | ...        | ...    |

### Clasificación

| Modelo              | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| **Logistic Regression** | ...      | ...       | ...    | ...      |
| **KNN**                 | ...      | ...       | ...    | ...      |
| **XGBClassifier**       | ...      | ...       | ...    | ...      |
| **Decision Tree**       | 0.0975   | 0.0996    | 0.0975 | 0.0915   |
| **Random Forest**       | 0.1075   | 0.1129    | 0.1075 | 0.0974   |

---

## Comparaciónes o evaluaciones etc

### Mejores modelos obtenidos 

(mostrar graficos, metricas, hallazgos,etc)

--- 

## Conclusión

### Cierre

### Reflexion 

Puede incluir un "llamado a la acción" o una reflexión final que invite a nuevas investigaciones.

--- 

## Herramientas  y Framework 

### Framework

- **[Kedro](https://kedro.org/#get-started)**: Es el framework principal utilizado en este proyecto con el propósito de realizar el procesamiento y la limpieza de datos, el entrenamiento de modelos, la implementación de pipelines, entre otras tareas.

### Herramientas

- **[Jupyter Notebooks](notebooks):** En este proyecto, Kedro incorpora Jupyter Notebooks para la creación y edición de cuadernos digitales en formato `.ipynb`, utilizando Python.  
  Dentro de la carpeta `notebooks` se organizan los distintos notebooks asociados a la metodología **CRISP-DM**, así como aquellos destinados a la implementación de modelos de aprendizaje **supervisados y no supervisados**.

- **[DVC con Dagshub](https://dagshub.com/)**: Se utiliza la herramienta **DVC (Data Version Control)** que permite realizar el versionamiento de los datos generados por el proyecto, con el objetivo de mantener un respaldo seguro y reproducible.  
DVC establece una conexión con **DagsHub**, donde se alojan los datos en una plataforma de colaboración en la nube diseñada específicamente para científicos de datos.

- **[Airflow-apache](https://airflow.apache.org)**: Es una plataforma de código abierto diseñada para orquestar, programar y monitorear flujos de trabajo (pipelines) de datos complejos mediante código Python. [Ver más](https://liora.io/es/todo-sobre-apache-airflow)

- **[Docker Hub](https://hub.docker.com/) y [Docker Desktop](https://docs.docker.com/desktop/):** Docker nos permite crear un **entorno de pruebas aislado** de la producción real, manteniendo controladas las **dependencias**, **versiones de lenguajes** y **librerías** mediante el uso de **imágenes y contenedores**.

## Librerias 

Algunas de las librerías utilizadas durante las etapas de [Data Understanding](notebooks/02_Data_Understanding.ipynb), [Data Preparation](notebooks/03_Data_Preparation.ipynb) y [Modeling](notebooks/04_Modeling.ipynb) en Jupyter Notebook. De la misma forma, estas librerías son aplicadas dentro de los pipelines del proyecto.

- **numpy** 
- **pandas**
- **seaborn**
- **matplotlib**
- **sklearn** 

## Instalación / Colaboración

```bash
git clone <url_del_proyecto>
cd machine_learning_project
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

## Referencias 



