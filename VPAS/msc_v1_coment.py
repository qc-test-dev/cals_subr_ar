#!/usr/local/bin/python3

'''

En este script tiene como fin imprimir el mosaico de cualquier categoria para dispositivos ZTE ATV de TATA
Los parametros que se usan es ingresando la region solicitada y el id del mosaico a usar

'''
import requests  # Importa la biblioteca requests para hacer solicitudes HTTP

def obtener_epg_version(region):
    # Construye la URL para obtener la versión de la guía electrónica de programación (EPG)
    url = f"https://mfwkstbzte-api.clarovideo.net/services/epg/version?api_version=v5.93&authpn=tataelxsi&authpt=vofee7ohhecai&device_category=stb&device_manufacturer=ZTE&device_model=androidTV&device_so=Android%2010&device_type=ptv&format=json&region={region}"
    # Realiza una solicitud GET a la URL y guarda la respuesta en 'response'
    response = requests.get(url)
    # Convierte la respuesta JSON en un diccionario de Python
    data = response.json()
    # Extrae la versión de la EPG de los datos JSON obtenidos
    epg_version = data['response']['epg_version']
    # Retorna la versión de la EPG
    return epg_version

def obtener_lineup(region, node_id):
    # Obtiene la versión de la EPG para la región dada
    epg_version = obtener_epg_version(region)
    # Construye la URL para obtener la lista de canales en la región y el nodo específico
    url = f"https://mfwkstbzte-api.clarovideo.net/services/epg/lineup?authpn=tataelxsi&authpt=vofee7ohhecai&device_category=stb&device_manufacturer=ZTE&device_type=ptv&format=json&from=0&metadata=full&quantity=2000&api_version=v5.93&device_model=androidTV&epg_version={epg_version}&node_id={node_id}&region={region}"
    # Realiza una solicitud GET a la URL y guarda la respuesta en 'response'
    response = requests.get(url)
    # Convierte la respuesta JSON en un diccionario de Python
    data = response.json()
    # Extrae la lista de canales de los datos JSON obtenidos
    canales = data['response']['channels']
    # Itera sobre cada canal y muestra su número y nombre
    for canal in canales:
        print("Channel:")
        print(f"\tNumber: {canal['number']}")
        print(f"\tName: {canal['name']}")
        print()

if __name__ == "__main__":
    # Solicita al usuario ingresar la región y el node_id
    region = input("Ingrese la región: ")
    node_id = input("Ingrese el node_id: ")
    # Llama a la función obtener_lineup con la región y el node_id proporcionados
    obtener_lineup(region, node_id)
