[English](Step-7-Barriers) · **Dansk** · [Bahasa Malaysia](Step-7-Barriers-ms)

# Trin 7: Barrierer

![Fire barrierer, én blok beskadiget af en kugle](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-7-barriers.png)

## Det vi byggede

Fire barrierer af blokke mellem skibet og rumvæsnerne. En blok tåler tre træf og skifter farve fra grøn til gul til rød, før den er væk. En kugle, der rammer en blok, forsvinder.

## Det vi lærte

- At bygge en større figur af mange små objekter (`BarrierBlock`, `BarrierWall`)
- At vise et objekts tilstand med dets farve
- At genbruge `is_hit` til en ny slags kollision
- At beregne blokkenes positioner i en ren funktion (`barrier_positions`)

## Prøv det

Skyd mod en barriere og se blokken skifte farve.

## Hvor koden er

`src/barrier.py`, `src/rules.py`: `barrier_positions`

Forrige: [Skyd rumvæsnerne](Step-6-Shooting-Aliens-da) · Næste: [Game over og sejr](Step-8-Game-Over-and-Win-da) · [Oversigt](Home-da)
