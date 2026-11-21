[English](Step-6-Shooting-Aliens) · **Dansk** · [Bahasa Malaysia](Step-6-Shooting-Aliens-ms)

# Trin 6: Skyd rumvæsnerne

![Et hul i nederste række, hvor et rumvæsen blev skudt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-6-hits.png)

## Det vi byggede

En kugle, der rører et rumvæsen, fjerner det. Et træf findes ud fra afstanden mellem centrene, `is_hit`. Jo færre rumvæsner der er tilbage, jo kortere er tiden mellem to bevægelser, ned til et minimum, så spillet bliver sværere, jo mere du vinder.

## Det vi lærte

- At finde en kollision ud fra afstanden mellem to centre
- At fjerne et element fra en liste sikkert, uden at ændre listen mens man løber igennem den
- At lade sværhedsgraden vokse med fremskridtet (`move_interval`)
- At lade én regel, `is_hit`, tjene flere slags kollisioner

## Prøv det

Flyt dig under et rumvæsen og tryk på <kbd>Space</kbd>.

## Hvor koden er

`src/fleet.py`: `remove_hit`; `src/rules.py`: `is_hit`, `move_interval`

Forrige: [Rumvæsnernes bevægelse](Step-5-Alien-Movement-da) · Næste: [Barrierer](Step-7-Barriers-da) · [Oversigt](Home-da)
