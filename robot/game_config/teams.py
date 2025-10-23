import enum

"""
This defines each team, and a corresponding Tx value for the team (x is the team index). Make sure that 
the value of the Tx matches its team, and is unique.
"""
class TEAM(enum.Enum): 
    RED = "Mocking Jay (Red)" # This matches T0, for example.
    YELLOW = "Haymitch (Yellow)"
    GREEN = "Finnick (Green)"
    BLUE = "Snow (Blue)"
    ARENA = "Arena" 
    # There is no T value for ARENA, so there is no way that the assignment of team to a marker can accidentally assign ARENA if the logic goes wrong.

    T0 = "Mocking Jay (Red)"
    T1 = "Haymitch (Yellow)"
    T2 = "Finnick (Green)"
    T3 = "Snow (Blue)"

