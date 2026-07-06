---
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Points for Grading & Refereeing


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
        for line in d['back']
display_flashcards(data, shuffle_cards=True)

```


