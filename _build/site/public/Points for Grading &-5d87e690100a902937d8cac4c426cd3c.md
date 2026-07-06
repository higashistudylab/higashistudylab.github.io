---
downloads: [iaido_points.csv]
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Points for Grading & Refereeing

:::{dropdown} Ordered
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "iaido_points.csv"
split_points = []
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
    for d in data:
        #d['back'] = d['back'].replace('\n', '<br>')
        for i, line in enumerate(d['back'].split('\n')):
            split_points.append({'front':d['front'].split()[1].capitalize()+f" | Point {i+1}", 'back':line[3:]})
display_flashcards(split_points, shuffle_cards=False)
```
:::

:::{dropdown} Shuffled
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "iaido_points.csv"
split_points = []
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
    for d in data:
        #d['back'] = d['back'].replace('\n', '<br>')
        for i, line in enumerate(d['back'].split('\n')):
            split_points.append({'front':d['front'].split()[1].capitalize()+f" | Point {i+1}", 'back':line[3:]})
display_flashcards(split_points, shuffle_cards=True)

```
:::