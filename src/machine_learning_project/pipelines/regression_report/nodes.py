import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

def def_report_regresion(nombre_modelo, y_test, y_pred):

    if isinstance(y_test, pd.DataFrame):
        y_test = y_test.iloc[:, 0]

    if isinstance(y_pred, pd.DataFrame):
        y_pred = y_pred.iloc[:, 0]

    residuals = y_test - y_pred

    #  Predicho vs Real
    fig1 = plt.figure(figsize=(5,5))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()],
             'r--')
    plt.xlabel("Valores Reales")
    plt.ylabel("Predicciones")
    plt.title(f"Predicho vs Real: {nombre_modelo}")
    plt.close()

    # Residual Plot
    fig2 = plt.figure(figsize=(5,4))
    plt.scatter(y_pred, residuals, alpha=0.7)
    plt.axhline(0, color='r', linestyle='--')
    plt.xlabel("Predicciones")
    plt.ylabel("Residuos")
    plt.title(f"Residuals Plot: {nombre_modelo}")
    plt.close()

    # 3 Q-Q Plot
    fig3 = plt.figure(figsize=(5,4))
    stats.probplot(residuals, dist="norm", plot=plt)
    plt.title(f"Q-Q Plot: {nombre_modelo}")
    plt.close()

    #  Histograma (comentado)
    #fig4 = plt.figure(figsize=(5,4))
    #plt.hist(residuals, bins=20, edgecolor='k', alpha=0.7)
    #plt.xlabel("Residuos")
    #plt.ylabel("Frecuencia")
    #plt.title(f"Histograma de Residuos: {nombre_modelo}")
    #plt.close()

    return fig1, fig2, fig3

def combinar_metricas(*metricas):
    return pd.concat(metricas, ignore_index=True)

def seleccionar_mejor_modelo(metrics_all_models):

    best_row = metrics_all_models.loc[
        metrics_all_models["R2"].idxmax()
    ]

    return pd.DataFrame([best_row])

def report_comparacion_modelos(model_comparison_report):
    
    """
El más importante es:

🔹 Barplot comparativo de métricas

Ejemplo:

Eje X: modelos

Eje Y: R2

Otro gráfico para RMSE

Eso es suficiente.
"""

    plt.figure(figsize=(8,5))
    plt.bar(model_comparison_report['Model'], model_comparison_report['R2_Score'], color='skyblue')
    plt.xlabel('Modelos')
    plt.ylabel('R2 Score')
    plt.title('Comparación de Modelos de Regresión')
    plt.ylim(0, 1)
    plt.xticks(rotation=45)
    plt.show()
    
    return None

