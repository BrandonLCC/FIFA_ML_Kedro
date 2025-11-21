# Uso de Dockerfile con Kedro (Primer Proyecto)

Este documento resume los pasos utilizados para crear y ejecutar imágenes Docker con Kedro, Jupyter y Airflow.  
Se utiliza una carpeta `docker/` donde se almacenan todos los Dockerfiles del proyecto.

---

## 1. Flujo General

1. Crear cuenta en DockerHub  
2. Instalar Docker  
3. Crear directorio `docker/`  
4. Crear los archivos:
   - `Dockerfile.kedro`
   - `Dockerfile.jupyter`
   - `Dockerfile.airflow`
5. Construir las imágenes
6. Ejecutar contenedores y validar pipelines

---

## 2. Conceptos Clave

Dockerfile  
↓  
**docker build**  
↓  
**Imagen**  
↓  
**docker run**  
↓  
**Contenedor**

- Una imagen genera contenedores.  
- Las imágenes **no contienen** contenedores.  
- Los contenedores **no contienen** imágenes.

---

## 3. Errores Comunes y Correcciones

### Estructura recomendada
project/
│
├── docker/
│ ├── Dockerfile.kedro
│ ├── Dockerfile.jupyter
│ └── Dockerfile.airflow

### Dependencias
- Mantener `requirements.txt` **siempre actualizado**.

---

## 4. Construcción de Imágenes

### Si el Dockerfile está en `docker/`
```bash
docker build -t fifa-ml-kedro -f docker/Dockerfile.kedro .
```

Si está en la raíz del proyecto

```bash
docker build -t fifa-ml-kedro -f Dockerfile.kedro .
```

Verificar imágenes creadas

```bash
docker images
```

5. Contenedores
Crear un contenedor interactivo
```bash
docker run -it fifa-ml-kedro /bin/bash
```

Acceder al proyecto y a la carpeta data/ con bind mount

```bash
docker run -it -v "${PWD}:/app" fifa-ml-kedro /bin/bash
```
6. Ejecución de Pipelines Kedro
Pipeline de clasificación
```bash

kedro run --pipeline classification_models
```

Procesamiento de datos

```bash
kedro run --pipeline data_processing
```

Otros pipelines

```bash
kedro run --pipeline classification_report
kedro run --pipeline regression_report
```

7. Buenas Prácticas

- Bind mounts → sincroniza el código local con el contenedor.

- Named volumes → persistencia de datos entre contenedores.

- Validar pipelines antes de integrarlos con Airflow.

- Reconstruir imágenes cuando cambien dependencias o Dockerfiles.

8. Conclusión

- Verificar rutas, estructura y dependencias minimiza errores.

- obar imágenes creando contenedores interactivos es esencial.

- Asegurar que los pipelines funcionan antes de automatizar con Airflow.

- Eliminar y reconstruir imágenes/contendores es parte natural del flujo Docker.


flujo de ejecucion de pipelines

kedro run --pipeline data_processing

kedro run --pipeline regression_models
kedro run --pipeline classification_models

kedro run --pipeline regression_report
kedro run --pipeline classification_report


¿como hacer kedro run dentro del contenedor?

(resumen: estos pasos es como realizar el tutoral de arriba, solo que para entender que se hace cada vez que queremos hacer kedro run )

✔️ OPCIÓN 1: Ejecutar kedro run manualmente dentro del contenedor

(La más flexible)

1. Levanta el contenedor

Si tu Dockerfile ya crea la imagen:

docker build -t fifa-ml-kedro -f docker/Dockerfile.kedro .


Entonces creas un contenedor:

docker run -it fifa-ml-kedro /bin/bash

Dentro del contenedor puedes ejecutar:

kedro run

si da error usa el contendor con este codigo para acceder a las carpetas ya que kedro necesita algunas carpetas que no estan o no puede accerder por x razon

docker run -it -v "${PWD}:/app" fifa-ml-kedro /bin/bash

