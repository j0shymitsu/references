from enum import Enum

class Button:
    def __init__(self):
        self.color = Enum('Colour', ['RED', 'GREEN', 'BLUE'])

btn = Button()

print(btn.colour.RED)
print(btn.colur.TEAL)   # error 