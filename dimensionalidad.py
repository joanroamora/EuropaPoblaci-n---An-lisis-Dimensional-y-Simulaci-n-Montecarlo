import pandas as pd
from sklearn.decomposition import PCA

# Función para aplicar PCA al dataset
def apply_pca(df, n_components=2):
    # Seleccionar solo las columnas numéricas
    numeric_cols = df.select_dtypes(include=[float, int])

    # Aplicar PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(numeric_cols)

    # Crear un nuevo DataFrame con las componentes principales
    pca_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(n_components)])
    
    return pca_df, pca.explained_variance_ratio_

# Función para guardar los resultados de PCA
def save_pca_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)
