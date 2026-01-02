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

docker-compose -f docker/docker-compose.airflow.yml build # ejecuta de esta forma si el archivo compose no esta dentro de una carpeta o directorio
docker-compose -f docker/compose/docker-compose.airflow.yml up -d # ejecuta de esta forma si estan dentro de una carpeta o directorio

# ejecucion de airflow 

1. Ubícate en la raíz del proyecto

cd C:\Users\brand\Downloads\Proyecto_ML_Kedro

2. Inicializar Airflow (solo la PRIMERA VEZ)
docker compose -f compose/docker-compose.airflow.yml up airflow-init

Esto crea:

base de datos Airflow

usuario admin

estructura interna

Si ya lo hiciste antes: puedes saltarlo.

3. Levantar Airflow (webserver + scheduler + postgres)
docker compose -f docker/docker-compose.airflow.yml up -d


Esto inicia los servicios en segundo plano.

4. Abrir Airflow en el navegador

http://localhost:8080

Credenciales por defecto:

user: admin

pass: admin

(Salvo que hayas definido otras en tu archivo .env.)

5. Ver logs si algo falla
Webserver:
docker logs airflow-webserver -f

Scheduler:
docker logs airflow-scheduler -f

6. Reiniciar solo los DAGs (sin tumbar todo)

Si editaste archivos en dags/:

docker compose -f docker/docker-compose.airflow.yml restart airflow-scheduler
docker compose -f docker/docker-compose.airflow.yml restart airflow-webserver


Esto es lo más usado durante el desarrollo.

7. Apagar Airflow
docker compose -f docker/docker-compose.airflow.yml down

## No veo los dags?

puedes verificar en  docker-compose.yaml y revisa que tenga:

volumes:
  - ./dags:/opt/airflow/dags
  - ./logs:/opt/airflow/logs
  - ./plugins:/opt/airflow/plugins

---

## Errores solucionados 

**No se detecta los DAGs**

- Cambio en las rutas de volumes en docker-compose.airflow.yml: - ../airflow/dags:/opt/airflow/dags 

Esto depende de tu proyecto, en mi caso, no se estaba leyendo la carpeta que tenia los dags ya que tenia otra ruta configurada. 
Luego de eso, de pudo detectar los DAGs.

**No detecta los otros archivos .py**

- Solucion: 

Descripcion: 

---


Dockerfile de Airflow — Explicación Rápida

Este proyecto utiliza Airflow + Kedro, por lo que es necesario usar un Dockerfile personalizado para Airflow.
La razón principal es que Airflow no se ejecuta en tu computador, sino dentro de contenedores Docker, y estos contenedores no tienen Kedro instalado por defecto.

¿Por qué usar un Dockerfile para Airflow?

Si no se usa un Dockerfile personalizado, dentro del contenedor aparecerán errores como:

ModuleNotFoundError: No module named 'kedro'


Esto ocurre porque el contenedor de Airflow no tiene:

Kedro instalado

El operador personalizado kedro_operator

Acceso interno al proyecto Kedro

¿Qué soluciona el Dockerfile?

El dockerfile-airflow permite:

- Instalar Kedro dentro del contenedor Airflow

- Instalar el operador kedro_operator

-  Copiar o montar las rutas necesarias de Airflow (dags, plugins, etc.)

- Permitir que los DAGs interactúen con el proyecto Kedro

# no eliminar importante

¿Çomo cree mis dags de airflow?

como estrategia, primero en vez de genrarlos manualmente, realizar estos pasos para que se generen automaticamente y luego pegarlo en el archivo original de airflow.


1. Instala el plugin

  pip install kedro-airflow


2. Genera los DAGs (en la terminal)

  kedro airflow create


3. Copia los archivos generados
  Desde:

  airflow_dags/
  
  Hacia la carpeta real de tu Airflow:

  compose/airflow/dags/





data_engineering → supervised → unsupervised → reporting
