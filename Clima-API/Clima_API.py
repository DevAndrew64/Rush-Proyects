
import os
import requests
from dotenv import load_dotenv

# Obtenernos variable privada en archivo de entorno (Donde está la API)
load_dotenv()

# Obtener clima actual de la ciudad
ciudad = "Barranquilla"
api_key =  os.getenv("API_KEY")
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

respuesta = requests.get(url)
datos = respuesta.json()

# Aqui para buscar los datos se acceden a ellos por indices, como si se "desglosara"
if respuesta.status_code == 200:
    temperatura = datos["main"]["temp"]
    descripcion = datos["weather"][0]["description"]
    print(f"En {ciudad}: {temperatura}°C, {descripcion}")
else:
    print(f"Error: {respuesta.status_code}")
    