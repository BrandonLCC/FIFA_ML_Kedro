# readme no creado hasta el momento 

## Estructura del Proyecto  (eva 3 no actualizado)

```
proyecto-ml-final/

├── airflow/ <- manejo de dags
│   └── dags/
│
│
├── conf/
│   ├── base/
│   │   ├── catalog.yml     
│   │   └── parameters.yml
│   └── local/ 
├── data/ 
│   ├── 01_raw/ 
│   ├── 05_model_input/
│   ├── 06_models/   
│   ├── 07_model_output/         
│   └── 08_reporting/    
├── docker/ 
│   ├── Dockerfiles              
│   └── docker-compose.yml  
│
├── src/proyecto_ml/pipelines/ 
│   ├── data_engineering/ 
│   ├── supervised_learning/ 
│   │   ├── classification/ 
│   │   └── regression/ 
│   ├── unsupervised_learning/   # ← NUEVO 
│   │   ├── clustering/ 
│   │   ├── dimensionality_reduction/ 
│   │   ├── anomaly_detection/ 
│   │   └── association_rules/ 
│   └── reporting/ 
├── notebooks/ 
│   ├── 01-04: De EP1 y EP2 
│   ├── 05_unsupervised_learning.ipynb  # ← NUEVO 
│   └── 06_final_analysis.ipynb         # ← NUEVO 
├── docs/ 
│   ├── architecture.md          # ← NUEVO 
│   └── unsupervised_analysis.md     
└── README.md                    
```

# Instalacion (actualizado al 19/11/2025)

1. clonar repositorio 

...

2. Crea un entorno virtual 

python -m venv .venv

3. instalar dependencias 

pip install -r requirements.txt


