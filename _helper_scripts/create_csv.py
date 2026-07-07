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

numbers_r = """1 - ichi (いち)
2 - ni (に)
3 - san (さん)
4 - shi (し) <br> yon (よん)
5 - go (ご)
6 - roku (ろく)
7 - shichi (しち) <br> nana (なな)
8 - hachi (はち)
9 - kyu (きゅう)
10 - ju (じゅう)
11 - ju-ichi (じゅういち)
12 - ju-ni (じゅうに)
13 - ju-san (じゅうさん)
14 - ju-shi (じゅうし) <br> ju-yon (じゅうよん)
15 - ju-go (じゅうご)
16 - ju-roku (じゅうろく)
17 - ju-shichi (じゅう <br> ju-nana (じゅうなな)
18 - ju-hachi (じゅうはち)
19 - ju-kyu (じゅうきゅう)
20 - ni-ju (にじゅう)
100 - hyaku (ひゃく)"""

to_csv(numbers_r, 'numbers_reading.csv')

numbers_k = """1 - 一
2 - 二
3 - 三
4 - 四
5 - 五
6 - 六
7 - 七
8 - 八
9 - 九
10 - 十
11 - 十一
12 - 十二
13 - 十三
14 - 十四
15 - 十五
16 - 十六
17 - 十七
18 - 十八
19 - 十九
20 - 二十
100 - 百"""

to_csv(numbers_k, 'numbers_kanji.csv')