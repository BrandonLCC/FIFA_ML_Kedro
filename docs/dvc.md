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

Instalar DVC

Inicializar DVC en tu proyecto

Configurar Dagshub como storage remoto para DVC

Rastrear tus datasets con DVC

Subir los datos al remoto con dvc push

1. paso 1 pip instal dvc

pip install "dvc[s3]"

2. inicializar el poryecto (desde aqui se genera el archivo .dvc simial al .gitinit)

dvc init
