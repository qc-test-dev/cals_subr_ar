#!/usr/local/bin/python3

import requests


class EPGClient:
    def __init__(self, authpn, authpt, device_id, device_category, device_model, device_type, device_so, region):
        self.authpn = authpn
        self.authpt = authpt
        self.device_id = device_id
        self.device_category = device_category
        self.device_model = device_model
        self.device_type = device_type
        self.device_so = device_so
        self.region = region
        self.base_url = "https://mfwkweb-api.clarovideo.net/services/epg"
        self.epg_version = self.obtener_epg_version()

    def obtener_epg_version(self):
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
            "region": self.region,
            "HKS": "crfo8vqovsr96omiuhi8dqlkt2"
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data['response']['epg_version']

    def obtener_lineup(self, node_id):
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
            "region": self.region,
            "epg_version": self.epg_version,
            "node_id": node_id,
            "HKS": "crfo8vqovsr96omiuhi8dqlkt2"
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data['response']['channels']




if __name__ == "__main__":
    authpn = "webclient"
    authpt = "tfg1h3j4k6fd7"
    device_id = "web"
    device_category = "web"
    device_model = "web"
    device_type = "web"
    device_so = "Chrome"
    region = input("Ingrese la región: ")
    node_id = input("Ingrese el node_id: ")

    epg_client = EPGClient(authpn, authpt, device_id, device_category, device_model, device_type, device_so, region)
    canales = epg_client.obtener_lineup(node_id)

    for canal in canales:
        print("Channel:")
        print(f"\tNumber: {canal['number']}")
        print(f"\tName: {canal['name']}")
        print(f"\tImage: {canal['image']}")



