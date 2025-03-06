import requests

def obtener_info_colombia():
    url = "https://api-colombia.com/api/v1/Country/Colombia"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Nombre: {data['name']}")
        print(f"Descripción: {data['description']}")
        print(f"Moneda: {data['currencyCode']}")
    else:
        print("Error al obtener la información")

obtener_info_colombia()
