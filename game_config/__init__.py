from .teams import TEAM
from .markers import (
    MARKER_TYPE,
    ARENA_MARKER,
    MARKER,
    by_id,
    COLOURS,
)
from .startup_poems import POEM_ON_STARTUP

PURPLE = (255, 0, 215)  # Purple
ORANGE = (0, 128, 255)  # Orange
YELLOW = (0, 255, 255)  # Yellow
GREEN = (0, 255, 0)  # Green
RED = (0, 0, 255)  # Red
BLUE = (255, 0, 0)  # Blue
WHITE = (255, 255, 255)  # White

__all__ = (
    "TEAM",
    "MARKER_TYPE",
    "ARENA_MARKER",
    "MARKER",
    "by_id",
    "COLOURS",
    "POEM_ON_STARTUP",
)