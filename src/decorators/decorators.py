import time  # Importa el módulo time para medir el tiempo de ejecución
import logging  # Importa el módulo logging para registrar mensajes

# Configurar el logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

"""
Configura el registro de mensajes (logging) para que muestre mensajes de nivel INFO y superior.
Define el formato de los mensajes de registro, incluyendo la marca de tiempo (asctime), el nivel del mensaje (levelname) y el mensaje en sí (message).
"""

def timeit(func):
    """Decorador para medir el tiempo de ejecución de una función."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Registra el tiempo de inicio
        result = func(*args, **kwargs)  # Ejecuta la función decorada
        end_time = time.time()  # Registra el tiempo de finalización
        elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
        logging.info(f"{func.__name__} executed in {elapsed_time:.4f} seconds")  # Registra el tiempo de ejecución
        return result  # Devuelve el resultado de la función
    return wrapper  # Devuelve el decorador

def logit(func):
    """Decorador para registrar la ejecución de una función."""
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__}")  # Registra el inicio de la ejecución de la función
        result = func(*args, **kwargs)  # Ejecuta la función decorada
        logging.info(f"Completed {func.__name__}")  # Registra la finalización de la ejecución de la función
        return result  # Devuelve el resultado de la función
    return wrapper  # Devuelve el decorador
