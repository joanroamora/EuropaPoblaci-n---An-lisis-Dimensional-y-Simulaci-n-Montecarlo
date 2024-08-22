from preprocesamiento import load_data, clean_data, save_clean_data
from dimensionalidad import reduce_dimensionality, save_reduced_data
from montecarlo import montecarlo_simulation, save_simulation_results
from mongodb_export import inject_data_to_mongodb, export_data_from_mongodb

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
    
    # Reducir la dimensionalidad combinando pares de años
    print("Reduciendo la dimensionalidad del dataset...")
    reduced_df = reduce_dimensionality(df_cleaned)
    
    # Guardar el dataset reducido
    reduced_output_filepath = './data/europe_pca.csv'
    print(f"Guardando el dataset reducido en '{reduced_output_filepath}'...")
    save_reduced_data(reduced_df, reduced_output_filepath)
    
    # Realizar la simulación de Montecarlo
    print("Realizando simulación de Montecarlo...")
    combined_df = montecarlo_simulation(reduced_df)
    
    # Guardar los resultados de la simulación
    simulation_output_filepath = './data/europe_montecarlo.csv'
    print(f"Guardando los resultados de la simulación en '{simulation_output_filepath}'...")
    save_simulation_results(combined_df, simulation_output_filepath)
    
    # Inyectar datos a MongoDB
    print("Inyectando datos en MongoDB...")
    inject_data_to_mongodb(simulation_output_filepath, db_name="EuropePopulationDB", collection_name="PopulationProjections")
    
    # Exportar los datos desde MongoDB
    export_filepath = './data/europe_mongodb_export.csv'
    print(f"Exportando los datos desde MongoDB a '{export_filepath}'...")
    export_data_from_mongodb(db_name="EuropePopulationDB", collection_name="PopulationProjections", export_filepath=export_filepath)
    
    print("Proceso completado.")

if __name__ == "__main__":
    main()
