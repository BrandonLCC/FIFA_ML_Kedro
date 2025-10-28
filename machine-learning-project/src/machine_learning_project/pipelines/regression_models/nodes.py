"""
This is a boilerplate pipeline 'regression_models'
generated using Kedro 1.0.0
"""
from kedro.pipeline import Node, Pipeline 
import pandas as pd 
# -- Tratamiento de datos --
import numpy as np
import pandas as pd

# -- Procesado y modelado --
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# -- Metricas --
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error

# -- GridSearchCV -- 
from sklearn.model_selection import GridSearchCV

from sklearn.preprocessing import StandardScaler

#Funcion para dividir los datos (usado para todos los mdelos)
def division_datos_test_train(data: pd.DataFrame, parameters: dict) -> tuple:

    X = data[parameters["features"]]
    y = data[parameters["target"]]
    
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=parameters["test_size"], random_state=parameters["random_state"])

    return X_train, X_test, y_train, y_test #Esta es la salida (output) del nodo de division_datos_test_train y
                                            #tanbien tenemos que definirlo en catalogo.yml

#GridSearchCV de notebook adaptados a funciones

# src/<tu_paquete>/pipelines/regression/nodes.py
#import pandas as pd
#import numpy as np
#from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import GridSearchCV
#from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def entrenar_modelo_linear_cv(X_train, y_train, param_grid):
    grid = GridSearchCV(LinearRegression(), param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

# Linear Regression Multiple (si tienes varias features o regularización)
def entrenar_linear_multiple_cv(X_train, y_train, param_grid):
    grid = GridSearchCV(LinearRegression(), param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_
 
# Support Vector Regressor
def entrenar_svr_cv(X_train, y_train, param_grid):
    grid = GridSearchCV(SVR(), param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

# Decision Tree Regressor
def entrenar_dt_grid(X_train, y_train, param_grid):
    grid = GridSearchCV(DecisionTreeRegressor(random_state=42), param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

# Random Forest Regressor
def entrenar_random_forest_cv(X_train, y_train, param_grid):
    grid = GridSearchCV(RandomForestRegressor(random_state=42), param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def evaluacion_modelo(modelo, X_test, y_test):
    # Predicciones
    y_pred = modelo.predict(X_test)
    
    # Métricas principales
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error (MSE): {mse:.6f}")
    print(f"Mean Absolute Error (MAE): {mae:.6f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.6f}")
    print(f"R2 Score: {r2:.6f}")
    
    return {
        "MSE": mse,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }