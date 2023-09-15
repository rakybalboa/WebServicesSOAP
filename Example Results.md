#1 "SelectKategori" Service Call Code
for x in range(1, 72):
    url = "https://www.beautyparkanadolu.com/Servis/UrunServis.svc?wsdl"
    client = Client(url)
    response = client.service.SelectKategori(password,x)

    print(f"response: {x}", response)
    time.sleep(8)
#1 Example result of "SelectKategori" Service Call

Forcing soap:address location to HTTPS
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
}]

/////////////////////////////////////////////////////////////////////////

#2 Service Call Code
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


#2 Example of "SelectUrun" service call

Forcing soap:address location to HTTPS
response:  [{
    'Aciklama': '<h2 style="text-align: center;"><strong>ELİXİR ANTİ AKNE SERUMU - 10 ML</strong></h2>\n',
    'AdwordsAciklama': None,
    'AdwordsKategori': '567',
    'AdwordsTip': 'Cilt Bakımı',
    'Aktif': True,
    'AnaKategori': 'Cilt Bakım Seti',
    'AnaKategoriID': 14,
    'AramaAnahtarKelime': None,
    'AsortiGrupID': 0,
    'DuzenleyenKullanici': 0,
    'EklemeTarihi': datetime.datetime(2022, 1, 7, 18, 11, 1),
    'EkleyenKullanici': 0,
    'EntegrasyonID': '0',
    'Etiketler': None,
    'FBStoreGoster': True,
    'FirsatUrunu': False,
    'HediyeIpucu': False,
    'ID': 54,
    'IlgiliUrunResim': None,
    'IndirimliFiyatOzellik': 0,
    'IndirimliFiyatOzellikStok1': 0,
    'IndirimliFiyatOzellikStok2': 0,
    'IndirimliFiyatOzellikTarih1': datetime.datetime(2022, 12, 13, 23, 36, 44),
    'IndirimliFiyatOzellikTarih2': datetime.datetime(2022, 12, 14, 23, 36, 44),
    'Kapasite': 0.0,
    'KargoTipi': 0,
    'Kategoriler': {
        'int': [
            12,
            14
        ]
    },
    'ListedeGoster': True,
    'MaksTaksitSayisi': 1,
    'Marka': 'Elixir',
    'MarkaID': 8,
    'MarketPlaceAktif': True,
    'MarketPlaceAktif2': True,
    'MarketPlaceAktif3': True,
    'MarketPlaceAktif4': True,
    'MarketPlaceAktif5': False,
    'MarketPlaceGrup1Ayar': {
        'Aktif': True,
        'EksiStokAdedi': 0.0,
        'GrupAdi': 'Market Place Grup 1',
        'KomisyonDeger': 0.0,
        'KomisyonTip': 1
    },
    'MarketPlaceGrup2Ayar': {
        'Aktif': True,
        'EksiStokAdedi': 0.0,
        'GrupAdi': 'Market Place Grup 2',
        'KomisyonDeger': 0.0,
        'KomisyonTip': 1
    },
    'MarketPlaceGrup3Ayar': {
        'Aktif': True,
        'EksiStokAdedi': 0.0,
        'GrupAdi': 'Market Place Grup 3',
        'KomisyonDeger': 0.0,
        'KomisyonTip': 1
    },
    'MarketPlaceGrup4Ayar': {
        'Aktif': True,
        'EksiStokAdedi': 0.0,
        'GrupAdi': 'Market Place Grup 4',
        'KomisyonDeger': 0.0,
        'KomisyonTip': 1
    },
    'MarketPlaceGrup5Ayar': {
        'Aktif': False,
        'EksiStokAdedi': 0.0,
        'GrupAdi': 'Market Place Grup 5',
        'KomisyonDeger': 0.0,
        'KomisyonTip': 1
    },
    'MenseiUlke': {
        'Alpha2Code': None,
        'Alpha3Code': None,
        'ID': 0,
        'NumericCode': None,
        'Tanim': None
    },
    'OnYazi': None,
    'OzelAlan1': None,
    'OzelAlan2': None,
    'OzelAlan3': None,
    'OzelAlan4': None,
    'OzelAlan5': None,
    'PuanDeger': 0,
    'Resimler': {
        'string': [
            'https://static.ticimax.cloud/48957/Uploads/UrunResimleri/buyuk/elixir-anti-akne-serumu-10-ml-5-573e.jpg',
            'https://static.ticimax.cloud/48957/Uploads/UrunResimleri/buyuk/elixir-anti-akne-serumu-10-ml-ff5f-4.jpg'
        ]
    },
    'SatisBirimi': None,
    'SeoAnahtarKelime': None,
    'SeoNoFollow': False,
    'SeoNoIndex': False,
    'SeoSayfaAciklama': None,
    'SeoSayfaBaslik': None,
    'Sira': 999,
    'TahminiTeslimSuresi': 3,
    'TahminiTeslimSuresiAyniGun': False,
    'TahminiTeslimSuresiGoster': True,
    'TahminiTeslimSuresiTarih': datetime.datetime(2022, 1, 7, 18, 11, 1),
    'TakimKampanyaId': 0,
    'TakimUrun': False,
    'TedarikciID': 1,
    'TedarikciKodu': 'EXCEL|54-54',
    'TedarikciKodu2': None,
    'TedarikciKomisyonOrani': 0.0,
    'TeknikDetayGrupID': 0,
    'TeknikDetaylar': None,
    'ToplamStokAdedi': 4.0,
    'TumVaryasyonlarStokDusur': False,
    'UcretsizKargo': False,
    'UrunAdediKademeDeger': 0.0,
    'UrunAdediMinimumDeger': 0.0,
    'UrunAdediOndalikliSayiGirilebilir': False,
    'UrunAdediVarsayilanDeger': 0.0,
    'UrunAdi': 'ELİXİR ANTİ AKNE SERUMU - 10 ML',
    'UrunKapidaOdemeYasakli': False,
    'UrunSayfaAdresi': '/elixir-anti-akne-serumu-10-ml',
    'UyeAlimMax': 999999.0,
    'UyeAlimMin': 1.0,
    'Varyasyonlar': {
        'Varyasyon': [
            {
                'Aktif': True,
                'AlisFiyati': 199.89996000000002,
                'Barkod': 'EAA-02',
                'Barkodlar': None,
                'Desi': 0.0,
                'Desi2': 0.0,
                'DuzenleyenKullanici': 0,
                'EkleyenKullanici': 0,
                'EksiStokAdedi': 0.0,
                'GtipKodu': None,
                'ID': 54,
                'IndirimliFiyati': 119.9,
                'IndirimliFiyati1': 0.0,
                'IndirimliFiyati10': 0.0,
                'IndirimliFiyati11': 0.0,
                'IndirimliFiyati12': 0.0,
                'IndirimliFiyati13': 0.0,
                'IndirimliFiyati14': 0.0,
                'IndirimliFiyati15': 0.0,
                'IndirimliFiyati16': 0.0,
                'IndirimliFiyati17': 0.0,
                'IndirimliFiyati18': 0.0,
                'IndirimliFiyati19': 0.0,
                'IndirimliFiyati2': 0.0,
                'IndirimliFiyati20': 0.0,
                'IndirimliFiyati3': 0.0,
                'IndirimliFiyati4': 0.0,
                'IndirimliFiyati5': 0.0,
                'IndirimliFiyati6': 0.0,
                'IndirimliFiyati7': 0.0,
                'IndirimliFiyati8': 0.0,
                'IndirimliFiyati9': 0.0,
                'IscilikAgirlik': 0,
                'IscilikParaBirimi': 'TL',
                'IscilikParaBirimiId': 1,
                'IscilikParaBirimiKodu': 'TRY',
                'KargoUcreti': 0.0,
                'Kategoriler': {
                    'int': []
                },
                'KdvDahil': True,
                'KdvDahil1': False,
                'KdvDahil10': False,
                'KdvDahil11': False,
                'KdvDahil12': False,
                'KdvDahil13': False,
                'KdvDahil14': False,
                'KdvDahil15': False,
                'KdvDahil16': False,
                'KdvDahil17': False,
                'KdvDahil18': False,
                'KdvDahil19': False,
                'KdvDahil2': False,
                'KdvDahil20': False,
                'KdvDahil3': False,
                'KdvDahil4': False,
                'KdvDahil5': False,
                'KdvDahil6': False,
                'KdvDahil7': False,
                'KdvDahil8': False,
                'KdvDahil9': False,
                'KdvOrani': 20.0,
                'KdvOrani1': 0.0,
                'KdvOrani10': 0.0,
                'KdvOrani11': 0.0,
                'KdvOrani12': 0.0,
                'KdvOrani13': 0.0,
                'KdvOrani14': 0.0,
                'KdvOrani15': 0.0,
                'KdvOrani16': 0.0,
                'KdvOrani17': 0.0,
                'KdvOrani18': 0.0,
                'KdvOrani19': 0.0,
                'KdvOrani2': 0.0,
                'KdvOrani20': 0.0,
                'KdvOrani3': 0.0,
                'KdvOrani4': 0.0,
                'KdvOrani5': 0.0,
                'KdvOrani6': 0.0,
                'KdvOrani7': 0.0,
                'KdvOrani8': 0.0,
                'KdvOrani9': 0.0,
                'MarkaID': 0,
                'MarketPlaceAktif': True,
                'MarketPlaceAktif2': True,
                'MarketPlaceAktif3': True,
                'MarketPlaceAktif4': True,
                'MarketPlaceAktif5': False,
                'MarketPlaceGrup1Ayar': {
                    'Aktif': True,
                    'EksiStokAdedi': 0.0,
                    'GrupAdi': 'Market Place Grup 1',
                    'KomisyonDeger': 0.0,
                    'KomisyonTip': 1
                },
                'MarketPlaceGrup2Ayar': {
                    'Aktif': True,
                    'EksiStokAdedi': 0.0,
                    'GrupAdi': 'Market Place Grup 2',
                    'KomisyonDeger': 0.0,
                    'KomisyonTip': 1
                },
                'MarketPlaceGrup3Ayar': {
                    'Aktif': True,
                    'EksiStokAdedi': 0.0,
                    'GrupAdi': 'Market Place Grup 3',
                    'KomisyonDeger': 0.0,
                    'KomisyonTip': 1
                },
                'MarketPlaceGrup4Ayar': {
                    'Aktif': True,
                    'EksiStokAdedi': 0.0,
                    'GrupAdi': 'Market Place Grup 4',
                    'KomisyonDeger': 0.0,
                    'KomisyonTip': 1
                },
                'MarketPlaceGrup5Ayar': {
                    'Aktif': False,
                    'EksiStokAdedi': 0.0,
                    'GrupAdi': 'Market Place Grup 5',
                    'KomisyonDeger': 0.0,
                    'KomisyonTip': 1
                },
                'Ozellikler': None,
                'ParaBirimi': 'TL',
                'ParaBirimi10Id': 0,
                'ParaBirimi11Id': 0,
                'ParaBirimi12Id': 0,
                'ParaBirimi13Id': 0,
                'ParaBirimi14Id': 0,
                'ParaBirimi15Id': 0,
                'ParaBirimi16Id': 0,
                'ParaBirimi17Id': 0,
                'ParaBirimi18Id': 0,
                'ParaBirimi19Id': 0,
                'ParaBirimi1Id': 0,
                'ParaBirimi20Id': 0,
                'ParaBirimi2Id': 0,
                'ParaBirimi3Id': 0,
                'ParaBirimi4Id': 0,
                'ParaBirimi5Id': 0,
                'ParaBirimi6Id': 0,
                'ParaBirimi7Id': 0,
                'ParaBirimi8Id': 0,
                'ParaBirimi9Id': 0,
                'ParaBirimiID': 1,
                'ParaBirimiKodu': 'TRY',
                'Resimler': None,
                'SatisFiyati': 199.89996000000002,
                'SatisFiyati1': 0.0,
                'SatisFiyati10': 0.0,
                'SatisFiyati11': 0.0,
                'SatisFiyati12': 0.0,
                'SatisFiyati13': 0.0,
                'SatisFiyati14': 0.0,
                'SatisFiyati15': 0.0,
                'SatisFiyati16': 0.0,
                'SatisFiyati17': 0.0,
                'SatisFiyati18': 0.0,
                'SatisFiyati19': 0.0,
                'SatisFiyati2': 0.0,
                'SatisFiyati20': 0.0,
                'SatisFiyati3': 0.0,
                'SatisFiyati4': 0.0,
                'SatisFiyati5': 0.0,
                'SatisFiyati6': 0.0,
                'SatisFiyati7': 0.0,
                'SatisFiyati8': 0.0,
                'SatisFiyati9': 0.0,
                'StokAdedi': 4.0,
                'StokGuncellemeTarihi': datetime.datetime(2000, 1, 1, 0, 0),
                'StokKodu': 'ELİXİR-ANTİ-AKNE-10-ML',
                'TahminiTeslimSuresi': 3,
                'TahminiTeslimSuresiAyniGun': False,
                'TahminiTeslimSuresiGoster': True,
                'TahminiTeslimSuresiTarih': datetime.datetime(2022, 1, 7, 18, 11, 1),
                'TedarikciKodu': 'EXCEL|ELİXİR-ANTİ-AKNE-10-ML',
                'TedarikciKodu2': None,
                'TedarikciKomisyonOrani': 0.0,
                'UpdateKey': None,
                'UrunAgirligi': 0.0,
                'UrunBarkodlar': None,
                'UrunDerinlik': 0.0,
                'UrunGenislik': 0.0,
                'UrunKartiAktif': False,
                'UrunKartiID': 54,
                'UrunYukseklik': 0.0,
                'UyeAlimMax': 0.0,
                'UyeAlimMin': 0.0,
                'UyeTipiFiyat1': 139.89996,
                'UyeTipiFiyat10': 0.0,
                'UyeTipiFiyat11': 0.0,
                'UyeTipiFiyat12': 0.0,
                'UyeTipiFiyat13': 0.0,
                'UyeTipiFiyat14': 0.0,
                'UyeTipiFiyat15': 0.0,
                'UyeTipiFiyat16': 0.0,
                'UyeTipiFiyat17': 0.0,
                'UyeTipiFiyat18': 0.0,
                'UyeTipiFiyat19': 0.0,
                'UyeTipiFiyat2': 139.89996,
                'UyeTipiFiyat20': 0.0,
                'UyeTipiFiyat3': 139.89996,
                'UyeTipiFiyat4': 139.89996,
                'UyeTipiFiyat5': 139.89996,
                'UyeTipiFiyat6': 139.89996,
                'UyeTipiFiyat7': 139.89996,
                'UyeTipiFiyat8': 139.89996,
                'UyeTipiFiyat9': 139.89996
            }
        ]
    },
    'Vitrin': False,
    'YayinTarihi': datetime.datetime(2022, 1, 9, 0, 54, 52),
    'YeniUrun': False,
    'YonlendirmeAdresi': None
}]


#1 Service Call
"""for x in range(1, 72):
    url = "https://www.beautyparkanadolu.com/Servis/UrunServis.svc?wsdl"
    client = Client(url)
    response = client.service.SelectKategori(password,x)

    print(f"response: {x}", response)
    time.sleep(8)"""
#1 Result of first request
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