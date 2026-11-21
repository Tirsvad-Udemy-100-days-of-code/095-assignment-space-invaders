[English](Step-1-Game-Screen) · **Dansk** · [Bahasa Malaysia](Step-1-Game-Screen-ms)

# Trin 1: Spilskærm

![Et tomt, sort spilvindue](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-1-screen.png)

## Det vi byggede

Et sort vindue på 800 gange 600 med titlen "Space Invaders" og en billedløkke. Animationen er slået fra med `tracer(0)`, så spillet selv tegner et billede med `update()`, og `ontimer` kalder det næste billede uden at blokere vinduet.

## Det vi lærte

- At opsætte en turtle-`Screen`: størrelse, baggrundsfarve og titel
- At slå automatisk animation fra med `tracer(0)` og tegne med `update()`
- At køre en løkke med `ontimer`, så vinduet forbliver responsivt og kan lukkes
- At lægge alle tal i `constants.py` fra første linje

## Prøv det

Start spillet; et tomt, sort vindue åbner.

## Hvor koden er

`src/main.py`: `create_screen`, `main`

Næste: [Rumskib](Step-2-Spaceship-da) · [Oversigt](Home-da)
