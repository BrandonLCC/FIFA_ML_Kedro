import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    confusion_matrix,
    roc_curve,
    auc,
    precision_recall_curve
)


def evaluacion_completa_modelo_clasificacion(
    model,X_test,y_test,
    y_pred,model_name: str,y_proba=None
):

    figures = {}

    # =============================
    # MATRIZ DE CONFUSIÓN
    # =============================
    cm = confusion_matrix(y_test, y_pred)

    fig_cm, ax_cm = plt.subplots(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax_cm)
    ax_cm.set_title(f"Matriz de Confusión: {model_name}")
    ax_cm.set_ylabel("Clase verdadera")
    ax_cm.set_xlabel("Clase predicha")
    figures["confusion_matrix"] = fig_cm


    # =============================
    # ROC y PR (solo binario)
    # =============================
    if y_proba is not None and len(np.unique(y_test)) == 2:

        # ROC
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)

        fig_roc, ax_roc = plt.subplots()
        ax_roc.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
        ax_roc.plot([0,1], [0,1], "k--")
        ax_roc.set_title(f"Curva ROC: {model_name}")
        ax_roc.set_xlabel("FPR")
        ax_roc.set_ylabel("TPR")
        ax_roc.legend()
        figures["roc_curve"] = fig_roc


        # PR Curve
        precision_curve, recall_curve, _ = precision_recall_curve(y_test, y_proba)

        fig_pr, ax_pr = plt.subplots()
        ax_pr.plot(recall_curve, precision_curve)
        ax_pr.set_title(f"Curva Precision-Recall: {model_name}")
        ax_pr.set_xlabel("Recall")
        ax_pr.set_ylabel("Precision")
        figures["pr_curve"] = fig_pr

    # =============================
    # FEATURE IMPORTANCE
    # =============================
    if hasattr(model, "feature_importances_"):

        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]

        fig_fi, ax_fi = plt.subplots(figsize=(8,6))
        ax_fi.bar(range(len(importances)), importances[indices])
        ax_fi.set_xticks(range(len(importances)))
        ax_fi.set_xticklabels(
            X_test.columns[indices],
            rotation=90
        )
        ax_fi.set_title(f"Importancia de Features: {model_name}")
        figures["feature_importance"] = fig_fi

        # Comentario técnico:
        # Este gráfico muestra qué variables contribuyen más a las decisiones
        # del modelo. Solo es válido para modelos basados en árboles
        # (RandomForest, DecisionTree, GradientBoosting).
        # No debe usarse para modelos lineales o SVM sin coeficientes interpretables.

    return figures


def combinar_metricas(*metricas):
    return pd.concat(metricas, ignore_index=True)

def seleccionar_mejor_modelo(metrics_all_models):

    best_row = metrics_all_models.loc[
        metrics_all_models["f1_score"].idxmax()
    ]

    return pd.DataFrame([best_row])