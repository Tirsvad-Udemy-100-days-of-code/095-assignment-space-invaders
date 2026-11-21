**English** · [Dansk](Step-7-Barriers-da) · [Bahasa Malaysia](Step-7-Barriers-ms)

# Step 7: Barriers

![Four barriers, one block damaged by a bullet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-7-barriers.png)

## What we built

Four barriers of blocks between the ship and the aliens. A block takes three hits and changes colour from green to yellow to red before it is gone. A bullet that hits a block disappears.

## What we gained

- Building a larger shape from many small objects (`BarrierBlock`, `BarrierWall`)
- Showing the state of an object with its colour
- Reusing `is_hit` for a new kind of collision
- Computing the block positions in a pure function (`barrier_positions`)

## Try it

Fire at a barrier and watch the block change colour.

## Where the code is

`src/barrier.py`, `src/rules.py`: `barrier_positions`

Previous: [Shooting aliens](Step-6-Shooting-Aliens) · Next: [Game over and win](Step-8-Game-Over-and-Win) · [Overview](Home)
