from math import floor

def zam_dam(dakikalar):
    dakika = floor(dakikalar%1440)
    toplam_saat = dakika // 60
    toplam_dakika = "%02d"%(dakika%60)
    zaman_damgası = "{}:{}".format(toplam_saat, toplam_dakika)
    return zaman_damgası