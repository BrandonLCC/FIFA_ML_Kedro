"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.0.0
"""

#Copiado del proyecto de ejemplo de Kedro (Borrar cuando no sea necesario)

import pandas as pd
import numpy as np
import pandas as pd

def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    x = x.str.replace("%", "")
    x = x.astype(float) / 100
    return x


def _parse_money(x: pd.Series) -> pd.Series:
    x = x.str.replace("M", "").str.replace(",", "")
    x = x.astype(float)
    return x

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
    

# Procesando los dataset FIFA
# haremos lo mismo que en jupyter notebook pero ahora en el pipeline de kedro
#Retorna un dataframe limpio

def preprocess_fifa_22(fifa_22: pd.DataFrame) -> pd.DataFrame:
    try:
        """Preprocesa columnas de dinero de FIFA 22 y devuelve el DataFrame limpio."""
        
        fifa_22["Value_num"] = fifa_22["Value"].apply(money_to_number)
        fifa_22["Wage_num"]  = fifa_22["Wage"].apply(money_to_number)
        fifa_22["ReleaseClause_num"] = fifa_22["Release Clause"].apply(money_to_number)

        return fifa_22
    
    except Exception as e:
        print(f"Error al preprocesar FIFA 22: {e}")
        return fifa_22



def preprocess_fifa_21(fifa_21: pd.DataFrame) -> pd.DataFrame:
    try:
        """Preprocesa columnas de dinero de FIFA 22 y devuelve el DataFrame limpio."""
        
        fifa_21["Value_num"] = fifa_21["Value"].apply(money_to_number)
        fifa_21["Wage_num"]  = fifa_21["Wage"].apply(money_to_number)
        fifa_21["ReleaseClause_num"] = fifa_21["Release Clause"].apply(money_to_number)

        return fifa_21

    except Exception as e:
        print(f"Error al preprocesar FIFA 22: {e}")
        return fifa_21
    
def preprocess_fifa_20(fifa_20: pd.DataFrame) -> pd.DataFrame:
    try:
        """Preprocesa columnas de dinero de FIFA 22 y devuelve el DataFrame limpio."""
        
        fifa_20["Value_num"] = fifa_20["Value"].apply(money_to_number)
        fifa_20["Wage_num"]  = fifa_20["Wage"].apply(money_to_number)
        fifa_20["ReleaseClause_num"] = fifa_20["Release Clause"].apply(money_to_number)

        return fifa_20

    except Exception as e:
        print(f"Error al preprocesar FIFA 22: {e}")
        return fifa_20


#DA ERROR AL EJECUTAR kedro run