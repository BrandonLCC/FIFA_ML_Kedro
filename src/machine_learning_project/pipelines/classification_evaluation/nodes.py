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
    # Asegurar formato correcto
    if isinstance(y_test, pd.DataFrame):
        y_test = y_test.iloc[:, 0]
    if isinstance(y_pred, pd.DataFrame):
        y_pred = y_pred.iloc[:, 0]

    metrics = {
        "Model": nombre_modelo,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted"),
        "Recall": recall_score(y_test, y_pred, average="weighted"),
        "F1_score": f1_score(y_test, y_pred, average="weighted")
    }
    return metrics

""" 
def evaluacion_completa_modelo_clasificacion(model, X_test, y_test, model_name: str, save_path: str):
 
    os.makedirs(save_path, exist_ok=True)

    
    # --- Matriz de confusión ---
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"Matriz de confusión: {model_name}")
    plt.ylabel("Clase verdadera")
    plt.xlabel("Clase predicha")
    plt.savefig(f"{save_path}/{model_name}_confusion_matrix.png")
    plt.close()
    
    # --- Curva ROC y PR (solo binario) ---
    if y_proba is not None and len(np.unique(y_test)) == 2:
        from sklearn.metrics import roc_curve, auc, precision_recall_curve
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)
        plt.figure()
        plt.plot(fpr, tpr, label=f"ROC AUC = {roc_auc:.2f}")
        plt.plot([0,1], [0,1], "k--")
        plt.title(f"ROC: {model_name}")
        plt.xlabel("FPR")
        plt.ylabel("TPR")
        plt.legend(loc="lower right")
        plt.savefig(f"{save_path}/{model_name}_roc_curve.png")
        plt.close()
        
        precision, recall, _ = precision_recall_curve(y_test, y_proba)
        plt.figure()
        plt.plot(recall, precision, label=f"PR curve")
        plt.title(f"Curva Precision-Recall: {model_name}")
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.legend()
        plt.savefig(f"{save_path}/{model_name}_pr_curve.png")
        plt.close()
    
    # --- Importancia de características ---
    if hasattr(model, "feature_importances_"):
        plt.figure(figsize=(8,6))
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]
        plt.bar(range(X_test.shape[1]), importances[indices])
        plt.xticks(range(X_test.shape[1]), X_test.columns[indices], rotation=90)
        plt.title(f"Importancia de features: {model_name}")
        plt.tight_layout()
        plt.savefig(f"{save_path}/{model_name}_feature_importance.png")
        plt.close()
    
    metrics_df = pd.DataFrame([metrics])
    metrics_df.index = [model_name]
    return metrics_df

"""