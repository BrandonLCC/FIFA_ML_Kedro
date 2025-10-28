import pandas as pd
import numpy as np
import pandas as pd

# Introduccion

# Para el procesamiento de los datos, realizaremos las funciones def en la que se realizara cada tarea 
# en especifico como limpieza, imputacion, generacion de features, union de tablas, etc. 
# Este primer proceso se realizara como en los proyectos de kedro tutorial. 

#--- Eliminacion de columnas ---

def eliminar_columnas(df: pd.DataFrame, columnas_a_eliminar: list) -> pd.DataFrame:
    """Elimina las columnas especificadas del DataFrame."""
    return df.drop(columns=columnas_a_eliminar, errors='ignore')

#--- Eliminacion de datos atipicos ---

def eliminar_filas(df: pd.DataFrame, columna: str, condicion) -> pd.DataFrame:
  
    # Selecciona los índices donde la condición es True
    indices_a_eliminar = df[df[columna].apply(condicion)].index
    # Elimina esas filas y devuelve un nuevo DataFrame
    return df.drop(indices_a_eliminar)

#--- Featyre engineering ---

def crear_skills(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea columnas ofensivas y defensivas como promedio de varias habilidades.
    """
    # Offensive Skills
    df['Offensive_Skills'] = df[['Finishing', 'Dribbling', 'ShotPower']].mean(axis=1)

    # Defensive Skills
    df['Defensive_Skills'] = df[['Marking', 'StandingTackle', 'SlidingTackle',
                                 'Interceptions', 'Strength', 'Aggression']].mean(axis=1)
    
    return df

def overall_class(x):
    if pd.isna(x):
        return "Desconocido"
    elif x >= 85:
        return "Alto"
    elif x >= 70:
        return "Medio"
    else:
        return "Bajo"


def joined_separado(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if 'Joined' not in df.columns:
        # Si no existe la columna, crear columnas vacías
        df['Joined_Year'] = pd.Series([pd.NA]*len(df), dtype='Int64')
        df['Joined_Month'] = pd.Series([pd.NA]*len(df), dtype='Int64')
        df['Joined_Day'] = pd.Series([pd.NA]*len(df), dtype='Int64')
        return df

    # Convertir a string y reemplazar NaN
    df['Joined'] = df['Joined'].astype(str).replace('nan', '')

    # Separar en máximo 3 columnas, reindexando para garantizar existencia
    joined_split = df['Joined'].str.split('-', expand=True).reindex(columns=[0, 1, 2])

    # Convertir a numérico y luego a Int64 para permitir NA
    df['Joined_Year'] = pd.to_numeric(joined_split[0], errors='coerce').astype('Int64')
    df['Joined_Month'] = pd.to_numeric(joined_split[1], errors='coerce').astype('Int64')
    df['Joined_Day'] = pd.to_numeric(joined_split[2], errors='coerce').astype('Int64')

    return df


# --- Formatear y transformar datos ---

def formato_position(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Position'] = df['Position'].fillna('Unknown') 
    df['Position'] = df['Position'].str.replace(">", "", regex=False).str.strip()
    df['Position'] = df['Position'].str[-3:]  

    return df

def formato_height(x: pd.Series) -> pd.Series:
    def convertir_altura(valor):
        if isinstance(valor, str):
            if "cm" in valor:
                # Caso: viene en centímetros
                return int(valor.replace("cm", "").strip())
            elif "'" in valor:
                # Caso: viene en pies y pulgadas -> ej. "5'11"
                partes = valor.replace('"', "").split("'")
                pies = int(partes[0])
                pulgadas = int(partes[1]) if partes[1] else 0
                return round((pies * 30.48) + (pulgadas * 2.54))
        return None  # si no cumple formato o es NaN
    
    return x.apply(convertir_altura)

def formato_weight(x: pd.Series) -> pd.Series:
    def convertir(valor):
        if isinstance(valor, str):
            if 'lbs' in valor:
                return float(valor.replace('lbs', '').strip()) * 0.453592
            elif 'kg' in valor:
                return float(valor.replace('kg', '').strip())
        elif isinstance(valor, (int, float)):
            return valor
        return np.nan
    return x.apply(convertir)


#--- Conversion ---

#de mondena a number de FIFA
def money_to_number(s):
    """Convert '€110.5M','€500K','€1.2B' or numeric-like strings into float (euros)."""
    if pd.isna(s): return np.nan
    if isinstance(s, (int, float)): return float(s)
    s = str(s).strip().replace('€','').replace('£','').replace(' ','')
    if s == '': return np.nan
    try:
        if s.endswith('M'): return float(s[:-1]) * 1e6
        if s.endswith('K'): return float(s[:-1]) * 1e3
        if s.endswith('B'): return float(s[:-1]) * 1e9
        # remove non-numeric chars
        return float(re.sub(r'[^\d.]','', s))
    except:
        return np.nan

#aplicamos la primera funcion, luego la segunda

def convertir_monetary_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convierte las columnas 'Value', 'Wage' y 'Release Clause' a números y elimina las originales.
    """
    monetary_cols = ['Value', 'Wage', 'Release Clause']
    for col in monetary_cols:
        if col in df.columns:
            newc = col + '_num'
            df[newc] = df[col].apply(money_to_number)
    # Eliminar columnas originales
    df.drop(columns=[c for c in monetary_cols if c in df.columns], inplace=True)
    return df

# --- Imputacion de datos ---

def imputar_con_cero(df: pd.DataFrame, columna: str) -> pd.DataFrame:

    if columna in df.columns:
        df[columna].fillna(0, inplace=True)
    return df

def imputar_medianas(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    for col in columnas:
        if col in df.columns:
            median = df[col].median()
            df[col].fillna(median, inplace=True)
    return df

def imputar_categoricas(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    for col in columnas:
        if col in df.columns:
            if df[col].mode().empty:
                df[col].fillna("Unknown", inplace=True)
            else:
                moda = df[col].mode()[0]
                df[col].fillna(moda, inplace=True)
    return df

#ojo con esta funcion, algo compleja 
def procesar_joined(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  # Evita warnings de "chained assignment"
    
    for col in ['Joined_Year', 'Joined_Month', 'Joined_Day']:
        if col in df.columns and df[col].isnull().any():
            moda = df[col].mode()
            if not moda.empty:
                df[col] = df[col].fillna(moda[0])
            else:
                # Si toda la columna es NaN, rellenar con un valor por defecto
                df[col] = df[col].fillna(0)
    
    if 'Joined' in df.columns:
        df.drop(columns=['Joined'], inplace=True)
    
    return df


# transformacion de datos 2: label y onehot
# en la creacion de esta funcion, estaba toda la limpieza terminada
# pero luego al crear los 5 modelos de regresion, me di cuenta que se me olvido 
#tranformar las columnas categorias a valores numericos
#por lo que esta funcion se realiza al final, no se si el orden esta bien o mal, pero para considerar que esta es una excepcion
#Lo bueno de este error, es que podemos ver la reutilizacion de codigo en kedro en pipeline.py
#en la que realizamos una transformacion utilizando todas las funciones y luego la funcion transformacion2_columns_node
#para los 3 datasets

#Este proceso se puede hacer con muchos nodos en nodes.py 
#tambien se pueden crear otros pipelines para disminuir la cantidad de codigo en nodes.py
# ejemplo: se sabe que para cada pipeline se realizan tareas similares como limpieza, transformacion, etc
# por lo que se puede crear un pipeline para limpieza, otro para transformacion, etc


'''
pipelines >
> classification_models
> data_engineering
> data_science
> feature_engineering
> feature_selection
> regression_models
> reporting

'''

def transformacion2_columns(df, target='Overall_Class'):
    """
    Reduce columnas One-Hot y LabelEncoder para FIFA datasets:
    - Agrupa Best Position
    - Agrupa Body Type
    - Simplifica Attack/Defense Work Rate
    - Codifica el target
    """

    from sklearn.preprocessing import LabelEncoder
    import pandas as pd

    # --- Agrupar Best Position ---
    pos_map = {
        'GK':'GK', 'CB':'DF', 'LB':'DF', 'RB':'DF', 'LWB':'DF', 'RWB':'DF',
        'CM':'MF', 'CDM':'MF', 'CAM':'MF', 'LM':'MF', 'RM':'MF',
        'LW':'FW', 'RW':'FW', 'ST':'FW', 'CF':'FW'
    }

    if 'Best Position' in df.columns:
        df['Best_Position_Grouped'] = df['Best Position'].map(pos_map)
        df = pd.get_dummies(df, columns=['Best_Position_Grouped'], drop_first=True)
        df = df.drop(columns=[c for c in df.columns if c.startswith('Best Position_')])

    # --- Agrupar Body Type ---
    body_map = {
        'Lean (170-185)': 'Lean', 'Lean (185+)': 'Lean',
        'Normal (170-)': 'Normal', 'Normal (170-185)': 'Normal', 'Normal (185+)': 'Normal',
        'Stocky (170-)': 'Stocky', 'Stocky (170-185)': 'Stocky', 'Stocky (185+)': 'Stocky',
        'Unique': 'Unique'
    }
    body_cols = [c for c in df.columns if c.startswith('Body Type_')]
    for col in body_cols:
        for old, new in body_map.items():
            if old in col:
                df[new] = df[new] if new in df.columns else False
                df[new] = df[new] | df[col]
    df = df.drop(columns=body_cols)

    # --- Simplificar Work Rate ---
    # Attack
    attack_cols = [c for c in df.columns if c.startswith('Attack Work Rate_')]
    attack_keep = ['Attack Work Rate_Low', 'Attack Work Rate_Medium', 'Attack Work Rate_High']
    if 'Attack Work Rate_N' in df.columns:
        df['Attack Work Rate_High'] = df.get('Attack Work Rate_High', False) | df['Attack Work Rate_N']
    df = df.drop(columns=[c for c in attack_cols if c not in attack_keep])
    # Defense
    defense_cols = [c for c in df.columns if c.startswith('Defense Work Rate_')]
    defense_keep = ['Defense Work Rate_Low', 'Defense Work Rate_Medium', 'Defense Work Rate_High']
    if 'Defense Work Rate_A/ N/A' in df.columns:
        df['Defense Work Rate_High'] = df.get('Defense Work Rate_High', False) | df['Defense Work Rate_A/ N/A']
    df = df.drop(columns=[c for c in defense_cols if c not in defense_keep])

    # --- Codificar target ---
    if target in df.columns:
        df[f'{target}_Encoded'] = LabelEncoder().fit_transform(df[target])

    return df

# Procesando los dataset FIFA
# haremos lo mismo que en jupyter notebook pero ahora en el pipeline de kedro
#Retorna un dataframe limpio


def preprocess_fifa_22(fifa_22: pd.DataFrame) -> pd.DataFrame:
    """Preprocesa columnas de dinero de FIFA 22 y devuelve el DataFrame limpio."""

    # -- Eliminacion de columnas innecesarias --  

    fifa_22 = eliminar_columnas(fifa_22, ['Photo', 'Flag', 'Club Logo', 'Real Face', 'Loaned From'])
    
    # -- Eliminacion de datos atipicos --
    
    fifa_22 = eliminar_filas(fifa_22, 'Age', lambda x: x >= 39)
    fifa_22 = eliminar_filas(fifa_22, 'Overall', lambda x: x < 32)
    fifa_22 = eliminar_filas(fifa_22, 'Crossing', lambda x: x <= 7.0)
    fifa_22 = eliminar_filas(fifa_22, 'Dribbling', lambda x: x >= 96.0)
    fifa_22 = eliminar_filas(fifa_22, 'Vision', lambda x: x >= 92.0)
    fifa_22 = eliminar_filas(fifa_22, 'Penalties', lambda x: x >= 92.0)
    fifa_22 = eliminar_filas(fifa_22, 'Penalties', lambda x: x <= 8.0)
    fifa_22 = eliminar_filas(fifa_22, 'Composure', lambda x: x >= 91.0)

    # -- feature engineering --

    fifa_22 = crear_skills(fifa_22)

    fifa_22['Overall_Class'] = fifa_22['Overall'].apply(overall_class)
    fifa_22 = joined_separado(fifa_22)

    # -- Cambio de formato -- 
    
    fifa_22 = formato_position(fifa_22)
    fifa_22['Height_cm'] = formato_height(fifa_22['Height'])
    fifa_22['Weight_kg'] = formato_weight(fifa_22['Weight'])
    # Eliminar columnas originales para evitar la redundancia 
    fifa_22 = fifa_22.drop(columns=['Height', 'Weight'], errors='ignore')

    fifa_22 = convertir_monetary_columns(fifa_22)

    #fifa_22["Value_num"] = fifa_22["Value"].apply(money_to_number)
    #fifa_22["Wage_num"]  = fifa_22["Wage"].apply(money_to_number)
    #fifa_22["ReleaseClause_num"] = fifa_22["Release Clause"].apply(money_to_number)

    # -- imputacion de datos --
    fifa_22 = imputar_con_cero(fifa_22, 'Marking')

    num_cols = ['Marking', 'Volleys', 'Curve', 'Agility', 'Balance', 'Jumping', 
            'Interceptions', 'Positioning', 'Vision', 'Composure', 'SlidingTackle', 
            'DefensiveAwareness', 'ReleaseClause_num']
    fifa_22 = imputar_medianas(fifa_22, num_cols)
    
    cat_cols = ['Club', 'Body Type', 'Position', 'Jersey Number', 'Contract Valid Until']
    fifa_22 = imputar_categoricas(fifa_22, cat_cols)

    fifa_22 = procesar_joined(fifa_22)

    money_cols = ['Value_num', 'Wage_num', 'ReleaseClause_num']
    fifa_22 = imputar_medianas(fifa_22, money_cols)
    
    return fifa_22

   

def preprocess_fifa_21(fifa_21: pd.DataFrame) -> pd.DataFrame:
    # -- Eliminacion de columnas innecesarias --  
    
    fifa_21 = eliminar_columnas(fifa_21, ['Photo', 'Flag', 'Club Logo', 'Real Face', 'Loaned From'])
    
    # -- Eliminacion de datos atipicos --
    fifa_21 = eliminar_filas(fifa_21, 'Age', lambda x: x >= 39)
    fifa_21 = eliminar_filas(fifa_21, 'Overall', lambda x: x <= 46)
    fifa_21 = eliminar_filas(fifa_21, 'Special', lambda x: x >= 2303)
    fifa_21 = eliminar_filas(fifa_21, 'Reactions', lambda x: x <= 24.0)
    fifa_21 = eliminar_filas(fifa_21, 'Penalties', lambda x: x >= 94.0)
    fifa_21 = eliminar_filas(fifa_21, 'Penalties', lambda x: x <= 8.0)

    # -- feature engineering --
    fifa_21 = crear_skills(fifa_21)
    fifa_21['Overall_Class'] = fifa_21['Overall'].apply(overall_class)
    fifa_21 = joined_separado(fifa_21)

    # -- Cambio de formato --

    fifa_21 = formato_position(fifa_21)
    fifa_21['Height_cm'] = formato_height(fifa_21['Height'])
    fifa_21['Weight_kg'] = formato_weight(fifa_21['Weight'])
    fifa_21 = fifa_21.drop(columns=['Height', 'Weight'], errors='ignore')

    fifa_21 = convertir_monetary_columns(fifa_21)

    # -- imputacion de datos --
    fifa_21 = imputar_con_cero(fifa_21, 'Marking')

    num_cols = ['Marking', 'Volleys', 'Curve', 'Agility', 'Balance', 'Jumping', 
            'Interceptions', 'Positioning', 'Vision', 'Composure', 'SlidingTackle', 
            'DefensiveAwareness', 'ReleaseClause_num']
    fifa_21 = imputar_medianas(fifa_21, num_cols)

    cat_cols = ['Club', 'Body Type', 'Position', 'Jersey Number', 'Contract Valid Until']
    fifa_21 = imputar_categoricas(fifa_21, cat_cols)

    fifa_21 = procesar_joined(fifa_21)

    money_cols = ['Value_num', 'Wage_num', 'ReleaseClause_num']
    fifa_21 = imputar_medianas(fifa_21, money_cols)

    return fifa_21



def preprocess_fifa_20(fifa_20: pd.DataFrame) -> pd.DataFrame:
    # -- Eliminacion de columnas innecesarias --
    fifa_20 = eliminar_columnas(fifa_20, ['Photo', 'Flag', 'Club Logo', 'Real Face', 'Loaned From'])

    # -- Eliminacion de datos atipicos --
    fifa_20 = eliminar_filas(fifa_20, 'Age', lambda x: x >= 38)
    fifa_20 = eliminar_filas(fifa_20, 'Overall', lambda x: x <= 44)
    fifa_20 = eliminar_filas(fifa_20, 'Special', lambda x: x >= 2299)
    fifa_20 = eliminar_filas(fifa_20, 'ShortPassing', lambda x: x >= 92)
    fifa_20 = eliminar_filas(fifa_20, 'Potential', lambda x: x <= 46)
    fifa_20 = eliminar_filas(fifa_20, 'LongPassing', lambda x: x <= 13)
    fifa_20 = eliminar_filas(fifa_20, 'BallControl', lambda x: x >= 93)
    fifa_20 = eliminar_filas(fifa_20, 'ShotPower', lambda x: x <= 19)
    fifa_20 = eliminar_filas(fifa_20, 'Penalties', lambda x: x <= 8)

    # -- feature engineering --
    fifa_20 = crear_skills(fifa_20)
    fifa_20['Overall_Class'] = fifa_20['Overall'].apply(overall_class)
    fifa_20 = joined_separado(fifa_20)

    # -- Cambio de formato --
    fifa_20 = formato_position(fifa_20)
    fifa_20['Height_cm'] = formato_height(fifa_20['Height'])
    fifa_20['Weight_kg'] = formato_weight(fifa_20['Weight'])
    fifa_20 = fifa_20.drop(columns=['Height', 'Weight'], errors='ignore')

    fifa_20 = convertir_monetary_columns(fifa_20)

    # -- imputacion de datos --
    fifa_20 = imputar_con_cero(fifa_20, 'Marking')
    num_cols = ['Marking', 'Volleys', 'Curve', 'Agility', 'Balance', 'Jumping', 
            'Interceptions', 'Positioning', 'Vision', 'Composure', 'SlidingTackle', 
            'DefensiveAwareness', 'ReleaseClause_num']
    fifa_20 = imputar_medianas(fifa_20, num_cols)

    cat_cols = ['Club', 'Body Type', 'Position', 'Jersey Number', 'Contract Valid Until']
    fifa_20 = imputar_categoricas(fifa_20, cat_cols)

    fifa_20 = procesar_joined(fifa_20)

    money_cols = ['Value_num', 'Wage_num', 'ReleaseClause_num']
    fifa_20 = imputar_medianas(fifa_20, money_cols)


    return fifa_20

#Union de tablas 

def create_model_input_table(fifa_22: pd.DataFrame, fifa_21: pd.DataFrame, fifa_20: pd.DataFrame) -> pd.DataFrame:
   
    fifa_22 = fifa_22.copy()
    fifa_21 = fifa_21.copy()
    fifa_20 = fifa_20.copy()
    
    # Añadir columna de año a cada DataFrame
    fifa_22['Year'] = 2022
    fifa_21['Year'] = 2021
    fifa_20['Year'] = 2020

    # Seleccionar columnas comunes
    #Se reliza la union de las tablas de manera vertical ya que tienen las mismas columnas
    #Esto tiene mas sentido para nuestro contexto porque sino habria que hacer muchas transformaciones para que tengan las mismas columnas
 
    FIFA_DF = pd.concat([fifa_22, fifa_21, fifa_20], ignore_index=True)

    #Eliminamos la ID porque ya no sera necesario ya que realizamos la union de los dataframes
    FIFA_DF = FIFA_DF.drop(columns=['ID'], errors='ignore')

    model_input_table = FIFA_DF

    return model_input_table    


## Como mencione anteriormente, podemos hacer varias funcionres madres en la que cada
#una puede tener su proposito para que no haga una sola funcion todo el trabajo

#Ojo, verificar si esto deberia ser asi o no (Brandon)

#ejemplos

#def limpieza_datos(fifa_data: pd.DataFrame) -> pd.DataFrame:
#   # Realiza todas las tareas de limpieza de datos
#   return fifa_data_cleaned
#def transformacion_datos(fifa_data: pd.DataFrame) -> pd.DataFrame:
#   # Realiza todas las tareas de transformacion de datos
#   return fifa_data_transformed
#def imputacion_datos(fifa_data: pd.DataFrame) -> pd.DataFrame:
#   # Realiza todas las tareas de imputacion de datos
#   return fifa_data_imputed
#def feature_engineering(fifa_data: pd.DataFrame) -> pd.DataFrame:
#   # Realiza todas las tareas de feature engineering
#   return fifa_data_featurized
#def create_model_input_table(fifa_22: pd.DataFrame, fifa_21: pd.DataFrame, fifa_20: pd.DataFrame) -> pd.DataFrame:
#   # Realiza la union de las tablas procesadas
#   return model_input_table
