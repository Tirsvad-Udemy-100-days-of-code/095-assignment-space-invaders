[English](Step-2-Spaceship) · **Dansk** · [Bahasa Malaysia](Step-2-Spaceship-ms)

# Trin 2: Rumskib

![Rumskibet flyttet til venstre](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-2-ship.png)

## Det vi byggede

Klassen `Ship`, en grøn trekant nederst på skærmen. Piletasterne flytter den ét skridt til venstre eller højre, og den stopper ved skærmens kant. Grænsen er en ren funktion, `clamp`, i `rules.py`.

## Det vi lærte

- At arve fra `Turtle` for at lave et spilobjekt
- At binde taster med `listen` og `onkeypress`
- At holde en regel fri af skærmen (`clamp`), så en test ikke behøver et vindue
- At teste skærmobjekter i en container i stedet for på skrivebordet

## Prøv det

Tryk på <kbd>Left</kbd> og <kbd>Right</kbd>.

## Hvor koden er

`src/ship.py`, `src/rules.py`: `clamp`

Forrige: [Spilskærm](Step-1-Game-Screen-da) · Næste: [Skydning](Step-3-Shooting-da) · [Oversigt](Home-da)
