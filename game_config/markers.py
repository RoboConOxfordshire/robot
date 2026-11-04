import enum
import typing

from .teams import TEAM


class MARKER_TYPE(enum.Enum):
    ARENA = enum.auto()     # These are the wall markers
    QUAFFLE = enum.auto()   # this year's game object markers
    SNITCH = enum.auto()


class BASE_MARKER:
    """Base marker class that holds id, type, owning team and size."""
    def __init__(self, mid: int, mtype: MARKER_TYPE):
        self.id = mid
        self.type = mtype
        self.owning_team: typing.Union[TEAM, None] = None
        # sizes are in metres
        self.size = 0.2 if mtype == MARKER_TYPE.ARENA else 0.1

    def __repr__(self) -> str:
        return f"<Marker id={self.id} type={self.type} team={self.owning_team}>"


class ARENA_MARKER:
    """Represents an arena wall marker with a team owner."""
    def __init__(self, mid: int, owner: TEAM) -> None:
        self.id = mid
        self.type = MARKER_TYPE.ARENA
        self.owning_team = owner

    def __repr__(self) -> str:
        return f"<ARENA_MARKER id={self.id} team={self.owning_team}>"


class MARKER:
    """ convenience class to get a marker from an id """

    @staticmethod
    def by_id(id: int, team: typing.Union[TEAM, None] = None) -> typing.Union[ARENA_MARKER, None]:
        """
        Get a marker definition for an AprilTag ID.

        ID ranges (inclusive):
            • 0 – 3   : Quaffle (team‑coloured)
            • 4       : Snitch (gold)
            • 100 – 123 : Arena wall markers (team‑coloured)

        The *team* parameter is used for Quaffles and arena walls; if omitted
        the function looks up the team from the global *TEAM* enum based on the ID.
        """
        # ---- Quaffles (0‑3) -------------------------------------------------
        if 0 <= id <= 3:
            if team is None:
                # map ID → team: 0→RED, 1→YELLOW, 2→GREEN, 3→BLUE
                team = [TEAM.RED, TEAM.YELLOW, TEAM.GREEN, TEAM.BLUE][id]
            # return a simple marker object; we just return a dict-like info
            return {"id": id, "type": "Quaffle", "team": team}

        # ---- Snitch --------------------------------------------------------
        if id == 4:
            return {"id": id, "type": "Snitch", "team": team if team else TEAM.RED}

        # ---- Arena walls (100‑123) -----------------------------------------
        if 100 <= id <= 123:
            # team assignment from the rules PDF:
            #   100‑102 and 121‑123 → RED
            #   103‑108           → YELLOW
            #   109‑114           → GREEN
            #   115‑120           → BLUE
            if id <= 102 or id >= 121:
                owner = TEAM.RED
            elif id <= 108:
                owner = TEAM.YELLOW
            elif id <= 114:
                owner = TEAM.GREEN
            else:
                owner = TEAM.BLUE
            return ARENA_MARKER(id, owner)

        # ---- unknown --------------------------------------------------------
        raise ValueError(f"AprilTag ID {id} is out of the 2027 Quidditch range")

    @staticmethod
    def bounding_box_color(marker) -> typing.Tuple[int, int, int]:
        """Return an RGB tuple for drawing the marker border."""
        if marker.type == MARKER_TYPE.ARENA or marker.type == "Quaffle":
            # pick the team colour from above
            if marker.owning_team:
                return MARKER.team_marker_colors[marker.owning_team]
            return (255, 255, 255)  # white fallback
        elif marker.type == "Snitch":
            return (215, 128, 0)  # orange
        else:
            return (55, 255, 255)  # white-ish

    # team colour lookup (same as in teams.py)
    team_marker_colors: typing.ClassVar[typing.Dict[TEAM, typing.Tuple[int, int, int]]] = {
        TEAM.RED: (255, 64, 0),
        TEAM.YELLOW: (255, 255, 32),
        TEAM.GREEN: (50, 255, 0),
        TEAM.BLUE: (0, 100, 255),
    }