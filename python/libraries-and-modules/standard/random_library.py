import random

# Class to roll a dice:
class Dice():
    def __init__(self, sides, colour):
        self.sides = sides
        self.color = colour

    def __str__(self):
        resultstr = (f"{self.sides}-sided {self.color} dice".lower())
        return resultstr
    
    def roll(self):
        die = random.randint(1, self.sides)
        return die