---
downloads: []
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Jodo Kihon

::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards

from jupytercards import display_flashcards
kihon = ['Honteuchi', 'Gyakuteuchi', 'Hikiotoshiuchi', 'Kaeshizuki', 'Gyakutezuki', 'Makiotoshi', 'Kuritsuke', 'Kurihanashi', 'Taiatari', 'Tsukihazushiuchi', 'Dobaraiuchi', 'Taihazushiuchi']

flashcards = []
for i, k in enumerate(kihon):
    flashcards.append({"front":k, "back":str(i+1)})
    flashcards.append({"front":str(i+1), "back":k})
    
display_flashcards(flashcards, shuffle_cards=True)

```
:::
:::{tab-item} Ordered
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
kihon = ['Honteuchi', 'Gyakuteuchi', 'Hikiotoshiuchi', 'Kaeshizuki', 'Gyakutezuki', 'Makiotoshi', 'Kuritsuke', 'Kurihanashi', 'Taiatari', 'Tsukihazushiuchi', 'Dobaraiuchi', 'Taihazushiuchi']

flashcards = []
for i, k in enumerate(kihon):
    #print(F"{i+1}. **{k}**")
    flashcards.append({"front":k, "back":str(i+1)})
    flashcards.append({"front":str(i+1), "back":k})

display_flashcards(flashcards, shuffle_cards=False)

```
:::
::::

:::{dropdown} Answer Overview
1. **Honteuchi**
2. **Gyakuteuchi**
3. **Hikiotoshiuchi**
4. **Kaeshizuki**
5. **Gyakutezuki**
6. **Makiotoshi**
7. **Kuritsuke**
8. **Kurihanashi**
9. **Taiatari**
10. **Tsukihazushiuchi**
11. **Dobaraiuchi**
12. **Taihazushiuchi**
:::


Ipponme - First
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
Junihonme - Twelfth