import requests

def obtener_departamentos():
    url = "https://api-colombia.com/api/v1/Department"
    response = requests.get(url)

    if response.status_code == 200:
        departamentos = response.json()
        for depto in departamentos:
            print(f"Departamento: {depto['name']}")
            print(f"Descripción: {depto.get('description', 'No disponible')}")

           
            city = depto.get('city')
            if city:
                print(f"Capital: {city.get('name', 'No disponible')}")
                print(f"Descripción de la capital: {city.get('description', 'No disponible')}")
            else:
                print("Capital: No disponible")
                print("Descripción de la capital: No disponible")

            print("-" * 50)
    else:
        print("Error al obtener la información")

obtener_departamentos()
