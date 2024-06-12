import pandas as pd  # Importa pandas para manejo de datos
import os  # Importa os para manejo del sistema de archivos
from ..decorators.decorators import timeit, logit  # Importa los decoradores personalizados

@logit  # Añade logging a la función
@timeit  # Mide el tiempo de ejecución de la función
def load_data(data_path):
    """
    Cargamos los datos desde un archivo CSV o Excel.

    Args :
        data_path (str) : Ruta del archivo a cargar.

    Returns :
        pd.DataFrame: DataFrame de pandas con los datos cargados.

    Raises :
        ValueError: Si el formato del archivo no es soportado.
    """
    if data_path.endswith('.csv'):
        df = pd.read_csv(data_path)  # Lee datos desde un archivo CSV
    elif data_path.endswith('.xlsx'):
        df = pd.read_excel(data_path)  # Lee datos desde un archivo Excel
    else:
        raise ValueError("Unsupported file format")  # Lanza un error si el formato no es compatible
    print("Data loaded successfully")  # Imprime un mensaje indicando que los datos se cargaron correctamente
    return df  # Devuelve el DataFrame con los datos cargados

@logit  # Añade logging a la función
@timeit  # Mide el tiempo de ejecución de la función
def clean_data(df):
    """
    Limpiamos los datos.

    Args :
        df (pd.DataFrame) : DataFrame con los datos a limpiar.

    Returns :
        pd.DataFrame: DataFrame con los datos limpios
    """
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)  # Limpia y convierte la columna de precios a tipo float
    print("Data cleaned successfully")  # Imprime un mensaje indicando que los datos se limpiaron correctamente
    return df  # Devuelve el DataFrame con los datos limpiados

@logit  # Añade logging a la función
@timeit  # Mide el tiempo de ejecución de la función
def analyze_data(df):
    """
    Realizamos un analisis basico de los datos.

    Args :
        df (pd.DataFrame) : DataFrame con los datos a utilizar

    """
    print("Basic Data Analysis:")  # Imprime un título para la sección de análisis básico
    print(df.describe())  # Muestra estadísticas descriptivas de los datos
    print("\nProducts with highest prices:")  # Imprime un título para la sección de productos con precios más altos
    print(df.nlargest(5, 'price'))  # Muestra los 5 productos con los precios más altos

@logit  # Añade logging a la función
@timeit  # Mide el tiempo de ejecución de la función
def save_clean_data(df, output_path):
    """
    Guardamos los datos limpios en un archivo CSV o Excel.

    Args :
        df (pd.DataFrame) : DataFrame con los datos a guardar.
        output_path (str) : Ruta del archivo de salida.

    Raises :
        ValueError: Si el formato del archivo no es soportado.
    """
    if output_path.endswith('.csv'):
        df.to_csv(output_path, index=False)  # Guarda los datos en un archivo CSV sin índice
    elif output_path.endswith('.xlsx'):
        df.to_excel(output_path, index=False)  # Guarda los datos en un archivo Excel sin índice
    else:
        raise ValueError("Unsupported file format")  # Lanza un error si el formato no es compatible
    print(f"Clean data saved to {output_path}")  # Imprime un mensaje indicando que los datos se guardaron correctamente

if __name__ == "__main__":
    data_path = "data/raw/products.csv"  # Define la ruta del archivo de datos
    output_path = "data/processed/cleaned_products.csv"  # Define la ruta del archivo de datos limpios
    
    df = load_data(data_path)  # Carga los datos
    df = clean_data(df)  # Limpia los datos
    analyze_data(df)  # Analiza los datos
    os.makedirs("/data/processed", exist_ok=True)  # Crea el directorio de salida si no existe
    save_clean_data(df, output_path)  # Guarda los datos limpios
