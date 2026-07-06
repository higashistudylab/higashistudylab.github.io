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

with open("iaido_points.csv", newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))

print(data)
display_flashcards('example.json', shuffle_cards=True)
```