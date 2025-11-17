# Airflow DAGs para Pipelines FIFA ML

Este directorio contiene los **Apache Airflow DAGs** utilizados para orquestar los pipelines de **Kedro** del proyecto *FIFA ML*.  
La estructura sigue el estándar enseñado en clases y replica buenas prácticas de MLOps del repositorio de referencia.

---

## Objetivo

Transformar los pipelines del proyecto Kedro en DAGs operables desde Airflow, permitiendo:

- Automatizar la ingesta, preparación y procesamiento de datos.  
- Entrenar modelos de forma periódica.  
- Ejecutar el flujo completo del proyecto mediante un **DAG maestro**.  
- Realizar ejecuciones manuales o experimentales de forma controlada.

---

## Propocíto de los archivos 

### 1. `FIFA_ml_pipeline`
- **Tipo:** DAG maestro  
- **Propósito:** Ejecuta el flujo completo (ETL → ML → Reporting).  
- **Uso:** Producción / ejecución diaria.

### Ejemplo (modificar)
start → data_processing → data_science → reporting → end

---

## DAGs por frecuencia (próximos a implementar)

Estos DAGs dividen el proyecto en procesos independientes:

### 2. `FIFA_daily_data_processing`
- Corre cada pocas horas.  
- Ejecuta únicamente el pipeline de preparación de datos.

### 3. `FIFA_weekly_model_training`
- Corre semanalmente.  
- Ejecuta el pipeline de entrenamiento del modelo.

### 4. `FIFA_on_demand`
- Sin programación automática.  
- Sirve para pruebas, debugging o ejecuciones manuales.

---

## KedroOperator

Todos los DAGs utilizan un **operador personalizado** que permite ejecutar nodos o pipelines de Kedro dentro de tareas Airflow.

Este operador manejará:

- Logs  
- Errores  
- Parámetros de ejecución  
- Rutas del proyecto  
- Integración con configuraciones de Airflow  

---

## Estructura

```txt
dags/
├── operators/
│   └── kedro_operator.py         # Operador personalizado para integrar Kedro
├── config.py                     # Configuración común (rutas, package_name, etc.)
├── FIFA_ml_pipeline.py           # DAG maestro (ETL + ML + Reporting)
├── FIFA_daily_data_processing.py # Procesamiento de datos (frecuencia alta)
├── FIFA_weekly_model_training.py # Entrenamiento de modelo semanal
└── FIFA_on_demand.py             # Ejecución manual / experimental
```

## Ejecución 



## Referencia 

Repositorio: [Link](https://github.com/Giocrisrai/kedro_tutorial_test/blob/main/dags/README.md)


# Pasos Previos para Ejecutar Airflow con Docker Compose

Antes de correr Airflow y probar los DAGs, sigue estos pasos mínimos.

## 1. Estar en la carpeta correcta
Debes ejecutar los comandos desde tu máquina (host), **no dentro de un contenedor**.

Ubícate en la carpeta donde está tu archivo:
compose/docker-compose.airflow.yml

Ejemplo:

```bash
cd compose
```

2. Construir o reconstruir los servicios de Airflow

Ejecuta esto si agregas nuevos DAGs, cambios en dependencias o archivos importantes:

docker-compose -f docker-compose.airflow.yml build
docker-compose -f compose/docker-compose.airflow.yml up -d

3. Levantar Airflow

Este comando inicia Postgres, Scheduler y Webserver dentro de contenedores:

docker-compose -f docker-compose.airflow.yml up -d #dentro 
docker-compose -f compose/docker-compose.airflow.yml up -d # fuera de raiz

4. Verificar que Airflow está corriendo

Abrir en el navegador:

http://localhost:8080


Usuario y contraseña por defecto (si no se cambió):

user: airflow
pass: airflow

5. Ver logs si algo falla

Scheduler:

docker logs airflow-scheduler -f


Webserver:

docker logs airflow-webserver -f

6. Actualizar DAGs sin reiniciar todo

Si solo modificaste un DAG o un archivo dentro de dags/, puedes reiniciar solo los servicios clave:

docker-compose -f docker-compose.airflow.yml restart airflow-scheduler
docker-compose -f docker-compose.airflow.yml restart airflow-webserver

7. Apagar Airflow cuando termines
docker-compose -f docker-compose.airflow.yml down


# ultimo visto (ver si es necesario anotarlo)

Inicializar Airflow solo la primera vez
docker-compose -f compose/docker-compose.airflow.yml up airflow-init

3. Levantar webserver + scheduler
docker-compose -f compose/docker-compose.airflow.yml up -d

4. Ver logs (si algo falla)
docker-compose -f compose/docker-compose.airflow.yml logs -f webserver

5. Detener todo
docker-compose -f compose/docker-compose.airflow.yml down


## No veo los dags?

puedes verificar en  docker-compose.yaml y revisa que tenga:

volumes:
  - ./dags:/opt/airflow/dags
  - ./logs:/opt/airflow/logs
  - ./plugins:/opt/airflow/plugins