import enum
import typing

from .teams import TEAM

"""
Marker definitions for RoboCon Oxfordshire 2027 - Quidditch.

The game objects are Quaffles (the coloured boxes) and the Snitch.
Quaffles are identified by AprilTags 0 to 3, one per team colour:
    0 = Red, 1 = Yellow, 2 = Green, 3 = Blue.
The Snitch is AprilTag 4 (Gold).

Arena wall markers start at ID 100. Each side of the arena belongs to a
team corner:
    100 - 102, 121 - 123 : Red corner
    103 - 108            : Yellow corner
    109 - 114            : Green corner
    115 - 120            : Blue corner

Wall markers are 200x200 mm and 50 mm off the floor; game object markers
are 100x100 mm.
"""


class MARKER_TYPE(enum.Enum):
    QUAFFLE = enum.auto()  # A coloured box you are trying to gather
    SNITCH = enum.auto()  # The gold snitch, worth a x3 multiplier
    ARENA = enum.auto()  # These are the wall markers


class BASE_MARKER:  # Base marker class that QUAFFLE/SNITCH/ARENA derive from.
    team_marker_colors: dict = {  # Colour definitions for each team defined in TEAMS
        TEAM.RED: (255, 64, 0),  # RED
        TEAM.YELLOW: (255, 255, 32),  # YELLOW
        TEAM.GREEN: (50, 255, 0),  # GREEN
        TEAM.BLUE: (0, 100, 255),  # BLUE
    }
    snitch_color: tuple = (255, 215, 0)  # Gold

    def __init__(
        self,
        id: int,
        type: MARKER_TYPE,
    ) -> None:
        self.id = id
        self.type = type
        self.owning_team: typing.Union[TEAM, None] = None

        # Sizes are in meters
        self.size = 0.2 if self.type == MARKER_TYPE.ARENA else 0.1

    def __repr__(self) -> str:
        return f"<Marker type={self.type} owning_team={self.owning_team} />"

    @property
    def bounding_box_color(self) -> tuple:
        if self.type == MARKER_TYPE.ARENA:  # If it is a wall
            return tuple(self.team_marker_colors[self.owning_team])  # Picks the team colour from above
        if self.type == MARKER_TYPE.SNITCH:
            return tuple(self.snitch_color)  # Gold
        return tuple(self.team_marker_colors[self.owning_team])  # Quaffle colour


class ARENA_MARKER(BASE_MARKER):  # Not much going on here. This represents a wall.
    def __init__(self, id: int, owner: TEAM) -> None:
        super().__init__(id, MARKER_TYPE.ARENA)
        self.owning_team = owner

    def __repr__(self) -> str:
        return f"<Marker(ARENA) owning_team={self.owning_team} />"


class QUAFFLE_MARKER(BASE_MARKER):  # A coloured game object rather than a wall.
    def __init__(self, id: int, colour: TEAM) -> None:
        super().__init__(id, MARKER_TYPE.QUAFFLE)
        self.owning_team = colour

    def __repr__(self) -> str:
        return f"<Marker(QUAFFLE) colour={self.owning_team} />"


class SNITCH_MARKER(BASE_MARKER):  # The gold snitch, worth a x3 multiplier.
    def __init__(self, id: int = 4) -> None:
        super().__init__(id, MARKER_TYPE.SNITCH)

    def __repr__(self) -> str:
        return "<Marker(SNITCH) />"


# Drops/crates existed in previous years; keep the alias for any residual
# imports but it is no longer produced by by_id.
BOX_MARKER = QUAFFLE_MARKER


class MARKER(BASE_MARKER):  # This is literally just how the code gets the different marker types.
    @staticmethod
    def by_id(id: int, team: typing.Union[TEAM, None] = None) -> BASE_MARKER:
        """
        Get a marker object from an id

        Marker IDs are read as April tags, so use an online 6x6 April tag
        generator to test values, such as:
        https://chaitanyantr.github.io/apriltag (remember to set to tag36h11)

        In 2027 low marker IDs are in-game objects:
            0-3: Quaffles (one per team colour)
            4:   The Snitch

        Higher marker IDs (100+) are part of the arena. These markers are the
        arena walls, grouped per team corner:
            100-102, 121-123: Red corner
            103-108:         Yellow corner
            109-114:         Green corner
            115-120:         Blue corner
        """

        ARENA_WALL_LOWER_ID = 100
        if id >= ARENA_WALL_LOWER_ID:
            # 100-102, 121-123: Red corner
            # 103-108:         Yellow corner
            # 109-114:         Green corner
            # 115-120:         Blue corner
            if id <= 102 or id >= 121:
                owner = TEAM.T0
            elif id <= 108:
                owner = TEAM.T1
            elif id <= 114:
                owner = TEAM.T2
            else:
                owner = TEAM.T3
            return ARENA_MARKER(id, owner)

        if id == 4:
            return SNITCH_MARKER(id)

        if 0 <= id <= 3:
            return QUAFFLE_MARKER(id, TEAM[f"T{id}"])

        # Unknown game object: label it as a quaffle without a colour.
        return QUAFFLE_MARKER(id, TEAM.ARENA)