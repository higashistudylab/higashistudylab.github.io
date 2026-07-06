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
for i, k in enumerate(kata):
    flashcards.append({"front":k, "back":i+1})
    flashcards.append({"front":i+1, "back":k})
    
display_flashcards(flashcards, shuffle_cards=True)

table = []
for i, k in enumerate(kata):
    table.append([i+1, k])
from tabulate import tabulate
print(tabulate(table, headers=["nr", "Kata"], tablefmt="github"))

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
|   nr | Kata       |
|------|------------|
|    1 | Mae        |
|    2 | Ushiro     |
|    3 | Ukenagashi |
|    4 | Tsuka-ate  |
|    5 | Kesagiri   |
|    6 | Morotezuki |
|    7 | Sanpogiri  |
|    8 | Ganmenate  |
|    9 | Soetezuki  |
|   10 | Shihogiri  |
|   11 | Sougiri    |
|   12 | Nukiuchi   |
:::