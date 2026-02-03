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
        
###

class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4

def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            content = content.replace("# ", "<h1>")
            content += "</h1>"
            return content
        case(DocFormat.TXT, DocFormat.PDF):
            return "[PDF] " + content + " [PDF]" 
        case(DocFormat.HTML, DocFormat.MD):
            content = content.replace("<h1>", "# ")
            content = content.replace("</h1>", "")
            return content 
        case _:
            raise Exception("invalid type")