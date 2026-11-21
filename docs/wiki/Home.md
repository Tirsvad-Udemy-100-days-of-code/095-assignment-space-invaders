**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Space Invaders

The classic Space Invaders shoot 'em up for one player with Python turtle graphics: move your spaceship, shoot the aliens before they reach you, and hide behind the barriers.

![The score and lives line above the fleet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-9-score-lives.png)

## What is it?

Day 95 of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*. A black 800 by 600 window titled "Space Invaders" opens with a green spaceship at the bottom, four barriers above it and five rows of aliens at the top. <kbd>Left</kbd> and <kbd>Right</kbd> move the ship and <kbd>Space</kbd> fires one bullet at a time. Every second the aliens move closer, they turn and drop at the edges, and they move faster as fewer are left. They shoot back; a hit costs a life. The game is lost when an alien touches the ship, reaches its row or the lives run out, and won when the last alien is shot. The game was built in nine steps, one pull request per step, and each step has its own page with a screenshot and what we gained.

## The nine steps

1. [Game screen](Step-1-Game-Screen)
2. [Spaceship](Step-2-Spaceship)
3. [Shooting](Step-3-Shooting)
4. [Alien fleet](Step-4-Alien-Fleet)
5. [Alien movement](Step-5-Alien-Movement)
6. [Shooting aliens](Step-6-Shooting-Aliens)
7. [Barriers](Step-7-Barriers)
8. [Game over and win](Step-8-Game-Over-and-Win)
9. [Score and lives](Step-9-Score-and-Lives)

## Next

- [Getting Started](Getting-Started)
- [[('How did I approach the project?', 'I planned before I coded. The project was split into three gateways: set-up, the game and the documentation. The game itself was built in nine small steps, each on its own branch with its own pull request, tests, screenshot and review record, so the history shows how the game grew. Everything that does not need a window, such as clamping, fleet layout, collisions, the move interval and the game state, went into `rules.py` so it could be tested without a display.'), ('What was hard?', 'Testing a window-based game. `turtle` needs Tk and a display, so the tests that open a window cannot run on the continuous integration runner or on my desktop. I solved it with a Docker image that runs the game and the tests on a virtual display. Timing was also tricky: taking a screenshot of a bullet in flight or of a fleet that has moved needs the key presses and the waiting time to match the frame loop.'), ('What was easy?', 'Once the rules were separate from the drawing, the logic was short and easy to test. Subclassing `Turtle` for the ship, the bullet, the aliens and the barrier blocks gave each thing its own small class, and the constants in `constants.py` made tuning the game a one-line change.'), ('How can I improve for the next project?', 'Start the screenshot and test environment first, before the first line of game code, and write the test for a rule before the rule. I would also run the scan rules of the pipeline locally in the same way the server runs them, to find findings earlier.'), ('What was my biggest learning?', 'Keeping the rules of a game free of the screen is what makes a graphical project testable, and a time-based loop (a move every second) is simpler and fairer than counting frames.'), ('What would I do differently?', 'I would draw the aliens and the ship as custom shapes instead of the built-in `turtle` shapes, add sound and a high-score list, and let the fleet shoot in patterns. I would also take the screenshots from a recorded play-through instead of single key presses.')]](Reflection)
- [Project Documents](Project-Documents)
