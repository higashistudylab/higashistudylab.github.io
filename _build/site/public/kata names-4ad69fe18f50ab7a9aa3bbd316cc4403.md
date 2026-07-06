---
downloads: []
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Kata Names



::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]

from jupytercards import display_flashcards
kata = ['Tsukizue', 'Suigetsu', 'Hissage', 'Shamen', 'Sakan', 'Monomi', 'Kasumi', 'Tachiotoshi', 'Raiuchi', 'Seigan', 'Midaredome', 'Ranai']

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
kata = ['Tsukizue', 'Suigetsu', 'Hissage', 'Shamen', 'Sakan', 'Monomi', 'Kasumi', 'Tachiotoshi', 'Raiuchi', 'Seigan', 'Midaredome', 'Ranai']

flashcards = []
for i, k in enumerate(kata):
    flashcards.append({"front":k, "back":str(i+1)})
    flashcards.append({"front":str(i+1), "back":k})
    
display_flashcards(flashcards, shuffle_cards=False)

```
:::
::::