# Arquitectura ANTES (no modular)

- Seguir esta arquitectura por si no quieres complicarte con Pipelines orquestadores de clasificacion y clasificacion. 

- Tambien, en esta arquitectura no se crea o los pipelines de prediccion, sino que directamente se crean los reportes. 

Al crear pipelines orquestadores En este caso, el proyecto se realizo lo que seria en un entorno real en el que se puede complicar los proyectos con varios pipelines y realizar una arquitectura mas limpia. Se elimina el pipeline de reportes_comparacion_final. se realizara una funcion de comparacion final en los mismos pipelines de reportes con el propocito de una mejor limpieza.

```
machine_learning_project/
│
├── pipelines/
│
│   ├── data_processing/
│   │   ├── nodes.py
│   │   └── pipeline.py
│
│   ├── unsupervised_learning/
│   │   ├── dimensionality_reduction/
│   │   │   ├── nodes.py
│   │   │   └── pipeline.py
│   │   │
│   │   ├── clustering/
│   │   │   ├── nodes.py
│   │   │   └── pipeline.py
│   │   │
│   │   └── anomaly_detection/
│   │       ├── nodes.py
│   │       └── pipeline.py
│
│   ├── regression_models/
│   │   ├── nodes.py
│   │   └── pipeline.py
│   │
│   ├── regression_evaluation/
│   │   ├── nodes.py
│   │   └── pipeline.py
│   │
│   ├── regression_report/
│   │   ├── nodes.py
│   │   └── pipeline.py
│   │
│   ├── classification_models/
│   │   ├── nodes.py
│   │   └── pipeline.py
│   │
│   ├── classification_evaluation/
│   │   ├── nodes.py
│   │   └── pipeline.py
│   │
│   ├── classification_report/
│   │   ├── nodes.py
│   │   └── pipeline.py
│   │
│   └── final_report_comparativo/
│       ├── nodes.py
│       └── pipeline.py
│
└── pipeline_registry.py
```

## Cómo se veía el flujo antes

El __default__ hacía algo así:
```
data_processing
→ dimensionality_reduction
→ clustering
→ anomaly_detection
→ regression_models
→ classification_models
→ regression_evaluation
→ classification_evaluation
→ regression_report
→ classification_report
→ final_report_comparativo
```

Todo concatenado manualmente.

# Nueva arquitectura modular para modelos de regresión y clasificación.

Ejemplo profesional completo
Node 1 — entrenamiento

Devuelve:

random_forest_model

Node 2 — predicción

Recibe:

random_forest_model
X_test


Devuelve:

classification_predictions

Node 3 — evaluación

Recibe:

classification_predictions
y_test


Devuelve:

metrics_random_forest

"""
X_train → train → random_forest_model
random_forest_model + X_test → predict → classification_predictions
classification_predictions + y_test → evaluate → metrics_random_forest
"""


# OJO, SE PUEDE HACER UNO O LO OTRO, LA DIFERENCIA ESTA EN LA MODULARIDAD

Opción 1 — Todo en un solo pipeline (más simple)
train → predict → evaluate


Un único modeling_pipeline.

✔ Ventajas

Más simple

Fácil de ejecutar

Perfecto para proyectos académicos

❌ Desventajas

Menos modular

Difícil reutilizar solo predicción en producción

🚀 Opción 2 — Separar en 3 pipelines (arquitectura profesional)

Esta es la arquitectura más limpia en Kedro.

📂 1️⃣ training_pipeline

Solo entrena y guarda modelo:

X_train → train → model.pkl


Se ejecuta cuando:

Haces experimentación

Reentrenas modelo

📂 2️⃣ inference_pipeline

Carga modelo entrenado y genera predicciones:

model.pkl + X_test → predict → predictions.parquet


Se ejecuta cuando:

Quieres usar el modelo en producción

Haces scoring nuevo

📂 3️⃣ evaluation_pipeline

Evalúa desempeño:

predictions + y_test → metrics.csv



# Como hacer un diagrama 

| Lo que quieres  | Lo que escribes   |
| --------------- | ----------------- |
| Caja            | `A[Texto]`        |
| Flecha          | `A --> B`         |
| Flecha punteada | `A -.-> B`        |
| Subgrupo        | `subgraph Nombre` |

