# Crear la imagen

docker build -t fifa-ml-kedro-jupyter -f docker/Dockerfile.jupyter .

# Ejecutar dockerfile notebooks: 
# (ver si se puede simplificar)
docker run -it -p 8888:8888 -v "C:\Users\brand\Downloads\Proyecto_ML_Kedro:/app" fifa-ml-kedro-jupyter

o 

docker run -it --rm -p 8888:8888 -v "C:\Users\brand\Downloads\Proyecto_ML_Kedro:/app" fifa-ml-kedro-jupyter

# ERRORES 

✅ 1. IPython parent '/home/kedro' is not a writable location

Causa: Estás usando un usuario (kedro) dentro del contenedor cuya carpeta /home/kedro no tiene permisos de escritura.

Consecuencias:

Jupyter usa carpetas temporales en lugar del home

Se generan mensajes molestos

Algunas configuraciones no se guardan (trusted notebooks, caché, etc.)

Solución recomendada: