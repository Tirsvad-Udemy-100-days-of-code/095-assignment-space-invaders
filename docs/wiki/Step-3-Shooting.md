**English** · [Dansk](Step-3-Shooting-da) · [Bahasa Malaysia](Step-3-Shooting-ms)

# Step 3: Shooting

![A bullet flying up from the ship](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-3-shooting.png)

## What we built

The `Bullet` class and the `Game` class. <kbd>Space</kbd> fires a bullet from the ship; it flies up and is hidden again when it leaves the top of the screen. Only one bullet flies at a time. `Game` now owns the objects, binds the keys and runs the frame loop.

## What we gained

- Using a flag (`active`) to allow one shot at a time
- Showing and hiding a turtle instead of creating new ones
- Introducing a `Game` class to own the objects and the loop
- Testing movement with simple numbers: one step is `BULLET_STEP` pixels

## Try it

Press <kbd>Space</kbd>.

## Where the code is

`src/bullet.py`, `src/game.py`

Previous: [Spaceship](Step-2-Spaceship) · Next: [Alien fleet](Step-4-Alien-Fleet) · [Overview](Home)
