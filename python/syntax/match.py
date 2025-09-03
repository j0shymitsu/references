# (basically a switch statement)

from enum import Enum

Colour = Enum("Colour", ["RED", "GREEN", "BLUE"])

def get_hex(colour):
    match colour:
        case Colour.RED:
            return "#FF0000"
        case Colour.GREEN:
            return "#00FF00"
        case Colour.BLUE:
            return "#0000FF"
        
        # default case (invalid)
        case _:
            return "#FFFFFF"