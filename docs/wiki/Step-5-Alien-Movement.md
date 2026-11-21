**English** · [Dansk](Step-5-Alien-Movement-da) · [Bahasa Malaysia](Step-5-Alien-Movement-ms)

# Step 5: Alien movement

![The fleet after it has moved to the right](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-5-movement.png)

## What we built

Every second the fleet moves one step sideways. When the next step would take an alien past the edge, the fleet drops closer and turns around. The time is read with `time.monotonic`, and the decision is made by the pure functions `is_due` and `next_fleet_move`.

## What we gained

- Moving by time, not by counting frames, so the speed does not depend on the computer
- Writing the decision of the next move as a function that returns the change and the new direction
- Dropping and reversing at an edge
- Testing a time rule by passing the time in

## Try it

Wait a few seconds and watch the fleet move.

## Where the code is

`src/fleet.py`: `update`, `move`; `src/rules.py`: `is_due`, `next_fleet_move`

Previous: [Alien fleet](Step-4-Alien-Fleet) · Next: [Shooting aliens](Step-6-Shooting-Aliens) · [Overview](Home)
