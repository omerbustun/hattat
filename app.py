from etiket_olustur import etiket_olustur
from hiz_treni import HTcikart
from yuk_treni import YTcikart
from anahat_treni import ATcikart
import json

# Çıkartma fonksiyonlarının parametreleri: sefer_suresi, gecikme(dk), tren, durak_suresi(dk), genel_bakimKM, genel_bakim(saat), sefer_bakim(saat)

HTsayisi = int(input("Kaç adet hız treni var? "))
YTsayisi = int(input("Kaç adet yük treni var? "))
ATsayisi = int(input("Kaç adet anahat treni var? "))

SeferGunu = int(input("Kaç gün için sefer planlanacak? " ))
sefer_suresi = SeferGunu*1440

# Parametreler

HT_gecikme = 15 # DK cinsinden
HT_durak_suresi = 20 # DK cinsinden
HT_genel_bakimKM = 6000 # KM cinsinden
HT_genel_bakim = 12 # saat
HT_sefer_bakim = 2 # saat
HT_hiz = 200 # km/saat
HT_kazanc = 60000

YT_gecikme = 15 # DK cinsinden
YT_durak_suresi = 20 # DK cinsinden
YT_genel_bakimKM = 3000 # KM cinsinden
YT_genel_bakim = 12 # saat
YT_sefer_bakim = 2 # saat
YT_hiz =75 # km/saat
YT_kazanc = 50000

AT_gecikme = 15 # DK cinsinden
AT_durak_suresi = 20 # DK cinsinden
AT_genel_bakimKM = 2500 # KM cinsinden
AT_genel_bakim = 12 # saat
AT_sefer_bakim = 2 # saat
AT_hiz = 100 # km/saat
AT_kazanc = 45000

etiket_olustur(HTsayisi, YTsayisi, ATsayisi)

trains = "trains.json"

with open(trains, 'r+') as f:
        data = json.load(f)

kazanc = 0

for i in data:
    if i['type'] == "speed":
        print(i['label'])
        sefer = HTcikart(HT_hiz, sefer_suresi, HT_gecikme, i['label'], HT_durak_suresi, HT_genel_bakimKM, HT_genel_bakim, HT_sefer_bakim)
        kazanc += sefer*HT_kazanc
    elif i['type'] == "freight":
        print(i['label'])
        sefer = YTcikart(YT_hiz, sefer_suresi, YT_gecikme, i['label'], YT_durak_suresi, YT_genel_bakimKM, YT_genel_bakim, YT_sefer_bakim)
        kazanc += sefer*YT_kazanc
    elif i['type'] == "mainline":
        print(i['label'])
        sefer = ATcikart(AT_hiz, sefer_suresi, AT_gecikme, i['label'], AT_durak_suresi, AT_genel_bakimKM, AT_genel_bakim, AT_sefer_bakim)
        kazanc += sefer*AT_kazanc

print("Toplam Kazanc: ", kazanc)