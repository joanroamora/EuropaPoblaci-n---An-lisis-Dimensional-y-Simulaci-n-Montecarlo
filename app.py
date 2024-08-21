from preprocesamiento import load_data, clean_data, save_clean_data
from dimensionalidad import apply_pca, save_pca_data

def main():
    # Ruta al archivo CSV original
    filepath = './data/europe.csv'
    
    # Cargar los datos
    print("Cargando los datos...")
    df = load_data(filepath)
    
    # Limpiar los datos
    print("Limpiando los datos...")
    df_cleaned = clean_data(df)
    
    # Guardar el dataset limpio
    cleaned_output_filepath = './data/europe_cleaned.csv'
    print(f"Guardando el dataset limpio en '{cleaned_output_filepath}'...")
    save_clean_data(df_cleaned, cleaned_output_filepath)
    
    # Aplicar PCA para reducción de dimensionalidad
    print("Aplicando PCA para reducción de dimensionalidad...")
    pca_df, explained_variance = apply_pca(df_cleaned, n_components=2)
    print(f"Varianza explicada por las componentes principales: {explained_variance}")
    
    # Guardar el dataset reducido
    pca_output_filepath = './data/europe_pca.csv'
    print(f"Guardando el dataset reducido en '{pca_output_filepath}'...")
    save_pca_data(pca_df, pca_output_filepath)
    
    print("Proceso completado.")

if __name__ == "__main__":
    main()
