# Proyecto_ML_Kedro
Al iniciar el proyecto debes

1. Activa tu entorno virual 

.\.venv\Scripts\Activate.ps1 

2. Si te da error, da acceso desde tu powershell o CMD

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Kedro y Jupyter notebook 

1. Ejecuta este código para 

kedro jupyter notebook

Tutorial para crear un proyecto con Kedro 

Link de referencia: https://kedro.org/#get-started

 1. crear un nuevo proyecto con kedro

uvx kedro new --starter spaceflights-pandas --name spaceflights

o Crea un proyecto kedro personalizado

 uvx kedro new 

2. Nombre del proyecto (carpeta): machine-learning-project

3. Opciones escogidas en este caso: 1-5 y "n"

4. Entrar al archivo machine-learning-project

cd machine-learning-project

4. uv sync para la creación del entorno virutal de python

uv sync

¡Instalación completada!

Ahora entra a visual estudio code 

code . 

-------------------------

Ubicación básica de los archivos

### 01_raw 

En la carpeta 01_raw se almacenaran todos los archivos del conjunto de datos como CSV, parquet, xpt Entre otros.


----------------------

Modificaciones agregados al proyecto

1. Dentro del archiv src creamos data_procesing en el archivo pipelines

kedro pipeline create data_processing


