[English](Step-3-Shooting) · **Dansk** · [Bahasa Malaysia](Step-3-Shooting-ms)

# Trin 3: Skydning

![En kugle, der flyver op fra skibet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-3-shooting.png)

## Det vi byggede

Klasserne `Bullet` og `Game`. <kbd>Space</kbd> skyder en kugle fra skibet; den flyver opad og skjules igen, når den forlader skærmens top. Kun én kugle flyver ad gangen. `Game` ejer nu objekterne, binder tasterne og kører billedløkken.

## Det vi lærte

- At bruge et flag (`active`) til kun at tillade ét skud ad gangen
- At vise og skjule en turtle i stedet for at oprette nye
- At indføre en `Game`-klasse, der ejer objekterne og løkken
- At teste bevægelse med simple tal: ét skridt er `BULLET_STEP` pixels

## Prøv det

Tryk på <kbd>Space</kbd>.

## Hvor koden er

`src/bullet.py`, `src/game.py`

Forrige: [Rumskib](Step-2-Spaceship-da) · Næste: [Rumvæsenflåde](Step-4-Alien-Fleet-da) · [Oversigt](Home-da)
