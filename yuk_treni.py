from dakikadan_zaman_damgasi import zam_dam

YT_route = {'G': 0, 'H': 77, 'I': 159, 'F': 209, 'J': 306, 'K': 406, 'L': 518}
YT_route_rev = {'L': 0, 'K': 112, 'J': 212, 'F': 309, 'I': 359, 'H': 441, 'G': 518}
YT_distances = {'G': 77, 'H': 82, 'I': 50, 'F': 97, 'J': 100, 'K': 112, 'L':0}
YT_distances_rev = {'L': 112, 'K': 100, 'J': 97, 'F': 50, 'I': 82, 'H': 77, 'G': 0}


def YTcikart(YT_max_hiz, sefer_suresi, gecikme, tren, durak_suresi, genel_bakimKM, genel_bakim, sefer_bakim):
    gecen_sure = 0 + gecikme
    gidilenKM = 0
    sefer = 0
    genel_bakim_dk = genel_bakim*60
    sefer_bakim_dk = sefer_bakim*60
    while gecen_sure <= sefer_suresi:
        if gidilenKM <= genel_bakimKM:
            if ((sefer)%2) == 1:
                sefer += 1 
                print("Tren: " + tren + " G-L Güzergahı")
                print("Gün " + str((gecen_sure//1440)+1) + " - " + "Sefer " + str(sefer))
                for key in YT_route:
                    if YT_route[key] != 0:
                        print(key, YT_route[key], YT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure + durak_suresi), durak_suresi)
                        gecen_sure += durak_suresi + (YT_distances[key]/YT_max_hiz)*60
                    else:
                        print(key, YT_route[key], YT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure), durak_suresi)
                sefer += 1    
            elif ((sefer)%2) == 0:
                sefer += 1 
                print("Tren: " + tren + " L-G Güzergahı")
                print("Gün " + str((gecen_sure//1440)+1) + " - " + "Sefer " + str(sefer))
                for key in YT_route_rev:
                    if YT_route_rev[key] != 0:
                        print(key, YT_route_rev[key], YT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure + durak_suresi), durak_suresi)
                        gecen_sure += durak_suresi + (YT_distances_rev[key]/YT_max_hiz)*60
                    else:
                        print(key, YT_route_rev[key], YT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure), durak_suresi)
                sefer += 1
            print("Sefer bakımı zamanı, " + str(sefer_bakim_dk/60) + " saat bekleme")
            gecen_sure += sefer_bakim_dk
            gidilenKM += 450 #YT_distances[key]
            print("Gidilen KM: " + str(gidilenKM))  
            print("\n")  

        elif gidilenKM > genel_bakimKM:
            print(tren + " Genel bakım zamanı, " + str(genel_bakim_dk/60) + " saat bekleme")
            print("\n")
            gecen_sure += genel_bakim_dk
            gidilenKM = 0
    return sefer