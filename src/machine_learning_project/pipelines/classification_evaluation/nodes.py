import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    auc,
    precision_recall_curve
)

from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier

import os

# eliminar funcion, esta funcion ya se encuentra en el pipeline de clasificación, y se llama evaluacion_completa_modelo_clasificacion, se puede usar la misma funcion para ambos pipelines, tanto de regresion como de clasificacion, solo cambiando los parametros de entrada.
# Eliminar las funcinoes o elementos de generacion de reportes y moverlo en el pipeline de reportes.




def evaluacion_modelo_individual(y_pred, y_test, nombre_modelo):

    if isinstance(y_test, pd.DataFrame):
        y_test = y_test.iloc[:, 0]

    if isinstance(y_pred, pd.DataFrame):
        y_pred = y_pred.iloc[:, 0]

    return pd.DataFrame([{
        "model": nombre_modelo,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="weighted"),
        "recall": recall_score(y_test, y_pred, average="weighted"),
        "f1_score": f1_score(y_test, y_pred, average="weighted")
    }])
