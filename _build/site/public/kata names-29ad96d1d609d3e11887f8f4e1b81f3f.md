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
import csv

file = "iaido_points.csv"
split_points = []
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
    for d in data:
        split_points.append({'front':d['front'].split()[0][:-1], 'back':d['front'].split()[1].capitalize()})
        split_points.append({'back':d['front'].split()[0][:-1], 'front':d['front'].split()[1].capitalize()})
display_flashcards(split_points, shuffle_cards=True)
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