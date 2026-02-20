from kedro.pipeline import Node, Pipeline  # noqa

#def create_pipeline(**kwargs) -> Pipeline:
#   return Pipeline([])

# Necesitamos que esto se ejecute de manera automática
from .nodes import preprocess_fifa_22, preprocess_fifa_21, preprocess_fifa_20, create_model_input_table, transformacion_columns

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [  
            # En el pipeline, establecemos las pequeñas tareas (nodes) que esperamos que se realicen.
            # Limpieza de los datos dataset 1
            Node(
                func=preprocess_fifa_22,        # Funcion de node
                inputs="DataSetFIFA22",
                outputs="preprocess_fifa_22",   # Definir las Salidas en catalog y aquí
                name="preprocess_fifa_22_node",
            ),
            # Limpieza de los datos dataset 2
            Node(
                func=preprocess_fifa_21, 
                inputs="DataSetFIFA21",
                outputs="preprocess_fifa_21", 
                name="preprocess_fifa_21_node",
            ),
            #Limpieza de los datos dataset 3
            Node(
                func=preprocess_fifa_20, 
                inputs="DataSetFIFA20",
                outputs="preprocess_fifa_20", 
                name="preprocess_fifa_20_node",
            ),

            # Procesamiento 2

            # Reduce_columns_node: Es la unica funcion (funcion que esta al final de las funciones)
            # que se utilizara aparte de las funciones de preprocess 
            # debido a su extension y reutilizacion en los 3 datasets
            # Aqui tendremos un ejemplo practico de reutilizacion de codigo en kedro
            # En vez de utilizarla en la funcion orquestadora preprocess_fifa_22

            # Para futuras ocasiones, considerar realizar otros pipelines para disminuir la cantidad de codigos en nodes.py (para limpieza y transformacion de datos etc)

            Node(
                func=transformacion_columns,
                inputs="preprocess_fifa_22",                             # Dataset crudo
                outputs="FIFA22_processed_con_transformacion_columns",  # Dataset procesado
                name="transformacion_columns_fifa22.node",
            ),
            Node(
                func=transformacion_columns,
                inputs="preprocess_fifa_21",
                outputs="FIFA21_processed_con_transformacion_columns",
                name="transformacion_columns_fifa21.node",
            ),
            Node(
                func=transformacion_columns,
                inputs="preprocess_fifa_20",
                outputs="FIFA20_processed_con_transformacion_columns",
                name="transformacion_columns_fifa20.node",
            ),
            Node(
                func=create_model_input_table,
                inputs=["FIFA22_processed_con_transformacion_columns", "FIFA21_processed_con_transformacion_columns", "FIFA20_processed_con_transformacion_columns"],
                outputs="model_input_table", # del catalog
                name="create_model_input_table_node",
            )

            # Imputacion de los datos: valores missing (usar tecnicas como KNN, Valores Media mediana etc)
            # Generacion de Feature 
         
        ]
    )
