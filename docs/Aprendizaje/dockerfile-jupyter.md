# Crear la imagen

docker build -t fifa-ml-kedro-jupyter -f docker/Dockerfile.jupyter .

# Ejecutar dockerfile notebooks: 
# (ver si se puede simplificar)
docker run -it -p 8888:8888 -v "C:\Users\brand\Downloads\Proyecto_ML_Kedro:/app" fifa-ml-kedro-jupyter

o 

docker run -it --rm -p 8888:8888 -v "C:\Users\brand\Downloads\Proyecto_ML_Kedro:/app" fifa-ml-kedro-jupyter

