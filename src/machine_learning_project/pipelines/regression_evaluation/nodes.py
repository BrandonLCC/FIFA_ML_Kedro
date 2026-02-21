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
#  X_test eliminado
# input model eliminado
# se agrega y_pred

def evaluacion_modelo_individual(y_pred, y_test, nombre_modelo):

    # Asegurar Series unidimensionales
    if isinstance(y_test, pd.DataFrame):
        y_test = y_test.iloc[:, 0]
    elif isinstance(y_test, np.ndarray) and y_test.ndim > 1:
        y_test = pd.Series(y_test.ravel())

    if isinstance(y_pred, pd.DataFrame):
        y_pred = y_pred.iloc[:, 0]
    elif isinstance(y_pred, np.ndarray) and y_pred.ndim > 1:
        y_pred = pd.Series(y_pred.ravel())

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    df_result = pd.DataFrame([{
        "Modelo": nombre_modelo,
        "MSE": mse,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }])

    return df_result
