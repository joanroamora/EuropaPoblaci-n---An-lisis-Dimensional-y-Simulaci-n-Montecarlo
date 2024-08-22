import pandas as pd

# Función para aplicar la reducción de dimensionalidad personalizada
def reduce_dimensionality(df):
    # Crear nuevas columnas combinando pares de años
    df['Population 2013-2014'] = df[['Population 2013', 'Population 2014']].mean(axis=1)
    df['Population 2015-2016'] = df[['Population 2015', 'Population 2016']].mean(axis=1)
    df['Population 2017-2018'] = df[['Population 2017', 'Population 2018']].mean(axis=1)
    df['Population 2019-2020'] = df[['Population 2019', 'Population 2020']].mean(axis=1)
    df['Population 2021-2022'] = df[['Population 2021', 'Population 2022']].mean(axis=1)
    
    # Seleccionar las columnas finales
    reduced_df = df[['Country', 'Population 2013-2014', 'Population 2015-2016', 
                     'Population 2017-2018', 'Population 2019-2020', 'Population 2021-2022']]
    
    return reduced_df

# Función para guardar el DataFrame reducido
def save_reduced_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)
