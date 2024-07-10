import requests

class EpgCategory:
    def __init__(self, authpn, authpt, device_id, device_category, device_model, device_type, device_so):
        self.authpn = authpn
        self.authpt = authpt
        self.device_id = device_id
        self.device_category = device_category
        self.device_model = device_model
        self.device_type = device_type
        self.device_so = device_so
        self.base_url = "https://mfwkweb-api.clarovideo.net/services/epg"

    def obtener_menu_id(self, region, category):
        url = f"{self.base_url}/menu"
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
            "region": region,
            "HKS": "crfo8vqovsr96omiuhi8dqlkt2"
        }
        response = requests.get(url, params=params)
        data = response.json()
        for entry in data["response"]["nodes"]:
            if entry["text"] == category:
                return entry["id"]
        return None

    def obtener_lineup(self, region, category, node_id):
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
            "region": region,
            "HKS": "web660db1a7c502b",
            "user_id": "73602464",
            "date_from": "20240402153000",
            "date_to": "20240403153000",
            "node_id": node_id,
            "quantity": "200",
            "tenant_code": "clarovideo",
            "type": "epg",
            "metadata": "reduced"
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data['response']['channels']

    def buscar_canal(self, region, category, channel_name, node_id):
        channels = self.obtener_lineup(region, category, node_id)
        for channel in channels:
            if channel['name'] == channel_name:
                return channel
        return None


if __name__ == "__main__":
    authpn = "webclient"
    authpt = "tfg1h3j4k6fd7"
    device_id = "web"
    device_category = "web"
    device_model = "web"
    device_type = "web"
    device_so = "Chrome"

    region = input("Ingrese la región: ").lower()
    category = input("Ingrese la categoría: ")
    category = category.capitalize()
    channel_name = input("Ingrese el nombre del canal que desea buscar: ")
    channel_name = channel_name.upper()

    epg_client = EpgCategory(authpn, authpt, device_id, device_category, device_model, device_type, device_so)
    menu_id = epg_client.obtener_menu_id(region, category)

    if menu_id:
        canal = epg_client.buscar_canal(region, category, channel_name, menu_id)

        if canal:
            print(f"Se encontró el canal {channel_name} en la categopria de {category.upper()}:")
            print(f"\tNumber: {canal['number']}")
            print(f"\tName: {canal['name']}")
            print(f"\tImage: {canal['image']}")
        else:
            print(f"No se encontró el canal {channel_name} en la categoría {category}. "
                  f"Revisa si es correcto el nombre del canal ingresado.")
    else:
        print(f"No se encontró la categoría '{category}' en la región de '{region}'.")


'''

Parsear toda la string , hacerlo en minusculas , funcion con regex , expreciones regulares 
que traiga todas la info que tenga espn / ENGLISH PREMIER LEAGUE
agregar funcion del tiempo , date from / Date to 
'''