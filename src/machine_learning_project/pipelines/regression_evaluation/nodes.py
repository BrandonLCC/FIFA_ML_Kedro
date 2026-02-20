from kedro.pipeline import Node, Pipeline 
# -- Graficos --
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# -- Metricas --
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error

#Importaciones para generar los reportes
 
#Graficos y reportes necesarias
#Funcion que evalua todos los modelo individualmente y genera reportes
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

import pandas as pd

# La evaluacion esta bien, pero los reportes en pipeline de reportes y definir salidas. si es necesario ya que las salidas se definen si, pero en parameters??
 
def evaluacion_modelo_individual(modelo, X_test, y_test, nombre_modelo):
    # Asegurar Series unidimensionales
    if isinstance(y_test, pd.DataFrame):
        y_test = y_test.iloc[:, 0]
    elif isinstance(y_test, np.ndarray) and y_test.ndim > 1:
        y_test = pd.Series(y_test.ravel())

    y_pred = modelo.predict(X_test)
    if isinstance(y_pred, np.ndarray) and y_pred.ndim > 1:
        y_pred = pd.Series(y_pred.ravel())

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

 
    # Devolver DataFrame para que Kedro pueda guardarlo como CSV
    df_result = pd.DataFrame([{
        "Modelo": nombre_modelo,
        "MSE": mse,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }])
    return df_result

'''
#Funcion que realiza una comparativa de todos los modelos entrenados

def generate_regression_report(results_regresion, X_test_dict, y_test_dict):
    report_data = []
    
    # Evaluación individual de cada modelo
    for model_name, model in results_regresion.items():
        metrics = evaluacion_modelo_individual(
            modelo=model,
            X_test=X_test_dict[model_name],
            y_test=y_test_dict[model_name],
            nombre_modelo=model_name
        )
        report_data.append(metrics)
    
    # Crear DataFrame resumen
    df_report = pd.DataFrame(report_data)
    print("\nTabla comparativa de métricas")
    print(df_report[["Modelo","MSE","MAE","RMSE","R2"]])
    
    # --- Gráficos comparativos ---
    metrics = ["MSE", "MAE", "RMSE", "R2"]
    plt.figure(figsize=(12,4))
    for i, metric in enumerate(metrics):
        plt.subplot(1, len(metrics), i+1)
        plt.bar(df_report["Modelo"], df_report[metric], color='skyblue')
        plt.title(metric)
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return df_report[["Modelo","MSE","MAE","RMSE","R2"]]

'''