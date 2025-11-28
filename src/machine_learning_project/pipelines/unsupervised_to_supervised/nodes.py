import pandas as pd
from sklearn.model_selection import train_test_split

def create_supervised_datasets(
    clean_dataset: pd.DataFrame,
    features_regression: list,
    target_regression: str,
    features_classification: list,
    target_classification: str,
    test_size_reg: float,
    test_size_class: float,
    random_state: int,
    stratify_class: bool
):
    # --- REGRESIÓN ---
    X_reg = clean_dataset[features_regression]
    y_reg = clean_dataset[target_regression]
    
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
        X_reg, y_reg, test_size=test_size_reg, random_state=random_state
    )
    
    # --- CLASIFICACIÓN ---
    X_class = clean_dataset[features_classification]
    y_class = clean_dataset[target_classification]
    
    stratify = y_class if stratify_class else None
    
    X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(
        X_class, y_class, test_size=test_size_class, random_state=random_state, stratify=stratify
    )
    
    return (
        X_train_reg, X_test_reg, y_train_reg, y_test_reg,
        X_train_class, X_test_class, y_train_class, y_test_class
    ) 
