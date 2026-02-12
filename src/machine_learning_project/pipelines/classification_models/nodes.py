# -- Tratamiento de datos --
import numpy as np
import pandas as pd

# -- Visualización --
import matplotlib.pyplot as plt
import seaborn as sns

# -- Preprocesamiento y modelado --
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
#from xgboost import XGBClassifier # , plot_importance # type: ignore
#import xgboost as xgb  # type: ignore
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder

# -- Balanceo --
#from imblearn.over_sampling import SMOTE

# -- pipeline --
from sklearn.pipeline import Pipeline

# -- Métricas --
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score,
    precision_score, recall_score, f1_score
)

from sklearn.metrics import roc_curve, auc, precision_recall_curve

# --- Funcion normal para la division de datos para los modelos que no requieren de escalado ---

# Version corregida: agrregamos statify
"""def division_datos_test_train(data: pd.DataFrame, parameters: dict) -> tuple:
    
    X = data[parameters["features"]]
    y = data[parameters["target"]]

    stratify_value = y if parameters.get("stratify", False) else None

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=parameters["test_size"],
        random_state=parameters["random_state"],
        stratify=stratify_value
    )

    return X_train, X_test, y_train, y_test
"""

def division_datos_test_train(data: pd.DataFrame, parameters: dict) -> tuple:
 
    X = data[parameters["features"]]
    y = data[parameters["target"]]
    #En caso de error, si y necesita ser 1D usar .values.ravel
    if isinstance(y, pd.DataFrame):
        y = y.values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=parameters["test_size"], random_state=parameters["random_state"])

    return X_train, X_test, y_train, y_test


# Modelos como: SVM, KNN, LogisticRegression se le aplicara escalado

#GridSearchCV de notebook adaptados a funciones

def entrenar_modelo_logistic_cv(X_train, y_train, param_grid):
    # Asegura que y sea un vector 1D
    if isinstance(y_train, pd.DataFrame):
        y_train = y_train.values.ravel()

    pipeline = Pipeline([
        ('scaler', StandardScaler()),       # Escala los datos
        ('logistic', LogisticRegression())  # Clasificador
    ])

    grid = GridSearchCV(pipeline, param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

# Resultado anterior sin escalar: Malos resultados
# Resultados escalado: 
def entrenar_knn_cv(X_train, y_train, param_grid):
    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Escala los datos
        ('knn', KNeighborsClassifier())
    ])

    grid = GridSearchCV(pipeline, param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def entrenar_svc_cv(X_train, y_train, param_grid):
    # Asegura que y sea un vector 1D
    if isinstance(y_train, pd.DataFrame):
        y_train = y_train.values.ravel()

    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Escala los datos
        ('svc', SVC())                 # Clasificador SVM
    ])

    grid = GridSearchCV(pipeline, param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def entrenar_decision_tree_cv(X_train, y_train, param_grid):
    grid = GridSearchCV(DecisionTreeClassifier(), param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def entrenar_random_forest_cv(X_train, y_train, param_grid):
    grid = GridSearchCV(RandomForestClassifier(), param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

# Evaluamos los modelos con las metricas de clasificacionn

#Primera version funcional de evuacion sin especificity y sensitivity
'''
def evaluacion_modelo(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))
    
    # Curva ROC
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    print("ROC AUC:", roc_auc)
    
    # Curva Precision-Recall
    precision, recall, _ = precision_recall_curve(y_test, y_prob)
    pr_auc = auc(recall, precision)
    print("Precision-Recall AUC:", pr_auc)
'''
    
def evaluacion_modelo(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    # Ajuste de average para multiclass
    average_type = "weighted"  # 'micro', 'macro' o 'weighted'

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred, average=average_type, zero_division=0))
    print("Recall (Sensitivity):", recall_score(y_test, y_pred, average=average_type, zero_division=0))
    print("F1 Score:", f1_score(y_test, y_pred, average=average_type, zero_division=0))
    
    # Specificity solo tiene sentido en binario, así que podemos omitirlo o calcularlo por clase
    # Por ahora lo comentamos
    # cm = confusion_matrix(y_test, y_pred)
    # tn, fp, fn, tp = cm.ravel()
    # specificity = tn / (tn + fp)
    # print("Specificity:", specificity)
    
    return {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average=average_type, zero_division=0),
        'recall': recall_score(y_test, y_pred, average=average_type, zero_division=0),
        'f1': f1_score(y_test, y_pred, average=average_type, zero_division=0),
    }
