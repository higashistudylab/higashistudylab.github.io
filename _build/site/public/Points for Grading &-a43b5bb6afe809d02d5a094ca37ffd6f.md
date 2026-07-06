---
downloads: []
kernelspec:
  name: python3
  display_name: 'Python 3'
---
# Jodo Points for Grading & Refereeing

**Points for Shi:**
::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "jodo_points_shi.csv"
split_points = []
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
    for d in data:
        for i, line in enumerate(d['back'].split('\n')):
            split_points.append({'front':d['front']+f" | Point {i+1}", 'back':line[3:]})
display_flashcards(split_points, shuffle_cards=True)
```
:::
:::{tab-item} Ordered
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "jodo_points_shi.csv"
split_points = []
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
    for d in data:
        for i, line in enumerate(d['back'].split('\n')):
            split_points.append({'front':d['front']+f" | Point {i+1}", 'back':line[3:]})
display_flashcards(split_points, shuffle_cards=False)
```
:::
::::


**Points for Uchi:**
::::{tab-set}

:::{tab-item} Shuffled
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "jodo_points_uchi.csv"
split_points = []
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
    for d in data:
        for i, line in enumerate(d['back'].split('\n')):
            split_points.append({'front':d['front']+f" | Point {i+1}", 'back':line[3:]})
display_flashcards(split_points, shuffle_cards=True)
```
:::
:::{tab-item} Ordered
```{code-cell} python
:tags: ["remove-input"]
from jupytercards import display_flashcards
import csv

file = "jodo_points_uchi.csv"
split_points = []
with open(file, newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f, delimiter=';'))
    for d in data:
        for i, line in enumerate(d['back'].split('\n')):
            split_points.append({'front':d['front']+f" | Point {i+1}", 'back':line[3:]})
