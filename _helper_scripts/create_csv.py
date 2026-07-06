import csv

def to_csv(data, name):
    print(name)
    rows = [["front", "back"]]
    print(":::{dropdown} Answer Overview")
    for i, k in enumerate(data.split('\n')):
        rows.append(k.split(" - "))
        print(F"{i+1}. {k}")
    print(":::\n")
    with open(name, "w", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(rows)

def to_csv2(data, data2, name):
    print(name)
    rows = [["front", "back"]]
    print(":::{dropdown} Answer Overview")
    for i, (k, o) in enumerate(zip(data.split('\n'), data2.split('\n'))):
        rows.append([o.split(" - ")[0], k.split(" - ")[0]])
        print(F"{i+1}.", o.split(" - ")[0],'-', k.split(" - ")[0])
    print(":::\n")
    with open(name, "w", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(rows)

jodo_kata = """Tsukizue - Walking stick
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
Ranai - From disorder to harmony"""

to_csv(jodo_kata, "jodo_kata_desc.csv")

iaido_kata = """Mae - Front
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
Nukiuchi - Sudden draw"""

to_csv(iaido_kata, "iaido_kata_desc.csv")

ordinal = """Ipponme - First
Nihonme - Second
Sanbonme - Third
Yonhonme - Fourth
Gohonme - Fifth
Ropponme - Sixth
Nanahonme - Seventh
Happonme - Eighth
Kyuhonme - Ninth
Jupponme - Tenth
Juipponme - Eleventh
Junihonme - Twelfth"""

to_csv(ordinal, 'ordinal_numbers.csv')

to_csv2(iaido_kata, ordinal, 'iaido_kata_ordinal.csv')


to_csv2(jodo_kata, ordinal, 'jodo_kata_ordinal.csv')