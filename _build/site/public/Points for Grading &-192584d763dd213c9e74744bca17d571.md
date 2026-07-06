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
print(file)
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
display_flashcards(data, shuffle_cards=True)
```