display_flashcards(split_points, shuffle_cards=False)
```
:::
::::

:::{dropdown} Answer Overview
**Tsukizue**

Shi:
1) How is your posture after you have moved your body diagonally backwards and to the right?
2) Are you striking Uchi's left wrist after rotating the Jo diagonally upwards and to the right in a large movement?
3) Are you striking Uchi's left wrist with a correct Honteuchi?

Uchi:
1) From a correct Hasso-no-kamae are you entering Shi's Maai and cutting down to a line parallel to the floor?
2) Are you adopting the correct Hidari-jodan-no-kamae?
---
**Suigetsu**

Shi:
1) After moving your body diagonally forwards and to the right, are you correctly thrusting Uchi's Suigetsu by pulling back your left shoulder?
2) Have you correctly adopted Hikiotoshi-no-kamae?
3) How is the strength of your Hikiotoshiuchi?

Uchi:
1) Are you correctly cutting Shi's Shomen?
2) After taking sufficient Maai from Hasso-no-kamae are you correctly adopting the Chudan no Kamae?
---
**Hissage**

Shi:
1) Is the Josaki equally aligned with the Tachi in Awase?
2) From a correct Kuritsuke are you correctly thrusting the Suigetsu?

Uchi:
1) Is the Tachi's Kissaki equally aligned with the Jo in Awase?
2) From Hidari-jodan-no-kamae are you correctly cutting the Shomen?
3) Have you had Kuritsuke correctly performed on you?

---
**Shamen**

Shi:
1) After moving your body diagonally forwards and to the right, are you correctly dividing the Jo into four equal parts, sliding your right hand and striking Uchi's temple with the Josaki?
2) Are you correctly thrusting Uchi's Suigetsu?

Uchi:
1) Are you correctly cutting Shomen to a line parallel to the floor?
2) After taking sufficient Maai are you correctly adopting Hidari-jodan-no-kamae?

---
**Sakan**

Shi:
1) Are you taking an appropriate amount of Maai when you go into Ma Hanmi and move backwards to parry the Kensaki that has been thrust at you?
2) When you strike the Tachi is your right foot forwards?
3) Aligning your left foot to your right foot, are you carrying out the Hikiotoshi in a large movement after holding the entire Jo in both hands?

Uchi:
1) Are you correctly thrusting Shi's Suigetsu?
2) After the Tachi is struck and you move backwards, are you doing so with your right, then left and right foot?
3) Is your Chudan and Hasso-no-kamae correct?

---
**Monomi**

Shi:
1) How is your Ashi Sabaki (footwork)?
2) Are you striking Uchi's wrist after rotating the Jo in a large movement?
3) Are you correctly executing Kaeshizuki?

Uchi:
1) Are you cutting Shi's Shomen to a line parallel with the floor?
2) Have you correctly adopted Hidari-jodan-no-kamae?
---
**Kasumi**

Shi:
1) When you strike in Gyakuteuchi how is your posture and attack?
2) Are you correctly performing Hikiotoshi-no-kamae and Taiatari?

Uchi:
1) Stepping forwards with your left then right from a Nisoku-ittou-no-maai are you correctly cutting Shomen?
2) After having Taiatari performed on you are you correctly moving backwards?
---
**Tachiotoshi**

Shi:
1) After moving your body are you correctly carrying out Gyakuteuchi?
2) Are you in a correct posture for Kuritsuke?

Uchi:
1) Are you parrying the Jo after correctly moving your body horizontally to the left?
2) Are you cutting Shi's neck after rotating the Tachi above your head in a large movement?
3) Are you moving backwards correctly after having had Kuritsuke performed on you?
---
**Raiuchi**

Shi:
1) Are you correctly thrusting Uchi's Suigetsu?
2) After moving your body diagonally forwards and to the left, are you correctly thrusting Uchi's Hibara?

Uchi:
1) Are you correctly cutting Shi's upper arm?
2) After taking a large step backwards with your left foot, are you cutting Shi from their shoulder to their neck?
---
**Seigan**

Shi:
1) Are you correctly entering Uchi's Maai to attack their eyes with the Josaki and then correctly thrusting their Suigetsu?
2) After moving your body diagonally forwards and to the left, are you correctly thrusting at Uchi's Hibara?
3) In response to Uchi's Katategiri, do you move your wrist out of reach and strike their Suigetsu from a correct Hasso posture?

Uchi:
1) In the correct Maai relative to Shi how is your posture when you grip the Tsuka with your right hand?
2) Are you correctly carrying out Katategiri (one handed cut)?
---
**Midaredome**

Shi:
1) When you strike in Gyakuteuchi what is the position of your left hand?
2) When the Josaki is above your head are you correctly attacking Uchi's face?

Uchi:
1) Are you correctly cutting Shi's Do (upper body)?
2) After moving your right foot slightly closer to your left foot, do you retaliate by cutting Shi's Shomen?
---
**Ranai**

Shi:
1) From Hikiotoshi-no-kamae, are you using your left and right feet to sufficiently contain Uchi; are you entering his Temoto?
2) Are you correctly thrusting Uchi's Hibara?
3) After stepping forwards with your right foot, are you immediately cutting Shomen?
4) Are you moving back correctly in response to Uchi's attack?
5) Are you correctly separating from Uchi?
6) Is your posture on receiving Dobarai correct?

Uchi:
1) How is your posture after you have drawn the Tachi diagonally upwards and to the right?
2) Are you correctly cutting Shi's Do (upper side body)?
3) After moving your left foot backwards are you correctly parrying the Jo in front of your forehead?
4) Are you correctly attacking Shi's chest and cutting it?
5) After Shi has performed Kurihanashi on you, move backwards using your right, left and right foot, how is your posture and Metsuke?
6) Are you cutting Shi's right wrist with Katategiri; and are you stepping forwards and correctly thrusting?
7) Are you correctly cutting Shi's Do (upper side body)?

**Appendix for Uchi (Tachi)**
1) Be sure to keep your arms and wrists flexible.
2) How to correctly cut with an effective Hasuji.
:::