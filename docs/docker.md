Dockerfile 
   ↓
(docker build)   ← se ejecuta en la terminal
   ↓
Docker Image     ← resultado del Dockerfile
   ↓
(docker run)     ← se ejecuta en la terminal
   ↓
Contenedor       ← instancia en ejecución de la imagen (

 - Cada contenedor proviene de una imagen.

 - Pero la imagen no contiene al contenedor, ni el contenedor contiene a la imagen.
)


Al iniciar el proyecto, genera llamando el nombre de las imagenes

docker build -t fifa-ml-kedro -f docker/Dockerfile.kedro .

Inicia el container o containers necesarios (eveces se debe usar un container que inicie varios programas o un kubernete para iniciar varios containers)

> docker build -t fifa-ml-kedro -f docker/Dockerfile.kedro .


# subir imagenes o contenedores del proyecto 

