**English** · [Dansk](Step-1-Game-Screen-da) · [Bahasa Malaysia](Step-1-Game-Screen-ms)

# Step 1: Game screen

![An empty black game window](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-1-screen.png)

## What we built

A black 800 by 600 window titled "Space Invaders" and a frame loop. Animation is switched off with `tracer(0)`, so the game draws a frame itself with `update()`, and `ontimer` calls the next frame without blocking the window.

## What we gained

- Setting up a turtle `Screen`: size, background colour and title
- Turning automatic animation off with `tracer(0)` and drawing with `update()`
- Running a loop with `ontimer` so the window stays responsive and can be closed
- Putting every number in `constants.py` from the first line

## Try it

Start the game; an empty black window opens.

## Where the code is

`src/main.py`: `create_screen`, `main`

Next: [Spaceship](Step-2-Spaceship) · [Overview](Home)
