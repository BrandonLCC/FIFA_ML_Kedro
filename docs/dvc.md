# instalacion de DVC con DagsHub (SSH)

1. pip install "dvc[ssh]"

2. verificar la version

dvc --version

# usar git para subir y push 


PASO 0 — Estar dentro del proyecto
cd C:\Users\brand\Downloads\Proyecto_ML_Kedro

✅ PASO 1 — Inicializar Git (solo la primera vez)

Si el proyecto ya tenía Git, este paso solo lo reconfigura.

git init

✅ PASO 2 — Añadir todos los archivos al staging
git add .

✅ PASO 3 — Crear el primer commit
git commit -m "Primer commit del proyecto ML Kedro + DVC"

✅ PASO 4 — Conectar el repositorio local con Dagshub

Ir a Dagshub

Crear repo: ML-Kedro-FIFA-DVC

Copiar URL HTTPS:

https://dagshub.com/br.casas/ML-Kedro-FIFA-DVC.git


Agregar el remoto en tu proyecto:

git remote remove origin   # solo si ya existía otro
git remote add origin https://dagshub.com/br.casas/ML-Kedro-FIFA-DVC.git

✅ PASO 5 — Crear un Access Token en Dagshub

Ir a:

🔗 https://dagshub.com/user/settings/tokens

"Generate New Token"

Nombre: git-token

Dar permisos por defecto

Copiar el token (muy importante)

Ese token actúa como password.

✅ PASO 6 — Autenticar y hacer push

Finalmente:

git push -u origin main


Git pedirá:

Username: br.casas
Password: <token_generado>



# preguntas

¿Los datos se suben automáticamente al repo?

NO.
Y esto es intencional.

- Git SOLO guarda archivos pequeños

Código, scripts, configs, etc.

- DVC guarda archivos grandes

Datasets, modelos, features, etc.

- DVC NO sube datos automáticamente para evitar que subas archivos gigantes por error.

¿Entonces qué se sube realmente a Git?

Cuando haces:

dvc add data/dataset.csv


DVC crea un archivo pequeño:

dataset.csv.dvc

Ese archivo SÍ va a Git, porque solo contiene metadata:

ruta del dataset

checksum/hash

tamaño

versión

Pero el dataset real NO se sube a Git.

📌 3. ¿Dónde van los datos reales?

A tu remote de DVC, por ejemplo:

DagsHub DVC storage

AWS S3, Google Drive, Azure, SSH, etc

Con:

dvc push

 Ahí sí se sube el archivo completo.

¿Qué es lo que se versiona realmente?

DVC versiona archivos de datos completos, pero solo subes los que tú decidas.

Cada vez que cambias el dataset:
dvc add data/dataset.csv
git commit -am "Nuevo dataset"
dvc push

DVC guarda una nueva versión del dataset, igual que Git guarda una nueva versión del código.


siguientes pasos

- Instalar DVC

- Inicializar DVC en tu proyecto

- Configurar Dagshub como storage remoto para DVC

- Rastrear tus datasets con DVC

- Subir los datos al remoto con dvc push


## siguiente paso 

1. paso 1 pip instal dvc

pip install "dvc[s3]"


### siguiente paso 

2. inicializar el poryecto (desde aqui se genera el archivo .dvc similar al .gitinit)

dvc init

Luego:

git add .
git commit -m "Configuración inicial de DVC"
git push


# siguiente paso 


ASO 3 — Configurar Dagshub como almacenamiento remoto

Dagshub te da URLs S3 para DVC.

Tu remoto quedará así (reemplazando br.casas/ML-Kedro-FIFA-DVC):

dvc remote add -d dagshub s3://ML-Kedro-FIFA-DVC


Ahora tenemos que decirle la URL real del bucket:

dvc remote modify dagshub endpointurl https://dagshub.com/api/v1/repo-buckets/br.casas/ML-Kedro-FIFA-DVC


Y autenticación:
pag: https://dagshub.com/user/settings/tokens
dvc remote modify dagshub --local access_key_id <TU_TOKEN>
dvc remote modify dagshub --local secret_access_key <TU_TOKEN>

# dvc remote modify dagshub --local access_key_id 2d8fd105d2d7382e72c260433bf54148edf0eb34
# dvc remote modify dagshub --local secret_access_key 2d8fd105d2d7382e72c260433bf54148edf0eb34

# siguiente paso 

PASO 4 — Versionar tus datasets

Por ejemplo, si tienes data/01_raw/dataset.csv:

dvc add data/01_raw/dataset.csv


O si quieres versionar carpetas completas:

dvc add data/01_raw


DVC creará:

un archivo .dvc

registrará los hashes del contenido

ignorará el archivo real para Git

Luego:

git add .
git commit -m "Añadido dataset versionado con DVC"
git push

## siguiente paso — Subir datos al remoto Dagshub

Finalmente:

dvc push

# Qué carpetas deberías versionar con DVC?
🔥 Regla de oro en ciencia de datos con DVC:

Versiona solo los datos que NO se pueden regenerar.
📂 01_raw → SÍ o SÍ se versiona



en la terminal del proyecto ejecutar 

 dvc add data/01_raw/

 en mi caso tambien versionaremos el archivo 06_models

 dvc add data/01_raw


Versionar modelos:



dvc add data/06_models

Luego:

git add data/.gitignore data/01_raw.dvc data/06_models.dvc

git commit -m "Versionando datos crudos (01_raw) y modelos (06_models)"

🚀 4. Sube los cambios al repositorio en DagsHub
git push
dvc push

