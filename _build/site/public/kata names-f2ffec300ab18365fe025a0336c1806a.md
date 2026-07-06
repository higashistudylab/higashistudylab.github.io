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

## Name - Meaning

These flashcards are based on the translations found on the [Ryoshinkan website](https://www.ryoshinkan.org/more-detail/iaido-curriculum), which also includes further explanations of the kata naming, which is interesting and aids in memorization so reading it is recommended.

::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]
import csv

file = "jodo_kata_desc.csv"
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
display_flashcards(data, shuffle_cards=True)
```
:::
:::{tab-item} Ordered
```{code-cell} python
:tags: ["remove-input"]
import csv

file = "jodo_kata_desc.csv"
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
display_flashcards(data, shuffle_cards=False)
```
:::
::::