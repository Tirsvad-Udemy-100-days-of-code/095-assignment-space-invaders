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
