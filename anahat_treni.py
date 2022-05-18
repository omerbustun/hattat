from dakikadan_zaman_damgasi import zam_dam

AT_route = {'A': 0, 'B': 100, 'C': 200, 'D': 275, 'E': 325, 'F': 375, 'O': 450}
AT_route_rev = {'O': 0, 'F': 75, 'E': 125, 'D': 175, 'C': 250, 'B': 350, 'A': 450}
AT_distances = {'A': 100, 'B': 100, 'C': 75, 'D': 50, 'E': 50, 'F': 75, 'O': 0}
AT_distances_rev = {'O': 25, 'F': 75, 'E': 75, 'D': 100, 'C': 75, 'B': 100, 'A': 0}

def ATcikart(AT_max_hiz, sefer_suresi, gecikme, tren, durak_suresi, genel_bakimKM, genel_bakim, sefer_bakim):
    gecen_sure = 0 + gecikme
    gidilenKM = 0
    sefer = 0
    genel_bakim_dk = genel_bakim*60
    sefer_bakim_dk = sefer_bakim*60
    while gecen_sure <= sefer_suresi:
        if gidilenKM <= genel_bakimKM:
            if ((sefer)%2) == 1:
                sefer += 1 
                print("Tren: " + tren + " N-P Güzergahı")
                print("Gün " + str((gecen_sure//1440)+1) + " - " + "Sefer " + str(sefer))
                for key in AT_route:
                    if AT_route[key] != 0:
                        print(zam_dam(gecen_sure))
                        print(key, AT_route[key], AT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure + durak_suresi), durak_suresi)
                        gecen_sure += durak_suresi + (AT_distances[key]/AT_max_hiz)*60
                    else:
                        print(key, AT_route[key], AT_max_hiz, zam_dam(gecen_sure), zam_dam(gecen_sure), durak_suresi)
                    gidilenKM += AT_distances[key]
                sefer += 1
                    
            elif ((sefer)%2) == 0:
                sefer += 1 
                print("Tren: " + tren + " P-N Güzergahı")
                print("Gün " + str((gecen_sure//1440)+1) + " - " + "Sefer " + str(sefer))
                for key in AT_route_rev:
                    if AT_route_rev[key] != 0:
                        print(key, AT_route_rev[key], AT_max_hiz, gecen_sure, (gecen_sure + durak_suresi), durak_suresi)
                        gecen_sure += durak_suresi + (AT_distances_rev[key]/AT_max_hiz)*60
                    else:
                        print(key, AT_route_rev[key], AT_max_hiz, gecen_sure, gecen_sure, durak_suresi)
                    gidilenKM += AT_distances[key]
                sefer += 1
            print("Sefer bakımı zamanı, " + str(sefer_bakim_dk/60) + " saat bekleme")
            gecen_sure += sefer_bakim_dk
            #gidilenKM += 450 #AT_distances[key]
            print("Gidilen KM: " + str(gidilenKM))  
            print("\n")  

        elif gidilenKM > genel_bakimKM:
            print(tren + " Genel bakım zamanı, " + str(genel_bakim_dk/60) + " saat bekleme")
            print("\n")
            gecen_sure += genel_bakim_dk
            gidilenKM = 0
    return sefer

#ATcikart(100, 10*1440, 15, "AT-01", 20, 2500, 24*60, 4*60)