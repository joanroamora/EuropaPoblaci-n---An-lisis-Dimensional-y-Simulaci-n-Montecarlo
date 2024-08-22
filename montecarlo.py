import numpy as np
import pandas as pd

# Función para realizar la simulación de Montecarlo
def montecarlo_simulation(df, num_simulations=1000):
    countries = df['Country']
    initial_population = df.iloc[:, -1].values  # Toma la población del último período disponible
    
    # Tasas de crecimiento anual aleatorias (normalmente distribuidas) en un rango razonable
    growth_rates = np.random.normal(loc=0.01, scale=0.005, size=(num_simulations, 4, len(initial_population)))
    
    # Array para almacenar las simulaciones
    simulations = np.zeros((num_simulations, 4, len(initial_population)))
    
    # Simulación de Montecarlo
    for i in range(num_simulations):
        for j in range(4):
            if j == 0:
                simulations[i, j, :] = initial_population * (1 + growth_rates[i, j, :])
            else:
                simulations[i, j, :] = simulations[i, j-1, :] * (1 + growth_rates[i, j, :])
    
    # Promedio de las simulaciones y redondeo para mantener la precisión adecuada
    mean_simulations = np.mean(simulations, axis=0).astype(int)
    
    # Crear un DataFrame con las proyecciones futuras
    future_df = pd.DataFrame(data=mean_simulations.T, columns=[
        'Population 2023-2024', 'Population 2025-2026', 
        'Population 2027-2028', 'Population 2029-2030'
    ])
    future_df.insert(0, 'Country', countries)
    
    # Combinar los datos originales con las proyecciones futuras
    combined_df = pd.concat([df, future_df.iloc[:, 1:]], axis=1)
    
    return combined_df

# Función para guardar los resultados de la simulación
def save_simulation_results(df, output_filepath):
    df.to_csv(output_filepath, index=False)
