import requests # Importar el modulo requests para hacer las solicitudes HTTP
from bs4 import BeautifulSoup # Importamos BeautifulSoup para analizar los documentos HTML
import pandas as pd # Importamos pandas para manejar datos en los DataFrames 

def fetch_page(url):

    """
    Obtenemos el contenido de una pagina.
    
    Args :
        url (str) : URL de la pagina web a solicitar.

    Returns :
        str: Contenido HTML de la pagina Web.

    Raises :
        System exit: Si ocurre un error en la solicitud HTTP.
    """

    response= requests.get(url) # Realizamos una solicitud GET a la URL proporcionada.
    if response.status_code == 200: # Comparamos el status code con el 200 que significa que fue una peticion exitosa
        return response.content # Devolvemos el contenido de la pagina si la solicitud fue exitosa
    else:
        raise Exception(f"Failed to fetch page: {url}") # Lanzamos una excepcion por si la solicitud falla

def parse_product(product):
    """
    Analizamos los detalles de un producto.
    
    Args :
        product (bs4.element.Tag) : Objeto BeautifulSoup que contiene la informacion del producto.

    Returns :
        dict: Diccionario con Titulo, Descripcion y precio del producto

    """
    title= product.find("a",class_="title").text.strip() # Encontramos y obtenemos el titulo del producto
    description = product.find("p",class_="description").text.strip() # Encontramos y obtenemos la descripcion del producto
    price = product.find("h4",class_="price").text.strip() # Encontramos y obtenemos el precio del producto
    return{  # Retornamos un diccionario con el titulo , la descripcipn y el precio del producto
        "title":title,
        "description":description,
        "price":price,
    }

def scrape(url):
    """
    Metodo principal de scraping con soporte para multiples paginas.
    
    Args :
        url (str) : URL de la pagina web a scraoear.

    Returns :
        pd.DataFrame : DataFrame de pandas con los datos de los productos
    """
    page_content = fetch_page(url) # Obtenemos el codigo base de la pagina
    soup = BeautifulSoup(page_content, "html.parser") # Analizamos el contenido de la pagina con Beautiful Soup
    products = soup.find_all("div", class_="thumbnail") # Encontramos todos los elementos div con la clase "thumbnail" que representan productos
    products_data=[] #Inicializamos una lista para almacenar los datos de los producots.

    for product in products:
        product_info = parse_product(product) # Analizamos cada producto encontrado
        products_data.append(product_info) # Agregamos los datos del producto a la lista.

    return pd.DataFrame(products_data)

# Definnimos el URL base para el Scraping.
base_url="https://webscraper.io/test-sites/e-commerce/allinone"

# Llamamos a la funcion scrape para obtener los datos de los productos

df = scrape(base_url)

# Imprimos el DF resultante

print(df)

# Guardamos los datos en un archivo CSV sin incluir el indice.

df.to_csv('data/raw/products.csv', index=False) # Guardamos los datos en un archivo CSV sin incluir el indice.