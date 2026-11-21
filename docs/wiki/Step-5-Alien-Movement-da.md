[English](Step-5-Alien-Movement) · **Dansk** · [Bahasa Malaysia](Step-5-Alien-Movement-ms)

# Trin 5: Rumvæsnernes bevægelse

![Flåden efter at have bevæget sig til højre](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-5-movement.png)

## Det vi byggede

Hvert sekund rykker flåden ét skridt til siden. Når næste skridt ville føre et rumvæsen forbi kanten, rykker flåden ned og vender om. Tiden aflæses med `time.monotonic`, og beslutningen træffes af de rene funktioner `is_due` og `next_fleet_move`.

## Det vi lærte

- At bevæge efter tid og ikke ved at tælle billeder, så hastigheden ikke afhænger af computeren
- At skrive beslutningen om næste bevægelse som en funktion, der returnerer ændringen og den nye retning
- At rykke ned og vende ved en kant
- At teste en tidsregel ved at give tiden som parameter

## Prøv det

Vent et par sekunder og se flåden bevæge sig.

## Hvor koden er

`src/fleet.py`: `update`, `move`; `src/rules.py`: `is_due`, `next_fleet_move`

Forrige: [Rumvæsenflåde](Step-4-Alien-Fleet-da) · Næste: [Skyd rumvæsnerne](Step-6-Shooting-Aliens-da) · [Oversigt](Home-da)
