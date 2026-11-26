**English** · [Dansk](Step-9-Score-and-Lives-da) · [Bahasa Malaysia](Step-9-Score-and-Lives-ms)

# Step 9: Score and lives

![The score and lives line above the fleet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-9-score-lives.png)

## What we built

A `Scoreboard` with the score and three lives. The aliens shoot back: every two seconds the lowest alien of a random column fires a red bullet, which a barrier stops and the ship pays for with a life. A row of aliens is worth 50, 40, 30, 20 or 10 points.

## What we gained

- Keeping score and lives in one small class that also writes them
- Reusing `Bullet` for a bullet that flies down (a negative step)
- Picking a random shooter, with the random source passed in so a test can fix it
- Finding the lowest item of each column with a pure function (`lowest_per_column`)

## Try it

Play a full game and watch the score and lives.

## Where the code is

`src/scoreboard.py`, `src/game.py`, `src/fleet.py`: `choose_shooter`

Previous: [Game over and win](Step-8-Game-Over-and-Win) · Next: [Reflection](Reflection) · [Overview](Home)
