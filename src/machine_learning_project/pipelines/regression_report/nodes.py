
"""""
def_report_regresion(){


       # Gráficos
    plt.figure(figsize=(5,5))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Valores Reales")
    plt.ylabel("Predicciones")
    plt.title(f"Predicho vs Real: {nombre_modelo}")
    plt.show()

    residuals = y_test - y_pred
    plt.figure(figsize=(5,4))
    plt.scatter(y_pred, residuals, alpha=0.7)
    plt.axhline(0, color='r', linestyle='--')
    plt.xlabel("Predicciones")
    plt.ylabel("Residuos")
    plt.title(f"Residuals plot: {nombre_modelo}")
    plt.show()

}

"""