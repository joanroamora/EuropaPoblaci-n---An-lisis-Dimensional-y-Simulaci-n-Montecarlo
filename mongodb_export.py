import pandas as pd
from pymongo import MongoClient

def inject_data_to_mongodb(csv_filepath, db_name, collection_name, mongo_url="mongodb://localhost:27017/"):
    # Conectar a MongoDB
    client = MongoClient(mongo_url)
    db = client[db_name]
    collection = db[collection_name]

    # Leer los datos del archivo CSV
    df = pd.read_csv(csv_filepath)

    # Convertir el DataFrame a un diccionario para inyectarlo en MongoDB
    data_dict = df.to_dict("records")
    
    # Insertar los datos en la colección de MongoDB
    collection.insert_many(data_dict)
    
    print(f"Datos inyectados en la base de datos '{db_name}', colección '{collection_name}'.")

def export_data_from_mongodb(db_name, collection_name, export_filepath, mongo_url="mongodb://localhost:27017/"):
    # Conectar a MongoDB
    client = MongoClient(mongo_url)
    db = client[db_name]
    collection = db[collection_name]

    # Extraer los datos de la colección y convertirlos en un DataFrame
    data = list(collection.find())
    df = pd.DataFrame(data)
    
    # Remover la columna '_id' si existe
    if '_id' in df.columns:
        df.drop('_id', axis=1, inplace=True)
    
    # Exportar los datos a un archivo CSV
    df.to_csv(export_filepath, index=False)
    
    print(f"Datos exportados de la colección '{collection_name}' a '{export_filepath}'.")

