![imagen-readme-presentacion](/img/img-presentacion.jpg)

<!--<img src="img/img-presentacion.jpg" alt="imagen-readme-presentacion" width="90%" head=50%>
-->

# Proyecto FIFA 23

(Título principal y descripción corta)

## Objectivos 

Breve contexto del problema o análisis que se quiere realizar.

**Colaboradores:**

## Empresa / Fuente de Datos

**Empresa:**

**FIFA 23 OFFICIAL DATASET** : [Link](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1)	

## Metodología y Proceso de desarrollo 

explicar brevemente las etapas 

## Machine-Learning (modelos y técnicas usadas)

Introduccion del proyecto con machine learning

Objectivo con machine learning: 

### Modelos de regresión 
Descripción
Resultados y métricas

### Modelos de clasificación 
Descripción
Resultados y métricas

### Resultados y Visualizaciones
Gráficos, comparaciones, insights

## Framework y Herramientas

- **Framework principal:** kedro, versión 1.0.0
- **Lenguaje:** Python, versión 3.11.9
- **IDE:** VS Code
- **Control de versiones:** Git

## Librerias 

- **pandas:** [Version] 
- **seaborn:** [Version]  

## Instalación y Ejecución del Proyecto (Deployment)

**Kedro:** [Link](https://kedro.org/#get-started)	

1. **Entra en el proyecto**

```
cd machine-learning-project
```

2. **Crea tu entorno virutal de python**

```
 uv sync 
```
3. **Activa tu entorno virual**

```
.\.venv\Scripts\Activate.ps1 
```
> **En caso de error ejecuta este codigo** 

```
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
```

4. **Dependencias**

```
pip install -r requirements.txt
```

4. **Ejecuta para visualizar tus notebooks** 

```
 Kedro y Jupyter notebook 
``` 
## Conclusiones


## Aprendizajes

Errores cometido 

diplicado de carpeta raiz

Primero, abre tu explorador de archivos y confirma que tienes esta estructura:

text
machine-learning-project/          (carpeta raíz del repositorio)
└── machine-learning-project/      (carpeta hija duplicada)
    ├── airflow/
    ├── conf/
    ├── src/
    └── etc...


corregido a

machine-learning-project/          (solo esta carpeta)
├── airflow/
├── compose/
├── conf/
├── data/
├── docker/
├── docs/
├── notebooks/
├── src/
├── tests/
├── .dockerignore
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
├── start.sh
└── uv.lock

