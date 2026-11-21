**English** · [Dansk](Step-8-Game-Over-and-Win-da) · [Bahasa Malaysia](Step-8-Game-Over-and-Win-ms)

# Step 8: Game over and win

![The GAME OVER message with the aliens at the ship](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-8-game-over.png)

![The YOU WIN message after the last alien was shot](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-8-win.png)

## What we built

The game is lost when an alien touches the ship or reaches the ship's row, and won when the last alien is shot. The pure function `game_state` decides, the `Banner` class writes GAME OVER or YOU WIN, and the keys stop working. The screenshots of this step come from prepared situations in `tools/scenarios/`.

## What we gained

- Describing the game as a state: playing, lost or won
- Letting one function decide the state, so the rule is in one place
- Stopping the frame loop and the keys when the game has ended
- Preparing a situation in a script to take a screenshot of a rare moment

## Try it

Let the aliens reach the ship, or shoot them all.

## Where the code is

`src/banner.py`, `src/game.py`: `check_state`, `src/rules.py`: `game_state`

Previous: [Barriers](Step-7-Barriers) · Next: [Score and lives](Step-9-Score-and-Lives) · [Overview](Home)
