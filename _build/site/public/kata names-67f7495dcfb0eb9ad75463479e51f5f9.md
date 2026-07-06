---
downloads: []
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Kata Names

```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
kata_names = ['Mae', 'Ushiro', 'Ukenagashi', 'Tsuka-ate', 'Kesagiri', 'Morotezuki', 'Sanpogiri', 'Ganmenate', 'Soetezuki', 'Shihogiri', 'Sougiri', 'Nukiuchi']
kata_names = [{'front': '1', 'back': 'Mae'}, {'front': '2', 'back': 'Ushiro'}, {'front': '3', 'back': 'Ukenagashi'}, {'front': '4', 'back': 'Tsuka-ate'}, {'front': '5', 'back': 'Kesagiri'}, {'front': '6', 'back': 'Morotezuki'}, {'front': '7', 'back': 'Sanpogiri'}, {'front': '8', 'back': 'Ganmenate'}, {'front': '9', 'back': 'Soetezuki'}, {'front': '10', 'back': 'Shihogiri'}, {'front': '11', 'back': 'Sougiri'}, {'front': '12', 'back': 'Nukiuchi'}]
kata = []
for a in kata_names:
    kata.append(a['back'])
print(kata)
display_flashcards(split_points, shuffle_cards=True)

table = []
from tabulate import tabulate
for d in split_points:
    table.append([d[front]])

```
:::{dropdown} Flashcard Controls
On mobile, tap to flip the card over. Swipe left or tap Next to advance to the next card.  
On desktop, click or press the Spacebar to flip the card over. Tap Next or use the Right Arrow key to advance to the next card.
:::

```{code-cell} python
:tags: ["remove-input"]
from tabulate import tabulate

```
:::{dropdown} Cheat sheet
| Name  |   Age |
|-------|-------|
| Alice |    24 |
| Bob   |    30 |
:::