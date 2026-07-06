import csv

def to_csv(data, name):
    print(name)
    rows = [["front", "back"]]
    for i, k in enumerate(data.split('\n')):
        rows.append(k.split(" - "))
        print(F"{i+1}. {k}")
    with open(name, "w", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(rows)


to_csv("""Tsukizue - Walking stick
Suigetsu - Solar plexus
Hissage - Carry in the hands
Shamen - Slope
Sakan - Left thrust
Monomi - Look out
Kasumi - Mist
Tachiotoshi - Drop the sword
Raiuchi - Thunderstrike
Seigan - Straight to the eyes
Midaredome - Preventing chaos
Ranai - From disorder to harmony""", "jodo_kata_desc.csv")

to_csv("""Mae - Front
Ushiro - Rear
Ukenagashi - Deflection
Tsukaate - Handle strike
Kesagiri - Diagonal cut
Morotezuki - Two-handed thrust
Sanpogiri - Three-way cut
Ganmenate - Face strike
Soetezuki - Joined-hand thrust
Shihogiri - Four-way cut
Sogiri - Complete cutting
Nukiuchi - Sudden draw""", "iaido_kata_desc.csv")