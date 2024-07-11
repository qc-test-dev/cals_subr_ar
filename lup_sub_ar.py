#!/usr/local/bin/python3
'''
En esta rama se imprimen los resultados en la terminal  y se tienen los dispos:

                            Android Mobile : ADR M \n"
                              "iOS Mobile : IOS M \n"
                              "WEB : WEB \n"
                              "Claro TV TATA o IPTV/AOSP : Iptv \n"
                              "Roku : Rk \n"
No guarda info en excel
'''
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Deshabilitar advertencias de solicitudes inseguras
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class EpgCategory:
    def __init__(self, base_url, authpn, authpt, device_id, device_category, device_model, device_type, device_so,
                 node_id):
        """
        Inicializa la clase EpgCategory con los parámetros de autenticación y del dispositivo.

        :param base_url: URL base para las solicitudes de la API
        :param authpn: Nombre de autenticación
        :param authpt: Tipo de autenticación
        :param device_id: ID del dispositivo
        :param device_category: Categoría del dispositivo
        :param device_model: Modelo del dispositivo
        :param device_type: Tipo de dispositivo
        :param device_so: Sistema operativo del dispositivo
        :param node_id: Node ID del dispositivo
        """
        self.base_url = base_url
        self.authpn = authpn
        self.authpt = authpt
        self.device_id = device_id
        self.device_category = device_category
        self.device_model = device_model
        self.device_type = device_type
        self.device_so = device_so
        self.node_id = node_id

    def obtener_menu_id(self, subregion):
        """
        Obtiene el ID del menú (epg_version) para una subregión dada.

        :param subregion: Subregión para la cual se quiere obtener el epg_version
        :return: epg_version si se encuentra, de lo contrario None
        """
        url = f"{self.base_url}/version"
        params = {
            "authpn": self.authpn,
            "authpt": self.authpt,
            "device_id": self.device_id,
            "device_category": self.device_category,
            "device_model": self.device_model,
            "device_type": self.device_type,
            "device_so": self.device_so,
            "format": "json",
            "device_manufacturer": "generic",
            "api_version": "v5.93",
            "region": "argentina",
            "subregion": subregion
        }
        response = requests.get(url, params=params, verify=False)
        data = response.json()

        # Verificar que "response" esté en los datos y sea un diccionario
        if "response" in data and isinstance(data["response"], dict):
            if "epg_version" in data["response"]:
                return data["response"]["epg_version"]
        return None

    def obtener_lineup(self, epg_version, subregion):
        """
        Obtiene la lista de canales y el total de canales para un epg_version dado.

        :param epg_version: Versión del EPG para la cual se quiere obtener la lista de canales
        :param subregion: Subregión para la cual se quiere obtener la lista de canales
        :return: Lista de canales y el total de canales
        """
        url = f"{self.base_url}/lineup"
        params = {
            "authpn": self.authpn,
            "authpt": self.authpt,
            "device_id": self.device_id,
            "device_category": self.device_category,
            "device_model": self.device_model,
            "device_type": self.device_type,
            "device_so": self.device_so,
            "format": "json",
            "device_manufacturer": "generic",
            "api_version": "v5.93",
            "region": "argentina",
            "subregion": subregion,
            "epg_version": epg_version,
            "from": 0,
            "quantity": 2000,
            "metadata": "reduced"
        }
        response = requests.get(url, params=params, verify=False)
        data = response.json()

        # Validar que 'response' esté en los datos y tenga las claves necesarias
        if "response" in data and isinstance(data["response"], dict):
            if "channels" in data["response"] and "total" in data["response"]:
                return data["response"]["channels"], data["response"]["total"]
        return None, 0


if __name__ == "__main__":
    device_type_input = input("Android Mobile : ADR M \n"
                              "iOS Mobile : IOS M \n"
                              "WEB : WEB \n"
                              "Claro TV TATA o IPTV/AOSP : Iptv \n"
                              "Roku : Rk \n"
                              "Ingrese el dispositivo a consultar: ").strip().lower()
    subregion = input("Ingrese la subregion: ").strip()

    if device_type_input == "web":
        # Datos de autenticación y del dispositivo Web (OTT)
        base_url = "https://mfwkweb-api.clarovideo.net/services/epg"
        authpn = "webclient"
        authpt = "tfg1h3j4k6fd7"
        device_id = "web"
        device_category = "web"
        device_model = "web"
        device_type = "web"
        device_so = "Chrome"
        node_id = "19442"

    elif device_type_input == "iptv":
        # Datos de autenticación y del dispositivo ZTE (IPTV)
        base_url = "https://mfwkstbzte-api.clarovideo.net/services/epg"
        authpn = "tataelxsi"
        authpt = "vofee7ohhecai"
        device_id = "ZTEATV41200438593"
        device_category = "stb"
        device_model = "B866V2_V1_0_0"
        device_type = "ptv"
        device_so = "Android 12"
        node_id = "19083"

    elif device_type_input == "adr m":
        base_url = "https://mfwkmobileandroid-api.clarovideo.net/services/epg"
        authpn = "amco"
        authpt = "12e4i8l6a581a"
        device_id = "50e940ca-9ffa-4e91-a184-a4878e41238e"
        device_category = "mobile"
        device_model = "android"
        device_type = "SM-G970F"
        device_so = "Android 2013"
        node_id = "19442"

    elif device_type_input == "ios m":
        base_url = "https://mfwkmobileios-api.clarovideo.net/services/epg"
        authpn = "amco"
        authpt = "12e4i8l6a581a"
        device_id = "467C066A-F668-41A8-AC58-404B122EA991"
        device_category = "mobile"
        device_model = "aapl"
        device_type = "iPhone"
        device_so = "iOS 2015.0"
        node_id = "19442"

    elif device_type_input == "rk":
        base_url = "https://mfwkstbroku-api.clarovideo.net/services/epg"
        authpn = "roku"
        authpt = "IdbIIWeFzYdy"
        device_id = "f7785395-3dc0-5ca4-b2bd-b4e6346221e3"
        device_category = "stb"
        device_model = "generic"
        device_type = "generic"
        device_so = ""
        node_id = "19442"

    else:
        print("Tipo de dispositivo no reconocido. Verifique que sea ingresado correctamente.")
        exit()

    # Crear una instancia de EpgCategory con los parámetros correspondientes
    epg_client = EpgCategory(base_url, authpn, authpt, device_id, device_category, device_model, device_type, device_so,
                             node_id)

    # Obtener el ID del menú (epg_version) para la subregión ingresada
    menu_id = epg_client.obtener_menu_id(subregion)

    if menu_id:
        # Obtener la lista de canales y el total de canales para el epg_version
        canales, total = epg_client.obtener_lineup(menu_id, subregion)

        # Imprimir el total de canales
        print(f"\nTotal de canales: {total}")

        # Imprimir la información de cada canal
        if canales:
            for canal in canales:
                print(f"Channel: ")
                print(f"\tNumber: {canal['number']}")
                print(f"\tName: {canal['name']}")
                print(f"\tImage: {canal['image']}")
        print(f"\nTotal de canales: {total}")
    else:
        print(f"No se encontró la subregion '{subregion}' en la región de argentina.")
