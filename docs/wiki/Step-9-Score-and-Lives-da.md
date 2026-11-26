[English](Step-9-Score-and-Lives) · **Dansk** · [Bahasa Malaysia](Step-9-Score-and-Lives-ms)

# Trin 9: Point og liv

![Linjen med point og liv over flåden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-9-score-lives.png)

## Det vi byggede

En `Scoreboard` med point og tre liv. Rumvæsnerne skyder igen: hvert andet sekund skyder det nederste rumvæsen i en tilfældig kolonne en rød kugle, som en barriere stopper, og som skibet betaler for med et liv. En række rumvæsner er 50, 40, 30, 20 eller 10 point værd.

## Det vi lærte

- At holde point og liv i én lille klasse, der også skriver dem
- At genbruge `Bullet` til en kugle, der flyver nedad (et negativt skridt)
- At vælge en tilfældig skytte, hvor tilfældighedskilden gives udefra, så en test kan fastlægge den
- At finde det laveste element i hver kolonne med en ren funktion (`lowest_per_column`)

## Prøv det

Spil et helt spil og følg point og liv.

## Hvor koden er

`src/scoreboard.py`, `src/game.py`, `src/fleet.py`: `choose_shooter`

Forrige: [Game over og sejr](Step-8-Game-Over-and-Win-da) · Næste: [Refleksion](Reflection-da) · [Oversigt](Home-da)
