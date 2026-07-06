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
kata = ['Mae', 'Ushiro', 'Ukenagashi', 'Tsuka-ate', 'Kesagiri', 'Morotezuki', 'Sanpogiri', 'Ganmenate', 'Soetezuki', 'Shihogiri', 'Sougiri', 'Nukiuchi']

flashcards = []
table = []
for i, k in enumerate('kata')
    flashcards.append(i+1, k)
    flashcards.append(k, i+1)
    table.append(i+1, k)
display_flashcards(flashcards, shuffle_cards=True)


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