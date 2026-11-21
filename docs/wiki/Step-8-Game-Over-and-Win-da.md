[English](Step-8-Game-Over-and-Win) · **Dansk** · [Bahasa Malaysia](Step-8-Game-Over-and-Win-ms)

# Trin 8: Game over og sejr

![Beskeden GAME OVER med rumvæsnerne ved skibet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-8-game-over.png)

![Beskeden YOU WIN, efter det sidste rumvæsen blev skudt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-8-win.png)

## Det vi byggede

Spillet er tabt, når et rumvæsen rører skibet eller når skibets række, og vundet, når det sidste rumvæsen er skudt. Den rene funktion `game_state` afgør det, klassen `Banner` skriver GAME OVER eller YOU WIN, og tasterne holder op med at virke. Skærmbillederne til dette trin kommer fra forberedte situationer i `tools/scenarios/`.

## Det vi lærte

- At beskrive spillet som en tilstand: i gang, tabt eller vundet
- At lade én funktion afgøre tilstanden, så reglen står ét sted
- At stoppe billedløkken og tasterne, når spillet er slut
- At forberede en situation i et script for at tage et skærmbillede af et sjældent øjeblik

## Prøv det

Lad rumvæsnerne nå skibet, eller skyd dem alle.

## Hvor koden er

`src/banner.py`, `src/game.py`: `check_state`, `src/rules.py`: `game_state`

Forrige: [Barrierer](Step-7-Barriers-da) · Næste: [Point og liv](Step-9-Score-and-Lives-da) · [Oversigt](Home-da)
