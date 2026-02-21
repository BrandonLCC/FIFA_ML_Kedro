# Arquitectura ANTES (no modular)

```
data/                    # (gitignored)
├── 01_raw/              # Datos originales, inmutables
│   ├── FIFA21_official_data.csv
│   ├── FIFA22_official_data.csv
│   └── FIFA23_official_data.csv
│
├── 02_intermediate/     # Datos procesados intermedios
│   ├── preprocess_fifa_21.parquet
│   ├── preprocess_fifa_22.parquet
│   └── preprocess_fifa_23.parquet
│
├── 03_primary/          # Tablas principales para modelado
│   └── model_input_table.parquet
│
├── 04_feature/          # Features engineered: clustering, association (si aplica)
│
├── 05_model_input/      # Datos listos para modelo
│
├── 06_models/           # Modelos entrenados (versioned)
│   └── regressor.pickle/
│       └── <timestamp>/
│
├── 07_model_output/     # Predicciones (si aplica)
│
└── 08_reporting/        # Reportes y visualizaciones (versioned)
    ├── shuttle_passenger_capacity_plot_exp.json/
    ├── shuttle_passenger_capacity_plot_go.json/
    └── dummy_confusion_matrix.png/
```