from zeep import Client
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken
import time

import json

password = input("Please enter WebServices Authorization Code: ")
for x in range(1, 72):
    url = "https://www.beautyparkanadolu.com/Servis/UrunServis.svc?wsdl"
    client = Client(url)
    response = client.service.SelectKategori(password,x)

    print(f"response: {x}", response)
    time.sleep(8)
#Result of 1
"""Forcing soap:address location to HTTPS
response:  [{
    'Aktif': True,
    'ID': 1,
    'Icerik': None,
    'KategoriMenuGoster': True,
    'Kod': None,
    'PID': 0,
    'SeoAnahtarKelime': 'CİHAZLAR ',
    'SeoSayfaAciklama': 'CİHAZLAR CİHAZLAR Protez Tırnak ve Cilt Bakım Ekipmanları',
    'SeoSayfaBaslik': ' CİHAZLAR CİHAZLAR',
    'Sira': 1,
    'Tanim': 'CİHAZLAR',
    'Url': '/cihazlar'
}]"""