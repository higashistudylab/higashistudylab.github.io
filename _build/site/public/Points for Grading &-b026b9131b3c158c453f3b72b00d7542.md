---
downloads: []
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Points for Grading & Refereeing
::::{tab-set}

:::{tab-item} Shuffled
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
:::{tab-item} Ordered
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
::::

:::{dropdown} Answer Overview

**Mae**  
1. Does the performer do enough Sayabiki when they cut the opponent's face with Nukitsuke?  
2. Is the sword taken into Furikaburi with a feeling of thrusting to behind the left ear?  
3. Is the tip of the sword above the horizontal position when in Furikaburi?  
4. Is the sword brought down without hesitation during Kirioroshi?  
5. Is the tip of the sword slightly below horizontal at the end of Kirioroshi?  
6. Is the shape and form of Chiburi correct?  
7. Is Noto performed correctly?  
---
**Ushiro**  
1. When the turn is made, is the left foot moved sufficiently to the front left?  
2. Is the horizontal cut made to the opponent's temple?  
---
**Ukenagashi**  
1. When the parry is made, does it protect the upper body?  
2. Is the left foot brought back behind the right foot and the cut made along the Kesa line?  
3. After the cut has been made, is the left hand in front of the navel and the sword tip a little below horizontal?  
---
**Tsuka-ate**  
1. Is the Tsukagashira surely pointed at the opponent's solar plexus?   
2. When the rear opponent is thrust, is this done with the right elbow extended fully and does the left hand bring the Koiguchi to the navel?   
3. When the cut is made, is it on the vertical centerline and from the correct position above the head?  
---
**Kesagiri**  
1. When the initial upper cut is made, is the right hand above the right shoulder when the sword is rotated?  
2. When Chiburi is performed, is it at the correct angle while the person steps back with the left foot at the same time when their left hand takes hold of the Koiguchi?  
---
**Morotezuki**  
1. Is the initial cut correctly made from the opponent's upper head down to their chin when making Nuki Uchi?  
2. Does the performer bring their left foot up behind their right? Is Chudan No Kamae correctly made and the sword thrust into the correct target of the body? Is the thrust made with certainty?  
3. Does the performer bring their sword above their head in a parrying action when pulling it out from the first opponent?  
---
**Sanpogiri**  
1. Is the initial cut to the first opponent made through the correct diagonal angle from the top right side of the head down to the base of the chin?  
2. Is the cut to the opponent on the left performed without hesitation?  
3. Is the sword brought up to Furikaburi with a parrying action and does the last cut finish at the horizontal?  
---
**Ganmenate**  
1. Is the initial strike with the Tsukagashira made between the eyes?  
2. When turning to face the opposite direction, is the right hand placed on the hip?  
3. When facing the rear opponent, is the body turned completely to the rear with the rear heel slightly raised and in a straight line?  
4. Is the thrust performed without too much bend in the knees?  
---
**Soetezuki**  
1. When the initial diagonal cut is made from the opponent's right shoulder down through to the waist, is the right hand at the height of the navel and the sword tip slightly above the horizontal level?  
2. Is the sword held securely between the left thumb and forefinger with the right hand near the hip?  
3. Does the right hand finish in front of the navel after making the thrust and does the thrusting action adequately reach the opponent's body?  
4. When showing Zanshin, is the right elbow naturally straight and the right hand no higher or lower than the chest level?  
---
**Shiogiri**  
1. Is the strike to the first opponent's hand done firmly and effectively with the flat side of the Tsuka?  
2. In making Sayabiki, is the Mune near the Monouchi of the sword on the chest and is the thrust made surely into the solar plexus of the opponent?  
3. When the thrust is made, is the left hand brought to the center of the navel and both arms aid the technique with the correct tension?  
4. Is the final cut made by going through Waki Gamae without hesitation or pause?  
---
**Sougiri**  
1. When the sword is drawn up, is it in a correct position to parry an attack?  
2. When moving forwards, does the performer use Okuri Ashi footwork?  
3. When making the horizontal cut, is it performed horizontally with the correct angle of the blade?  
---
**Nukiuchi**  
1. When the sword is drawn up and out, have both feet moved back adequately to evade the downward cut of the opponent?  
2. When the right hand is taken upwards, is it in the center line of the body and is the step forwards with the right foot sufficient to enable the sword to reach the target?  
:::