import requests
from colombia import obtener_info_colombia
from departamentos import obtener_departamentos
from regiones import obtener_regiones
from turismo import obtener_atracciones

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Información general de Colombia")
        print("2. Lista de departamentos")
        print("3. Regiones de Colombia")
        print("4. Atracciones turísticas")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            obtener_info_colombia()
        elif opcion == "2":
            obtener_departamentos()
        elif opcion == "3":
            obtener_regiones()
        elif opcion == "4":
            obtener_atracciones()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()
