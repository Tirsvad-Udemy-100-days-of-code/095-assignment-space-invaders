**English** · [Dansk](Step-4-Alien-Fleet-da) · [Bahasa Malaysia](Step-4-Alien-Fleet-ms)

# Step 4: Alien fleet

![Five rows of aliens in different colours](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-4-fleet.png)

## What we built

The `Alien` and `Fleet` classes: five rows of eight aliens, each row in its own colour, centred at the top of the screen. The positions are worked out by `fleet_positions` in `rules.py`.

## What we gained

- Turning a grid into a list of positions with nested loops
- Separating the layout calculation (pure, tested) from the drawing
- Using one colour per row to tell rows apart
- Keeping the alien objects in a list the rest of the game can use

## Try it

Start the game; the fleet is in place.

## Where the code is

`src/alien.py`, `src/fleet.py`, `src/rules.py`: `fleet_positions`

Previous: [Shooting](Step-3-Shooting) · Next: [Alien movement](Step-5-Alien-Movement) · [Overview](Home)
