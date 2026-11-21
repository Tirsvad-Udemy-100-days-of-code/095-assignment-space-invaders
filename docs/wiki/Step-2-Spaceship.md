**English** · [Dansk](Step-2-Spaceship-da) · [Bahasa Malaysia](Step-2-Spaceship-ms)

# Step 2: Spaceship

![The spaceship moved to the left](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-2-ship.png)

## What we built

The `Ship` class, a green triangle at the bottom of the screen. The arrow keys move it one step left or right, and it stops at the screen edges. The limit is a pure function, `clamp`, in `rules.py`.

## What we gained

- Subclassing `Turtle` to make a game object
- Binding keys with `listen` and `onkeypress`
- Keeping a rule free of the screen (`clamp`) so a test needs no window
- Testing screen objects in a container instead of on the desktop

## Try it

Press <kbd>Left</kbd> and <kbd>Right</kbd>.

## Where the code is

`src/ship.py`, `src/rules.py`: `clamp`

Previous: [Game screen](Step-1-Game-Screen) · Next: [Shooting](Step-3-Shooting) · [Overview](Home)
