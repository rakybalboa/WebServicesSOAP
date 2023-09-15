from zeep import Client
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken
import time

import json

class UrunFiltre:
    def __init__(self, id):
        self.UrunKartiID = id


password = input("Please enter WebServices Authorization Code: ")

url = "https://www.beautyparkanadolu.com/Servis/UrunServis.svc?wsdl"
client = Client(url)
product_filter = {
    "Aktif":1, #When this line is acctive only, the first product with ID=8 is shown
    #"UrunKartiID": 0
    "Barkod": 'EAA-02' #This line doesn't work without when "Aktif" option isn't active
    #"ToplamStokAdediBas": 0,
    #"ToplamStokAdediSon": 0,
    #"TedarikciID": 0,
}
response = client.service.SelectUrun(password, product_filter,"")

print("response: ", response)