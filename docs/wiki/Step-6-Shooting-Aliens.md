**English** · [Dansk](Step-6-Shooting-Aliens-da) · [Bahasa Malaysia](Step-6-Shooting-Aliens-ms)

# Step 6: Shooting aliens

![A gap in the bottom row where an alien was shot](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-6-hits.png)

## What we built

A bullet that touches an alien removes it. A hit is found by the distance between the centres, `is_hit`. The fewer aliens that are left, the shorter the time between two moves, down to a minimum, so the game gets harder as you win.

## What we gained

- Detecting a collision by distance between two centres
- Removing an item from a list safely, without changing the list while looping over it
- Making the difficulty grow with the progress (`move_interval`)
- Letting one rule, `is_hit`, serve several kinds of collision

## Try it

Move under an alien and press <kbd>Space</kbd>.

## Where the code is

`src/fleet.py`: `remove_hit`; `src/rules.py`: `is_hit`, `move_interval`

Previous: [Alien movement](Step-5-Alien-Movement) · Next: [Barriers](Step-7-Barriers) · [Overview](Home)
