import json
import os
from os import path

def etiket_olustur(HTsayisi, YTsayisi, ATsayisi):
    TrainCount = 1
    trains = 'trains.json'

    if path.isfile(trains) is True:
        os.remove(trains)
        print("Eski trenler kaldırıldı!")

    if path.isfile(trains) is False:
        with open(trains, 'w') as f:
            json.dump([], f, indent=4)
            print("Yeni trenler oluşturuldu!")

    with open(trains, 'r+') as f:
        data = json.load(f)

        for i in range(HTsayisi):
            x = {
                "id": TrainCount,
                "type": "speed",
                "label": "HT-" + "%02d"%(i+1)
            }
            data.append(x)
            TrainCount += 1

        for i in range(YTsayisi):
            x = {
                "id": TrainCount,
                "type": "freight",
                "label": "YT-" + "%02d"%(i+1)
            }
            data.append(x)
            TrainCount += 1

        for i in range(ATsayisi):
            x = {
                "id": TrainCount,
                "type": "mainline",
                "label": "AH-" + "%02d"%(i+1)
            }
            data.append(x)
            TrainCount += 1
        f.seek(0)
        json.dump(data, f, indent=4)