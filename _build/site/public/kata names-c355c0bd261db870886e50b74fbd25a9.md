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
    flashcards.append({"front":k, "back":str(i+1)})
    flashcards.append({"front":str(i+1), "back":k})
    
display_flashcards(flashcards, shuffle_cards=True)


```


<!-- :::{dropdown} Flashcard Controls
On mobile, tap to flip the card over. Swipe left or tap Next to advance to the next card.  
On desktop, click or press the Spacebar to flip the card over. Tap Next or use the Right Arrow key to advance to the next card.
::: -->