import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

def aplicar_pca(datos: pd.DataFrame, n_componentes: int) -> pd.DataFrame:
    pca = PCA(n_components=n_componentes)
    componentes = pca.fit_transform(datos)
    columnas = [f"PC{i+1}" for i in range(n_componentes)]
    df_pca = pd.DataFrame(componentes, columns=columnas, index=datos.index)
    return df_pca

def aplicar_tsne_umap(datos: pd.DataFrame, metodo: str, n_componentes: int, random_state: int) -> pd.DataFrame:
    if metodo == "tsne":
        modelo = TSNE(n_components=n_componentes, random_state=random_state)
        salida = modelo.fit_transform(datos)
    elif metodo == "umap":
        modelo = umap.UMAP(n_components=n_componentes, random_state=random_state)
        salida = modelo.fit_transform(datos)
    else:
        raise ValueError("Método debe ser 'tsne' o 'umap'")
    
    columnas = [f"{metodo.upper()}_{i+1}" for i in range(n_componentes)]
    df_transformado = pd.DataFrame(salida, columns=columnas, index=datos.index)
    return df_transformado
