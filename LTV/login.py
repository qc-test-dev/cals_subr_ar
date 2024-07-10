#!/usr/bin/python3
import requests
from openpyxl import load_workbook


def login_cv(user,password,region,dispositivo,url_silo,device_id,device_model,device_type,device_so,device_category,device_manufacturer):
    try:
        serial_id='0'
        region = region
        usuario = user
        password = password

        base_url_login = f'http://mfwk{url_silo}-api.clarovideo.net/services/user/login'
        params = {
            'device_id': device_id,
            'device_category': device_category,
            'device_model': device_model,
            'device_type': device_type,
            'device_so': device_so,
            'format': 'json',
            'device_manufacturer': device_manufacturer,
            'authpn': 'webclient',
            'authpt': 'tfg1h3j4k6fd7',
            'api_version': 'v5.93',
            'HKS': 'b9iu6knalnpolkaeu5dagfs5e5',
            'includpaywayprofile': 'true',
            'region': region,
            'username': usuario,
            'password': password,
        }

        parametros_login = [
             'user_id',
             'session_stringvalue',
             'user_hash',
             'paymentMethods',

        ]
        resultados_login={}

# Construyendo la URL con los parámetros
        url_login = base_url_login + '?' + '&'.join([f'{key}={value}' for key, value in params.items()])
        #print(url_login)
        
        if usuario:
            response = requests.get(url_login)
            data_login = response.json()
            #print(data_login)
            for k,v in data_login['response'].items():
                
                if k in parametros_login:
                    resultados_login.update({k:v})

            return resultados_login
        else:
            return("parametros invalidos")
    except Exception as e:
        print('error login')
    