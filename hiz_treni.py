from dakikadan_zaman_damgasi import zam_dam

HT_route = {'A': 0, 'B': 100, 'C': 175, 'D': 275, 'E': 350, 'F': 425, 'O': 450}
HT_route_rev = {'O': 0, 'F': 25, 'E': 100, 'D': 175, 'C': 275, 'B': 350, 'A': 450}
HT_distances = {'A': 100, 'B': 75, 'C': 100, 'D': 75, 'E': 75, 'F': 25, 'O': 0}
HT_distances_rev = {'O': 25, 'F': 75, 'E': 75, 'D': 100, 'C': 75, 'B': 100, 'A': 0}

HT_max_hiz = 200

def HTcikart(HT_max_hiz, sefer_suresi, gecikme, tren, durak_suresi, genel_bakimKM, genel_bakim, sefer_bakim):
    gecen_sure = 0 + gecikme
    gidilenKM = 0
    sefer = 0
    genel_bakim_dk = genel_bakim*60
    sefer_bakim_dk = sefer_bakim*60
    while gecen_sure <= sefer_suresi:
        if gidilenKM <= genel_bakimKM:
            if ((sefer)%2) == 1:
                sefer += 1 
                print("Tren: " + tren + " A-O Guzergahi")
                print("Gun " + str((gecen_sure//1440)+1) + " - " + "Sefer " + str(sefer))
                for key in HT_route:
                    if HT_route[key] != 0:
                        print(key, HT_route[key], HT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure + durak_suresi), durak_suresi)
                        gecen_sure += durak_suresi + (HT_distances[key]/HT_max_hiz)*60
                    else:
                        print(key, HT_route[key], HT_max_hiz, gecen_sure, gecen_sure, durak_suresi)
                    gidilenKM += HT_distances[key]
            elif ((sefer)%2) == 0:
                sefer += 1 
                print("Tren: " + tren + " O-A Guzergahi")
                print("Gun " + str((gecen_sure//1440)+1) + " - " + "Sefer " + str(sefer))
                for key in HT_route_rev:
                    if HT_route_rev[key] != 0:
                        print(key, HT_route_rev[key], HT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure + durak_suresi), durak_suresi)
                        gecen_sure += durak_suresi + (HT_distances_rev[key]/HT_max_hiz)*60
                    else:
                        print(key, HT_route_rev[key], HT_max_hiz, gecen_sure, gecen_sure, durak_suresi)
                    gidilenKM += HT_distances[key]
            print("Sefer bakimi zamani, 2 saat bekleme")
            gecen_sure += sefer_bakim_dk
            print("Gidilen KM: " + str(gidilenKM))  
            print("\n")  

        elif gidilenKM > genel_bakimKM:
            print(tren + " Genel bakim zamani, 12 saat bekleme")
            print("\n")
            gecen_sure += genel_bakim_dk
            gidilenKM = 0
    return sefer

#HTcikart(10*1440, 15, "HT-01", 20, 6000, 12*60, 2*60) #(sefer_suresi, gecikme, tren, durak_suresi, genel_bakimKM, genel_bakim_dk, sefer_bakim_dk)