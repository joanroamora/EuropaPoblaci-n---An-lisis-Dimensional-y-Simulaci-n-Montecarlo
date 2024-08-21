import pandas as pd
import numpy as np

# Función para cargar el dataset
def load_data(filepath):
      return pd.read_csv(filepath)

# Función para limpiar el dataset
def clean_data(df):
    # Aplicar la imputación solo a columnas numéricas
    numeric_cols = df.select_dtypes(include=[np.number])
    df[numeric_cols.columns] = numeric_cols.apply(lambda row: row.fillna(row.mean()), axis=1)
    return df


# Función para guardar el dataset limpio
def save_clean_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)