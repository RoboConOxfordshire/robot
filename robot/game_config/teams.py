import enum

"""
This defines each team, and a corresponding Tx value for the team (x is the
team index). Make sure that the value of the Tx matches its team, and is
unique - this year Quaffles are coloured by team, so T0..T3 line up with the
Red/Yellow/Green/Blue Quaffles (AprilTags 0..3).
"""
class TEAM(enum.Enum):
    RED = "Red (T0)"  # This matches T0, for example.
    YELLOW = "Yellow (T1)"
    GREEN = "Green (T2)"
    BLUE = "Blue (T3)"
    ARENA = "Arena"
    # There is no T value for ARENA, so there is no way that the assignment of
    # team to a marker can accidentally assign ARENA if the logic goes wrong.

    T0 = "Red (T0)"
    T1 = "Yellow (T1)"
    T2 = "Green (T2)"
    T3 = "Blue (T3)"
