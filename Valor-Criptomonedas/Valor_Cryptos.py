import requests
import json
import os

""""
Autor: Jhon Ponton
Inspiracion: Propia
Proyecto numero 3 de 50

Este programa obtiene el valor de algunas criptomonedas del mercado bursatil en tiempo real
y la dispone en la divisa que se configure.
"""

# Funcion para obtener el precio de la bitcoin (Oportunidad dde mejora)
def obtener_precio_bitcoin():
    """
    Esta función obtiene el precio actual de Bitcoin en la moneda especificada.
    Por defecto, devuelve el precio en USD.
    """
    key = os.getenv("API_CRIPTO_CONSULTA")
    url = f"https://data-api.coindesk.com/index/cc/v1/latest/tick?market=ccix&instruments=BTC-USD&api_key={key}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() # Verifica errores de conexión
        datos = respuesta.json()
        precio = datos["Data"]["BTC-USD"]["VALUE"] # sacamos el precio según la moneda en este caso USD
        tendencia = datos["Data"]["BTC-USD"]["VALUE_FLAG"]
        
        if tendencia == "UP":
            tendencia = "Subir"
        elif tendencia == "DOWN":
            tendencia = "Bajar"
        
        return f"Valor actual de BTC: {precio} con tendencia a {tendencia} "
    
    except requests.exceptions.RequestException as e:
        return f"Error al obtener datos de Bitcoin {e}"
    
# Ejecutamos en primer plano
if __name__ == "__main__":
    print(obtener_precio_bitcoin())