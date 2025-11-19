# instalacion de DVC con DagsHub (SSH)

1. pip install "dvc[ssh]"

2. verificar la version

dvc --version

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