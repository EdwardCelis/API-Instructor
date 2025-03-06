import requests

def obtener_regiones():
    url = "https://api-colombia.com/api/v1/Region"
    response = requests.get(url)

    if response.status_code == 200:
        regiones = response.json()
        for region in regiones:
            print(f"Región: {region['name']}")
            print(f"Descripción: {region.get('description', 'No disponible')}")
            print("-" * 50)
    else:
        print("Error al obtener la información")

obtener_regiones()
