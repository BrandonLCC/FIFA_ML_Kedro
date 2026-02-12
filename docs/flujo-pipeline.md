# Flujo pipeline de modelos supervizados


# Pipelines 

Al realizar kedro run o el flujo inicial primero el proyecto ejecuta 

el pipeline llamado "data_procesing"

Ejecucion de pipelines supervizados 

data_procesing > regression_models > classifitacion_models > reportes > comparativos

**Codigos docker runs**
kedro run --pipeline data_processing -  [OK]

kedro run --pipeline regression_models - [OK]

Prueba pasada, metrica del unico modelo ejecutado

Mean Squared Error (MSE): 4287408515877.725586
Mean Absolute Error (MAE): 631584.990884
Root Mean Squared Error (RMSE): 2070605.833054
R2 Score: 0.896787

kedro run --pipeline classification_models -  [NOOK] 

mal desempeño 

kedro run --pipeline data_processing -  [OK] 

## Archivos modificables

Modificar pipeline_registry para hacer kedro run ya que se modifico.

Modificar catalog.yml para la entradas o salidas. 


# ERROR CONCEPTUAL 

Error conceptual cometido durante la etapa del desarrollo de entradas y salidas en catalog. 

### Mi error conceptual

Mi error conceptual fue pensar que el problema venía de tener varios train_test_split o de “conflictos” por repetir train y test, cuando en realidad el problema estaba en la inconsistencia entre el orden de los outputs del node y el orden esperado en el pipeline. Es decir, los datasets sí se estaban generando, pero estaban siendo asignados con nombres incorrectos (por ejemplo, métricas de clasificación usando datos de regresión). No era un problema de cantidad de splits, sino de coherencia estructural entre lo que retorna la función y lo que el pipeline declara como salida.

### La lógica correcta 

Cada tipo de modelo (regresión y clasificación) **puede tener su propio train_test_split** si sus parámetros son distintos (test_size, stratify, etc.). No hay conflicto mientras cada salida tenga un nombre único y consistente. Si quieres cambiar el tamaño de train/test, debes modificar los valores en **`parameters.yml`** y volver a ejecutar el pipeline completo para regenerar los datasets con la nueva configuración. Esa es la lógica limpia y correcta en Kedro: los parámetros gobiernan el comportamiento, y el pipeline se vuelve reproducible simplemente re-ejecutándolo.

Excepción:
No es incorrecto tener más de un train/test split dentro de una arquitectura de pipelines si cada modelo (por ejemplo, regresión y clasificación) responde a objetivos distintos y requiere configuraciones diferentes (como test_size, stratify o selección de features). En ese caso, generar particiones separadas desde el mismo clean_dataset es una decisión válida de diseño y no un error técnico.

Criterios:
Se recomienda usar un único train/test split cuando se busca coherencia experimental, comparabilidad directa entre modelos o evitar inconsistencias en la evaluación. En cambio, se justifica tener múltiples splits cuando los modelos tienen targets distintos, necesitan estratificación específica o cumplen propósitos independientes dentro del sistema. La clave no es cuántos splits existen, sino que la decisión sea consciente, documentada y coherente con los objetivos del proyecto.




