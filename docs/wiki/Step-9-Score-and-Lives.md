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

Previous: [Game over and win](Step-8-Game-Over-and-Win) · Next: [[('How did I approach the project?', 'I planned before I coded. The project was split into three gateways: set-up, the game and the documentation. The game itself was built in nine small steps, each on its own branch with its own pull request, tests, screenshot and review record, so the history shows how the game grew. Everything that does not need a window, such as clamping, fleet layout, collisions, the move interval and the game state, went into `rules.py` so it could be tested without a display.'), ('What was hard?', 'Testing a window-based game. `turtle` needs Tk and a display, so the tests that open a window cannot run on the continuous integration runner or on my desktop. I solved it with a Docker image that runs the game and the tests on a virtual display. Timing was also tricky: taking a screenshot of a bullet in flight or of a fleet that has moved needs the key presses and the waiting time to match the frame loop.'), ('What was easy?', 'Once the rules were separate from the drawing, the logic was short and easy to test. Subclassing `Turtle` for the ship, the bullet, the aliens and the barrier blocks gave each thing its own small class, and the constants in `constants.py` made tuning the game a one-line change.'), ('How can I improve for the next project?', 'Start the screenshot and test environment first, before the first line of game code, and write the test for a rule before the rule. I would also run the scan rules of the pipeline locally in the same way the server runs them, to find findings earlier.'), ('What was my biggest learning?', 'Keeping the rules of a game free of the screen is what makes a graphical project testable, and a time-based loop (a move every second) is simpler and fairer than counting frames.'), ('What would I do differently?', 'I would draw the aliens and the ship as custom shapes instead of the built-in `turtle` shapes, add sound and a high-score list, and let the fleet shoot in patterns. I would also take the screenshots from a recorded play-through instead of single key presses.')]](Reflection) · [Overview](Home)
