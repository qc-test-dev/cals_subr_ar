
#!/usr/local/bin/python3
'''
En este script tiene como fin imprimir el mosaico de cualquier categoría para dispositivos ZTE ATV de TATA
Los parámetros que se usan es ingresando la región solicitada y el id del mosaico a usar
'''
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def obtener_epg_version(region):
    url = f"https://mfwkstbzte-api.clarovideo.net/services/epg/version?api_version=v5.93&authpn=tataelxsi&authpt=vofee7ohhecai&device_category=stb&device_manufacturer=ZTE&device_model=androidTV&device_so=Android%2010&device_type=ptv&format=json&region={region}"
    session = requests.Session()
    retry = Retry(connect=5, read=5, redirect=5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    response = session.get(url, verify=False)
    data = response.json()
    epg_version = data['response']['epg_version']
    return epg_version

def obtener_lineup(region, node_id):
    epg_version = obtener_epg_version(region)
    url = f"https://mfwkstbzte-api.clarovideo.net/services/epg/lineup?authpn=tataelxsi&authpt=vofee7ohhecai&device_category=stb&device_manufacturer=ZTE&device_type=ptv&format=json&from=0&metadata=full&quantity=2000&api_version=v5.93&device_model=androidTV&epg_version={epg_version}&node_id={node_id}&region={region}"
    session = requests.Session()
    retry = Retry(connect=5, read=5, redirect=5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    response = session.get(url, verify=False)
    data = response.json()
    canales = data['response']['channels']
    for canal in canales:
        print("Channel:")
        print(f"\tNumber: {canal['number']}")
        print(f"\tName: {canal['name']}")
        print(f"\tImage: {canal['image']}")
        #print()

if __name__ == "__main__":
    region = input("Ingrese la región: ")
    node_id = input("Ingrese el node_id: ")
    obtener_lineup(region, node_id)
