# FIFA 

![imagen-readme-presentacion](machine-learning-project/img/img-presentacion.jpg)

>**Link de FIFA23 OFFICIAL DATASET (Actualizado)** : https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1

## Etapa de instalación (confirmar instalacion)

Una vez realizado el `git clone` y cargado el proyecto, deberás realizar los siguientes pasos para poder modificar y ejecutar el proyecto:

>**Link para Kedro:** https://kedro.org/#get-started

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
## Framework y Herramientas

- **Framework principal:** kedro, versión 1.0.0
- **Lenguaje:** Python, versión 3.11.9
- **IDE:** VS Code
- **Control de versiones:** Git

## Librerias utilizadas 

Para cada libreria se debera realizar un pip install en tu entorno virtual

- **pandas:** [Version] ```pip install pandas```
- **seaborn:** [Version]  ```pip install seaborn```


## Ubicación de archivos

**01_raw:** En la carpeta 01_raw se almacenaran todos los archivos del conjunto de datos como CSV, parquet, xpt Entre otros.



