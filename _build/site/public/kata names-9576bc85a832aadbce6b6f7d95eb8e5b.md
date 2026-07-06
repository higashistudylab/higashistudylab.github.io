---
downloads: []
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Iaido Kata

## Name - Number
::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
kata = ['Mae', 'Ushiro', 'Ukenagashi', 'Tsuka-ate', 'Kesagiri', 'Morotezuki', 'Sanpogiri', 'Ganmenate', 'Soetezuki', 'Shihogiri', 'Sougiri', 'Nukiuchi']

flashcards = []
for i, k in enumerate(kata):
    flashcards.append({"front":k, "back":str(i+1)})
    flashcards.append({"front":str(i+1), "back":k})
    
display_flashcards(flashcards, shuffle_cards=True)

```
:::
:::{tab-item} Ordered
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
kata = ['Mae', 'Ushiro', 'Ukenagashi', 'Tsuka-ate', 'Kesagiri', 'Morotezuki', 'Sanpogiri', 'Ganmenate', 'Soetezuki', 'Shihogiri', 'Sougiri', 'Nukiuchi']

flashcards = []
for i, k in enumerate(kata):
    flashcards.append({"front":k, "back":str(i+1)})
    flashcards.append({"front":str(i+1), "back":k})
    
display_flashcards(flashcards, shuffle_cards=False)

```
:::
::::

:::{dropdown} Answer Overview
1. **Mae**
2. **Ushiro**
3. **Ukenagashi**
4. **Tsuka-ate**
5. **Kesagiri**
6. **Morotezuki**
7. **Sanpogiri**
8. **Ganmenate**
9. **Soetezuki**
10. **Shihogiri**
11. **Sougiri**
12. **Nukiuchi**
:::

---

## Name - Ordinal number
Japanese ordinal numbers such as `Ipponme` and `Nihonme` are often prepended to names or used to directly refer to Kata or Kihon within a set. 
You can find a set to practice the literal meaning e.g. `Gohonme` -> `Fifth` [Here](numbers).

::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "iaido_kata_ordinal.csv"
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
result = []
for d in data:
    result.append(d)
    result.append({'front': d['back'], 'back': d['front']})
data = result
display_flashcards(data, shuffle_cards=False)
```
:::
:::{tab-item} Ordered
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "iaido_kata_ordinal.csv"
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
display_flashcards(data, shuffle_cards=False)
```
:::
::::

:::{dropdown} Answer Overview
1. Ipponme - Mae
2. Nihonme - Ushiro
3. Sanbonme - Ukenagashi
4. Yonhonme - Tsukaate
5. Gohonme - Kesagiri
6. Ropponme - Morotezuki
7. Nanahonme - Sanpogiri
8. Happonme - Ganmenate
9. Kyuhonme - Soetezuki
10. Jupponme - Shihogiri
11. Juipponme - Sogiri
12. Junihonme - Nukiuchi
:::

---

## Name - Meaning

These flashcards are based on the translations found on the [Ryoshinkan website](https://www.ryoshinkan.org/more-detail/iaido-curriculum), which also includes further explanations of the kata naming, which is interesting and aids in memorization so reading it is highly recommended.

::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "iaido_kata_desc.csv"
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
result = []
for d in data:
    result.append(d)
    result.append({'front': d['back'], 'back': d['front']})
data = result
display_flashcards(data, shuffle_cards=False)
```
:::
:::{tab-item} Ordered
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "iaido_kata_desc.csv"
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
display_flashcards(data, shuffle_cards=False)
```
:::
::::

:::{dropdown} Answer Overview
1. Mae - Front
2. Ushiro - Rear
3. Ukenagashi - Deflection
4. Tsukaate - Handle strike
5. Kesagiri - Diagonal cut
6. Morotezuki - Two-handed thrust
7. Sanpogiri - Three-way cut
8. Ganmenate - Face strike
9. Soetezuki - Joined-hand thrust
10. Shihogiri - Four-way cut
11. Sogiri - Complete cutting
12. Nukiuchi - Sudden draw
:::