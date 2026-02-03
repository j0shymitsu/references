# Standard if-else block
def choose_parser(file_extension):
    if file_extension.lower() in ("markdown", "md"):
        return "markdown"
    else:
        return "plaintext"
    
# Ternary
def ternary_parser(file_extension):
        return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"