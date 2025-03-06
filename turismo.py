import requests

def obtener_atracciones():
    url = "https://api-colombia.com/api/v1/TouristicAttraction"  # URL corregida
    response = requests.get(url)

    if response.status_code == 200:
        atracciones = response.json()
        
        if not atracciones:
            print("No se encontraron atracciones turísticas.")
            return
        
        for atraccion in atracciones:
            print(f"Atracción: {atraccion.get('name', 'No disponible')}")
            print(f"Descripción: {atraccion.get('description', 'No disponible')}")

            city = atraccion.get('city')
            if city:
                print(f"Ciudad: {city.get('name', 'No disponible')}")
            else:
                print("Ciudad: No disponible")

            print("-" * 50)
    else:
        print(f"Error al obtener la información. Código de estado: {response.status_code}")

obtener_atracciones()
