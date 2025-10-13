"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline  # noqa


#def create_pipeline(**kwargs) -> Pipeline:
#   return Pipeline([])


# Copiado del proyecto de ejemplo de Kedro (Borrar cuando no sea necesario)

# Necesitamos que esto se ejecute de manera automática
from .nodes import preprocess_fifa_22, preprocess_fifa_21, preprocess_fifa_20

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            #Limpieza de los datos dataset 1
            Node(
                func=preprocess_fifa_22, #funcion de node
                inputs="DataSetFIFA22",
                outputs="preprocess_fifa_22", # Definir las Salidas en catalog y aquí
                name="preprocess_fifa_22_node",
            ),
            #Limpieza de los datos dataset 2
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
            
            #Imputacion de los datos: valores missing (usar tecnicas como KNN, Valores Media mediana etc)

            #Generacion de Feature 

            #Node x : Union de las tablas

         
        ]
    )
