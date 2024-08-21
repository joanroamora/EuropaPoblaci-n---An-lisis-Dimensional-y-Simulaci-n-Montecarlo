import pandas as pd
from sklearn.decomposition import PCA

# Función para aplicar PCA al dataset
def apply_pca(df, n_components=2):
    # Mantener los nombres de los países
    countries = df['Country']

    # Seleccionar solo las columnas numéricas
    numeric_cols = df.select_dtypes(include=[float, int])

    # Aplicar PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(numeric_cols)

    # Crear un nuevo DataFrame con las componentes pclear
    # rincipales y los nombres de los países
    pca_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(n_components)])
    pca_df.insert(0, 'Country', countries)  # Insertar los nombres de los países al principio
    
    return pca_df, pca.explained_variance_ratio_

# Función para guardar los resultados de PCA
def save_pca_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)
