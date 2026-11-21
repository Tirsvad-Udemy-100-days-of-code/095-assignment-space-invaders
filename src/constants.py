"""@file constants.py
@brief Constants of the Space Invaders game.

Every number and colour used by the game lives here; the other modules import
them instead of repeating literals.
"""

## Window width in pixels.
SCREEN_WIDTH: int = 800
## Window height in pixels.
SCREEN_HEIGHT: int = 600
## Window background colour.
SCREEN_COLOR: str = "black"
## Window title.
SCREEN_TITLE: str = "Space Invaders"

## Pause between two frames in milliseconds.
FRAME_DELAY_MS: int = 20

## Colour of the spaceship.
SHIP_COLOR: str = "green"
## Vertical position of the spaceship.
SHIP_Y: int = -250
## Pixels the spaceship moves per key press.
SHIP_STEP: int = 20
## Stretch factors of the spaceship's triangle (width, length).
SHIP_STRETCH: tuple[float, float] = (1.5, 2.0)
## Distance between the screen edge and the outermost spaceship position.
SHIP_EDGE_MARGIN: int = 30
## Largest horizontal position of the spaceship.
SHIP_MAX_X: int = SCREEN_WIDTH // 2 - SHIP_EDGE_MARGIN

## Colour of the bullet.
BULLET_COLOR: str = "yellow"
## Pixels the bullet moves up per frame.
BULLET_STEP: int = 12
## Stretch factors of the bullet's square (width, length).
BULLET_STRETCH: tuple[float, float] = (0.2, 1.0)
## Distance between the ship and the point where the bullet appears.
BULLET_START_OFFSET: int = 20
## Vertical position above which the bullet has left the screen.
SCREEN_TOP: int = SCREEN_HEIGHT // 2

## Number of alien rows.
ALIEN_ROWS: int = 5
## Number of aliens in a row.
ALIEN_COLUMNS: int = 8
## Colours of the alien rows, from the top row down.
ALIEN_COLORS: tuple[str, ...] = ("red", "orange", "yellow", "cyan", "magenta")
## Horizontal distance between two aliens.
ALIEN_SPACING_X: int = 70
## Vertical distance between two alien rows.
ALIEN_SPACING_Y: int = 45
## Vertical position of the top alien row.
FLEET_TOP_Y: int = 260
## Stretch factors of the alien shape (width, length).
ALIEN_STRETCH: tuple[float, float] = (1.2, 1.2)

## Seconds between two moves of the fleet: it moves closer once a second.
FLEET_MOVE_INTERVAL: float = 1.0
## Pixels the fleet moves sideways per move.
FLEET_STEP_X: int = 20
## Pixels the fleet drops when it turns at an edge.
FLEET_DROP: int = 25
## Largest horizontal position an alien may reach.
FLEET_EDGE_X: int = SCREEN_WIDTH // 2 - 40

## Distance between bullet and alien centres that counts as a hit.
HIT_DISTANCE: int = 22
## Shortest time between two fleet moves, reached when few aliens are left.
FLEET_MIN_INTERVAL: float = 0.2
